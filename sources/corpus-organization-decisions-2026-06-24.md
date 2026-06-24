# Corpus Organization Decisions (2026-06-24)

Record of merge/split/reorder analysis for the goal pass. Preserves audit trail for structural changes.

## Strategic reading order (23 files, logical 00–22)

**Decision:** Renumber to measurement-first path, not historical DOCX import order.

| Range | Rationale |
| --- | --- |
| 00–02 | Harness validity and organism core before any strategy imports |
| 03 | **Merged** RSI literature digest + organism framework (former Ch03+Ch04) |
| 05–07, 07b | Agent law, gap closure (split), backlog |
| 08–12 | Five new chapters closing fleet-stats, network, LLM runtime, identity, OSS funding gaps |
| 13–18 | Platform depth (kernel, GPU, AI tuning, security, firmware, local agent) |
| 19–22 | Historical DOCX imports last — living layers required before citing import body |

**Not merged:** Ch13 (kernel) and Ch14 (GPU) — distinct hardware layers; cross-linked via Ch00 harness and integration notes.

**Not merged:** Ch19 (strategy) and Ch20 (market) — strategy moat vs market/TEE context; living layers reconcile disproven import passages separately.

## Ch03 + Ch04 RSI merge (executed 2026-06-24)

**Previous state:** Separate files — paper digest (Ch03) and organism theory synthesis (Ch04).

| Dimension | Former Ch03 | Former Ch04 |
| --- | --- | --- |
| Source | Curated paper/system digest | Uploaded intake `Software Organisms_ Self-Improvement Research.md` |
| Structure | Paper-by-paper lessons, 25-paper cross-links | Definitions, ALife/cybernetics framework, organism taxonomy, failure modes |
| Overlap | Verifier/fitness framing, Goodhart risk | Same themes at theory depth |

**Decision: MERGED** into `chapters/03-rsi-literature-and-organism-synthesis.md`:

- **Part A** — peer-reviewed literature digest (preserved intake)
- **Part B** — software organism critical synthesis (preserved intake)
- Ch04 file deleted; both intake blocks retained in one navigation entry
- Inline reinforcement notes merge in Part A executive summary

## Ch07 split (executed 2026-06-24)

**Previous state:** Single file `07-main-repo-gap-closure-and-research-backlog.md` covered both gap-closure status and research backlog.

**Decision: SPLIT** to keep 23 chapter files after Ch03+Ch04 merge:

| File | Content |
| --- | --- |
| `07-main-repo-gap-closure.md` | Gaps 1–5 status vs main repo |
| `07b-research-backlog-and-pipeline.md` | What Should Be Added Next + pipeline experimental lift |

## Ch07 tokenomics vs Ch02 economics

**Decision:** No merge. Ch21 (tokenomics DOCX) superseded for product by Ch02; Ch21 kept as DePIN comparison. Documented in Ch02/Ch21 living layers and Ch12 OSS chapter.

## Five new chapters (08–12)

Identified from `RESEARCH_PIPELINE.md` gaps and Ch07 backlog — not covered by merges:

| Ch | Gap closed |
| --- | --- |
| 08 | Population confirmation statistics (Ch01 N-rule + Ch00 noise floor) |
| 09 | Network transport validity (loopback vs real-path) |
| 10 | Local LLM runtime architecture (Ch05 daemon/shell + Ollama path) |
| 11 | Hardware identity / anti-spoofing for fleet independence |
| 12 | OSS funding vs sensor-gated BTC (complements Ch02) |

## Reinforcement pattern (two classes)

| Class | Chapters | Method |
| --- | --- | --- |
| Native (00–12, 17, 07b) | Living layer + reinforced research + **Corpus inline** in body | `sources/reinforcement-manifest.json` + manual anchors |
| DOCX import (13–16, 18–22) | Above + integration notes + **inline** after key import paragraphs | Preserves import text; targeted narrowing in body |

See `REINFORCEMENT_LOG.md` for per-chapter audit rows.