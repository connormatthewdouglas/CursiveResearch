# MAP-Elites — Claims and Results Inventory

Source: https://arxiv.org/abs/1504.04909 | RSI-028 | Extraction only

Grounded in the folder's `deep-extraction.md` (Mouret & Clune, 2015). The paper is an early arXiv draft; body-level numbers are marked **[needs full-text]** where the extraction did not capture them.

## Headline Claims

| # | Claim | Evidence Type | Extraction Confidence |
| --- | --- | --- | --- |
| 1 | Traditional search returns one solution; MAP-Elites illuminates the whole behavior space | Algorithm contrast | High |
| 2 | An archive stores the elite per cell in a user-defined behavior space | Method | High |
| 3 | The resulting map reveals how performance varies across chosen behavior dimensions | Maps | High |
| 4 | Returns diverse high performers, often more useful than a single best | Applications | Medium |
| 5 | Tends to find a better overall best than standard single-objective search | Experiments | Medium |
| 6 | Validated on modular neural networks and soft robots (simulated and real) | Three domains | High |

## Result Categories

| Category | Reported Outcome | Notes |
| --- | --- | --- |
| Illumination | Coverage of behavior–performance landscape vs single-best search | Descriptor choice is decisive |
| Quality-diversity | Many deployable elites across niches | May trade peak fitness for spread |
| Global best (side effect) | Better peak fitness than a traditional EA | Not a universal guarantee — **[needs full-text]** |

## What Not To Overclaim

- Abstract-complete only; early-draft body details and scalability limits are **[needs full-text]**.
- The behavior-descriptor choice is load-bearing — wrong dimensions produce a misleading map, and descriptors accidentally correlated with fitness can be gamed.
- A 2D grid does not capture the full CursiveOS fitness landscape; archives must still pass population confirmation (Ch08), not just per-cell elitism. CVT-MAP-Elites (CodeEvolve) is the continuous-space descendant.
