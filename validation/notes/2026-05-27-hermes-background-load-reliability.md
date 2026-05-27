# Validation Note: Hermes Background Load Reliability

Date checked: 2026-05-27
Agent / reviewer: Codex / GPT-5
Scope: local Hermes gateway behavior under overlapping foreground, background-review, cron, and OVMS startup load
Status: locally reproduced operational issue; mitigated in the inspected deployment
Related chapter: `chapters/09-local-agent-arc-b70.md`

## Summary

The local Hermes deployment can appear stuck under load even when CPU and host
memory are healthy. The inspected failure mode was not a general host resource
shortage. It was foreground user work competing with autonomous background
Hermes work on the same Arc-hosted OVMS model.

For the inspected single-local-model deployment, automatic background work
should be treated as capacity-consuming production traffic. It should be
disabled, serialized behind user work, or routed to a separate smaller/provider
model before unattended use is restored.

## Incident Pattern Observed

During the private-repository access task, a foreground Telegram exchange
completed at `2026-05-27 01:32:44 EDT`. Hermes then started an automatic
background skill-review run with the prompt shape:

```text
Review the conversation above and consider saving or updating a skill if appropriate.
```

That background review included the prior conversation, tool history, and tool
schema context. A corrective user message arrived at `2026-05-27 01:35:12 EDT`
while the review was still active. OVMS then showed two simultaneous requests
sharing the local model executor, with dynamic cache usage reaching roughly
`99.7%` to `100.0%` for extended periods.

Observed session sizes:

| Session | Role | System Prompt Chars | Message Content Chars | Tool Schema Chars |
| --- | --- | ---: | ---: | ---: |
| `20260526_214515_2d241f90` | foreground GitHub troubleshooting session | 14,404 | 47,277 | 20,625 |
| `20260527_013244_1bc1dd` | background skill-review session | 27,867 | 79,591 | 39,478 |

The background review had a larger active context footprint than the foreground
task and competed for the same OVMS GPU/KV-cache budget.

## Additional Startup Race

A separate reliability issue was found during the same inspection. The gateway
startup guard waited for `GET /v3/models` to succeed, but OVMS exposes the HTTP
server before the `Qwen3-Coder-30B-A3B-Instruct` mediapipe graph is fully
available. On restart, cron could send work during this window and receive:

```text
HTTP 404: Mediapipe graph definition with requested name is not found
```

In a cold restart verification, OVMS reported the model `AVAILABLE` at
`2026-05-27 11:57:38 EDT`; the corrected gateway guard started the gateway at
`2026-05-27 11:57:41 EDT`, after a real completion request succeeded.

## Mitigations Applied Locally

Operational changes made to the inspected deployment:

- Disabled periodic memory-review nudges: `memory.nudge_interval: 0`.
- Disabled periodic skill-creation reviews: `skills.creation_nudge_interval: 0`.
- Disabled all enabled Hermes cron jobs so scheduled prompts do not compete
  with foreground Telegram work.
- Replaced the gateway readiness probe with a minimal successful
  `/v3/chat/completions` request against the actual configured model.

After mitigation, a direct model health request completed with HTTP `200` in
approximately `1.33 s`.

## What This Supports

Supported for the inspected deployment:

- Background self-review can materially degrade foreground responsiveness when
  it shares the same local OVMS model and GPU cache.
- A simple `/v3/models` readiness check is not sufficient for this OVMS setup;
  the gateway should wait for an actual completion from the target model.
- Cron jobs and autonomous maintenance loops should be considered part of the
  model load budget, not "free" control-plane work.

Not established:

- A general maximum safe concurrency for Arc Pro B70-class local agent service.
- A precise KV-cache capacity threshold for all prompt/tool-envelope shapes.
- Whether the same issue occurs with a smaller auxiliary model, CPU fallback,
  non-streaming calls, or an external provider for background review tasks.

## Guidance for Chapter 09

Chapter 09 should treat local-agent reliability as a scheduling and workload
isolation problem, not only a model-selection or context-window problem.

Practical guidance for current CursiveOS/Hermes work:

1. Keep the foreground interactive agent as the priority workload.
2. Disable autonomous background review and cron work on single-GPU local model
   deployments until a queue or priority system exists.
3. Route memory flushes, skill reviews, title generation, and cron summaries to
   a separate low-cost provider or smaller local model if those features are
   required during interactive use.
4. Use model-completion health checks for gateway readiness, not HTTP-port or
   model-list availability alone.
5. Record active prompt size, tool-schema size, concurrent request count, and
   OVMS cache usage in future Arc B70 local-agent benchmarks.

## Follow-Up Experiments

- Extend `experiments/arc-b70-local-agent-benchmark-plan.md` with a concurrency
  section: one foreground request alone, foreground plus skill review,
  foreground plus cron, and two foreground-like sessions.
- Measure time-to-first-token, total latency, cache usage, and interruption
  behavior for each case.
- Test whether an explicit single-flight queue in the gateway improves perceived
  reliability more than relying on OVMS continuous batching.
- Test a separate auxiliary model/provider for review and cron tasks.
