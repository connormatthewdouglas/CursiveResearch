# GPU and Accelerator Tuning Validation Plan

Date created: 2026-05-26
Linked chapter: `chapters/04-gpu-and-accelerator-tuning.md`
Status: Proposed validation plan; not yet executed.

## Purpose

Validate Chapter 04's GPU, accelerator, memory, virtualization, and mixed-workload tuning claims before any of them become operational CursiveOS presets.

Chapter 04 contains many real mechanisms but several hardware-specific recommendations. This plan treats every device-specific claim as untrusted until the exact hardware, driver, kernel, firmware, runtime, and workload are measured.

## Core Principle

GPU tuning is not generic. It is a device-specific mutation layer.

A setting that is safe and useful on one GPU can be unstable, unavailable, or harmful on another GPU, even within the same product family.

## Claims This Plan Must Validate

| Claim ID | Claim Group | Current Status | Validation Method |
| --- | --- | --- | --- |
| CH04-BM-001 | GPU power/clock controls are exposed on target hardware | partially verified generally | Probe sysfs/vendor tools and record available controls. |
| CH04-BM-002 | RX 580 undervolt tables improve efficiency | unverified | Test only on sacrificial Polaris hardware with before/after stability and power metrics. |
| CH04-BM-003 | Intel Arc optimization should use power caps/frequency/runtime controls rather than direct undervolting | partially verified | Probe Arc device controls and test supported changes only. |
| CH04-BM-004 | Consumer GPU SR-IOV is viable for CursiveOS | unverified / lab-only | Test only in isolated lab systems and record support matrix. |
| CH04-BM-005 | Hugepages/THP/NUMA changes improve LLM inference | unverified | Measure model load, TTFT, decode, memory pressure, and tail latency. |
| CH04-BM-006 | Kyber or other I/O schedulers improve mixed storage/inference workloads | unverified | Compare under controlled mixed read/write contention. |
| CH04-BM-007 | sched_ext/scx schedulers improve mixed mining+inference workloads | unverified | Use Chapter 03 kernel benchmark plan with GPU/mixed workloads. |

## Phase 0: Hardware Capability Probe

Before applying any tuning, capture:

```text
host_id
date_time_utc
motherboard_model
BIOS_version
firmware_state_hash
kernel_version
OS_distribution_version
GPU_vendor
GPU_model
GPU_PCI_ID
GPU_VBIOS_or_firmware_version_if_available
active_kernel_driver
Mesa_version
ROCm_version_if_available
Intel_compute_runtime_version_if_available
Level_Zero_version_if_available
OpenVINO_version_if_available
available_sysfs_controls
available_vendor_tool_controls
SR_IOV_capability_reported
Secure_Boot_state
IOMMU_state
```

The first CursiveOS implementation should collect this as read-only inventory.

## Phase 1: Power and Clock Tuning

Only test controls that are discovered as available on the target hardware.

Minimum measurements:

```text
idle_power
load_power_average
load_power_peak
temperature_average
temperature_peak
clock_average
clock_peak
thermal_throttle_events
driver_reset_events
inference_prefill_tps
inference_decode_tps
time_to_first_token_ms
stability_failures
```

Acceptance requirement:

- Any power/clock change must improve efficiency or thermals without increasing error rate, driver resets, or tail latency.
- Device-specific values cannot be generalized across GPU families.

## Phase 2: Virtualization and SR-IOV

Treat GPU virtualization as lab-only until proven.

Record:

```text
host_kernel_version
guest_kernel_version
module_or_driver_name
module_version_or_commit
Secure_Boot_state
IOMMU_state
VF_count_requested
VF_count_created
host_stability
guest_stability
GPU_visibility_in_guest
workload_success_rate
crash_or_reset_events
recovery_method
```

Promotion rule:

- Community SR-IOV modules cannot be promoted to production guidance unless repeated tests show stable VF creation, workload execution, teardown, and recovery on the exact target hardware.

## Phase 3: Hugepages, THP, and NUMA

Compare default memory behavior against candidate tuned modes.

Metrics:

```text
model_load_time_ms
time_to_first_token_ms
prefill_tokens_per_second
decode_tokens_per_second
p95_latency_ms
p99_latency_ms
page_faults
TLB_miss_proxy_if_available
memory_pressure
OOM_events
```

Acceptance requirement:

- Hugepage/NUMA recommendations must be workload-specific.
- Do not promote universal rules like “always disable THP” or “always use 1GB pages” without evidence.

## Phase 4: I/O Scheduler

Compare scheduler behavior only under controlled storage contention.

Candidate schedulers:

```text
none
mq-deadline
kyber
bfq
```

Metrics:

```text
model_cold_load_time_ms
small_read_latency
large_read_throughput
p95_read_latency
p99_read_latency
write_interference_impact
CPU_overhead
inference_TTFT_under_IO_load
```

Acceptance requirement:

- Dedicated model-serving nodes and mixed blockchain/inference nodes may require different scheduler choices.
- Do not promote Kyber globally without mixed-load evidence.

## Phase 5: Mixed Workload Test

Run a sustained background compute or storage workload alongside an LLM inference workload.

Measure:

```text
inference_TTFT
inter_token_latency
p95_latency
p99_latency
throughput
GPU_power
GPU_temperature
CPU_contention
I/O_contention
error_rate
foreground_task_success
background_task_throughput
```

This is the real Chapter 04 target: keeping latency-sensitive inference responsive while throughput-oriented background work consumes spare resources.

## Promotion Levels

| Level | Meaning |
| --- | --- |
| Imported claim | Present in Chapter 04, not trusted yet. |
| Source-supported mechanism | Supported by docs or repo, but not tested locally. |
| Hardware-probed | Control exists on target machine. |
| Locally reproduced | One successful controlled test. |
| Validated finding | Repeated runs with metadata and variance. |
| Decision-grade preset | Validated finding tied to a CursiveOS decision record and rollback strategy. |

## Follow-up Implementation

A future `cursive-gpu-probe` should:

1. detect GPU vendor/model/PCI ID;
2. list safe read-only telemetry paths;
3. list available tuning controls without writing them;
4. classify controls as read-only, reversible, reboot-required, lab-only, or unsupported;
5. emit a JSON hardware capability report for CursiveRoot.
