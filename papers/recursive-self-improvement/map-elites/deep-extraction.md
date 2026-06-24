# MAP-Elites — Deep Extraction

Source: https://arxiv.org/abs/1504.04909
Authors / Lab: Jean-Baptiste Mouret, Jeff Clune
Year / Venue: 2015, arXiv (1504.04909v1)
Corpus Status: unvalidated
Extraction Type: cornerstone
Rights Status: extraction only (arXiv non-exclusive)

## 1. Paper Map

| Paper Section | What It Covers | Why It Exists In The Paper |
| --- | --- | --- |
| Motivation | Limitations of single-best search | Need illumination + diversity |
| MAP-Elites algorithm | Archive over behavior dimensions | Core contribution |
| Comparison to traditional search | Finds best AND map | Empirical positioning |
| Domains | Neural modularity, soft robots (sim + real) | Generality |
| Analysis | Performance vs diversity tradeoffs | Insight generation |

## 2. Author's Core Claims

| Claim | Where It Appears | Evidence Used By Authors | Extraction Confidence |
| --- | --- | --- | --- |
| Traditional search returns one solution; MAP-Elites illuminates entire space | Abstract | Algorithm contrast | High |
| Archive stores elites per cell in user-defined behavior space | Abstract | MAP-Elites | High |
| Reveals how performance varies across chosen dimensions | Abstract | Maps | High |
| Returns diverse high-performing solutions, often more useful than single best | Abstract | Applications | Medium |
| Tends to find better overall best than standard search | Abstract | Experiments | Medium |
| Validated on modular nets and soft robots (simulated and real) | Abstract | Three domains | High |

## 3. System / Method Architecture

```
Define behavior characterization φ(solution) → behavior descriptor
Discretize behavior space into grid (or CVT cells)
Loop:
  sample cell / parent elite
  mutate solution
  evaluate fitness f(solution)
  map to cell; if f improves cell elite, replace
Output: archive of elites illuminating behavior-performance landscape
```

## 4. Key Mechanisms Inventory

| Mechanism | What It Does | Inputs | Outputs | Why It Matters |
| --- | --- | --- | --- | --- |
| Behavior dimensions | User-chosen variation axes | Domain knowledge | Descriptor space | Interpretable diversity |
| Elite archive | Per-cell best solution | Mutations + fitness | MAP of niches | Quality-diversity |
| Illumination | Coverage of behavior space | Exploration | Sensitivity analysis | Scientific insight |
| Improving global best | Side effect of filling cells | Archive | Strong single solution | Beats pure exploitation |

## 5. Experimental Setup

Three domains (abstract):
1. Modular neural networks.
2. Simulated soft robots.
3. Real soft robots.

Baselines: traditional evolutionary/search returning single best. Metrics: archive coverage, best fitness, behavioral diversity.

## 6. Results Inventory

| Result | Metric | Comparison | Author Interpretation | Caveat |
| --- | --- | --- | --- | --- |
| Illuminated maps | Coverage + insight | Single-best search | Shows performance-structure relationships | Descriptor choice critical |
| Diverse elites | Count + spread | N/A | Multiple deployable options | May trade peak fitness |
| Better global best | Peak fitness | Traditional EA | Illumination helps exploitation | Not universal guarantee |

## 7. Figures and Tables Inventory

| Figure/Table | What It Shows | Important Takeaway | Should Corpus Recreate/Summarize? |
| --- | --- | --- | --- |
| **[needs full-text]** | MAP heatmaps | Performance vs behavior dims | Yes — corpus visualization pattern |
| Soft robot morphologies | Diverse niches | Quality-diversity intuition | Summarize |

## 8. Limitations Stated By Authors

- Early draft (arXiv note); behavior descriptor design is user burden.
- **[needs full-text]** for scalability limits.

## 9. Limitations Inferred By Corpus

- Curse of dimensionality in behavior space (CVT-MAP-Elites in CodeEvolve mitigates).
- Descriptor gaming if correlated with fitness accidentally.
- Real hardware organisms: behavior dims might be {power, latency, stability} — careful normalization needed.

## 10. Failure Modes and Safety Concerns

- Wrong behavior dimensions → misleading map.
- Empty cells if mutation operators don't reach regions.
- Selecting elite from unsafe behavioral niche (high performance, unstable).

## 11. What Transfers To Software Organisms

- Archive presets by behavioral niche (e.g., power vs throughput).
- Maintain diverse high performers for different deployment contexts.
- CVT-MAP-Elites for continuous behavior spaces (see CodeEvolve).
- Illumination studies for Chapter 22 sensitivity analysis.

## 12. What Does Not Transfer

- Assuming 2D grid sufficient for full CursiveOS fitness landscape.
- Ignoring population confirmation when picking niche elites.

## 13. CursiveOS / Corpus Implications

RSI-028 foundational QD algorithm. CursiveOS population archives should be MAP-Elites-structured, not single-lineage hill-climbers. CodeEvolve's CVT-MAP-Elites is direct engineering descendant.

## 14. Open Questions

- Canonical behavior descriptors for OS tuning organisms?
- Integrate MAP-Elites with POET environment dimensions?

## 15. Extraction Coverage Notes

- Abstract-complete; early draft body **[needs full-text]**

## 16. Source Reliability

Highly influential QD paper (Clune/Mouret). Cornerstone credibility; later CVT variants standard in 2025+ coding agents.