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
| Chapter 09 / Hermes context | The inspected local Hermes build requires a configured context of at least 64,000 tokens; the deployed model config uses 65,536. | Validated | 2026-05-26 | Local Hermes source and `~/.hermes/config.yaml`; valid only for the inspected deployment/version. | Keep Hermes configuration at 64k or higher. |
| Chapter 09 / responsiveness | Reducing active prompt, tool-schema, and retained-history payloads improves responsiveness in the current Hermes/OVMS path. | Supported | 2026-05-26 | Initial local diagnostic run showed large latency differences, but cache state and repeated-run controls were not established. | Repeat testing only when tuning responsiveness becomes a priority. |
| Chapter 09 / tool calls | The current OVMS/parser path can return basic structured Hermes tool calls. | Supported | 2026-05-26 | Initial local calls succeeded for `read_file`, `skills_list`, and `session_search`; broad task reliability is not established. | Use for supervised testing; expand checks before unattended workflows. |
| Chapter 09 / unattended execution | The current local agent execution path is contained enough for unattended host-repository mutations. | Disproven | 2026-05-26 | Terminal execution is local and an enabled repo-hygiene task modified `~/CursiveOS`; the task was paused. | Require containment or an explicit approval boundary before re-enabling mutating automation. |
| Chapter 09 / Arc B70 performance | Imported throughput, model-comparison, power, and large-context performance claims are reliable for the local host. | Unvalidated | 2026-05-26 | Imported research and selected source review only; no controlled local benchmark. | Benchmark only claims needed for a runtime/model decision. |
| Chapter 08 / firmware interfaces | Linux/UEFI/Redfish/flashrom expose the control surfaces described for firmware-management exploration. | Supported | 2026-05-26 | Earlier review against primary documentation; actual motherboard/platform coverage remains hardware-specific. | Test on target hardware before building control features. |
| Chapters 03-06 / implementation claims | Imported optimization, tuning, and security recommendations are ready to apply as fixed CursiveOS defaults. | Unvalidated | 2026-05-26 | Earlier targeted review supported some mechanisms but did not establish all operational recommendations. | Validate individual claims when they are about to drive work. |

## Optional Supporting Records

Detailed records created before this compact status page remain available when
needed:

- `validation/notes/`
- `sources/extracted-source-index.md`
- `experiments/results/`

They are evidence archives, not mandatory workflow steps.
