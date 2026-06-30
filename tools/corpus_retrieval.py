#!/usr/bin/env python
"""Repo-native retrieval for the CursiveResearch corpus.

This is intentionally boring infrastructure: local SQLite + FTS5, no network,
no embeddings, no generated index committed to git. It gives humans and agents a
stable way to retrieve source passages with file/heading/line citations before
making research-backed claims.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sqlite3
import subprocess
import sys
import tempfile
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable, Sequence

SCHEMA_VERSION = "1"
DEFAULT_INDEX_DIR = ".cursive-research-rag"
DEFAULT_INDEX_FILE = "index.sqlite"
EXCLUDED_DIRS = {
    ".git",
    ".cursive-research-rag",
    ".mypy_cache",
    ".pytest_cache",
    ".ruff_cache",
    ".venv",
    "__pycache__",
    "node_modules",
    "venv",
}
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
TOKEN_RE = re.compile(r"[A-Za-z0-9_][A-Za-z0-9_./:+-]*")
FENCE_MARKERS = ("```", "~~~")


@dataclass(frozen=True)
class Section:
    path: str
    heading: str
    level: int
    start_line: int
    end_line: int
    lines: tuple[str, ...]


@dataclass(frozen=True)
class Chunk:
    path: str
    heading: str
    level: int
    start_line: int
    end_line: int
    text: str
    sha256: str

    @property
    def citation(self) -> str:
        return f"{self.path}:{self.start_line}-{self.end_line}"


@dataclass(frozen=True)
class SearchResult:
    id: int
    path: str
    heading: str
    start_line: int
    end_line: int
    snippet: str
    score: float

    @property
    def citation(self) -> str:
        return f"{self.path}:{self.start_line}-{self.end_line}"

    def to_dict(self) -> dict[str, object]:
        data = asdict(self)
        data["citation"] = self.citation
        return data


def repo_root_from_script() -> Path:
    return Path(__file__).resolve().parents[1]


def default_index_path(repo_root: Path) -> Path:
    return repo_root / DEFAULT_INDEX_DIR / DEFAULT_INDEX_FILE


def relpath(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8", errors="replace")).hexdigest()


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def iter_markdown_files(repo_root: Path) -> list[Path]:
    """Return Markdown files that belong to the working corpus.

    In a git checkout, respect the repository's ignore rules while still
    indexing newly-created, not-yet-staged Markdown files. This keeps local
    generated caches and ignored agent-only files out of retrieval, while letting
    the index grow during normal corpus-editing work before commit.
    """

    git_files = git_list_markdown_files(repo_root)
    if git_files is not None:
        return git_files

    files: list[Path] = []
    for path in repo_root.rglob("*.md"):
        rel_parts = path.relative_to(repo_root).parts
        if any(part in EXCLUDED_DIRS for part in rel_parts):
            continue
        if not path.is_file():
            continue
        files.append(path)
    return sorted(files, key=lambda p: relpath(p, repo_root).lower())


def git_list_markdown_files(repo_root: Path) -> list[Path] | None:
    try:
        proc = subprocess.run(
            ["git", "-C", str(repo_root), "ls-files", "--cached", "--others", "--exclude-standard", "--", "*.md"],
            check=False,
            text=True,
            capture_output=True,
        )
    except OSError:
        return None
    if proc.returncode != 0:
        return None
    files: list[Path] = []
    for line in proc.stdout.splitlines():
        if not line.strip():
            continue
        path = repo_root / line.strip()
        if path.is_file():
            files.append(path)
    return sorted(files, key=lambda p: relpath(p, repo_root).lower())


def clean_heading(raw: str) -> str:
    title = raw.strip()
    title = re.sub(r"\s+#+$", "", title).strip()
    return title or "(untitled)"


def split_markdown_sections(path: Path, repo_root: Path) -> list[Section]:
    relative = relpath(path, repo_root)
    text = read_text(path)
    lines = text.splitlines()
    if not lines:
        return []

    sections: list[Section] = []
    stack: list[tuple[int, str]] = []
    current_lines: list[str] = []
    current_start = 1
    current_heading = Path(relative).name
    current_level = 0
    fence: str | None = None

    def flush(end_line: int) -> None:
        nonlocal current_lines, current_start, current_heading, current_level
        if not current_lines:
            return
        body = "\n".join(current_lines).strip()
        if body:
            sections.append(
                Section(
                    path=relative,
                    heading=current_heading,
                    level=current_level,
                    start_line=current_start,
                    end_line=end_line,
                    lines=tuple(current_lines),
                )
            )
        current_lines = []

    for index, line in enumerate(lines, start=1):
        stripped = line.lstrip()
        fence_marker = next((m for m in FENCE_MARKERS if stripped.startswith(m)), None)
        if fence_marker:
            if fence is None:
                fence = fence_marker
            elif fence == fence_marker:
                fence = None

        match = None if fence else HEADING_RE.match(line)
        if match:
            flush(index - 1)
            level = len(match.group(1))
            title = clean_heading(match.group(2))
            while stack and stack[-1][0] >= level:
                stack.pop()
            stack.append((level, title))
            current_heading = " > ".join(title for _, title in stack)
            current_level = level
            current_start = index
            current_lines = [line]
        else:
            if not current_lines:
                current_start = index
            current_lines.append(line)

    flush(len(lines))
    return sections


def chunk_section(section: Section, max_chars: int = 4500) -> list[Chunk]:
    chunks: list[Chunk] = []
    buffer: list[str] = []
    start_line = section.start_line
    char_count = 0

    def flush(end_line: int) -> None:
        nonlocal buffer, start_line, char_count
        text = "\n".join(buffer).strip()
        if text:
            chunks.append(
                Chunk(
                    path=section.path,
                    heading=section.heading,
                    level=section.level,
                    start_line=start_line,
                    end_line=end_line,
                    text=text,
                    sha256=sha256_text(text),
                )
            )
        buffer = []
        char_count = 0

    for offset, line in enumerate(section.lines):
        absolute_line = section.start_line + offset
        line_len = len(line) + 1
        if buffer and char_count + line_len > max_chars:
            flush(absolute_line - 1)
            start_line = absolute_line
        buffer.append(line)
        char_count += line_len

    if buffer:
        flush(section.end_line)
    return chunks


def build_chunks(repo_root: Path, max_chars: int = 4500) -> tuple[list[Chunk], list[dict[str, object]]]:
    chunks: list[Chunk] = []
    documents: list[dict[str, object]] = []
    for path in iter_markdown_files(repo_root):
        text = read_text(path)
        stat = path.stat()
        relative = relpath(path, repo_root)
        documents.append(
            {
                "path": relative,
                "sha256": sha256_text(text),
                "size": stat.st_size,
                "mtime_ns": stat.st_mtime_ns,
            }
        )
        for section in split_markdown_sections(path, repo_root):
            chunks.extend(chunk_section(section, max_chars=max_chars))
    return chunks, documents


def connect(index_path: Path) -> sqlite3.Connection:
    con = sqlite3.connect(index_path)
    con.row_factory = sqlite3.Row
    return con


def reset_schema(con: sqlite3.Connection) -> None:
    con.executescript(
        """
        DROP TABLE IF EXISTS metadata;
        DROP TABLE IF EXISTS documents;
        DROP TABLE IF EXISTS chunks;
        DROP TABLE IF EXISTS chunk_fts;

        CREATE TABLE metadata (
            key TEXT PRIMARY KEY,
            value TEXT NOT NULL
        );

        CREATE TABLE documents (
            path TEXT PRIMARY KEY,
            sha256 TEXT NOT NULL,
            size INTEGER NOT NULL,
            mtime_ns INTEGER NOT NULL
        );

        CREATE TABLE chunks (
            id INTEGER PRIMARY KEY,
            path TEXT NOT NULL,
            heading TEXT NOT NULL,
            level INTEGER NOT NULL,
            start_line INTEGER NOT NULL,
            end_line INTEGER NOT NULL,
            text TEXT NOT NULL,
            sha256 TEXT NOT NULL
        );

        CREATE VIRTUAL TABLE chunk_fts USING fts5(
            path UNINDEXED,
            heading,
            text,
            tokenize = 'unicode61'
        );
        """
    )


def build_index(repo_root: Path, index_path: Path, max_chars: int = 4500) -> dict[str, object]:
    repo_root = repo_root.resolve()
    index_path = index_path.resolve()
    index_path.parent.mkdir(parents=True, exist_ok=True)
    chunks, documents = build_chunks(repo_root, max_chars=max_chars)

    con = connect(index_path)
    try:
        reset_schema(con)
        con.executemany(
            "INSERT INTO documents(path, sha256, size, mtime_ns) VALUES(:path, :sha256, :size, :mtime_ns)",
            documents,
        )
        for chunk in chunks:
            cur = con.execute(
                """
                INSERT INTO chunks(path, heading, level, start_line, end_line, text, sha256)
                VALUES(?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    chunk.path,
                    chunk.heading,
                    chunk.level,
                    chunk.start_line,
                    chunk.end_line,
                    chunk.text,
                    chunk.sha256,
                ),
            )
            chunk_id = cur.lastrowid
            con.execute(
                "INSERT INTO chunk_fts(rowid, path, heading, text) VALUES(?, ?, ?, ?)",
                (chunk_id, chunk.path, chunk.heading, chunk.text),
            )
        con.executemany(
            "INSERT INTO metadata(key, value) VALUES(?, ?)",
            [
                ("schema_version", SCHEMA_VERSION),
                ("repo_root", str(repo_root)),
                ("document_count", str(len(documents))),
                ("chunk_count", str(len(chunks))),
            ],
        )
        con.commit()
    finally:
        con.close()

    return {
        "index": str(index_path),
        "repo_root": str(repo_root),
        "documents": len(documents),
        "chunks": len(chunks),
        "schema_version": SCHEMA_VERSION,
    }


def quote_fts_token(token: str) -> str:
    return '"' + token.replace('"', '""') + '"'


def build_match_query(query: str, mode: str) -> str:
    if mode == "raw":
        return query
    tokens = TOKEN_RE.findall(query)
    if not tokens:
        raise ValueError("query has no searchable tokens")
    quoted = [quote_fts_token(token) for token in tokens]
    if mode == "all":
        return " ".join(quoted)
    if mode == "any":
        return " OR ".join(quoted)
    raise ValueError(f"unknown match mode: {mode}")


def search_index(index_path: Path, query: str, limit: int = 10, mode: str = "any") -> list[SearchResult]:
    if not index_path.exists():
        raise FileNotFoundError(f"index not found: {index_path}; run `python tools/corpus_retrieval.py index`")
    match_query = build_match_query(query, mode)
    con = connect(index_path)
    try:
        rows = con.execute(
            """
            SELECT
                c.id,
                c.path,
                c.heading,
                c.start_line,
                c.end_line,
                snippet(chunk_fts, 2, '[', ']', ' ... ', 28) AS snippet,
                bm25(chunk_fts) AS score
            FROM chunk_fts
            JOIN chunks c ON c.id = chunk_fts.rowid
            WHERE chunk_fts MATCH ?
            ORDER BY score ASC, c.path ASC, c.start_line ASC
            LIMIT ?
            """,
            (match_query, limit),
        ).fetchall()
    finally:
        con.close()
    return [SearchResult(**dict(row)) for row in rows]


def get_chunk(index_path: Path, chunk_id: int) -> dict[str, object]:
    if not index_path.exists():
        raise FileNotFoundError(f"index not found: {index_path}")
    con = connect(index_path)
    try:
        row = con.execute(
            "SELECT id, path, heading, level, start_line, end_line, text, sha256 FROM chunks WHERE id = ?",
            (chunk_id,),
        ).fetchone()
    finally:
        con.close()
    if row is None:
        raise KeyError(f"chunk not found: {chunk_id}")
    data = dict(row)
    data["citation"] = f"{data['path']}:{data['start_line']}-{data['end_line']}"
    return data


def load_index_documents(index_path: Path) -> dict[str, str]:
    if not index_path.exists():
        return {}
    con = connect(index_path)
    try:
        rows = con.execute("SELECT path, sha256 FROM documents").fetchall()
    finally:
        con.close()
    return {row["path"]: row["sha256"] for row in rows}


def get_metadata(index_path: Path) -> dict[str, str]:
    if not index_path.exists():
        return {}
    con = connect(index_path)
    try:
        rows = con.execute("SELECT key, value FROM metadata").fetchall()
    except sqlite3.Error:
        return {}
    finally:
        con.close()
    return {row["key"]: row["value"] for row in rows}


def corpus_status(repo_root: Path, index_path: Path) -> dict[str, object]:
    current = {}
    for path in iter_markdown_files(repo_root):
        current[relpath(path, repo_root)] = sha256_text(read_text(path))
    indexed = load_index_documents(index_path)
    metadata = get_metadata(index_path)
    stale = sorted(path for path, digest in current.items() if indexed.get(path) not in (None, digest))
    new = sorted(path for path in current if path not in indexed)
    missing = sorted(path for path in indexed if path not in current)
    return {
        "index": str(index_path),
        "exists": index_path.exists(),
        "schema_version": metadata.get("schema_version"),
        "documents_indexed": int(metadata.get("document_count", "0") or 0),
        "chunks_indexed": int(metadata.get("chunk_count", "0") or 0),
        "documents_current": len(current),
        "new": new,
        "stale": stale,
        "missing": missing,
        "up_to_date": index_path.exists() and not new and not stale and not missing,
    }


def print_json(data: object) -> None:
    print(json.dumps(data, indent=2, ensure_ascii=False, sort_keys=True))


def print_search_results(results: Sequence[SearchResult]) -> None:
    if not results:
        print("No matches.")
        return
    for result in results:
        print(f"[{result.id}] {result.citation}")
        print(f"Heading: {result.heading}")
        print(result.snippet.replace("\n", " "))
        print()


def print_status(status: dict[str, object]) -> None:
    print(f"Index: {status['index']}")
    print(f"Exists: {status['exists']}")
    print(f"Documents: indexed={status['documents_indexed']} current={status['documents_current']}")
    print(f"Chunks: {status['chunks_indexed']}")
    print(f"Up to date: {status['up_to_date']}")
    for key in ("new", "stale", "missing"):
        values = status[key]
        if values:
            print(f"{key.capitalize()} ({len(values)}):")
            for value in values[:20]:
                print(f"  - {value}")
            if len(values) > 20:
                print(f"  ... {len(values) - 20} more")


def add_common_args(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--repo-root", type=Path, default=repo_root_from_script(), help="CursiveResearch repo root")
    parser.add_argument("--index", type=Path, default=None, help="Index path; defaults to .cursive-research-rag/index.sqlite")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON")


def resolved_paths(args: argparse.Namespace) -> tuple[Path, Path]:
    repo_root = args.repo_root.resolve()
    index_path = args.index.resolve() if args.index else default_index_path(repo_root).resolve()
    return repo_root, index_path


def run_self_test() -> dict[str, object]:
    with tempfile.TemporaryDirectory(prefix="cursive-rag-selftest-") as tmp:
        root = Path(tmp)
        (root / "chapters").mkdir()
        (root / "README.md").write_text("# Mini Corpus\n\nA retrieval smoke test.\n", encoding="utf-8")
        (root / "chapters" / "01-measurement.md").write_text(
            "# Measurement Trust\n\n"
            "The measurement daemon owns organism truth.\n\n"
            "## Natural-language shell boundary\n\n"
            "The shell may read measurement state but must not write organism truth.\n",
            encoding="utf-8",
        )
        index_path = root / DEFAULT_INDEX_DIR / DEFAULT_INDEX_FILE
        summary = build_index(root, index_path)
        results = search_index(index_path, "shell organism truth", limit=5, mode="all")
        if not results:
            raise AssertionError("self-test search returned no results")
        if "shell" not in results[0].snippet.lower():
            raise AssertionError(f"self-test result did not mention shell: {results[0].snippet}")
        chunk = get_chunk(index_path, results[0].id)
        return {"summary": summary, "top_result": results[0].to_dict(), "chunk_citation": chunk["citation"]}


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="CursiveResearch local corpus retrieval")
    sub = parser.add_subparsers(dest="command", required=True)

    p_index = sub.add_parser("index", help="Rebuild the local SQLite FTS index")
    add_common_args(p_index)
    p_index.add_argument("--max-chars", type=int, default=4500, help="Maximum chunk size before splitting long sections")

    p_status = sub.add_parser("status", help="Check whether the local index is current")
    add_common_args(p_status)
    p_status.add_argument("--strict", action="store_true", help="Exit non-zero when index is missing or stale")

    p_search = sub.add_parser("search", help="Search indexed corpus passages")
    add_common_args(p_search)
    p_search.add_argument("query", help="Search query")
    p_search.add_argument("--limit", type=int, default=10)
    p_search.add_argument("--match", choices=("any", "all", "raw"), default="any", help="FTS matching mode")

    p_show = sub.add_parser("show", help="Show a retrieved chunk by id")
    add_common_args(p_show)
    p_show.add_argument("id", type=int, help="Chunk id from search output")

    p_self = sub.add_parser("self-test", help="Run a temp-corpus smoke test")
    p_self.add_argument("--json", action="store_true")

    args = parser.parse_args(argv)

    try:
        if args.command == "self-test":
            result = run_self_test()
            if args.json:
                print_json(result)
            else:
                print("CORPUS RETRIEVAL SELF-TEST: pass")
                print(f"Indexed {result['summary']['documents']} documents / {result['summary']['chunks']} chunks")
                print(f"Top citation: {result['top_result']['citation']}")
            return 0

        repo_root, index_path = resolved_paths(args)
        if args.command == "index":
            summary = build_index(repo_root, index_path, max_chars=args.max_chars)
            if args.json:
                print_json(summary)
            else:
                print(f"Indexed {summary['documents']} documents into {summary['chunks']} chunks")
                print(f"Index: {summary['index']}")
            return 0

        if args.command == "status":
            status = corpus_status(repo_root, index_path)
            if args.json:
                print_json(status)
            else:
                print_status(status)
            return 1 if args.strict and not status["up_to_date"] else 0

        if args.command == "search":
            results = search_index(index_path, args.query, limit=args.limit, mode=args.match)
            if args.json:
                print_json([result.to_dict() for result in results])
            else:
                print_search_results(results)
            return 0

        if args.command == "show":
            chunk = get_chunk(index_path, args.id)
            if args.json:
                print_json(chunk)
            else:
                print(f"[{chunk['id']}] {chunk['citation']}")
                print(f"Heading: {chunk['heading']}")
                print()
                print(chunk["text"])
            return 0

    except (FileNotFoundError, KeyError, ValueError, sqlite3.Error, AssertionError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    return 2


if __name__ == "__main__":
    raise SystemExit(main())
