# Research Index

This index is the primary navigation page for the CursiveOS research corpus.
Chapters are living documents: preserve the uploaded originals in
`sources/original-docx/`, but edit chapter guidance when better evidence or the
current deployment requires a correction.

Use [CORPUS_WORKFLOW.md](CORPUS_WORKFLOW.md) for intake and maintenance,
[VALIDATION.md](VALIDATION.md) for the status of important claims, and
[CHANGELOG.md](CHANGELOG.md) for the record of material edits.

## Reading Path

### Cohesive path (recommended for new agents)

Read in this order when joining the corpus or reconciling early imports with current truth:

1. [CORPUS_WORKFLOW.md](CORPUS_WORKFLOW.md) — intake, living-layer rule, cohesion checklist
2. [VALIDATION.md](VALIDATION.md) — what is validated, disproven, or open
3. [16 - Benchmark Schema](chapters/16-benchmark-schema-and-measurement-validity.md) — what numbers actually mean
4. [10 - Seed Organism](chapters/10-seed-organism-and-sensor-array.md) + [11 - Economics](chapters/11-bitcoin-native-economics-and-proof-of-useful-optimization.md) — evidence and incentives
5. [01 - First Principles](chapters/01-first-principles-and-strategy.md) + [02 - Market](chapters/02-market-and-viability.md) — **read the living layer first**, then the import below it
6. [13 - Gap Closure](chapters/13-main-repo-gap-closure-and-research-backlog.md) — what to research or build next

Chapters 00 and 07 are historical/comparison material. Chapters 03–06 are technical leads constrained by Chapter 16 and 17.

### Full chapter index

| Chapter | Topic | Use It For | Current Confidence |
| --- | --- | --- | --- |
| [00 - Research Master](chapters/00-research-master.md) | Collected snapshot and repo observations | Historical March 2026 context only | Superseded for architecture; see Ch10–13 |
| [01 - First Principles and Strategy](chapters/01-first-principles-and-strategy.md) | Foundational thesis, moat, roadmap implications | Moat/incentive framing; living layer corrects §2.1–2.2 | Strategic Supported; TCP import example Disproven |
| [02 - Market and Viability](chapters/02-market-and-viability.md) | Crypto/decentralized compute market, system thesis, positioning | Market background; living layer flags TEE/benchmark overclaims | Context Unvalidated; flagged import passages Disproven |
| [03 - Linux Kernel Optimization](chapters/03-linux-kernel-optimization.md) | Kernel changes and system tuning | Feature leads; magnitudes need Ch16 harness | Mechanisms partly Supported; perf Unvalidated |
| [04 - GPU and Accelerator Tuning](chapters/04-gpu-and-accelerator-tuning.md) | AMD/Intel GPU behavior and tuning | Hardware-specific experiments | Partly Supported; per-platform validation required |
| [05 - AI-Guided Tuning](chapters/05-ai-guided-tuning.md) | Automated tuning and agent approaches | Literature survey; proposer test pending | Architecture Supported; CH05-BM-002 Unvalidated |
| [06 - Security and Hardening](chapters/06-security-and-hardening.md) | Linux security and operational defense | External-threat checklist; see Ch17 for self-mutation | Partly Supported; deployment validation required |
| [07 - Tokenomics and Incentives](chapters/07-tokenomics-and-incentives.md) | DePIN models and incentive mechanisms | DePIN comparison only | Superseded by Chapter 11 for CursiveOS economics |
| [08 - Firmware and BIOS Control](chapters/08-firmware-and-bios-control.md) | UEFI, BIOS, BMC/Redfish, boot control, firmware mutation | Whole-machine self-optimization architecture | Core interfaces supported; platform-specific testing required |
| [09 - Local Agent Setup for Arc B70](chapters/09-local-agent-arc-b70.md) | Arc Pro B70 local agent stack, Hermes, model/tool behavior | Current local-agent implementation planning | Current Hermes context constraint validated locally; performance remains partly supported or unvalidated |
| [10 - Seed Organism and Sensor Array](chapters/10-seed-organism-and-sensor-array.md) | Phase 0 organism loop, sensors, population confirmation, truth model | Evidence model, selection pressure, CursiveRoot fitness logic | Current project architecture from main repo; implementation still maturing |
| [11 - Bitcoin-Native Economics and Proof of Useful Optimization](chapters/11-bitcoin-native-economics-and-proof-of-useful-optimization.md) | Layer 5 v3.3 economics, no-token design, BTC contributor payouts | Contributor incentives and economic metabolism | Current project architecture from main repo; specified, not yet deployed for real payments |
| [12 - Measurement Daemon and Natural-Language Shell](chapters/12-measurement-daemon-and-natural-language-shell.md) | Deterministic measurement daemon vs probabilistic shell agent | Agent trust boundaries, operator interface, prompt-injection risk, tool policy, and containment | Daemon specified; shell safety research pass added; shell not implemented |
| [13 - Main Repo Gap Closure and Research Backlog](chapters/13-main-repo-gap-closure-and-research-backlog.md) | Mapping main repo architecture to research gaps and next research targets | Gap closure, backlog prioritization, implementation research planning | Current synthesis; use to decide next corpus expansion |
| [14 - Peer-Reviewed Research: Recursive Self-Improvement and Agentic Evolution](chapters/14-peer-reviewed-research-recursive-self-improvement-and-agentic-evolution.md) | Published research on self-improving agents, evolutionary coding, evaluator-grounded discovery, and benchmark discipline | Foundational literature for software-organism research | Structured digest; source-level review started, not exhaustive |
| [15 - Foundations of Software Organisms: RSI Critical Synthesis](chapters/15-foundations-of-software-organisms-rsi-critical-synthesis.md) | Critical synthesis of the uploaded software-organisms/self-improvement research packet | Software-organism theory, verifier/fitness framing, failure modes, and adoption/avoidance lessons | Substantial intake synthesis; some source claims still need source-level validation |
| [16 - Benchmark Schema and Measurement Validity](chapters/16-benchmark-schema-and-measurement-validity.md) | What the deployed benchmark suite actually measures, per-channel validity, schema gaps, next telemetry | Interpreting CursiveRoot numbers honestly; prioritizing measurement improvements | Grounded in current harness code and live data (2026-06-11); recommendations not yet implemented |
| [17 - Mutation Safety and Permission Law](chapters/17-mutation-safety-and-permission-law.md) | Least-privilege permission law for the organism's own self-mutation; mutation-class → containment-primitive matrix; daemon/shell separation of duties | Deciding what agents/daemons/contributors may change and which mechanism enforces each gate | Research synthesis grounded in external security literature; gates specified, not yet implemented |

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
