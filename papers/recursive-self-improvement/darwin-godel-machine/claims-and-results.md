# Darwin Gödel Machine — Claims and Results Inventory

Source: https://arxiv.org/abs/2505.22954 | RSI-016 | Extraction only

## Headline Claims

| # | Claim | Confidence |
| --- | --- | --- |
| 1 | Agents can empirically self-improve by modifying own code | High |
| 2 | Open-ended archive exploration essential | Medium-High |
| 3 | Safety via sandbox + human oversight | High |

## Quantified Benchmark Results (Abstract)

| Benchmark | Start | End | Delta |
| --- | --- | --- | --- |
| SWE-bench | 20.0% | 50.0% | +30.0 pp |
| Polyglot | 14.2% | 30.7% | +16.5 pp |

## Ablations (Claimed)

- Beats baselines without self-improvement.
- Beats baselines without open-ended exploration.
- Details: **[needs full-text]**

## What Not To Overclaim

- Coding benchmarks ≠ CursiveOS hardware-scoped fitness.
- Self-modifying agents risk hacking their own evaluators.
- 50% SWE-bench is not autonomous unsupervised production readiness.