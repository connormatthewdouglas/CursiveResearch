# Extraction Depth-Tier Reconciliation

Audit of every paper folder against the **Extraction depth tiers** policy in
`papers/README.md`:

- `cornerstone` → requires `deep-extraction.md` **and** `claims-and-results.md`
- `important` → requires `deep-extraction.md` **and** `claims-and-results.md`
- `supporting` / `lead-only` → `deep-extraction.md` only (or source entry)

Each folder's tier is read from its own `Extraction Type:` header. Last audited
2026-06-24.

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
