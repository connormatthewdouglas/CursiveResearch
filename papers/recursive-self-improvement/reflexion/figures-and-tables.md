# Reflexion — Figures and Tables Inventory

Source: https://arxiv.org/abs/2303.11366 | RSI-006 | Extraction only (CC BY 4.0 — attribution required)

Inventory of every figure and table referenced in the locally stored `paper.md`. Figure images are degraded in the ar5iv→Markdown conversion; contents are described from the surrounding text. Table values are transcribed from `paper.md` and cited to their section. No **[needs full-text]** markers — the full text is local.

## Figures

| Figure | Location | What It Shows | Corpus Takeaway |
| --- | --- | --- | --- |
| Figure 1 | §1 | Reflexion operating across decision-making, programming, and reasoning | One framework spans three task families |
| Figure 2 | §3 | Reflexion diagram + the reinforcement-via-self-reflection algorithm | Defines the Actor / Evaluator / Self-Reflection loop |
| Figure 3 | §4.1 | ALFWorld performance over 134 tasks + failure-type classification | Learning continues past the trial 6–7 stall of ReAct-only |
| Figure 4 | §4.2 | Reflexion (CoT and ReAct) on 100 HotPotQA questions over learning steps | Reflexion retries failed tasks; baselines do not improve at temp 0.7 |
| Figure 5 | App. B | ALFWorld "examine a mug with a desklamp" failure→correction | Concrete example of reflection fixing a planning error |
| Figure 6 | App. B.1 | Reflexion vs ReAct on WebShop | Negative result: Reflexion fails to significantly outperform ReAct |
| Figure 7 | App. D.1 | Two HotPotQA trials in one task | Self-reflection yields a better search strategy on the retry |

## Tables

### Table 1 — Code pass@1 vs prior/SOTA (§4.3)

Base strategy is zero-shot; base model GPT-4.

| Benchmark + Language | Previous SOTA Pass@1 | SOTA Pass@1 | Reflexion Pass@1 |
| --- | ---: | ---: | ---: |
| HumanEval (Python) | 65.8 (CodeT + GPT-3.5) | 80.1 (GPT-4) | 91.0 |
| HumanEval (Rust) | — | 60.0 (GPT-4) | 68.0 |
| MBPP (Python) | 67.7 (CodeT + Codex) | 80.1 (GPT-4) | 77.1 |
| MBPP (Rust) | — | 70.9 (GPT-4) | 75.4 |
| Leetcode Hard (Python) | — | 7.5 (GPT-4) | 15.0 |

Takeaway: new SOTA everywhere except MBPP Python.

### Table 2 — Accuracy and test-generation outcomes (§4.3)

Rust rows use the 50 hardest HumanEval Python problems translated to Rust via MultiPL-E. TP = tests pass & solution passes; FN = tests fail but solution passes; FP = tests pass but solution fails; TN = tests fail & solution fails.

| Benchmark + Language | Base | Reflexion | TP | FN | FP | TN |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| HumanEval (Python) | 0.80 | 0.91 | 0.99 | 0.40 | 0.01 | 0.60 |
| MBPP (Python) | 0.80 | 0.77 | 0.84 | 0.59 | 0.16 | 0.41 |
| HumanEval (Rust) | 0.60 | 0.68 | 0.87 | 0.37 | 0.13 | 0.63 |
| MBPP (Rust) | 0.71 | 0.75 | 0.84 | 0.51 | 0.16 | 0.49 |

Takeaway: the high FP column for MBPP Python (0.16) is the mechanism behind its below-SOTA score.

### Table 3 — Rust ablation: test generation × self-reflection (§4.3)

50 hardest HumanEval-Rust problems, GPT-4.

| Approach | Test Generation | Self-Reflection | Pass@1 Accuracy |
| --- | --- | --- | ---: |
| Base model | False | False | 0.60 |
| Test generation omission | False | True | 0.52 |
| Self-reflection omission | True | False | 0.60 |
| Reflexion | True | True | 0.68 |

Takeaway: only the full combination beats baseline; reflection without tests underperforms base.

### Table 4 — HumanEval Python with starchat-beta (App. A)

| Approach | Pass@1 (avg over 8 trials) | Std |
| --- | ---: | ---: |
| Baseline | 0.26 | 0.00481 |
| Reflexion | 0.26 | 0.00305 |

Takeaway: no gain on a weaker model — self-correction is emergent in stronger models.

### Table 5 — HotPotQA across models (App. A)

| Model | Baseline Accuracy | Reflexion Accuracy |
| --- | ---: | ---: |
| CoT (GT) + text-davinci-003 | 0.60 | 0.77 |
| CoT (GT) + gpt-3.5-turbo | 0.57 | 0.71 |
| CoT (GT) + gpt-4 | 0.68 | 0.80 |
| ReAct + text-davinci-003 | 0.30 | 0.55 |
| ReAct + gpt-3.5-turbo | 0.26 | 0.38 |
| ReAct + gpt-4 | 0.39 | 0.51 |

Takeaway: Reflexion improves every model/configuration here; absolute level still tracks base-model strength.

## Corpus Recreation Guidance

Tables 1–5 may be summarized in chapters with attribution to Shinn et al. (2023), CC BY 4.0. Do not reproduce figure images. When citing any number, route CursiveOS-relevance through the corpus taxonomy (these are author-reported results, **Unvalidated** on the CursiveOS harness).
