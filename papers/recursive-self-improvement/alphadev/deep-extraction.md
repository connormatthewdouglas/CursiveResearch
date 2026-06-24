# AlphaDev — Deep Extraction

Source: https://www.nature.com/articles/s41586-023-06004-9
Authors / Lab: Daniel J. Mankowitz et al., Google DeepMind
Year / Venue: 2023, Nature (s41586-023-06004-9)
Corpus Status: unvalidated
Extraction Type: important
Rights Status: extraction only (Nature proprietary license)

## 0. Extraction Provenance

Based on Nature abstract, public summaries, and DeepMind announcements. Full text not stored. **[needs full-text]** for assembly listings and training details.

## 1. Paper Map

| Paper Section | What It Covers | Why It Exists In The Paper |
| --- | --- | --- |
| Introduction | Discovering faster sorting via RL | Bridge AI + systems performance |
| AlphaDev agent | RL + MCTS in assembly program space | Search method |
| Correctness verification | Ensure semantic equivalence to reference sort | Safety gate |
| CPU integration | Optimized routines in production libraries | Real-world impact |
| Analysis | Why discovered instructions help | Interpretability |

## 2. Author's Core Claims

| Claim | Where It Appears | Evidence Used By Authors | Extraction Confidence |
| --- | --- | --- | --- |
| Deep RL can discover faster sorting algorithms at assembly level | Abstract / press | Nature peer review | High |
| Discovered routines integrated into LLVM libc++ sort | Reported deployment | Production adoption claim | Medium-High |
| MCTS + RL explores instruction sequences humans overlook | Method summaries | Search narrative | Medium |
| Correctness preserved vs reference implementations | Verification pipeline | Formal/testing checks | High (claimed) |

## 3. System / Method Architecture

```
Reference sorting specification
    → RL agent proposes assembly instruction sequences
    → MCTS explores search tree
    → Verifier checks functional correctness
    → Performance benchmark on target CPU uarch
    → keep improvements
```

Low-level program discovery with strict equivalence checking before acceptance.

## 4. Key Mechanisms Inventory

| Mechanism | What It Does | Inputs | Outputs | Why It Matters |
| --- | --- | --- | --- | --- |
| Assembly-level search | Optimizes real machine instructions | ISA, uarch | Instruction routines | Deployable artifacts |
| MCTS + RL | Balances exploration/exploitation | Search state | Candidate programs | Finds non-obvious sequences |
| Correctness verifier | Blocks wrong sorts | Candidate + spec | Accept/reject | Non-negotiable gate |
| Microbenchmark fitness | Latency on hardware | Routines | Performance score | Grounded selection |

## 5. Experimental Setup

- Target: sorting routines (e.g., small array sorts) in assembly.
- Baselines: human-optimized standard library sorts.
- Metrics: instruction count / runtime on specific CPUs.
- Deployment: LLVM libc++ integration (reported).

## 6. Results Inventory

| Result | Metric | Comparison | Author Interpretation | Caveat |
| --- | --- | --- | --- | --- |
| Faster sort routines | Cycle count / wall time | Prior libc++ sorts | Meaningful micro-optimization | uarch-specific |
| Production integration | Adoption | N/A | Not just toy benchmark | Maintenance burden |
| Novel instruction patterns | Qualitative | Human designs | AI discovery credible | **[needs full-text]** |

## 7. Figures and Tables Inventory

| Figure/Table | What It Shows | Important Takeaway | Should Corpus Recreate/Summarize? |
| --- | --- | --- | --- |
| **[needs full-text]** | Discovered vs baseline assembly | Instruction-level gains | Summarize qualitatively |
| **[needs full-text]** | Speedups across sizes | When gains appear | Yes |

## 8. Limitations Stated By Authors

- Scope limited to specific sort families and hardware targets.
- **[needs full-text]** for generalization limits.

## 9. Limitations Inferred By Corpus

- Assembly discovery pipeline not trivially reusable for high-level OS knob tuning.
- Uarch specificity → organism gains may not transfer across hardware population.
- Nature licensing blocks full method reproduction in corpus.

## 10. Failure Modes and Safety Concerns

- Verifier gaps → subtle mis-sorts.
- Overfitting to benchmark array distributions.
- Deployment of evolved code without population confirmation risky.

## 11. What Transfers To Software Organisms

- Always verify correctness before performance selection.
- Low-level discoverable artifacts can ship if gates are strong.
- Search + verifier pattern precedes FunSearch/AlphaEvolve.

## 12. What Does Not Transfer

- Claiming CursiveOS will evolve libc++ sorts by default.
- RL assembly MCTS without equivalent correctness proofs on OS configs.

## 13. CursiveOS / Corpus Implications

RSI-009 anchors the DeepMind discovery lineage (AlphaDev → FunSearch → AlphaEvolve). For CursiveOS, use as evidence that verifier-gated search can yield deployable systems improvements — but organism focus is higher-level presets/knobs with hardware-scoped sensors, not assembly MCTS.

## 14. Open Questions

- Any AlphaDev-style micro-kernel paths relevant to CursiveOS network/cold-start stacks?

## 15. Extraction Coverage Notes

- Partial extraction from public sources; Nature body **[needs full-text]**

## 16. Source Reliability

Peer-reviewed Nature (DeepMind). Very high authority; details rights-limited.