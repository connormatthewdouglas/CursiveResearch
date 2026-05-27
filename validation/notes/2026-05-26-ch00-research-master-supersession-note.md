# Supersession Note: Chapter 00 Research Master

Date checked: 2026-05-26
Agent / reviewer: GPT-5.5 Thinking / ChatGPT
Scope: `chapters/00-research-master.md`
Status: historical snapshot; superseded for current technical truth by topic chapters

## Summary

Chapter 00 is a useful March 26, 2026 snapshot of the project, but it should not be used as the current source of truth. It mixes repo-state observations, kernel/GPU research leads, and AI-guided tuning hooks that are now better covered by later topic chapters and validation notes.

## Supersession Map

| Chapter 00 Claim Area | Current Source of Truth |
| --- | --- |
| Repo state / rebrand history | Git history and `sources/source-register.md` |
| Kernel/sched_ext claims | `chapters/03-linux-kernel-optimization.md` plus `validation/notes/2026-05-26-ch03-linux-kernel-optimization-validation.md` |
| GPU/Arc/ROCm claims | `chapters/04-gpu-and-accelerator-tuning.md`, `chapters/09-local-agent-arc-b70.md`, and their validation notes |
| AI-guided tuning / OS-R1 / SchedCP / PolicySmith | `chapters/05-ai-guided-tuning.md` plus validation note |
| Firmware/BIOS control | `chapters/08-firmware-and-bios-control.md` |
| CursiveRoot schema evolution | source register, current codebase, and future decision records |

## Validation Result

Chapter 00 should remain in the corpus as historical evidence of the project's thinking at that time. It should not be silently edited into current truth. Future readers should treat it as an archive and follow the supersession map above for updated claims.

## Follow-up

- Add a short status note near the top of Chapter 00 in a future cleanup pass.
- If a claim from Chapter 00 matters, migrate it into the relevant topic chapter and validate it there.
