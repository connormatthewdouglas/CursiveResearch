# Corpus Retrieval

CursiveResearch includes a small local retrieval layer so humans and agents can
find source passages before making research-backed claims. It is intentionally
simple: SQLite FTS5, Markdown-section chunks, no network calls, no embeddings,
and no generated index committed to git.

## Why it exists

CursiveResearch is the grounding corpus for CursiveOS. Retrieval gives every
agent a repeatable way to ask:

- What does the corpus say about this claim?
- Which chapter or source constrains this implementation decision?
- What exact passage should be cited before changing CursiveOS?
- Did the new material I added become discoverable?

Use retrieval to find evidence. Do not treat a retrieved passage as validated by
itself; check `VALIDATION.md` for decision-impacting claim status.

## Quick start

From the repository root:

```bash
# Build or refresh the local index.
python tools/corpus_retrieval.py index

# Check whether the index matches current Markdown files.
python tools/corpus_retrieval.py status

# Search for cited passages.
python tools/corpus_retrieval.py search "measurement daemon shell truth" --limit 5

# Show a full passage from a search result.
python tools/corpus_retrieval.py show <chunk_id>

# Machine-readable output for agents.
python tools/corpus_retrieval.py search "BBR fairness retransmit" --json
```

The generated database lives at:

```text
.cursive-research-rag/index.sqlite
```

That directory is ignored by git. Rebuild it locally instead of committing it.

## Required habit when adding corpus content

After adding or materially editing Markdown content:

1. Run `python tools/corpus_retrieval.py index`.
2. Run `python tools/corpus_retrieval.py status` and confirm it is up to date.
3. Run at least one representative search for the claim/topic you added.
4. Use the returned `path:start-end` citation when summarizing or applying the
   research elsewhere.
5. Commit only source files, docs, and tool/test changes — not the generated DB.

This makes the retrieval layer grow with the corpus without creating a second
copy of the corpus.

## Search modes

Default search uses `--match any`, which is broad and useful for discovery.
Use stricter matching when needed:

```bash
python tools/corpus_retrieval.py search "shell organism truth" --match all
python tools/corpus_retrieval.py search '"BBR" NEAR "fairness"' --match raw
```

Raw mode sends the query directly to SQLite FTS5. Use it only when you know FTS5
query syntax.

## What gets indexed

In a git checkout, the indexer uses:

```bash
git ls-files --cached --others --exclude-standard -- '*.md'
```

That includes tracked Markdown plus new unignored Markdown, and it respects
`.gitignore` / `.git/info/exclude`. Fallback mode scans Markdown across the repo
while skipping generated/cache directories such as `.git/`,
`.cursive-research-rag/`, `.pytest_cache/`, virtualenvs, and `node_modules/`.

Each Markdown section becomes one or more chunks with:

- file path;
- heading path;
- start and end line;
- text;
- content hash.

Search results are designed to be cited as:

```text
chapters/09-network-transport-and-congestion-control.md:42-88
```

## Agent usage pattern

Before answering or changing CursiveOS from CursiveResearch evidence:

1. Search the corpus for the relevant topic.
2. Read the top passages with `show`.
3. Cross-check `VALIDATION.md` for confidence/status if the claim affects
   implementation, safety, spending, security, or product direction.
4. Cite the exact passage path/line range in your summary or handoff.
5. If retrieval misses a known source, improve the source/chapter wording or add
   metadata so future agents can find it.

## Verification

Run the retrieval smoke test:

```bash
python tools/corpus_retrieval.py self-test
```

For repo-level verification after changing retrieval code or docs, also run:

```bash
python -m py_compile tools/corpus_retrieval.py
python -m unittest tests.test_corpus_retrieval -v
powershell.exe -NoProfile -ExecutionPolicy Bypass -File tools/run-verification.ps1
```

## Current scope

Version 0.1 is FTS-only by design. Do not add embeddings, a vector database, or a
conversational RAG app until the simple retrieval spine proves insufficient.
