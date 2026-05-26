# AI-Guided Tuning Loop Validation Plan

Date created: 2026-05-26
Linked chapter: `chapters/05-ai-guided-tuning.md`
Status: Proposed validation plan; not yet executed.

## Purpose

Validate the core Chapter 05 thesis: an AI-guided tuning loop can improve a CursiveOS system by observing telemetry, proposing bounded changes, evaluating results, and preserving only changes that improve measured fitness.

This plan intentionally begins with low-risk, reversible configuration experiments. It should not begin with kernel recompilation, generated kernel code, firmware control, or production-host mutation. The first goal is to prove that the control loop itself creates value.

## Core Loop

```text
observe telemetry
-> propose bounded configuration change
-> validate proposal against schema and allowlist
-> evaluate in a controlled test environment
-> accept, reject, or quarantine result
-> record evidence in CursiveRoot
```

## Research Claims to Validate

| Claim ID | Claim Group | Current Status | Validation Method |
| --- | --- | --- | --- |
| CH05-BM-001 | LLM-guided tuning can outperform static defaults | unverified locally | Compare fixed workloads under default settings versus LLM-guided suggestions. |
| CH05-BM-002 | LLM-guided tuning can outperform random search | unverified locally | Compare against random allowed changes using the same evaluation budget. |
| CH05-BM-003 | Structured action schemas reduce invalid proposals | unverified locally | Track invalid proposal rate with and without schema restrictions. |
| CH05-BM-004 | Historical mutation memory improves future proposals | unverified locally | Compare LLM-guided tuning with and without prior-run retrieval. |
| CH05-BM-005 | Always-on bounded tuning is the safest first prototype | hypothesis | Start with reversible, low-risk knobs before scheduler policies, kernel configuration, or generated heuristics. |

## Initial Scope

Phase 1 should only test bounded configuration surfaces that are:

- documented;
- reversible;
- allowlisted;
- measurable;
- safe to run in a test environment;
- recorded before and after evaluation.

Examples of acceptable Phase 1 targets include service-level concurrency, agent runtime settings, benchmark parameters, and non-destructive system tuning controls. Deeper changes such as scheduler-policy synthesis, kernel build options, generated C/C++ heuristics, or firmware settings belong in later phases after the loop proves itself.

## Baselines

Compare AI-guided tuning against:

| Baseline | Purpose |
| --- | --- |
| Static default | Measures improvement over no tuning. |
| Hand-written heuristic | Measures against human-authored rules. |
| Random search | Tests whether the model adds value over blind exploration. |
| Grid search | Useful for very small parameter spaces. |
| Bayesian optimization | Stronger black-box tuning baseline where feasible. |
| LLM without memory | Tests one-shot reasoning. |
| LLM with CursiveRoot retrieval | Tests value of historical mutation memory. |

## Required Evidence Per Run

Every run should record:

```text
run_id
date_time_utc
host_id
firmware_state_hash
kernel_version
workload_name
baseline_config_hash
candidate_config_hash
agent_model
agent_prompt_hash
retrieval_context_hash
schema_version
benchmark_command_or_harness
fitness_before
fitness_after
decision
```

## Metrics

Minimum metrics:

```text
p50_latency_ms
p95_latency_ms
p99_latency_ms
throughput
error_rate
time_to_first_token_ms
prefill_tokens_per_second
decode_tokens_per_second
tool_call_success_rate
invalid_proposal_rate
accepted_change_count
rejected_change_count
quarantined_change_count
net_fitness_delta
```

Stability metrics:

```text
service_crashes
benchmark_failures
manual_intervention_required
unexpected_resource_spikes
```

## Acceptance Rules

A tuning strategy should not be promoted unless:

- all proposals are typed and schema-validated;
- all target settings are allowlisted;
- before/after values are recorded;
- evaluation results are reproducible;
- the strategy beats at least two baselines under the same budget;
- guardrail metrics do not regress beyond threshold;
- results are logged in a format suitable for CursiveRoot.

## Phase Plan

### Phase 1 — Bounded Configuration Agent

Use typed actions over low-risk settings. Compare against defaults, random search, and hand-written heuristics.

### Phase 2 — Memory-Augmented Agent

Add retrieval from the prior mutation ledger and test whether history improves proposals or reduces repeated bad suggestions.

### Phase 3 — Scheduler Experiment

Introduce scheduler-related experiments only after Phase 1 is stable. Use Chapter 03's kernel benchmark plan as the evaluation harness.

### Phase 4 — Kernel Configuration Experiment

Evaluate AutoOS/OS-R1-style approaches only in an isolated research environment with compile, boot, and benchmark gates.

### Phase 5 — Generated Heuristic Experiment

Evaluate PolicySmith-style generated heuristics only after static review, test replay, and isolated evaluation are available.

## Promotion Levels

| Level | Meaning |
| --- | --- |
| Imported claim | Mentioned in Chapter 05, not independently trusted. |
| Source-supported claim | Supported by paper/repo documentation. |
| Locally reproduced claim | Reproduced once in CursiveOS environment. |
| Validated finding | Reproduced across repeated runs with captured metadata. |
| Decision-grade finding | Validated finding tied to a dated CursiveOS decision record. |

## Next Implementation Step

Build a small validation harness that can:

1. capture telemetry snapshots;
2. load an allowlist of tunable settings;
3. collect proposals from an agent or baseline strategy;
4. validate proposals against schema;
5. evaluate candidates under a fixed workload;
6. record before/after metrics;
7. emit a structured result for CursiveRoot.
