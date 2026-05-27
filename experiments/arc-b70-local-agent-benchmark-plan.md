# Arc B70 Local Agent Benchmark Plan

Date created: 2026-05-26
Linked chapter: `chapters/09-local-agent-arc-b70.md`
Status: Proposed validation plan; not yet executed.

## Purpose

Convert Chapter 09 from imported/partially validated research into CursiveOS-grade evidence. This plan should be executed before Chapter 09 is used as a build guide, purchasing justification, model-selection baseline, or local-agent deployment recipe.

The key principle: no B70 performance, model, backend, tool-calling, or long-context claim becomes decision-grade until it is reproduced on target hardware with environment metadata, commands, model hashes, and variance captured.

## Claims This Plan Must Validate

| Claim ID | Claim Group | Current Status | Validation Method |
| --- | --- | --- | --- |
| CH09-BM-001 | Arc Pro B70 hardware inventory and memory/ECC exposure | partially supported | Capture `lspci`, `clinfo`, Level Zero inventory, OpenVINO device query, vendor tools, and board-vendor docs. |
| CH09-BM-002 | llama.cpp SYCL works reliably on B70 | supported generally; B70-specific unverified | Build from source; record commit, oneAPI version, driver stack, and repeated model benchmark results. |
| CH09-BM-003 | Vulkan vs SYCL backend tradeoff | unverified | Run identical model/prompt/context tests through both backends. |
| CH09-BM-004 | OpenVINO GenAI/OVMS viability | supported generally; B70-specific unverified | Convert/test supported models and compare throughput, latency, tool-output structure, and memory behavior. |
| CH09-BM-005 | MoE models outperform dense models for local agents | unverified | Compare dense/MoE candidates on throughput, latency, power, tool-call success, loop rate, and task success. |
| CH09-BM-006 | Qwen parser/template recommendations reduce tool-call failures | unverified | Run deterministic tool-calling harness across parser/template combinations. |
| CH09-BM-007 | Smaller active prompt/tool/history footprints improve Hermes responsiveness within its required context window | corrected from local inspection; performance unverified | For Hermes, configure at least 64,000 tokens and vary injected schema/history footprint; separately test 8k/16k/32k configured contexts only on runtimes that permit them. |
| CH09-BM-008 | Hermes/OpenClaw/Bifrost/Clanker stack is viable locally | unverified | Validate repos, install path, licenses, maintenance status, local endpoint compatibility, and sandbox behavior. |

## Required Environment Capture

Every run must record:

```text
host_id
run_id
date_time_utc
operator
motherboard_model
BIOS_version
firmware_state_hash
CPU_model
RAM_capacity_speed_ECC
GPU_model
GPU_PCI_ID
GPU_VBIOS_version_if_available
kernel_version
OS_distribution_version
Mesa_version
Intel_compute_runtime_version
Level_Zero_version
oneAPI_version
OpenVINO_version
llama_cpp_commit
compiler_versions
Vulkan_driver_version
model_name
model_source_url
model_file_hash
quantization
context_length
batch_size
ubatch_size
backend
command_line
ambient_temperature_if_available
power_measurement_method
```

No benchmark result should be accepted into CursiveRoot without this metadata.

## Hardware and Driver Inventory Commands

```bash
uname -a
cat /etc/os-release
lscpu
free -h
lspci -nn | grep -Ei 'vga|display|3d|intel'
lspci -vv -s <GPU_BUS_ID>
ls /dev/dri
clinfo || true
sycl-ls || true
ze_info || true
vulkaninfo --summary || true
vainfo || true
lsmod | grep -Ei 'xe|i915|drm'
dmesg | grep -Ei 'xe|i915|drm|arc|guc|huc|firmware' | tail -200
```

## Runtime Build Matrix

| Backend | Build / Install Path | Required Evidence |
| --- | --- | --- |
| llama.cpp SYCL | Source build with oneAPI compilers and `-DGGML_SYCL=ON` | Build log, commit hash, compiler version, `llama-bench` output |
| llama.cpp Vulkan | Source build with Vulkan enabled | Build log, commit hash, Vulkan driver summary, `llama-bench` output |
| OpenVINO GenAI / OVMS | Official OpenVINO install path | Version output, model conversion logs, benchmark output |
| IPEX-LLM / other Intel runtime | Optional second pass | Install log and benchmark output |

## Model Test Matrix

| Model Class | Candidate | Reason |
| --- | --- | --- |
| Small dense baseline | Llama 3.1 8B Q4_K_M or Hermes 3 8B Q4_K_M | Establish fast local-agent baseline. |
| Mid dense reasoning | Qwen dense ~14B or Phi-class dense model | Measure latency/quality middle ground. |
| Large dense | Qwen 3.5 27B Q4_K_M or nearest available verified equivalent | Test obedience and structured output at higher reasoning class. |
| MoE candidate | Qwen 35B-A3B class Q4/UD-Q4 | Validate claimed active-parameter efficiency. |
| OpenVINO-supported model | Intel/OpenVINO-supported Qwen/Llama variant | Compare Intel-native stack against GGUF path. |

For each model, record exact source, license, file hash, quantization, tokenizer/template, and any local modifications.

## Performance Metrics

Minimum metrics:

```text
prompt_prefill_tokens_per_second
decode_tokens_per_second
time_to_first_token_ms
end_to_end_task_latency_ms
VRAM_used_idle
VRAM_used_peak
system_RAM_used_peak
GPU_power_average_watts
GPU_power_peak_watts
CPU_power_if_available
tokens_per_joule
thermal_throttle_events
driver_reset_events
crash_or_deadlock_events
```

Preferred measurement methods:

- Use runtime-reported `llama-bench` or server metrics for token timings.
- Use `intel_gpu_top`, Level Zero telemetry, vendor tools, smart PDU, or wall-power meter for power.
- Treat software-reported power as lower confidence unless cross-checked.

## Context Scaling Test

Separate general runtime context-capacity testing from Hermes operating-profile testing.

For server/runtime paths that permit smaller configured windows, run each viable model at:

```text
8k configured context
16k configured context
32k configured context if memory allows
```

For each configured context size:

1. Load model fresh.
2. Run a fixed 512-token prefill prompt.
3. Run a fixed decode target, such as 128 and 512 generated tokens.
4. Run a long-context retrieval prompt with facts placed near the beginning, middle, and end.
5. Record VRAM, TTFT, decode speed, errors, and output quality.

For Hermes Agent specifically, do not use 8k as the configured context target unless its implementation changes. The build inspected on 2026-05-26 enforces `MINIMUM_CONTEXT_LENGTH = 64_000`, and the deployed configuration uses 65,536 tokens. Run Hermes at a configured context of at least 64,000 tokens while varying the active request footprint:

```text
minimal no-tool request
core interactive tool profile
expanded tool profile
short fresh session history
accumulated session history
```

For each Hermes footprint, record prompt tokens, serialized tool-schema size, TTFT, end-to-end latency, cache-warm versus cache-cold behavior, VRAM, tool-call validity, and task outcome. The tuning target is the smallest practical active prompt/tool/history payload inside Hermes' required configured context window, not an unsupported 8k Hermes context setting.

Acceptance target for personal-agent mode:

```text
TTFT < 2.5 seconds preferred
Decode > 25 tokens/sec preferred
No driver reset
No failed generation
No tool-call corruption
```

## Tool-Calling Reliability Harness

Tool-call validation matters more than raw tokens/sec for CursiveOS agents.

Run a fixed suite of at least 50 tool tasks per model/backend/template combination:

| Test Type | Example Requirement | Pass Criterion |
| --- | --- | --- |
| Simple function call | Call one tool with two scalar args | Valid call, correct args |
| Nested JSON | Call tool with nested config object | JSON validates against schema |
| Long argument | Call tool with 1k-4k token payload | No truncation or malformed JSON |
| Multi-step repair | Use tool result, then call second tool | Correct sequence and final answer |
| No-tool task | Answer without tool | Does not hallucinate a tool call |
| Refusal/safety task | Decline unsafe tool command | No command execution |
| Thinking-tag stress | Prompt induces `<thinking>` leakage | Parser still emits valid tool call or clean failure |

Record:

```text
tool_call_success_rate
json_schema_validity_rate
wrong_tool_rate
missing_tool_rate
malformed_tool_rate
truncated_argument_rate
loop_rate
mean_steps_to_completion
```

Parser/template variants to test:

```text
official template + native function calling
custom Jinja template
qwen3_xml parser if available
qwen3_coder parser if available
preserve_thinking=true
preserve_thinking=false
high max output tokens
low/default max output tokens
```

Any parser/template recommendation in Chapter 09 must be backed by this harness before being promoted to `Verified Finding`.

## Agentic Task Harness

After raw model tests, run higher-level agent tasks:

1. Read a small repo and summarize architecture.
2. Modify a toy script and run tests.
3. Parse a config file and propose a safe patch.
4. Use shell in a sandbox to inspect system info.
5. Perform a multi-file search and produce a grounded answer.
6. Recover from a failing command.
7. Refuse or sandbox a dangerous command.

Record:

```text
task_success_rate
human_intervention_count
unsafe_action_attempts
sandbox_escape_attempts
average_wall_time
model_tokens_used
number_of_tool_calls
retries
```

## Safety and Containment Test

Before any local agent is considered acceptable:

- Run tools in a container or VM.
- Drop unnecessary Linux capabilities.
- Use read-only root where possible.
- Restrict filesystem mounts.
- Limit CPU, memory, process count, and wall time.
- Disable privileged Docker mode.
- Block network egress except allowlisted endpoints.
- Log all commands and outputs.

Minimum security evidence:

```bash
docker inspect <container>
capsh --print
cat /proc/self/status | grep Cap
ulimit -a
nft list ruleset || true
```

## Pass / Fail Promotion Rules

A Chapter 09 claim can be promoted only if it has:

- exact source or command provenance;
- repeatable benchmark command;
- at least three successful runs;
- no unexplained driver resets or crashes;
- model hash and runtime commit captured;
- comparable baseline;
- clear result variance;
- validation note added under `validation/notes/`;
- source index updated with all supporting sources.

Promotion levels:

| Evidence Level | Meaning |
| --- | --- |
| Imported claim | Came from source document; not trusted yet. |
| Source-supported claim | Supported by official docs or credible external source. |
| Locally reproduced claim | Reproduced once on CursiveOS hardware. |
| Validated finding | Reproduced across at least three runs with captured environment and variance. |
| Decision-grade finding | Validated finding tied to a CursiveOS decision record. |

## Benchmark Output Schema

Recommended JSON output shape:

```json
{
  "run_id": "arc_b70_local_agent_YYYYMMDD_001",
  "host_fingerprint": "sha256:...",
  "firmware_state_hash": "sha256:...",
  "backend": "llama_cpp_sycl",
  "runtime_commit": "...",
  "driver_stack": {
    "kernel": "...",
    "mesa": "...",
    "level_zero": "...",
    "oneapi": "..."
  },
  "model": {
    "name": "...",
    "quantization": "...",
    "file_hash": "sha256:...",
    "context_length": 65536
  },
  "metrics": {
    "prefill_tps": 0.0,
    "decode_tps": 0.0,
    "ttft_ms": 0,
    "vram_peak_gib": 0.0,
    "power_avg_w": 0.0,
    "tokens_per_joule": 0.0,
    "tool_call_success_rate": 0.0,
    "json_validity_rate": 0.0,
    "loop_rate": 0.0
  },
  "stability": {
    "driver_resets": 0,
    "deadlocks": 0,
    "crashes": 0,
    "thermal_throttle_events": 0
  },
  "decision": "reject|rerun|candidate|validated"
}
```

## Next Implementation Step

Create a repeatable benchmark runner under `tools/` that emits the JSON schema above and appends results into a future `experiments/results/` directory or CursiveRoot export.
