# Reflexion — Deep Extraction

Source: https://arxiv.org/abs/2303.11366
Authors / Lab: Noah Shinn, Federico Cassano, Edward Berman (Northeastern University); Ashwin Gopinath (MIT); Karthik Narasimhan, Shunyu Yao (Princeton University)
Year / Venue: 2023, arXiv (2303.11366)
Corpus Status: unvalidated
Extraction Type: important
Rights Status: extraction only (CC BY 4.0 — attribution required)

## 0. Extraction Provenance

Grounded in the locally stored full text (`paper.md`, an ar5iv HTML→Markdown conversion of arXiv:2303.11366). Because the full text is local, quantitative results are traceable to specific sections/tables and are cited inline as (paper.md §X / Table N). Per the conversion note in `paper.md`, some figure images and mathematical notation are degraded in the Markdown; figure *content* is preserved in prose. No abstract-only gaps remain, so this extraction carries no **[needs full-text]** markers. Catalog ID: RSI-006 (per `sources/peer-reviewed-rsi-selected-sources.md`).

## 1. Paper Map

| Paper Section | What It Covers | Why It Exists In The Paper |
| --- | --- | --- |
| Introduction (§1) | Verbal reinforcement vs. weight-update RL; three reflection sources; headline gains | Motivate learning from trial-and-error without fine-tuning |
| Related Work (§2) | Self-Refine, test-driven code agents (AlphaCode, CodeT, Self-Debugging, CodeRL) | Position Reflexion as memory + self-reflection over prior methods |
| Method (§3) | Actor / Evaluator / Self-Reflection roles; short- and long-term memory; the loop | Core Reflexion algorithm |
| Experiments (§4) | ALFWorld, HotPotQA, MBPP/HumanEval/LeetcodeHard | Empirical evidence across decision-making, reasoning, coding |
| Limitations (§5) | Local minima; bounded memory; TDD limits | Author-stated scope |
| Broader Impact (§6) | Automation risk vs. interpretability of verbal traces | Safety framing |
| Conclusion / Reproducibility (§7–8) | Summary; sandboxing advice for code execution | Wrap-up and safe-use note |
| Appendices A–D | Extra models (Table 4–5), WebShop limitation, prompt templates, worked examples | Supporting detail and ablations |

## 2. Author's Core Claims

| Claim | Where It Appears | Evidence Used By Authors | Extraction Confidence |
| --- | --- | --- | --- |
| Agents can be reinforced via *language* (reflective text in episodic memory) without updating weights | Abstract; §1; §3 | Gains across three task families | High (full text local) |
| Verbal self-reflection acts as a "semantic gradient" that directs the next attempt | §1; §3 Self-Reflection | Qualitative trajectory corrections (App. B–D) | High |
| Reflexion sets new pass@1 SOTA on several code benchmarks | §1 contributions; §4.3 Table 1 | 91.0 HumanEval Python vs 80.1 GPT-4 | High (Table 1) |
| Self-reflection adds value *beyond* episodic memory alone | §4.2 analysis | +8 pp absolute over memory-only ablation | High (stated number) |
| Test generation and self-reflection are complementary, not independent | §4.3 Table 3 | Rust ablation: 0.60 → 0.68 only with both | High (Table 3) |
| The ability to self-correct is emergent in stronger models | App. A, Table 4 | starchat-beta shows no gain (0.26 → 0.26) | High (Table 4) |

## 3. System / Method Architecture

```
Actor (LLM; e.g. CoT or ReAct)  --trajectory-->  Evaluator (exact-match / heuristic / LLM)
        ^                                                   |
        | conditions on memory                              v  reward signal
   Long-term memory  <--verbal feedback--  Self-Reflection model (LLM)
   (1-3 distilled reflections)
   loop until Evaluator passes or trial limit reached
```

Key invariant: the policy is parameterized as **agent memory + fixed LLM weights** (§1 contributions); no gradient updates occur. The Evaluator — not the Self-Reflection model — decides success (§3 Evaluator).

## 4. Key Mechanisms Inventory

| Mechanism | What It Does | Inputs | Outputs | Why It Matters |
| --- | --- | --- | --- | --- |
| Actor | Generates text/actions from the current policy | State observation + memory | Trajectory | Acts in the environment (§3 Actor) |
| Evaluator | Scores a trajectory | Trajectory | Reward / pass-fail | Grounds reflection in real feedback (§3 Evaluator) |
| Self-Reflection model | Converts sparse reward into actionable verbal feedback | Reward + trajectory + memory | Reflection text | The "semantic gradient" (§3 Self-Reflection) |
| Episodic memory | Stores 1–3 distilled reflections across trials | Reflection text | Added context | Carries lessons between attempts (§3 Memory) |
| Self-generated unit tests | Provide grounded self-evaluation for code tasks | NL spec | Up to 6 tests (AST-filtered) | Enables verifier-grounded coding (§4.3) |

## 5. Experimental Setup

- **ALFWorld** (§4.1): 134 text-based household environments, six task types; ReAct as action generator; reflection triggered by a heuristic (same action+response > 3 cycles, or > 30 actions) or by an LLM classifier; memory truncated to last 3 reflections.
- **HotPotQA** (§4.2): Wikipedia QA (dataset of 113,000 pairs); evaluated on 100 questions; CoT 6-shot, ReAct 2-shot, self-reflection 2-shot; exact-match binary signal; memory of 3.
- **Programming** (§4.3): MBPP, HumanEval, and the authors' **LeetcodeHardGym** (40 hard Leetcode problems across 19 languages, released after the GPT-4 pretraining cutoff of 2022-10-08); MultiPL-E used to translate subsets to Rust; up to 6 self-generated unit tests; memory limited to 1 experience.
- Base model for headline results is GPT-4; Appendix A adds starchat-beta, text-davinci-003, and gpt-3.5-turbo.

## 6. Results Inventory

| Result | Metric | Comparison | Author Interpretation | Caveat |
| --- | --- | --- | --- | --- |
| HumanEval Python 91.0 pass@1 | pass@1 | GPT-4 SOTA 80.1 | New SOTA (+11 pp) | Low false-positive test rate (1.4%) helps (§4.3) |
| ALFWorld 130/134 tasks | tasks solved | ReAct-only stalls at trials 6–7 | Learns over 12 trials | Heuristic-driven; six task types |
| HotPotQA +14 pp | accuracy | CoT w/ ground-truth context (fails 39%) | Gains without ground-truth answer | Tested on 100 questions |
| Self-reflection ablation +8 pp | accuracy | Episodic-memory-only | Reflection > refinement alone | HotPotQA only (§4.2) |
| MBPP Python 77.1 | pass@1 | GPT-4 SOTA 80.1 | *Below* SOTA — the one miss | 16.3% false-positive test rate (§4.3) |
| Rust ablation 0.60→0.68 | pass@1 | needs both test-gen + reflection | Mechanisms cooperate | 50 hardest HumanEval-Rust (Table 3) |

## 7. Figures and Tables Inventory

| Figure/Table | What It Shows | Important Takeaway | Should Corpus Recreate/Summarize? |
| --- | --- | --- | --- |
| Figure 1 | Reflexion across decision-making/coding/reasoning | Single framework, three domains | Summarize in own words |
| Figure 2 | Reflexion diagram + algorithm | The Actor/Evaluator/Reflection loop | Already captured in §3 above |
| Figure 3 | ALFWorld performance over trials | Learning continues past trial 6–7 stall | Summarize |
| Figure 4 | HotPotQA over learning steps | Reflexion retries failed tasks | Summarize |
| Table 1 | pass@1 vs prior/SOTA across benchmarks | Headline coding gains | Mirrored in claims-and-results.md |
| Table 2 | Accuracy + TP/FN/FP/TN | Test-suite quality drives outcomes | Mirrored in figures-and-tables.md |
| Table 3 | Rust test-gen × self-reflection ablation | Mechanisms are complementary | Mirrored |
| Table 4 | starchat-beta (no gain) | Self-correction is emergent | Mirrored |
| Table 5 | HotPotQA across models | Gains scale with model strength | Mirrored |

## 8. Limitations Stated By Authors

- Reflexion is a natural-language policy optimizer and can still settle in non-optimal local minima (§5).
- Long-term memory is a bounded sliding window; richer stores (vector/SQL) are future work (§5).
- Test-driven self-evaluation is hard for nondeterministic generators, impure/API-calling functions, **functions whose outputs vary by hardware specification**, and parallel/concurrent functions (§5).
- WebShop: a 2-shot ReAct+Reflexion agent over 100 environments showed no improvement after 4 trials; Reflexion struggles where tasks demand high diversity/exploration (App. B.1).

## 9. Limitations Inferred By Corpus

- All headline numbers are single-benchmark, single-base-model (GPT-4) snapshots from early 2023; no claim of robustness across model generations.
- "Success" is defined by the Evaluator; weak evaluators (flaky tests) directly cap the method (the MBPP false-positive case proves this).
- The Markdown `paper.md` is an ar5iv conversion; exact figure images and some notation are degraded — wording-sensitive claims should be checked against the PDF.

## 10. Failure Modes and Safety Concerns

- **False positives**: self-generated tests pass but the solution is wrong → premature, invalid submission (§4.3 analysis). Authors prefer false negatives over false positives.
- **Reward/evaluator gaming**: because the Self-Reflection model writes the feedback the Actor consumes, a weak Evaluator lets the loop reinforce wrong behavior.
- The paper explicitly advises **isolated execution environments** for autonomous code-writing because generated code runs unvalidated (§8).

## 11. What Transfers To Software Organisms

- The Actor/Evaluator/Self-Reflection split mirrors CursiveOS's "proposer suggests, measurement daemon disposes" separation — only a grounded evaluator should write fitness truth.
- Distilling a long failed trajectory into a short, reusable lesson is a cheap, interpretable memory primitive.
- The insistence on sandboxed execution aligns directly with Ch06 mutation-safety/permission law.

## 12. What Does Not Transfer

- Reflexion's "reward" is exact-match / unit-test pass on *language and code* tasks — not hardware-scoped, noisy performance sensors.
- Verbal self-reflection assumes the agent can read and reason about textual feedback; CursiveOS fitness is numeric, variance-laden, and hardware-specific (the paper itself flags hardware-dependent outputs as a TDD limitation, §5).
- Single-model SOTA numbers do not imply transfer to a fleet of heterogeneous nodes.

## 13. CursiveOS / Corpus Implications

RSI-006. Reflexion is the canonical "verbal reinforcement without weight updates" reference and pairs with the test-driven SWE-agent cluster as an *evaluation-pattern* source for Ch05's natural-language shell. For CursiveOS its relevance is **Supported as a pattern, Unvalidated as a mechanism** (see corpus taxonomy note in `papers/README.md`): the proposer/reflection loop is reusable, but the verifier must be a hardware-grounded sensor, not an LLM judge. Consistent with Ch18's note that verbal self-correction is insufficient without executable post-checks.

## 14. Open Questions

- Can a Reflexion-style verbal memory be paired with a numeric, variance-aware fitness sensor without the reflection model gaming it?
- Does the "emergent self-correction" finding (Table 4) hold for the smaller local models CursiveOS targets, or does it gate the whole approach?
- What is the analogue of "false-positive test rate" for hardware benchmarks (i.e., a win that does not replicate on real workloads)?

## 15. Extraction Coverage Notes

- All major claims extracted: yes (full text local)
- All experiments extracted: yes (ALFWorld, HotPotQA, MBPP/HumanEval/LeetcodeHard, WebShop)
- All figures/tables inventoried: yes (Figures 1–7; Tables 1–5) — see figures-and-tables.md
- Source-level validation complete: n/a (corpus does not re-run experiments)
- Sections skipped: none material; appendix prompt templates summarized, not copied

## 16. Source Reliability

arXiv preprint (2303.11366) with public code and CC BY 4.0 license; widely cited in the agent literature (referenced by the stored SWE-agent paper). High credibility as a method/pattern source; numbers are author-reported and not independently re-verified by the corpus.
