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

## External Safety Research: Agentic Shells

External security guidance supports the core CursiveOS split: the model-driven
shell can help the user act, but deterministic software must own authority,
measurement truth, and policy enforcement.

The practical lesson from OWASP, NCSC, Microsoft, NIST, and Linux sandboxing
documentation is that agent safety is not a single prompt. It is a stack:

```text
untrusted input handling
-> model proposes intent
-> deterministic policy checks tool scope
-> risk-based sandbox or helper executes
-> user confirms high-risk actions
-> result is logged and reviewable
```

### Prompt Injection Boundary

The shell will read untrusted text constantly: terminal output, issue comments,
documentation, source files, webpages, logs, package metadata, and model
responses. Prompt injection should therefore be treated as a standing condition,
not an exceptional event.

Design consequence:

- external text can inform the model, but cannot authorize action;
- model confidence is not a permission check;
- tool execution must be constrained even when the model claims the instruction
  came from the user;
- sensitive operations need impact containment, because input filtering will not
  catch every malicious instruction.

This strengthens the daemon boundary. A prompt-injected shell may suggest a bad
command; it must not be able to rewrite sensor results, mark a bad preset as
good, or submit false CursiveRoot evidence.

### Tool and Skill Authority

Agentic skills and tools are a supply-chain surface. A skill is not just prose;
it can route natural-language intent toward real filesystem, network, package,
system, or credential behavior.

Minimum research guidance:

| Artifact | Required Metadata | Why It Matters |
| --- | --- | --- |
| Tool | name, owner, version, read/write/root/network scope, destructive flag | lets policy reject overbroad or surprising execution |
| Skill | purpose, allowed tools, forbidden tools, trust level, update source | prevents prompt-only instructions from smuggling authority |
| Command proposal | exact command, target paths/services/devices, network destinations, privilege level | gives the user and policy layer something concrete to approve |
| Execution result | exit status, changed files, stdout/stderr summary, rollback hint | makes agent action reviewable and teachable |

The shell should never treat a newly discovered tool, plugin, MCP server, or
skill as trusted merely because it is available in the environment.

### Risk-Based Execution Tiers

The shell's read/write/root permission modes are necessary but not sufficient.
The execution substrate should also change by risk.

| Risk Class | Examples | Suggested Execution Boundary |
| --- | --- | --- |
| Read-only inspection | `ls`, `cat`, hardware inventory, non-mutating status checks | direct execution with allowlist and logging |
| User-workspace edit | Markdown/code edit inside approved project | workspace-scoped filesystem boundary, diff preview, undo path |
| Network read | fetching docs, package metadata, source references | domain/URL logging, no ambient credential forwarding |
| Build or test | compiler, test runner, package install inside repo | container, Landlock, or equivalent filesystem boundary |
| Untrusted code | downloaded script, unknown benchmark, third-party repo | gVisor-like sandbox or Firecracker-like microVM with clean state |
| Root/system mutation | services, kernel parameters, package manager, boot settings | explicit confirmation, narrow helper, reversible plan, post-check |
| Measurement truth | sensor execution and result submission | deterministic daemon only; no LLM write path |

seccomp, Landlock, containers, gVisor, and microVMs are complementary rather
than interchangeable. The research direction should be a risk-based selector:
use the lightest boundary that preserves the required safety property, and
escalate isolation when code or input is untrusted.

### Memory Boundary

Persistent shell memory is useful for operator experience, but it must not
become organism truth. Memory can be poisoned by malicious docs, stale terminal
output, or attacker-shaped repository content.

Safe memory properties:

- scoped to the shell, not the measurement daemon;
- inspectable and deletable by the user;
- tagged with source, timestamp, and confidence;
- excluded from policy unless explicitly promoted by the user;
- forbidden from storing secrets, credentials, shell history, browser history,
  clipboard contents, or sensitive file excerpts by default.

This keeps the model helpful without letting yesterday's untrusted text become
tomorrow's hidden instruction.

### Confirmation UX

Confirmation should be concrete enough that a user can say yes or no with real
understanding.

Bad confirmation:

```text
Allow the agent to fix networking?
```

Better confirmation:

```text
Run: sudo sysctl -w net.ipv4.tcp_congestion_control=bbr
Scope: kernel network behavior until reboot
Risk: may affect throughput/latency for active connections
Rollback: sudo sysctl -w net.ipv4.tcp_congestion_control=cubic
Post-check: sysctl net.ipv4.tcp_congestion_control
```

The confirmation boundary should become stricter when an action can delete
data, expose secrets, alter services, change boot behavior, spend money, mutate
firmware, or affect measurement truth.

### Rights-Cleared Agent Evaluation Papers

Three rights-cleared papers were added to the paper library because they give
the shell design something better than intuition:

| Paper | Why It Matters For Chapter 12 | Corpus Lesson |
| --- | --- | --- |
| `papers/agent-evaluation/swe-bench/` | Turns real GitHub issue resolution into execution-based tasks. | Grounded tests and reconstructed starting state matter more than model confidence. |
| `papers/software-engineering-agents/swe-agent/` | Introduces agent-computer interfaces and shows that LM-friendly tools improve software-agent performance. | The Cursive shell should be an explicit ACI with bounded tools, concise feedback, and policy metadata. |
| `papers/agent-evaluation/osworld/` | Benchmarks agents in real computer environments with GUI/CLI tasks, VM setup, and execution evaluators. | Cursive shell evaluation should use VM snapshots, OS/app state, executable post-checks, and reset paths. |

Together they sharpen the shell design:

```text
do not benchmark the shell as chat
benchmark it as controlled computer operation
```

For CursiveOS, a useful shell benchmark should combine the SWE-bench discipline
of executable success criteria, the SWE-agent lesson that interface design
changes agent capability, and the OSWorld lesson that real computer tasks need
VM-backed state, GUI/CLI observations, and resettable evaluation.

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

1. Define the shell's persistent memory model, including provenance, decay,
   deletion, and promotion rules.
2. Design the exact command confirmation UX for destructive, network, root,
   firmware, payment, and measurement-adjacent actions.
3. Decide which model families fit each hardware tier.
4. Build risk-based containment for unattended tool execution before enabling
   host mutations.
5. Specify the remote-tier privacy disclosure boundary.
6. Implement daemon/plugin signing and sensor manifest verification.
7. Define the tool/skill manifest format used by the policy layer.

## Source anchors from main CursiveOS repo

- `docs/architecture/agent-architecture.md` — full daemon specification and shell architecture sketch.
- `ROADMAP.md` — v1.0 natural-language shell as flagship feature.
- `white-paper.md` v2.4 — deterministic measurement path and five-layer architecture.
- `README.md` — current project positioning and roadmap summary.

## External Source Anchors

- `sources/local-agent-safety-selected-sources.md` — selected-source digest for
  prompt injection, agentic skills, risk management, sandboxing, and operator
  confirmation design.
- `papers/agent-evaluation/swe-bench/` — rights-cleared full paper and deep
  extraction on executable software-engineering benchmarks.
- `papers/software-engineering-agents/swe-agent/` — rights-cleared full paper
  and deep extraction on agent-computer interfaces.
- `papers/agent-evaluation/osworld/` — rights-cleared full paper and deep
  extraction on real computer-use agent evaluation.
