# OSWorld — Deep Extraction

Source: https://arxiv.org/abs/2404.07972  
Authors / Lab: Tianbao Xie et al.  
Year / Venue: 2024, arXiv preprint  
Corpus Status: supported  
Extraction Type: cornerstone  
Rights Status: full-text allowed; CC BY 4.0

## 1. Paper Map

| Paper Section | What It Covers | Why It Exists In The Paper |
| --- | --- | --- |
| Abstract / Introduction | Defines OSWorld as a real-computer environment for multimodal agents. | Frames the gap between web/app benchmarks and real OS operation. |
| Environment Definition | Formalizes observations, actions, setup, execution, and evaluation. | Makes desktop operation measurable. |
| Benchmark Construction | Describes 369 Ubuntu tasks, 43 Windows analytic tasks, setup configs, evaluation scripts, and quality control. | Shows task diversity and reproducibility work. |
| Baselines / Results | Evaluates LLM/VLM agents with screenshots, accessibility trees, and Set-of-Marks. | Quantifies current agent weakness in real computer tasks. |
| Analysis | Studies GUI grounding, operational knowledge, screenshots, a11y trees, and workflow tasks. | Identifies failure classes relevant to OS shells. |
| Conclusion / Future Work | Calls for better GUI grounding, context encoding, exploration, memory, and reflection. | Connects benchmark gaps to agent architecture research. |

## 2. Author's Core Claims

| Claim | Where It Appears | Evidence Used By Authors | Extraction Confidence |
| --- | --- | --- | --- |
| Existing benchmarks do not cover the diversity of real computer use. | Introduction / comparison table | Comparison to web, mobile, code, and static benchmarks | High |
| OSWorld provides a scalable executable environment for arbitrary computer tasks. | Environment and benchmark sections | VM setup, action space, setup configs, evaluation scripts | High |
| Current agents are far below human performance on real computer tasks. | Abstract / results | Humans about 72.36%; best reported model about 12.24% in table | High |
| GUI grounding and operational knowledge are major bottlenecks. | Results / analysis | Low screenshot and workflow performance; qualitative analysis | High |
| Execution-based evaluation is essential and expensive. | Benchmark construction | 134 unique evaluation functions, multi-round checks, large annotation effort | High |

## 3. System / Method Architecture

OSWorld provides a virtualized real-computer task environment:

```text
task instruction
-> VM image and initial-state setup
-> agent observes screenshot and/or accessibility tree
-> agent emits keyboard/mouse/code action
-> environment executes action
-> loop continues until DONE/FAIL/limit
-> evaluator extracts final state
-> execution-based script scores success
```

The benchmark is important because it does not reduce computer use to a single
browser page or toy UI. It includes files, applications, OS settings, workflows,
and cross-application tasks.

## 4. Key Mechanisms Inventory

| Mechanism | What It Does | Inputs | Outputs | Why It Matters |
| --- | --- | --- | --- | --- |
| Real OS VM | Runs tasks inside actual operating-system environments. | VM image, setup config | Interactive desktop state | Gives agents real computer state and side effects. |
| Initial-state setup | Prepares files, apps, windows, and settings. | Task config | Reproducible starting state | Makes tasks closer to midstream real use. |
| Raw action space | Uses keyboard/mouse / pyautogui-style actions. | Agent command | UI mutation | Avoids narrow app-specific action APIs. |
| Accessibility tree input | Provides structured UI element data. | OS a11y APIs | Text/table observation | Helps language models ground UI elements. |
| Screenshot input | Provides human-like visual observation. | Desktop screenshot | Image observation | Tests visual grounding. |
| Set-of-Marks | Annotates screenshot elements with labels. | Screenshot plus element boxes | Marked image / metadata | Attempts to improve coordinate grounding. |
| Execution evaluators | Check final task outcome. | Final OS/app state | Success/failure | Provides grounded task scoring. |

## 5. Experimental Setup

| Experiment | Task/Environment | Baseline | Metric | What It Tests |
| --- | --- | --- | --- | --- |
| Human performance | OSWorld and sampled WebArena tasks | Human annotators | Accuracy, time | Establishes human reference difficulty. |
| A11y-tree agents | Text-form UI tree input | Mixtral, Llama, GPT, Gemini, Qwen, Claude | Success rate | Whether text-only UI structure is enough. |
| Screenshot agents | Raw screenshots | VLM baselines | Success rate | Whether visual perception can drive OS actions. |
| Screenshot + a11y | Combined observations | VLM baselines | Success rate | Whether hybrid inputs improve grounding. |
| Set-of-Marks | Annotated screenshot plus metadata | VLM baselines | Success rate | Whether mark-based grounding helps desktop tasks. |
| Category analysis | OS, Office, Daily, Professional, Workflow | Model groups and humans | Success by category | Which task classes are hardest. |

## 6. Results Inventory

| Result | Metric | Comparison | Author Interpretation | Caveat |
| --- | --- | --- | --- | --- |
| Human performance is about 72.36%. | Accuracy | OSWorld human study | Tasks are difficult but feasible. | Annotators are CS students, not all user populations. |
| Best reported model reaches about 12.24%. | Overall success | GPT-4 with a11y tree in table | Current agents are far from reliable computer assistants. | Model landscape changes; check current leaderboard before quoting as latest. |
| Workflow tasks are especially weak for agents. | Category success | Human performance remains more stable | Cross-app state and operational knowledge are hard. | Exact rates depend on input modality/model. |
| OSWorld has 369 Ubuntu tasks and 134 unique evaluation functions. | Dataset statistics | Compared with other benchmarks | Execution-based desktop evaluation is complex. | Windows tasks have copyright/activation caveats. |
| Screenshot-only is low but strategically important. | Success rate | Screenshot vs a11y / hybrid settings | Human-like visual input remains hard but portable. | a11y is easier where available. |

## 7. Figures and Tables Inventory

| Figure/Table | What It Shows | Important Takeaway | Should Corpus Recreate/Summarize? |
| --- | --- | --- | --- |
| Figure 1 | OSWorld environment overview | Real desktop tasks need setup, action, and evaluation. | Summarize. |
| Table 3 | Dataset statistics | 369 tasks, 302 initial states, 134 eval scripts, 101 workflow tasks. | Preserve key numbers. |
| Table 4 | Benchmark comparison | OSWorld uniquely combines real computer environment, multimodal support, cross-app tasks, and many evaluators. | Summarize. |
| Table 5 | Baseline model results | Human-computer gap is large. | Preserve key numbers with date caveat. |

## 8. Limitations Stated By Authors

- Current agents struggle with GUI grounding and operational knowledge.
- Screenshot-only input is difficult but important for portability.
- Accessibility trees can be large, noisy, unavailable, or inconsistent.
- The benchmark required substantial human labor and may still contain false
  positives/negatives.
- Windows tasks have copyright/activation restrictions.

## 9. Limitations Inferred By Corpus

- OSWorld is a strong benchmark analogue for CursiveOS shell work, but CursiveOS
  also needs safety, privilege, rollback, daemon integrity, and hardware
  measurement criteria.
- Success in a VM benchmark does not prove safety on a user's live host.
- Agents can still optimize to benchmark quirks if OSWorld becomes a training
  target.

## 10. Failure Modes and Safety Concerns

- Coordinate-level GUI mistakes.
- Misreading or overloading accessibility trees.
- Cross-application state loss.
- Incomplete task termination or false DONE/FAIL.
- Accidental side effects in realistic OS environments.
- Copyright/licensing complexity around proprietary app tasks.

## 11. What Transfers To Software Organisms

- CursiveOS shell evaluation should use VM snapshots and execution-based checks.
- Real OS tasks require both GUI and CLI awareness.
- Starting from intermediate state is important; not every task begins at a clean
  desktop.
- Workflow tasks are a distinct difficulty class.
- Evaluation scripts are expensive but necessary for grounded progress.

## 12. What Does Not Transfer

- OSWorld does not evaluate CursiveRoot measurement truth, Bitcoin payouts,
  firmware mutation, or hardware tuning.
- It focuses on task completion, not long-term organism fitness or fleet
  confirmation.

## 13. CursiveOS / Corpus Implications

OSWorld is the best current reference in this intake for evaluating a
natural-language shell as an OS operator. A future Cursive shell benchmark should
look more like OSWorld than a chat benchmark:

```text
VM snapshot
-> task instruction
-> bounded agent action
-> observable OS/app state
-> execution-based evaluator
-> rollback / reset
```

For live CursiveOS, this must be paired with the safety rules from Chapter 12:
deterministic policy, explicit confirmation, containment, and no LLM write path
to measurement truth.

## 14. Open Questions

- Which Cursive shell tasks should be benchmarked in VM before live host access?
- Can CursiveOS reuse OSWorld-style configs for Linux-first operator testing?
- What is the right mix of CLI, GUI, a11y tree, and screenshot observations?
- How should infeasible tasks be represented so agents can correctly refuse?

## 15. Extraction Coverage Notes

- All major claims extracted: yes
- All experiments extracted: yes at main-result level; appendix details
  compressed
- All figures/tables inventoried: key figures/tables only
- Source-level validation complete: license and main results checked from local
  full text
- Sections intentionally skipped or compressed: long task examples, detailed
  appendix prompts, full evaluator descriptions

## 16. Source Reliability

arXiv preprint with public benchmark/project release. Strong source for desktop
agent evaluation methodology. Treat model performance numbers as time-sensitive;
recheck leaderboard before using them as current capability claims.
