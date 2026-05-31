# SWE-bench — Deep Extraction

Source: https://arxiv.org/abs/2310.06770  
Authors / Lab: Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, Karthik Narasimhan  
Year / Venue: 2024, ICLR; arXiv preprint  
Corpus Status: supported  
Extraction Type: cornerstone  
Rights Status: full-text allowed; CC BY 4.0

## 1. Paper Map

| Paper Section | What It Covers | Why It Exists In The Paper |
| --- | --- | --- |
| Abstract / Introduction | Defines real-world GitHub issue resolution as the benchmark target. | Frames software engineering as more than code completion. |
| Benchmark Construction | Explains how task instances are built from merged pull requests linked to issues. | Shows why the benchmark has executable, realistic task targets. |
| Task Format / Retrieval | Defines model inputs, retrieved files, oracle files, and patch generation. | Establishes the baseline evaluation setup and the localization problem. |
| Models / Results | Evaluates closed and open models on full SWE-bench and Lite. | Measures how hard real issue resolution is for non-agentic LMs. |
| Analysis | Studies repository difficulty, context length, retrieval quality, and input collapse. | Explains why long context alone does not solve the problem. |
| Limitations / Ethics | Notes Python-only scope, limits of execution-based tests, public repo data, and reproducibility. | Prevents overclaiming and records release constraints. |

## 2. Author's Core Claims

| Claim | Where It Appears | Evidence Used By Authors | Extraction Confidence |
| --- | --- | --- | --- |
| Real software engineering requires repository-scale localization and multi-file edits, not only code generation. | Introduction and benchmark motivation | GitHub issue / PR task construction from popular Python repositories | High |
| SWE-bench creates a more realistic arena than synthetic coding benchmarks. | Benchmark construction and comparison discussion | 2,294 task instances from real repositories with execution-based tests | High |
| Baseline LMs solve only a small fraction of tasks. | Results | Claude 2 resolves about 1.96% with BM25 retrieval; other baselines lower or comparable | High |
| More retrieved context can hurt performance even when recall improves. | Results / analysis | BM25 recall rises with larger context, but resolve rate can fall; oracle-collapsed context improves outcomes | High |
| Execution-based tests are necessary but insufficient for complete reliability. | Limitations | Authors note generated code can be less comprehensive, efficient, or readable than human solutions even when tests pass | High |

## 3. System / Method Architecture

SWE-bench is an evaluation framework, not an agent. It converts real GitHub issue
resolution into machine-evaluable tasks.

```text
select popular Python repo
-> find merged PR linked to issue
-> recover pre-fix repository state
-> preserve issue text as task prompt
-> use PR tests / changed tests to evaluate candidate patch
-> model generates patch
-> run tests in repository environment
-> mark task resolved only if tests pass
```

The model does not receive a toy function stub. It receives an issue and a
large repository context. The central challenge is localization: finding the
right file, class, function, or behavior inside a large codebase before making a
valid patch.

## 4. Key Mechanisms Inventory

| Mechanism | What It Does | Inputs | Outputs | Why It Matters |
| --- | --- | --- | --- | --- |
| Issue-to-PR mining | Builds tasks from real fixed issues. | GitHub issues, merged pull requests, repository history | Task instances | Grounds evaluation in real work. |
| Pre-fix checkout | Reconstructs codebase before the solution. | Repository commit history | Buggy starting state | Prevents evaluating on already-fixed code. |
| Patch generation | Asks model to produce a diff. | Issue text, retrieved context, prompt | Candidate patch | Keeps output comparable and executable. |
| Execution-based validation | Runs tests after patch application. | Candidate patch, repository tests | Resolved / unresolved | Provides grounded success signal. |
| Lite subset | Provides 300 more tractable instances. | Filtered full benchmark tasks | SWE-bench Lite | Improves adoption and iteration speed. |
| Oracle retrieval analysis | Uses known edited files as context. | Gold PR files | Upper-bound style localization setting | Separates retrieval/localization difficulty from editing ability. |

## 5. Experimental Setup

| Experiment | Task/Environment | Baseline | Metric | What It Tests |
| --- | --- | --- | --- | --- |
| BM25 retrieval | Full SWE-bench with retrieved files | ChatGPT-3.5, GPT-4, Claude 2, SWE-Llama | `% Resolved`, `% Apply` | Whether standard retrieval plus patch generation solves real issues. |
| Oracle retrieval | Known relevant files supplied | Same model families | `% Resolved`, `% Apply` | Whether localization is the bottleneck. |
| Context-length analysis | Vary retrieved context budget | BM25 recall and resolve rate | Recall vs resolved tasks | Whether more context helps or distracts. |
| Oracle-collapsed | Show only edited regions plus buffer | Oracle file setting | `% Resolved`, `% Apply` | Whether irrelevant code inside correct files hurts performance. |
| Date partition | Pre/post 2023 PRs | Oracle retrieval | `% Resolved` | Checks whether benchmark leakage is likely driving results. |

## 6. Results Inventory

| Result | Metric | Comparison | Author Interpretation | Caveat |
| --- | --- | --- | --- | --- |
| Claude 2 with BM25 resolves about 1.96% of full tasks. | `% Resolved` | Best baseline in main BM25 table | Real issue resolution is very hard for direct patch-generation LMs. | Later agentic systems improve, so use this as a baseline era result. |
| BM25 recall improves with longer context, but task resolution can drop. | Recall vs `% Resolved` | 13k, 27k, 50k context budgets | Retrieval recall is not enough; models struggle to use large noisy context. | Tokenization and model-specific context behavior vary. |
| Oracle-collapsed context improves performance. | `% Resolved` | More targeted code around edited lines | Irrelevant code inside long context distracts models. | This uses gold information unavailable in real deployment. |
| SWE-bench Lite makes iteration easier. | 300-task subset | Full 2,294-task benchmark | Smaller subset supports faster research cycles. | Lite may not capture the full distribution. |

## 7. Figures and Tables Inventory

| Figure/Table | What It Shows | Important Takeaway | Should Corpus Recreate/Summarize? |
| --- | --- | --- | --- |
| Figure 1 / task construction | GitHub issue and PR pipeline | The benchmark mirrors real open-source maintenance flow. | Summarize only. |
| Tables 2-6 | Model, retrieval, context, and oracle-collapsed results | Localization and context management dominate difficulty. | Summarize key numbers. |
| Figure 5 | Performance by context length / issue length | Bigger context is not automatically better. | Summarize in chapter guidance. |

## 8. Limitations Stated By Authors

- The benchmark is Python-only in the paper's evaluated form.
- Baseline methods are intentionally simple and do not exhaust future agentic
  methods.
- Passing execution-based tests does not guarantee comprehensive, efficient, or
  human-quality code.
- Repository and issue data are public, but benchmark construction still depends
  on GitHub task availability and filtering.

## 9. Limitations Inferred By Corpus

- SWE-bench rewards passing the available tests, which can still invite
  benchmark-specific behavior.
- The task format is software-engineering specific; CursiveOS shell tasks will
  include OS state, privileges, hardware, files, services, and user intent beyond
  GitHub bug fixes.
- Agent performance on SWE-bench should not be treated as proof of safe root
  operation.

## 10. Failure Modes and Safety Concerns

- Patches can pass tests while being brittle or unreadable.
- Models can apply syntactically valid but semantically wrong patches.
- Long-context retrieval can bury relevant information.
- If used as an optimization target, agents may learn benchmark-specific
  shortcuts rather than robust software engineering.

## 11. What Transfers To Software Organisms

- CursiveOS should prefer executable, grounded evaluation over self-judgment.
- Task success should be tied to tests, sensors, and post-checks, not prose
  confidence.
- Context minimization matters: feeding the whole machine state into an agent
  may reduce performance.
- Benchmark subsets should exist for rapid iteration, but acceptance needs the
  fuller distribution.

## 12. What Does Not Transfer

- SWE-bench does not evaluate hardware tuning, daemon integrity, firmware
  mutation, payment flows, or root-level OS operation.
- The benchmark assumes a repository patch target, while CursiveOS shell actions
  may mutate live system state.

## 13. CursiveOS / Corpus Implications

For CursiveOS, SWE-bench is most useful as evaluation philosophy:

```text
real task
-> reconstructed starting state
-> candidate action
-> executable evaluation
-> explicit success/failure
```

The natural-language shell should borrow this pattern. Every non-trivial action
should have a starting state, proposed diff/command, post-check, and rollback
where possible. The measurement daemon should remain the source of truth for
organism fitness.

## 14. Open Questions

- What is the CursiveOS analogue of SWE-bench for OS operation?
- Can shell tasks be represented as reproducible VM snapshots plus
  execution-based checks?
- How much of local-agent performance comes from base model quality versus
  interface design and tool scaffolding?

## 15. Extraction Coverage Notes

- All major claims extracted: yes
- All experiments extracted: mostly; appendices compressed
- All figures/tables inventoried: key figures/tables only
- Source-level validation complete: license and main results checked from local
  full text
- Sections intentionally skipped or compressed: detailed appendices and full
  repository/license tables

## 16. Source Reliability

Peer-reviewed conference paper at ICLR 2024 with public arXiv version. Strong
source for benchmark design and baseline results. Use later leaderboard numbers
only after checking current benchmark records separately.
