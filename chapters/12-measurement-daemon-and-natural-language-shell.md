# Measurement Daemon and Natural-Language Shell

Status: Current architecture imported from the main `CursiveOS` repo. Measurement daemon is specified; natural-language shell is architectural sketch, not implemented.

## Why this chapter exists

The research corpus had local-agent and Arc B70 material, but it did not fully capture a critical CursiveOS distinction from the main repo:

```text
measurement daemon != natural-language shell
```

This separation is load-bearing. It preserves the integrity of the organism's fitness ledger while still allowing a powerful local agent interface for human operators.

## Core conclusion

CursiveOS should run two separate agent-like components:

| Component | Nature | Trust Level | Role |
| --- | --- | --- | --- |
| Measurement daemon | deterministic, mechanical, non-LLM | high integrity | runs sensors, records results, submits to CursiveRoot |
| Natural-language shell | probabilistic, model-driven | user-interface risk | translates human intent into commands and explanations |

They can share infrastructure, but they must not share write paths or trust boundaries.

## Measurement Daemon

The measurement daemon is the autonomic nervous system of CursiveOS.

It executes sensors, collects structured results, stores them locally, and submits them to the hub/CursiveRoot when the user has consented.

The daemon must not use an LLM in the measurement path. A sensor result that passes through a probabilistic system is no longer a clean sensor result. This is a hard architectural boundary.

### What it runs

The daemon runs versioned sensor plugins from the active sensor suite. In Phase 0 and early Phase 1, this means the genesis performance and regression sensors. Later it can run concurrent sensors for multiple workload classes.

Each sensor has a manifest declaring:

- name;
- version;
- curator identity;
- declared outputs;
- schedule/cadence;
- schema.

The daemon verifies the manifest against the hub's registered sensor list before execution. Unrecognized sensors do not run just because they exist on disk.

### Execution modes

| Mode | Purpose |
| --- | --- |
| Scheduled | Cron-like cadence per sensor, such as daily performance or weekly regression. |
| Event-driven | Triggered by workload transitions, such as inference job start or long compile. |
| Manual | User or hub asks for a measurement run. |

The daemon respects quiet hours and system load.

### Results pipeline

```text
sensor executes
-> emits structured JSON
-> daemon validates against schema
-> valid result written to local durable queue
-> queued results submitted on batched cadence
-> hub ack removes pending result
-> failed submission stays queued
```

Local durable storage path in the current architecture:

```text
/var/lib/cursiveos/sensor_results/
```

## Privacy Boundary

With user consent, the daemon may submit:

- hardware fingerprint;
- CPU/GPU/RAM/kernel/distro class data;
- sensor measurements and deltas;
- preset version;
- pseudonymous machine ID.

It must not submit:

- user files;
- documents;
- browser history;
- shell history;
- clipboard;
- arbitrary filesystem content;
- process lists with arguments;
- user activity details.

Workload classification happens locally and submits only class labels.

## Local Preset Application

When the hub publishes a new canonical preset for a hardware class, the daemon can stage it and run local regression tests.

The intended flow:

```text
hub publishes signed preset
-> daemon downloads to staging
-> daemon applies temporarily
-> local regression sensor runs
-> if no regression: apply or request user confirmation depending on mode
-> if regression: reject locally and report divergence
```

Default for v1.0 should be manual confirmation. Auto-apply can become optional only after fleet confidence improves.

## Daemon Failure Modes

- If the daemon crashes, the system continues working.
- If the hub is unreachable, results queue locally.
- If a sensor crashes or emits malformed output, the daemon quarantines that sensor and reports the fault.
- If a candidate preset fails local regression, it does not apply.

The daemon should run with minimum privilege. It needs broad read access to system state and write access to its own results directory. System mutation should happen through a scoped helper, not by giving the daemon general root authority.

## Natural-Language Shell

The natural-language shell is the planned default terminal experience for v1.0.

It is a conversational interface backed by a local or optional remote language model. Users describe outcomes; the agent finds mechanisms.

Conventional terminal access remains available. The shell is not supposed to hide Linux from the user; it should expose commands clearly and help users learn.

## Model Tiers

The main repo defines model tiers by hardware class:

| Tier | Hardware | Role |
| --- | --- | --- |
| Entry | modest CPU, 8-16GB RAM | small local model, 4-8B, routine command translation |
| Workstation | dGPU or high-end iGPU, 16-32GB VRAM | 20-30B model class, multi-step tasks, file reasoning |
| Fleet | multiple machines plus one workstation | shared local inference server for edge nodes |
| Remote | opt-in | frontier model for specific requests with visible disclosure |

This connects directly to the Arc B70 research. The B70 is a candidate workstation-tier accelerator for the natural-language shell and local-agent workflows, but not yet validated as the default reference card.

## Permission Model

The shell agent has three permission modes:

| Mode | Scope |
| --- | --- |
| Read | inspect system state, run non-mutating commands, answer questions |
| Write | edit files in user home and user-level services; destructive actions require confirmation |
| Root | system-level changes; always require explicit confirmation and sudo-style authentication |

The agent does not cache credentials. Each root escalation is a confirmation boundary.

## Command Transparency

Every command should be visible to the user.

The shell agent may make Linux easier, but it must not become a hidden automation box. Users should be able to see, learn from, rerun, and modify commands.

## Relationship Between Shell and Daemon

The shell can read from the daemon:

- recent sensor results;
- preset state;
- organism activity on the local machine;
- measurement summaries.

The shell cannot write to daemon state. It cannot fabricate sensor results, suppress bad measurements, or alter the fitness ledger.

This is the key trust boundary:

```text
measurement daemon writes organism truth
natural-language shell reads organism truth and helps the human act
```

## Why this matters

A buggy shell is annoying and potentially risky for the local user. A buggy measurement daemon corrupts organism-level truth.

These are different failure classes. CursiveOS should treat them differently.

## What this adds to the research corpus

This chapter fills three gaps:

1. **Local agent architecture** — distinguishes the deterministic organism layer from the probabilistic interface layer.
2. **Permission model** — defines read/write/root modes for the shell agent.
3. **Arc B70 relevance** — places B70 as a possible workstation-tier inference backend, not the organism's measurement authority.

## Current limits

- The natural-language shell is not implemented.
- Exact models, prompts, tool-use harness, persistence model, and remote-routing UI are still design work.
- The measurement daemon needs implementation and hardening.
- The current local Hermes path showed containment risk in earlier inspection, so unattended execution requires explicit approval boundaries.
- Shell/daemon separation must be preserved in code, not merely in docs.

## Research questions answered

| Research Question | Current Answer |
| --- | --- |
| Can the local agent participate in measurement? | It can read and explain results, but must not produce or modify sensor truth. |
| What is the default human interface? | Planned v1.0 natural-language shell with conventional terminal fallback. |
| What does the measurement daemon do? | Runs deterministic sensors, validates JSON output, queues/submits results. |
| What permission modes does the shell need? | Read, Write, Root, with explicit escalation boundaries. |
| Where does Arc B70 fit? | Workstation-tier local model backend candidate, not a trust anchor. |

## Open research gaps

1. Define the shell's persistent memory model.
2. Design the exact command confirmation UX for destructive and root actions.
3. Decide which model families fit each hardware tier.
4. Build containment for unattended tool execution before enabling host mutations.
5. Specify the remote-tier privacy disclosure boundary.
6. Implement daemon/plugin signing and sensor manifest verification.

## Source anchors from main CursiveOS repo

- `docs/architecture/agent-architecture.md` — full daemon specification and shell architecture sketch.
- `ROADMAP.md` — v1.0 natural-language shell as flagship feature.
- `white-paper.md` v2.4 — deterministic measurement path and five-layer architecture.
- `README.md` — current project positioning and roadmap summary.
