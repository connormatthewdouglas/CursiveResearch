# Darwin Gödel Machine (DGM) — Deep Extraction

Source: https://arxiv.org/abs/2505.22954
Authors / Lab: Jenny Zhang, Shengran Hu, Cong Lu, Robert Lange, Jeff Clune
Year / Venue: 2025–2026, arXiv (2505.22954v3)
Corpus Status: unvalidated
Extraction Type: cornerstone
Rights Status: extraction only (CC BY 4.0)

## 1. Paper Map

| Paper Section | What It Covers | Why It Exists In The Paper |
| --- | --- | --- |
| Motivation | Limits of fixed architectures + meta-learning | Need self-modifying agents |
| Gödel machine theory | Provable self-improvements impossible practically | Contrast |
| DGM method | Archive + FM mutations + benchmark validation | Core algorithm |
| Open-ended exploration | Tree of diverse coding agents | Stepping stones |
| Experiments | SWE-bench, Polyglot, ablations | Empirical results |
| Safety | Sandboxing, human oversight | Risk mitigation |

## 2. Author's Core Claims

| Claim | Where It Appears | Evidence Used By Authors | Extraction Confidence |
| --- | --- | --- | --- |
| Fixed human-designed agents cannot autonomously continuously self-improve | Abstract | Argument | High |
| Gödel machine proofs impractical; DGM uses empirical validation on coding benchmarks | Abstract | Method | High |
| DGM modifies own code, improving ability to modify codebase over time | Abstract | Loop design | High |
| Maintains archive; FM creates interesting variants from sampled agents | Abstract | Open-endedness | High |
| SWE-bench: 20.0% → 50.0%; Polyglot: 14.2% → 30.7% | Abstract | Benchmarks | High |
| Outperforms baselines without self-improvement or open-ended exploration | Abstract | Ablations | Medium |
| Safety: sandboxing + human oversight used | Abstract | Precautions | High |

## 3. System / Method Architecture

```
Archive of coding agents (diverse tree)
Sample agent A from archive
Foundation model proposes modified agent A' (interesting variant)
Empirically validate A' on coding benchmarks (SWE-bench, Polyglot)
If improved → add to archive
Parallel exploration of many branches
```

Combines Darwinian evolution + Gödel-inspired self-modification without formal proofs.

## 4. Key Mechanisms Inventory

| Mechanism | What It Does | Inputs | Outputs | Why It Matters |
| --- | --- | --- | --- | --- |
| Self-code modification | Agent edits own implementation | Source + FM | New agent | Strongest RSI form |
| Archive sampling | Parent selection for mutations | Tree archive | Parent agent | Diversity |
| Interestingness mutation | FM bias toward novel variants | Parent | Child agents | Open-ended exploration |
| Benchmark validation | Empirical acceptance test | Child agent | Pass/fail + score | Practical Gödel substitute |
| Capability meta-improvement | Better editors over time | Iterations | Higher solve rates | RSI on RSI tools |

## 5. Experimental Setup

- Benchmarks: SWE-bench, Polyglot.
- Starting performance: 20.0% / 14.2%.
- Final performance: 50.0% / 30.7%.
- Baselines: no self-improvement; no open-ended exploration **[needs full-text details]**.
- Safety: sandbox, human oversight.
- Code: github.com/jennyzzt/dgm.

## 6. Results Inventory

| Result | Metric | Comparison | Author Interpretation | Caveat |
| --- | --- | --- | --- | --- |
| SWE-bench lift | 20.0% → 50.0% | Initial agent | Strong self-improvement | Benchmark-specific |
| Polyglot lift | 14.2% → 30.7% | Initial agent | Generalizes across suites | Still coding-only |
| Ablation superiority | Solve rate | Non-OE / non-self-improve baselines | Both components needed | **[needs full-text]** |
| Auto-improved tooling | Qualitative | Evolved editors, context mgmt, peer review | Meta-capability gains | **[needs full-text examples]** |

## 7. Figures and Tables Inventory

| Figure/Table | What It Shows | Important Takeaway | Should Corpus Recreate/Summarize? |
| --- | --- | --- | --- |
| **[needs full-text]** | Archive tree growth | Open-ended branching | Yes |
| **[needs full-text]** | Ablation bars | Component contributions | Yes |

## 8. Limitations Stated By Authors

- Empirical validation ≠ provable improvement.
- Safety precautions required; not fully autonomous unsupervised deployment.
- **[needs full-text]** for compute, failure cases.

## 9. Limitations Inferred By Corpus

- Agent modifies own judge/tooling — risks reward hacking without frozen verifier.
- SWE-bench ≠ hardware-scoped OS fitness.
- Interestingness criterion may be subjective/FM-biased.

## 10. Failure Modes and Safety Concerns

- Self-modification of evaluation harness.
- Archive pollution with brittle agents.
- Capability overhang if oversight removed.

## 11. What Transfers To Software Organisms

- Archive-based open-ended search with parallel branches.
- Empirical benchmark gates instead of proof gates.
- Validate meta-improvements (better editors) on same frozen benchmarks.
- Safety: sandbox + human oversight patterns.

## 12. What Does Not Transfer

- Full agent self-rewrite of CursiveOS sensor array or verifier.
- Claiming 50% SWE-bench ⇒ OS tuning success.
- Removing human oversight in production organism deployment.

## 13. CursiveOS / Corpus Implications

RSI-016: closest coding-agent analogue to software organisms. CursiveOS deliberately constrains RSI: mutate presets/genomes, not agent self-code; frozen sensor array as external validator. DGM demonstrates what's possible with fewer constraints — use as upper-bound reference and safety cautionary tale. Pairs with Gödel Agent paper in corpus.

## 14. Open Questions

- DGM archive on CursiveOS preset space with sensor confirmation?
- Can "interestingness" be replaced by MAP-Elites behavioral novelty?

## 15. Extraction Coverage Notes

- Strong abstract extraction; v3 body **[needs full-text]** for ablations and tooling examples

## 16. Source Reliability

Recent arXiv from Clune lineage with open code. High relevance; benchmarks are standard agent evals.