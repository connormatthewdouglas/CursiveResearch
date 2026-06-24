# Fork, Explore, Commit (BranchFS / FEC) — Deep Extraction

Source: https://arxiv.org/abs/2602.08199
Authors / Lab: Cong Wang, Yusheng Zheng
Year / Venue: 2026, arXiv (2602.08199v2)
Corpus Status: unvalidated
Extraction Type: important
Rights Status: extraction only (CC BY 4.0)

## 1. Paper Map

| Paper Section | What It Covers | Why It Exists In The Paper |
| --- | --- | --- |
| Motivation | Parallel agentic exploration needs isolation + atomic commit | OS gap for agents |
| Branch context abstraction | fork / explore / commit / abort lifecycle | Core concept |
| BranchFS | FUSE CoW filesystem per branch | Userspace realization |
| branch() syscall proposal | Kernel process + FS integration | Future kernel path |
| Evaluation | Creation/commit latency | Performance evidence |

## 2. Author's Core Claims

| Claim | Where It Appears | Evidence Used By Authors | Extraction Confidence |
| --- | --- | --- | --- |
| Agentic exploration needs isolated envs with atomic commit/rollback for FS + processes | Abstract | Problem | High |
| Branch context provides CoW isolation, lifecycle, first-commit-wins, nestable contexts | Abstract | Design | High |
| BranchFS: FUSE CoW, O(1) creation, atomic commit, sibling invalidation, no root | Abstract + eval | Implementation | High |
| branch() syscall proposed for kernel-enforced isolation/termination | Abstract | Design | Medium (proposal) |
| Branch creation <350µs; small-change commit <1ms | Abstract | Preliminary eval | High (abstract numbers) |

## 3. System / Method Architecture

```
Parent workspace
    → fork branch context (CoW FS view + process group)
    → explore (parallel solution paths)
    → commit winner (atomic merge to parent) OR abort
    → first-commit-wins invalidates sibling branches
    → nestable for hierarchical search trees
```

Components: BranchFS (open source), BranchContext Python library, proposed branch() syscall.

## 4. Key Mechanisms Inventory

| Mechanism | What It Does | Inputs | Outputs | Why It Matters |
| --- | --- | --- | --- | --- |
| Copy-on-write isolation | Independent FS views | Parent state | Branch workspace | Safe parallel tries |
| First-commit-wins | Resolves race between branches | Successful commit | Siblings invalidated | Deterministic winner |
| Atomic commit/abort | Merge or discard all branch state | Branch delta | Parent update / rollback | Agent safety |
| Nestable contexts | Sub-branches for hierarchical search | Parent branch | Child branches | Multi-level organisms |
| Process group binding | Couples FS + process lifecycle | branch() / library | Terminated explorers on abort | No zombie side effects |

## 5. Experimental Setup

- BranchFS on Linux (FUSE).
- Metrics: branch creation time vs base FS size; commit overhead vs change size.
- Preliminary microbenchmarks (not full agent end-to-end suite in abstract).

## 6. Results Inventory

| Result | Metric | Comparison | Author Interpretation | Caveat |
| --- | --- | --- | --- | --- |
| Fast branch creation | <350µs | Independent of base FS size | Cheap speculation | Preliminary |
| Small commit cost | <1ms | Modification-proportional | Low merge overhead | Small changes only |
| Open source availability | N/A | github.com/multikernel/branchfs | Deployable now | FUSE limitations |

## 7. Figures and Tables Inventory

| Figure/Table | What It Shows | Important Takeaway | Should Corpus Recreate/Summarize? |
| --- | --- | --- | --- |
| **[needs full-text]** | Latency vs change size | Scaling behavior | Yes |

## 8. Limitations Stated By Authors

- branch() syscall is proposal, not merged kernel **[inferred from abstract]**.
- Preliminary evaluation scope.

## 9. Limitations Inferred By Corpus

- FUSE performance overhead vs native overlayfs/btrfs snapshots.
- First-commit-wins may discard useful partial work from siblings.
- Does not replace population-level statistical confirmation on hardware.

## 10. Failure Modes and Safety Concerns

- Committed bad branch pollutes parent if verifier wrong.
- Resource exhaustion from too many parallel branches.
- Kernel-adjacent operations may escape FS-only isolation.

## 11. What Transfers To Software Organisms

- Parallel organism trials without contaminating lineage.
- Atomic promote/discard of preset mutations.
- Infrastructure for beam search / population exploration at OS level.
- Pairs with SchedCP/SemaTune speculative tuning sessions.

## 12. What Does Not Transfer

- Replacing hardware-scoped sensor confirmation with first-commit-wins alone.
- Assuming syscall available in production kernels today.

## 13. CursiveOS / Corpus Implications

BranchFS-FEC is enabling infrastructure for safe organism branching — aligns with population-based evolution and Chapter 01 confirmation. Use BranchContext for parallel preset evaluation; still require sensor array on committed winners.

## 14. Open Questions

- BranchFS + CursiveOS benchmark harness integration path?
- Nestable branches for MAP-Elites island parallelism?

## 15. Extraction Coverage Notes

- Abstract + evaluation summary extracted; syscall design details **[needs full-text]**

## 16. Source Reliability

Recent arXiv OS paper with open-source artifact. Credible systems contribution; agent-level eval limited.