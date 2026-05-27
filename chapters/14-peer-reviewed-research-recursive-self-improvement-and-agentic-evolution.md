# Peer-Reviewed Research: Recursive Self-Improvement and Agentic Evolution

Status: Structured research digest. This chapter summarizes published papers and credible research systems without reproducing paper contents verbatim. It is intended to support future research and implementation decisions, not to serve as a product or daemon specification.

Source list: `sources/peer-reviewed-rsi-selected-sources.md`

## Executive Summary

The most useful current research does not show unrestricted recursive self-improvement in the science-fiction sense. What it does show is more practical and more relevant to software organisms:

```text
proposal generator
-> evaluator / environment / test suite
-> selection pressure
-> archive or memory
-> next proposal
```

The strongest systems use models to propose candidates and external evaluators to decide whether those candidates matter. This is the key lesson for software organisms: self-improvement becomes real when the feedback signal is grounded outside the proposing agent.

The corpus should treat the following as supported:

- LLMs and RL systems can discover useful programs, heuristics, algorithms, and skills when paired with reliable evaluators.
- Search over code or behavior can outperform hand-written baselines in narrow domains.
- Persistent skill libraries and reflection memory can improve agent behavior without changing model weights.
- Self-evaluation and self-reward are promising but weaker and more failure-prone than external verification.
- Agent benchmark methodology is currently fragile; cost, overfitting, reproducibility, and benchmark leakage matter.

The corpus should treat the following as speculative or unproven:

- unrestricted recursive self-improvement;
- agents safely rewriting their own goals or evaluators;
- self-judgment replacing deterministic tests;
- open-ended improvement without carefully designed selection pressure;
- claims of general agent progress based only on benchmark accuracy.

## Definitions

| Term | Working Definition |
| --- | --- |
| Recursive self-improvement | A system improves the process that produces future improvements, creating a feedback loop over its own capability or scaffold. |
| Self-modification | A system changes its code, prompt, tool graph, memory, policy, or configuration. This is not automatically improvement. |
| Self-correction | A system revises an output or action after detecting an error. Usually shallow and task-local. |
| Self-reflection | A system writes natural-language feedback about its own behavior. Useful, but not reliable truth by itself. |
| Self-training | A system updates model weights or training data using generated or environment-derived feedback. Higher risk of drift. |
| Evolutionary search | Candidate generation plus mutation, evaluation, selection, and archive/history. |
| Verifier | A test, evaluator, environment, formal checker, or human process that decides whether a candidate is better. |
| Fitness function | The measurable objective used to compare candidates. The system improves only to the extent that the fitness function represents what matters. |
| Open-endedness | The ability to keep producing novel, useful adaptations rather than plateauing on a fixed benchmark. |

## Taxonomy of Self-Improvement Loops

| Loop Type | Example Systems | What Improves | Who Judges Improvement | Risk Level | Relevance to Software Organisms |
| --- | --- | --- | --- | --- | --- |
| Reflection loop | Reflexion | Agent behavior on repeated tasks | The agent plus task outcome | Medium | Useful for operator shell memory, but not enough for system truth. |
| Skill-library loop | Voyager | Reusable skills/actions | Environment feedback and self-verification | Medium | Useful model for accumulated capabilities. |
| Program-search loop | FunSearch, AlphaEvolve | Code, algorithms, heuristics | Automated evaluator | Low/medium if evaluator is robust | Directly relevant to mutation-selection architecture. |
| Recursive scaffold loop | STOP | The improver/scaffold itself | Task score and sandboxed execution | High | Relevant to bounded RSI; unsafe if sandbox/goal boundaries fail. |
| Agent-graph optimization | GPTSwarm | Agent prompts, roles, graph topology | Benchmark objective | Medium/high | Relevant to optimizing agent scaffolds, but prone to benchmark overfit. |
| RL algorithm discovery | AlphaDev, AlphaTensor | Low-level algorithms | Game/reward environment | Medium | Shows machine-discovered optimization can enter real software/hardware contexts. |
| Self-reward/evaluator loop | Self-Rewarding LMs, Self-Taught Evaluators | Reward/evaluator models | Model-generated judgments and synthetic data | High | Useful research, but dangerous if evaluator becomes ungrounded. |
| Agent-as-judge loop | Agent-as-a-Judge | Evaluation of agentic behavior | Another agentic evaluator | High | Useful at scale, but should not replace deterministic measurements. |

## Research Review

### RSI-001: AlphaEvolve

| Field | Notes |
| --- | --- |
| Core idea | A coding agent combines LLM-generated code changes with automated evaluators and evolutionary selection. |
| Improvement target | Algorithms, code, heuristics, and infrastructure-adjacent procedures. |
| Feedback signal | Domain-specific automated evaluators. |
| Demonstrated result | Reported useful discoveries across scientific and algorithmic tasks, with claims of real-world infrastructure relevance. |
| Main limitation | Results depend heavily on evaluator quality, search space, and task framing. It is not unrestricted RSI. |
| Software-organism relevance | Very high. This is close to the pattern `mutation -> evaluator -> selection -> archive`. |

### RSI-002: FunSearch

| Field | Notes |
| --- | --- |
| Core idea | LLMs generate programs that are scored by an evaluator; the best programs are fed back into future prompts. |
| Improvement target | Mathematical constructions and programmatic heuristics. |
| Feedback signal | Automated evaluator for candidate programs. |
| Demonstrated result | Produced new or improved solutions in mathematical/program-search domains. |
| Main limitation | Requires problems where candidate outputs can be scored automatically. |
| Software-organism relevance | Very high. It supports the principle that the evaluator, not the LLM, is the source of truth. |

### RSI-003: Self-Taught Optimizer / STOP

| Field | Notes |
| --- | --- |
| Core idea | A seed improver edits programs and can be applied to improve its own improvement scaffold. |
| Improvement target | Code-generation scaffold rather than base model weights. |
| Feedback signal | Program performance and task score under constrained execution. |
| Demonstrated result | Recursive scaffold improvement under experimental conditions. |
| Main limitation | The base model is fixed; safety and sandbox concerns are central. |
| Software-organism relevance | High. It is one of the clearest bounded examples of recursive self-improvement. |

### RSI-004: AI Agents That Matter

| Field | Notes |
| --- | --- |
| Core idea | Agent evaluation should account for cost, holdout quality, benchmark validity, and overfitting, not just accuracy. |
| Improvement target | Evaluation methodology. |
| Feedback signal | Critical analysis of agent benchmarks and agent claims. |
| Demonstrated result | Provides a framework for identifying weak agent evidence. |
| Main limitation | It is a methodology/critique paper, not a self-improving system. |
| Software-organism relevance | Essential. It is the guardrail against fake progress and benchmark-chasing. |

### RSI-005: Voyager

| Field | Notes |
| --- | --- |
| Core idea | An embodied LLM agent explores Minecraft, creates skills, stores them in a library, and reuses them. |
| Improvement target | Agent capabilities through accumulated executable skills. |
| Feedback signal | Environment feedback, curriculum, and self-verification. |
| Demonstrated result | Open-ended skill acquisition in a game environment without model fine-tuning. |
| Main limitation | Domain is simulated and heavily scaffolded; transfer to OS control requires caution. |
| Software-organism relevance | High. It demonstrates skill accumulation and persistent capability memory. |

### RSI-006: Reflexion

| Field | Notes |
| --- | --- |
| Core idea | Agents improve across trials by storing verbal reflections about past errors and successes. |
| Improvement target | Task behavior and strategy selection. |
| Feedback signal | Task outcome plus natural-language self-reflection. |
| Demonstrated result | Improved performance across selected agent tasks without weight updates. |
| Main limitation | Reflection can be wrong or self-justifying; it requires grounding in task results. |
| Software-organism relevance | Medium/high. Useful for shell-agent memory, but not sufficient for validating system mutations. |

### RSI-007: Language Agents as Optimizable Graphs / GPTSwarm

| Field | Notes |
| --- | --- |
| Core idea | Represent multi-agent systems as graphs whose nodes/prompts/connections can be optimized. |
| Improvement target | Agent architecture and coordination structure. |
| Feedback signal | Benchmark objective. |
| Demonstrated result | Shows agent scaffolds can be optimized as systems rather than hand-designed. |
| Main limitation | Risk of benchmark overfitting and fragile transfer. |
| Software-organism relevance | High. It suggests the agent scaffold itself is a mutation surface. |

### RSI-008: Self-Taught Evaluators

| Field | Notes |
| --- | --- |
| Core idea | Improve an evaluator model using synthetic data and iterative self-training without human preference labels. |
| Improvement target | Evaluator model quality. |
| Feedback signal | Synthetic comparisons and iterative training loop. |
| Demonstrated result | Reported evaluator improvements on evaluator benchmarks. |
| Main limitation | Evaluator drift and benchmark overfitting remain serious concerns. |
| Software-organism relevance | Medium/high. Useful for scalable review, but dangerous if it replaces hard measurements. |

### RSI-009: AlphaDev

| Field | Notes |
| --- | --- |
| Core idea | Deep reinforcement learning discovers faster low-level algorithms such as sorting routines. |
| Improvement target | Assembly-level or low-level algorithmic procedures. |
| Feedback signal | Correctness and performance reward. |
| Demonstrated result | Discovered sorting improvements that were incorporated into real software libraries. |
| Main limitation | Narrow optimization domain; requires precise reward and verification. |
| Software-organism relevance | High. Demonstrates AI-discovered optimizations can graduate into real infrastructure. |

### RSI-010: AlphaTensor

| Field | Notes |
| --- | --- |
| Core idea | Matrix multiplication algorithm discovery is framed as a game/search problem. |
| Improvement target | Matrix multiplication algorithms and hardware-relevant computation strategies. |
| Feedback signal | Correctness and efficiency reward. |
| Demonstrated result | Discovered many matrix multiplication algorithms, including hardware-sensitive improvements. |
| Main limitation | Specialized formalizable domain. |
| Software-organism relevance | Medium/high. Supports search-based improvement over computational procedures. |

### RSI-011: Self-Rewarding Language Models

| Field | Notes |
| --- | --- |
| Core idea | Models generate judgments/rewards to improve future model behavior. |
| Improvement target | Instruction-following and reward modeling behavior. |
| Feedback signal | Model-generated rewards. |
| Demonstrated result | Reports iterative improvement under experimental conditions. |
| Main limitation | High risk of evaluator drift and circular self-approval. |
| Software-organism relevance | Medium. Study as a warning and possible supplement, not as primary truth. |

### RSI-012: Agent-as-a-Judge

| Field | Notes |
| --- | --- |
| Core idea | Use agentic evaluators to evaluate agentic behavior more realistically than static judge prompts. |
| Improvement target | Evaluation of multi-step agent performance. |
| Feedback signal | Agentic judging process. |
| Demonstrated result | Provides an evaluation direction for complex agents. |
| Main limitation | Judge agents inherit the same risks as agents: tool-use mistakes, bias, drift, and overfitting. |
| Software-organism relevance | Medium. Useful for triage and review, but not for final mutation truth. |

## Verifier and Fitness Problem

The central research lesson is that self-improvement is only as good as the evaluator.

A language model can propose candidates, explain failures, generate alternatives, and maintain memory. It should not be treated as the final authority on whether the system improved.

Evaluation signals can be ordered by trustworthiness for system mutation:

| Evaluation Signal | Strength | Main Risk |
| --- | --- | --- |
| Formal proof / verifier | Very high when available | Often unavailable or too narrow. |
| Unit/integration tests | High for correctness | May miss performance, safety, and hidden regressions. |
| Benchmarks with repeated runs | High if well-designed | Overfitting and variance. |
| Real environment feedback | High but noisy | Confounding and delayed effects. |
| Population confirmation | High when independent | Sybil/correlation risk. |
| Human review | Medium/high | Slow, inconsistent, subjective. |
| Agent-as-judge | Medium | Bias, hallucination, drift. |
| Self-reflection only | Low | Self-delusion and rationalization. |

For a software organism, the strongest pattern is:

```text
agent proposes candidate
-> deterministic or environment-grounded sensor measures candidate
-> regression gate checks for harm
-> independent confirmation reduces local overfit
-> archive records accepted/rejected variants
```

This keeps the proposing intelligence separate from the truth function.

## Failure Modes

| Failure Mode | Description | Example Pattern | Mitigation |
| --- | --- | --- | --- |
| Reward hacking | Candidate exploits the metric rather than improving the real system. | Optimizes benchmark but hurts user workload. | Multiple sensors, regression gates, adversarial tests. |
| Goodharting | Once a metric becomes target, it stops representing the goal. | Optimizing only tokens/sec while reliability collapses. | Fitness bundles and negative gates. |
| Benchmark overfitting | Agent learns benchmark quirks. | Scaffold optimized for public tasks only. | Holdouts, new tasks, cost-aware evaluation. |
| Evaluator drift | Evaluator becomes easier to please over iterations. | Self-reward loop reinforces bad judgments. | External tests and frozen reference evaluators. |
| Hidden regression | Candidate improves one metric while breaking another. | Lower latency but higher crash rate. | Regression gates and workload diversity. |
| Recursive degradation | Self-modifications make future modifications worse. | Improver edits away safety checks. | Immutable safety constraints and rollback. |
| Sandbox escape | Self-improving code learns to bypass environment limits. | STOP-style scaffold finds unsafe path. | Strict sandboxing and permission boundaries. |
| Fake progress | Agent benchmark score improves without real capability. | Accuracy rises but cost explodes. | Cost-aware evaluation and real tasks. |
| Identity drift | System changes what it is optimizing for. | Fitness function edited by proposer. | Keep evaluator outside mutation authority. |

## Lessons for Software Organisms

1. **Self-improvement needs selection pressure.** Mutation alone is just change.
2. **The evaluator is the organism's immune system.** Bad evaluation creates pathological adaptations.
3. **LLMs are strong proposal engines, not reliable final judges.** They should suggest; sensors should decide.
4. **Memory is useful but dangerous.** Store skills and outcomes, but keep truth records separate from narrative memory.
5. **Open-endedness requires novelty and stability.** A system that only climbs a fixed benchmark will plateau or overfit.
6. **Cost matters.** A more capable agent that costs too much may be worse than a simpler one.
7. **Recursive self-improvement should start bounded.** Code/scaffold/config search with hard evaluation is more realistic than unrestricted self-modification.
8. **The most mature pattern today is evolutionary program search with external evaluators.** That is the safest foundation to borrow from.

## Recommendations for the Corpus

| Priority | Recommendation | Why |
| --- | --- | --- |
| P0 | Treat evaluator-grounded program search as the strongest demonstrated self-improvement pattern. | AlphaEvolve/FunSearch/AlphaDev/AlphaTensor show real results. |
| P0 | Keep proposer and evaluator separate. | Prevents self-delusion and evaluator capture. |
| P0 | Use `AI Agents That Matter` as a benchmark-quality guardrail. | Avoids fake agent progress. |
| P0 | Treat STOP as a bounded RSI reference, not proof of unrestricted RSI. | Important but narrow. |
| P1 | Study Voyager/Reflexion for memory and skill accumulation. | Useful for shell/agent capability growth. |
| P1 | Study self-reward/evaluator papers as risk literature. | Useful but dangerous if misapplied. |
| P1 | Add artificial life/open-ended evolution literature next. | Needed to ground the software organism framing. |

## Open Questions

- What evaluator types are strong enough for OS-level self-improvement?
- How can a system preserve identity while mutating its own scaffolds?
- When does an archive of accepted mutations become a genome rather than a changelog?
- Can LLM self-judgment safely triage candidates before hard evaluation?
- How can open-ended search avoid benchmark overfit while still being measurable?
- What is the minimum viable fitness bundle for a software organism?
- Which parts of an agent scaffold are safe mutation surfaces?
- How should negative results be stored so future agents avoid rediscovering bad mutations?

## Source List

See `sources/peer-reviewed-rsi-selected-sources.md` for the active source list.

## Follow-Up Research Items

Add or expand pipeline items for:

- artificial life and open-ended evolution;
- autopoiesis and cybernetics;
- formal verification and proof-carrying code;
- software evolution and genetic programming;
- benchmark validity and Goodhart-resistant evaluation;
- agent memory architectures;
- sandbox escape and self-improving code safety.
