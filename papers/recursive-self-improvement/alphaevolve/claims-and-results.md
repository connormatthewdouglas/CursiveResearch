# AlphaEvolve — Claims and Results Inventory

Source: https://arxiv.org/abs/2506.13131 | RSI-001 | Extraction only

## Headline Claims

| # | Claim | Evidence Type | Extraction Confidence |
| --- | --- | --- | --- |
| 1 | Evolutionary coding agent improves SOTA LLMs on scientific/algorithmic tasks | White paper + deployments | Medium-High |
| 2 | LLM pipeline mutates code with evaluator feedback | Architecture | High |
| 3 | Improved Google datacenter scheduling | Internal case study | Medium — **[needs full-text]** |
| 4 | Hardware accelerator functional simplification | Internal case study | Medium — **[needs full-text]** |
| 5 | Accelerated training of AlphaEvolve's own LLM | Self-referential case | Medium — **[needs full-text]** |
| 6 | Provably correct algorithms beating prior automated discovery | Math/CS results | Medium-High |
| 7 | 4×4 complex matrix multiply in 48 scalar mults (Strassen-class advance) | Specific algorithm | High if independently verified |

## Quantified Results (Abstract-Level)

| Domain | Result | Baseline | Caveat |
| --- | --- | --- | --- |
| Matrix multiplication (4×4 complex) | 48 scalar multiplications | 56-year Strassen-class barrier | Specialist verification |
| FunSearch lineage | Expanded scope vs Romera-Paredes et al. 2023 | FunSearch | Qualitative comparison |
| Infrastructure | "More efficient" scheduling; simpler accelerators | Prior Google stacks | Proprietary |

## What Not To Overclaim

- Do not store or redistribute full white paper text (CC BY-NC-ND).
- Do not assume CursiveOS can replicate Google-internal evaluators.
- Matrix multiplication result is one problem — not general OS tuning proof.