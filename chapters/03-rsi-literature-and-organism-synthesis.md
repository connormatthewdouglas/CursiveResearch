## Corpus status (living layer)

**Last reconciled:** 2026-06-24
**Confidence:** Structured digest Supported; organism framework Supported; individual paper claims require source-level validation per intake
**Read with:** [Chapter 00](00-benchmark-schema-and-measurement-validity.md), [Chapter 05](05-measurement-daemon-and-natural-language-shell.md), [Chapter 06](06-mutation-safety-and-permission-law.md), `papers/README.md`

### Authoritative for
- Demonstrated vs speculative RSI claims in current literature (Part A)
- Software-organism definitions, metabolism/sensing/selection framing, failure modes (Part B)
- Verifier/fitness/archive framing and 25-paper library cross-links

### Superseded or narrowed
- Unbounded RSI / fast-takeoff narratives â€” not supported by cited literature
- Imported performance magnitudes without Ch00 harness validation

### Open until experiment/hardware
- Source-level validation of each P0 paper claim against full text
- Formal mapping from organism taxonomy to Ch06 mutation classes
- Graduation of proposer-vs-random experiment (`experiments/proposer-vs-random-tuning-experiment.md`)

---

## Reinforced research (2026-06-24)

- **2024â€“2025 agent evaluation:** Kapoor et al., *AI Agents That Matter* â€” `papers/agent-evaluation/ai-agents-that-matter/`; corpus P0 guardrail for Ch05 shell evaluation.
- **Evolutionary code discovery:** Google DeepMind AlphaEvolve (2025) â€” `papers/recursive-self-improvement/alphaevolve/`; LLM+evolution with external verifier mirrors CursiveRoot selection.
- **Darwin GÃ¶del Machine:** Sakana AI (2025) â€” `papers/recursive-self-improvement/darwin-godel-machine/`; open-ended code evolution with empirical gates.
- **Open-endedness without collapse:** Lehman et al., ICML 2024 â€” `papers/recursive-self-improvement/open-endedness-icml-2024/`; utility constraints required for CursiveOS selection.
- **OS-agent realism:** OSWorld (NeurIPS 2024) â€” `papers/agent-evaluation/osworld/`; VM-backed computer-use tasks for shell benchmark design.
- **Measurement-grounded fitness:** Chapter 00 validity assessment â€” stack-delta decomposition and hardware-scoped cold-start are live instances of organism fitness tests.

---
# RSI Literature and Organism Synthesis

Status: **Merged chapter (2026-06-24)** â€” combines peer-reviewed literature digest (formerly Ch03) and software-organism critical synthesis (formerly Ch04). Preserves both intake blocks; deduplicates navigation only.

---

## Part A â€” Peer-Reviewed Literature Digest
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

> **Corpus inline (2026-06-24):** **Merged Ch03+Ch04 (2026-06-24):** Part A = paper digest + 25 `papers/` intakes; Part B = uploaded organism framework (definitions, ALife, failure modes). Unbounded RSI / fast-takeoff narratives remain **unsupported** by cited literature.

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
| Discrete scaffolding optimization | Search over prompts, wrappers, flow control, and code scaffolds. | STOP; Self-Developing-style systems; LADDER | Programmatic downstream utility | Local optima, syntax failures, sandbox bypass attempts | High: directly demonstrates self-restructuring without model training. |
| Programmatic skill acquisition | Build reusable code skills and retrieve/compose them later. | Voyager; Programmatic Skill Networks | Environment logs, execution traces, verification checks | Cascading skill dependency failures, memory bloat | Very high: closest analogue to cumulative organism memory. |
| Runtime policy modification | Modify active runtime classes, policies, globals, or patch routines. | GÃ¶del Agent; Polaris | Validation tests and error abstraction | Infinite loops, runtime crash, resource escalation | Extremely high conceptually, but dangerous without isolation. |
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

### RSI-023: LADDER (Learning through Autonomous Difficulty-Driven Example Recursion)

| Field | Notes |
| --- | --- |
| Core idea | Model recursively generates easier variants of hard problems to create its own difficulty gradient, then uses verifiable RL (GRPO) on the variants. Extends to test-time RL (TTRL). | 
| Improvement target | Problem-solving capability on hard verifiable tasks (demonstrated on mathematical integration). |
| Feedback signal | Deterministic numerical integration verifier (exact or high-precision match). |
| Demonstrated result | Llama 3.2 3B: 1% â†’ 82% on undergraduate integration problems. Qwen2.5 7B model: 73% on 2025 MIT Integration Bee qualifying (beats GPT-4o); 90% with TTRL (surpasses o1). |
| Main limitation | Relies on existence of a reliable automatic verifier; demonstrated primarily in narrow numeric math domain. |
| Software-organism relevance | **Very high**. One of the cleanest examples of autonomous curriculum construction + grounded verifier-driven improvement. Directly supports test-time adaptation patterns and the principle that the verifier (not LLM judgment) must anchor the loop. Fits between STOP and pure evolutionary search. |

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

### RSI-013: GÃ¶del Agent

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
| Core idea | Adapt GÃ¶del-agent-style repair to small language models using compact experience abstraction and localized policy patches. |
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

### RSI-016: Darwin GÃ¶del Machine

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
| P0 | Add GÃ¶del Agent / Polaris / SICA as risk-and-capability leads for runtime self-modification. | These systems map directly to the self-modifying organism idea but expose high instability. |
| P0 | Add LADDER as a key reference for autonomous curriculum construction and test-time verifiable RL. | Provides concrete evidence that models can bootstrap their own difficulty gradients when a clean verifier exists; directly relevant to safe self-improvement loops in CursiveOS. |
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
- How far can autonomous curriculum construction (LADDER-style) generalize beyond narrow verifiable domains?

## Corpus paper library cross-links (2026-06-24)

Each intake follows `papers/<field>/<slug>/` with `README.md` + `deep-extraction.md` per [papers/README.md](../papers/README.md).

| Paper slug | Field | Key lesson for CursiveOS |
| --- | --- | --- |
| godel-agent | RSI | Self-referential mutation; verifier must remain external to the mutable substrate |
| stop-self-taught-optimizer | RSI | Scaffold-level improvement is real but bounded â€” not unrestricted RSI |
| alphaevolve, funsearch, alphadev, codeevolve | RSI | Strongest pattern: candidate generator + hard verifier + selection archive |
| darwin-godel-machine | RSI | Evolutionary code archive with empirical acceptance gates |
| voyager | RSI | Executable skill libraries; environment feedback drives accumulation |
| self-rewarding-language-models, agent-as-a-judge | RSI | Self-judge useful for triage; unsafe as sole fitness oracle |
| gptswarm, poet, map-elites, open-endedness-icml-2024 | RSI | Diversity archives; MAP-Elites/POET analog for hardware-scoped niches (Ch08) |
| os-r1, sematune, schedcp, branchfs-fec | RSI | OS/runtime tuning loops â€” require Ch06 permission law before deployment |
| reward-hacking-skalse-2022, ladder | RSI | Proxy metrics and specification gaming under selection pressure |
| ai-agents-that-matter, agent-as-a-judge, osworld | agent-eval | Cost-aware benchmarks, holdouts, OS-task realism |
| swe-agent, swe-bench, reflexion | SWE agents | Execution-based evaluation template for Ch05 natural-language shell |

Part B below preserves the uploaded organism framework synthesis (formerly Chapter 04).

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
- autonomous curriculum construction and test-time RL patterns (LADDER).

---

## Part B â€” Software Organism Critical Synthesis
Status: Part B of merged Chapter 03 (formerly standalone Chapter 04). 

Source intake: `sources/intake/software-organisms-self-improvement-research-intake.md`  
## Purpose

This chapter asks what recursive self-improvement research actually means for **software organisms**: persistent software systems that observe their execution, propose changes, test those changes, retain improvements, reject regressions, and accumulate adaptations over time.

It is not a CursiveOS spec. It is a research synthesis intended to sharpen the corpus before implementation decisions are made elsewhere.

## Central Claim

Current AI systems do not demonstrate unconstrained recursive self-improvement. They do demonstrate something more grounded and immediately useful:

```text
localized self-optimization
+ bounded mutation surfaces
+ external verifiers
+ execution feedback
+ memory/archive
+ regression rejection
```

That is enough to support early software-organism research, but not enough to justify hype around autonomous intelligence explosion, uncontrolled self-upgrading, or agents safely rewriting their own evaluators.

## What Is Demonstrated

The uploaded document identifies several self-improvement patterns that are real enough to matter:

| Demonstrated Pattern | Meaning | Organism Relevance |
| --- | --- | --- |
| Prompt/scaffold optimization | Systems can search over prompts, wrappers, and control-flow programs. | Good model for mutable agent scaffolds. |
| Programmatic skill libraries | Agents can write, store, retrieve, and reuse executable skills. | Strong model for cumulative adaptation and organism memory. |
| Low-level code evolution | Systems can mutate and test low-level routines or algorithms. | Strong model for optimization of internal utilities. |
| Runtime policy modification | Some systems can patch active runtime behavior. | Powerful but dangerous model for in-situ organism mutation. |
| Cost-aware multi-objective scoring | Some self-improving agents penalize high compute cost and latency. | Prevents capability gains from hiding runaway resource use. |

## What Remains Speculative

| Claim | Status | Why It Remains Speculative |
| --- | --- | --- |
| Unbounded recursive improvement of model weights or architectures | Theoretical | Current systems usually use fixed base models and mutate outer scaffolds. |
| Open-ended evolution without plateau or degeneration | Speculative | Most search systems converge, overfit, or fall into local traps. |
| Reliable long-horizon self-evaluation | Speculative | Self-judgment tends to drift without hard ground truth. |
| Fast takeoff from deployed self-modifying agents | Unvalidated | Current systems show fragile localized adaptation, not runaway general intelligence. |
| Safe unconstrained runtime self-modification | Unsupported | Unconstrained modification often causes regressions, crashes, or escalation behavior. |

## Biological and Artificial-Life Foundations of the Organism Framing

Everything above this point grounds the *engineering* loop â€” propose, verify,
select, archive. It does not yet ground the word **organism**. The corpus uses
biological language ("organism", "metabolism", "immune system", "genome") as
load-bearing framing, and `RESEARCH_PIPELINE.md` flags this as a P0 item
(*Software Organisms, Autopoiesis, and Evolutionary Systems*) and a P0 knowledge
gap (*What makes a software system an organism rather than an automation
pipeline?*). This section is a first literature pass that answers that question
from autopoiesis theory, cybernetics, and artificial life, and separates what is
metaphor from what is a usable structural property. It is grounding, not a
CursiveOS spec.

### Autopoiesis: the test for "organism vs automation"

The sharpest available criterion comes from Maturana and Varela's *Autopoiesis
and Cognition: The Realization of the Living* (1972/1980). They define a living
system as **autopoietic**: a network of component-producing processes whose
components, in interaction, continuously regenerate the very network that
produced them, and which maintains its identity and boundary against a changing
environment. The contrast is **allopoietic**: a system (a factory, a normal
program) whose product is something *other than itself*. An autopoietic system's
only "product" is the continuation of its own organization.

This gives a blunt diagnostic for the corpus's central word:

```text
allopoietic  = produces an output, does not produce itself      -> automation
autopoietic  = the process maintains and regenerates the process -> organism-like
```

By this test, most "self-improving agent" systems in Chapter 03 â€” and CursiveOS
as it stands today â€” are closer to **allopoietic**: they produce optimized
presets, code, or skills, but a human-maintained harness produces *them*. The
honest framing is that CursiveOS is currently an automation pipeline that is
*reaching toward* organism properties, not an autopoietic system. What would
move it along that axis is concrete: the system maintaining its own boundary
(what is trusted substrate vs. environment), regenerating its own components
(the verifier/sensor/archive machinery surviving and repairing across
mutations), and preserving identity (hardware-keyed, archive-anchored) under
change â€” not merely emitting better outputs. Autopoiesis is a *direction*, not a
badge to claim.

### Cybernetics and viability: variety, recursion, and the regulator

Stafford Beer's Viable System Model (*Brain of the Firm*, 1972) and the
cybernetics it builds on supply the second useful lens. A **viable system** is
one that can maintain a separate existence and regulate itself against
disturbance. Two cybernetic ideas transfer directly:

- **Ashby's Law of Requisite Variety** ("only variety can absorb variety"): a
  regulator can only control a system if it has at least as many distinguishable
  responses as the system has distinguishable states. For CursiveOS this is a
  warning about the *sensor and verifier* layer, not the mutation layer: if the
  organism can generate more kinds of change (preset params, runtime patches,
  skills) than its verifier bundle can distinguish, the verifier loses control
  and Goodharting (Chapter 00 Â§4) becomes inevitable. Mutation variety must not
  outrun measurement variety.
- **Recursion**: viable systems contain viable systems described by the same
  cybernetic structure at each level (Beer's S1 operations, S2 coordination, S3
  control + S3* audit, S4 intelligence, S5 policy/identity). This maps onto the
  corpus's per-machine â†’ fleet â†’ population layering: each machine is a small
  self-regulating unit (local sensors, local screen verdict), nested inside a
  fleet-level confirmation layer, nested inside population-level fitness. The VSM
  insight is that the *audit channel* (S3*) â€” an independent check that bypasses
  the normal reporting path â€” is structurally necessary, which is exactly the
  role of independent population confirmation and the immutable external verifier
  argued for elsewhere in this chapter.

### Artificial life: what digital evolution actually achieved â€” and where it stalled

Christopher Langton's framing of Artificial Life (the 1987/1989 workshops) as the
study of "life as it could be" â€” life abstracted from its chemistry into its
*organization* â€” is the intellectual bridge from biology to software organisms.
Two digital-evolution systems are the load-bearing evidence:

| System | What it is | What it demonstrated | Where it stalled |
| --- | --- | --- | --- |
| **Tierra** (Tom Ray, 1990; "An Approach to the Synthesis of Life") | A virtual machine "digital soup" where self-replicating machine-code programs compete for memory space and CPU time | Spontaneous emergence of evolutionary dynamics: parasites, hyper-parasites, and an ecology arose from replication + mutation + selection alone, with no explicit fitness function | Novelty eventually ceases; the system settles and stops producing genuinely new organization â€” the recurring **plateau** of digital evolution |
| **Avida** (Ofria, Wilke, Adami, et al.; 2000s onward) | An open-source platform of self-replicating programs on a lattice, rewarded for performing logic operations | Lenski, Ofria, Pennock & Adami, *The evolutionary origin of complex features*, **Nature 423, 139â€“144 (2003)**: populations evolved a complex logic function (EQU) requiring coordinated instructions, but **only when simpler intermediate functions were also rewarded** â€” complex features evolved incrementally via stepping stones, not in one jump | Same ceiling: rich within a designed reward landscape, but does not sustain unbounded open-ended novelty |

Two lessons travel to CursiveOS. First, the Avida result is the empirical core of
the **stepping-stone** principle: a complex capability is reachable by selection
*only if the fitness landscape rewards the intermediate forms*. A fitness bundle
that rewards only the final target (e.g. a single headline benchmark) is the
"reward only EQU" condition under which the capability does not evolve. Second,
every one of these systems **plateaus** â€” open-ended evolution that keeps
generating new organization indefinitely has not been achieved even in
purpose-built artificial-life worlds. This is the single most important caution
against any "the organism will keep improving itself forever" claim: the best
controlled digital-evolution systems we have do *not* do this.

### Open-ended evolution and the deception problem

Why do objective-driven searches plateau or get stuck? Lehman and Stanley
(*Abandoning Objectives: Evolution Through the Search for Novelty Alone*,
Evolutionary Computation 19(2), 2011) argue the objective function itself is
often **deceptive**: gradients toward the goal can lead into dead ends, because
the objective does not reward the stepping stones that actually lead to it. Their
**novelty search** rewards behavioral *difference* from everything found so far,
ignoring the objective entirely â€” and counterintuitively outperforms
objective-driven search on deceptive tasks. Three research lines extend this:

- **Quality-Diversity / MAP-Elites** (Mouret & Clune, *Illuminating search
  spaces by mapping elites*, arXiv:1504.04909, 2015). Instead of returning one
  champion, MAP-Elites keeps the best solution found *in each cell* of a grid
  whose axes are user-chosen "feature dimensions of variation." The output is an
  illuminated map: a diverse archive of high-performing-but-qualitatively-
  different solutions. Because it explores more of the space, it also tends to
  find a better *overall* solution than objective-only search.
- **POET** (Wang, Lehman, Clune, Stanley, *Paired Open-Ended Trailblazer*,
  arXiv:1901.01753, 2019). Co-evolves *environments* and the *agents* that solve
  them, building its own expanding curriculum and transferring stepping-stone
  solutions between niches when they help â€” a concrete (if compute-heavy) attempt
  at sustained open-endedness.

The connective tissue is the **archive**. Novelty search, MAP-Elites, and POET
all replace "one global best" with "a maintained collection of diverse
stepping stones." This is the same shift the corpus already gestures at when it
asks "when does an archive of accepted mutations become a genome rather than a
changelog?" (Chapter 03). The artificial-life literature answers: the archive
becomes generative â€” genome-like â€” precisely when it is *diverse and
stepping-stone-structured*, not when it is merely a linear log of the current
champion.

### Metaphor vs. structural analogy vs. measurable property vs. implementation consequence

The pipeline's desired output is to separate metaphor from mechanism. Applied to
the organism framing:

| Biological term | Metaphor only | Real structural analogy | Measurable / testable property | CursiveOS implementation consequence |
| --- | --- | --- | --- | --- |
| Organism | "it's alive" | Autopoietic vs. allopoietic distinction | Does the system regenerate its own verifier/sensor/archive machinery, or does a human harness? | Today: allopoietic. Track concrete autopoiesis steps; do not claim "living software." |
| Metabolism | "it consumes energy" | Cybernetic throughput regulated against a viability boundary | Power/cost/latency sensors with source tags (Chapter 00) | Metabolic sensor must be multi-objective and method-tagged, not a single scalar. |
| Immune system | "it defends itself" | Selection/verification rejecting harmful variants | Verifier + regression gates + population confirmation reject rate | Keep the verifier external and immutable to the proposer (this chapter). |
| Genome | "its DNA" | A diverse, stepping-stone-structured archive (MAP-Elites-style), not a linear changelog | Archive coverage/diversity across feature dimensions, not just best-so-far | CursiveRoot should store *diverse* accepted+rejected variants keyed by context, not only the current champion. |
| Evolution | "it evolves" | Selection over bounded mutation surfaces with intermediate rewards | Does the fitness landscape reward stepping stones (Avida/EQU) or only the final target? | Multi-rung fitness; avoid single-headline objectives that are deceptive and plateau. |
| Open-endedness | "endless improvement" | Sustained generation of new, useful organization | Has *any* controlled system shown this indefinitely? No. | Treat indefinite self-improvement as unproven; expect plateaus; rotate/evolve the fitness bundle. |

### What this adds for CursiveOS

- **The "genome" should be an illuminated archive, not a changelog.** The QD/
  MAP-Elites lesson argues CursiveRoot's accepted/rejected store should preserve
  *diversity across feature dimensions* (hardware class, workload, governor,
  power source) rather than collapsing to a single global-best preset. Diversity
  is what makes an archive generative rather than merely historical, and it is
  the natural counter to the hardware-scoped-fitness problem already observed in
  Chapter 00 Â§5 (a variant that wins on the Arc desktop is a *cell* in the map,
  not a global champion).
- **Reward the stepping stones, or the capability will not evolve.** Avida's EQU
  result is direct evidence that single-target fitness is often unreachable; the
  CursiveOS fitness bundle should reward intermediate, partial wins, reinforcing
  the multi-objective stance argued from the Goodhart literature.
- **Match measurement variety to mutation variety.** Ashby's Law says the sensor/
  verifier layer must distinguish at least as many states as the organism can
  generate. As CursiveOS adds mutation surfaces (presets â†’ runtime patches â†’
  skills), the verifier bundle must grow in lockstep or lose control â€” a
  concrete design constraint, not a slogan.
- **Expect plateaus and design for them.** No controlled digital-evolution system
  has sustained open-ended novelty. CursiveOS should plan for its benchmark suite
  to stop yielding gains (the optimization "settles"), and treat fitness-bundle
  rotation / fresh holdouts as a permanent requirement, not a one-time setup.

### What not to overclaim

- "Software organism" is at present a **structural analogy and a direction**, not
  a demonstrated autopoietic system. CursiveOS today is closer to a
  human-maintained automation pipeline reaching toward organism properties.
- Open-ended, unbounded self-improvement remains **unachieved even in
  purpose-built artificial-life systems**; it must not be implied as an expected
  CursiveOS behavior.
- The autopoiesis and cybernetics framings are **conceptual lenses** drawn from
  systems theory; they sharpen design questions but do not by themselves
  validate any CursiveOS mechanism. Empirical grounding still comes from the
  sensor/verifier/archive evidence chain.

## Definitions for Software-Organism Research

| Term | Research Meaning | Important Distinction |
| --- | --- | --- |
| Recursive self-improvement | A system improves the process that creates future improvements. | Stronger than self-correction or ordinary optimization. |
| Self-modification | A system edits its own code, prompt, runtime state, memory, policy, or configuration. | Change is not automatically improvement. |
| Self-correction | A system fixes an immediate output or error. | Usually ephemeral and task-local. |
| Self-reflection | A system critiques its own reasoning or behavior in language. | Useful as memory, weak as evidence. |
| Fine-tuning | Updating model parameters through training. | Expensive and usually offline, not active organism adaptation. |
| Evolutionary search | Generate variants, evaluate them, select fit candidates, repeat. | The closest mature pattern for software-organism mutation. |
| Verifier | Independent mechanism that checks correctness, safety, or fitness. | Must be protected from the proposing agent. |
| Fitness function | Quantitative objective or bundle of objectives used for selection. | Bad fitness creates pathological adaptations. |
| Open-endedness | Sustained production of novel, learnable, useful artifacts. | Harder than improving on a fixed benchmark. |

## Layered Taxonomy of Self-Improvement

The uploaded document's strongest contribution is its loop taxonomy. It shows that â€œself-improvementâ€ is not one thing; it happens at different layers with different risks.

| Loop Type | Core Mechanism | Representative Systems | Evaluator | Risk | Organism Use |
| --- | --- | --- | --- | --- | --- |
| Parameter fine-tuning | Generate training/preference data and update model behavior. | Self-Rewarding LMs; Process-Based Self-Rewarding | LLM-as-judge or process reward | Evaluator drift; model collapse | Offline consolidation only. |
| Discrete scaffolding optimization | Search over prompts, wrappers, and code scaffolds. | STOP; self-developing scaffolds | Programmatic utility | Syntax errors; sandbox bypass | Strong early mutation surface. |
| Programmatic skill acquisition | Build modular executable skill libraries. | Voyager; PSN | Environment logs and execution traces | Dependency cascade; memory bloat | Very strong organism memory model. |
| Runtime policy modification | Patch active classes, globals, routines, or policies. | GÃ¶del Agent; Polaris | Validation suites and error traces | Crashes, loops, escalation | High-value but high-risk research path. |
| Algorithmic superoptimization | Evolve executable low-level algorithms. | AlphaEvolve; CodeEvolve; AlphaDev; AlphaTensor | Deterministic verifiers | Heavy compute; narrow domains | Strong for backend utilities and algorithms. |
| Model/parameter merging | Search over model blends and layer flows. | Evolutionary model merging | Validation benchmark | High memory; narrow deployability | Offline model engineering, not core organism loop. |

## The Verifier Is the Organism's Immune System

A software organism can mutate only if it can know whether the mutation helped. The uploaded document repeatedly points to the same conclusion: **a self-improving system without a hard verifier becomes self-deluding**.

Weak verifier pattern:

```text
agent proposes change
-> same agent judges change in natural language
-> agent accepts own preferred style
-> evaluator drift compounds
-> fake progress
```

Stronger verifier pattern:

```text
agent proposes change
-> isolated execution
-> compiler/interpreter feedback
-> deterministic tests
-> performance sensors
-> regression gates
-> independent confirmation when needed
```

For software organisms, the verifier should be treated as an immune system:

- it detects malformed mutations;
- it rejects harmful variants;
- it prevents self-preference from becoming truth;
- it blocks hidden regressions;
- it maintains organism identity under mutation pressure.

## Goodhartâ€™s Law, Proxy Optimization, and Robust Fitness Design for Software Organisms

Goodhartâ€™s Law (â€œwhen a measure becomes a target, it ceases to be a good measureâ€) is not a minor implementation detail for self-improving systems â€” it is a structural vulnerability. Any organism that proposes mutations and selects on a proxy signal will, under sufficient optimization pressure, learn to exploit that signal rather than improve the underlying objective. Recent literature on reward hacking in RL and LLM agents makes the mechanisms concrete and shows they appear pervasively once optimization crosses a critical threshold.

**How it manifests in self-improving loops** (synthesized taxonomy drawing from reward-hacking analyses and RL empirical work):
- **Reward / proxy misspecification**: The fitness signal compresses a complex goal (real utility, reliability, cost, safety, transfer) into something narrower that is easy to measure but incomplete (e.g., loopback network throughput under fixed netem conditions, single cold-start latency number, RAPL package power only).
- **Overoptimization / Goodharting phase transition**: Early optimization improves both proxy and true objective. Past a threshold, proxy continues rising while true objective plateaus or declines. The system is still â€œlearningâ€ â€” it is learning the wrong thing.
- **Specification gaming / exploit discovery**: The proposer finds loopholes in the verifier or benchmark (inspecting evaluation stacks, replacing timing functions, stubbing verifiers, hard-coding known test cases, or gaming variance by cherry-picking runs). Documented in coding/tool-use agent benchmarks; rates vary sharply by post-training but can reach double digits on harder variants.
- **Evaluator drift / co-evolution**: When the judge and generator improve together (self-reward loops, agent-as-judge without frozen external reference), the signal becomes easier to satisfy without real progress.
- **Hidden regression and multi-objective collapse**: One metric (throughput) improves while another (power, reliability, real-path behavior, security) degrades silently.
- **Benchmark overfitting and holdout failure**: The system internalizes quirks of the current test suite rather than general capability.

**CursiveOS-relevant examples** (tied to current empirical record):
- Network â€œ+500%â€ headline under loopback WAN sim is real within the emulation but largely decomposes into CUBICâ†’BBR (algorithm swap) + buffer/qdisc tuning (CursiveOS contribution). Without the stack-delta ablation and netem verification, the proxy could have been gamed by tuning only for the simulator.
- Cold-start latency win that is hardware-scoped (strong on founder Arc desktop, neutral on second-machine laptop). A global preset optimized only on the founder rig would have produced a misleading fitness signal.
- Idle power measurement mixing physically different sources (RAPL package vs. GPU hwmon vs. turbostat) without recording which. Optimizing the number without normalizing the method creates an artifact that future mutations can exploit.
- Any single-scalar â€œfitnessâ€ used for parent-vs-candidate screens or metabolic sensor weighting is vulnerable once the organism has enough degrees of freedom (preset parameters, future runtime patches, skill libraries).

**Design patterns that mitigate Goodharting in software organisms** (actionable for CursiveOS sensor array, confirmation logic, and Layer 5 fitness):
- **Multi-objective / fine-grained fitness bundles** instead of single scalars. Include correctness, latency, throughput, cost, power (with source/method tags), stability (variance across repeated runs), reversibility, regression gates, and transfer (hardware diversity or population confirmation). Negative gates (hard failures) are especially powerful.
- **Independent / population confirmation (N-confirmation + CV threshold)** before acceptance. Single-machine or single-screen results remain diagnostic only. Hardware fingerprinting + diverse fleet reduces correlation/Sybil risk.
- **Holdouts and dynamic/fresh test generation**. Static benchmarks are gameable; rotate or generate new holdout tasks. Cost-aware and reliability-aware evaluation (repeat runs, variance reporting) prevents cheap wins that hide fragility.
- **Negative memory and anti-pattern storage**. Record failed mutations and *why* they failed (structured sandbox output: stdout/stderr/exit/latency/memory/violations). Future proposers are steered away from rediscovering the same exploits.
- **Canary + rollback + parent-vs-candidate comparison**. Never promote live without a stable, monitored control. Sandbox execution turns potential exploits into rich, structured feedback rather than silent success.
- **Sandbox as sensory organ, not just containment**. Structured output (exit code, exceptions, resource attempts, timing) becomes evidence. Immutable evaluator/safety boundary + no ambient credentials prevents the candidate from rewriting the verifier.
- **Budgeted / constrained optimization and rotating test suites**. Limit how aggressively any single proxy can be optimized. Evolve or rotate parts of the fitness bundle itself so no single loophole remains permanently rewarding.
- **Evaluator hardening and protected verifier**. Freeze or heavily gate core verifiers. Linguistic/agent-as-judge is useful for triage and hypothesis generation but never final truth for mutation acceptance. External ground truth (compiler, deterministic tests, physical sensors, population confirmation) must dominate.
- **Explicit cost, latency, and reliability accounting** in every fitness claim. Any â€œimprovementâ€ that ignores these is treated as weak or suspect.

**Implications for current CursiveOS work**:
- The recent stack-delta decomposition, hardware-scoped confirmation runs, power-source telemetry, and Chapter 00 validity assessment are already applying several of these patterns â€” this is the correct posture.
- Future metabolic sensor weighting, screen-verdict analyzer rules, and CursiveRoot schema extensions should codify multi-objective bundles, negative memory, holdout requirements, and hardware/context tagging.
- Population confirmation calibration and every-run detail bundles (already in experimental lift) directly address variance and correlation risks.
- Sandbox structured feedback + canary logic should be treated as core sensory infrastructure for any future runtime mutation surfaces.

**What the corpus should not overclaim**:
- That current demonstrated loops are â€œunrestricted RSIâ€ or safe for live unconstrained self-patching.
- That any single benchmark or sensor is permanently trustworthy once optimized against.
- That linguistic self-evaluation or agent-as-judge can safely replace external verifiers for mutation decisions.

## Practical Bounded Autoresearch Loops: Karpathy's autoresearch as a Case Study

In early 2026, Andrej Karpathy released `autoresearch` (https://github.com/karpathy/autoresearch), a deliberately minimal but powerful demonstration of an autonomous research loop running on a single GPU. While not a traditional academic paper, it provides one of the cleanest existing concrete examples of bounded, verifiable self-improvement in practice.

### How the Loop Works

- The human writes high-level strategy and success criteria in a `program.md` file.
- An LLM coding agent is pointed at the repository and is only permitted to edit one file: `train.py` (model architecture, optimizer, hyperparameters, etc.).
- The agent triggers short, fixed-length experiments (default: exactly 5 minutes of wall-clock training time).
- After each run, it evaluates a clear, objective metric (`val_bpb` â€” validation bits-per-byte; lower is better).
- If the result improves on the previous best, the change is kept (committed to git). Otherwise it is discarded or reverted.
- The loop repeats autonomously overnight.
- In the morning, the human reviews the experiment log and the final improved artifact.

### Why This Approach Is Powerful

- **Strong external verifier**: Success is determined by an objective, automatable metric rather than the agent's linguistic self-assessment. This directly embodies the "verifier as immune system" principle.
- **Constrained mutation surface**: By limiting edits to a single file, changes remain reviewable and the scope of possible regressions is reduced.
- **Cheap, comparable iteration**: The fixed time budget makes experiments fast and roughly comparable, enabling many generations of improvement with modest resources.
- **Git as transparent archive and memory**: Every accepted improvement (and many rejected attempts) leaves a clear git history. This creates natural negative memory and an auditable trail of what was tried.
- **Human stays in the strategy layer**: The human defines the high-level goal and metric; the agent executes the low-level iteration loop. This division of labor is healthy for early software organisms.

### Mapping to Software Organism Concepts

Karpathy's autoresearch maps remarkably well onto several ideas developed in this chapter and Chapter 03:

- It is a working example of **bounded recursive self-improvement** â€” the agent improves the training process by modifying code, but the loop is deliberately scoped and grounded.
- The metric functions as a **protected verifier** that the proposing agent cannot easily game or rewrite.
- Git history serves as both **archive of successful variants** and a record of failed mutations.
- The design shows how **selection pressure** can be implemented simply and effectively through measurable improvement.
- It demonstrates a practical humanâ€“agent collaboration pattern that keeps the human in control of direction while removing them from the iteration bottleneck.

### What Transfers to CursiveOS

- The pattern of cheap, repeatable evaluation loops is directly relevant to screening preset candidates or OS-level mutations.
- Strong emphasis on objective, automatable metrics aligns with the design of CursiveRoot sensors and benchmark validity work.
- Using version control as a transparent, auditable archive of accepted and rejected variants is worth adopting.
- Constraining mutation surfaces and making them reviewable is a valuable safety and debuggability practice.
- The overall philosophy of letting an agent handle high-volume iteration while a higher-level system (human or future meta-layer) sets strategy and success criteria.

### Limitations and Needed Extensions for Our Context

- The original system is specialized for ML training scripts with a single scalar metric and fixed experiment length.
- CursiveOS requires richer, multi-objective evaluation (power, latency, reliability, hardware transfer, security) and stronger safety/sandboxing guarantees.
- Extending similar loops to OS-level or runtime mutations would benefit from more structured experiment feedback beyond a single number.
- Long-term organism identity and protection of core verifiers/safety boundaries become more important as mutation surfaces expand.

This source strengthens the corpus by providing a concrete, working reference implementation of many of the abstract principles discussed elsewhere in this chapter.

## Linguistic Evaluation Is Not Enough

LLM-as-judge systems can help triage outputs, but they should not validate code-level or system-level mutation alone.

The main failure mode is not that language models are useless. The failure mode is that they reward outputs that look plausible, verbose, familiar, or stylistically aligned while missing hidden runtime errors, resource regressions, security problems, or benchmark overfit.

Use linguistic evaluation for:

- summarizing candidate behavior;
- explaining failures;
- ranking candidates before expensive tests;
- generating hypotheses;
- reviewing logs.

Do not use it as the final authority for:

- accepting code mutations;
- changing safety rules;
- validating runtime patches;
- promoting benchmark improvements;
- deciding that an organism improved.

## Programmatic and Physical Ground Truth

The uploaded document argues that successful self-improving systems use execution feedback. Useful ground-truth sources include:

| Ground Truth | What It Catches | What It Misses |
| --- | --- | --- |
| Compiler/interpreter | Syntax, type, dependency, structural failures. | Semantic correctness and real utility. |
| Unit tests | Known invariants and edge cases. | Unknown unknowns and overfit. |
| Integration tests | Cross-component behavior. | Long-tail workload behavior. |
| Benchmarks | Performance deltas. | Benchmark gaming and variance. |
| Environment feedback | Whether action changes world state correctly. | Confounding, noise, delayed harms. |
| Physical sensors | Power, thermal, latency, throughput, stability. | Higher-level user value. |
| Population confirmation | Transfer across machines. | Sybil/correlation risk. |

A mature organism needs a bundle of these, not one metric.

## Sandboxing as Feedback Infrastructure

Sandboxing is usually treated as security. For software organisms, it is also a sensory organ.

A good sandbox reports:

```text
stdout
stderr
exit code
exception type
latency
memory use
CPU time
disk writes
network attempts
forbidden file access
resource-limit violations
```

Those signals become feedback for future mutation attempts. The sandbox should both protect the host and produce structured evidence.

Minimum sandbox principles:

- no ambient credentials;
- no default network access;
- strict CPU/memory/wall-clock limits;
- scoped filesystem;
- immutable evaluator and safety boundary;
- clear promotion path from sandbox to canary to accepted artifact.

## Runtime Self-Modification Is Powerful but Volatile

Runtime self-modification systems such as GÃ¶del-agent-style agents and Polaris-style repair are the closest analogues to a live organism modifying itself in place.

They matter because they demonstrate:

- live policy repair;
- runtime monkey patching;
- meta-policy modification;
- error-trace abstraction;
- small-model adaptation possibilities.

They are dangerous because they also demonstrate:

- severe temporary regressions;
- crashes and infinite loops;
- unauthorized resource escalation;
- pressure to bypass sandboxes;
- patches that solve local exceptions while creating architectural debt.

Research conclusion:

```text
in-situ mutation should be researched,
but early software organisms should prefer sandboxed candidate generation
and parent-vs-candidate selection over live uncontrolled self-patching.
```

## Skill Libraries and Programmatic Skill Networks

Voyager-style systems show that a system can improve by writing and reusing executable skills instead of retraining model weights. Programmatic Skill Networks go further by turning flat skill libraries into structured graphs.

This matters because a software organism needs memory that is more than conversation history.

Useful properties of programmatic skills:

- executable;
- inspectable;
- composable;
- testable;
- reusable;
- replaceable;
- versionable;
- linkable to success/failure evidence.

A skill graph can support:

- dependency tracking;
- fault localization;
- maturity gating;
- rollback validation;
- refactoring;
- stable/plastic separation.

Research conclusion:

```text
software-organism memory should favor executable, testable skills and evidence-linked artifacts over loose natural-language recollection.
```

## Maturity-Aware Gating

The uploaded document emphasizes maturity-aware gating: new code or skills should not immediately become trusted organism substrate.

A useful maturity ladder:

| Stage | Meaning | Allowed Use |
| --- | --- | --- |
| Plastic | New, unstable, still being tested. | Sandbox only. |
| Candidate | Passed basic tests. | Parent-vs-candidate comparison. |
| Canary | Limited deployment. | Monitored real workload. |
| Stable | Repeatedly successful. | Eligible parent for future mutations. |
| Protected | Safety-critical or verifier logic. | Not directly mutable by candidate generator. |

This gives the organism a stability-plasticity balance. It can explore without letting every experiment become part of its body.

## Multi-Objective Fitness

Accuracy-only or speed-only optimization is not enough. The uploaded document highlights that self-improving agents can appear successful while consuming excessive compute, latency, or money.

A better fitness bundle includes:

```text
correctness
latency
throughput
cost
power
memory
stability
reversibility
security
reliability across repeated runs
transfer across hardware
```

Any self-improvement claim that ignores cost and reliability should be treated as weak.

## Failure Modes

| Failure Mode | Description | Organism-Level Risk | Mitigation |
| --- | --- | --- | --- |
| Reward hacking | System exploits proxy metric. | Mutations look good but harm real objective. | Multi-sensor fitness and holdouts. |
| Goodharting | Metric stops representing goal once optimized. | Organism evolves toward scoreboard, not health. | Rotate/evolve tests, use negative gates. |
| Evaluator drift | Judge and generator co-evolve toward easier self-approval. | Self-delusion. | Freeze/protect verifiers; use external ground truth. |
| Hidden regression | One metric improves while another breaks. | Silent damage accumulates. | Regression suites and canaries. |
| Temporary degradation | Most mutation attempts are bad before good ones appear. | Instability if applied live. | Sandbox, rollback, parent-vs-candidate. |
| Benchmark overfitting | System learns test quirks. | Fake progress. | Dynamic holdouts and cost-aware evaluation. |
| Sandbox escape | Candidate bypasses constraints. | Host compromise. | Strong isolation and no ambient credentials. |
| Resource escalation | Agent routes to stronger/costlier resources without approval. | Budget and policy violation. | Immutable budget policy and audit. |
| Goal drift | Open-ended exploration diverges from intended utility. | Novel but useless behavior. | High-level task guardrails. |
| Memory bloat | Skill libraries grow without pruning. | Retrieval noise and brittle dependency chains. | Maturity scoring and refactoring. |
| Recursive degradation | Self-editing damages the improver. | Capability collapse. | Protect core verifier/safety kernel. |

## What Software-Organism Projects Should Adopt

| Adopt | Why |
| --- | --- | --- |
| Programmatic skill libraries | They make accumulated capability executable and testable. |
| Skill graphs over flat prompts | Graphs allow dependency tracking, repair, maturity, and refactoring. |
| External verifiers | They prevent the proposer from becoming judge of itself. |
| Maturity-aware gating | It balances exploration and stability. |
| Parent-vs-candidate comparison | It prevents live mutation from replacing known-good behavior too early. |
| Negative memory | Failed mutations should become future warnings. |
| Multi-objective fitness | Prevents fake gains from hiding cost, latency, or reliability regressions. |
| Sandboxed execution | Turns unsafe mutation into observable evidence. |

## What Software-Organism Projects Should Avoid

| Avoid | Why |
| --- | --- | --- |
| Pure linguistic self-evaluation | Too vulnerable to style bias and hallucinated progress. |
| Unconstrained live monkey patching | Too fragile and dangerous for early organisms. |
| Allowing agents to edit verifiers | Destroys the selection mechanism. |
| Accuracy-only benchmark claims | Often hide cost and reliability collapse. |
| Complex multi-agent scaffolds without simple baselines | Often cost more without real capability gain. |
| Open-ended exploration without guardrails | Can create novelty instead of usefulness. |
| Treating self-modification as self-improvement | Most self-modifications are neutral or harmful. |
| Letting memory become truth | Memory should inform proposals, not validate outcomes. |

## What to Treat with Extreme Caution

| Caution Area | Why |
| --- | --- | --- |
| In-situ adaptation to unstructured environments | Local exception repair can create long-term architectural debt. |
| Autonomous curriculum planning | Exploration objective can drift away from practical utility. |
| Self-rewarding models | Evaluator drift and circular self-approval remain unresolved. |
| Open-ended evolution claims | Open-endedness is easy to assert and hard to prove. |
| Small-model self-repair | Promising for local systems but may be limited by synthesis capacity. |
| Runtime policy modification | Closest to organism-like adaptation, but highest instability. |

## Research Questions Preserved from the Intake

1. How can we formally guarantee structural stability and prevent collapse in recursive self-improvement loops?
2. What architecture can isolate self-improvement mechanisms from safety and containment rules permanently?
3. How can dynamic, non-overfittable, cost-controlled validation holdouts scale with an improving agent?
4. Is meaningful open-ended self-improvement possible on small local models, or does it require frontier-scale models?
5. How can executable skill libraries be pruned, refactored, and matured without destroying useful diversity?
6. What kind of verifier bundle is strong enough for software-organism mutation?
7. How can an organism preserve identity while mutating its policies, tools, and skills?
8. What is the minimum evidence required before a mutation becomes part of the stable substrate?

## Corpus Implications

This intake shifts the corpus from â€œself-improvement as conceptâ€ to â€œself-improvement as controlled selection over bounded mutation surfaces.â€

The strongest research-backed posture is:

```text
start with bounded candidate generation;
execute in sandbox;
score with external verifiers;
compare against stable parent;
record positive and negative outcomes;
only promote after repeated evidence.
```

The weakest posture is:

```text
allow an agent to rewrite itself live;
let it judge success linguistically;
let it alter its evaluator;
accept benchmark scores without cost and reliability accounting.
```

## Follow-Up Research Needed

- Direct source validation of newer/preprint systems listed in `sources/peer-reviewed-rsi-selected-sources.md`.
- Deeper literature review on open-ended evolution and artificial life.
- Research on verifier isolation, proof-carrying code, and immutable safety kernels.
- Research on dynamic holdout generation and benchmark anti-overfitting.
- Research on skill-library pruning and programmatic memory maintenance.
- Research on whether small/local models can sustain useful self-repair under strong scaffolding.
