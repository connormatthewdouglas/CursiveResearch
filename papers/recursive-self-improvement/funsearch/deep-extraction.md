# FunSearch — Deep Extraction

Source: https://www.nature.com/articles/s41586-023-06924-6
Authors / Lab: Bernardino Romera-Paredes et al., Google DeepMind
Year / Venue: 2024, Nature (s41586-023-06924-6)
Corpus Status: unvalidated
Extraction Type: cornerstone
Rights Status: extraction only (Nature proprietary license)

## 0. Extraction Provenance

Grounded in Nature abstract, public summaries, and AlphaEvolve citations (Romera-Paredes et al., 2023). Full Nature text not stored. Specific numeric results and algorithm listings marked **[needs full-text]**.

## 1. Paper Map

| Paper Section | What It Covers | Why It Exists In The Paper |
| --- | --- | --- |
| Introduction | LLMs for mathematical/program discovery | Motivate combining search + neural priors |
| Method | Evolutionary program search with LLM proposals | Core FunSearch loop |
| Evaluator harness | Automated judges score programs | Ground truth separate from proposer |
| Cap set problem | New constructions in extremal combinatorics | Hard science result |
| Bin packing / optimization | Heuristic discovery for NP-hard problems | Practical CS result |
| Analysis | Sample efficiency, diversity | Why it works |

## 2. Author's Core Claims

| Claim | Where It Appears | Evidence Used By Authors | Extraction Confidence |
| --- | --- | --- | --- |
| LLM + evolutionary search discovers new mathematical results | Abstract / press | Cap set constructions | High (peer-reviewed Nature) |
| Automated evaluators make programs first-class searchable artifacts | Method summaries | Evaluator-led selection | High |
| Discovered heuristics outperform known baselines on bin packing instances | Reported results | Benchmark eval | Medium — **[needs full-text numbers]** |
| Approach generalizes across problems sharing evaluator interface | Discussion | Multiple domains | Medium |

## 3. System / Method Architecture

```
Program database (archive of solutions)
    → LLM proposes new/modified programs (functions in code)
    → Automated evaluator executes and scores
    → Evolutionary selection (keep diverse high scorers)
    → repeat
```

Key invariant: LLM never directly judges final acceptance — evaluator does.

## 4. Key Mechanisms Inventory

| Mechanism | What It Does | Inputs | Outputs | Why It Matters |
| --- | --- | --- | --- | --- |
| LLM program prior | Biases search toward plausible code | Spec + past programs | Candidate functions | Efficient exploration |
| Island/evolutionary sampling | Maintains diversity | Archive | Parents for mutation | Avoid premature convergence |
| Automated evaluator | Objective ground truth | Program execution | Score / validity | Verifier grounding |
| Program-as-solution representation | Executable artifact is the discovery | Domain API | Measurable behavior | Unifies math + CS |

## 5. Experimental Setup

Problems reported publicly:
- Cap set problem (extremal combinatorics).
- Online bin packing / heuristic optimization.

Components: pretrained LLM (DeepMind internal), custom evaluators per problem, evolutionary outer loop. **[needs full-text]** for model IDs, population sizes, compute.

## 6. Results Inventory

| Result | Metric | Comparison | Author Interpretation | Caveat |
| --- | --- | --- | --- | --- |
| New cap set constructions | Set size / dimension | Prior best constructions | Genuine mathematical progress | Specialist verification needed |
| Improved bin packing heuristics | Excess / waste metric | Published heuristics | Practical OR impact | Instance distribution matters |
| Sample-efficient search | Programs to discovery | Traditional search | LLM prior helps | **[needs full-text]** |

## 7. Figures and Tables Inventory

| Figure/Table | What It Shows | Important Takeaway | Should Corpus Recreate/Summarize? |
| --- | --- | --- | --- |
| **[needs full-text]** | FunSearch loop diagram | Evaluator-centric architecture | Yes |
| **[needs full-text]** | Cap set improvements | Science outcome credibility | Summarize in own words |

## 8. Limitations Stated By Authors

- Requires problem-specific automated evaluators (not all domains have them).
- LLM and search compute costs significant.
- **[needs full-text]** for full author limitations list.

## 9. Limitations Inferred By Corpus

- Nature paper methods partially proprietary; reproduction depends on open reimplementations (CodeEvolve, OpenEvolve).
- Evaluator engineering is the hidden labor — not the LLM alone.
- Mathematical discoveries don't automatically imply OS tuning success.

## 10. Failure Modes and Safety Concerns

- Evaluator bugs → false discoveries.
- Overfitting to evaluator instance distribution.
- If evaluator and LLM share blind spots, search wastes compute.

## 11. What Transfers To Software Organisms

- Template for CursiveOS: phenotype code + deterministic sensor evaluation + archive.
- Program databases as organism lineage records.
- Diversity maintenance during fitness optimization.

## 12. What Does Not Transfer

- Assuming cap-set-level discoveries in CursiveOS near term.
- Omitting evaluator engineering from project plans.
- Storing Nature full text without rights.

## 13. CursiveOS / Corpus Implications

RSI-002 lineage root for AlphaEvolve/CodeEvolve. CursiveOS organism loop should cite FunSearch as the canonical "LLM proposes, verifier disposes" pattern. Pairs with Skalse reward hacking: evaluators must resist gaming.

## 14. Open Questions

- Open evaluator suites mirroring FunSearch problems for regression testing organism loops?
- Transfer from combinatorial evaluators to noisy hardware benchmarks?

## 15. Extraction Coverage Notes

- All major claims extracted: partial (secondary sources + abstract knowledge)
- All experiments extracted: no
- All figures/tables inventoried: no
- Source-level validation complete: no
- Sections skipped: full Nature body — rights restricted

## 16. Source Reliability

Peer-reviewed Nature article from DeepMind. Very high credibility; corpus extraction limited by publisher rights.