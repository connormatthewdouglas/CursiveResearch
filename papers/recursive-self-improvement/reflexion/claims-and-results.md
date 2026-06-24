# Reflexion — Claims and Results Inventory

Source: https://arxiv.org/abs/2303.11366 | RSI-006 | Extraction only (CC BY 4.0 — attribution required)

All numbers below are traceable to the locally stored `paper.md` (ar5iv conversion of arXiv:2303.11366); section/table citations are given inline.

## Headline Claims

| # | Claim | Extraction Confidence |
| --- | --- | --- |
| 1 | Language agents can be reinforced via verbal feedback in episodic memory, without weight updates (§1, §3) | High |
| 2 | Reflexion sets new pass@1 SOTA on most listed code benchmarks (§4.3, Table 1) | High |
| 3 | Self-reflection adds value beyond episodic memory alone (§4.2) | High |
| 4 | Test generation and self-reflection are complementary mechanisms (§4.3, Table 3) | High |
| 5 | Self-correction is an emergent ability of stronger models (App. A, Table 4) | Medium-High |

## Quantified Benchmark Results

Headline deltas (§1, §4):

| Task family | Benchmark | Reported gain |
| --- | --- | --- |
| Decision-making | ALFWorld | +22 pp over baseline, across 12 iterative steps |
| Reasoning | HotPotQA | +20 pp (headline); +14 pp vs CoT w/ ground-truth context |
| Coding | HumanEval | up to +11 pp |

Code pass@1, Table 1 (base strategy = zero-shot; base model GPT-4):

| Benchmark + Language | Previous SOTA | SOTA (GPT-4) | Reflexion |
| --- | ---: | ---: | ---: |
| HumanEval (Python) | 65.8 (CodeT+GPT-3.5) | 80.1 | 91.0 |
| HumanEval (Rust) | — | 60.0 | 68.0 |
| MBPP (Python) | 67.7 (CodeT+Codex) | 80.1 | 77.1 |
| MBPP (Rust) | — | 70.9 | 75.4 |
| Leetcode Hard (Python) | — | 7.5 | 15.0 |

Reflexion sets new SOTA on every listed benchmark **except MBPP Python** (§4.3). The miss is attributed to a 16.3% false-positive self-test rate on MBPP Python vs 1.4% on HumanEval Python (§4.3 analysis).

ALFWorld (§4.1): ReAct+Reflexion solves **130 / 134** tasks with the simple heuristic; ReAct-only stalls between trials 6–7 and converges at a ~22% hallucination rate.

## Ablations (Claimed)

- **HotPotQA self-reflection ablation** (§4.2): self-reflection gives **+8 pp absolute** over episodic-memory-only.
- **Rust test-gen × self-reflection ablation** (Table 3, 50 hardest HumanEval-Rust, GPT-4):
  | Approach | Test Gen | Self-Reflection | Pass@1 |
  | --- | --- | --- | ---: |
  | Base model | False | False | 0.60 |
  | Test-generation omission | False | True | 0.52 |
  | Self-reflection omission | True | False | 0.60 |
  | Reflexion | True | True | 0.68 |
  Reflection without tests (0.52) is *worse* than base — the agent cannot tell whether its code is correct.
- **Model-strength ablation** (Table 4): starchat-beta shows no gain (Baseline 0.26 → Reflexion 0.26 pass@1, avg over 8 trials), supporting the emergent-ability claim.
- **WebShop** (App. B.1): no improvement after 4 trials over 100 environments — a stated negative result.

## What Not To Overclaim

- **Verbal self-reflection on language tasks ≠ hardware-scoped fitness selection.** Reflexion's reward is exact-match / unit-test pass on text and code; CursiveOS fitness is numeric, noisy, and hardware-specific. The paper itself lists "functions whose outputs vary by hardware specification" as a case where its test-driven evaluation breaks down (§5) — exactly CursiveOS's regime.
- The headline numbers are **single-base-model (GPT-4), single-benchmark** snapshots from early 2023; they are not robustness or generalization guarantees.
- "SOTA" depends entirely on the Evaluator. The MBPP Python miss and the 16.3% false-positive rate show that a weak verifier caps the method — a direct warning for any LLM-as-judge shortcut in CursiveOS.
- Emergence (Table 4) means the loop can **fail outright on weaker/smaller models** — relevant because CursiveOS targets local, smaller models.
- For CursiveOS the loop is **Supported as a pattern, Unvalidated as a mechanism** (corpus taxonomy): reuse the proposer/reflection structure, but the verifier must be a grounded sensor (Ch00/Ch06), never the reflection model itself.
