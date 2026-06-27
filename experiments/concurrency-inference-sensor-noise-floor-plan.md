# Concurrency Inference Sensor Noise-Floor Plan

**Status:** Failed/Blocked (2026-06-27) — H3 signal gate failed (0% v0.8 vs v0.12 on Stardust); H1/H2 passed; fitness weight stays 0
**Sensor:** `benchmark-inference-concurrency-v0.1.sh` (CursiveOS)
**Harness:** v1.4.5 observe-only (`telemetry.concurrency_inference`, weight 0)

## Problem

Single-stream sustained tok/s sits below the selection noise floor on current
hardware (see `docs/action-plan.md` 2026-06-16 noise-floor sprint). Scheduler
and memory-class tweaks may only show under parallel inference load.

## Hypothesis

Aggregate tok/s under N parallel Ollama streams (default N=4) has lower
within-machine CV than single-stream sustained and can discriminate preset
effects that single-stream misses.

## Pre-registered gates

| ID | Gate | Pass criterion |
| --- | --- | --- |
| H1 | Within-machine repeatability | CV ≤ 0.15 on Stardust, 3 runs, same model |
| H2 | Cross-order stability | Normal vs reversed preset order within 5% on aggregate tok/s |
| H3 | Signal vs noise | ≥10% delta between canonical untuned and v0.12 parent on at least one machine |

## Method

1. Run `benchmark-inference-concurrency-v0.1.sh [streams] [model]` on Stardust
   and laptop with streams=4 (override via `CURSIVEOS_CONC_STREAMS`).
2. Record `METRIC_JSON` aggregate_tok_s per run.
3. Compare CV to cold-start channel (CV 0.002 benchmark).

## Results (2026-06-27)

| Gate | Stardust (mistral) | Laptop (tinyllama) | Pass? |
| --- | --- | --- | --- |
| H1 CV ≤ 0.15 | CV 0.0009 (6.66, 6.67, 6.67) | CV 0.0002 (33.22, 33.22, 33.23) | **yes** |
| H2 order ≤ 5% | 0.00% (6.67 vs 6.67) | not run (H2 required ≥1 H1 pass) | **yes** |
| H3 signal ≥ 10% | 0.00% (v0.8 6.67 vs v0.12 6.67) | not run | **no** |

**Decision:** Keep observe-only (weight 0). Concurrency is selection-grade for *repeatability* but not for discriminating the current memory-class parent stack. Re-test H3 only after a scheduler-axis candidate exists.

## Integration path (only if H1–H3 pass)

- Add provisional fitness weight (observe → weight 0 → small weight after CV proof).
- Mirror memory-channel introduction pattern in `seed_organism.py` and `runs` schema.

**Blocked on H3** — do not wire fitness weight until a preset axis shows ≥10% concurrency delta.

## Non-goals

- Replace cold-start or single-stream sustained channels.
- Gate selection on concurrency until CV validated.