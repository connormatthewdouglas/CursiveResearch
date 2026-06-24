# CodeEvolve — Claims and Results Inventory

Source: https://arxiv.org/abs/2510.14150 | RSI-017 | Extraction only

## Benchmark Comparison (AlphaEvolve 9-Problem Suite)

| Comparison | Result | Notes |
| --- | --- | --- |
| vs reported AlphaEvolve | 5/9 match or surpass | 4/9 not beaten |
| vs OpenEvolve (matched) | 6/9 wins | Open-source leader |
| vs ShinkaEvolve (matched) | 6/9 wins | Open-source leader |
| Qwen3-Coder-30B CirclePackingSquare | Beats reported AlphaEvolve both instances | ~10× lower cost (abstract) |
| vs EoH (heuristic design) | Competitive without retuning | Secondary task class |

## Architecture Claims

- CVT-MAP-Elites + island evolution + weighted LLM ensemble.
- Inspiration crossover, meta-prompting, depth refinement.
- Ablations: synergy required; no single operator sufficient.

## What Not To Overclaim

- 5/9 ≠ solved AlphaEvolve entirely.
- Math/optimization benchmarks ≠ OS tuning until evaluators ported.
- Cost comparisons depend on model pricing and matched conditions.