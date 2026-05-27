# Main Repo Gap Closure and Research Backlog

Status: Current synthesis from the main `CursiveOS` repo and the private `CursiveResearch` corpus. Use this as the bridge between research questions and active project architecture.

## Why this chapter exists

Earlier corpus work identified five high-value research gaps:

1. CursiveRoot evidence model.
2. Mutation safety model.
3. Seed organism specification.
4. Arc B70 / local-agent runtime architecture.
5. Proof of Useful Optimization and contributor incentives.

After reviewing the main `CursiveOS` repo, several of those gaps are no longer empty. The repo already contains active architecture for the seed organism, sensor array, measurement daemon, natural-language shell, Layer 5 economics, and biological design rationale. This chapter records what has been answered, what remains open, and what should be researched next.

## Main Repo Sources Reviewed

| Source | What it contributes |
| --- | --- |
| `README.md` | Current public summary, one-command test path, v0.8/v0.9 status, CursiveRoot upload behavior, initial benchmark results, Layer 5 summary. |
| `ROADMAP.md` | Four transitions: tweak stack → tuned distribution → measurement-native → workload-native → substrate. |
| `docs/architecture/sensor-array.md` | Sensor families, genesis sensor suite, population confirmation, independence criteria, curator model. |
| `docs/architecture/agent-architecture.md` | Measurement daemon vs natural-language shell trust boundary, permission model, model tiers. |
| `docs/specs/layer5-economics-v3.3.md` | Bitcoin-native economics, current/lifetime streams, metabolic sensor, tester/contributor role split. |
| `docs/architecture/biological-architecture.md` | Five-layer organism mapping, biological design principle, substrate compounding, no-governance logic. |

## Gap 1: CursiveRoot Evidence Model

### What the main repo already answers

The evidence model is no longer just a research gap. The main repo defines the sensor array as the organism's sensory nervous system. It determines which contributions improve the organism and replaces voting, appeals, and subjective governance with measurement.

Current evidence primitives:

| Primitive | Current Answer |
| --- | --- |
| Performance signal | Signed numeric delta plus confidence interval. |
| Regression signal | Boolean pass/fail gate that blocks bad variants regardless of upside. |
| Genesis sensors | Network throughput, cold-start latency, sustained inference, idle power. |
| Reversibility | Explicit regression gate; variants must undo cleanly. |
| Hardware compatibility | Variants that help one machine but hurt another should become hardware-scoped, not global. |
| Population confirmation | Required confirmations grow with active tester fleet. |
| Independence | Distinct hardware fingerprints, wallets, and anomaly profiles. |
| Ambiguity handling | High coefficient of variation requires more confirmations. |

Current confirmation rule:

```text
N = max(1, min(5, floor(sqrt(fleet_size))))
```

Current ambiguity escalation:

```text
if CV > 0.15: required_confirmations = N + 2
```

This directly answers the earlier question: **what counts as truth?**

Current answer:

```text
sensor result
+ schema validity
+ confidence interval
+ regression gates
+ population confirmation
+ hardware/wallet/anomaly independence
= organism-usable evidence
```

### Remaining research needed

1. Define the exact CursiveRoot schema for sensor outputs, confidence, confirmations, and hardware-scoped fitness.
2. Calibrate the CV threshold with real fleet data.
3. Build immune sensors for spoofing, coordinated measurements, curator self-dealing, and Goodhart drift.
4. Define how measurements from heterogeneous hardware become reusable recommendations.
5. Decide how much local variance is acceptable before a global preset becomes hardware-scoped.

## Gap 2: Mutation Safety Model

### What the main repo already answers

The main repo partly answers mutation safety through reversible presets, regression gates, local staging, and daemon/shell separation.

Current safety architecture:

| Safety Layer | Current Answer |
| --- | --- |
| Preset changes | Temporary/reversible; full-test wrapper reverts at run end. |
| Candidate mutations | Parent vs candidate comparison on same host; repeat/counterbalance before acceptance. |
| Regression gate | Any breakage gates variant out of merge. |
| Reversibility gate | Variant must return the system to pre-apply state. |
| Local preset updates | Daemon stages new signed preset, runs local regression, rejects on regression. |
| Default auto-apply posture | Manual confirmation for v1.0; auto-apply optional only after fleet confidence improves. |
| Privilege boundary | Measurement daemon should not run as broad root; mutation uses scoped helper. |
| Shell root actions | Explicit confirmation and sudo-style authentication; no credential caching. |

This is a strong start, but it is not yet a full mutation law.

### Remaining research needed

The corpus still needs a formal mutation classification model:

| Class | Mutation Type | Example | Required Safety Gate |
| --- | --- | --- | --- |
| 0 | Read-only observation | hardware probe, sensor read | no mutation; log only |
| 1 | User/service config | agent runtime setting | before/after capture, rollback |
| 2 | Reversible OS tuning | sysctl/sysfs value | allowlist, scoped helper, regression sensor |
| 3 | GPU runtime tuning | power/frequency profile | device-specific probe, telemetry, crash recovery |
| 4 | Scheduler/eBPF | `sched_ext` policy | isolated test, verifier, regression gate |
| 5 | Kernel/package/base image | kernel config, ISO build | VM/lab validation, boot test, signed artifact |
| 6 | Firmware/BMC/BIOS | UEFI/Redfish setting | staged reboot, OOB recovery, human approval |

Recommended expansion: create `chapters/14-mutation-safety-and-permission-law.md` or integrate this into Chapter 06/08.

## Gap 3: Seed Organism Specification

### What the main repo already answers

The seed organism is now concrete.

Current Phase 0 organism:

```text
reversible preset stack
+ full benchmark harness
+ CursiveRoot submission
+ sensor array
+ parent-vs-candidate comparison
+ regression gates
+ repeat/counterbalanced measurement
+ no payout until accepted mutation
```

The main repo says current CursiveOS is still pre-Transition-One: it is a set of shell scripts and measurement apparatus, not yet an operating system. Transition 1 is the move from tweak stack to tuned distribution.

Roadmap sequence:

1. **Tweak stack → tuned distribution**: v0.9 ISO alpha to v1.0 stable.
2. **Tuned distribution → measurement-native**: sensor daemon and signed preset channel make self-improvement empirical.
3. **Measurement-native → workload-native**: workload detection and per-workload preset families.
4. **Workload-native → substrate**: CursiveOS becomes a reference platform others build on.

### Remaining research needed

1. Define the minimum viable v0.9 ISO package list and install flow.
2. Define measurement daemon implementation language and service layout.
3. Define signed preset update format and signature verification flow.
4. Specify local CursiveRoot cache and offline behavior.
5. Decide how seed organism state is displayed to the user.
6. Write the first end-to-end Phase 0 acceptance report after parent/candidate repeat/counterbalance runs.

## Gap 4: Arc B70 and Local Agent Runtime

### What the main repo already answers

The main repo does not make Arc B70 the organism's trust anchor. It places local models inside the natural-language shell layer, not the measurement layer.

This is a critical correction.

Current model:

```text
measurement daemon = deterministic organism truth
natural-language shell = probabilistic operator interface
```

The natural-language shell can read measurement state, summarize sensor results, and help the user operate the system. It cannot fabricate, suppress, or modify sensor truth.

Hardware tiers:

| Tier | Hardware | Model Role |
| --- | --- | --- |
| Entry | modest CPU, 8-16GB RAM | 4-8B local model for routine commands |
| Workstation | dGPU or high-end iGPU, 16-32GB VRAM | 20-30B model class for multi-step tasks |
| Fleet | multiple machines plus one workstation | shared local inference server for edge nodes |
| Remote | opt-in | remote frontier model with clear disclosure |

Arc B70 fits as a candidate workstation-tier backend, not as a requirement and not as the source of organism truth.

### Remaining research needed

1. Benchmark Arc B70 vs A750 vs GB10/NVIDIA alternatives for the natural-language shell workload, not just raw tokens/sec.
2. Define shell model selection criteria: latency, tool-call reliability, JSON validity, local privacy, cost, power, and context handling.
3. Specify persistent memory for the shell without contaminating sensor truth.
4. Design command confirmation UX for destructive/write/root actions.
5. Build containment for unattended tool execution before any host mutation is re-enabled.
6. Define what the remote-tier disclosure UI looks like when requests leave the machine.

## Gap 5: Proof of Useful Optimization and Contributor Incentives

### What the main repo already answers

Chapter 07's token-first research is superseded for CursiveOS's own design by Layer 5 v3.3.

Current CursiveOS economics:

```text
Fast tier users pay BTC-settled subscription
-> cycle revenue is split by metabolic sensor
-> current-cycle stream pays contributors merged this cycle
-> lifetime stream pays all historical contributors by cumulative fitness
-> testers get Fast tier access, not lifetime fitness
-> no custom token
-> no yield pool
-> no voting/governance
```

Proof of Useful Optimization is now concrete:

```text
proposed variant
-> measured on real hardware
-> confirmed by sensor array
-> passes regression/reversibility gates
-> produces positive fitness
-> merges into organism
-> contributor earns lifetime fitness
```

The economic design also answers why testers should not earn lifetime revenue: testers contribute measurement flow, not durable genome improvements. Giving testers lifetime fitness would make fake measurement farms more profitable.

### Remaining research needed

1. Formalize wallet binding for contributors and testers.
2. Define BTC payment, accrual, and claim mechanics.
3. Simulate the metabolic sensor across artificial contributor histories.
4. Research fork obligation inheritance technically and legally.
5. Build anti-Sybil and anti-spoofing economics around hardware fingerprints, wallets, anomaly profiles, and delayed rewards.
6. Define how accepted non-code contributions, such as benchmark methods or sensors, earn fitness.

## What Should Be Added Next

Based on the main repo, the highest-value new research expansions are now:

### 1. Mutation Safety and Permission Law

The corpus has enough pieces, but not yet the formal rulebook. This should define exactly what agents, daemons, contributors, and users are allowed to change under which gates.

### 2. CursiveRoot Schema and Evidence Storage

The sensor-array theory is strong. Now the database/storage schema needs to be formalized: raw run, sensor result, variant, hardware fingerprint, confidence, confirmation set, anomaly flags, fitness ledger.

### 3. Natural-Language Shell Implementation Spec

The architecture sketch is good, but the product needs implementation details: UI, command preview, memory, model selection, permission escalation, remote-tier disclosure, and tool sandboxing.

### 4. Signed Preset Channel and Regression-Gated Update Flow

This is the heart of Transition 2. The corpus needs a deep spec on signed presets, staging, local regression, rollback, and divergence reporting.

### 5. Fork Obligation and Bitcoin-Anchored Ledger Research

This is unique and high-risk. It needs legal, technical, and adversarial analysis before being relied on as an economic primitive.

## Corpus Implication

The biggest update is that the project is farther along architecturally than the earlier research gaps implied.

The gaps are no longer:

```text
What is the organism?
What counts as truth?
How are contributors rewarded?
Where does the local agent fit?
```

The main repo answers those at architecture level.

The new gaps are implementation-level:

```text
How is the evidence stored?
How are mutations permissioned?
How are presets signed and rolled back?
How is the shell safely implemented?
How is the economic ledger enforced?
```

That is good news. The corpus should now move from discovery research to specification research.
