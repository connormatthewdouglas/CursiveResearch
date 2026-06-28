# Idle-Power Selection-Channel Validation Plan

Date created: 2026-06-22
Linked chapters: `chapters/00-benchmark-schema-and-measurement-validity.md`
(§2.2, §5 items 7–8), `chapters/01-seed-organism-and-sensor-array.md`
(Population Confirmation, CV ≤ 0.15 rule).
Status: **Partial (2026-06-28)** — Stardust H1 **PASS**; laptop-on-AC H1 **FAIL**
(cold-run outlier); H3 **PASS**. Battery cohort deferred.

## Results (2026-06-28, production full-test v1.4.5, preset v0.9, N=10)

| Cohort | Machine | idle_baseline_w (10 runs) | CV | H1 | power_source |
| --- | --- | --- | --- | --- | --- |
| AC | Stardust (`3e6b165ddf112a75`) | 9.34, 8.93, 8.93, 8.86, 8.91, 8.87, 8.85, 8.88, 8.89, 8.93 | **0.016** | **PASS** | `energy_counter:…/intel-rapl:0/energy_uj` + GPU `gpu_energy_counter:…/energy1_input` |
| AC | Laptop (`42e7c7257af11f46`) | 32.11, 3.44, 3.1, 2.46, 3.07, 3.07, 2.64, 2.55, 2.84, 2.56 | **1.60** | **FAIL** | `energy_counter:…/intel-rapl:0/energy_uj`; GPU `gpu_none` |

- **Stardust:** CV 0.016 ≪ 0.15 gate — idle power is selection-usable on desktop in the
  production path (confirms Phase-D probe finding in harness, not bespoke probe).
- **Laptop-on-AC:** Full N=10 cohort fails H1 because **run 1 (cold session)** reads
  32.11 W vs ~2.5–3.4 W for runs 2–10. Runs 2–10 alone: CV ≈ **0.12** (would pass).
  Consistent with §2.2 cold-start / post-activity tail bias — first run of a session
  must not gate selection on this hardware class without extra settle or drop-first-run.
- **H3 (comparability):** PASS — Stardust reports RAPL + GPU energy counter; laptop
  reports RAPL only (`gpu_none`). Cross-machine idle-power pooling stays barred.
- **Harness fixes during sprint:** `observe_only: true` → `True` in RESULT_JSON heredoc
  (`8566b86`); CRLF line-ending strip on rigs after Windows SCP (`deaa9a4`).
- Rig logs: `/tmp/idle-power-Stardust-ac-20260628-031719.out`,
  `/tmp/idle-power-elizabethslaptop-ac-20260628-031719.out`

### Integration decision (2026-06-28, locked)

- **Stardust:** idle-power penalty term is **selection-usable within-machine** (CV 0.016 ≪ 0.15).
- **Laptop:** idle power is **hardware/condition-scoped** — full N=10 AC cohort fails H1;
  warmed runs 2–10 alone would pass; require drop-first-run or extra settle before gating.
- **H3:** **PASS** — different `power_source` per machine; **no cross-machine pooling**.
- **Fitness weight:** stays **0** fleet-wide (observe + document); do not wire idle-power
  into `seed_organism.py` until laptop battery cohort completes.

## Purpose

Decide whether idle power is now a usable per-channel **selection** signal in
the production benchmark path, or whether it must stay a same-machine,
directional-only term.

On 2026-06-16 two facts were recorded and are currently in tension:

1. The 6× v0.9 full-test noise floor showed idle-power (CPU) **CV ≈ 0.83**
   ("near-random as currently measured"), so the fitness idle-power penalty
   term was being fed near-random input (Chapter 22 §5 item 7; VALIDATION).
2. A dedicated **Phase-D total-power probe** (settle delay + 12 samples per
   state) on the same Arc A750 desktop showed idle power is actually
   **CV ≈ 0.01** when sampled after settling, and concluded the 0.83 was a
   *sampling artifact* fixed by adding a settle delay + more samples to the
   harness (Chapter 22 §5 item 8; VALIDATION "idle-power noise is sampling").

The gap this plan closes: claim (2) was demonstrated by a **bespoke probe on
one machine**, not by the **production full-test path**, and never on a second
hardware class. Chapter 01's confirmation rule (CV ≤ 0.15) and the live v0.9
screen's idle-power term both depend on this channel being trustworthy, so the
fix must be validated where decisions are actually made.

## Hypotheses (pre-registered)

| ID | Hypothesis | Falsified if |
| --- | --- | --- |
| H1 | The patched harness (pre-capture settle delay + increased sample count, wrapper ≥ v1.4.3) reduces within-machine idle-power CV from ~0.83 to **≤ 0.15** in the **production full-test path** on each tested machine/condition cohort. | Any cohort shows CV > 0.15 with N = 10. |
| H2 | The CV reduction is attributable to the fix, not the environment. | A pre-fix wrapper on the same machine/session also shows CV ≤ 0.15 (i.e. the channel was already quiet and the "fix" changed nothing), or post-fix CV does not improve over a matched pre-fix cohort. |
| H3 (comparability guardrail) | Even where within-machine CV ≤ 0.15, recording `power_source` confirms the test machines report **different physical quantities** (Arc-A750 GPU-energy + RAPL vs laptop RAPL-package-only), so cross-machine idle-power pooling stays invalid. | All machines report the same `power_source` and physical quantity (would weaken §2.2's comparability bar). |

Null for H1: idle-power CV in the production path remains > 0.15 on at least one
machine/condition (fix insufficient, or the channel is hardware/condition-scoped).

## Machines (minimum)

Use the two machines already in the record so results extend existing data:

| Role | Hardware | Fingerprint | Why |
| --- | --- | --- | --- |
| Desktop | Ryzen 7 5700 + Arc A750 ("Stardust") | `3e6b165ddf112a75` | Source of the 0.83 noise floor and the 0.01 Phase-D probe; the channel must work here in production, not just in a probe. |
| Laptop | i5-11300H | `42e7c7257af11f46` | Different power source (RAPL package only, no GPU-energy) + DVFS/battery dynamics; the established hardware-scoping counter-case. |

Add any further fleet machines if available; more `power_source` variety
strengthens H3.

## Method

For each machine:

1. Run the **production full-test** (patched wrapper, the same path that writes
   `runs`/`run_detail_bundles`), **N = 10** times, fixed preset (v0.9), fixed
   model + quantization + Ollama version.
2. **Counterbalance / split** the 10 runs across at least two sessions and
   both a cold-boot start and a warmed-up start, to expose any one-directional
   thermal/C-state drift in the "idle" capture (the original §2.2 bias).
3. **Laptop only:** run two separate cohorts — **on AC** and **on battery**
   (N = 10 each). The corpus already found AC/governor state is decision-
   relevant on this machine; do not pool the two.
4. **H2 attribution (if an unpatched wrapper is available):** run a matched
   pre-fix cohort (N = 10) interleaved on the desktop in the same session, so
   the only difference is settle+samples.
5. Record `power_source` explicitly in structured output for every run
   (this is also §3 item 1, "collect next" — the highest decision-value-per-
   effort schema add; the guard log already knows the source).

### Per-run capture (in structured output, not just stderr)

```text
wrapper_version
machine_fingerprint
power_source            # rapl_pkg | amd_powercap | gpu_hwmon_energy | hwmon_instant | turbostat
idle_settle_seconds     # actual settle elapsed before capture
idle_sample_count       # actual samples taken
power_idle_baseline_w    + raw sample array
power_idle_tuned_w       + raw sample array
governor
ac_online               # 1 | 0
cpu_pkg_temp_c_at_capture
gpu_temp_c_at_capture (if available)
session_id / run_order  # for counterbalancing audit
```

## Metrics

Per machine × condition cohort (N = 10):

- mean, std, **CV** of `power_idle_baseline_w`;
- mean, std, CV of the **idle-power delta term** actually fed to fitness;
- `power_source` (must be constant within a cohort; flag if it switches);
- settle/sample counts actually applied (verify the fix is engaged).

## Success criteria

- **H1 supported** only if every machine × condition cohort has CV ≤ 0.15 at
  N = 10. Report each cohort's CV; do not average CVs across cohorts.
- **H1 falsified** if any cohort exceeds 0.15. Report which cohort (e.g.
  "laptop-on-battery") so the channel can be scoped, not globally trusted.
- **H2 supported** only if the post-fix CV is meaningfully below a matched
  pre-fix cohort on the same machine/session (rules out "already quiet").
- **H3 supported** if `power_source` differs across machines (expected) — in
  which case cross-machine idle-power pooling remains barred regardless of CV.

## Expected outcome (honest prior)

The desktop production path will most likely confirm CV well under 0.15 (the
Phase-D probe already saw ≈ 0.01), so the genuinely open results are: (a) does
the **production path** — not a bespoke probe — actually engage a long-enough
settle, and (b) does the **laptop**, especially **on battery**, stay under
0.15 given DVFS and thermal behavior. Plausible falsification: the production
settle is shorter than the probe's, or battery-state power management keeps
laptop idle power swinging. H3 is near-certain to hold (the two machines are
known to report different sources), which keeps the §2.2 cross-machine bar in
place even on a positive H1.

## Decision impact

- **If H1 holds (per machine):** idle power graduates from "same-machine
  directional only" to a per-channel selection signal with its own (small)
  confirmation count under Chapter 01's per-channel-CV model, and the v0.9
  screen's power term becomes selection-usable *within a machine*.
- **If H1 fails on some hardware:** idle power stays a per-hardware-class
  channel; it must not gate global decisions — consistent with the project's
  first hardware-scoped-fitness finding (cold-start).
- **Either way (H3):** cross-machine idle-power pooling stays barred until
  `power_source`-normalized; this experiment hardens that guardrail with data
  and ships the `power_source` field as a side effect.

## Promotion rules

An idle-power VALIDATION claim may move only if:

- the result is reproduced at N ≥ 10 per cohort on target hardware;
- **variance (CV) is reported per cohort**, not pooled;
- exact wrapper version and `power_source` are captured for every run;
- the result is stated with its hardware/condition scope (no universal claim);
- the relevant Chapter 22 §5 items 7–8 / §2.2 VALIDATION rows are updated.

## Scope boundary (graduate to main repo)

The harness changes themselves — settle-delay/sample-count tuning and adding
the `power_source` structured field — are main-`CursiveOS`-repo build tasks
(§3 items 1; the corpus already lists them). This plan only **validates** that
those changes make idle power selection-usable; it does not specify the code.

## Open assumptions / clarifications needed

- Assumes the patched wrapper (≥ v1.4.3 with settle + extra samples) is the
  one deployed in the production full-test path the operators run. If the
  settle/sample fix is still probe-only and not in the full-test, run that
  graduation first — this plan then measures the production path after it lands.
- Assumes both fingerprinted machines remain accessible to the operator. If
  only the desktop is available, run the desktop cohorts (H1 production-path +
  H2 attribution) and defer the laptop/battery cohorts.
