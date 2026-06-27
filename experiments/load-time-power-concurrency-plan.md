# Load-Time Power During Concurrent Inference — Plan

**Status:** Partial signal (2026-06-27) — load power moves; v0.13 worse than v0.12
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

## Results (Stardust, 2026-06-27, first clean pair)

| Arm | total_w_median | aggregate_tok_s | joules_per_token |
| --- | --- | --- | --- |
| v0.12 parent | 83.87 W | 6.30 | 13.32 |
| v0.13-sched | 85.23 W | 5.03 | 16.94 |

- **Δ total W:** 1.6% (below 10% H3-power gate)
- **Δ joules/token:** 27% — **detectable** but v0.13 is *less* efficient (higher J/token, lower tok/s)

**Interpretation:** Load-time power is a **discriminative** channel (unlike aggregate tok/s alone), but the scheduler candidate regresses on perf/watt. Do not promote v0.13. Next: idle-power CV validation (production harness path) or a different scheduler knob.

Rig log: `/tmp/lp-paired.out` (note: duplicate launches from parallel starters — use first pair only).

## Non-goals

- Fitness weight assignment until gates pass
- Full harness integration (observe-only first)