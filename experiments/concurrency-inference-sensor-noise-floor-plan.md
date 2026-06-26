# Concurrency Inference Sensor Noise-Floor Plan

**Status:** Proposed (kickoff 2026-06-26)
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

## Integration path (only if H1–H3 pass)

- Add provisional fitness weight (observe → weight 0 → small weight after CV proof).
- Mirror memory-channel introduction pattern in `seed_organism.py` and `runs` schema.

## Non-goals

- Replace cold-start or single-stream sustained channels.
- Gate selection on concurrency until CV validated.