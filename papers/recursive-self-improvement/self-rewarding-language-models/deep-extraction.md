# Self-Rewarding Language Models — Deep Extraction

Source: https://arxiv.org/abs/2401.10020
Authors / Lab: Weizhe Yuan, Richard Yuanzhe Pang, Kyunghyun Cho, Xian Li, Sainbayar Sukhbaatar, Jing Xu, Jason Weston (Meta FAIR)
Year / Venue: 2024, ICML 2024 (arXiv:2401.10020v3)
Corpus Status: unvalidated
Extraction Type: important
Rights Status: extraction only (arXiv non-exclusive)

## 1. Paper Map

| Paper Section | What It Covers | Why It Exists In The Paper |
| --- | --- | --- |
| Motivation | Human reward bottleneck; frozen reward models | Why self-rewarding |
| LLM-as-a-Judge | Model scores own outputs | Reward generation |
| Iterative DPO | Train on self-generated preferences | Weight-level improvement |
| Experiments | Llama 2 70B, 3 iterations, AlpacaEval 2.0 | Empirical validation |

## 2. Author's Core Claims

| Claim | Where It Appears | Evidence Used By Authors | Extraction Confidence |
| --- | --- | --- | --- |
| Superhuman agents need superhuman feedback; human labels bottleneck | Abstract | Conceptual + results | Medium |
| Frozen separate reward models cannot improve during LLM training | Abstract | Method critique | High |
| LLM-as-a-Judge on own outputs can supply training rewards | Abstract | Iterative DPO setup | High |
| Instruction following AND reward quality improve across iterations | Abstract | Training curves / eval | Medium |
| Llama 2 70B after 3 iterations beats Claude 2, Gemini Pro, GPT-4 0613 on AlpacaEval 2.0 | Abstract | Leaderboard comparison | High (abstract claim) |

## 3. System / Method Architecture

```
Iteration k:
  LLM_k generates responses
  LLM_k judges responses (LLM-as-a-Judge prompts)
  Build preference pairs from self-judgment
  DPO train → LLM_{k+1}
Repeat (3 iterations reported)
```

Both policy and implicit reward model co-evolve inside same weights.

## 4. Key Mechanisms Inventory

| Mechanism | What It Does | Inputs | Outputs | Why It Matters |
| --- | --- | --- | --- | --- |
| Self-rewarding | Model scores own outputs | Prompt, candidates | Preference labels | Removes human label cost |
| Iterative DPO | Aligns to self-preferences | Pairs from judge | Updated weights | True weight-level RSI |
| Dual improvement | Better answers + better judging | Iteration index | Higher AlpacaEval | Closed-loop capability gain |

## 5. Experimental Setup

- Base model: Llama 2 70B.
- Iterations: 3.
- Evaluation: AlpacaEval 2.0 leaderboard.
- Baselines: Claude 2, Gemini Pro, GPT-4 0613 **[needs full-text for training data, judge prompts]**.

## 6. Results Inventory

| Result | Metric | Comparison | Author Interpretation | Caveat |
| --- | --- | --- | --- | --- |
| Post-iteration model leads AlpacaEval 2.0 | Win rate / LC | Named frontier models | Self-rewarding viable | AlpacaEval ≠ OS benchmarks |
| Improving judge quality | Implicit in loop | Iteration ablation | Model learns to judge better | Risk of self-confirming bias |
| Instruction following gains | Task success | Iteration 0 vs 3 | Axis 1 improvement | **[needs full-text ablations]** |

## 7. Figures and Tables Inventory

| Figure/Table | What It Shows | Important Takeaway | Should Corpus Recreate/Summarize? |
| --- | --- | --- | --- |
| **[needs full-text]** | Iteration vs AlpacaEval | Gains per round | Yes |
| **[needs full-text]** | Judge calibration | Self-reward quality | Yes for safety analysis |

## 8. Limitations Stated By Authors

- "Much left to explore" (abstract).
- **[needs full-text]** for safety, judge bias, collapse modes.

## 9. Limitations Inferred By Corpus

- Classic reward hacking risk: model optimizes judge, not true task (see Skalse et al.).
- AlpacaEval preference judging differs from hardware-scoped deterministic fitness.
- Weight-level RSI without frozen external verifier conflicts with CursiveOS safety posture.

## 10. Failure Modes and Safety Concerns

- Self-reinforcing bias loops (model rewards its own failure modes).
- Judge drift across iterations without external anchor.
- Capability gain on leaderboard may not generalize.

## 11. What Transfers To Software Organisms

- Iterative preference optimization as optional *inner* loop for local models.
- LLM-as-Judge useful as *auxiliary* signal when anchored by external tests.
- Demonstrates co-improvement of capability + evaluation — with caution.

## 12. What Does Not Transfer

- Using self-judgment as sole organism fitness (violates frozen verifier principle).
- Claiming AlpacaEval gains imply kernel/network benchmark gains.
- Unbounded iterative DPO on production organism controllers without holdouts.

## 13. CursiveOS / Corpus Implications

RSI-011 documents the attractive but risky path CursiveOS deliberately avoids as primary fitness. Contrast with sensor array + population confirmation. Pair with Agent-as-a-Judge (process evaluation) and reward hacking theory. If used locally, restrict to proposal ranking with deterministic final gate.

## 14. Open Questions

- Hybrid: self-reward for exploration, sensor array for acceptance?
- Detecting judge-policy collapse in organism loops?

## 15. Extraction Coverage Notes

- All major claims extracted: yes (abstract)
- All experiments extracted: partial
- All figures/tables inventoried: no
- Source-level validation complete: no

## 16. Source Reliability

ICML 2024 peer-reviewed paper. High credibility for LLM alignment context; not direct OS agent evidence.