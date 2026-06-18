# LADDER: Self-Improving LLMs Through Recursive Problem Decomposition — Deep Extraction

**Source**: https://arxiv.org/abs/2503.00735 (HTML v3)
**Authors / Lab**: Toby Simonds, Akira Yoshiyama (Tufa Labs)
**Year / Venue**: 2025, arXiv preprint (cs.LG)
**Corpus Status**: supported
**Extraction Type**: cornerstone
**Rights Status**: full-text allowed (CC BY 4.0)

## 1. Paper Map

| Paper Section | What It Covers | Why It Exists In The Paper |
| --- | --- | --- |
| Abstract & Introduction | Problem of RL needing difficulty gradients; LADDER's core idea of recursive variant generation for autonomous curriculum | Sets up the motivation and high-level contribution |
| Methodology | Variant generation process, numerical verification, GRPO RL protocol, TTRL extension | Core technical description of how the self-improvement loop works |
| Experiments & Results | Llama 3B gains (1%→82%), MIT Integration Bee results (73% then 90% with TTRL) | Empirical evidence of effectiveness on hard math reasoning |
| Discussion & Conclusion | Test-time compute scaling interpretation, extension to other verifiable domains, future work | Places the work in broader context of inference-time adaptation |

## 2. Author's Core Claims

| Claim | Where It Appears | Evidence Used By Authors | Extraction Confidence |
| --- | --- | --- | --- |
| LADDER enables autonomous improvement via recursive difficulty-driven example generation without human data or curated datasets | Abstract, Introduction, Methodology | Llama 3B experiment: 1% → 82% on undergraduate integration; 7B model reaches 73% on MIT Integration Bee | High |
| TTRL extends the same mechanism to inference time and yields further gains (73% → 90%) | Abstract, Methodology 3.1.5, Results | Direct before/after on MIT Integration Bee qualifying exam, outperforming o1 | High |
| Only a reliable verifier (numerical integration) is needed; no human feedback required | Introduction, Methodology | All experiments use only the numerical checker for rewards | High |
| The approach generalizes beyond the specific math domain to any verifiable task | Discussion | Explicit statement that it can extend to other domains with verifiable rewards | Medium-High |

## 3. System / Method Architecture

LADDER is a two-phase framework:

1. **Training phase (LADDER)**: 
   - Start with a set of hard problems (e.g., integration questions).
   - For each problem, recursively generate a tree of easier variants using model-prompted transformations (reduction of complexity, simplification, etc.).
   - Use deterministic numerical integration verifier to label solutions.
   - Train the base model with GRPO on the variant trees (model learns to solve from easy → hard).

2. **Test-time phase (TTRL)**:
   - At inference on a new hard problem, dynamically generate variants of that specific problem.
   - Run RL on those variants at test time.
   - Use the improved policy for the final answer.

This creates a self-bootstrapping curriculum entirely from the model's own generation capability + a simple verifier.

## 4. Key Mechanisms Inventory

| Mechanism | What It Does | Inputs | Outputs | Why It Matters |
| --- | --- | --- | --- | --- |
| Recursive Variant Generation | Creates tree of progressively simpler sub-problems | Hard problem + transformation library + model prompt | Difficulty gradient tree | Enables autonomous curriculum without human design |
| Numerical Verifier | Provides ground-truth reward signal | Candidate solution + integral | Correct/incorrect (or score) | Makes the entire loop verifiable and safe for RL |
| GRPO Training | Policy optimization on grouped variants | Variant trees + verifier labels | Improved model policy | Allows the model to learn the progression from easy to hard |
| TTRL (Test-Time RL) | On-the-fly adaptation per test instance | New hard problem | Refined answer for that instance | Shows inference-time self-improvement is practical |

## 5. Experimental Setup

| Experiment | Task/Environment | Baseline | Metric | What It Tests |
| --- | --- | --- | --- | --- |
| Llama 3.2 3B | Undergraduate integration problems | Standard prompting / pass@k | Accuracy | Whether LADDER can lift a small model from near-zero to high performance |
| Qwen2.5 7B (Deepseek-R1 Distilled) on MIT Integration Bee 2025 qualifying | Hard competition math (integration) | GPT-4o, human average, o1 | % correct | Real-world hard benchmark; comparison to frontier models |
| LADDER + TTRL | Same MIT Integration Bee | LADDER alone | % correct | Value of additional test-time compute via the same mechanism |

## 6. Results Inventory

| Result | Metric | Comparison | Author Interpretation | Caveat |
| --- | --- | --- | --- | --- |
| Llama 3B improvement | Accuracy 1% → 82% | vs. base model | Dramatic lift via self-generated curriculum | Domain-specific (math integration with numerical verifier) |
| 7B model on MIT Integration Bee | 73% correct | Beats GPT-4o (42%), human 15-30% | Strong evidence of autonomous improvement on hard tasks | Specific to problems with reliable numerical verification |
| LADDER + TTRL | 90% on MIT Integration Bee | Beats o1 | Test-time scaling via recursive variants is highly effective | Compute cost at test time; still domain-constrained |

## 7. Figures and Tables Inventory

- Figure 1: Example variant generation tree for an integration problem (shows progressive simplification).
- Algorithm 1: LADDER pseudocode.
- Algorithm 2: TTRL pseudocode.
- Results tables for Llama experiments and MIT Integration Bee scores.

## 8. Limitations Stated By Authors

- Primarily demonstrated on mathematical integration (verifiable numeric answers).
- Requires a reliable automatic verifier.
- Test-time compute cost for TTRL.
- Future work needed for broader domains.

## 9. Limitations Inferred By Corpus

- Still relies on the base model's ability to generate useful variants (may degrade on very out-of-distribution hard problems).
- The "curriculum" is generated per-problem or per-training-set; not a persistent long-term skill library like Voyager.
- Safety is high because of the narrow verifiable domain, but transferring the pattern to open-ended agent tasks requires additional guardrails.

## 10. Failure Modes and Safety Concerns

- If the verifier is gameable or noisy, the loop can reinforce wrong behaviors (classic reward hacking risk, though numerical integration is robust).
- Variant generation could produce low-diversity or degenerate easier problems if prompting is weak.
- TTRL increases per-query compute; unbounded use could be expensive.

## 11. What Transfers To Software Organisms

- **Autonomous curriculum construction** via recursive decomposition is highly relevant to CursiveOS agent scaffolding and skill acquisition.
- **Verifier-grounded RL loops** reinforce the core principle that the verifier (not the model) must be the source of truth.
- **Test-time adaptation** (TTRL) maps to runtime self-optimization ideas in local agents without permanent weight changes.
- Shows that significant capability jumps are possible with relatively simple mechanisms when a clean verifier exists.

## 12. What Does Not Transfer

- The specific transformation library and numerical integration verifier are domain-specific.
- Gains are demonstrated in a narrow, fully verifiable math domain; open-ended agent tasks (OS control, tool use) will need analogous strong verifiers or multi-objective fitness bundles.
- Does not address long-horizon persistent memory or skill graphs (more Voyager-like).

## 13. CursiveOS / Corpus Implications

LADDER is an excellent concrete reference for the "test-time self-improvement" and "self-taught optimizer" directions in the P0 RSI pipeline. It strengthens the argument for keeping proposer and verifier separate and for using grounded, verifiable signals even in self-improvement loops. It suggests that CursiveOS could benefit from similar recursive decomposition patterns when an agent faces a hard task that can be broken into verifiable sub-tasks.

Strong candidate for citation in Chapter 14 and for future experiments in agent curriculum / test-time adaptation on verifiable OS or benchmark tasks.

## 14. Open Questions

- How well does the variant-generation quality transfer when the verifier is more complex (e.g., unit tests + performance sensors instead of pure numerical match)?
- Can the same recursive decomposition idea be combined with programmatic skill libraries or skill graphs?
- What is the compute-efficiency trade-off of TTRL-style test-time RL vs. one-shot inference or simpler self-consistency?

## 15. Extraction Coverage Notes

- All major claims extracted: yes
- All experiments extracted: yes (key results)
- All figures/tables inventoried at high level: yes
- Source-level validation complete: yes (based on official arXiv HTML)
- Sections intentionally compressed: Full related work and some algorithmic pseudocode details omitted for brevity; core contribution and results preserved.

## 16. Source Reliability

Peer-reviewed quality preprint on arXiv with clear empirical results on public benchmarks. Authors from Tufa Labs. CC BY 4.0 license. High reliability for the claims made within the demonstrated domain.
