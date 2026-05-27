# Seed Organism and Sensor Array

Status: Current project architecture imported from the main `CursiveOS` repo. Treat as the current internal specification for Phase 0/Transition 1 unless superseded by later CursiveOS implementation changes.

## Why this chapter exists

The research corpus had strong chapters on firmware control, kernel tuning, GPU/accelerator tuning, local agents, AI-guided tuning, and security. What was missing was the live project architecture that binds those pieces into a software organism.

The main `CursiveOS` repo already answers this gap: the seed organism is not a metaphorical future plan. It is a concrete Phase 0 loop built around reversible presets, paired measurement, CursiveRoot submission, sensor evaluation, and candidate selection.

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
| Preset layer | Reversible Linux tuning stack for network, scheduler, VM, memory pressure, CPU/GPU power-state behavior | Chapter 03/04 claims must be measured on real hosts, not treated as universal presets. |
| Benchmark layer | Paired before/after tests for network throughput, cold-start latency, sustained inference, and isolated tweak effects | CursiveRoot truth begins with repeated measurement, not imported research. |
| CursiveRoot | Shared hardware/performance database receiving hardware fingerprint, kernel/distro, preset version, and measured deltas | This is the organism's sensory nervous system. |
| Sensor array | Versioned measurement protocols and evaluation logic | This replaces governance for technical decisions. |
| Economic layer | Bitcoin-native contributor compensation based on measured fitness | Covered separately in Chapter 11. |
| Agent layer | Measurement daemon plus natural-language shell with strict trust separation | Covered in Chapter 12. |

## Genesis Sensor Suite

The main repo defines a small genesis sensor suite because adding too many sensors before the loop works would slow learning and introduce confounds.

### Performance Sensors

Initial performance sensors include:

- **Network throughput sensor** — measures TCP throughput over a simulated WAN link, currently using a 50ms RTT and 0.5% loss setting.
- **Cold-start latency sensor** — measures GPU idle to first inference token time.
- **Sustained inference sensor** — measures steady-state tokens per second on a warm model.
- **Idle power sensor** — measures the power cost of disabling C-states or pinning GPU frequency.

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

## Source anchors from main CursiveOS repo

- `README.md` — current public project summary, seed organism path, v0.8/v0.9 status, CursiveRoot overview.
- `white-paper.md` v2.4 — measurement-first architecture and five-layer structure.
- `docs/architecture/sensor-array.md` — sensor families, genesis sensor suite, population confirmation, curator model.
- `ROADMAP.md` — transitions from tweak stack to tuned distribution, measurement-native OS, workload-native OS, and substrate.
