# Scheduler-Axis Concurrency H3 Plan

**Status:** Failed/Blocked (2026-06-27) — H3-sched null: 0% v0.12 vs v0.13 on Stardust
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

## Results (2026-06-27, Stardust mistral 4 streams)

| Arm | aggregate_tok_s | Notes |
| --- | --- | --- |
| v0.12 parent | 6.66 | baseline |
| v0.13-sched | 6.66 | sched_util_clamp_min=256 applied; min/wakeup granularity sysctl N/A on kernel |

**H3_DELTA_PCT=0.00 — FAIL** (criterion ≥10%)

Rig log: `/tmp/h3-sched-Stardust-20260627-183321.out`

**Decision:** Concurrency channel remains observe-only (weight 0). Scheduler sysctl candidate does not move parallel tok/s on founder Stardust.

**Next:** load-time power measurement (action-plan); sched_ext only after kernel capability audit.

## Non-goals

- Full accept cycle or parent promotion
- Swappiness tune (v0.12b) unless operator scopes it