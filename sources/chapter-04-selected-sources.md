# Chapter 04 Selected Sources

Date extracted: 2026-05-26  
Agent / reviewer: GPT-5.5 Thinking / ChatGPT  
Chapter: `chapters/04-gpu-and-accelerator-tuning.md`  
Status: Selected high-priority extraction only. Full works-cited extraction remains open.

## Purpose

This file captures the first selected source extraction for Chapter 04. It should eventually be merged or mirrored into `sources/extracted-source-index.md`, but is kept separate for now to avoid blocking the validation pass on a large canonical-index rewrite.

## Selected Sources

| Source ID | Title | Author / Organization | URL / DOI / Repo | Source Type | Date Published / Updated | Date Accessed | Used In | Claims Supported | Reliability Tier | Validation Status | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-04-001 | AMDGPU Module Parameters | Linux Kernel Documentation | https://docs.kernel.org/gpu/amdgpu/module-parameters.html | primary documentation | rolling kernel docs | 2026-05-26 | AMD Polaris / amdgpu power and runtime controls | Documents amdgpu module parameters including `runpm`, `ppfeaturemask`, `gpu_recovery`, power feature mask, and VM/queue parameters | A | verified for feature existence | Supports broad control surface; does not validate specific RX 580 voltage tables or magic feature-mask recommendations. |
| SRC-04-002 | Extensible Scheduler Class | Linux Kernel Documentation | https://docs.kernel.org/scheduler/sched-ext.html | primary documentation | rolling kernel docs | 2026-05-26 | sched_ext section | Documents sched_ext as BPF-defined scheduler class, dynamic enable/disable, fallback behavior, SysRq-S abort, and required config options | A | verified | Supports reversible scheduler-control claims; does not validate individual scx scheduler behavior or production readiness. |
| SRC-04-003 | HugeTLB Pages | Linux Kernel Documentation | https://docs.kernel.org/admin-guide/mm/hugetlbpage.html | primary documentation | rolling kernel docs | 2026-05-26 | Hugepages section | Documents hugepage support, page sizes, `nr_hugepages`, persistent hugepage pools, and reservation behavior | A | verified | Supports hugepage mechanism; not the chapter's 20-40% latency reduction claim. |
| SRC-04-004 | Transparent Hugepage Support | Linux Kernel Documentation | https://docs.kernel.org/admin-guide/mm/transhuge.html | primary documentation | rolling kernel docs | 2026-05-26 | THP latency/jitter caveats | Documents khugepaged controls, THP enablement, process-level controls, defrag, and boot parameters | A | verified | Supports THP/khugepaged configuration claims; does not prove THP should always be disabled for inference. |
| SRC-04-005 | Kyber I/O Scheduler Tunables | Linux Kernel Documentation | https://docs.kernel.org/block/kyber-iosched.html | primary documentation | rolling kernel docs | 2026-05-26 | NVMe / I/O scheduler section | Documents Kyber target read/write latency tunables and throttling behavior | A | verified | Supports Kyber mechanism, not the chapter's exact 99.3% P99 latency improvement. |
| SRC-04-006 | strongtz/i915-sriov-dkms README | strongtz / GitHub | https://github.com/strongtz/i915-sriov-dkms | community repo | rolling repo; latest release noted 2026-05-06 at extraction | 2026-05-26 | Intel SR-IOV section | Community i915/xe DKMS module with SR-IOV support, required kernel parameters, up to 7 VFs on Intel UHD Graphics, Secure Boot caveat, and host/guest module guidance | C | partially verified | Repo explicitly says it is experimental and not affiliated with Intel. Do not treat as production-grade Intel Arc support without hardware-specific proof. |
| SRC-04-007 | AMD MxGPU-Virtualization README | AMD / GitHub | https://github.com/amd/MxGPU-Virtualization | official vendor repo | rolling repo | 2026-05-26 | AMD MxGPU / GIM section | GIM is a Linux kernel module for AMD SR-IOV-based MxGPU virtualization; handles GPU IOV init, VF config, world-switch scheduling, hang detection, VF reset, and PF/VF utilities | A | verified for GIM role | Hardware support must be checked against current release notes and AMD Instinct docs. |
| SRC-04-008 | AMD Instinct Virtualization Driver: Getting started with MxGPU | AMD Instinct Documentation | https://instinct.docs.amd.com/projects/virt-drv/en/latest/userguides/Getting_started_with_MxGPU.html | official vendor docs | 2025 docs page | 2026-05-26 | AMD MxGPU / supported GPU claims | Documents MxGPU/SR-IOV concept and supported GPU models: MI210X, MI300X, MI325X, MI350X/MI355X, Radeon PRO V710 | A | verified | This weakens any broad claim that community MxGPU support extends cleanly to arbitrary consumer cards. |
| SRC-04-009 | Towards Agentic OS: An LLM Agent Framework for Linux Schedulers | Zheng et al. / arXiv | https://arxiv.org/abs/2509.01245 | paper/preprint | 2025-09-01 | 2026-05-26 | sched_ext / agentic OS overlap | Supports SchedCP as an agentic scheduler-control framework on sched_ext | B | partially verified | Reused from Chapters 03 and 05. Relevant but not GPU-specific. |

## Extraction Caveats

- Chapter 04 contains many Reddit/forum/blog sources. These should be treated as leads, not decision-grade evidence.
- Hardware-specific claims must be validated on the exact target device, kernel, driver, firmware, and runtime stack.
- RX 580 undervolt values, Intel Arc power-control claims, and consumer GPU SR-IOV claims should not be promoted without local hardware tests.
