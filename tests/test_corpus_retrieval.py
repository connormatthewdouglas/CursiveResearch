from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "tools" / "corpus_retrieval.py"
spec = importlib.util.spec_from_file_location("corpus_retrieval", MODULE_PATH)
corpus_retrieval = importlib.util.module_from_spec(spec)
sys.modules["corpus_retrieval"] = corpus_retrieval
assert spec.loader is not None
spec.loader.exec_module(corpus_retrieval)


def write_sample_repo(root: Path) -> None:
    (root / "chapters").mkdir(parents=True)
    (root / "sources").mkdir(parents=True)
    (root / ".cursive-research-rag").mkdir(parents=True)
    (root / "README.md").write_text("# Sample Corpus\n\nIntro text.\n", encoding="utf-8")
    (root / "chapters" / "01-measurement.md").write_text(
        "# Measurement Trust\n\n"
        "The measurement daemon owns organism truth.\n\n"
        "## Natural-language shell boundary\n\n"
        "The shell may read measurement state but must not write organism truth.\n",
        encoding="utf-8",
    )
    (root / "sources" / "source-register.md").write_text(
        "# Source Register\n\nBBR fairness and retransmit risk remain review flags.\n",
        encoding="utf-8",
    )
    (root / ".cursive-research-rag" / "ignored.md").write_text(
        "# Generated Cache\n\nThis should not be indexed.\n",
        encoding="utf-8",
    )


class CorpusRetrievalTests(unittest.TestCase):
    def test_index_search_show_and_status(self) -> None:
        with tempfile.TemporaryDirectory(prefix="corpus-retrieval-test-") as tmp:
            root = Path(tmp)
            write_sample_repo(root)
            index_path = root / ".cursive-research-rag" / "index.sqlite"

            summary = corpus_retrieval.build_index(root, index_path)
            self.assertEqual(summary["documents"], 3)
            self.assertGreaterEqual(summary["chunks"], 4)

            results = corpus_retrieval.search_index(index_path, "shell organism truth", limit=5, mode="all")
            self.assertTrue(results)
            self.assertEqual(results[0].path, "chapters/01-measurement.md")
            self.assertLessEqual(results[0].start_line, results[0].end_line)
            self.assertIn("shell", results[0].snippet.lower())

            chunk = corpus_retrieval.get_chunk(index_path, results[0].id)
            self.assertTrue(chunk["citation"].startswith("chapters/01-measurement.md:"))
            self.assertIn("must not write organism truth", chunk["text"])

            status = corpus_retrieval.corpus_status(root, index_path)
            self.assertTrue(status["up_to_date"])

            (root / "chapters" / "02-new.md").write_text("# New\n\nFresh research.\n", encoding="utf-8")
            status = corpus_retrieval.corpus_status(root, index_path)
            self.assertFalse(status["up_to_date"])
            self.assertEqual(status["new"], ["chapters/02-new.md"])

    def test_cli_json_search(self) -> None:
        with tempfile.TemporaryDirectory(prefix="corpus-retrieval-test-") as tmp:
            root = Path(tmp)
            write_sample_repo(root)
            index_path = root / ".cursive-research-rag" / "index.sqlite"
            subprocess.run(
                [sys.executable, str(MODULE_PATH), "index", "--repo-root", str(root), "--index", str(index_path), "--json"],
                check=True,
                text=True,
                capture_output=True,
            )
            proc = subprocess.run(
                [
                    sys.executable,
                    str(MODULE_PATH),
                    "search",
                    "BBR retransmit",
                    "--repo-root",
                    str(root),
                    "--index",
                    str(index_path),
                    "--json",
                ],
                check=True,
                text=True,
                capture_output=True,
            )
            results = json.loads(proc.stdout)
            self.assertTrue(results)
            self.assertTrue(results[0]["citation"].startswith("sources/source-register.md:"))

    def test_git_checkout_respects_ignore_rules_but_includes_new_markdown(self) -> None:
        with tempfile.TemporaryDirectory(prefix="corpus-retrieval-git-test-") as tmp:
            root = Path(tmp)
            subprocess.run(["git", "init"], cwd=root, check=True, text=True, capture_output=True)
            (root / ".gitignore").write_text("ignored.md\n", encoding="utf-8")
            (root / "README.md").write_text("# Tracked\n", encoding="utf-8")
            (root / "draft.md").write_text("# New untracked corpus note\n", encoding="utf-8")
            (root / "ignored.md").write_text("# Ignored local note\n", encoding="utf-8")
            subprocess.run(["git", "add", ".gitignore", "README.md"], cwd=root, check=True, text=True, capture_output=True)

            files = [path.relative_to(root).as_posix() for path in corpus_retrieval.iter_markdown_files(root)]
            self.assertEqual(files, ["draft.md", "README.md"])


if __name__ == "__main__":
    unittest.main()
