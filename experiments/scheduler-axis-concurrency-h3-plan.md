# Scheduler-Axis Concurrency H3 Plan

**Status:** In progress (2026-06-27)
**Parent:** v0.12 (canonical)
**Candidate:** v0.13-sched-concurrency (`cursiveos-presets-v0.13-sched-concurrency.sh`)
**Sensor:** `benchmark-inference-concurrency-v0.1.sh` (4 streams, observe-only weight 0)

## Hypothesis

Tighter CFS granularity + higher `sched_util_clamp_min` on top of the v0.12 memory stack
will move aggregate parallel tok/s by ≥10% on Stardust under 4× mistral streams.

## Candidate knobs (reversible)

| Knob | v0.12 (via v0.8) | v0.13 candidate |
| --- | --- | --- |
| sched_util_clamp_min | 128 | 256 |
| sched_min_granularity_ns | 1_000_000 | 500_000 |
| sched_wakeup_granularity_ns | 1_500_000 | 750_000 |

## Gate

| ID | Criterion |
| --- | --- |
| H3-sched | ≥10% aggregate tok/s delta (v0.12 parent vs v0.13) on Stardust, single paired run minimum |

If H3-sched passes: re-run concurrency noise-floor H3 formally; consider provisional fitness weight ≤0.05.
If null: try load-time power axis or sched_ext (later phase).

## Non-goals

- Full accept cycle or parent promotion
- Swappiness tune (v0.12b) unless operator scopes it