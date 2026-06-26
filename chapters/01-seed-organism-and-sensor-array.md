## Corpus status (living layer)

**Last reconciled:** 2026-06-24
**Confidence:** Supported as current main-repo architecture; fleet-scale selection **Unvalidated**
**Read with:** [Chapter 00](00-benchmark-schema-and-measurement-validity.md), [Chapter 08](08-population-confirmation-and-fleet-statistics.md), [Chapter 02](02-bitcoin-native-economics-and-proof-of-useful-optimization.md), [Chapter 05](05-measurement-daemon-and-natural-language-shell.md)

### Authoritative for
- Phase 0 loop: reversible presets, paired measurement, CursiveRoot submission, parent-vs-candidate selection
- Population confirmation requirements: N-rule, CV threshold, hardware/wallet/anomaly independence
- Sensor families: regression gates before performance channels

### Superseded or narrowed
- Universal preset claims from kernel/GPU chapters — magnitudes are hardware-scoped (Ch00 cold-start split)

### Open until experiment/hardware
- Fleet calibration of N and CV thresholds (Ch08)
- Immune-sensor prototypes for correlated confirmations

---

## Reinforced research (2026-06-24)

- **Quality-diversity archives:** Mouret & Clune, MAP-Elites (2015); Wang et al., POET (2019) — intakes `papers/recursive-self-improvement/map-elites/`, `poet/`; hardware-scoped fitness is the fleet analogue of behavioral niches (Ch08 §3).
- **Open-ended evolution guardrails:** Lehman et al., ICML 2024 open-endedness tutorial — `papers/recursive-self-improvement/open-endedness-icml-2024/`; novelty without utility constraints is not selection-grade.
- **Verifier-grounded loops:** Romera-Paredes et al., FunSearch (Nature 2023) — `papers/recursive-self-improvement/funsearch/`; external evaluator is non-negotiable for organism mutations.
- **Rollback / branch isolation:** BranchFS (2024 preprint) — `papers/recursive-self-improvement/branchfs-fec/`; aligns with reversible preset design in the core loop.

---

# Seed Organism and Sensor Array

Status: Current project architecture imported from the main `CursiveOS` repo. Treat as the current internal specification for Phase 0/Transition 1 unless superseded by later CursiveOS implementation changes.

## Why this chapter exists

The research corpus had strong chapters on firmware control, kernel tuning, GPU/accelerator tuning, local agents, AI-guided tuning, and security. What was missing was the live project architecture that binds those pieces into a software organism.

The main `CursiveOS` repo already answers this gap: the seed organism is not a metaphorical future plan. It is a concrete Phase 0 loop built around reversible presets, paired measurement, CursiveRoot submission, sensor evaluation, and candidate selection.

> **Corpus inline (2026-06-24):** Fleet N-rule and CV escalation are formalized in **Ch08**; population confirmation requires Ch11 hardware fingerprints — magnitudes from kernel/GPU chapters remain hardware-scoped until Ch00 harness confirms.

## Current Seed Organism State

The main repo describes CursiveOS as a measurement-first Linux optimization layer for local compute, with two current core audiences: decentralized compute/mining operators and local AI/LLM users. Its current operational loop benchmarks a host, applies reversible presets, benchmarks again, reports the measured delta, and reverts automatically unless the operator chooses otherwise.

The current Phase 0 path is explicit:

```text
clone/update CursiveOS
-> run full-test benchmark/preset loop
-> record genesis baseline measurement
-> upload seed artifacts to CursiveRoot
-> compare parent preset against candidate mutation
-> require repeat/counterbalanced measurements before acceptance
```

As of the May 2026 main-repo state, Phase 0 has one real genesis baseline bundle recorded, a first narrow candidate screen prepared, no accepted mutation, and no payout report.

## Core Loop

The living seed organism loop is:

```text
baseline phenotype
-> apply candidate phenotype
-> measure both on the same host
-> compare tuned absolute outcomes
-> repeat/counterbalance order
-> compute signed deltas and confidence
-> accept, reject, or keep investigating
-> record in CursiveRoot
```

This matters because the organism is not optimizing by assertion. It is selecting by measured fitness.

## Current Implemented Components

| Component | Current Role | Research Implication |
| --- | --- | --- |
| Preset layer | Reversible Linux tuning stack for network, scheduler, VM, memory pressure, CPU/GPU power-state behavior | Chapter 07/04 claims must be measured on real hosts, not treated as universal presets. |
| Benchmark layer | Paired before/after tests for network throughput, cold-start latency, sustained inference, and isolated tweak effects | CursiveRoot truth begins with repeated measurement, not imported research. |
| CursiveRoot | Shared hardware/performance database receiving hardware fingerprint, kernel/distro, preset version, and measured deltas | This is the organism's sensory nervous system. |
| Sensor array | Versioned measurement protocols and evaluation logic | This replaces governance for technical decisions. |
| Economic layer | Bitcoin-native contributor compensation based on measured fitness | Covered separately in Chapter 02. |
| Agent layer | Measurement daemon plus natural-language shell with strict trust separation | Covered in Chapter 05. |

## Genesis Sensor Suite

The main repo defines a small genesis sensor suite because adding too many sensors before the loop works would slow learning and introduce confounds.

### Performance Sensors

Initial performance sensors include:

- **Network throughput sensor** — measures TCP throughput over a simulated WAN link, currently using a 50ms RTT and 0.5% loss setting.
- **Cold-start latency sensor** — measures GPU idle to first inference token time.
- **Sustained inference sensor** — measures steady-state tokens per second on a warm model.
- **Idle power sensor** — measures the power cost of disabling C-states or pinning GPU frequency.
- **Memory-pressure sensor** — measures cgroup-`memory.high` refault time under a fixed compressible working set; lower is better. Added as the validated fifth channel in harness v1.4.5 / cycle 3 with provisional fitness weight 0.10.

**Memory-pressure gap closed (2026-06-25/26).** The original genesis suite
measured network, cold-start, sustained inference, and idle power, but nothing
that put the machine under memory pressure. This gap was made concrete by cycle 2: the
`candidate-v0.10-zram` variant (v0.9 parent stack plus a compressed-RAM swap
device — the organism's first *added* optimization rather than a v0.8 subset)
screened on the i5-11300H laptop and came back **inconclusive** — fitness
≈ +0.0136 (neutral, inside the per-channel noise floor; reproducible from the
backfilled CursiveRoot bundle), confidence 0.50 from a single screen. That is the
*expected and honest* result, pre-registered in the variant hypothesis: a
swap-compression change cannot move sensors that never touch memory, so the
screen only proved safe apply/revert and non-regression. Two consequences worth
recording: (1) optimizations whose benefit lives in an unmeasured channel will
correctly read as neutral and never accumulate fitness unless the sensor array
grows, and (2) the v0.9 parent sets `swappiness=0`, which further suppresses
any zram effect. The sensor has now landed, and the active candidate is the
swappiness-aware successor **v0.11-zram-swappiness**, not v0.10-zram.

**Validated sensor (2026-06-25):** `benchmarks/benchmark-memory-pressure-v0.2.sh`
in the main repo creates deterministic pressure with a cgroup-v2 `memory.high`
ceiling smaller than a fixed compressible working set, then times faulting that
set back in. With a zram swap device the refault is a fast in-RAM (de)compress;
with disk swap it is slow; with no fast swap it throttles to the wall-clock cap —
so a lower median time means the memory subsystem is coping better. Three design
choices make it a fair sensor: (1) the cgroup ceiling fixes the pressure point
independent of total RAM, so the same parameters mean the same thing on a 16 GB
laptop and a 64 GB desktop (Chapter 08 comparability); (2) `memory.high`
throttles rather than OOM-kills, so it is safe to run unattended; (3) the v0.2
peak sampler reads `/sys/block/zram0/mm_stat` during the run to prove zram
actually engaged and report the achieved compression ratio. It is now wired into
`cursiveos-full-test-v1.4.sh`, the CursiveRoot `runs` memory columns, and
`tools/seed_organism.py` as a lower-is-better fifth channel with provisional
weight 0.10.

**Validated (2026-06-25, i5-11300H laptop).** A counterbalanced run (working set
1024 MB, ceiling 384 MB, 5 reps each order) cleared that gate decisively. With a
zram swap device the refault time was **5.779 s median in *both* orders**
(CV 0.006 and 0.019 — cold-start tier); against the laptop's existing disk
`/swapfile` it was 13.9–14.1 s (CV 0.116 and 0.193). zram is **2.4× faster and
6–30× steadier**, and the identical median across run orders rules out a warmup
artifact. Two findings fall out: (1) the sensor is trustworthy enough to weight
in fitness, and (2) disk-swap memory pressure is itself a high-variance regime
that zram *tames* — so the win is both lower latency and lower variance.

**Cross-machine confirmation (Stardust, Ryzen 7 5700 / 64 GB).** Re-running the
same parameters on a machine with 4× the RAM gave zram 11.56 s (CV 0.003) vs a
disk-swapfile baseline of 24.27 s — again ~2× faster and low-noise. The decisive
detail: the zram `peak_orig` was ~647 MiB on *both* the 16 GB laptop and the
64 GB desktop, because the cgroup ceiling — not total RAM — sets the pressure.
That is the Chapter 08 comparability claim demonstrated directly: the same
sensor parameters produce the same pressure regime across hardware. Absolute
times still differ by hardware (disk-swap speed, CPU, governor), which is exactly
why fitness stays hardware-scoped; the within-machine zram-vs-disk delta is the
clean, portable signal. These measurements justified integrating memory refault
as a lower-is-better fifth channel and screening the swappiness-aware v0.11
variant.

**Cycle-3 v0.11 screen (2026-06-26, Stardust).** The first full multi-channel
screen of **v0.11-zram-swappiness** against the v0.9 parent earned positive
fitness via the new memory channel: **fitness +0.0954**, decision `inconclusive`
only because one screen gives confidence 0.50. Per-channel result: memory
**+75.4%** (the driver; refault about 45 s capped → **10.86 s**), cold-start
**−0.5%**, sustained **0.0%**, idle **−0.1%**, and network **−24%** treated as
gate-only loopback noise with no severe trip. The important safety result is
that raising `vm.swappiness` from 0 to 60 did **not** regress inference in this
screen. Next step is confirmation (reversed order and/or second machine) before
accepting v0.11 and promoting a new canonical parent.

### Regression Sensors

Regression sensors are gates. They do not add fitness. They block bad variants.

Genesis gates include:

- **Full-test regression sensor** — the full benchmark/test suite must still pass.
- **Reversibility sensor** — the variant must undo cleanly.
- **Hardware compatibility gate** — a variant that improves one machine while damaging another must become hardware-scoped, not globally accepted.

This is a major answer to one of the research gaps: the organism's immune system starts with regression gates and grows into anomaly detection.

## Population Confirmation

A single machine's result should not become global truth once the fleet grows. The main repo defines a confirmation rule:

```text
N = max(1, min(5, floor(sqrt(fleet_size))))
```

Where `fleet_size` is the active tester count in the last 30 days. The cap at 5 keeps validation practical. During single-machine Phase 0, N=1 is accepted as a bootstrap limitation.

Consistency is measured by coefficient of variation. If CV exceeds the threshold, the system requires more confirmations:

```text
if CV > 0.15: required_confirmations = N + 2
```

This should be incorporated into CursiveRoot's evidence model. It directly answers the earlier research gap around what counts as truth.

## Independence Requirement

Independent machines require:

- distinct hardware fingerprints;
- distinct wallets;
- distinct anomaly profiles.

Hardware fingerprints include signals such as CPU microcode, GPU VBIOS, and kernel version. If machines appear distinct but show suspiciously correlated behavior, immune sensors can count them as one confirmation source.

## Sensor Families

The main repo defines five sensor families:

| Sensor Family | Role |
| --- | --- |
| Performance sensors | Produce signed numeric deltas and confidence intervals. |
| Regression sensors | Gate bad variants regardless of performance gain. |
| Immune sensors | Detect spoofing, fraud, coordination, and Goodhart drift. |
| Behavioral sensors | Track contributor/tester/curator patterns over time. |
| Metabolic sensors | Control allocation parameters, especially economics stream split. |

This is a stronger and more concrete architecture than the research corpus previously had.

## Sensor Curation

Curators maintain sensors, tune thresholds, deprecate broken sensors, and resolve sensor conflicts. But the main repo is explicit: curators do not vote on contributions, do not override sensor decisions, and do not receive special economic rewards for the curator role.

Curator succession is measurable:

1. merged sensor code with positive fitness;
2. operated valid tester machine for multiple cycles without anomaly flags;
3. sustained engagement over a time gate.

Revocation is anomaly-triggered and reversible. This fits the larger CursiveOS principle: measure the trait rather than vote on the role.

## What this adds to the research corpus

This chapter fills several gaps:

1. **CursiveRoot evidence model** — now grounded in sensor outputs, confidence, population confirmation, CV thresholds, and hardware independence.
2. **Seed organism specification** — now defined as a real Phase 0 loop, not a vague concept.
3. **Mutation acceptance path** — parent vs candidate, repeat/counterbalance, confidence thresholds, and regression gates.
4. **Anti-gaming architecture** — immune sensors, independent hardware/wallets, and anomaly profiles.
5. **Bridge to economics** — the same sensor array that validates technical fitness also feeds contributor compensation.

## Current limits

- Phase 0 currently has only founder hardware in the fleet, so population confirmation is mostly architectural rather than operational.
- The benchmark surface is intentionally narrow.
- Sensor thresholds such as CV <= 0.15 are starting values, not deeply validated constants.
- Immune sensors are planned, not fully deployed.
- Candidate acceptance has not yet happened at meaningful population scale.

## Research questions now answered

| Research Question | Current Answer |
| --- | --- |
| What is the seed organism? | The reversible preset + benchmark + CursiveRoot + sensor-array loop running on real Linux hosts. |
| What counts as truth? | Sensor output plus confidence, population confirmation, and hardware/wallet/anomaly independence. |
| How does the organism avoid governance? | Sensor array decisions replace votes, appeals, and subjective adjudication. |
| How does a local result become reusable? | Only after enough independent machines report consistent measurements. |
| How does it prevent fake benchmark farms? | Distinct hardware fingerprints, wallets, anomaly profiles, and immune sensors. |

## Open research gaps

1. Define the exact CursiveRoot schema for storing sensor outputs, confidence intervals, and population-confirmation state.
2. Implement and test immune sensors for spoofing, correlated measurements, and curator self-dealing.
3. Calibrate the CV threshold and confirmation rule with real fleet data.
4. Define hardware-scoped fitness for changes that help one hardware class and hurt another.
5. Decide how local agent recommendations consume sensor results without contaminating the deterministic measurement pipeline.
6. **Closed for Phase 0:** add a memory-pressure sensor so memory-class optimizations such as zram can be selected on evidence instead of reading as neutral. Exposed by the cycle-2 `candidate-v0.10-zram` inconclusive screen; closed by validated `benchmark-memory-pressure-v0.2.sh`, harness v1.4.5 memory columns, and provisional fifth-channel fitness integration. Remaining work is confirmation/promotion of the active swappiness-aware v0.11 candidate and later tuning of the swappiness value.

## Source anchors from main CursiveOS repo

- `README.md` — current public project summary, seed organism path, v0.9/v0.11 status, CursiveRoot overview.
- `white-paper.md` v2.4 — measurement-first architecture and five-layer structure.
- `docs/architecture/sensor-array.md` — sensor families, genesis sensor suite, population confirmation, curator model.
- `ROADMAP.md` — transitions from tweak stack to tuned distribution, measurement-native OS, workload-native OS, and substrate.
