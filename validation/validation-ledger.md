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
| 2026-05-26 | GPT-5.5 Thinking / ChatGPT | Targeted validation of `chapters/03-linux-kernel-optimization.md` | partially verified | SRC-03-001 through SRC-03-006 | Kernel features such as `sched_ext`, PREEMPT_RT in 6.12, fscrypt cipher modes, and zram sysfs attributes are supported. Exact speedup numbers, kernel-version projections, and inference-specific performance extrapolations remain unverified pending local benchmarks. | Extract remaining Chapter 03 sources; add upstream commit references; run `experiments/kernel-inference-optimization-benchmark-plan.md`; amend chapter with verified findings after local tests. |
| 2026-05-26 | GPT-5.5 Thinking / ChatGPT | Targeted validation of `chapters/05-ai-guided-tuning.md` | partially verified | SRC-05-001 through SRC-05-008 | Core architecture is supported: LLM/RL/search-based OS tuning is an active research line. SchedCP, OS-R1, PolicySmith, SemaTune, and Fork-Explore-Commit are relevant leads. Performance numbers, maturity/license claims, costs, and recommended ranking remain provisional. SemaTune should supplement the older always-on tuning framing. | Inspect repos for license/activity/reproducibility; validate AutoOS separately; run `experiments/ai-guided-tuning-loop-validation-plan.md`; amend Chapter 05 with updated SemaTune note. |

## Chapter Validation Matrix

| Chapter | Last Checked | Last Agent / Reviewer | Current Status | Source Extraction | Validation Notes |
| --- | --- | --- | --- | --- | --- |
| `chapters/00-research-master.md` | — | — | not started | not started | Snapshot chapter; likely should be decomposed or superseded by topic chapters. |
| `chapters/01-first-principles-and-strategy.md` | — | — | not started | not started | Needs strategic evidence and internal benchmark cross-reference. |
| `chapters/02-market-and-viability.md` | — | — | not started | not started | Market, protocol, and project-status claims are highly time-sensitive. |
| `chapters/03-linux-kernel-optimization.md` | 2026-05-26 | GPT-5.5 Thinking / ChatGPT | partially verified | selected high-priority sources extracted | See `validation/notes/2026-05-26-ch03-linux-kernel-optimization-validation.md`; benchmark plan: `experiments/kernel-inference-optimization-benchmark-plan.md`. |
| `chapters/04-gpu-and-accelerator-tuning.md` | — | — | not started | not started | Needs hardware validation on target GPUs and source validation for driver claims. |
| `chapters/05-ai-guided-tuning.md` | 2026-05-26 | GPT-5.5 Thinking / ChatGPT | partially verified | selected high-priority sources extracted | See `validation/notes/2026-05-26-ch05-ai-guided-tuning-validation.md`; validation plan: `experiments/ai-guided-tuning-loop-validation-plan.md`. |
| `chapters/06-security-and-hardening.md` | — | — | not started | not started | Security recommendations need careful freshness review. |
| `chapters/07-tokenomics-and-incentives.md` | — | — | not started | not started | Needs protocol-doc and current-tokenomics verification. |
| `chapters/08-firmware-and-bios-control.md` | 2026-05-26 | GPT-5.5 Thinking / ChatGPT | supported with minor caveats | complete for current chapter | See `validation/notes/2026-05-26-ch08-firmware-bios-control-validation.md`. |
| `chapters/09-local-agent-arc-b70.md` | 2026-05-26 | GPT-5.5 Thinking / ChatGPT | partially verified | selected high-priority sources extracted | See `validation/notes/2026-05-26-ch09-arc-b70-targeted-validation.md`; benchmark plan: `experiments/arc-b70-local-agent-benchmark-plan.md`. Full works-cited extraction remains open. |

## Open Validation Work Queue

### P0

1. Inspect SchedCP, OS-R1, PolicySmith, AutoOS, and SemaTune repos/papers for license, activity, installability, and reproducibility.
2. Extract and validate `chapters/09-local-agent-arc-b70.md` fully because it informs immediate local-agent and home-rack hardware planning.
3. Extract remaining `chapters/03-linux-kernel-optimization.md` sources and run the kernel inference benchmark plan.
4. Convert validated Chapter 08 findings into an experiment/prototype plan for `cursive-firmware-probe`.

### P1

1. Extract and validate `chapters/06-security-and-hardening.md` before using it for deployment hardening.
2. Extract and validate `chapters/04-gpu-and-accelerator-tuning.md` against actual hardware and driver documentation.
3. Add an internal benchmark evidence directory or link to CursiveRoot benchmark exports.

### P2

1. Extract and validate `chapters/02-market-and-viability.md` against current DePIN, Bittensor, io.net, Render, and mining data.
2. Extract and validate `chapters/07-tokenomics-and-incentives.md` against official protocol docs and current governance changes.
3. Convert validated findings into decision records.

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
