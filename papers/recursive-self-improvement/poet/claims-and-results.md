# POET — Claims and Results Inventory

Source: https://arxiv.org/abs/1901.01753 | RSI-029 | Extraction only

Grounded in the folder's `deep-extraction.md` (Wang, Lehman, Clune & Stanley, 2019). Domain-level and ablation numbers are marked **[needs full-text]** where the extraction did not capture them.

## Headline Claims

| # | Claim | Evidence Type | Extraction Confidence |
| --- | --- | --- | --- |
| 1 | Algorithms should generate new problems while solving them | Conceptual argument | High |
| 2 | POET pairs environment generation with agent optimization | Algorithm | High |
| 3 | It simultaneously explores many problem/solution paths in one population | Population structure | High |
| 4 | Transfer of stepping-stone solutions between environments is essential | Ablations | High |
| 5 | Produces diverse, sophisticated behaviors unsolvable by direct optimization | Experiments | Medium |
| 6 | Outperforms a direct-path curriculum-building control | Baseline comparison | Medium |
| 7 | The open-ended process can in principle continue without bound | Discussion | Medium (philosophical) |

## Result Categories

| Category | Reported Outcome | Notes |
| --- | --- | --- |
| Beyond direct optimization | Solves tasks direct optimization cannot | Domain-specific (toy locomotion/terrain) |
| Transfer ablation | Removing transfer degrades results | Stepping stones essential — **[needs full-text numbers]** |
| Vs curriculum control | Paired open-endedness beats fixed curriculum | Baseline design matters |

## What Not To Overclaim

- Demonstrated in toy physics/terrain domains, not OS tuning — the "environment genome" must be redefined for hardware benchmarks before any transfer claim.
- Transfer-event counts and the 28-page experimental detail are **[needs full-text]**; only the abstract-level argument is captured.
- Unbounded open-ended OS self-modification is **not** safe without gates: weak verifiers let transfer spread bad behaviors (Skalse), and complexity growth needs Ch06 mutation-safety bounds. Combine with MAP-Elites (quality-diversity) and the open-endedness ICML-2024 framing.
