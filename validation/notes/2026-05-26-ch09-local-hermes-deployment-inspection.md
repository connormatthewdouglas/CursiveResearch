# Validation Note: Chapter 09 Local Hermes Deployment Inspection

Date checked: 2026-05-26
Agent / reviewer: Codex / GPT-5
Scope: current local Hermes configuration, OVMS endpoint, operational context requirement, tool-envelope responsiveness, and execution containment
Status: partially supported; configuration facts locally reproduced, performance observations require repeated benchmarking
Source IDs: SRC-09-003, SRC-09-004, SRC-09-005; local deployment evidence recorded below

## Claims Checked

| Claim ID | Claim | Status | Evidence | Notes / Required Rewrite |
| --- | --- | --- | --- | --- |
| CL-09-013 | The currently deployed Hermes build can be configured for an approximately 8k context window as an interactive operating target. | disputed for current deployment | Local source inspection of `~/.hermes/hermes-agent/agent/model_metadata.py`, `run_agent.py`, and `agent/context_compressor.py`; local `~/.hermes/config.yaml` | Current code defines `MINIMUM_CONTEXT_LENGTH = 64_000`, rejects smaller contexts, and the deployment uses `65536`. Preserve the imported recommendation but append a correction distinguishing configured context from active request footprint. |
| CL-09-014 | Smaller injected tool-schema and history payloads materially improve the responsiveness of the local Hermes/OVMS work path. | locally reproduced once; not yet validated | Direct OpenAI-compatible calls to local OVMS on 2026-05-26 using the configured Qwen3-Coder model and tool parser | A no-tool trivial response completed in approximately 0.50 seconds. A broad Hermes tool-envelope trivial request was canceled after more than 120 seconds. Reduced interactive profiles emitted valid tool calls, including `read_file` in 1.024 seconds after one profile pass and `skills_list` in 0.831 seconds on a warm prefix. Repeat under a controlled harness before treating as decision-grade. |
| CL-09-015 | The deployed local model endpoint supports structured tool invocation through the selected parser path. | locally reproduced once | OVMS service command uses `--tool_parser qwen3coder --enable_tool_guided_generation true`; live reduced-profile probes returned valid structured `read_file`, `skills_list`, and `session_search` calls | Supports continued parser evaluation. It does not establish broad tool-call reliability or long-argument correctness. |
| CL-09-016 | The current execution path satisfies Chapter 09 containment recommendations for shell/code work. | disputed for current deployment | Local `~/.hermes/config.yaml` and enabled cron/job inspection | `terminal.backend` is `local`, not a hardened container or VM. A scheduled repo-hygiene task modified `~/CursiveOS`; it was paused during this inspection. Containerization and task-level safety testing remain required. |
| CL-09-017 | Arc Pro B70 memory is exposed on the current host and the deployed OVMS path is operational. | locally reproduced once | Kernel `xe` log reported physical VRAM `0x0000000800000000`; OVMS `/v3/models` returned `Qwen3-Coder-30B-A3B-Instruct`; services were active on 2026-05-26 | Confirms the local test platform is available. The kernel also recommended newer GuC firmware (`70.45.2` versus installed `70.44.1`), which should be resolved before formal performance benchmarking. |

## Local Evidence Captured

| Evidence Item | Result |
| --- | --- |
| Model endpoint | OVMS at `http://127.0.0.1:8000/v3`, bound to localhost |
| Model | `Qwen3-Coder-30B-A3B-Instruct` OpenVINO INT4 model |
| Tool parser | `qwen3coder` with tool-guided generation enabled |
| Hermes configured context | `65536` tokens |
| Hermes implementation minimum | `MINIMUM_CONTEXT_LENGTH = 64_000` |
| B70 VRAM exposure | 32 GiB physical VRAM reported by `xe` kernel driver |
| Firmware caveat | GuC `70.44.1` installed; kernel recommends `70.45.2` |
| Execution containment | Fails recommended boundary: interactive/cron terminal backend is local |

## Configuration Changes Made During Inspection

These are deployment changes, not imported research findings:

- Changed interactive skill injection to on-demand and reduced always-injected CLI/Telegram toolsets to lower request-envelope cost.
- Restored `skills` and `session_search` to the interactive profile after confirming they are necessary for installed workflows and continuity across sessions.
- Added an explicit reduced cron tool profile and patched the local scheduler to honor that profile for unattended jobs.
- Paused the enabled `daily-cursiveos-repo-hygiene` scheduled task after identifying direct host-repository mutation and a failed push.

## Corpus Changes Required and Applied

- Restored the unchanged imported Chapter 09 wording after an initial correction was incorrectly written into the `Source Import` body.
- Appended `Correction: Hermes Context Guidance for the Current Deployment (2026-05-26)` to Chapter 09, keeping the imported 8k recommendation visible while narrowing its applicability for current Hermes.
- Updated `experiments/arc-b70-local-agent-benchmark-plan.md` to separate general 8k/16k/32k runtime capacity testing from Hermes testing at a configured context of at least 64,000 tokens with varied active prompt/tool/history footprints.
- Added this dated validation note and a corresponding entry in `validation/validation-ledger.md`.

## Implications for CursiveOS

- Current Hermes responsiveness work should target active prompt, schema, and history size rather than reducing its configured context below its enforced minimum.
- The local OVMS/Qwen tool parser path is viable enough for controlled benchmarking but has not been shown reliable across a meaningful task suite.
- Unattended agent work should not be restored for host repository maintenance until terminal execution is containerized or otherwise constrained and destructive actions require an explicit review boundary.

## Follow-up

- Run repeated cache-cold and cache-warm tool-envelope benchmarks under `experiments/arc-b70-local-agent-benchmark-plan.md` and preserve output as internal benchmark evidence.
- Update Intel GPU firmware/driver evidence and repeat latency measurements after firmware state is captured.
- Test hardened Docker or VM execution for file/shell task workflows before re-enabling mutating cron work.
- Extend parser reliability testing to multi-step tasks, malformed-tool resistance, and long arguments before promoting CL-09-015 beyond a local reproduction.
