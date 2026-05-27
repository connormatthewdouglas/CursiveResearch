# Hermes OVMS Tool-Envelope Smoke Test

Date run: 2026-05-26
Operator: Codex / GPT-5
Status: Locally reproduced smoke test; not a validated benchmark
Related chapter: `chapters/09-local-agent-arc-b70.md`
Related plan: `experiments/arc-b70-local-agent-benchmark-plan.md`

## Purpose

Record the observation that prompted the Chapter 09 Hermes-context correction and the local tool-profile changes. This run was diagnostic: it establishes a reproducible lead for the formal benchmark plan, but it does not satisfy repeated-run, cache-control, or full environment-capture requirements.

## Environment Captured

| Field | Value |
| --- | --- |
| Host | `Vega` |
| OS | Linux Mint 22.3 / Ubuntu noble base |
| Kernel | `6.17.0-19-generic` |
| GPU | Intel discrete GPU, BMG G31 / Arc Pro B70-class card via `xe` driver |
| GPU VRAM evidence | Kernel reported physical VRAM `0x0000000800000000` (32 GiB) |
| GPU firmware caveat | GuC `70.44.1` active; kernel recommends `70.45.2` |
| Model server | OpenVINO Model Server / OpenVINO GenAI `2026.1` container |
| Endpoint | `http://127.0.0.1:8000/v3`, localhost-bound |
| Model | `Qwen3-Coder-30B-A3B-Instruct` from OpenVINO INT4 model files |
| Target device | GPU |
| Tool parser | `qwen3coder` |
| Guided tool generation | enabled |
| Hermes configured context | `65536` tokens |
| Hermes source requirement | `MINIMUM_CONTEXT_LENGTH = 64_000` |

## Configuration Evidence

The locally inspected Hermes source and configuration established these facts:

```text
~/.hermes/hermes-agent/agent/model_metadata.py
  MINIMUM_CONTEXT_LENGTH = 64_000

~/.hermes/hermes-agent/run_agent.py
  rejects a detected context window below MINIMUM_CONTEXT_LENGTH

~/.hermes/hermes-agent/agent/context_compressor.py
  floors the compression threshold at MINIMUM_CONTEXT_LENGTH

~/.hermes/config.yaml
  model.context_length: 65536
  model.default: Qwen3-Coder-30B-A3B-Instruct
  model.base_url: http://127.0.0.1:8000/v3
```

Reproduction inspection commands:

```bash
rg -n 'MINIMUM_CONTEXT_LENGTH|threshold_tokens' \
  ~/.hermes/hermes-agent/agent/model_metadata.py \
  ~/.hermes/hermes-agent/agent/context_compressor.py \
  ~/.hermes/hermes-agent/run_agent.py
rg -n 'default:|base_url:|context_length:' ~/.hermes/config.yaml
curl -fsS http://127.0.0.1:8000/v3/models
systemctl --user status hermes-ovms.service hermes-gateway.service --no-pager
```

## Endpoint Probe Method

Requests were sent directly to the configured OpenAI-compatible endpoint at `/chat/completions` using the deployed model. Hermes tool definitions were loaded from the local registry using the corresponding enabled toolsets. Each request used `tool_choice: auto`; tool-call probes set `max_tokens: 96` and `temperature: 0`.

The probe intentionally changed tool-envelope size to determine whether the observed work-path delay was associated with tool injection. OVMS prefix caching was not reset between every probe, so cache-warm versus cache-cold conclusions remain provisional.

## Observations

| Case | Request / Tool Envelope | Observed Result | Status |
| --- | --- | --- | --- |
| A | No tools; reply exactly `OK` | Completed in approximately `0.501 s`; usage reported 13 prompt tokens and 2 completion tokens | locally reproduced once |
| B | One simple synthetic weather schema; request a weather call | Valid structured `get_weather({"city":"Boston"})` call in approximately `4.376 s` | locally reproduced once |
| C | Prior broad Hermes interactive profile, approximately 28 tools / 36,056 serialized schema characters; no-tool answer requested | Still generating after more than `120 s`; request manually canceled | diagnostic failure observation |
| D | Lean execution profile, 9 tools / approximately 14,585 serialized schema characters; no-tool answer requested | Completed in approximately `55.01 s`; usage reported 4,133 prompt tokens and 2 completion tokens | locally reproduced once; likely cold prefix |
| E | Reduced interactive profile, 9 tools; request `read_file` for `/etc/os-release` | Valid structured `read_file({"path":"/etc/os-release"})` call in approximately `1.024 s`; usage reported 4,141 prompt tokens and 23 completion tokens | locally reproduced once; cache state not controlled |
| F | Reduced profile with `skills` restored, 13 tools; request `read_file`, then `skills_list` | Valid `read_file` in `37.414 s`; valid `skills_list({})` in `0.831 s` | locally reproduced once; first request likely cold, second warm |
| G | Reduced profile with `skills` and `session_search`, 14 tools / 21,210 serialized schema characters; request session search | Valid `session_search({"query":"CursiveOS"})` call in `13.929 s` | locally reproduced once; cache state not controlled |

## Interpretation Boundary

Supported by this smoke test:

- The current Hermes implementation cannot treat an 8k configured context as a valid operating setting because its inspected source requires at least 64,000 tokens.
- The deployed OVMS/parser path can emit valid structured calls for tools exposed by reduced interactive profiles.
- Large injected tool-schema envelopes are a credible contributor to work-path latency and warrant controlled measurement.

Not supported by this smoke test:

- A general performance guarantee for any tool profile.
- A validated latency improvement magnitude.
- A conclusion about the best backend, model, parser, cache policy, or context length for production.
- Safety approval for unattended host mutation.

## Deployment Actions Triggered

- Reduced always-injected interactive toolsets, while retaining file, terminal, web search, memory, todo, clarification, skills, and session-search capabilities.
- Added an explicit reduced cron tool profile and local scheduler support for it.
- Paused the observed mutating `daily-cursiveos-repo-hygiene` cron task after it modified `~/CursiveOS` through the local terminal backend.

These actions are operational mitigations, not evidence that the full Chapter 09 deployment recommendation is validated.

## Required Next Test

Execute the formal plan with repeated runs and captured variance:

1. Hold model, parser, prompt, and endpoint constant.
2. Measure no-tools, minimal-tools, normal interactive-tools, and expanded-tools profiles.
3. Separate cold-prefix and warm-prefix measurements.
4. Record actual prompt tokens, tool-schema serialized size, TTFT, total latency, VRAM, and call validity.
5. Repeat each case at least three times after GPU firmware state is recorded or updated.
6. Run tool-bearing actions only in a hardened container or non-destructive test workspace when evaluating autonomy.
