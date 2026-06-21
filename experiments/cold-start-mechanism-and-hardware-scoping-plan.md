# Cold-Start Mechanism Isolation and Hardware-Scoping Predictor Plan

Date created: 2026-06-21
Linked chapters: `chapters/16-benchmark-schema-and-measurement-validity.md` (§5.1, §5.5, §5.7), `chapters/10-seed-organism-and-sensor-array.md`
Status: Proposed experiment; not yet executed.

## Why this experiment, now

Cold-start latency is the project's single most trustworthy signal. The
2026-06-16 noise-floor run measured its within-machine CV at **0.002**
(`chapters/16` §5.7) — rock-solid, ~1 confirmation needed — while every other
channel is too noisy to gate selection. The cold-start result therefore drives
selection today, which makes its *mechanism* and its *transferability* the
highest-value things left to pin down.

Two corpus findings frame the open question:

1. **Mechanism is half-isolated.** Complementary ablation (`chapters/16` §5.1)
   showed v0.9b (GPU frequency pin only) gave **0%** cold-start change while
   v0.9c (full preset minus the GPU pin) kept the full **−51%**. Conclusion on
   record: "the Arc cold-start win is CPU-side (governor/C-state/EPP), and the
   GPU pin is dead weight." The bundle has been narrowed to a *set* of CPU
   idle-exit knobs, but **not to a single causal knob.**

2. **It does not transfer, and we don't know why.** The same preset gives −51%
   on the Ryzen 7 5700 + Arc A750 desktop and **~0%** on the i5-11300H laptop
   (`chapters/16` §5.5), with telemetry ruling out the obvious confounds (the
   laptop *did* switch `powersave → performance`, *was* on AC, preset applied
   cleanly). This is the corpus's "first empirical instance of hardware-scoped
   fitness," and the standing instruction (VALIDATION.md) is: "label cold-start
   gains by hardware class; **build hardware-scoped fitness before any
   fleet-wide preset claim.**"

The network thread already showed the payoff of this style of work: a factorial
A/B collapsed a 9× headline down to "it's just BBR; our buffer stack is dead
weight on ≤1GbE" (`chapters/16` §5.6). This plan applies the **same
decomposition discipline** to cold-start, the signal we actually rely on.

## Hypotheses (falsifiable)

### H1 — Single dominant CPU knob (mechanism)

The desktop's −51% cold-start win is produced by **one** CPU idle-exit factor,
not by interaction across the bundle. Candidate factors, applied independently:

- `governor` (`powersave` → `performance`)
- `EPP` / `energy_performance_preference` (e.g. `balance_power` → `performance`)
- deep C-state limit (e.g. capping `intel_idle.max_cstate` / AMD equivalent, or
  `cpu_dma_latency` / PM-QoS floor that blocks deep package C-states)

**Falsifiable prediction:** in a full factorial over these three factors on the
desktop, one factor accounts for **≥ 80%** of the −51% (measured as its main
effect), and the other two each account for **< 10%**.

**Null / alternative that would falsify H1:** no single main effect exceeds 50%
of the total, i.e. the win is an interaction effect (the bundle only works when
≥2 knobs are set together). That result is equally publishable and changes the
preset story, but it falsifies the "one knob like BBR" framing.

### H2 — Deep-idle exit penalty predicts the gain (hardware-scoping)

The cold-start *benefit* a machine can receive is bounded by, and predicted by,
its **baseline deep-idle exit penalty** — the first-token latency it pays for
having gone into deep package C-state / dGPU idle versus a warm, idle-suppressed
state. The desktop (Ryzen deep C-states + discrete Arc A750 idling down) carries
a large penalty the preset removes; the laptop (shallow idle, integrated
graphics, already near its floor) has little penalty to remove, so the same
preset buys nothing.

**Falsifiable prediction:** a cheap, preset-free **pre-probe** — cold TTFT
(after forced deep idle) minus warm TTFT (back-to-back call, idle suppressed) —
predicts the **sign and rough magnitude** of the eventual preset cold-start
gain across machines. Concretely: machines whose pre-probe penalty is large
(≳ 40%) gain a lot; machines whose penalty is small (≲ 10%) gain ~0.

**Falsified if:** the laptop (or any machine) shows a *large* pre-probe penalty
yet still gets ~0% from the preset, or a machine with a *small* pre-probe
penalty nonetheless gets a large preset gain. Either decouples the predictor
from the outcome and means we still cannot forecast hardware-scoped value from a
cheap probe.

## Method

Use the existing CursiveOS benchmark harness and the cold-start sensor
(`chapters/10`: GPU/CPU idle → first inference token). Do **not** build new
machinery; this is a measurement design over knobs the harness already toggles.

### Part A — Mechanism (desktop only)

1. **Factor levels.** Define the three factors above, each at {baseline, tuned}.
   Record the exact applied value and verify it stuck using the existing
   phase-context telemetry (the §5.1 lesson: an unverified knob is
   indistinguishable from a failed apply).
2. **Full factorial.** 2³ = 8 cells: baseline-all, each single knob, each pair,
   all-three (= v0.9c). All-baseline and all-three reproduce the known endpoints
   (~0 and −51%) and serve as internal controls.
3. **Replication + counterbalancing.** ≥ 6 paired cold-start measurements per
   cell (cold-start CV is 0.002, so 6 is ample), with cell order randomized /
   counterbalanced across sessions to absorb drift and thermal tail. Enforce a
   fixed deep-idle settle before each cold measurement (page cache for the model
   weights is a known confound — `chapters/16` §2.3; hold it constant, e.g.
   pre-warm weights into page cache so the measured penalty is idle-exit, not
   disk read, or explicitly drop caches for every cell identically).
4. **Effect attribution.** Compute main effects and 2-way interactions on the
   cold-start delta. Report each factor's share of the −51%.

### Part B — Hardware-scoping predictor (multi-machine)

1. **Pre-probe.** On each available machine, before any preset, measure
   `penalty = (cold_TTFT − warm_TTFT) / cold_TTFT`. Cold = after a forced deep
   idle window; warm = immediate repeat call. Cheap, no tuning, < 1 min.
2. **Outcome.** On the same machine, run baseline vs winning-preset cold-start
   (≥ 6 paired) and record the gain.
3. **Fit.** Plot pre-probe penalty (x) against preset gain (y) across machines.
   Start with the two characterized machines (desktop large penalty / −51%;
   laptop small penalty / ~0) and add every tester machine available. Test
   whether penalty predicts gain.
4. **Honesty guard.** Two points cannot fit a curve. Treat ≤ 3 machines as a
   *directional consistency check* of H2, not a fitted predictor; state the N
   explicitly and do not quote a regression slope until N ≥ ~5 distinct
   hardware classes.

## Required evidence per run

```text
run_id
date_time_utc
host_id / hardware_fingerprint
cpu_model, igpu/dgpu_model
kernel_version
factor_cell            # which of the 8 cells (Part A) or {baseline,preset} (Part B)
governor_applied, governor_verified
epp_applied, epp_verified
max_cstate_applied, cstate_verified
ac_online, governor_phase_context
page_cache_state       # warmed | dropped (held constant per cell)
cold_ttft_ms, warm_ttft_ms
cold_start_delta_pct
n_paired_measurements
session_id, cell_order_index
```

## Success criteria

| Outcome | Interpretation |
| --- | --- |
| One factor ≥ 80% of −51%, others < 10% | **H1 supported.** Ship that single knob as the cold-start preset; drop the rest as dead weight (the "it's just BBR" outcome for cold-start). |
| No factor > 50%; win needs ≥ 2 knobs together | **H1 falsified.** Cold-start preset must stay a small *bundle*; document the interaction. |
| Pre-probe penalty tracks preset gain in sign + rough magnitude across ≥ 3 machines | **H2 directionally supported.** Cheap pre-probe becomes the gate for "should this machine even run the cold-start preset" — the seed of hardware-scoped fitness. |
| Penalty and gain decouple on any machine | **H2 falsified.** Cold-start value is not predictable from idle-exit penalty alone; hardware-scoping needs a richer fingerprint (escalate to Chapter 10 backlog). |

## Expected outcome (prediction on record)

Best guess, stated so it can be wrong: H1 resolves to the **deep C-state limit /
PM-QoS floor** as the dominant factor (the desktop's Ryzen deep package
C-states impose a real wake penalty the laptop's shallower idle does not), with
governor and EPP contributing little once C-state exit is fast — explaining why
the laptop's verified `powersave → performance` switch bought nothing. H2 then
holds directionally: the laptop's pre-probe penalty will measure small, the
desktop's large, consistent with the −51% / ~0 split. If instead governor
carries the desktop win, H2 is in trouble (the laptop changed governor and still
got nothing), which would itself be the most informative result.

## Boundaries

- This is an `experiments/` plan, per CORPUS_WORKFLOW.md §4. The executable
  runner, harness changes, and CursiveRoot schema fields belong in the main
  `CursiveOS` repo; this file is the design and the evidence bar.
- Read/observe-only on idle behavior; all knobs here are reversible, allowlisted
  config (governor/EPP/C-state limit), not firmware, kernel build, or generated
  code. Keep within the existing reversible-preset envelope (`chapters/10`).
- Outcomes update `chapters/16` §5 and the VALIDATION.md cold-start rows; a
  confirmed predictor (H2) would graduate into Chapter 10's hardware-scoped
  fitness work.
