# Research Index

This index is the primary navigation page for the private CursiveOS research
corpus. Chapters are living documents: preserve the uploaded originals in
`sources/original-docx/`, but edit chapter guidance when better evidence or the
current deployment requires a correction.

Use [VALIDATION.md](VALIDATION.md) for the status of important claims and
[CHANGELOG.md](CHANGELOG.md) for the record of material edits.

## Reading Path

| Chapter | Topic | Use It For | Current Confidence |
| --- | --- | --- | --- |
| [00 - Research Master](chapters/00-research-master.md) | Collected snapshot and repo observations | Orientation and historical context | Mostly imported; review before use |
| [01 - First Principles and Strategy](chapters/01-first-principles-and-strategy.md) | Foundational thesis, moat, roadmap implications | Product and strategic framing | Mostly imported; review before use |
| [02 - Market and Viability](chapters/02-market-and-viability.md) | Crypto/decentralized compute market, system thesis, positioning | Viability analysis and competitive context | Unvalidated where decisions depend on current market facts |
| [03 - Linux Kernel Optimization](chapters/03-linux-kernel-optimization.md) | Kernel changes and system tuning | Technical opportunity discovery | Mechanisms partly supported; performance needs testing |
| [04 - GPU and Accelerator Tuning](chapters/04-gpu-and-accelerator-tuning.md) | AMD/Intel GPU behavior and tuning | Hardware-specific experiments | Partly supported; hardware claims need testing |
| [05 - AI-Guided Tuning](chapters/05-ai-guided-tuning.md) | Automated tuning and agent approaches | Architecture and research backlog | Partly supported; implementation claims remain provisional |
| [06 - Security and Hardening](chapters/06-security-and-hardening.md) | Linux security and operational defense | Threat model and deployment hardening | Partly supported; deployment validation required |
| [07 - Tokenomics and Incentives](chapters/07-tokenomics-and-incentives.md) | DePIN models and incentive mechanisms | Economic design research | Superseded for CursiveOS design by Chapter 11; useful comparison material |
| [08 - Firmware and BIOS Control](chapters/08-firmware-and-bios-control.md) | UEFI, BIOS, BMC/Redfish, boot control, firmware mutation | Whole-machine self-optimization architecture | Core interfaces supported; platform-specific testing required |
| [09 - Local Agent Setup for Arc B70](chapters/09-local-agent-arc-b70.md) | Arc Pro B70 local agent stack, Hermes, model/tool behavior | Current local-agent implementation planning | Current Hermes context constraint validated locally; performance remains partly supported or unvalidated |
| [10 - Seed Organism and Sensor Array](chapters/10-seed-organism-and-sensor-array.md) | Phase 0 organism loop, sensors, population confirmation, truth model | Evidence model, selection pressure, CursiveRoot fitness logic | Current project architecture from main repo; implementation still maturing |
| [11 - Bitcoin-Native Economics and Proof of Useful Optimization](chapters/11-bitcoin-native-economics-and-proof-of-useful-optimization.md) | Layer 5 v3.3 economics, no-token design, BTC contributor payouts | Contributor incentives and economic metabolism | Current project architecture from main repo; specified, not yet deployed for real payments |
| [12 - Measurement Daemon and Natural-Language Shell](chapters/12-measurement-daemon-and-natural-language-shell.md) | Deterministic measurement daemon vs probabilistic shell agent | Agent trust boundaries and v1.0 operator interface | Daemon specified; shell architectural sketch, not implemented |
| [13 - Main Repo Gap Closure and Research Backlog](chapters/13-main-repo-gap-closure-and-research-backlog.md) | Mapping main repo architecture to research gaps and next research targets | Gap closure, backlog prioritization, implementation research planning | Current synthesis; use to decide next corpus expansion |
| [14 - Peer-Reviewed Research: Recursive Self-Improvement and Agentic Evolution](chapters/14-peer-reviewed-research-recursive-self-improvement-and-agentic-evolution.md) | Published research on self-improving agents, evolutionary coding, evaluator-grounded discovery, and benchmark discipline | Foundational literature for software-organism research | Structured digest; source-level review started, not exhaustive |

## Confidence Labels

| Label | Meaning |
| --- | --- |
| `Unvalidated` | A useful lead or imported claim that has not been checked sufficiently. |
| `Supported` | Evidence points in the claim's direction, but it is not strong enough for an irreversible or broad decision. |
| `Validated` | Confirmed sufficiently for the stated local decision or implementation use. |
| `Disproven` | Evidence shows the claim does not apply or is wrong for the stated use. |
| `Superseded` | Replaced by newer guidance or a changed environment. |

## Practical Boundary

Do not confuse readability with confidence. Chapters should say what the team
currently believes is useful, and `VALIDATION.md` should identify important
remaining uncertainty. Routine changes do not require a separate source ID,
validation note, or ledger entry; add detailed evidence only when it will help
repeat, audit, or reverse a consequential decision.
