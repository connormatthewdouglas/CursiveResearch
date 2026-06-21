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

## Flagged for Review

Items an agent or contributor spotted as wrong, unsupported, outdated, or
needing a human/agent decision — but did **not** edit directly. Newest on top.
When a flag is resolved, delete its row (git history preserves it).

| Date | Item | Location (file §) | Issue | Suggested action | Status |
| --- | --- | --- | --- | --- | --- |
| 2026-06-21 | Covenant-72B's 67.1 MMLU described as "competitive with early GPT-4-class models," cited as evidence "decentralized compute can achieve data-center-level results." | `chapters/02-market-and-viability.md` § "The Bittensor (TAO) Ecosystem: Performance Benchmarks" → "Model Benchmarks: Covenant-72B" (and the summary-table "Average Model MMLU" row). | Overstated, contradicts external evidence. GPT-4 (2023) scored 86.4% on MMLU; 67.1 is ~19 pts lower, at the Llama-2-70B (~68.9%) / GPT-3.5 (~70%) tier. Covenant-72B's *own* reported peer set is LLaMA-2-70B (65.6) and LLM360 K2 (65.5) — 2023-era open base models, not GPT-4. The decentralized-training feat (72B, 1.1T tokens, ~70 commodity-hardware contributors) is real and not disputed; only the "GPT-4-class / data-center-level" framing is. | Do not edit the preserved-DOCX wording in place. Treat the "GPT-4-class" comparison as Disproven and do not reuse it in external/marketing material; when Chapter 02 is next revised, rephrase to the Llama-2-70B / open-base-model framing. Evidence: `validation/notes/2026-06-21-ch02-covenant-72b-gpt4-class-overstatement-challenge.md`. | Open |

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
| Chapter 16 / network headline | On a real ≤1GbE NIC under loss, the entire network win is the CUBIC→BBR swap (+1875%); the CursiveOS buffer/qdisc stack adds ~0% (−0.7%). The loopback "+246% from our tuning" is a loopback BDP artifact and does NOT transfer to ordinary links. | Validated | 2026-06-16 | Real-path A/B (Stardust→2nd machine, real 1GbE, netem 50ms+0.5% loss): CUBIC 43.1, BBR 851.1, BBR+stack 845.0 Mbit/s. Supersedes the 2026-06-13 loopback decomposition. Buffers may still matter on >1Gbit/high-latency WAN (untested). | Public claim = "switch to BBR" (real, large under loss). Do NOT credit buffer tuning with a magnitude. Treat loopback stack-delta as mechanism-only. Test a genuine high-BDP link before any buffer claim. |
| Chapter 16 / measurement noise floor | Per-channel within-machine CV (6 identical v0.9 runs): cold-start 0.002 (rock-solid), network 0.192 (above 0.15 → needs CV-escalation; magnitude unreliable), sustained sign-unstable (signal<noise), idle-power(CPU) 0.83 (near-random). Selection should use per-channel confirmation counts, not one global N. | Validated | 2026-06-16 | 6× v0.9 on Stardust. First fleet-variance data for Chapter 10's confirmation model. | Trust cold-start at ~1 confirmation; require CV-escalation for network and never quote its magnitude; do NOT gate on sustained-single-stream or idle-power until measurement improves. |
| Chapter 16 / GPU power now measurable | The v1.4.3 GPU-side sensor reads the Arc A750 energy counter (~37 W idle); total power (CPU+GPU ≈ 42 W package) is now visible, closing the §2.2 CPU-package-only blindspot on this hardware. | Validated | 2026-06-16 | run_detail_bundles structured_telemetry.gpu_power, source hwmon4/energy1_input; confirmed by Phase D probe. | Use total power for any GPU-pin/power claim. |
| Chapter 16 / GPU pin idle cost ≈ 0 | The v0.8 Arc GPU frequency pin costs ~0 W at idle (42.15 unpinned vs 42.16 pinned, reproduced). v0.9 drops it on parsimony grounds, not power. A750 idle is static-dominated; load-time power untested. | Validated | 2026-06-16 | Phase D total-power probe, 12 settled samples ×2 reps. | Do not claim v0.9 saves power vs v0.8; the win is fewer inert knobs. Test load-time power before any load-power claim. |
| Chapter 16 / idle-power noise is sampling | The CV 0.83 idle-power noise is a sampling artifact (sampling during the post-benchmark thermal tail), NOT inherent. Settled true-idle sampling gives CV ≈ 0.01. | Validated | 2026-06-16 | Phase D probe: CPU 5.49/5.49/5.46, GPU 36.66/36.67/36.66 across runs with 2 s settle + 12 samples. | Add settle + more samples before the harness idle capture (done); idle power becomes a usable selection channel once sampled correctly. |
| Chapter 16 / cold-start is hardware-scoped | The v0.8/v0.9c cold-start optimization gives ~−51% on the Ryzen 7 5700 + Arc A750 desktop but ~0% on the i5-11300H laptop. It must not be claimed as a universal gain. | Validated | 2026-06-13 | Two machines, multiple runs each; phase-context telemetry confirms governor changed to performance on AC on the laptop (not a confound). First empirical hardware-scoped-fitness instance for Chapter 10's evidence model. | Label cold-start gains by hardware class; build hardware-scoped fitness before any fleet-wide preset claim. v0.9c still safely replaces v0.8 on both machines (GPU pin is dead weight everywhere). |
| Chapter 16 / idle power comparability | Cross-machine idle-power deltas in CursiveRoot are not yet comparable because the harness reads physically different sources (RAPL package, GPU hwmon energy, instantaneous hwmon, turbostat) without recording which one in structured output. | Supported | 2026-06-11 | `read_watts` source-priority code; source identity only in stderr guard logs. Same-machine same-session deltas remain directionally useful. | Add `power_source` to structured results before pooling power data across machines; treat the v0.9 screen power term as same-machine evidence only. |

## Optional Supporting Records

Detailed records created before this compact status page remain available when
needed:

- `validation/notes/`
- `sources/extracted-source-index.md`
- `experiments/results/`

They are evidence archives, not mandatory workflow steps.
