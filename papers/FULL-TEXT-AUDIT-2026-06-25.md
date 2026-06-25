# Cornerstone Full-Text Audit — 2026-06-25

Purpose: prevent CursiveResearch from becoming an agent-alignment corpus built on summaries-of-summaries. This audit records which current cornerstone paper folders have local full text, which rights-cleared gaps were repaired, and which cornerstone sources must remain citation/deep-extraction only under the current corpus storage rule.

Policy reference: `CORPUS_WORKFLOW.md` § Paper Storage Rule — full verbatim paper text is stored only when redistribution/copying is clearly permitted (for example CC BY/CC0/public domain/explicit permission). Otherwise the corpus stores citation metadata plus a deep paraphrased extraction.

## Audit method

- Scanned `papers/**` for cornerstone paper folders (`Extraction Type: cornerstone` and/or `Corpus Status: Cornerstone`).
- Checked whether each folder has `paper.pdf`, `paper.md`, `deep-extraction.md`, and `claims-and-results.md`.
- Checked source/license pages directly:
  - arXiv abs pages for license hrefs (`creativecommons.org/...` vs `arxiv.org/licenses/nonexclusive-distrib/1.0/`).
  - Nature FunSearch page for Open Access / CC BY 4.0 license text.
- Generated `paper.md` with `pdftotext -layout` when full storage was rights-cleared.

## Rights-cleared and now stored locally

| Folder | Source | License / rights basis | Local full text status | Notes |
| --- | --- | --- | --- | --- |
| `papers/agent-evaluation/osworld/` | arXiv:2404.07972 | CC BY 4.0 | `paper.pdf` + `paper.md` already present | Real computer-use benchmark; full extraction already present. |
| `papers/agent-evaluation/swe-bench/` | arXiv:2310.06770 | CC BY 4.0 | `paper.pdf` + `paper.md` already present | GitHub issue benchmark; full extraction already present. |
| `papers/software-engineering-agents/swe-agent/` | arXiv:2405.15793 | CC BY 4.0 | `paper.pdf` + `paper.md` already present | Agent-computer interface paper; full extraction already present. |
| `papers/recursive-self-improvement/funsearch/` | Nature `s41586-023-06924-6` | Nature page states Open Access / CC BY 4.0 | **Added this pass**: `paper.pdf` + `paper.md` | Existing extraction was abstract/summary-limited; second-pass numeric/table/figure hardening pending. |
| `papers/recursive-self-improvement/ladder/` | arXiv:2503.00735v3 | CC BY 4.0 | **Repaired this pass**: full `paper.md` + new `paper.pdf` | Previous `paper.md` was partial abstract/core excerpt despite being labeled full. |
| `papers/recursive-self-improvement/darwin-godel-machine/` | arXiv:2505.22954v3 | CC BY 4.0 | **Added this pass**: `paper.pdf` + `paper.md` | Second-pass ablation/tooling/archive-tree hardening pending. |
| `papers/recursive-self-improvement/open-endedness-icml-2024/` | arXiv:2406.04268v1 | CC BY 4.0 | **Added this pass**: `paper.pdf` + `paper.md` | Second-pass formal novelty/learnability and safety-scope extraction pending. |

## Not stored under current corpus policy

These are still cornerstone or near-cornerstone sources, but full mirroring is not allowed under the current storage rule unless the author/publisher grants explicit permission or a separate rights-cleared copy is obtained.

| Folder | Source | Observed license / rights status | Local status | Correct next action |
| --- | --- | --- | --- | --- |
| `papers/agent-evaluation/ai-agents-that-matter/` | arXiv:2407.01502 | arXiv non-exclusive distribution license | No `paper.pdf` / `paper.md`; extraction + claims only | Deepen paraphrased extraction against directly inspected source; do not mirror full text. |
| `papers/recursive-self-improvement/alphaevolve/` | arXiv:2506.13131 | CC BY-NC-ND 4.0; current policy treats ND as not compatible for transformed corpus text | No `paper.pdf` / `paper.md`; extraction + claims only | Keep extraction-only unless policy explicitly permits verbatim PDF storage; do not create derived `paper.md`. |
| `papers/recursive-self-improvement/map-elites/` | arXiv:1504.04909 | arXiv non-exclusive distribution license | No `paper.pdf` / `paper.md`; extraction + claims only | Deepen paraphrased extraction; request/locate rights-cleared copy if full mirroring is needed. |
| `papers/recursive-self-improvement/poet/` | arXiv:1901.01753 | arXiv non-exclusive distribution license | No `paper.pdf` / `paper.md`; extraction + claims only | Deepen paraphrased extraction; request/locate rights-cleared copy if full mirroring is needed. |
| `papers/recursive-self-improvement/reward-hacking-skalse-2022/` | arXiv:2209.13085v2 / NeurIPS 2022 | arXiv non-exclusive distribution license | No `paper.pdf` / `paper.md`; extraction + claims only | Deepen paraphrased extraction; keep Goodhart/unhackable-proxy claims source-traceable without full mirroring. |

## Immediate strategic implications

1. **Stop treating “deep extraction exists” as equivalent to “source body exists.”** A future agent needs to know whether it is reading the paper, a verified extraction, or a lead-level summary.
2. **Second-pass the newly repaired full texts before architectural decisions.** Priority order: FunSearch numeric/table claims, DGM ablations/tooling examples, Open-Endedness formal novelty/learnability definition, then LADDER figures/tables if not already covered.
3. **For rights-restricted cornerstones, maximize extraction fidelity instead of mirroring.** The goal is not tiny abstracts; it is source-inspected, paraphrased, section-by-section extraction with exact claim/result inventories and no substantial verbatim copying.
4. **Add a repeatable full-text/license audit gate.** The repo should be able to flag cornerstone folders where `paper.md` is absent, too short, or inconsistent with license metadata.
5. **Feed this into provenance design.** Every claim should eventually know whether it came from `paper.md`, `deep-extraction.md`, a publisher page, a source register, or a chapter interpretation.
