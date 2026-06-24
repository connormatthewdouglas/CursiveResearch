# AI Agents That Matter — Deep Extraction

Source: https://arxiv.org/abs/2407.01502
Authors / Lab: Sayash Kapoor, Benedikt Stroebl, Zachary S. Siegel, Nitya Nadgir, Arvind Narayanan (Princeton)
Year / Venue: 2024, arXiv preprint (2407.01502v1)
Corpus Status: unvalidated
Extraction Type: cornerstone
Rights Status: extraction only (arXiv non-exclusive)

## 1. Paper Map

| Paper Section | What It Covers | Why It Exists In The Paper |
| --- | --- | --- |
| Critique of current benchmarks | Accuracy-only focus, cost ignored | Diagnose misleading leaderboard conclusions |
| Cost-accuracy joint optimization | Proposed optimization + implementation | Actionable fix for expensive SOTA agents |
| Model vs application developer needs | Conflated benchmarking goals | Clarify who benchmarks serve |
| Holdout / overfitting | Inadequate holdouts, shortcut learning | Explain fragile agents |
| Anti-overfitting framework | Principled prescription | Methodological remedy |
| Reproducibility | Lack of standardization | Community practice gap |

## 2. Author's Core Claims

| Claim | Where It Appears | Evidence Used By Authors | Extraction Confidence |
| --- | --- | --- | --- |
| Current agent benchmarks overemphasize accuracy, ignore cost/complexity | Abstract | Analysis of SOTA agents | High |
| Community misattributes accuracy gains to wrong sources | Abstract | Benchmark postmortems | Medium |
| Joint cost-accuracy optimization can cut cost while keeping accuracy | Abstract | Authors' implemented optimization | Medium — details **[needs full-text]** |
| Model-developer and app-developer benchmarking needs are conflated | Abstract | Conceptual argument | High |
| Many benchmarks lack adequate holdouts; agents overfit via shortcuts | Abstract | Case studies | Medium |
| Principled anti-overfitting framework is needed | Abstract | Prescription | Medium |
| Evaluation lacks standardization → poor reproducibility | Abstract | Survey of practices | High |

## 3. System / Method Architecture

Meta-methodology paper. Proposed architecture for agent evaluation:

```
Task suite with proper holdouts
    → measure accuracy AND cost (API $, latency, steps)
    → separate leaderboards: model capability vs deployment fit
    → anti-overfitting checks (shortcut detection)
    → standardized reporting for reproducibility
```

Authors implement one cost-accuracy optimization as demonstration **[needs full-text]**.

## 4. Key Mechanisms Inventory

| Mechanism | What It Does | Inputs | Outputs | Why It Matters |
| --- | --- | --- | --- | --- |
| Cost-accuracy Pareto optimization | Trade efficiency vs performance | Agent configs, benchmark | Cheaper equivalent agents | Practical deployment |
| Holdout discipline | Prevents train-on-test leakage | Public/dev/private splits | Generalization estimate | Organism fitness validity |
| Stakeholder-separated benchmarks | Match eval to use case | Model vs app requirements | Right agent selection | CursiveOS multi-channel fitness |
| Anti-overfitting framework | Detect shortcut exploitation | Agent traces, ablations | Robustness flags | Goodhart mitigation |

## 5. Experimental Setup

- Analysis spans multiple existing agent benchmarks **[needs full-text list]**.
- Demonstration optimization on at least one agent setting **[needs full-text]**.
- Metrics: accuracy, monetary cost, possibly latency/steps.
- Baselines: complex costly SOTA configurations.

## 6. Results Inventory

| Result | Metric | Comparison | Author Interpretation | Caveat |
| --- | --- | --- | --- | --- |
| Cost reduction with maintained accuracy | Cost + accuracy | Naive SOTA vs optimized | Accuracy-cost joint goal viable | **[needs full-text numbers]** |
| Misleading gain attribution | Qualitative | Prior leaderboard analyses | Methodological errors common | Case-study dependent |
| Overfitting via shortcuts | Success rate inflation | Holdout vs train | Agents fragile in production | **[needs full-text examples]** |

## 7. Figures and Tables Inventory

| Figure/Table | What It Shows | Important Takeaway | Should Corpus Recreate/Summarize? |
| --- | --- | --- | --- |
| **[needs full-text]** | Cost vs accuracy scatter | Pareto frontier for agents | Yes — Chapter 22 figure candidate |
| **[needs full-text]** | Shortcut/overfitting examples | What "looks SOTA" means | Yes |

## 8. Limitations Stated By Authors

- **[needs full-text]** — position/analysis paper; scope of covered benchmarks TBD.

## 9. Limitations Inferred By Corpus

- Focus may be LLM API agents, not hardware-scoped OS organisms.
- Cost metric may not include human oversight or infrastructure.
- Framework prescription may need adaptation for multi-channel CursiveOS fitness.

## 10. Failure Modes and Safety Concerns

- Optimizing cost alone can drop safety checks (fewer verification steps).
- Holdouts insufficient → organisms deploy overfit presets that fail on new hardware.
- Non-reproducible evals hide regression in self-improvement loops.

## 11. What Transfers To Software Organisms

- Always report fitness with cost (compute, API, wall time, power).
- Maintain private holdout benchmarks for organism confirmation.
- Separate "can the model/agent solve X" from "should we deploy variant Y."
- Document evaluation protocol for reproducibility.

## 12. What Does Not Transfer

- Treating single accuracy number as organism fitness.
- Publishing only public-benchmark deltas without hardware-scoped confirmation.
- Ignoring shortcut overfitting because leaderboard rank improved.

## 13. CursiveOS / Corpus Implications

RSI-004 cornerstone for Chapter 22. Directly supports multi-metric organism evaluation (tok/s, power, stability, cost). Reinforces population confirmation gates and Goodhart awareness. Any CursiveOS self-improvement claim should cite cost-accuracy joint reporting and holdout discipline.

## 14. Open Questions

- Standard cost accounting for local vs API LLM organisms?
- Holdout design for evolving benchmark suites (open-endedness)?
- How to detect shortcut overfitting in kernel-tuning fitness channels?

## 15. Extraction Coverage Notes

- All major claims extracted: yes (abstract)
- All experiments extracted: no
- All figures/tables inventoried: no
- Source-level validation complete: no
- Sections skipped: case studies, optimization algorithm details — **[needs full-text]**

## 16. Source Reliability

arXiv preprint from established Princeton ML + society lab. High methodological credibility; empirical demonstrations need full-text.