# Reflexion: Language Agents with Verbal Reinforcement Learning

> Converted for agent readability from the ar5iv HTML rendering of arXiv:2303.11366.  
> Source: https://ar5iv.labs.arxiv.org/html/2303.11366  
> arXiv: https://arxiv.org/abs/2303.11366  
> PDF: https://arxiv.org/pdf/2303.11366  
> Code: https://github.com/noahshinn024/reflexion  
> License noted in the paper folder README: CC BY 4.0.  
>
> Conversion note: this Markdown version is intended for agent readability. Some formulas, figure images, and table formatting from the PDF/ar5iv source may be simplified or degraded. Figure captions and reported results are preserved in text where available.

## Authors

Noah Shinn — Northeastern University — noahshinn024@gmail.com  
Federico Cassano — Northeastern University — cassano.f@northeastern.edu  
Edward Berman — Northeastern University — berman.ed@northeastern.edu  
Ashwin Gopinath — Massachusetts Institute of Technology — agopi@mit.edu  
Karthik Narasimhan — Princeton University — karthikn@princeton.edu  
Shunyu Yao — Princeton University — shunyuy@princeton.edu

## Abstract

Large language models (LLMs) have been increasingly used to interact with external environments such as games, compilers, and APIs as goal-driven agents. However, it remains challenging for these language agents to quickly and efficiently learn from trial-and-error, because traditional reinforcement learning methods require extensive training samples and expensive model fine-tuning.

The authors propose **Reflexion**, a framework for reinforcing language agents not by updating weights, but through linguistic feedback. Reflexion agents verbally reflect on task feedback signals, then maintain reflective text in an episodic memory buffer to improve decision-making in subsequent trials. Reflexion can incorporate different feedback signal types, including scalar values and free-form language, and different feedback sources, including external and internally simulated feedback.

The paper reports significant improvements over baseline agents across sequential decision-making, coding, and language reasoning tasks. For example, Reflexion reports 91% pass@1 accuracy on the HumanEval coding benchmark, compared with a previous GPT-4 result of 80%. The authors also conduct ablation and analysis studies using different feedback signals, feedback incorporation methods, and agent types.

## 1. Introduction

Recent works such as ReAct, SayCan, Toolformer, HuggingGPT, generative agents, and WebGPT demonstrate that autonomous decision-making agents can be built around a large language model core. These systems use LLMs to generate text and actions that can be used in API calls and executed in an environment.

Because these systems rely on large models with many parameters, they are often limited to teaching agents through in-context examples. More traditional optimization methods such as reinforcement learning with gradient descent require substantial compute and time.

Reflexion proposes an alternative: verbal reinforcement that helps agents learn from prior failings. Reflexion converts binary or scalar feedback from an environment into verbal feedback in the form of a textual summary. That summary is then added to the LLM agent's context in the next episode.

This self-reflective feedback acts as a semantic gradient signal. It provides a concrete direction for improvement, helping an agent learn from mistakes and perform better in the next attempt. The authors compare this to how humans learn complex tasks in a few-shot manner by reflecting on failures and forming improved plans.

Generating useful reflective feedback is difficult. It requires understanding where the model made mistakes, the credit assignment problem, and generating a summary with actionable insights. The paper explores three ways of producing reflection:

1. simple binary environment feedback;
2. predefined heuristics for common failure cases;
3. self-evaluation using LLMs or self-written unit tests.

In all implementations, the evaluation signal is amplified into natural-language experience summaries, which are stored in long-term memory.

Reflexion has several advantages over traditional reinforcement learning:

- it is lightweight and does not require fine-tuning the LLM;
- it supports more nuanced feedback than scalar or vector rewards;
- it provides interpretable episodic memory over prior experiences;
- it gives explicit hints for future actions.

Its disadvantages include reliance on LLM self-evaluation capability or heuristics and the absence of formal success guarantees.

The paper evaluates Reflexion on:

1. decision-making tasks requiring sequential action choices over long trajectories;
2. reasoning tasks requiring knowledge-intensive, single-step generation improvement;
3. programming tasks requiring external tools such as compilers and interpreters.

Reported improvements include:

- 22 percentage-point improvement on ALFWorld decision-making tasks over strong baselines in 12 iterative learning steps;
- 20 percentage-point improvement on HotPotQA reasoning questions;
- up to 11 percentage-point improvement on HumanEval Python programming tasks.

The paper states these contributions:

- Reflexion introduces a new paradigm for verbal reinforcement that parameterizes a policy as an agent memory encoding paired with fixed LLM parameters.
- It explores self-reflection as an emergent property of LLMs and empirically shows it can help agents learn complex tasks over a small number of trials.
- It introduces LeetcodeHardGym, a code-generation reinforcement learning gym environment with 40 hard-level Leetcode questions in 19 programming languages.
- It reports improvements over strong baselines across several tasks and state-of-the-art results on several code-generation benchmarks.

Figure 1 shows Reflexion working across decision-making, programming, and reasoning tasks.

## 2. Related Work

### Reasoning and Decision-Making

Self-Refine uses an iterative framework for self-refinement to improve generated outputs through self-evaluation. These self-evaluation and self-improvement steps are conditioned on task constraints, such as asking how a generation can be rewritten more positively. Self-Refine is effective but limited to single-generation reasoning tasks.

Other work performs semantic prompt-writing optimization or fine-tunes critic models to provide intermediate feedback over reasoning trajectories. Some approaches use stochastic beam search over actions to improve decision-making through self-evaluation. Others use decider models to reason over several generations or retry patterns without explicit evaluation.

The paper argues Reflexion differs by building persistent memory of self-reflective experiences, allowing agents to identify errors and suggest lessons over time.

### Programming

Several programming systems use test-driven development or code debugging techniques. AlphaCode evaluates generations on hidden test cases. CodeT generates tests to score generated implementations. Self-Debugging improves implementations using feedback from a code execution environment. CodeRL frames code generation as reinforcement learning with an actor-critic setup.

AlphaCode, Self-Debugging, and CodeRL can fix simpler bugs, but they rely on ground-truth test cases that invalidate pass@1 eligibility and do not use self-reflection to bridge error identification and implementation improvement. CodeT does not access hidden test cases, but it also does not implement a self-learning step to improve code writing.

The paper's related-work comparisons emphasize that Reflexion combines:

- self-refinement;
- hidden decision-making;
- binary rewards;
- memory;
- test execution;
- debugging execution;
- self-generated tests;
- multiple languages;
- self-reflection.

## 3. Reflexion: Reinforcement via Verbal Reflection

Figure 2 contains a diagram of Reflexion and an algorithm for reinforcement via self-reflection.

At a high level:

```text
initialize Actor, Evaluator, Self-Reflection model
initialize policy

generate initial trajectory using Actor
evaluate trajectory using Evaluator
generate self-reflection using Self-Reflection model
store self-reflection in memory

while not solved and max trials not reached:
    generate new trajectory using Actor conditioned on memory
    evaluate trajectory
    generate self-reflection
    append reflection to memory
    increment trial

return final result
```

The Reflexion framework uses three model roles:

- **Actor**: generates text and actions;
- **Evaluator**: scores the Actor's outputs;
- **Self-Reflection model**: generates verbal reinforcement cues to help the Actor improve.

### Actor

The Actor is built on an LLM prompted to generate text and actions conditioned on state observations. It samples an action or generation from the current policy, receives an environment observation, and continues the trajectory.

The authors explore Actor models including Chain-of-Thought and ReAct. The Actor also receives memory as additional context, inspired by in-context policy iteration.

### Evaluator

The Evaluator assesses generated outputs from the Actor. It takes a trajectory and computes a reward score. The paper investigates several evaluator variants because semantic reward functions are difficult to define.

For reasoning tasks, the paper uses exact-match grading against expected answers. For decision-making tasks, it uses predefined heuristic functions tailored to the evaluation criteria. It also experiments with using another LLM instantiation as an Evaluator for decision-making and programming tasks.

### Self-Reflection

The Self-Reflection model is instantiated as an LLM. It generates verbal feedback for future trials. Given a sparse reward signal, current trajectory, and persistent memory, it generates more nuanced feedback than the scalar or binary reward itself.

In a multi-step decision-making task, for example, a failure signal may allow the agent to infer that a specific action caused later incorrect actions. The Self-Reflection model can then state which alternative action should have been taken and store that experience.

### Memory

Reflexion uses both short-term and long-term memory.

- Short-term memory: trajectory history from the current trial.
- Long-term memory: outputs from the Self-Reflection model.

At inference time, the Actor conditions decisions on both. Long-term memory stores distilled lessons learned over several trials.

The paper notes that memory is bounded in practice by context window limits. The authors usually store 1–3 reflections.

### The Reflexion Process

In the first trial, the Actor interacts with the environment and produces a trajectory. The Evaluator produces a task-specific reward. The Self-Reflection model converts that sparse reward into verbal experience feedback, which is appended to memory.

In later trials, the Actor uses the memory to adjust behavior. The Actor, Evaluator, and Self-Reflection model repeat until the Evaluator judges the trajectory successful or a trial limit is reached.

## 4. Experiments

The paper evaluates Reflexion on natural-language reinforcement learning setups across decision-making, reasoning, and code generation:

- ALFWorld for multi-step household decision-making tasks;
- HotPotQA for search-based question answering and reasoning;
- HumanEval, MBPP, and LeetcodeHard for code writing with compilers/interpreters.

The paper reports headline improvements of:

- 22 percentage points in ALFWorld;
- 20 percentage points in HotPotQA;
- 11 percentage points on HumanEval.

### 4.1 Sequential Decision-Making: ALFWorld

ALFWorld is a suite of text-based environments for solving multi-step tasks in interactive household environments. The authors run the agent in 134 ALFWorld environments across six task types, including finding hidden objects, moving objects, and manipulating objects with other objects.

The paper uses ReAct as the action generator because prior work showed ReAct can help long-trajectory decision-making with explicit intermediate thoughts.

ALFWorld tasks require self-evaluation because the environment only signals when a task is complete. The authors implement two self-evaluation techniques:

1. natural-language classification with an LLM;
2. a hand-written heuristic.

The heuristic triggers reflection if:

- the agent executes the same action and receives the same response more than three cycles; or
- the action count exceeds 30, indicating inefficient planning.

In baseline runs, when self-reflection is suggested, the system skips the reflection process, resets the environment, and starts a new trial. In Reflexion runs, the agent uses reflection to identify its mistake, update memory, reset the environment, and retry.

To avoid long prompts, memory is truncated to the last three reflections. To avoid syntactic errors, the authors provide two domain-specific few-shot trajectories, matching prior ReAct prompts.

#### Results

Figure 3 reports ALFWorld performance across 134 tasks and failure-type classifications.

The paper reports that ReAct + Reflexion completes 130 out of 134 tasks using the simple heuristic to detect hallucinations and inefficient planning. ReAct + Reflexion continues learning over 12 consecutive trials. In the ReAct-only approach, performance increase stalls between trials 6 and 7.

#### Analysis

A common baseline failure occurs when the agent believes it has possession of an item when it does not. It then executes a long trajectory and cannot backtrack to the source of the mistake.

Reflexion reduces this failure mode by distilling long failed trajectories into relevant experiences used as future self-hints.

Long-term memory helps in two main cases:

1. when an early mistake in a long trajectory can be identified and corrected;
2. when too many surfaces or containers must be searched and the agent can use memory across trials to search more thoroughly.

The authors report a sharp improvement after the first two trials and then steady improvement over the next 11 trials to near-perfect performance. ReAct-only converges at a hallucination rate of about 22% with no sign of long-term recovery.

### 4.2 Reasoning: HotPotQA

HotPotQA is a Wikipedia-based dataset with 113,000 question-answer pairs requiring reasoning over supporting documents.

The paper tests:

- Reflexion + Chain-of-Thought for reasoning-only behavior;
- Chain-of-Thought with ground-truth context, to isolate reasoning over provided text;
- Reflexion + ReAct for retrieval plus reasoning, using a Wikipedia API.

Prompting setup:

- CoT uses six-shot prompting;
- ReAct uses two-shot prompting;
- self-reflection uses two-shot prompting.

Between trials, exact-match answer grading provides a binary success signal. The reflection loop amplifies that binary signal into natural language feedback. Memory size is again limited to three experiences.

#### Results

Figure 4 reports Reflexion performance with Chain-of-Thought and ReAct on 100 HotPotQA questions.

The paper reports that Reflexion outperforms all baseline approaches over several learning steps. ReAct-only, CoT-only, and CoT with ground-truth context do not probabilistically improve on failed tasks in later trials at temperature 0.7. Reflexion allows the agent to gather experience and retry failed tasks until producing three consecutive failed attempts.

The paper reports that CoT with ground-truth context has higher accuracy because it receives context. Even then, CoT with ground-truth context fails on 39% of questions; Reflexion improves accuracy by 14 percentage points without access to the ground-truth answer.

#### Analysis

The authors perform an ablation to isolate the advantage of self-reflection. They compare CoT with ground-truth context, episodic memory containing the most recent trajectory, and Reflexion with a final self-reflection pass.

The paper reports that self-reflection improves learning by an 8 percentage-point absolute boost over episodic memory alone. This supports the authors' argument that refinement-only approaches are less effective than self-reflection-guided refinement.

### 4.3 Programming

The paper evaluates Reflexion on Python and Rust code-writing tasks using MBPP, HumanEval, and LeetcodeHardGym.

MBPP and HumanEval measure function-body generation accuracy from natural-language descriptions. The paper uses MultiPL-E to translate subsets of HumanEval and MBPP into Rust. The Rust experiments are meant to show that Reflexion can operate with interpreted and compiled languages.

The paper introduces **LeetcodeHardGym**, an interactive programming environment with 40 hard-rated Leetcode questions released after October 8, 2022, the stated pretraining cutoff date of GPT-4.

Programming is a strong Reflexion target because it can use grounded self-evaluation through self-generated unit tests and execution feedback.

The programming implementation:

1. uses Chain-of-Thought prompting to generate diverse unit tests with natural-language descriptions;
2. filters syntactically valid test statements by checking AST construction;
3. samples up to six unit tests for the test suite;
4. uses the same reflection loop as reasoning and decision-making, with memory limited to one experience.

#### Reported Results: Table 1

| Benchmark + Language | Previous SOTA Pass@1 | SOTA Pass@1 | Reflexion Pass@1 |
| --- | ---: | ---: | ---: |
| HumanEval (Python) | 65.8, CodeT + GPT-3.5 | 80.1, GPT-4 | 91.0 |
| HumanEval (Rust) | — | 60.0, GPT-4 | 68.0 |
| MBPP (Python) | 67.7, CodeT + Codex | 80.1, GPT-4 | 77.1 |
| MBPP (Rust) | — | 70.9, GPT-4 | 75.4 |
| Leetcode Hard (Python) | — | 7.5, GPT-4 | 15.0 |

The paper states that all instruction-based models use zero-shot code generation as the base strategy.

#### Reported Results: Table 2

| Benchmark + Language | Base | Reflexion | TP | FN | FP | TN |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| HumanEval (Python) | 0.80 | 0.91 | 0.99 | 0.40 | 0.01 | 0.60 |
| MBPP (Python) | 0.80 | 0.77 | 0.84 | 0.59 | 0.16 | 0.41 |
| HumanEval (Rust) | 0.60 | 0.68 | 0.87 | 0.37 | 0.13 | 0.63 |
| MBPP (Rust) | 0.71 | 0.75 | 0.84 | 0.51 | 0.16 | 0.49 |

Table 2 reports overall accuracy and test-generation performance for HumanEval and MBPP. For Rust, HumanEval uses the 50 hardest HumanEval Python problems translated to Rust with MultiPL-E.

The labels mean:

- TP: unit tests pass and solution passes;
- FN: unit tests fail but solution passes;
- FP: unit tests pass but solution fails;
- TN: unit tests fail and solution fails.

The paper reports that Reflexion outperforms baselines and sets new state-of-the-art on all listed benchmarks except MBPP Python.

#### Programming Analysis

Self-reflecting code agents depend on their ability to write diverse and comprehensive tests. Flaky or weak test suites can produce false positives, where all internal tests pass but the actual solution is incorrect. Incorrectly written tests can also produce false negatives, where tests fail on a correct solution.

The paper argues false negatives are preferred over false positives in Reflexion. If tests falsely fail a correct solution, the agent may identify the bad test and keep the original implementation. If tests falsely pass an incorrect solution, the agent prematurely reports an invalid submission.

The paper identifies a large false-positive difference between HumanEval Python and MBPP Python. It reports a false-positive test execution rate of 16.3% for MBPP Python and 1.4% for HumanEval Python, explaining why Reflexion achieves 91% overall accuracy on HumanEval Python but underperforms on MBPP Python.

#### Ablation Study

Table 3 reports an ablation on the 50 hardest HumanEval Rust problems using GPT-4:

| Approach | Test Generation | Self-Reflection | Pass@1 Accuracy |
| --- | --- | --- | ---: |
| Base model | False | False | 0.60 |
| Test generation omission | False | True | 0.52 |
| Self-reflection omission | True | False | 0.60 |
| Reflexion | True | True | 0.68 |

The paper interprets this as showing that test generation and self-reflection must cooperate. Without unit tests, self-reflection alone performs worse than the baseline because the agent cannot determine whether its implementation is correct. Without self-reflection, test execution catches syntax and logic errors, but the agent fails to translate those indications into effective implementation fixes.

## 5. Limitations

Reflexion is an optimization technique that uses natural language for policy optimization. It can improve action choices through experience, but it can still fall into non-optimal local minima.

The paper limits long-term memory to a sliding window with maximum capacity, but suggests future work could use more advanced memory structures such as vector embedding databases or SQL databases.

For code generation, the paper notes limitations in test-driven development. Accurate input-output mapping is difficult for:

- nondeterministic generator functions;
- impure functions that interact with APIs;
- functions whose outputs vary by hardware specification;
- parallel or concurrent functions that are difficult to predict.

## 6. Broader Impact

LLMs are increasingly used to interact with external environments, including the Internet, software, robotics, and humans. Reflexion can reinforce and empower agents toward greater automation and efficiency, but can also amplify risk when agents are misused.

The paper argues this research direction needs further safety and ethical work.

It also notes that reinforcement learning often suffers from black-box policy and optimization setups that make interpretability and alignment difficult. Verbal reinforcement may help make autonomous agents more interpretable and diagnosable. For example, in tool-use contexts that are hard for humans to understand, reflections could be monitored to check intent before tool use.

## 7. Conclusion

The paper presents Reflexion as an approach that uses verbal reinforcement to teach agents to learn from mistakes. The authors empirically report that Reflexion agents outperform widely used decision-making approaches by using self-reflection.

The paper suggests future work could combine Reflexion with more advanced reinforcement learning techniques, including value learning in natural language or off-policy exploration.

## 8. Reproducibility

The paper strongly advises using isolated execution environments when running autonomous code-writing experiments, because generated code is not validated before execution.

## References

The ar5iv conversion lists references including:

- Ahn et al. (2022), SayCan / grounding language in robotic affordances.
- Austin et al. (2021), program synthesis with large language models.
- Brooks et al. (2022), in-context policy iteration.
- Cassano et al. (2022), MultiPL-E.
- Chen et al. (2022), CodeT.
- Chen et al. (2021), evaluating large language models trained on code.
- Chen et al. (2023), self-debugging.
- Côté et al. (2019), TextWorld.
- Goodman (2023), Meta-prompt.
- Kim et al. (2023), language models solving computer tasks.
- Lam et al. (2020), flaky tests.
- Le et al. (2022), CodeRL.
- Li et al. (2023), StarCoder.
- OpenAI (2023), GPT-4 technical report.
- Park et al. (2023), generative agents.
- Paul et al. (2023), Refiner.
- Pryzant et al. (2023), automatic prompt optimization with gradient descent and beam search.
- Schick et al. (2023), Toolformer.
- Shen et al. (2023), HuggingGPT.
- Shridhar et al. (2021), ALFWorld.
- Sutton and Barto (2018), Reinforcement Learning: An Introduction.
- Wei et al. (2022), Chain-of-Thought prompting.
- Xie et al. (2023), self-evaluation guided decoding.
- Yang et al. (2018), HotpotQA.
- Yao et al. (preprint), WebShop.
- Yao et al. (2023), ReAct.
- Yoran et al. (2023), meta-reasoning over multiple chains of thought.

## Appendix A: Evaluation with Additional Models

The paper further investigates trial-and-error problem-solving with models of different strengths. It reports that the ability to specify self-corrections is an emergent quality of stronger, larger models.

### Table 4: HumanEval Python with starchat-beta

| Approach | Pass@1 Accuracy, Avg over 8 trials | Std |
| --- | ---: | ---: |
| Baseline | 0.26 | 0.00481 |
| Reflexion | 0.26 | 0.00305 |

### Table 5: HotPotQA with Various Models

| Model | Baseline Accuracy | Reflexion Accuracy |
| --- | ---: | ---: |
| CoT (GT) + text-davinci-003 | 0.60 | 0.77 |
| CoT (GT) + gpt-3.5-turbo | 0.57 | 0.71 |
| CoT (GT) + gpt-4 | 0.68 | 0.80 |
| ReAct + text-davinci-003 | 0.30 | 0.55 |
| ReAct + gpt-3.5-turbo | 0.26 | 0.38 |
| ReAct + gpt-4 | 0.39 | 0.51 |

## Appendix B: Decision-Making

The appendix includes an ALFWorld example where the task is to examine a mug with a desklamp.

In Trial 1, the agent searches drawers and desks, finds a mug, later finds a desklamp, but repeats `use desklamp 1` and fails.

The reflection states that the agent should have looked for the desklamp first, then found the mug. It remembers the desklamp was on desk 1 and plans to go there first next time.

In Trial 2, the agent goes to desk 1, sees the desklamp and mug, takes the mug, uses the desklamp, and succeeds.

Figure 5 shows this failure and correction: the agent failed due to inefficient planning, reflected on the mistake, and corrected its sequence in the next trial.

### B.1 WebShop Limitation

The paper briefly reports a limitation on WebShop. WebShop is a web-based benchmark where agents navigate an e-commerce website to find and purchase products based on user requests.

The authors test a two-shot ReAct + Reflexion agent in 100 environments. After four trials, they terminate the runs because the agent does not show improvement and does not generate helpful self-reflections after failure.

They conclude Reflexion struggles on tasks requiring significant diversity and exploration. In ALFWorld, permissible actions are visible in observations, making exploration easier. In HotPotQA, the Wikipedia search space is more diverse and requires less precise search queries than e-commerce. WebShop requires more diverse and unique behavior from the agent.

Figure 6 shows Reflexion vs ReAct on WebShop and reports that ReAct + Reflexion fails to significantly outperform ReAct.

## Appendix C: Programming

Programming LLM calls require strict instructions to produce function bodies only because of dialogue training.

### C.1 HumanEval Python Function Example

Sample function signature:

```python
def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any
    non-empty sub-array of nums.

    Example:
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
```

Sample function body:

```python
    min_sum = float('inf')
    for i in range(len(nums)):
        current_sum = 0
        for j in range(i, len(nums)):
            current_sum += nums[j]
            if current_sum < min_sum:
                min_sum = current_sum
    return min_sum
```

### C.2 Reflexion Actor Instruction

The paper includes an actor instruction for programming tasks. It tells the model it is a Python writing assistant and will receive:

- previous implementation;
- unit test results;
- self-reflection on the previous implementation.

The model is instructed to respond only with the improved function body, not the signature, and to start with four spaces of indentation.

The Reflexion Actor generations follow this form:

```text
Instruction
Function implementation
Unit test feedback
Self-reflection
Instruction for next function implementation
```

### C.3 Reflexion Self-Reflection Instruction and Example

The self-reflection prompt has a similar programming-assistant framing. It receives the previous implementation, unit test results, and prior self-reflection, then generates feedback for the next attempt.

The self-reflection generation form includes:

```text
Instruction
Function implementation
Unit test feedback
```

### C.4 No Self-Reflection Ablation

The no-self-reflection ablation preserves the actor-generation structure but omits the useful reflection content.

### C.5 No Test Generation Ablation

The no-test-generation ablation preserves the actor-generation structure but lacks generated unit test feedback.

## Appendix D: Reasoning

### D.1 HotPotQA Full Example

The appendix includes a HotPotQA example involving the film *Grown-Ups* and the TV series *'Allo 'Allo!*.

In Trial 1, the agent searches for *Grown-Ups*, then searches for *'Allo 'Allo!*, fails to find the right page directly, searches for Gorden Kaye, and answers René Artois. The answer is incorrect.

In Trial 2, the agent searches *Grown-Ups*, realizes the film stars Sam Kelly, searches Sam Kelly, and answers Captain Hans Geering. The answer is correct.

The reflection says the agent searched the wrong title for the show and should have searched the actor's name.

Figure 7 shows two HotPotQA trials in the same task. Reflexion + ReAct uses self-reflection to determine a better search strategy for the next trial.

### D.2 Chain-of-Thought + Reflexion

Example question: What profession do John Lanchester and Alan Dean Foster have in common?

Trial 1 answers “novelist and screenwriter” and is incorrect. Trial 2 answers “novelist” and is correct. The reflection notes that the agent incorrectly assumed both people had the same set of professions and should research both backgrounds more carefully.

### D.3 HotPotQA Chain-of-Thought with Ground Truth Context + Reflexion

The appendix includes a question about the Battle of White Plains and the New York and New Jersey campaign.

Trial 1 answers Battle of White Plains and is incorrect. Trial 2 answers the New York and New Jersey campaign and is correct. The reflection states that the question asked for a series of battles, not a single battle.

### D.4 HotPotQA Episodic Memory Ablation Prompts

The appendix includes episodic-memory ablation examples.

One example asks which of Jonny Craig and Pete Doherty has been a member of more bands. The first trial answers Pete Doherty and is incorrect. The second trial answers Jonny Craig and is correct. The reflection notes that the agent failed to account for past and current band memberships.

Another example asks what field a degree abbreviated MS, M.S., or ScM belongs to. The first trial answers a broad category, “Sciences, Engineering, and Medicine,” and is incorrect. The second trial correctly answers Engineering. The reflection notes that the agent misunderstood the question as asking for a category of degrees rather than the field of study.

## Agent-Readability Notes

This file is intended to make the paper readable without requiring PDF tooling. Agents should still consult the original PDF or ar5iv HTML if exact wording, omitted mathematical notation, figure images, or full appendix examples are needed.
