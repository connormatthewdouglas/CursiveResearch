# Validation Note: Chapter 05 AI-Guided Tuning

Date checked: 2026-05-26
Agent / reviewer: GPT-5.5 Thinking / ChatGPT
Scope: targeted validation of highest-impact Chapter 05 claims
Status: partially verified
Source IDs: SRC-05-001 through SRC-05-008

## Summary

Chapter 05 is directionally strong and directly relevant to CursiveOS. Its core thesis is supported: AI-guided OS tuning is a real emerging research line, and several systems already explore LLM/RL/search loops for scheduler policy, kernel configuration, heuristic synthesis, and online parameter tuning.

However, the chapter should not yet be treated as decision-grade implementation guidance. It blends validated architecture patterns with unverified performance numbers, optimistic timelines, incomplete license/maturity claims, and speculative CursiveOS/TAO integration estimates. The right next step is not to pick a winner blindly; it is to prototype a small, safe, reversible CursiveOS tuning loop and compare the approaches experimentally.

A notable update from validation: the imported chapter's “LLM Agents for Always-On OS Tuning” framing should be supplemented or partially superseded by `SemaTune: Semantic-Aware Online OS Tuning with Large Language Models` from May 2026. SemaTune appears to formalize the always-on approach with typed validation, bounded actions, telemetry, prior-run retrieval, and stronger reported improvements.

## Claims Checked

| Claim ID | Claim | Status | Evidence | Notes / Required Rewrite |
| --- | --- | --- | --- | --- |
| CL-05-001 | SchedCP is an LLM-agent framework for Linux scheduler policy synthesis using MCP-style components and `sched_ext`. | supported | SRC-05-001, SRC-05-002, SRC-03-001 | Architecture is supported. Need repo inspection and local reproduction before using performance numbers. |
| CL-05-002 | SchedCP achieved up to 1.79x speedup and 13x lower exploration cost. | partially supported | SRC-05-001 | Supported as a paper claim, not as a CursiveOS finding. Needs workload/methodology review and reproduction. |
| CL-05-003 | OS-R1 frames kernel tuning as an RL environment with rule-based rewards and reports around 5.6% improvement. | partially supported | SRC-05-003, SRC-05-004 | Supported as a paper/repo claim. Need code/license review and relevance check for CursiveOS workloads. |
| CL-05-004 | PolicySmith can synthesize new system heuristics/code with LLM + evolutionary search. | partially supported | SRC-05-005, SRC-05-006 | Architecture supported. License/maturity and production safety remain unverified. |
| CL-05-005 | Always-on LLM tuning should be treated as a serious CursiveOS control-loop candidate. | supported with update | SRC-05-007 | SemaTune provides a stronger/current version of this idea than the older workshop framing. Add SemaTune to the chapter as current source. |
| CL-05-006 | AutoOS is a useful prior for LLM-guided kernel config optimization. | needs verification | Chapter source only; external source search incomplete | The imported claim is plausible, but this pass did not fully verify AutoOS paper/repo details. Keep in queue. |
| CL-05-007 | BranchFS / Fork-Explore-Commit style primitives are relevant safety infrastructure for CursiveOS. | supported as research direction | SRC-05-008 | Strong conceptual fit with CursiveOS rollback/mutation cycle. Need prototype review before adoption. |
| CL-05-008 | The chapter's engineering effort and cost estimates are reliable. | unverified / speculative | none | Treat these as planning guesses, not validated evidence. |
| CL-05-009 | OS-R1 and AutoOS should be the first prototypes. | partially disputed / requires narrowing | SRC-05-003, SRC-05-007, SRC-05-008 | OS-R1/AutoOS are useful, but a safer first CursiveOS prototype may be an always-on bounded parameter tuner inspired by SemaTune, because it can operate over a small reversible knob set without full RL training or kernel recompilation. |

## Required Corpus Changes

### Recommended Chapter 05 wording changes

- Mark all reported improvements as `paper-reported`, not validated CursiveOS performance.
- Add SemaTune as the current/stronger always-on tuning source.
- Separate three maturity classes:
  - `safe early prototype`: bounded online parameter tuning with typed validation and rollback;
  - `medium complexity`: SchedCP-style scheduler policy synthesis;
  - `research-heavy`: OS-R1 RL training and PolicySmith code synthesis.
- Downgrade engineering cost/timeline estimates to provisional planning estimates.
- Add an experiment plan that implements a minimal CursiveOS tuner before adopting any single external framework.

## Implications for CursiveOS

The strongest architectural pattern is not any single paper. It is the shared loop:

```text
observe metrics -> propose bounded mutation -> validate action schema -> apply in sandbox/branch -> benchmark -> commit or rollback -> record fitness
```

This matches CursiveOS directly. The first implementation should avoid heavy RL and code synthesis. Start with a bounded, reversible, typed-action agent over safe knobs such as zram settings, CPU scheduling niceness/affinity, service-level concurrency, and selected GPU power/runtime settings. Only later move into scheduler BPF policy synthesis or kernel config recompilation.

## Suggested Experiment Plan

Create `experiments/ai-guided-tuning-loop-benchmark-plan.md` with these phases:

1. Build a typed mutation schema for safe OS knobs.
2. Feed the agent CursiveOS telemetry snapshots.
3. Allow only reversible changes.
4. Run benchmark gates after each mutation.
5. Commit only if fitness improves under thresholds.
6. Compare LLM-guided tuning against random search, Bayesian optimization, and hand-written heuristics.
7. Log all proposals, rejections, rollbacks, and accepted mutations to CursiveRoot.

## Follow-up

- Inspect SchedCP, OS-R1, PolicySmith, AutoOS repos for license, activity, installability, and reproducibility.
- Validate AutoOS with primary paper/repo source.
- Add SemaTune to Chapter 05 as an update/supersession note.
- Build a minimal CursiveOS tuning-loop experiment before committing to OS-R1 or PolicySmith.
- Convert any successful local experiment into a decision record.
