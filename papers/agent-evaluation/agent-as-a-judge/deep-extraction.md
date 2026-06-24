# Agent-as-a-Judge — Deep Extraction

Source: https://arxiv.org/abs/2410.10934
Authors / Lab: Mingchen Zhuge et al. (Meta auto AI / Schmidhuber lab collaborators)
Year / Venue: 2024, arXiv (2410.10934v2)
Corpus Status: unvalidated
Extraction Type: important
Rights Status: extraction only (arXiv CC BY 4.0; corpus stores paraphrase only)

## 1. Paper Map

| Paper Section | What It Covers | Why It Exists In The Paper |
| --- | --- | --- |
| Problem statement | Outcome-only vs manual eval inadequate | Motivate agentic evaluation |
| Agent-as-a-Judge framework | Agents evaluate agents with intermediate feedback | Core contribution |
| DevAI benchmark | 55 realistic AI dev tasks, 365 hierarchical requirements | Evaluation testbed |
| Experiments | Three popular agentic systems benchmarked | Empirical comparison |
| LLM-as-a-Judge comparison | Reliability vs human baseline | Positioning |

## 2. Author's Core Claims

| Claim | Where It Appears | Evidence Used By Authors | Extraction Confidence |
| --- | --- | --- | --- |
| Contemporary agent evaluation is inadequate for agentic systems | Abstract | Critique of outcome-only/manual methods | High |
| Agent-as-a-Judge extends LLM-as-a-Judge with process-level agentic features | Abstract | Framework design | High |
| DevAI: 55 tasks, 365 hierarchical user requirements | Abstract | Benchmark spec | High |
| Agent-as-a-Judge dramatically outperforms LLM-as-a-Judge | Abstract | Benchmark experiment | Medium — metrics **[needs full-text]** |
| Reliability matches human evaluation baseline | Abstract | Human comparison | Medium |
| Rich reliable rewards enable dynamic scalable self-improvement | Abstract | Implications | Medium (speculative extension) |

## 3. System / Method Architecture

```
Agent-under-test executes task (e.g., code generation)
    → Agent-as-a-Judge observes intermediate steps
    → Judge agent checks requirements hierarchically
    → Produces process-level scores + feedback
    → usable as reward signal for improvement loops
```

DevAI provides structured requirements for automated judging.

## 4. Key Mechanisms Inventory

| Mechanism | What It Does | Inputs | Outputs | Why It Matters |
| --- | --- | --- | --- | --- |
| Process-level evaluation | Scores steps not just final artifact | Traces, repos, tests | Intermediate rewards | Credit assignment for agents |
| Hierarchical requirements | Nested user specs | DevAI annotations | Checklist coverage | Fine-grained judging |
| Agentic judge | Tool-using evaluator | Same environment access | Reliable assessment | Reduces manual labor |
| DevAI benchmark | Realistic autonomous dev tasks | 55 projects | Standardized comparison | Corpus evaluation asset |

## 5. Experimental Setup

- Benchmark: DevAI (55 tasks, 365 requirements).
- Systems under test: three popular agentic systems **[needs full-text names]**.
- Judges: Agent-as-a-Judge vs LLM-as-a-Judge vs humans.
- Domain: code generation / AI development automation.

## 6. Results Inventory

| Result | Metric | Comparison | Author Interpretation | Caveat |
| --- | --- | --- | --- | --- |
| Agent-as-a-Judge >> LLM-as-a-Judge | Agreement / reliability metrics | Side-by-side on DevAI | Process awareness helps | **[needs full-text numbers]** |
| Parity with humans | Correlation / agreement | Human eval baseline | Scalable human-quality judging | Human baseline scope limited |
| Agent benchmarking | Success on DevAI | Three agents | DevAI discriminates systems | New benchmark — maturity TBD |

## 7. Figures and Tables Inventory

| Figure/Table | What It Shows | Important Takeaway | Should Corpus Recreate/Summarize? |
| --- | --- | --- | --- |
| **[needs full-text]** | Judge agreement charts | Quantified reliability | Yes |
| **[needs full-text]** | DevAI task examples | Requirement hierarchy | Yes |

## 8. Limitations Stated By Authors

- **[needs full-text]** — likely judge bias, cost, domain specificity.

## 9. Limitations Inferred By Corpus

- Judge agents may share model family biases with agents under test.
- Code dev tasks ≠ hardware-scoped OS performance.
- Using agent judges as *sole* fitness reintroduces Goodhart/proxy risks.

## 10. Failure Modes and Safety Concerns

- Collusive failure: judge and worker share blind spots.
- Process rewards gamed without true deployment success.
- Self-improvement loops optimizing judge-pleasing behaviors.

## 11. What Transfers To Software Organisms

- Evaluate intermediate organism steps (preset edit → compile → micro-benchmark → full sensor).
- Hierarchical requirements map to multi-channel fitness decomposition.
- Agent judges as auxiliary rich feedback before frozen sensor confirmation.

## 12. What Does Not Transfer

- Replacing deterministic hardware verifiers with agent judges.
- Assuming human-parity on OS safety-critical properties without proof.

## 13. CursiveOS / Corpus Implications

RSI-012 complements AI Agents That Matter: richer metrics *and* process awareness. For CursiveOS, use Agent-as-a-Judge patterns in development/debugging loops, but keep population confirmation on sensor array. DevAI may inspire software-organism dev benchmarks.

## 14. Open Questions

- DevAI-style benchmarks for kernel tuning organisms?
- Calibrating agent judges against hardware ground truth?

## 15. Extraction Coverage Notes

- All major claims extracted: yes (abstract)
- All experiments extracted: partial
- Source-level validation complete: no

## 16. Source Reliability

Recent arXiv with open DevAI dataset (HuggingFace). Credible; empirical details need full-text.