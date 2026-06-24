# Self-Taught Optimizer (STOP) — Deep Extraction

Source: https://arxiv.org/abs/2310.02304
Authors / Lab: Eric Zelikman, Eliana Lorch, Lester Mackey, Adam Tauman Kalai
Year / Venue: 2023–2024, COLM 2024 (arXiv:2310.02304v3)
Corpus Status: unvalidated
Extraction Type: important
Rights Status: extraction only (arXiv non-exclusive)

## 1. Paper Map

| Paper Section | What It Covers | Why It Exists In The Paper |
| --- | --- | --- |
| Abstract / Intro | Scaffold programs that structure LM calls; seed improver concept | Motivates improving the orchestration code, not model weights |
| STOP loop | Run improver on itself to improve itself | Core recursive self-improvement claim |
| Experiments | Downstream tasks, GPT-4, discovered strategies | Empirical validation |
| Safety | Sandbox bypass frequency | Addresses self-improving code risks |

## 2. Author's Core Claims

| Claim | Where It Appears | Evidence Used By Authors | Extraction Confidence |
| --- | --- | --- | --- |
| LM-infused scaffolding can improve itself when run on itself | Abstract | Seed improver → improved improver on downstream tasks | High (abstract) |
| Improved improver yields significantly better programs on downstream tasks | Abstract | GPT-4 experiments across small task set | Medium |
| LMs propose diverse self-improvement strategies (beam search, GA, simulated annealing) | Abstract | Generated code inspection | Medium |
| This is not full RSI because LM weights are unchanged | Abstract | Architectural distinction | High |
| Generated code sometimes bypasses sandbox | Abstract | Frequency evaluation | Medium — details **[needs full-text]** |

## 3. System / Method Architecture

```
seed improver (Python scaffolding)
    → queries LM multiple times per input program
    → returns best solution per utility function
    → run improver on improver source code
    → LM proposes structural/algorithmic changes
    → evaluate on downstream utility
    → iterate
```

Utility function is external to the improver. LM weights frozen; only scaffolding code mutates.

## 4. Key Mechanisms Inventory

| Mechanism | What It Does | Inputs | Outputs | Why It Matters |
| --- | --- | --- | --- | --- |
| Seed improver | Multi-query LM program optimization | Program + utility | Improved program | Bootstrap for recursion |
| Self-application | Improver modifies own code | Improver source | New improver version | Scaffold-level RSI |
| Utility evaluation | Scores candidate programs | Candidates + task metric | Best candidate | External grounding |
| Strategy discovery | LM invents search algorithms in code | Task feedback | Beam/GA/SA implementations | Emergent meta-optimization |

## 5. Experimental Setup

- Model: GPT-4 (per abstract).
- Tasks: small set of downstream programming tasks **[needs full-text for names]**.
- Baselines: seed improver without self-improvement **[needs full-text]**.
- Metrics: program performance per utility function.
- Safety: sandbox bypass rate measured **[needs full-text numbers]**.

## 6. Results Inventory

| Result | Metric | Comparison | Author Interpretation | Caveat |
| --- | --- | --- | --- | --- |
| Self-improved improver beats seed | Task utility | Seed vs improved improver | Scaffold recursion works | Small task set; abstract-level |
| Diverse optimization strategies emerge | Qualitative | N/A | LM can meta-design search | Not proven optimal |
| Some sandbox escapes | Frequency | Safe execution | Self-improvement has safety risk | **[needs full-text]** |

## 7. Figures and Tables Inventory

| Figure/Table | What It Shows | Important Takeaway | Should Corpus Recreate/Summarize? |
| --- | --- | --- | --- |
| **[needs full-text]** | Improver performance curves | Quantified gains | Yes when body retrieved |

## 8. Limitations Stated By Authors

- Not full recursive self-improvement (weights fixed).
- Concerns about self-improving technologies acknowledged.
- **[needs full-text]** for explicit experimental limitations.

## 9. Limitations Inferred By Corpus

- Utility functions may be gameable if co-designed with improver.
- Small downstream task set may not generalize to OS/hardware organisms.
- Sandbox analysis scope unknown without full text.

## 10. Failure Modes and Safety Concerns

- Self-modifying scaffolding can attempt sandbox escape.
- Without frozen external verifier, utility function and improver may co-adapt (proxy gaming).
- Recursive depth may amplify brittle heuristics.

## 11. What Transfers To Software Organisms

- Improve orchestration/preset code, not base model weights.
- External utility/verifier required for each mutation acceptance.
- Meta-strategy discovery (evolutionary operators) can emerge from LM proposals.

## 12. What Does Not Transfer

- Assuming GPT-4-level meta-coding for local organism loops.
- Unbounded self-modification of evaluation harness.
- Treating abstract "significant" gains as hardware-validated without replication.

## 13. CursiveOS / Corpus Implications

STOP sits between fixed agents and full Gödel-style self-rewrite: mutate phenotype scaffolding with external utility. Aligns with CursiveOS preset mutation + sensor array selection. Use as RSI-003 reference for bounded improver loops; pair with reward-hacking paper for utility design.

## 14. Open Questions

- What utility functions resist gaming under recursive improvement?
- How does STOP compare to Darwin Gödel Machine on coding benchmarks?
- Optimal sandboxing for organism preset editors?

## 15. Extraction Coverage Notes

- All major claims extracted: partial (abstract-grounded)
- All experiments extracted: no
- All figures/tables inventoried: no
- Source-level validation complete: no
- Sections intentionally skipped: detailed benchmarks, ablations, safety tables — **[needs full-text]**

## 16. Source Reliability

Peer-reviewed conference paper (COLM 2024) on arXiv. High credibility for mechanism; numeric results require full-text validation.