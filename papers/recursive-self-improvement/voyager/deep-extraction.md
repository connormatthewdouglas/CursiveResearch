# Voyager — Deep Extraction

Source: https://arxiv.org/abs/2305.16291
Authors / Lab: Guanzhi Wang et al. (NVIDIA / Caltech / UT Austin collaborators)
Year / Venue: 2023, arXiv preprint (2305.16291v2)
Corpus Status: unvalidated
Extraction Type: important
Rights Status: extraction only (arXiv non-exclusive)

## 1. Paper Map

| Paper Section | What It Covers | Why It Exists In The Paper |
| --- | --- | --- |
| Introduction | Lifelong embodied agent in Minecraft | Open-ended skill acquisition without fine-tuning |
| Automatic curriculum | Task proposals maximizing exploration | Drives continual learning |
| Skill library | Executable code storage/retrieval | Compositional persistent memory |
| Iterative prompting | Feedback + errors + self-verification | Code refinement loop |
| Experiments | Minecraft tech tree, generalization | Empirical claims |

## 2. Author's Core Claims

| Claim | Where It Appears | Evidence Used By Authors | Extraction Confidence |
| --- | --- | --- | --- |
| First LLM-powered embodied lifelong learning agent in Minecraft without human intervention | Abstract | System design + experiments | High |
| 3.3× more unique items, 2.3× travel distance, up to 15.3× faster tech milestones vs prior SOTA | Abstract | Minecraft metrics | High (abstract numbers) |
| Skill library enables zero-shot novel tasks in new worlds | Abstract | Transfer experiments | Medium |
| Skills are interpretable, compositional, temporally extended | Abstract | Qualitative + library design | Medium |
| Blackbox GPT-4 queries suffice (no fine-tuning) | Abstract | Method | High |

## 3. System / Method Architecture

```
Automatic Curriculum (proposes next tasks)
        ↓
GPT-4 → generates control/skill code
        ↓
Minecraft environment execution
        ↓
Iterative prompting (env feedback, stack traces, self-verify)
        ↓
Skill Library (store/retrieve/reuse code skills)
        ↓
Repeat (lifelong loop)
```

Three coupled components: curriculum, library, iterative refinement.

## 4. Key Mechanisms Inventory

| Mechanism | What It Does | Inputs | Outputs | Why It Matters |
| --- | --- | --- | --- | --- |
| Automatic curriculum | Selects exploratory tasks | Agent state, progress | Next objective | Open-ended drive |
| Skill library | Indexed executable behaviors | Successful programs | Reusable skills | Anti-forgetting, composition |
| Iterative prompting | Debug/improve code | Errors, observations | Revised program | Tight feedback loop |
| Self-verification | LLM checks own programs | Code + spec | Pass/fail refinement | Reduces bad commits |

## 5. Experimental Setup

- Environment: Minecraft (MineDojo ecosystem).
- Model: GPT-4 via API (blackbox).
- Baselines: prior SOTA Minecraft agents **[needs full-text names]**.
- Metrics: unique items, distance traveled, tech tree milestone time.
- Generalization: new Minecraft world, novel tasks from scratch.

## 6. Results Inventory

| Result | Metric | Comparison | Author Interpretation | Caveat |
| --- | --- | --- | --- | --- |
| More exploration | 3.3× unique items | vs prior SOTA | Strong lifelong learning | Minecraft-specific |
| Longer traversal | 2.3× distance | vs prior SOTA | Better exploration | Same |
| Faster progression | up to 15.3× tech milestones | vs prior SOTA | Curriculum + library effective | Best-case multiplier |
| Transfer to new world | Task success from scratch | vs other techniques | Library generalizes | **[needs full-text tables]** |

## 7. Figures and Tables Inventory

| Figure/Table | What It Shows | Important Takeaway | Should Corpus Recreate/Summarize? |
| --- | --- | --- | --- |
| **[needs full-text]** | Tech tree progression timelines | Quantified speedups | Yes |
| **[needs full-text]** | Skill library growth | Compositional accumulation | Yes |

## 8. Limitations Stated By Authors

- **[needs full-text]** — abstract does not list explicit limitations.

## 9. Limitations Inferred By Corpus

- GPT-4 API cost and latency at scale.
- Minecraft simulator ≠ real OS/hardware organisms.
- Self-verification is LLM-judged, not frozen external verifier.
- Curriculum may overfit Minecraft task structure.

## 10. Failure Modes and Safety Concerns

- Erroneous skills stored in library propagate.
- Self-verification false positives commit bad code.
- Open-ended exploration without hardware-scoped gates risky in production systems.

## 11. What Transfers To Software Organisms

- Persistent skill/code library as organism memory.
- Automatic curriculum for benchmark sequencing.
- Iterative execute-debug loop with environment feedback.
- Composition of verified sub-skills into larger behaviors.

## 12. What Does Not Transfer

- Embodied Minecraft action space to kernel tuning.
- Claiming 15.3× speedup on CursiveOS benchmarks without replication.
- Blackbox GPT-4 dependence for local closed-loop organisms.

## 13. CursiveOS / Corpus Implications

Voyager (RSI-005) exemplifies open-ended agent memory without weight updates — aligned with Chapter 03. CursiveOS can adopt library + curriculum patterns for preset/skill archives, but must substitute deterministic sensor array for self-verification. Pairs with POET/open-endedness papers for curriculum design.

## 14. Open Questions

- Can skill libraries transfer across benchmark suites (not just Minecraft worlds)?
- How to index/retrieve skills under hardware-scoped fitness dimensions?
- Curriculum safety constraints for OS-modifying organisms?

## 15. Extraction Coverage Notes

- All major claims extracted: yes (abstract-level)
- All experiments extracted: partial
- All figures/tables inventoried: no
- Source-level validation complete: no
- Sections skipped: prompt templates, ablations — **[needs full-text]**

## 16. Source Reliability

Widely cited arXiv preprint with open-source codebase (voyager.minedojo.org). Strong empirical claims; full validation needs paper body.