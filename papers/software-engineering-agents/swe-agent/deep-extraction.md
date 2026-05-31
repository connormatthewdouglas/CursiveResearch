# SWE-agent — Deep Extraction

Source: https://arxiv.org/abs/2405.15793  
Authors / Lab: John Yang, Carlos E. Jimenez, Alexander Wettig, Kilian Lieret, Shunyu Yao, Karthik Narasimhan, Ofir Press  
Year / Venue: 2024, NeurIPS; arXiv preprint  
Corpus Status: supported  
Extraction Type: cornerstone  
Rights Status: full-text allowed; CC BY 4.0

## 1. Paper Map

| Paper Section | What It Covers | Why It Exists In The Paper |
| --- | --- | --- |
| Abstract / Introduction | Introduces agent-computer interfaces (ACIs) and SWE-agent. | Frames LMs as a new kind of computer user. |
| Agent-Computer Interface | Defines ACI and design principles. | Shows why ordinary human UIs are often bad for agents. |
| SWE-agent System | Describes search, navigation, editing, command feedback, and context management. | Provides concrete interface patterns. |
| Evaluation | Tests on SWE-bench, SWE-bench Lite, and HumanEvalFix. | Measures whether ACI design changes outcomes. |
| ACI Analysis / Ablations | Compares search/edit/context designs. | Identifies which interface affordances matter. |
| Discussion / Limitations | Generalizes ACI as a research direction. | Transfers lessons beyond software engineering. |

## 2. Author's Core Claims

| Claim | Where It Appears | Evidence Used By Authors | Extraction Confidence |
| --- | --- | --- | --- |
| LMs are a new end-user category and need interfaces designed for their limitations. | Introduction / ACI section | Qualitative behavior plus ablations | High |
| ACI design can substantially improve agent performance without changing model weights. | Results and ablations | SWE-agent vs RAG and shell-only baselines | High |
| Small, simple, LM-friendly command sets outperform raw shell-only interaction for SWE tasks. | System design and Table 1 / Table 3 | Search/edit/context ablations on SWE-bench Lite | High |
| Guardrails and concise feedback reduce error propagation. | ACI principles and case studies | Interface analysis and observed trajectories | Medium/high |
| ACI principles may transfer to other digital-work domains. | Discussion and limitations | Conceptual argument from HCI analogy | Medium |

## 3. System / Method Architecture

SWE-agent is an LM agent wrapped in an agent-computer interface:

```text
issue description
-> system prompt and ACI instructions
-> model emits thought + command
-> ACI executes bounded command
-> ACI returns concise observation / error / state
-> model iterates
-> final repository state submitted as patch
-> tests determine resolution
```

The ACI is not a cosmetic wrapper. It defines available actions, observation
format, history compression, feedback messages, and guardrails. This makes the
interface part of the agent's intelligence.

## 4. Key Mechanisms Inventory

| Mechanism | What It Does | Inputs | Outputs | Why It Matters |
| --- | --- | --- | --- | --- |
| LM-friendly search | Provides concise search results and refinement guidance. | Query, repository | Bounded result list | Prevents exhaustive wandering through noisy shell output. |
| File viewer | Shows controlled windows of file content. | File path, line window | Focused code context | Keeps context relevant and navigable. |
| Edit command | Enables structured multi-line edits with feedback. | Target range and replacement | Modified file plus updated view | Avoids brittle `sed`/redirection patterns. |
| Command feedback | Returns specific messages for success/failure/no output. | Executed command | Observation | Reduces ambiguity for the model. |
| Context management | Keeps recent observations and demonstrations in model context. | Interaction history | Prompt context | Controls cost and distraction. |
| Guardrails | Prevents common command/edit mistakes. | Proposed action | Allowed/rejected/feedback | Reduces cascading failure. |

## 5. Experimental Setup

| Experiment | Task/Environment | Baseline | Metric | What It Tests |
| --- | --- | --- | --- | --- |
| Full SWE-bench | 2,294 real GitHub issue tasks | RAG baselines | `% Resolved`, average cost | Whether an interactive ACI improves real issue resolution. |
| SWE-bench Lite | 300 selected tasks | RAG and shell-only | `% Resolved`, average cost | Faster ACI comparison and ablation. |
| HumanEvalFix | Short-form debugging benchmark | Published model scores | pass@1 | Basic code editing/debugging ability. |
| Search ablations | Different search UI designs | Summarized, iterative, no search | `% Resolved` | How search presentation affects agent behavior. |
| Edit ablations | Structured edit vs no edit | No structured edit | `% Resolved` | Whether compact editing commands matter. |
| Context ablations | Recent observations vs full history / no demo | Context variants | `% Resolved` | How context policy affects performance. |

## 6. Results Inventory

| Result | Metric | Comparison | Author Interpretation | Caveat |
| --- | --- | --- | --- | --- |
| SWE-agent with GPT-4 Turbo solves 12.47% of full SWE-bench. | `% Resolved` | RAG GPT-4 Turbo at 1.31% in reported table | Interactive ACI is a large improvement over direct patch generation. | Still leaves most tasks unsolved. |
| SWE-agent solves 18.00% on SWE-bench Lite. | `% Resolved` | Shell-only GPT-4 Turbo 11.00%; RAG 2.67% | ACI improves over shell-only and RAG. | Higher API cost than RAG. |
| Claude 3 Opus with SWE-agent solves 10.46% full / 13.00% Lite. | `% Resolved` | Alternate base model | ACI transfers across strong LMs. | Not all models worked well. |
| HumanEvalFix pass@1 around 88.3% overall. | pass@1 | Prior reported model scores | Structured interaction can support debugging tasks. | HumanEvalFix is much narrower than real repo work. |
| Iterative search underperforms summarized search. | SWE-bench Lite ablation | Search UI variants | Human-like browsing can cause agents to exhaustively inspect results and waste budget/context. | Specific to this task/interface. |
| Full-file context underperforms 100-line file view. | SWE-bench Lite ablation | File viewer variants | More context can be worse than focused windows. | Needs rechecking for newer models. |

## 7. Figures and Tables Inventory

| Figure/Table | What It Shows | Important Takeaway | Should Corpus Recreate/Summarize? |
| --- | --- | --- | --- |
| Figure 1 | LM plus ACI loop | Interface is part of the agent system. | Summarize in Chapter 12. |
| Table 1 | SWE-bench and Lite results | ACI beats RAG and shell-only baselines. | Preserve key numbers. |
| Table 3 | ACI ablations | Search, edit, file view, and context management matter. | Summarize design lessons. |
| Search interface figure | Shell-only, iterative, summarized search | Agent-friendly search differs from human UI search. | Summarize conceptually. |

## 8. Limitations Stated By Authors

- Final toolkit is small; additional tools such as web browsing, static analysis,
  dynamic analysis, fault localization, and fuzzing could help.
- ACI design was manual and based on observations of trajectories.
- The system focuses on programmatic software-engineering tasks.
- Transfer to other domains remains an open question.

## 9. Limitations Inferred By Corpus

- Better task performance does not equal safety. ACI guardrails must be paired
  with authority control and sandboxing for OS-level agents.
- SWE-agent assumes a repository task where final state can be tested; live OS
  mutation needs rollback and system-health checks.
- ACI design might overfit to one benchmark or model family.

## 10. Failure Modes and Safety Concerns

- Agent-friendly tools can amplify capability and therefore amplify risk.
- A search/edit interface that is too powerful can make unsafe filesystem
  mutation easier.
- Cost budgets can force premature submission of existing edits.
- ACI commands become a supply-chain and policy surface.

## 11. What Transfers To Software Organisms

- The Cursive shell should be designed as an ACI, not just a chat prompt wrapped
  around a terminal.
- Agent tools should be few, explicit, documented, and guardrailed.
- Tool results should be concise, structured, and action-relevant.
- Full history can be worse than recent focused observations.
- Interface design is a measurable research variable.

## 12. What Does Not Transfer

- SWE-agent does not address measurement-daemon integrity.
- It does not solve prompt injection, root safety, hardware mutation, or
  persistent memory poisoning.
- The benchmark target is code patches, not whole-machine operation.

## 13. CursiveOS / Corpus Implications

Chapter 12 should treat the natural-language shell as an agent-computer
interface:

```text
human intent
-> shell ACI proposes bounded action
-> deterministic policy checks authority
-> sandbox/helper executes
-> concise observation returns
-> user and daemon truth remain separate
```

The most important transfer is that command design matters. A raw shell is not
automatically the best interface for a model. CursiveOS should expose
agent-native actions only when their authority, feedback, and rollback semantics
are explicit.

## 14. Open Questions

- What is the minimum useful Cursive shell command set?
- Which Cursive shell actions are agent-native wrappers and which remain raw
  terminal commands?
- Can ACI design be optimized without overfitting to a benchmark?
- How should ACI tools declare risk and privilege to the policy layer?

## 15. Extraction Coverage Notes

- All major claims extracted: yes
- All experiments extracted: yes at main-result level; appendices compressed
- All figures/tables inventoried: key ones only
- Source-level validation complete: license and main results checked from local
  full text
- Sections intentionally skipped or compressed: detailed appendix tables and
  examples

## 16. Source Reliability

NeurIPS 2024 paper with public code and arXiv version. Strong source for
agent-computer interface design and software-engineering agent evaluation. Do
not use it alone as evidence for safe unattended OS mutation.
