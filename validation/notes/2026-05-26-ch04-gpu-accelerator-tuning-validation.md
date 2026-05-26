# Validation Note: Chapter 04 GPU and Accelerator Tuning

Date checked: 2026-05-26
Agent / reviewer: GPT-5.5 Thinking / ChatGPT
Scope: targeted validation of highest-impact Chapter 04 claims
Status: partially verified, with significant caveats
Source IDs: SRC-04-001 through SRC-04-009 in `sources/chapter-04-selected-sources.md`

## Summary

Chapter 04 contains useful engineering leads, but it is less cleanly validated than Chapters 03, 05, 08, and 09. The broad control surfaces are real: AMDGPU exposes power/runtime controls; Linux supports sched_ext; Linux supports hugepages and Transparent Huge Pages controls; Kyber has documented target latency tunables; Intel and AMD GPU virtualization/SR-IOV ecosystems exist.

However, the chapter currently mixes source-supported mechanisms with aggressive hardware-specific claims. Specific RX 580 undervolt tables, universal hugepage recommendations, Intel Arc power-control claims, SR-IOV generalizations for consumer hardware, and exact percentage improvements should be treated as hypotheses until tested on target hardware.

## Claims Checked

| Claim ID | Claim | Status | Evidence | Notes / Required Rewrite |
| --- | --- | --- | --- | --- |
| CL-04-001 | AMDGPU exposes module/runtime controls such as `ppfeaturemask`, `runpm`, and recovery-related parameters. | supported | SRC-04-001 | Broad control surface is documented. Keep. |
| CL-04-002 | The specific RX 580 undervolt table is validated and safe to apply broadly. | unverified / unsafe as written | SRC-04-001 | Kernel docs support mechanism, not voltage values. Voltage stability is silicon-, board-, BIOS-, cooling-, and workload-specific. |
| CL-04-003 | `pp_od_clk_voltage` workflows can be reversible through amdgpu sysfs on supported cards. | partially supported | SRC-04-001 | Mechanism exists in amdgpu ecosystem, but exact interface availability depends on card/driver/feature mask. Must probe hardware first. |
| CL-04-004 | Intel Arc direct undervolting is generally restricted compared to AMD. | partially supported | Chapter sources and community reports; needs Intel docs | Likely directionally true, but this pass did not find primary Intel documentation validating every claim. Keep as caution, not hard rule. |
| CL-04-005 | The strongtz i915/xe SR-IOV DKMS module can create up to 7 VFs and requires host/guest module considerations. | supported as community project | SRC-04-006 | README supports this, but explicitly labels the project highly experimental and not Intel-affiliated. |
| CL-04-006 | i915-sriov-dkms is production-ready for Intel Arc multi-tenant CursiveOS deployments. | disputed / overbroad | SRC-04-006 | Repo says highly experimental. Treat as lab-only until proven on target hardware. |
| CL-04-007 | AMD GIM/MxGPU provides GPU IOV initialization, VF configuration, world-switch scheduling, and hang detection for supported hardware. | supported | SRC-04-007, SRC-04-008 | Official AMD sources support GIM role and current supported Instinct/Radeon PRO models. |
| CL-04-008 | AMD MxGPU community support extends cleanly to broad consumer GPUs. | unverified / likely overbroad | SRC-04-008 | Official support list is limited. Community experiments should not be treated as validated support. |
| CL-04-009 | Hugepages and THP controls are real Linux mechanisms relevant to memory-heavy workloads. | supported | SRC-04-003, SRC-04-004 | Mechanisms are documented. Performance impact must be benchmarked per workload. |
| CL-04-010 | Hugepages produce a universal 20-40% memory latency reduction for LLM workloads. | unverified / overbroad | SRC-04-003, SRC-04-004 | Need local benchmarks. THP vs explicit hugepages depends heavily on allocation, model runtime, page fault behavior, and memory pressure. |
| CL-04-011 | Disabling automatic NUMA balancing and using static pinning can help pinned AI workloads. | plausible but unverified in this pass | Kernel NUMA docs still need extraction | Needs dedicated source extraction and benchmark. Keep as candidate tuning knob. |
| CL-04-012 | sched_ext is dynamically controllable and reversible through documented mechanisms. | supported | SRC-04-002 | Kernel docs support dynamic enable/disable and fallback semantics. |
| CL-04-013 | Specific scx schedulers are production-ready and guaranteed to improve mining+inference mixed workloads. | unverified / overbroad | SRC-04-002, SRC-04-009 | sched_ext exists; scheduler-specific claims require scx repo review and local workload tests. |
| CL-04-014 | Kyber is a documented block I/O scheduler with read/write latency targets. | supported | SRC-04-005 | Mechanism is supported. |
| CL-04-015 | Kyber gives 99.3% lower P99 latency for all mixed inference/storage workloads. | unverified / overbroad | SRC-04-005 | Exact number needs original benchmark source and local reproduction. |
| CL-04-016 | RoCE/RDMA/GPUDirect-style cluster networking is relevant to multi-GPU/multi-node inference. | needs separate validation | none in this pass | Chapter mentions high-end cluster networking but current CursiveOS home-rack plan may not need it yet. |

## Required Corpus Changes

### Recommended Chapter 04 wording changes

- Mark RX 580 undervolt values as example hypotheses, not validated recommendations.
- Mark i915-sriov-dkms as experimental/community/lab-only unless target-hardware validation proves otherwise.
- Replace broad consumer GPU SR-IOV claims with hardware-specific support matrices.
- Replace universal hugepage/NUMA/IO scheduler claims with benchmark-required tuning candidates.
- Separate GPU-driver control surfaces from scheduler/storage/memory tuning; the chapter currently blends too many layers.
- Cross-link Chapter 04 to Chapter 09 for Arc B70 validation and Chapter 03 for sched_ext/kernel/memory validation.

## Implications for CursiveOS

Useful immediate takeaways:

- Treat GPU tuning as a device-specific mutation layer, not a generic preset.
- Build a hardware probe before applying any GPU power/clock/SR-IOV changes.
- GPU virtualization should start on official server/workstation-supported hardware, not consumer cards.
- RX 580/Polaris tuning is useful for cheap lab experiments, but not a strategic production baseline.
- Intel Arc control should focus on supported runtime/backend benchmarking first, not voltage-level tuning.

## Suggested Experiment Plan

Create `experiments/gpu-accelerator-tuning-benchmark-plan.md` with these tracks:

1. **Hardware capability probe:** collect GPU model, PCI ID, driver, firmware, available sysfs controls, SR-IOV capability, and supported power controls.
2. **Power/clock tuning:** test only allowlisted changes with automatic revert and stability monitoring.
3. **Virtualization/SR-IOV:** test only on lab systems; record host/guest kernel, DKMS module, Secure Boot state, VF creation/removal, and crash recovery.
4. **Memory/hugepage/NUMA:** measure model load, TTFT, prefill, decode, P95/P99 latency, and failures with default vs tuned memory policy.
5. **I/O scheduler:** compare `none`, `mq-deadline`, `kyber`, and `bfq` only under controlled mixed-load storage tests.
6. **Mixed workload:** run mining-like sustained compute plus LLM inference and measure fairness, latency, thermals, and error rate.

## Follow-up

- Extract all Chapter 04 sources into the canonical `sources/extracted-source-index.md` or merge `sources/chapter-04-selected-sources.md` into it.
- Validate LACT, scx scheduler repo, AMDGPU sysfs details, NUMA docs, and RDMA/GPUDirect claims.
- Build the GPU/accelerator benchmark plan before using Chapter 04 as operational guidance.
- Amend Chapter 04 with explicit `Validation Caveat` sections near RX 580, Intel Arc, SR-IOV, hugepages, and Kyber claims.
