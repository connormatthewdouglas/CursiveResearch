# Research Index

This index is the primary navigation page for the CursiveOS research corpus.
Chapters are living documents in strategic reading order (23 files, **00–22**
logical slots): measurement and organism architecture first, then literature and
platform depth, then historical strategy imports last.

Use [CORPUS_WORKFLOW.md](CORPUS_WORKFLOW.md) for intake and maintenance,
[VALIDATION.md](VALIDATION.md) for the status of important claims, and
[CHANGELOG.md](CHANGELOG.md) for the record of material edits.

**Paper library:** 25 peer-research intakes under `papers/` (see [papers/README.md](papers/README.md)).

**Organization decisions (merges/splits/order):** [sources/corpus-organization-decisions-2026-06-24.md](sources/corpus-organization-decisions-2026-06-24.md) — documents Ch03+Ch04 RSI merge, Ch07 split, strategic order, and five new chapter rationale.

## Reading Path

### Cohesive path (recommended for new agents)

1. [CORPUS_WORKFLOW.md](CORPUS_WORKFLOW.md) — intake, living-layer rule, cohesion checklist
2. [VALIDATION.md](VALIDATION.md) — what is validated, disproven, or open
3. [00 - Benchmark Schema](chapters/00-benchmark-schema-and-measurement-validity.md) — what harness numbers mean
4. [01 - Seed Organism](chapters/01-seed-organism-and-sensor-array.md) + [08 - Population Confirmation](chapters/08-population-confirmation-and-fleet-statistics.md) — evidence model and fleet statistics
5. [02 - Bitcoin-Native Economics](chapters/02-bitcoin-native-economics-and-proof-of-useful-optimization.md) + [12 - OSS Funding](chapters/12-open-source-funding-and-contributor-incentives.md) — incentives without token emissions
6. [05 - Measurement Daemon & NL Shell](chapters/05-measurement-daemon-and-natural-language-shell.md) + [06 - Mutation Safety](chapters/06-mutation-safety-and-permission-law.md) — trust boundaries
7. [03 - RSI Literature & Organism Synthesis](chapters/03-rsi-literature-and-organism-synthesis.md) — merged literature digest + organism framework
   - [03c - AlphaEvolve → Decentralized Evolution Mapping](chapters/03c-alphaevolve-decentralized-evolution-mapping.md) — the loop is validated at industrial scale; decentralizing the evaluator is the unsolved hard part
   - [03d - Verifying Decentralized Computation](chapters/03d-verifying-decentralized-computation.md) — the external prior art (replication/spot-checking, dispute games, TEE attestation, zk proofs, stake-weighted consensus) for the untrusted-evaluator frontier 03c names, and why CursiveOS can inherit only the statistical end of it
8. [07 - Gap Closure](chapters/07-main-repo-gap-closure.md) + [07b - Research Backlog](chapters/07b-research-backlog-and-pipeline.md) — what is closed vs what to research next
9. [19 - First Principles](chapters/19-first-principles-and-strategy.md) + [20 - Market](chapters/20-market-and-viability.md) — **read the living layer first**, then the DOCX import below it
10. [22 - Research Master](chapters/22-research-master.md) — March 2026 historical snapshot only

Chapters **19–22** preserve DOCX imports with living layers. Chapters **13–18** are platform and agent implementation leads constrained by **00**, **06**, and **VALIDATION.md**.

### Full chapter index (strategic order)

| # | Chapter | Topic | Use It For | Confidence |
| --- | --- | --- | --- | --- |
| 00 | [Benchmark Schema and Measurement Validity](chapters/00-benchmark-schema-and-measurement-validity.md) | Harness schema, per-channel validity, telemetry gaps | Interpreting CursiveRoot numbers honestly | Grounded in harness code (2026-06); fixes not all implemented |
| 01 | [Seed Organism and Sensor Array](chapters/01-seed-organism-and-sensor-array.md) | Phase 0 loop, sensors, population confirmation, fitness | Evidence model and selection pressure | Supported architecture; fleet calibration open |
| 02 | [Bitcoin-Native Economics](chapters/02-bitcoin-native-economics-and-proof-of-useful-optimization.md) | Layer 5 v3.3, no-token design, BTC contributor payouts | Current CursiveOS economic metabolism | Specified; real payments not deployed |
| 03 | [RSI Literature and Organism Synthesis](chapters/03-rsi-literature-and-organism-synthesis.md) | **Merged** peer-reviewed digest + organism framework (former Ch03+Ch04) | Verifier-grounded discovery, fitness framing, failure modes | Structured digest + intake synthesis |
| 03c | [AlphaEvolve → Decentralized Evolution Mapping](chapters/03c-alphaevolve-decentralized-evolution-mapping.md) | Maps AlphaEvolve's verifier-grounded loop onto a decentralized BTC-paid fleet; verifiable vs proprietary results; disanalogies | Why the loop is validated but evaluator decentralization is unsolved | Loop Validated at industrial scale; decentralization Unvalidated |
| 03d | [Verifying Decentralized Computation](chapters/03d-verifying-decentralized-computation.md) | Prior art for trusting untrusted compute: replication+spot-checking (Sarmenta/BOINC), dispute games (Truebit/Verde), TEE attestation, zk proofs, stake-weighted consensus (Bittensor); optimistic-vs-validity axis | The CS prior art for the untrusted-evaluator problem, and which techniques CursiveOS can actually use | Prior art Validated; transfer to hardware-scoped fitness Partly Supported |
| 05 | [Measurement Daemon and NL Shell](chapters/05-measurement-daemon-and-natural-language-shell.md) | Deterministic daemon vs probabilistic shell | Agent trust boundaries, containment, tool policy | Daemon specified; shell not implemented |
| 06 | [Mutation Safety and Permission Law](chapters/06-mutation-safety-and-permission-law.md) | Least-privilege law for self-mutation | Mutation-class → containment matrix | Research synthesis; gates not implemented |
| 07 | [Main Repo Gap Closure](chapters/07-main-repo-gap-closure.md) | Architecture → gap status (Gaps 1–5) | What main repo already answers | Current synthesis |
| 07b | [Research Backlog and Pipeline](chapters/07b-research-backlog-and-pipeline.md) | **Split** from former Ch07 — backlog + `RESEARCH_PIPELINE.md` lift | Next research targets and experiments | Current synthesis |
| 08 | [Population Confirmation and Fleet Statistics](chapters/08-population-confirmation-and-fleet-statistics.md) | N-rule, CV escalation, hardware-scoped fitness | Fleet truth without false positives | Partly Supported; multi-machine calibration open |
| 09 | [Network Transport and Congestion Control](chapters/09-network-transport-and-congestion-control.md) | BBR, BDP, loopback vs real-path | Network sensor interpretation | BBR win Validated on ≤1GbE loss; buffer magnitude Disproven |
| 10 | [Local LLM Inference Runtime](chapters/10-local-llm-inference-runtime-architecture.md) | Ollama, llama.cpp, daemon/shell split | Inference stack architecture | Supported direction; Arc B70 defaults Unvalidated |
| 11 | [Hardware Identity and Anti-Spoofing](chapters/11-hardware-identity-and-anti-spoofing.md) | Fingerprints, spoofing, independence inputs | Population confirmation integrity | Partly Supported; fleet logging open |
| 12 | [Open-Source Funding and Contributor Incentives](chapters/12-open-source-funding-and-contributor-incentives.md) | OSS funding models vs sensor-gated BTC | Complements Ch02; not tokenomics | External survey Supported; Ch02 authoritative for product |
| 13 | [Linux Kernel Optimization](chapters/13-linux-kernel-optimization.md) | Kernel tuning leads | Feature experiments | Mechanisms partly Supported; magnitudes need Ch00 harness |
| 14 | [GPU and Accelerator Tuning](chapters/14-gpu-and-accelerator-tuning.md) | AMD/Intel GPU behavior | Hardware-specific experiments | Partly Supported; per-platform validation required |
| 15 | [AI-Guided Tuning](chapters/15-ai-guided-tuning.md) | Automated tuning and agent loops | Literature + proposer test | Architecture Supported; CH05-BM-002 Unvalidated |
| 16 | [Security and Hardening](chapters/16-security-and-hardening.md) | External-threat Linux defense | Operational checklist | Partly Supported; see Ch06 for self-mutation |
| 17 | [Firmware and BIOS Control](chapters/17-firmware-and-bios-control.md) | UEFI, Redfish, firmware mutation | Whole-machine optimization surfaces | Interfaces Supported; platform testing required |
| 18 | [Local Agent: Arc B70](chapters/18-local-agent-arc-b70.md) | Hermes, OVMS, local agent stack | Workstation agent planning | Hermes context Validated; unattended mutation Disproven |
| 19 | [First Principles and Strategy](chapters/19-first-principles-and-strategy.md) | Thesis, moat, roadmap | Strategic framing; living layer corrects §2.1–2.2 | Strategic Supported; TCP import Disproven |
| 20 | [Market and Viability](chapters/20-market-and-viability.md) | DePIN market context | Background; living layer flags TEE/benchmark overclaims | Context Unvalidated; flagged passages Disproven |
| 21 | [Tokenomics and Incentives](chapters/21-tokenomics-and-incentives.md) | DePIN token models | Comparison only | Superseded by Ch02 for CursiveOS |
| 22 | [Research Master](chapters/22-research-master.md) | March 2026 repo snapshot | Historical context only | Superseded for architecture; see Ch00–07 |

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