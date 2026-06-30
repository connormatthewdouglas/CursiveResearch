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

# Rebuild only if the index is missing/stale.
python tools/corpus_retrieval.py index --if-stale

# Check whether the index matches current Markdown files.
python tools/corpus_retrieval.py status
python tools/corpus_retrieval.py status --changed-only

# Search for cited passages. If a direct non-raw search misses, the tool
# automatically tries lexical variants and a rare-anchor fallback.
python tools/corpus_retrieval.py search "measurement daemon shell truth" --limit 5
python tools/corpus_retrieval.py search "founder risk transition" --match all --explain

# Narrow by path prefix or heading substring.
python tools/corpus_retrieval.py search "GPU isolation" --path chapters/ --heading security

# Show a full passage from a search result.
python tools/corpus_retrieval.py show <chunk_id>

# Machine-readable output for agents.
python tools/corpus_retrieval.py search "BBR fairness retransmit" --json

# Built-in retrieval-quality spot check.
python tools/corpus_retrieval.py audit
```

The generated database lives at:

```text
.cursive-research-rag/index.sqlite
```

That directory is ignored by git. Rebuild it locally instead of committing it.

## Required habit when adding corpus content

After adding or materially editing Markdown content:

1. Run `python tools/corpus_retrieval.py index --if-stale`.
2. Run `python tools/corpus_retrieval.py status --changed-only` and confirm it is up to date.
3. Run at least one representative search for the claim/topic you added.
4. Use the returned `path:start-end` citation when summarizing or applying the
   research elsewhere.
5. Commit only source files, docs, and tool/test changes — not the generated DB.

This makes the retrieval layer grow with the corpus without creating a second
copy of the corpus.

## Query cookbook

Good retrieval queries are short, source-specific, and use the language the
corpus uses. Prefer nouns and trust-boundary terms over full natural-language
questions.

```bash
# Measurement daemon / shell boundary.
python tools/corpus_retrieval.py search "measurement daemon shell truth" --match all --path chapters/

# Shared GPU isolation caveat.
python tools/corpus_retrieval.py search "GPU isolation shared accelerators" --match all --path chapters/ --path VALIDATION.md

# Network caveat: BBR fairness and retransmit risk.
python tools/corpus_retrieval.py search "BBR fairness retransmit" --match all --path validation/notes/

# Current economics authority.
python tools/corpus_retrieval.py search "Layer 5 economics" --match all --path chapters/02-bitcoin-native

# Founder-risk / bootstrapping transition.
python tools/corpus_retrieval.py search "founder risk transition" --match all --explain

# Contributor privacy and telemetry governance.
python tools/corpus_retrieval.py search "contributor privacy telemetry governance" --match all --path chapters/24-contributor
```

If a direct query misses, the CLI does not stop at brittle keywords: default
`--expand auto` tries lexical variants, singular/plural forms, common suffix
variants, and then relaxes to the rarest surviving anchor term. Use `--explain`
to see which fallback fired. Use `--expand never` when you need strict lexical
proof that the exact query terms co-occur.

This is still local FTS, not magic semantic search. If the fallback finds the
right concept but the corpus lacks the phrase humans naturally ask for, improve
the chapter heading/source wording so the next agent can find it even faster.

## Search modes and filters

Default search uses `--match any`, which is broad and useful for discovery.
Use stricter matching when needed:

```bash
python tools/corpus_retrieval.py search "shell organism truth" --match all
python tools/corpus_retrieval.py search '"BBR" NEAR "fairness"' --match raw
python tools/corpus_retrieval.py search "founder risk transition" --match all --expand never
```

Raw mode sends the query directly to SQLite FTS5. Use it only when you know FTS5
query syntax. `--expand never` keeps the normal parser but disables fallback.

Filters are repeatable and combine with the FTS query:

```bash
# Any result under chapters/ or VALIDATION.md.
python tools/corpus_retrieval.py search "shared GPU isolation" --path chapters/ --path VALIDATION.md

# Only headings containing a substring.
python tools/corpus_retrieval.py search "truth" --heading "Relationship Between Shell and Daemon"

# Combine filters.
python tools/corpus_retrieval.py search "BBR retransmit" --path validation/notes/ --heading caveat
```

`--path` is a case-insensitive path-prefix filter, not a regex. `--heading` is a
case-insensitive heading substring filter.

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

## Retrieval-quality audit

Run the built-in audit after retrieval changes or before claiming the tool is in
good shape:

```bash
python tools/corpus_retrieval.py audit
python tools/corpus_retrieval.py audit --json
```

The audit is intentionally small. It checks that known high-value queries can
recover their expected source areas: measurement daemon/shell boundary, shared
GPU isolation, BBR fairness caveat, Layer 5 economics, contributor privacy /
telemetry governance, and the founder-risk fallback. It is not a semantic
benchmark. It is a smoke alarm for obvious retrieval drift.

## Verification

Run the retrieval smoke test:

```bash
python tools/corpus_retrieval.py self-test
```

For repo-level verification after changing retrieval code or docs, run:

```bash
python -m py_compile tools/corpus_retrieval.py
python -m unittest tests.test_corpus_retrieval -v
python tools/corpus_retrieval.py index --if-stale
python tools/corpus_retrieval.py status --strict
python tools/corpus_retrieval.py audit
powershell.exe -NoProfile -ExecutionPolicy Bypass -File tools/run-verification.ps1
```

`tools/run-verification.ps1` now includes the retrieval self-test, focused
retrieval unittests, index/status check, and retrieval audit as part of the
canonical corpus verification path.

## Current scope

Version 0.1 is FTS-only by design. Do not add embeddings, a vector database, or a
conversational RAG app until the simple retrieval spine proves insufficient.
