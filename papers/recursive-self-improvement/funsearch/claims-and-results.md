# FunSearch — Claims and Results Inventory

Source: https://www.nature.com/articles/s41586-023-06924-6 | RSI-002 | CC BY 4.0 full text stored in `paper.pdf` and `paper.md`

## Headline Claims

| # | Claim | Evidence Type | Extraction Confidence |
| --- | --- | --- | --- |
| 1 | LLM + evolution discovers new mathematical constructions | Nature peer review | High |
| 2 | Programs evaluated by automated evaluators, not LM judgment alone | Method | High |
| 3 | Improved heuristics for bin-packing-class problems | OR benchmarks | Medium — full text now stored; numbers need second-pass extraction hardening |
| 4 | General method across problems with evaluator interface | Multi-domain | Medium |

## Result Categories

| Category | Reported Outcome | Notes |
| --- | --- | --- |
| Extremal combinatorics (cap sets) | New constructions beyond prior best | Flagship science result |
| Combinatorial optimization | Better heuristics vs published baselines | Instance-dependent |
| Search efficiency | Fewer programs to strong solutions vs traditional search | Full text available; needs second-pass extraction |

## What Not To Overclaim

- Numeric tables remain paraphrase-only until second-pass extraction hardens them against local `paper.md`.
- Evaluator engineering is the real bottleneck — not "LLM alone discovers math."
- Cap-set results do not imply OS/kernel discovery without new evaluators.