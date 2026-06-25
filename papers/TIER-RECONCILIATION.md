# Extraction Depth-Tier Reconciliation

Audit of every paper folder against the **Extraction depth tiers** policy in
`papers/README.md`:

- `cornerstone` → requires `deep-extraction.md` **and** `claims-and-results.md`
- `important` → requires `deep-extraction.md` **and** `claims-and-results.md`
- `supporting` / `lead-only` → `deep-extraction.md` only (or source entry)

Each folder's tier is read from its own `Extraction Type:` header. Extraction-depth last audited 2026-06-24; rights-cleared full-text status last audited 2026-06-25.

Full-text status pass added 2026-06-25: rights-cleared cornerstone papers should
store `paper.pdf` and `paper.md`, not just abstract-level summaries or deep
extractions.

Detailed license/source map: `papers/FULL-TEXT-AUDIT-2026-06-25.md`.

## Rights-cleared full-text gaps — CLOSED 2026-06-25

These folders either had no full text or had only a partial `paper.md` despite
CC BY 4.0 rights. Added rights-cleared PDFs plus `pdftotext`-derived
agent-readable text:

| Folder | Paper | Fix |
| --- | --- | --- |
| `funsearch` | FunSearch (RSI-002, Nature s41586-023-06924-6) | Added Nature Open Access / CC BY 4.0 `paper.pdf` and full `paper.md`. |
| `ladder` | LADDER (RSI-023, arXiv 2503.00735v3) | Replaced partial abstract/core excerpt with full PDF text; added `paper.pdf`. |
| `darwin-godel-machine` | Darwin Gödel Machine (RSI-016, arXiv 2505.22954v3) | Added `paper.pdf` and full `paper.md`. |
| `open-endedness-icml-2024` | Open-Endedness is Essential for ASI (RSI-032, arXiv 2406.04268v1) | Added `paper.pdf` and full `paper.md`. |

## Remaining full-text constraints — documented, not copied

The following cornerstone folders remain extraction/citation-only under the
current corpus storage rule: `ai-agents-that-matter`, `alphaevolve`,
`map-elites`, `poet`, and `reward-hacking-skalse-2022`. Their license/source
status and next actions are recorded in `FULL-TEXT-AUDIT-2026-06-25.md`.

## Cornerstone gaps — CLOSED this pass

These cornerstone folders were missing `claims-and-results.md`. Added this pass,
grounded in each paper's `deep-extraction.md`, mirroring
`funsearch/claims-and-results.md`:

| Folder | Paper | Status |
| --- | --- | --- |
| `map-elites` | MAP-Elites (RSI-028, arXiv 1504.04909) | ✅ added |
| `open-endedness-icml-2024` | Open-Endedness is Essential for ASI (RSI-032, arXiv 2406.04268) | ✅ added |
| `poet` | POET (RSI-029, arXiv 1901.01753) | ✅ added |
| `reward-hacking-skalse-2022` | Defining and Characterizing Reward Hacking (NeurIPS 2022, arXiv 2209.13085) | ✅ added |

## Important gaps — FLAGGED only (decision pending)

These folders declare `Extraction Type: important` but have no
`claims-and-results.md`. Per task scope they are **flagged, not fixed** — decide
per folder whether to (a) add a claims inventory or (b) down-tier to
`supporting`:

| Folder | Declared tier | Has claims-and-results.md? |
| --- | --- | --- |
| `agent-as-a-judge` | important | NO |
| `alphadev` | important | NO |
| `branchfs-fec` | important | NO |
| `godel-agent` | important | NO |
| `gptswarm` | important | NO |
| `schedcp` | important | NO |
| `self-rewarding-language-models` | important | NO |
| `sematune` | important | NO |
| `stop-self-taught-optimizer` | important | NO |
| `tune-agent` | important | NO |
| `voyager` | important | NO |

Count: **11 important folders** pending.

## Compliant folders (reference)

Cornerstone/important folders that already satisfy the policy:
`ai-agents-that-matter`, `osworld`, `swe-bench`, `swe-agent`, `alphaevolve`,
`darwin-godel-machine`, `funsearch`, `ladder`, `codeevolve`, `reflexion`.

## Note

`reward-hacking-skalse-2022` declares its tier as "cornerstone for Goodhart/proxy
theory" and has no RSI catalog ID assigned anywhere in the corpus — its claims
file cites the NeurIPS 2022 venue instead. Consider assigning it a formal RSI ID
during the next source-register pass.
