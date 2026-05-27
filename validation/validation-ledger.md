# Research Validation Ledger

Purpose: track what research has been fact checked, when it was checked, what agent checked it, what sources were used, and what remains unresolved.

This ledger is the continuity layer for the corpus. Future agents should start here before validating claims so work does not restart from zero.

## Status Values

| Status | Meaning |
| --- | --- |
| `not started` | No validation pass has been performed. |
| `source extraction only` | External sources have been identified but claims have not been checked. |
| `in progress` | A validation pass has started but is incomplete. |
| `verified` | Material claims checked against strong sources and currently supported. |
| `partially verified` | Some claims supported; others need more evidence, correction, or narrower wording. |
| `triaged` | Broad classification pass completed, but not deep source validation. |
| `disputed` | Material claims conflict with strong evidence. |
| `stale` | Previously checked, but time-sensitive enough to require refresh. |
| `superseded` | Replaced by newer chapter, source, benchmark, or decision note. |

## Agent Naming

Use the model or agent identifier available at the time of validation. If unavailable, use a descriptive label.

Examples:

```text
GPT-5.5 Thinking / ChatGPT
Codex CLI
Human reviewer: <name>
```

## Validation Passes

| Date Checked | Agent / Reviewer | Scope | Status | Source Index IDs | Summary | Follow-up |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-05-26 | GPT-5.5 Thinking / ChatGPT | Created validation system scaffolding: source index, validation ledger, methodology upgrade | source extraction only | SRC-08-001 through SRC-08-005 | Established corpus governance for source extraction and claim validation. Extracted initial Chapter 08 source references. No full claim verification pass completed yet. | Validate Chapter 08 claims against primary sources; then extract/validate Chapter 03 and Chapter 05. |
| 2026-05-26 | GPT-5.5 Thinking / ChatGPT | Imported uploaded `Local Agent Setup for Arc B70.docx` into `chapters/09-local-agent-arc-b70.md` | not started | Pending SRC-09-* extraction | Converted uploaded DOCX into a corpus chapter, preserved source SHA-256, and registered the supplemental intake. No source extraction or validation pass completed yet. | Extract Chapter 09 sources into `sources/extracted-source-index.md`; validate Intel Arc Pro B70 hardware claims, llama.cpp SYCL claims, OpenVINO claims, model benchmark claims, and Hermes/OpenClaw ecosystem claims. |
| 2026-05-26 | GPT-5.5 Thinking / ChatGPT | Full first-pass validation of `chapters/08-firmware-and-bios-control.md` | supported with minor caveats | SRC-08-001 through SRC-08-005 | Core CursiveFirmware architecture is supported by primary sources: UEFI runtime services, Linux `efivarfs`, Linux `firmware-attributes`, Redfish BIOS schema, and flashrom docs. Main caveat is platform specificity; these sources validate control surfaces, not universal motherboard support. | Prototype `cursive-firmware-probe`; validate on real Dell/Lenovo/HP and BMC/Redfish systems; add real request/response examples. |
| 2026-05-26 | GPT-5.5 Thinking / ChatGPT | Targeted validation of highest-risk `chapters/09-local-agent-arc-b70.md` claims | partially verified | SRC-09-001 through SRC-09-009 | Broad local-agent architecture is supported: Intel Arc needs non-CUDA runtimes, llama.cpp SYCL exists, llama.cpp function-calling exists, OpenVINO 2025.3 has relevant LLM features. B70-specific performance/model/tool-calling claims remain unverified pending reproducible benchmarks. | Extract remaining works cited; inspect benchmark repo methodology; run `experiments/arc-b70-local-agent-benchmark-plan.md`; locate official Intel product docs. |
| 2026-05-26 | Codex / GPT-5 | Local deployment inspection and Hermes context/tool-envelope correction for `chapters/09-local-agent-arc-b70.md` | partially verified; local findings recorded | SRC-09-003 through SRC-09-005, SRC-09-010 | Restored imported source wording, appended a dated correction: current Hermes enforces a 64,000-token minimum and uses 65,536; smaller active tool/history payloads improved live tool-call responsiveness in a single local probe pass. Also identified non-contained local terminal execution and paused one mutating cron task. | Run repeated benchmark-plan probes, validate sandboxed execution, and resolve Intel GuC firmware warning before performance promotion. |
| 2026-05-26 | GPT-5.5 Thinking / ChatGPT | Targeted validation of `chapters/03-linux-kernel-optimization.md` | partially verified | SRC-03-001 through SRC-03-006 | Kernel features such as `sched_ext`, PREEMPT_RT in 6.12, fscrypt cipher modes, and zram sysfs attributes are supported. Exact speedup numbers, kernel-version projections, and inference-specific performance extrapolations remain unverified pending local benchmarks. | Extract remaining Chapter 03 sources; add upstream commit references; run `experiments/kernel-inference-optimization-benchmark-plan.md`; amend chapter with verified findings after local tests. |
| 2026-05-26 | GPT-5.5 Thinking / ChatGPT | Targeted validation of `chapters/05-ai-guided-tuning.md` | partially verified | SRC-05-001 through SRC-05-008 | Core architecture is supported: LLM/RL/search-based OS tuning is an active research line. SchedCP, OS-R1, PolicySmith, SemaTune, and Fork-Explore-Commit are relevant leads. Performance numbers, maturity/license claims, costs, and recommended ranking remain provisional. SemaTune should supplement the older always-on tuning framing. | Inspect repos for license/activity/reproducibility; validate AutoOS separately; run `experiments/ai-guided-tuning-loop-validation-plan.md`; amend Chapter 05 with updated SemaTune note. |
| 2026-05-26 | GPT-5.5 Thinking / ChatGPT | Targeted validation of `chapters/04-gpu-and-accelerator-tuning.md` | partially verified with significant caveats | SRC-04-001 through SRC-04-009 in `sources/chapter-04-selected-sources.md` | Broad mechanisms are supported: AMDGPU controls, sched_ext, hugepages/THP, Kyber tunables, and GPU virtualization ecosystems exist. Specific RX 580 voltage tables, consumer GPU SR-IOV generalizations, hugepage performance claims, Kyber percentages, and Intel Arc power-control details remain unverified and hardware-specific. | Merge selected sources into canonical source index; run `experiments/gpu-accelerator-tuning-validation-plan.md`; add validation caveats to Chapter 04; validate LACT/scx/NUMA/RDMA claims separately. |
| 2026-05-26 | GPT-5.5 Thinking / ChatGPT | Targeted validation of `chapters/06-security-and-hardening.md` | partially verified with safety-critical caveats | SRC-06-001 through SRC-06-014 in `sources/chapter-06-selected-sources.md` | Broad defense-in-depth architecture is supported. Absolute claims around CrowdSec, fwknop/SPA, Docker insufficiency, and universal kernel hardening presets require softer policy-tier wording and deployment validation. | Run `experiments/security-hardening-validation-plan.md`; create CursiveOS-specific hardening baseline; merge selected sources into canonical source index. |
| 2026-05-26 | GPT-5.5 Thinking / ChatGPT | Broad triage of Chapters 00, 01, 02, and 07 | triaged | See `validation/notes/2026-05-26-remaining-corpus-triage-validation.md` | Chapter 00 is historical/superseded; Chapter 01 is strategic thesis material; Chapter 02 is stale/time-sensitive market research; Chapter 07 needs protocol-level tokenomics validation. | Use `validation/notes/2026-05-26-ch02-market-revalidation-plan.md` and `validation/notes/2026-05-26-ch07-tokenomics-revalidation-plan.md`; convert Chapter 01 into decision records. |
| 2026-05-26 | GPT-5.5 Thinking / ChatGPT | Deeper validation of `chapters/02-market-and-viability.md` | partially verified; market numbers date-sensitive | SRC-02-001 through SRC-02-010 in `sources/chapter-02-selected-sources.md` | Broad market thesis survives: mining is industrial and margin-sensitive, miners are exploring AI/HPC, DePIN/local AI broaden the opportunity, and OS/network tuning matters. Numeric market values, Bittensor/io.net/project statuses, BBR speedup figures, ASIC comparisons, and profitability claims must be refreshed before use. | Extract remaining sources; add date-stamped mining dashboards; create market-positioning decision record. |
| 2026-05-26 | GPT-5.5 Thinking / ChatGPT | Deeper validation of `chapters/07-tokenomics-and-incentives.md` | partially verified; protocol-source validation started | SRC-07-001 through SRC-07-010 in `sources/chapter-07-selected-sources.md` | High-level tokenomics direction is supported: avoid pure inflation, use stable/customer-friendly pricing, tie rewards to verified value, and link burns/rewards to real demand. Helium mechanics are strongest validated source; Render/Bittensor/io.net/Hivemapper/Grass need deeper official-doc and dashboard validation. | Resolve original numeric citations; extract protocol proposal details; create contributor-incentive decision record before any token design. |
| 2026-05-26 | GPT-5.5 Thinking / ChatGPT | Strategy validation of `chapters/01-first-principles-and-strategy.md` | validated as strategic thesis | See `validation/notes/2026-05-26-ch01-first-principles-strategy-validation.md` | Chapter 01 is internally coherent and useful, but should become decision records rather than empirical fact claims. Data alone is not the moat; measurement-before-optimization and speed of validated iteration are strong operating principles. | Create decision records under `decisions/`. |
| 2026-05-26 | GPT-5.5 Thinking / ChatGPT | Supersession review of `chapters/00-research-master.md` | superseded / historical snapshot | See `validation/notes/2026-05-26-ch00-research-master-supersession-note.md` | Chapter 00 is valuable project history but should not be used as current technical truth. Later topic chapters and validation notes supersede its claims. | Add top-of-chapter status note in future cleanup. |

## Chapter Validation Matrix

| Chapter | Last Checked | Last Agent / Reviewer | Current Status | Source Extraction | Validation Notes |
| --- | --- | --- | --- | --- | --- |
| `chapters/00-research-master.md` | 2026-05-26 | GPT-5.5 Thinking / ChatGPT | superseded / historical snapshot | not required unless claim is revived | See `validation/notes/2026-05-26-ch00-research-master-supersession-note.md`. |
| `chapters/01-first-principles-and-strategy.md` | 2026-05-26 | GPT-5.5 Thinking / ChatGPT | validated as strategic thesis | not applicable | See `validation/notes/2026-05-26-ch01-first-principles-strategy-validation.md`; convert key points into decision records. |
| `chapters/02-market-and-viability.md` | 2026-05-26 | GPT-5.5 Thinking / ChatGPT | partially verified; market data refresh required | selected high-priority sources extracted separately | See `validation/notes/2026-05-26-ch02-market-viability-validation.md`; selected sources: `sources/chapter-02-selected-sources.md`. |
| `chapters/03-linux-kernel-optimization.md` | 2026-05-26 | GPT-5.5 Thinking / ChatGPT | partially verified | selected high-priority sources extracted | See `validation/notes/2026-05-26-ch03-linux-kernel-optimization-validation.md`; benchmark plan: `experiments/kernel-inference-optimization-benchmark-plan.md`. |
| `chapters/04-gpu-and-accelerator-tuning.md` | 2026-05-26 | GPT-5.5 Thinking / ChatGPT | partially verified with significant caveats | selected high-priority sources extracted separately | See `validation/notes/2026-05-26-ch04-gpu-accelerator-tuning-validation.md`; validation plan: `experiments/gpu-accelerator-tuning-validation-plan.md`; selected sources: `sources/chapter-04-selected-sources.md`. |
| `chapters/05-ai-guided-tuning.md` | 2026-05-26 | GPT-5.5 Thinking / ChatGPT | partially verified | selected high-priority sources extracted | See `validation/notes/2026-05-26-ch05-ai-guided-tuning-validation.md`; validation plan: `experiments/ai-guided-tuning-loop-validation-plan.md`. |
| `chapters/06-security-and-hardening.md` | 2026-05-26 | GPT-5.5 Thinking / ChatGPT | partially verified with safety-critical caveats | selected high-priority sources extracted separately | See `validation/notes/2026-05-26-ch06-security-hardening-validation.md`; validation plan: `experiments/security-hardening-validation-plan.md`; selected sources: `sources/chapter-06-selected-sources.md`. |
| `chapters/07-tokenomics-and-incentives.md` | 2026-05-26 | GPT-5.5 Thinking / ChatGPT | partially verified; protocol-source validation incomplete | selected high-priority sources extracted separately | See `validation/notes/2026-05-26-ch07-tokenomics-incentives-validation.md`; selected sources: `sources/chapter-07-selected-sources.md`. |
| `chapters/08-firmware-and-bios-control.md` | 2026-05-26 | GPT-5.5 Thinking / ChatGPT | supported with minor caveats | complete for current chapter | See `validation/notes/2026-05-26-ch08-firmware-bios-control-validation.md`. |
| `chapters/09-local-agent-arc-b70.md` | 2026-05-26 | Codex / GPT-5 | partially verified; local deployment inspection added | selected high-priority sources extracted; SRC-09-010 registered | See `validation/notes/2026-05-26-ch09-arc-b70-targeted-validation.md` and `validation/notes/2026-05-26-ch09-local-hermes-deployment-inspection.md`; benchmark plan: `experiments/arc-b70-local-agent-benchmark-plan.md`. Full works-cited extraction remains open. |

## Open Validation Work Queue

### P0

1. Convert validated/partially validated technical spine into decision records and prototype plans.
2. Create decision records from Chapter 01: data alone is not the moat, measurement-before-optimization, early contributor incentive signal, speed of validated iteration.
3. Inspect SchedCP, OS-R1, PolicySmith, AutoOS, and SemaTune repos/papers for license, activity, installability, and reproducibility.
4. Extract and validate `chapters/09-local-agent-arc-b70.md` fully because it informs immediate local-agent and home-rack hardware planning.
5. Convert validated Chapter 08 findings into an experiment/prototype plan for `cursive-firmware-probe`.

### P1

1. Run or prepare `experiments/gpu-accelerator-tuning-validation-plan.md` and merge Chapter 04 selected sources into the canonical source index.
2. Run or prepare `experiments/security-hardening-validation-plan.md` and create a CursiveOS-specific hardening baseline.
3. Extract remaining `chapters/03-linux-kernel-optimization.md` sources and run the kernel inference benchmark plan.
4. Resolve Chapter 07 protocol citations and create contributor incentive design record.
5. Add an internal benchmark evidence directory or link to CursiveRoot benchmark exports.

### P2

1. Refresh Chapter 02 market data whenever used externally.
2. Track protocol changes for Chapter 07 before any token/economic decision.
3. Add top-of-chapter status caveats to Chapters 00, 01, 02, and 07.

## Validation Note Template

When validating a section or chapter, append a note to the relevant chapter or create a file under `validation/notes/` using this structure:

```markdown
# Validation Note: <chapter or claim group>

Date checked: YYYY-MM-DD
Agent / reviewer: <name>
Scope: <specific section, claim group, or chapter>
Status: supported | partially supported | disputed | unverified | stale
Source IDs: SRC-XX-001, SRC-XX-002

## Claims Checked

| Claim ID | Claim | Status | Evidence | Notes / Required Rewrite |
| --- | --- | --- | --- | --- |
| CL-XX-001 | ... | supported | SRC-XX-001 | ... |

## Implications for CursiveOS

- ...

## Follow-up

- ...
```
