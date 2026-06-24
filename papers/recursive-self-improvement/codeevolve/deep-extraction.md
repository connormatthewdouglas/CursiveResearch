# CodeEvolve — Deep Extraction

Source: https://arxiv.org/abs/2510.14150
Authors / Lab: Henrique Assumpção, Diego Ferreira, Leandro Campos, Fabricio Murai
Year / Venue: 2025–2026, arXiv (2510.14150v5)
Corpus Status: unvalidated
Extraction Type: important
Rights Status: extraction only (arXiv non-exclusive)

## 1. Paper Map

| Paper Section | What It Covers | Why It Exists In The Paper |
| --- | --- | --- |
| Introduction | Open-source AlphaEvolve-class agent | Reproducibility gap |
| CodeEvolve framework | LLM ensemble + island evolution + MAP-Elites | Architecture |
| Operators | Inspiration crossover, meta-prompting, depth refinement | Search operators |
| AlphaEvolve benchmark suite | 9-problem comparison | Empirical positioning |
| Ablations | Component interactions | Mechanism analysis |
| Guidelines | Hyperparameters, cost | Practitioner value |

## 2. Author's Core Claims

| Claim | Where It Appears | Evidence Used By Authors | Extraction Confidence |
| --- | --- | --- | --- |
| CodeEvolve couples LLMs with island-based evolutionary search for algorithmic discovery | Abstract | Framework | High |
| Uses inspiration crossover, meta-prompting, depth refinement, CVT-MAP-Elites, weighted LLM ensemble | Abstract | Components | High |
| Matches/surpasses reported AlphaEvolve on 5/9 problems | Abstract | Benchmark suite | High |
| Under matched conditions, beats OpenEvolve and ShinkaEvolve on 6/9 | Abstract | Open frameworks | High |
| Qwen3-Coder-30B surpasses reported AlphaEvolve on both CirclePackingSquare instances at ~10× lower cost | Abstract | Cost/performance | Medium-High |
| Competitive with EoH on heuristic design without retuning | Abstract | Additional tasks | Medium |
| Interaction of components drives results, not single operator | Abstract | Ablations | Medium |
| Open release: code, data, hyperparameter guidelines | Abstract | github.com/inter-co/science-codeevolve | High |

## 3. System / Method Architecture

```
CVT-MAP-Elites archive (quality-diversity)
Island populations (parallel evolutionary search)
Weighted LLM ensemble proposes code mutations
Operators:
  - inspiration-based crossover
  - meta-prompting
  - depth-based refinement
Evaluator harness per problem (AlphaEvolve suite)
Select/update archive → iterate
```

## 4. Key Mechanisms Inventory

| Mechanism | What It Does | Inputs | Outputs | Why It Matters |
| --- | --- | --- | --- | --- |
| Island evolution | Parallel subpopulations | Islands + migrants | Diverse search | Scalable exploration |
| CVT-MAP-Elites | Continuous behavior archive | Solutions + descriptors | Elite map | Diversity + best solutions |
| Inspiration crossover | LLM recombines ideas from parents | Parent programs | Child programs | Exploit multiple lineages |
| Meta-prompting | Evolves prompts guiding mutations | Archive feedback | Better proposals | Meta-level search |
| Depth refinement | Iterative local improvement | Candidate | Polished code | Quality boost |
| Weighted LLM ensemble | Routes queries across models | Problem type | Responses | Cost-performance tradeoff |

## 5. Experimental Setup

- Benchmark: AlphaEvolve 9-problem suite.
- Comparisons: reported AlphaEvolve scores, OpenEvolve, ShinkaEvolve (matched conditions), EoH.
- Models: includes open-weight Qwen3-Coder-30B vs frontier closed ensembles.
- Metrics: problem scores, cost, ablation performance.
- 21 pages, 16 figures, 8 tables (per arXiv).

## 6. Results Inventory

| Result | Metric | Comparison | Author Interpretation | Caveat |
| --- | --- | --- | --- | --- |
| AlphaEvolve parity | Wins on 5/9 problems | Reported AlphaEvolve | Open stack competitive | 4/9 not surpassed |
| Open framework comparison | Wins 6/9 | OpenEvolve, ShinkaEvolve | CodeEvolve leads open tools | Matched conditions critical |
| CirclePackingSquare | Beat reported AlphaEvolve | Qwen3-Coder-30B | Open models viable | ~10× cost claim **[needs full-text]** |
| EoH comparison | Competitive | Without retuning | General heuristic strength | Task subset |
| Ablations | Component removal | Full system | Synergy required | **[needs full-text table]** |

## 7. Figures and Tables Inventory

| Figure/Table | What It Shows | Important Takeaway | Should Corpus Recreate/Summarize? |
| --- | --- | --- | --- |
| 8 tables (noted) | Per-problem scores | Where CodeEvolve wins/loses | Yes |
| 16 figures (noted) | Archive/evolution dynamics | Operator effects | When full-text retrieved |

## 8. Limitations Stated By Authors

- Not all AlphaEvolve problems beaten (4/9 gap).
- Hyperparameter sensitivity documented with guidelines.
- **[needs full-text]** for compute budgets, evaluator assumptions.

## 9. Limitations Inferred By Corpus

- AlphaEvolve suite ≠ CursiveOS OS/hardware benchmarks.
- LLM ensemble cost still significant at scale.
- Requires problem-specific evaluators like FunSearch.

## 10. Failure Modes and Safety Concerns

- Overfitting to benchmark harnesses.
- Ensemble cost blowups without weighting discipline.
- False parity claims if comparison conditions mismatched.

## 11. What Transfers To Software Organisms

- Practical open-source evolution loop for CursiveOS prototyping.
- CVT-MAP-Elites archive for preset populations.
- Component synergy lesson: need full loop, not single operator.
- Cost-aware open-model ensembles for local organisms.

## 12. What Does Not Transfer

- Circle packing success ⇒ kernel tuning success.
- Assuming 5/9 AlphaEvolve parity without porting evaluators to OS domain.

## 13. CursiveOS / Corpus Implications

RSI-017 is the most actionable open implementation reference for organism evolution engineering. CursiveOS can fork CodeEvolve patterns with sensor-array evaluators replacing math benchmarks. Report cost-accuracy jointly per AI Agents That Matter. Link to AlphaEvolve (RSI-001) as closed/industrial counterpart.

## 14. Open Questions

- CodeEvolve harness adapter for CursiveOS sensor channels?
- Which operators transfer to sysctl/sched preset mutations?

## 15. Extraction Coverage Notes

- Rich abstract; 21-page tables **[needs full-text]** for per-problem numbers

## 16. Source Reliability

Recent arXiv with open code and data. High practical value; peer review status TBD.