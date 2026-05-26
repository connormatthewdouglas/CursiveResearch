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

## Chapter Validation Matrix

| Chapter | Last Checked | Last Agent / Reviewer | Current Status | Source Extraction | Validation Notes |
| --- | --- | --- | --- | --- | --- |
| `chapters/00-research-master.md` | — | — | not started | not started | Snapshot chapter; likely should be decomposed or superseded by topic chapters. |
| `chapters/01-first-principles-and-strategy.md` | — | — | not started | not started | Needs strategic evidence and internal benchmark cross-reference. |
| `chapters/02-market-and-viability.md` | — | — | not started | not started | Market, protocol, and project-status claims are highly time-sensitive. |
| `chapters/03-linux-kernel-optimization.md` | — | — | not started | not started | High priority; many kernel-version and benchmark claims need primary-source verification. |
| `chapters/04-gpu-and-accelerator-tuning.md` | — | — | not started | not started | Needs hardware validation on target GPUs and source validation for driver claims. |
| `chapters/05-ai-guided-tuning.md` | — | — | not started | not started | High priority; cited papers/repos need extraction and evaluation. |
| `chapters/06-security-and-hardening.md` | — | — | not started | not started | Security recommendations need careful freshness review. |
| `chapters/07-tokenomics-and-incentives.md` | — | — | not started | not started | Needs protocol-doc and current-tokenomics verification. |
| `chapters/08-firmware-and-bios-control.md` | 2026-05-26 | GPT-5.5 Thinking / ChatGPT | source extraction only | partial | Initial sources listed as SRC-08-001 through SRC-08-005; claims still need formal verification. |

## Open Validation Work Queue

### P0

1. Validate `chapters/08-firmware-and-bios-control.md` because it is newly authored and compact.
2. Extract and validate `chapters/03-linux-kernel-optimization.md` because it informs near-term engineering.
3. Extract and validate `chapters/05-ai-guided-tuning.md` because it informs autonomous tuning architecture.

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
