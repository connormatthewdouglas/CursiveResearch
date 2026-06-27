# Load-Time Power During Concurrent Inference — Plan

**Status:** In progress (2026-06-27)
**Sensor:** `benchmark-inference-load-power-v0.1.sh`
**Parent:** v0.12 | **Candidate:** v0.13-sched (scheduler sysctl)

## Hypothesis

Parallel inference load power (CPU RAPL + GPU energy W) or joules/token may
discriminate presets when aggregate tok/s does not.

## Gates (pre-registered)

| ID | Criterion |
| --- | --- |
| H1-power | Within-machine CV of `total_w_median` ≤ 0.15, 3 runs, v0.12, Stardust |
| H3-power | ≥10% delta `total_w_median` or `joules_per_token` between v0.12 and v0.13 |

## Non-goals

- Fitness weight assignment until gates pass
- Full harness integration (observe-only first)