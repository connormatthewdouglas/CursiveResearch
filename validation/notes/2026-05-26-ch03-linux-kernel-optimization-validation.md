# Validation Note: Chapter 03 Linux Kernel Optimization

Date checked: 2026-05-26
Agent / reviewer: GPT-5.5 Thinking / ChatGPT
Scope: targeted validation of highest-impact Chapter 03 claims
Status: partially verified
Source IDs: SRC-03-001 through SRC-03-006

## Summary

Chapter 03 contains several real and important Linux-kernel features relevant to CursiveOS, but it currently overstates the decision-grade certainty of some performance claims. The strongest validated pieces are the existence and shape of `sched_ext`, PREEMPT_RT in Linux 6.12, fscrypt cipher-mode details, and zram sysfs controls such as `algorithm_params`, `compressed_writeback`, and `writeback_batch_size`.

The weaker pieces are exact speedup numbers, kernel-version projections such as 6.19/7.0, and broad inference-specific extrapolations from web/server/database/HPC benchmarks. These may be useful leads, but they should be treated as hypotheses until reproduced on CursiveOS hardware.

## Claims Checked

| Claim ID | Claim | Status | Evidence | Notes / Required Rewrite |
| --- | --- | --- | --- | --- |
| CL-03-001 | `sched_ext` allows BPF programs to define scheduler behavior and can be dynamically enabled/disabled. | supported | SRC-03-001 | Linux docs support the core feature. Keep. |
| CL-03-002 | `sched_ext` merged in Linux 6.12. | supported | SRC-03-002 | KernelNewbies release summary supports this; ideally add upstream commit references later. |
| CL-03-003 | `sched_ext` by itself guarantees 75% inference tail-latency reduction. | unsupported / overbroad | SRC-03-001, SRC-03-002, SRC-03-005, SRC-03-006 | Some sched_ext research/workloads show tail-latency improvements, but not a universal inference guarantee. Rewrite as workload-specific and benchmark-required. |
| CL-03-004 | PREEMPT_RT was included in Linux 6.12. | supported | SRC-03-002 | Release summary supports this. |
| CL-03-005 | fscrypt uses AES-256-XTS for file contents and AES-256-CBC-CTS for filenames. | supported | SRC-03-004 | Kernel fscrypt docs support this; filename modes vary by configuration, so wording should stay precise. |
| CL-03-006 | Kernel crypto improvements can improve encrypted model-loading paths. | partially supported | SRC-03-004 plus external performance sources not fully normalized | The mechanism is plausible if model loading is crypto-bound. Need local benchmark before claiming model-loading benefit or NVMe saturation. |
| CL-03-007 | zram exposes `algorithm_params`. | supported | SRC-03-003 | Kernel docs support. |
| CL-03-008 | zram exposes `compressed_writeback` and it avoids decompression for writeback. | supported | SRC-03-003 | Kernel docs support. |
| CL-03-009 | zram exposes `writeback_batch_size` and it controls number of in-flight writeback operations. | supported | SRC-03-003 | Kernel docs support. |
| CL-03-010 | zram writeback batching guarantees a 4x inference improvement. | unsupported / overbroad | SRC-03-003 | Feature exists; imported 4x writeback claim needs source/method validation and is not automatically an inference improvement. |
| CL-03-011 | Cache-aware scheduling and MIGRC are useful leads for memory-wall optimization. | partially supported | SRC-03-006 plus sources not fully normalized | Interesting, but still patch/research territory. Do not treat as current production guidance without kernel status confirmation. |
| CL-03-012 | Sysfs tunables like AMD `runpm`, AMD `pp_power_profile_mode`, zram `algorithm_params`, and Intel Xe power profiles are potential benchmark levers. | partially supported | SRC-03-003 plus additional sources pending | zram portions are validated. GPU power tunables need driver-specific source extraction and hardware validation. |

## Required Corpus Changes

### Recommended Chapter 03 wording changes

- Replace `cut tail latency by 75%` with `some sched_ext schedulers and research workloads report large tail-latency reductions; CursiveOS must reproduce this on inference workloads before adopting it as a validated finding`.
- Replace `kernel 7.0 brought` claims with dated, source-backed wording unless the exact kernel release/merge status is verified.
- Treat zram writeback speedups as memory-pressure hypotheses, not guaranteed inference wins.
- Separate upstream kernel features from Phoronix/LWN/news/benchmark leads.
- Add an experiment plan before using Chapter 03 as tuning guidance.

## Implications for CursiveOS

Validated enough to justify engineering exploration:

- Track `sched_ext` as a possible CursiveOS scheduling mutation surface.
- Track zram sysfs controls as reversible memory-pressure mutation candidates.
- Track fscrypt/kernel-crypto improvements as relevant only if encrypted model loading is measured as a bottleneck.

Not yet validated enough to hard-code:

- specific sched_ext scheduler choice;
- exact kernel version floor beyond feature requirements;
- expected percentage improvements;
- inference benefit from database/web/HPC benchmark data;
- GPU power-management tunables without target-device validation.

## Suggested Experiment Plan

Create `experiments/kernel-inference-optimization-benchmark-plan.md` with at least these dimensions:

| Dimension | Values |
| --- | --- |
| Kernel | current distro kernel, latest stable, selected LTS, custom mainline if needed |
| Scheduler | default EEVDF/CFS path, selected `sched_ext` scheduler, PREEMPT_RT where applicable |
| Memory pressure | zram off, zram default, zram tuned algorithm params, zram writeback enabled |
| Storage encryption | unencrypted, fscrypt, dm-crypt/LUKS if relevant |
| Workloads | model cold load, prefill, decode, multi-agent tool calls, concurrent background load |
| Metrics | TTFT, prefill tps, decode tps, P95/P99 latency, model-load time, page faults, PSI, CPU migrations, GPU utilization, power |

## Follow-up

- Extract all Chapter 03 sources fully into `sources/extracted-source-index.md`.
- Add upstream commit references for sched_ext, PREEMPT_RT, zram attributes, and any GPU SVM claims.
- Create and link a kernel inference benchmark plan.
- After local benchmarks, amend Chapter 03 with `Verified Finding` sections instead of imported performance claims.
