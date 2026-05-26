# Kernel Inference Optimization Benchmark Plan

Date created: 2026-05-26
Linked chapter: `chapters/03-linux-kernel-optimization.md`
Status: Proposed validation plan; not yet executed.

## Purpose

Validate Chapter 03's Linux kernel optimization claims against CursiveOS-relevant inference workloads. Chapter 03 contains promising kernel features and performance leads, but many claims are currently extrapolated from crypto, scheduler, memory-management, database, web, or synthetic benchmarks. This plan defines how to turn those leads into CursiveOS-grade evidence.

## Claims This Plan Must Validate

| Claim ID | Claim Group | Current Status | Validation Method |
| --- | --- | --- | --- |
| CH03-BM-001 | Newer kernels improve local inference performance versus older distro kernels | unverified | Compare fixed workloads across distro, LTS, and newer/mainline kernels. |
| CH03-BM-002 | sched_ext can improve inference tail latency | partially supported | Compare default scheduler against selected sched_ext policies under single-agent and multi-agent load. |
| CH03-BM-003 | PREEMPT_RT helps latency-sensitive local inference dispatch | partially supported | Compare default kernel and RT-enabled kernel where available. |
| CH03-BM-004 | zram tuning reduces stalls under memory pressure | partially supported | Compare zram off/default/tuned/writeback under constrained RAM. |
| CH03-BM-005 | fscrypt/dm-crypt crypto improvements reduce encrypted model-load time | partially supported | Compare encrypted and unencrypted model-load timing across kernels/CPUs. |
| CH03-BM-006 | GPU driver/runtime kernel paths improve Intel Arc/AMD GPU inference behavior | partially supported | Compare kernel/driver/runtime combinations with GPU inference workloads. |
| CH03-BM-007 | GPU power-management tunables reduce cold-start jitter | partially supported | Compare first-token latency after idle with default vs tuned power-management settings. |

## Required Environment Capture

Every run must record:

```text
run_id
date_time_utc
operator
host_id
motherboard_model
BIOS_version
firmware_state_hash
CPU_model
CPU_microcode_version
RAM_capacity_speed_ECC
GPU_model
GPU_PCI_ID
GPU_driver_kernel_module
GPU_firmware_version_if_available
kernel_version
kernel_config_hash_if_available
OS_distribution_version
filesystem
storage_device_model
storage_encryption_mode
Mesa_version
Intel_compute_runtime_version
Level_Zero_version
ROCm_version_if_applicable
OpenVINO_version_if_applicable
llama_cpp_commit
vllm_commit_if_applicable
sglang_commit_if_applicable
model_name
model_file_hash
quantization
context_length
backend
command_line
power_measurement_method
ambient_temperature_if_available
```

## Kernel Matrix

Minimum kernel comparison:

| Kernel Class | Example | Reason |
| --- | --- | --- |
| Distro baseline | Current Ubuntu/Fedora/Arch default | Measures what normal users get. |
| LTS baseline | Latest practical LTS | Measures stable deployment target. |
| New stable | Latest stable kernel | Captures recent scheduler/mm/driver changes. |
| Experimental/mainline | Only if needed | Tests features not yet in stable distro kernels. |

Do not promote a kernel recommendation without documenting the exact kernel version and config.

## Workload Matrix

| Workload | Why It Matters |
| --- | --- |
| Model cold load from disk | Validates storage/encryption/model-load claims. |
| First request after idle | Measures GPU/CPU cold-start latency and power-management impact. |
| Fixed prefill benchmark | Measures prompt-processing throughput. |
| Fixed decode benchmark | Measures generation throughput. |
| Long-context retrieval | Measures memory/cache/KV pressure. |
| Multi-agent concurrent tool tasks | Measures scheduler and latency behavior under real agent load. |
| Background compile or IO load + inference | Tests tail latency under contention. |
| Memory-constrained inference | Tests zram, PSI, reclaim behavior, and stall avoidance. |

## Scheduler Test

Compare:

```text
default scheduler / EEVDF path
selected sched_ext scheduler 1
selected sched_ext scheduler 2 if available
PREEMPT_RT kernel if available
SCHED_FIFO or SCHED_DEADLINE dispatch experiment only if safe
```

Metrics:

```text
P50/P95/P99 request latency
TTFT
prefill tokens/sec
decode tokens/sec
runqueue latency
CPU migrations
context switches
scheduler policy active
failed scheduler fallback events
tool-call task completion time
```

Acceptance requirement:

- No sched_ext policy should be promoted unless it improves P95/P99 latency or task completion without harming throughput/stability beyond an agreed threshold.
- Record fallback behavior and kernel logs.

## zram / Memory Pressure Test

Compare:

```text
zram disabled
zram default
zram with tuned algorithm_params
zram writeback enabled if supported
zram compressed_writeback enabled if supported
```

Metrics:

```text
model load success/failure
peak RAM
peak swap/zram usage
major page faults
PSI memory pressure
stall time
TTFT
prefill/decode throughput
writeback throughput
CPU overhead
system responsiveness
```

Do not claim inference improvement from zram unless the benchmark shows lower stall time, better task success, or better latency under the same memory constraint.

## Storage Encryption / Crypto Test

Compare:

```text
unencrypted model directory
fscrypt encrypted model directory
dm-crypt/LUKS encrypted volume if relevant
```

Run on at least two kernel versions if crypto improvement claims are being tested.

Metrics:

```text
model cold-load time
read throughput
CPU utilization during load
crypto algorithm in use
NVMe throughput
page cache state
repeat-run warm-cache timing
```

Required controls:

- Drop page cache or use fresh boot for cold-load tests.
- Separate cold-load time from model initialization time where possible.
- Record whether model loading is actually crypto-bound, storage-bound, or runtime-bound.

## GPU Power / Cold-Start Test

For Intel Arc and AMD GPU targets, compare default versus tuned power behavior.

Metrics:

```text
first-token latency after 1m idle
first-token latency after 10m idle
GPU clock ramp time
GPU power state before request
driver reset events
thermal state
average decode speed after warm-up
```

Candidate tunables must be validated per driver and hardware generation. Do not generalize AMD tunables to Intel or Intel Xe tunables to AMD.

## Output Schema

Recommended JSON output:

```json
{
  "run_id": "kernel_inference_YYYYMMDD_001",
  "host_fingerprint": "sha256:...",
  "firmware_state_hash": "sha256:...",
  "kernel": {
    "version": "...",
    "config_hash": "...",
    "scheduler": "default|sched_ext:<name>|preempt_rt",
    "boot_params": "..."
  },
  "memory": {
    "zram_mode": "off|default|tuned|writeback",
    "zram_algorithm": "...",
    "zram_params": "..."
  },
  "storage": {
    "filesystem": "...",
    "encryption": "none|fscrypt|dm-crypt",
    "device": "..."
  },
  "gpu": {
    "model": "...",
    "driver": "...",
    "runtime": "...",
    "power_profile": "..."
  },
  "model": {
    "name": "...",
    "hash": "sha256:...",
    "quantization": "...",
    "context_length": 0
  },
  "metrics": {
    "model_cold_load_ms": 0,
    "ttft_ms": 0,
    "prefill_tps": 0.0,
    "decode_tps": 0.0,
    "p95_latency_ms": 0,
    "p99_latency_ms": 0,
    "major_page_faults": 0,
    "psi_memory_some_avg10": 0.0,
    "gpu_power_avg_w": 0.0,
    "cpu_utilization_avg": 0.0
  },
  "stability": {
    "kernel_warnings": 0,
    "driver_resets": 0,
    "oom_events": 0,
    "sched_ext_fallbacks": 0
  },
  "decision": "reject|rerun|candidate|validated"
}
```

## Promotion Rules

A Chapter 03 claim can move from imported claim to verified finding only if:

- the feature is supported by primary source documentation or upstream commit evidence;
- the result is reproduced on target hardware;
- at least three runs are recorded;
- exact kernel version/config and runtime versions are captured;
- variance is reported;
- the result improves a CursiveOS-relevant metric, not just a synthetic benchmark;
- the validation ledger and source index are updated.

## Next Implementation Step

Build a small benchmark runner under `tools/` that captures environment metadata, executes fixed inference workloads, collects kernel/memory/GPU telemetry, and emits the JSON schema above.
