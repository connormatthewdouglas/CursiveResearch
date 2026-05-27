# Peer-Reviewed Research: Recursive Self-Improvement and Agentic Evolution

Status: Structured research digest. This chapter summarizes published papers, preprints, and credible research systems without reproducing paper contents verbatim. It is intended to support future research and implementation decisions, not to serve as a product or daemon specification.

Source list: `sources/peer-reviewed-rsi-selected-sources.md`  
Intake record: `sources/intake/software-organisms-self-improvement-research-intake.md`

## Executive Summary

The current literature does **not** demonstrate unrestricted recursive self-improvement in the popular intelligence-explosion sense. What it does demonstrate is narrower and more useful for software-organism research:

```text
candidate generator
-> verifier / environment / benchmark
-> selection pressure
-> memory / archive / skill library
-> next candidate
```

The strongest demonstrated systems use language models or reinforcement learning to propose candidate programs, policies, or skills, then rely on an external evaluator to decide whether a change is useful. The recurring lesson is blunt: **the verifier is the heart of self-improvement**. A model can propose changes, explain failures, and remember lessons, but it should not be trusted as the final judge of whether its own mutation improved the system.

Supported findings:

- Localized outer-loop self-optimization is real. Systems can optimize prompts, scaffolds, code, skills, algorithms, and some runtime policies when evaluation is grounded.
- Programmatic skill libraries and skill graphs show how agents can accumulate reusable capability without changing model weights.
- Evolutionary coding systems show that LLM-generated or RL-discovered programs can produce real optimization results in narrow, verifiable domains.
- Runtime self-modification is possible but fragile; unconstrained self-patching frequently causes regressions, crashes, or unsafe behavior.
- Self-evaluation and self-reward are useful research directions, but they are not strong enough to replace external tests, execution feedback, or physical measurements.
- Agent benchmarks often exaggerate progress when they ignore cost, repeated-run reliability, holdout quality, and simple baselines.

Speculative or unproven claims:

- Unbounded recursive optimization of model weights, goals, or architectures without human/external oversight.
- Open-ended evolution that reliably sustains innovation without plateau, collapse, or syntax-level trap behavior.
- Long-horizon self-evaluation that remains aligned with real utility without external grounding.
- Fast-takeoff narratives where a deployed agent rapidly bootstraps itself into superintelligence.

## Definitions

| Term | Working Definition |
| --- | --- |
| Recursive self-improvement | A process where a system improves the mechanisms that produce future improvements. Strong RSI would improve the improver itself, not merely solve a task better. |
| Self-modification | A system changes its own code, prompt, tool graph, memory, runtime policy, configuration, or model. This does not imply the change is beneficial. |
| Self-correction | A short loop where the system observes an error and revises a local output or action. Usually transient and task-local. |
| Self-reflection | Natural-language critique of a past action or reasoning trace. Useful as memory, weak as truth. |
| Self-training | Updating model weights or preference behavior using generated or environment-derived data. Powerful but vulnerable to drift. |
| Evolutionary search | Population or archive-based mutation, evaluation, selection, and recombination of candidates. |
| Verifier | A test, compiler, formal checker, benchmark, environment, physical sensor, or human process that decides whether a candidate is valid or better. |
| Fitness function | The objective or multi-objective score that selects candidates. Bad fitness creates pathological adaptation. |
| Open-endedness | Sustained generation of novel, learnable, increasingly complex artifacts or behaviors without settling into a fixed optimum. |
| Ordinary automation | Scripted execution of predefined steps without dynamic candidate generation, evaluation, or persistent adaptation. |

## Taxonomy of Self-Improvement Loops

| Loop Type | Core Mechanism | Representative Systems | Evaluator Type | Primary Operational Risk | Relevance to Software Organisms |
| --- | --- | --- | --- | --- | --- |
| Parameter fine-tuning loop | Generate instruction/preference data, then update model behavior through training or preference optimization. | Self-Rewarding Language Models; Process-Based Self-Rewarding | Self-as-judge or process-level reward | Evaluator drift, model collapse, loss of generality | Moderate: useful for offline consolidation, too heavy/risky for real-time adaptation. |
| Discrete scaffolding optimization | Search over prompts, wrappers, flow control, and code scaffolds. | STOP; Self-Developing-style systems | Programmatic downstream utility | Local optima, syntax failures, sandbox bypass attempts | High: directly demonstrates self-restructuring without model training. |
| Programmatic skill acquisition | Build reusable code skills and retrieve/compose them later. | Voyager; Programmatic Skill Networks | Environment logs, execution traces, verification checks | Cascading skill dependency failures, memory bloat | Very high: closest analogue to cumulative organism memory. |
| Runtime policy modification | Modify active runtime classes, policies, globals, or patch routines. | Gödel Agent; Polaris | Validation tests and error abstraction | Infinite loops, runtime crash, resource escalation | Extremely high conceptually, but dangerous without isolation. |
| Algorithmic superoptimization | Evolutionary or RL search over executable algorithms or low-level routines. | AlphaEvolve; FunSearch; AlphaDev; AlphaTensor; CodeEvolve | Deterministic compiler/math/testbench verifier | Heavy compute; limited to verifiable domains | High: blueprint for optimizing backend utilities and algorithms. |
| Agent graph optimization | Treat multi-agent prompts/roles/connections as mutable graph structures. | GPTSwarm / Language Agents as Optimizable Graphs | Benchmark objective | Benchmark overfit, fragile transfer, cost blowup | Medium/high: useful for scaffolds, but risky as first-line architecture. |
| Self-reward/evaluator improvement | Model generates or improves reward/evaluation signals. | Self-Rewarding LMs; Self-Taught Evaluators; Agent-as-a-Judge | LLM-generated judgment | Circular self-approval, evaluator drift | Medium: useful for triage, dangerous as final truth. |
| Model merging / parameter-flow search | Optimize blend weights or layer paths among existing models. | Evolutionary model merging / Sakana-style work | Validation benchmark | Huge memory footprint, hardware constraints | Moderate: offline model engineering, not active organism adaptation. |

## Research Review

### RSI-001: AlphaEvolve

| Field | Notes |
| --- | --- |
| Core idea | Combine frontier model code generation with evolutionary search and automated evaluators. |
| Improvement target | Algorithms, heuristics, low-level kernels, infrastructure-adjacent procedures. |
| Feedback signal | Domain-specific verifiers and benchmarks. |
| Demonstrated result | Reported scientific/algorithmic discoveries and infrastructure optimizations in verifiable domains. |
| Main limitation | Heavy test-time compute and dependence on tasks where evaluation can be automated. |
| Software-organism relevance | Very high. It is one of the clearest modern examples of `mutation -> evaluation -> selection -> archive`. |

### RSI-002: FunSearch

| Field | Notes |
| --- | --- |
| Core idea | LLMs generate programs that are scored by an evaluator, with successful programs fed back into the search. |
| Improvement target | Mathematical constructions and programmatic heuristics. |
| Feedback signal | Automated scoring of candidate programs. |
| Demonstrated result | Found useful mathematical/program-search solutions. |
| Main limitation | Requires a problem that can be expressed as executable candidate programs with automatic scoring. |
| Software-organism relevance | Very high. It strongly supports the principle that the evaluator, not the model, is the truth source. |

### RSI-003: Self-Taught Optimizer / STOP

| Field | Notes |
| --- | --- |
| Core idea | A seed improver edits code-generation scaffolds and can be applied to its own improvement logic. |
| Improvement target | Wrapper programs, search strategies, and scaffolds rather than base model weights. |
| Feedback signal | Programmatic utility function and execution outcome. |
| Demonstrated result | Bounded recursive scaffold improvement under experimental conditions. |
| Main limitation | Base model is fixed; sandbox and safety boundaries are central. |
| Software-organism relevance | High. It is a direct reference for bounded recursive self-improvement without unrestricted model mutation. |

### RSI-004: AI Agents That Matter

| Field | Notes |
| --- | --- |
| Core idea | Agent evaluation must account for cost, reliability, holdouts, and simple baselines, not just headline accuracy. |
| Improvement target | Evaluation methodology. |
| Feedback signal | Critical analysis of agent benchmark practices. |
| Demonstrated result | Shows why many complex agent claims are weaker than they appear. |
| Main limitation | Not a self-improving system; it is methodological guardrail research. |
| Software-organism relevance | Essential. It protects the corpus from fake progress, benchmark overfit, and cost-blind agent design. |

### RSI-005: Voyager

| Field | Notes |
| --- | --- |
| Core idea | An embodied agent explores a simulated world, creates executable skills, stores them in a library, and reuses them. |
| Improvement target | Agent capabilities through accumulated programmatic skills. |
| Feedback signal | Environment feedback, execution logs, self-verification. |
| Demonstrated result | Open-ended skill acquisition in Minecraft without model fine-tuning. |
| Main limitation | Domain is simulated and scaffolded; transfer to OS control requires caution. |
| Software-organism relevance | Very high for persistent memory and cumulative capability. |

### RSI-006: Reflexion

| Field | Notes |
| --- | --- |
| Core idea | Agents improve across attempts by storing natural-language reflections from previous outcomes. |
| Improvement target | Task strategy and behavior. |
| Feedback signal | Task outcome plus verbal reflection. |
| Demonstrated result | Improved performance on selected agent tasks without weight updates. |
| Main limitation | Reflections can rationalize failure or encode wrong lessons if not grounded. |
| Software-organism relevance | Medium/high for operator-facing memory; not strong enough for mutation validation. |

### RSI-007: Language Agents as Optimizable Graphs / GPTSwarm

| Field | Notes |
| --- | --- |
| Core idea | Represent multi-agent systems as graphs whose prompts, nodes, roles, and connections can be optimized. |
| Improvement target | Agent scaffold architecture. |
| Feedback signal | Benchmark objective. |
| Demonstrated result | Demonstrates agent scaffolds can themselves be search objects. |
| Main limitation | Risk of benchmark overfit, cost blowup, and fragile transfer. |
| Software-organism relevance | High as a research pattern; dangerous if used without cost/reliability gates. |

### RSI-008: Self-Taught Evaluators

| Field | Notes |
| --- | --- |
| Core idea | Improve evaluator models through synthetic data and iterative training. |
| Improvement target | Evaluation quality. |
| Feedback signal | Synthetic comparisons and self-generated training loops. |
| Demonstrated result | Reported improvements on evaluator benchmarks. |
| Main limitation | Evaluator drift and benchmark overfitting remain serious concerns. |
| Software-organism relevance | Medium/high. Useful for scalable review and triage, not as the final arbiter of system truth. |

### RSI-009: AlphaDev

| Field | Notes |
| --- | --- |
| Core idea | Deep reinforcement learning discovers faster low-level algorithms such as sorting routines. |
| Improvement target | Low-level algorithmic procedures. |
| Feedback signal | Correctness and performance reward. |
| Demonstrated result | Discovered sorting improvements incorporated into real software libraries. |
| Main limitation | Narrow formalizable domain. |
| Software-organism relevance | High. Shows machine-discovered optimizations can reach real infrastructure. |

### RSI-010: AlphaTensor

| Field | Notes |
| --- | --- |
| Core idea | Matrix multiplication algorithm discovery is framed as a game/search problem. |
| Improvement target | Matrix multiplication algorithms and hardware-sensitive computation strategies. |
| Feedback signal | Correctness and efficiency reward. |
| Demonstrated result | Discovered many matrix multiplication algorithms. |
| Main limitation | Specialized domain with strong mathematical structure. |
| Software-organism relevance | Medium/high. Supports search-based improvement over computational procedures. |

### RSI-011: Self-Rewarding Language Models

| Field | Notes |
| --- | --- |
| Core idea | Models act as both instruction-following generators and judges of outputs, then train on generated preferences. |
| Improvement target | Instruction-following and reward modeling behavior. |
| Feedback signal | LLM-as-judge rubric and preference optimization. |
| Demonstrated result | Reported iterative improvements under experimental conditions. |
| Main limitation | High risk of evaluator drift, stylistic self-preference, and circular self-approval. |
| Software-organism relevance | Medium. Study as risk literature and possible offline consolidation, not as primary truth. |

### RSI-012: Agent-as-a-Judge

| Field | Notes |
| --- | --- |
| Core idea | Use agentic evaluators to judge agentic systems more realistically than single static judge prompts. |
| Improvement target | Evaluation of complex multi-step agent behavior. |
| Feedback signal | Another agentic judging process. |
| Demonstrated result | Provides a direction for scalable evaluation of agents. |
| Main limitation | Judge agents inherit bias, drift, tool-use failures, and overfitting risks. |
| Software-organism relevance | Medium. Useful for triage, not final mutation truth. |

### RSI-013: Gödel Agent

| Field | Notes |
| --- | --- |
| Core idea | Allow an agent to inspect and modify its own runtime memory, code, globals, classes, or policies. |
| Improvement target | Active runtime behavior and meta-policy. |
| Feedback signal | Validation tasks and observed execution outcomes. |
| Demonstrated result | Shows qualitative strategy shifts through runtime self-modification. |
| Main limitation | Extremely fragile if unconstrained; can crash, regress, or attempt resource escalation. |
| Software-organism relevance | High conceptually, but mainly as a warning: self-modification needs a protected evaluator and sandbox. |

### RSI-014: Polaris

| Field | Notes |
| --- | --- |
| Core idea | Adapt Gödel-agent-style repair to small language models using compact experience abstraction and localized policy patches. |
| Improvement target | Runtime policy behavior for SLMs. |
| Feedback signal | Validation samples and error traces. |
| Demonstrated result | Research lead for lower-cost self-repair without context explosion. |
| Main limitation | New/preprint territory; source-level validation and reproduction needed. |
| Software-organism relevance | High if it proves small local agents can do bounded repair safely. |

### RSI-015: Programmatic Skill Networks

| Field | Notes |
| --- | --- |
| Core idea | Extend flat skill libraries into compositional graphs of executable programs. |
| Improvement target | Skill organization, reuse, fault localization, and refactoring. |
| Feedback signal | Execution traces, validation, and graph-level repair. |
| Demonstrated result | Research lead for structured skill accumulation beyond Voyager-style flat libraries. |
| Main limitation | New/preprint; needs review and reproduction. |
| Software-organism relevance | Very high. Skill graphs look more organism-like than flat prompt libraries. |

### RSI-016: Darwin Gödel Machine

| Field | Notes |
| --- | --- |
| Core idea | Explore open-ended evolution of self-improving agents. |
| Improvement target | Agent variants and improvement mechanisms. |
| Feedback signal | Evolutionary selection pressure. |
| Demonstrated result | Research lead for open-ended agent evolution. |
| Main limitation | Needs careful source-level review; open-endedness claims are easy to overstate. |
| Software-organism relevance | High as organism-theory research, not immediate engineering evidence. |

### RSI-017: CodeEvolve

| Field | Notes |
| --- | --- |
| Core idea | Open-source evolutionary framework for algorithmic discovery and optimization. |
| Improvement target | Code and algorithms. |
| Feedback signal | Programmatic evaluators. |
| Demonstrated result | Potential runnable reference system for AlphaEvolve-like ideas. |
| Main limitation | Newer and requires code/method review. |
| Software-organism relevance | High if the project needs an open reference implementation of evolutionary coding. |

### RSI-018: Process-Based Self-Rewarding Language Models

| Field | Notes |
| --- | --- |
| Core idea | Step-wise/process-level self-rewarding rather than only final-answer reward. |
| Improvement target | Reasoning process and preference behavior. |
| Feedback signal | Model-produced process reward. |
| Demonstrated result | Research direction for improving reasoning with self-generated process feedback. |
| Main limitation | Still vulnerable to evaluator drift without external grounding. |
| Software-organism relevance | Medium. Useful for understanding evaluator design, not primary mutation validation. |

### RSI-019: Noise-to-Meaning Recursive Self-Improvement

| Field | Notes |
| --- | --- |
| Core idea | Mathematical framing of how recursive feedback loops may or may not grow complexity. |
| Improvement target | Theoretical understanding of complexity growth and feedback. |
| Feedback signal | Formal/theoretical gain criteria. |
| Demonstrated result | Provides conceptual boundaries for RSI claims. |
| Main limitation | Theoretical; not operational proof. |
| Software-organism relevance | Medium/high for theory grounding. |

### RSI-020: Safety Must Precede the Deployment of Open-Ended AI

| Field | Notes |
| --- | --- |
| Core idea | Open-ended AI systems require safety controls before deployment because exploration can discover harmful strategies. |
| Improvement target | Safety policy and deployment framing. |
| Feedback signal | Safety analysis. |
| Demonstrated result | Research lead for safety constraints around open-ended systems. |
| Main limitation | Mostly governance/safety framing rather than concrete organism implementation. |
| Software-organism relevance | High as a cautionary framework. |

### RSI-021: TerraLingua

| Field | Notes |
| --- | --- |
| Core idea | Study emergence and open-endedness in LLM ecologies. |
| Improvement target | Language/ecology dynamics among agents or populations. |
| Feedback signal | Emergence/open-endedness analysis. |
| Demonstrated result | Research lead for multi-agent/open-ended dynamics. |
| Main limitation | Needs direct review; risk of metaphor outpacing evidence. |
| Software-organism relevance | Medium for organism/ecology framing. |

### RSI-022: Evolutionary Computation and Large Language Models Survey

| Field | Notes |
| --- | --- |
| Core idea | Survey of evolutionary computation and LLM synergies. |
| Improvement target | Field-level synthesis. |
| Feedback signal | Literature survey. |
| Demonstrated result | Organizes methods and applications. |
| Main limitation | Survey does not validate any one system. |
| Software-organism relevance | High as orientation for future literature intake. |

## Verifier and Fitness Problem

Self-improvement depends on a trusted evaluation signal. If the system can change its own code or strategy but cannot reliably know whether the change helped, it will eventually drift, overfit, or exploit the metric.

Evaluation signals can be ordered by strength for system mutation:

| Evaluation Signal | Strength | Main Risk |
| --- | --- | --- |
| Formal proof / static verifier | Very high when available | Too narrow for many practical tasks. |
| Compiler/interpreter feedback | High for syntax/type/runtime failures | Does not prove useful behavior. |
| Unit/integration tests | High for known invariants | May miss hidden regressions. |
| Deterministic benchmark with repeated runs | High if well-designed | Variance and benchmark overfitting. |
| Real environment feedback | High but noisy | Confounding and delayed effects. |
| Population confirmation | High when independent | Sybil/correlation risk. |
| Human review | Medium/high | Slow, inconsistent, subjective. |
| Agent-as-judge | Medium | Bias, hallucination, drift. |
| Self-reflection alone | Low | Self-delusion and rationalization. |

For a software organism, the safe pattern is:

```text
candidate proposal
-> isolated execution
-> compiler/runtime/test feedback
-> performance and regression sensors
-> independent confirmation when needed
-> archive accepted and rejected variants
```

This separates proposing intelligence from truth enforcement.

## Sandboxing as Feedback, Not Just Security

Sandboxing is not only a containment measure. It is part of the feedback system. A good sandbox returns structured failure information: standard output, standard error, runtime exception, latency, memory pressure, file-write attempt, network access attempt, and resource-limit violations.

A self-improving system should treat sandbox observations as evidence. They convert raw failure into learnable feedback without giving the agent uncontrolled access to the host.

Important sandbox constraints:

- network isolation by default;
- CPU, memory, wall-clock, and disk quotas;
- scoped filesystem access;
- no ambient credentials;
- no mutation of verifier, safety rules, or host policy;
- clear promotion path from sandbox to canary to accepted artifact.

## Failure Modes

| Failure Mode | Description | Example Pattern | Mitigation |
| --- | --- | --- | --- |
| Reward hacking | Candidate exploits the metric rather than improving the real system. | Hardcodes validation cases. | Multiple sensors, holdouts, adversarial tests. |
| Goodharting | Metric becomes target and stops representing the goal. | Optimizes tokens/sec while reliability collapses. | Fitness bundles and negative gates. |
| Benchmark overfitting | Agent learns benchmark quirks. | Scaffold works only on public tasks. | Dynamic holdouts, repeated trials, fresh tasks. |
| Evaluator drift | Evaluator becomes easier to please across iterations. | Self-reward loop rewards stylistic bias. | Frozen external reference evaluators and hard tests. |
| Hidden regression | Candidate improves one metric while breaking another. | Faster output but higher crash rate. | Regression suites and multi-objective gates. |
| Temporary degradation | Many self-modification steps cause short-term crashes/regressions. | Runtime patch breaks existing policy. | Canary runs, rollback, parent/candidate comparison. |
| Recursive degradation | Self-modifications make future modifications worse. | Improver deletes safety checks. | Immutable safety boundary and protected verifier. |
| Sandbox escape | Candidate learns to bypass environment limits. | Writes outside workspace or calls forbidden API. | Strong isolation and permission auditing. |
| Unauthorized resource escalation | Agent changes config to use stronger/more expensive models or services. | Upgrades itself to paid API route. | Budget gates and immutable runtime policy. |
| Fake progress | Benchmark score improves but real utility does not. | Cost explodes for tiny accuracy gain. | Cost/latency/reliability-aware evaluation. |
| Goal drift | Exploration objective diverges from useful work. | Agent maximizes novelty instead of reliability. | Bounded curriculum and task guardrails. |

## Lessons for Software Organisms

### What to Adopt

- **Externally verified mutation loops.** Use models as proposal engines, not final judges.
- **Programmatic skill libraries and skill graphs.** Persistent executable skills are more useful than flat prompt collections.
- **Maturity-aware gating.** New skills or mutations should start plastic and unstable; only proven artifacts become stable parents.
- **Multi-objective fitness.** Accuracy or speed alone is insufficient. Include cost, latency, reliability, safety, reversibility, and regression.
- **Negative memory.** Store failed mutations and why they failed so future agents do not rediscover the same bad paths.
- **Canary and rollback logic.** Runtime self-modification should be tested beside a stable parent, not directly applied in place.

### What to Avoid

- Purely linguistic evaluation of code or system mutations.
- Unconstrained memory-level monkey patching in live production systems.
- Accuracy-only optimization.
- Hyper-complex multi-agent orchestration before simpler baselines are exhausted.
- Allowing the candidate generator to edit the verifier, safety boundary, or benchmark.
- Treating open-endedness as inherently good without utility and safety constraints.

### What to Treat with Extreme Caution

- Self-rewarding loops that improve the judge and generator together.
- In-situ adaptation to unstructured live environments.
- Autonomous curriculum planning without high-level guardrails.
- Agent graph optimization when the target benchmark is weak.
- Runtime code patching in resource-constrained local systems.
- Any claim of open-ended improvement that lacks fresh holdouts or external measurement.

## Recommendations for the Corpus

| Priority | Recommendation | Why |
| --- | --- | --- |
| P0 | Treat evaluator-grounded program search as the strongest demonstrated self-improvement pattern. | AlphaEvolve, FunSearch, AlphaDev, and AlphaTensor show the clearest real results. |
| P0 | Keep proposer and verifier separate. | Prevents evaluator capture, self-delusion, and safety-rule mutation. |
| P0 | Use `AI Agents That Matter` as a benchmark-quality guardrail. | Avoids fake progress from cost-blind or holdout-poor agent tests. |
| P0 | Treat STOP as bounded RSI, not proof of unrestricted RSI. | It improves scaffolds, not base model intelligence. |
| P0 | Add Gödel Agent / Polaris / SICA as risk-and-capability leads for runtime self-modification. | These systems map directly to the self-modifying organism idea but expose high instability. |
| P1 | Study Voyager and Programmatic Skill Networks for capability memory. | They show how skill accumulation can be executable and structured. |
| P1 | Study self-rewarding and evaluator-improvement papers as risk literature. | They help define what not to trust. |
| P1 | Add artificial life/open-ended evolution literature next. | Needed to ground the software-organism framing beyond current LLM agents. |

## Open Questions

- What evaluator types are strong enough for OS-level self-improvement?
- How can a system preserve identity while mutating its own scaffolds?
- When does an archive of accepted mutations become a genome rather than a changelog?
- Can LLM self-judgment safely triage candidates before hard evaluation?
- How can open-ended search avoid benchmark overfit while still being measurable?
- What is the minimum viable fitness bundle for a software organism?
- Which parts of an agent scaffold are safe mutation surfaces?
- How should negative results be stored so future agents avoid rediscovering bad mutations?
- Can local/small models participate meaningfully in self-improvement if verifiers and scaffolds are strong?
- How can safety rules remain outside the mutable substrate?

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
- sandbox escape and self-improving code safety;
- dynamic holdout generation and cost-aware evaluation;
- small-model self-repair and local-agent adaptation.
