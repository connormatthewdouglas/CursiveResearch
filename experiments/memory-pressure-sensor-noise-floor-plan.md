# Memory-Pressure Sensor Noise-Floor Validation Plan

Date created: 2026-06-25
Linked chapters: `chapters/01-seed-organism-and-sensor-array.md`
(Performance Sensors, Open Gap #6, Population Confirmation CV ≤ 0.15 rule),
`chapters/00-benchmark-schema-and-measurement-validity.md`
(§5 noise-floor methodology, per-channel CV), `chapters/08-population-confirmation-and-fleet-statistics.md`
(per-channel confirmation counts).
Sharpens: the cycle-2 `candidate-v0.10-zram` inconclusive screen (VALIDATION,
2026-06-25) and the memory-pressure sensor validation row (VALIDATION,
2026-06-25/26).
Status: **Completed / validated.** The pre-registered noise-floor gate passed on
the i5-11300H laptop and Stardust; the probe is now integrated as the fifth
fitness channel in CursiveOS harness v1.4.5 and `seed_organism`.

## Completion note (2026-06-26)

Measured results closed the plan:

- i5-11300H / 16 GB: zram **5.78 s** median refault (CV 0.006/0.019 in both
  orders) vs disk swap **13.9–14.1 s** (CV 0.12/0.19): zram ~2.4× faster and
  steadier.
- Stardust / Ryzen 7 5700 / 64 GB: zram **11.56 s** (CV 0.003) vs disk swap
  **24.27 s** (CV 0.097): zram ~2.1× faster. Identical zram `peak_orig`
  (~647 MiB) across the 16 GB and 64 GB hosts confirmed the cgroup ceiling fixes
  the pressure regime.
- Swappiness finding: v0.9 and v0.10-zram both capped around **45 s** while
  `vm.swappiness=0`; v0.11 (`v0.9 + zram + swappiness=60`) cut refault to
  **10.86 s** with zram peak ~648 MiB.
- First full cycle-3 screen: v0.11 vs v0.9 on Stardust scored **fitness +0.0954**
  with **+75.4%** memory-channel delta and no inference regression
  (cold-start −0.5%, sustained 0.0%). It remains `inconclusive` only because one
  screen gives confidence 0.50; confirmation/promotion is the next step.

## 0. Why this experiment, why now

The genesis sensor suite (network, cold-start, sustained, idle power) has **no
memory-pressure channel**. Cycle 2 made the cost of that gap concrete: the
`candidate-v0.10-zram` variant (v0.9 stack + compressed-RAM swap) screened
**inconclusive** — fitness ≈ +0.0136, inside the per-channel noise floor — for
the simple reason that a swap-compression change cannot move sensors that never
touch memory (Chapter 01 Performance Sensors; VALIDATION "zram cycle-2 screen").
Before this experiment, any memory-class optimization (zram, swappiness, THP,
hugepages, NUMA) correctly read as neutral and could never accumulate fitness.
That was a selection blind spot, not a property of the optimizations.

A validated sensor now exists. `benchmarks/benchmark-memory-pressure-v0.2.sh`
(main repo, 2026-06-25) creates deterministic pressure with a cgroup-v2
`memory.high` ceiling smaller than a fixed compressible working set, then times
faulting that set back in. With a zram swap device the refault is a fast in-RAM
(de)compress; with disk swap it is slow; with no swap it throttles — so a lower
median refault time means the memory subsystem is coping better. It is
RAM-size-independent, throttles rather than OOM-kills (safe to run unattended),
uses a peak sampler for `/sys/block/zram0/mm_stat` to prove zram actually
engaged. The measured runs above cleared the same noise-floor gate every other
channel cleared on 2026-06-16 (Chapter 00 §5; Chapter 01 §"Population
Confirmation"), so the probe has graduated from proposed instrument to
validated fifth channel. This plan remains as the pre-registration and audit
trail for that decision.

## 1. Hypotheses (pre-registered)

| ID | Hypothesis | Falsified if |
| --- | --- | --- |
| **H1 (primary)** | The probe's within-machine median refault time has coefficient of variation **CV ≤ 0.15** (Chapter 01/08 escalation threshold) on each tested machine, making it a selection-usable channel. | Any tested machine shows CV > 0.15 across N = 10 reps. |
| **H2 (engagement)** | Under a zram swap device, the probe demonstrably routes the working set through zram: `/sys/block/zram0/mm_stat` `orig_data_size` rises by ≥ the configured working-set size between pre- and post-snapshots, even with `swappiness=0`. | mm_stat does not move (the probe is not exercising the memory subsystem it claims to, so a "neutral" reading would be an instrument failure, not a real null). |
| **H3 (discrimination)** | The probe **separates** the three swap regimes by more than the noise floor: median refault time `zram < disk-swap` and `no-swap` throttles/floors distinctly. A channel that cannot tell zram from disk-swap cannot credit zram. | The zram vs disk-swap medians overlap within CV, i.e. the channel is consistent but blind to the thing it is meant to measure. |
| **H4 (the payoff)** | With the probe added as a fifth fitness channel, a re-screen of `candidate-v0.10-zram` against the v0.9 parent moves off **inconclusive** — the zram variant shows a memory-channel delta larger than this channel's measured noise floor. | The zram re-screen is still inside the (now-measured) memory noise floor → zram is genuinely neutral on this hardware, or the benefit needs a swappiness-aware variant (Open Gap #6) to surface. |

H1 is the gate; H2 and H3 are validity checks that stop a "quiet" channel from
being mistaken for a *good* one (the idle-power CV-0.83 trap in reverse — there
a real signal looked like noise; here noise-free constancy must not be mistaken
for discrimination). H4 is the decision the whole thread is waiting on, and it
is only interpretable once H1–H3 pass.

## 2. What is measured (and what is not)

- **Primary metric:** median wall-clock refault time (ms) to fault the fixed
  compressible working set back in after the `memory.high` ceiling forced it
  out. Lower is better. This is the candidate fifth fitness channel.
- **Engagement metric (H2):** delta of `/sys/block/zram0/mm_stat`
  `orig_data_size` and `compr_data_size` across the probe window.
- **Guardrail telemetry only:** the four existing channels (cold-start,
  network, sustained, idle power) recorded but **not** used as the fitness
  signal here — this experiment is about the new channel's noise floor, not a
  preset bake-off. Keeping the verifier single-channel is the same discipline
  the proposer-vs-random and idle-power plans use.

## 3. Arms / conditions

| Condition | Swap backing | Tests |
| --- | --- | --- |
| Z | zram swap device active | The target regime; H1 noise floor + H2 engagement |
| D | disk/file swap, zram off | H3 discrimination floor (slow refault) |
| N | no swap (throttle only) | H3 lower bound; confirms `memory.high` throttles not OOMs |

Each condition: **N = 10 reps** on each machine. Ten reps resolves a CV-0.15
channel comfortably and matches the rep count the idle-power validation plan
uses for the same kind of "is this channel quiet enough" question. Reps are run
back-to-back with the working set re-dirtied between reps; record machine
thermal/idle state per rep (the idle-power lesson: sample after settling, not in
a thermal tail).

## 4. Machines

| Machine | Hardware | Role |
| --- | --- | --- |
| **Stardust** | Ryzen 7 5700 + Arc A750 desktop | Noise-floor reference machine (the 2026-06-16 cold-start CV-0.002 host); primary H1. |
| **Laptop** | i5-11300H (`42e7c7257af11f46`) | Second hardware class; the host where `candidate-v0.10-zram` actually screened inconclusive — so H4 re-screen lands here. |

Two machines, two memory subsystems. Per Chapter 01's hardware-scoped-fitness
rule (cold-start was −51% on the desktop, ~0% on the laptop), the noise floor is
reported **per machine**; a channel usable on one is not assumed usable on the
other. Cross-machine *magnitude* pooling is explicitly out of scope until the
fleet calibration in Chapter 08 exists.

## 5. Protocol

1. Snapshot environment: kernel version, `zram` module/algorithm
   (`lzo-rle`/`zstd`), `vm.swappiness`, `memory.high` value, working-set size,
   cgroup-v2 mount — into the run metadata so a future agent can reproduce.
2. For each condition Z/D/N, run the probe N = 10 times; capture median refault
   time, full sample vector (for CV), and mm_stat deltas.
3. Compute within-machine CV per condition. Compare against the 0.15 gate (H1)
   and the cold-start 0.002 gold standard for context.
4. Confirm engagement (H2) and regime separation (H3) before trusting any CV.
5. **Only if H1–H3 pass:** wire the probe into `seed_organism` fitness as a
   weighted fifth channel — weight/cap/severe-threshold set from the *measured*
   CV exactly as the existing channels were — and re-screen
   `candidate-v0.10-zram` vs the v0.9 parent on the laptop (H4). Because v0.9
   sets `swappiness=0`, run the re-screen both as-is (cgroup-forced reclaim
   isolates zram even at swappiness 0, per the probe design) and, if available,
   against a swappiness-aware variant so the two confounds are separated.
6. Record `run_detail_bundles`-style per-rep variance so the result is
   CursiveRoot-ready, matching the every-run-detail-bundles workflow item.

## 6. Success criteria

| Outcome | Decision |
| --- | --- |
| H1 ✔ (CV ≤ 0.15 both machines), H2 ✔, H3 ✔ | Promote the probe from `Unvalidated` toward `Validated` as a fifth selection channel; integrate with measured weight; proceed to H4. Update Chapter 01 Open Gap #6 and VALIDATION. |
| H1 ✔ on Stardust only | Hardware-scope the channel (label by hardware class, as cold-start was); usable for desktop-class selection, open on laptop-class. Do not pool. |
| H1 ✘ (CV > 0.15) | The probe is too noisy to gate selection as built. Treat like the network channel: require CV-escalation, never quote a magnitude, and redesign the working-set/timing before integration. Do **not** wire it into fitness. |
| H2 ✘ (mm_stat flat) | Instrument failure — the probe is not exercising the memory subsystem. Fix the probe (cgroup/working-set sizing) before any noise-floor claim; a "neutral" reading here would be meaningless. |
| H3 ✘ (zram ≈ disk-swap) | The channel is consistent but blind; it cannot credit zram specifically. Keep researching a more discriminating memory metric (PSI refault counters, `pgmajfault`) before integration. |
| H1–H3 ✔, H4 still inside floor | The most informative honest null: zram is genuinely neutral on this hardware at `swappiness=0`. Keep zram an *unscreened lead* pending a swappiness-aware variant; do not reject it, and do not claim it. |

## 7. Expected outcome (pre-registered honest guess)

The probe is deterministic by construction (fixed compressible working set,
forced reclaim, in-RAM (de)compress), so **H1 is likely to pass** with a CV much
closer to cold-start's 0.002 than to network's 0.192 — a refault timer has none
of the thermal-tail sampling pathology that gave idle power its spurious 0.83.
H2 should pass cleanly given the mm_stat instrumentation was designed in. The
real uncertainty is **H4**: given the corpus track record (the network "win"
collapsing to one sysctl; the inert GPU pin), the most probable result is that
zram shows a *small but now-measurable* memory-channel benefit on the laptop
that the genesis suite was simply blind to — converting an uninterpretable
"+0.0136 neutral" into a real, signed, channel-scoped delta. That would be the
first time a memory-class optimization could earn fitness at all, which is the
point. A clean H1 with an H4 null would be almost as valuable: it would say the
*channel* is sound and zram is honestly neutral at `swappiness=0`, redirecting
effort to the swappiness-aware variant rather than to more probe engineering.

## 8. Feasibility

- **Instrument:** built and validated — `benchmarks/benchmark-memory-pressure-v0.2.sh`.
  v0.2 adds peak zram engagement sampling and capped-rep reporting; no new probe
  design is needed for the current cycle-3 screen.
- **Hardware:** Stardust + the i5-11300H laptop, both already in the tester set
  and both already characterized for other channels.
- **Safety:** `memory.high` throttles, never OOM-kills; no host mutation beyond
  reversible swap/cgroup config; nothing graduates to unattended execution.
- **Main-repo build outcome:** the probe graduated into the full-test harness,
  CursiveRoot memory columns, and `seed_organism` fifth-channel scoring after
  H1–H3 passed. Remaining work is confirmation/promotion of v0.11, not probe
  design.

## 9. What would change our mind

Per RESEARCH_PIPELINE §3 ("What evidence would change our mind?"): a clean
H1–H3 pass converts memory pressure from an unmeasured blind spot into the fifth
selection channel and lets the corpus finally adjudicate zram on evidence
instead of leaving it perpetually "inconclusive." A CV > 0.15 result would
instead tell us the *metric* is wrong, not the *optimization* — sending the work
back to probe design (PSI/refault counters) before any memory-class change can
be selected. Either way the corpus stops treating "neutral" and "unmeasured" as
the same reading, which is the specific error cycle 2 exposed.
