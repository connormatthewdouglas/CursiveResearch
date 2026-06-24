# AI Agents That Matter — Claims and Results Inventory

Source: https://arxiv.org/abs/2407.01502 | RSI-004 | Extraction only

## Diagnosis Claims

| # | Claim | Implication for CursiveOS |
| --- | --- | --- |
| 1 | Benchmarks overemphasize accuracy, ignore cost | Report tok/s + power + API/wall cost jointly |
| 2 | Community misattributes accuracy gains | Audit ablations before crediting organism mutations |
| 3 | Model vs app developer needs conflated | Separate capability eval from deployment selection |
| 4 | Inadequate holdouts → shortcut overfitting | Private holdout sensor suites required |
| 5 | Non-standardized eval → irreproducibility | Document organism eval protocol in corpus |

## Prescriptive Claims

| # | Claim | Evidence |
| --- | --- | --- |
| 6 | Joint cost-accuracy optimization implemented | Demonstration — **[needs full-text numbers]** |
| 7 | Principled anti-overfitting framework proposed | Methodology |

## What Not To Overclaim

- Do not treat paper as empirical proof on OS organisms until adapted.
- Cost optimization must not drop safety verification steps.
- Framework details require full-text before implementation spec.