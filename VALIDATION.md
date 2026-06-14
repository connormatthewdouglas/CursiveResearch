# Validation Status

This is the current, compact status page for research claims that can affect
CursiveOS implementation or decisions. For editing rules, see
[CORPUS_WORKFLOW.md](CORPUS_WORKFLOW.md). For what changed, see
[CHANGELOG.md](CHANGELOG.md).

## Status Meanings

| Status | Meaning |
| --- | --- |
| `Unvalidated` | Collected research or a proposal that has not been checked enough to rely on. |
| `Supported` | Evidence is useful and points in the stated direction, but further checking is needed for a firm conclusion. |
| `Validated` | Confirmed sufficiently for the stated scope and current project use. |
| `Disproven` | Evidence shows the claim is wrong or does not apply in the stated scope. |
| `Superseded` | Replaced by changed conditions or better guidance. |

## Current High-Impact Claims

| Area | Claim | Status | Checked | Evidence / Scope | Action |
| --- | --- | --- | --- | --- | --- |
| Chapter 10 / seed organism | The seed organism is the Phase 0 loop of reversible presets, paired measurement, CursiveRoot submission, sensor evaluation, and parent-vs-candidate selection. | Supported | 2026-05-27 | Main `CursiveOS` `README.md`, `white-paper.md`, `docs/architecture/sensor-array.md`, and `ROADMAP.md`. Current architecture, not proof that fleet-scale selection works yet. | Use Chapter 10 as current architecture; validate at population scale as testers join. |
| Chapter 10 / evidence model | Population confirmation, hardware/wallet/anomaly independence, CV thresholding, regression gates, and sensor families are the current answer to “what counts as truth.” | Supported | 2026-05-27 | Main `CursiveOS` sensor-array spec. Thresholds and formulas are specified but not calibrated against a large fleet. | Implement, collect fleet data, then calibrate thresholds. |
| Chapter 11 / economics | CursiveOS's current economic design is Bitcoin-native: no custom token, no yield pool, no governance, direct cycle revenue to contributors weighted by measured fitness. | Supported | 2026-05-27 | Main `CursiveOS` Layer 5 Economics v3.3 and white paper. Specified, not deployed for real payments. | Treat Chapter 07 tokenomics as comparison; use Chapter 11 for current CursiveOS design. |
| Chapter 12 / daemon-shell split | The measurement daemon and natural-language shell must remain separate trust domains; the shell can read measurement state but cannot write sensor truth. | Supported | 2026-05-27 | Main `CursiveOS` agent architecture spec. Daemon specified; shell not implemented. | Preserve boundary in implementation. |
| Chapter 12 / natural-language shell | The natural-language shell is planned as the v1.0 default terminal experience, with conventional terminal fallback and read/write/root permission modes. | Supported | 2026-05-27 | Main `CursiveOS` `ROADMAP.md` and agent architecture spec. | Specify model tiers, memory, confirmation UX, and containment before implementation. |
| Chapter 12 / shell safety controls | Local shell actions should pass through deterministic policy, risk-based containment, concrete user confirmation, and memory boundaries instead of relying on prompts alone. | Supported | 2026-05-31 | Source-backed review of OWASP LLM risks, OWASP Agentic Skills risks, NCSC prompt-injection guidance, Microsoft indirect prompt-injection guidance, NIST AI RMF, and Linux/gVisor/Firecracker sandboxing docs. This supports architecture direction, not a complete implementation design. | Define tool/skill manifests, command risk classes, sandbox selector, and shell memory model before enabling unattended host mutation. |
| Chapter 12 / shell evaluation | The natural-language shell should be evaluated as controlled computer operation, not as chat quality. | Supported | 2026-05-31 | Rights-cleared paper intake of SWE-bench, SWE-agent, and OSWorld. These support execution-based tests, agent-computer interface design, VM-backed task setup, and realistic OS/computer-use evaluation. | Design shell benchmarks with starting state, proposed action, executable post-check, reset/rollback, and risk class. |
| Chapter 09 / Hermes context | The inspected local Hermes build requires a configured context of at least 64,000 tokens; the deployed model config uses 65,536. | Validated | 2026-05-26 | Local Hermes source and `~/.hermes/config.yaml`; valid only for the inspected deployment/version. | Keep Hermes configuration at 64k or higher. |
| Chapter 09 / responsiveness | Reducing active prompt, tool-schema, and retained-history payloads improves responsiveness in the current Hermes/OVMS path. | Supported | 2026-05-26 | Initial local diagnostic run showed large latency differences, but cache state and repeated-run controls were not established. | Repeat testing only when tuning responsiveness becomes a priority. |
| Chapter 09 / tool calls | The current OVMS/parser path can return basic structured Hermes tool calls. | Supported | 2026-05-26 | Initial local calls succeeded for `read_file`, `skills_list`, and `session_search`; broad task reliability is not established. | Use for supervised testing; expand checks before unattended workflows. |
| Chapter 09 / unattended execution | The current local agent execution path is contained enough for unattended host-repository mutations. | Disproven | 2026-05-26 | Terminal execution is local and an enabled repo-hygiene task modified `~/CursiveOS`; the task was paused. | Require containment or an explicit approval boundary before re-enabling mutating automation. |
| Chapter 09 / Arc B70 performance | Imported throughput, model-comparison, power, and large-context performance claims are reliable for the local host. | Unvalidated | 2026-05-26 | Imported research and selected source review only; no controlled local benchmark. | Benchmark only claims needed for a runtime/model decision. |
| Chapter 08 / firmware interfaces | Linux/UEFI/Redfish/fwupd/flashrom expose the control surfaces described for firmware-management exploration. | Supported | 2026-05-30 | Source-backed review of Linux `efivarfs`, Linux `firmware-attributes`, DMTF Redfish BIOS/Settings/AttributeRegistry schemas, fwupd UEFI capsule flow, and existing flashrom-backed chapter material. Actual motherboard/platform coverage remains hardware-specific. | Test on target hardware before building control features; start with read-only inventory. |
| Chapters 03-06 / implementation claims | Imported optimization, tuning, and security recommendations are ready to apply as fixed CursiveOS defaults. | Unvalidated | 2026-05-26 | Earlier targeted review supported some mechanisms but did not establish all operational recommendations. | Validate individual claims when they are about to drive work. |
| Chapter 16 / network headline | The +450–900% loopback delta decomposes into ~2.6× from the CUBIC→BBR algorithm swap and ~3.5× (+246%) from CursiveOS buffer/qdisc tuning measured with BBR held constant (stack-delta benchmark). Both are real on high-BDP loopback; neither magnitude is yet established on a real path. | Supported | 2026-06-13 | Stack-delta run on founder rig: BBR-only 395.5 → BBR+our-stack 1367.5 Mbit/s, netem verified. Corrects the earlier "mostly just BBR" assumption — buffer tuning is the larger factor on high-BDP paths. Still loopback. | Keep the WAN-simulation qualifier; the stack-delta is the honest "our contribution" number for fitness; run real-path A/B to bound transfer (magnitude is path-BDP-dependent). |
| Chapter 16 / cold-start is hardware-scoped | The v0.8/v0.9c cold-start optimization gives ~−51% on the Ryzen 7 5700 + Arc A750 desktop but ~0% on the i5-11300H laptop. It must not be claimed as a universal gain. | Validated | 2026-06-13 | Two machines, multiple runs each; phase-context telemetry confirms governor changed to performance on AC on the laptop (not a confound). First empirical hardware-scoped-fitness instance for Chapter 10's evidence model. | Label cold-start gains by hardware class; build hardware-scoped fitness before any fleet-wide preset claim. v0.9c still safely replaces v0.8 on both machines (GPU pin is dead weight everywhere). |
| Chapter 16 / idle power comparability | Cross-machine idle-power deltas in CursiveRoot are not yet comparable because the harness reads physically different sources (RAPL package, GPU hwmon energy, instantaneous hwmon, turbostat) without recording which one in structured output. | Supported | 2026-06-11 | `read_watts` source-priority code; source identity only in stderr guard logs. Same-machine same-session deltas remain directionally useful. | Add `power_source` to structured results before pooling power data across machines; treat the v0.9 screen power term as same-machine evidence only. |

## Optional Supporting Records

Detailed records created before this compact status page remain available when
needed:

- `validation/notes/`
- `sources/extracted-source-index.md`
- `experiments/results/`

They are evidence archives, not mandatory workflow steps.
