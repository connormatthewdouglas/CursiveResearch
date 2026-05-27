# Peer-Reviewed / Published Research Sources: Recursive Self-Improvement

Date extracted: 2026-05-27  
Scope: foundational papers and systems for recursive self-improvement, self-improving agents, evolutionary coding agents, verifier-guided discovery, and agent evaluation.

## Purpose

This file records the first source set for the recursive self-improvement research intake. It does not mirror paper contents. It preserves links and source-level notes so the corpus can maintain structured summaries without copying full papers.

## Source Set

| ID | Source | Link | Type | Why It Matters |
| --- | --- | --- | --- | --- |
| RSI-001 | AlphaEvolve: A coding agent for scientific and algorithmic discovery | https://arxiv.org/abs/2506.13131 | arXiv white paper / Google DeepMind system | Evolutionary coding agent using LLM-generated code changes and automated evaluators; directly relevant to mutation-selection loops. |
| RSI-002 | Mathematical discoveries from program search with large language models / FunSearch | https://www.nature.com/articles/s41586-023-06924-6 | Nature paper / Google DeepMind system | LLM proposes programs; evaluator selects useful candidates; clear precedent for evaluator-grounded discovery. |
| RSI-003 | Self-Taught Optimizer (STOP): Recursively Self-Improving Code Generation | https://arxiv.org/abs/2310.02304 | arXiv paper | Directly studies a scaffold that improves itself using a fixed LLM; important for bounded RSI and sandbox concerns. |
| RSI-004 | AI Agents That Matter | https://arxiv.org/abs/2407.01502 | arXiv paper | Guardrail paper for agent evaluation quality, cost, overfitting, benchmark validity, and fake progress. |
| RSI-005 | Voyager: An Open-Ended Embodied Agent with Large Language Models | https://arxiv.org/abs/2305.16291 | arXiv paper / open-source agent | Shows skill-library accumulation, automatic curriculum, environment feedback, and executable memory. |
| RSI-006 | Reflexion: Language Agents with Verbal Reinforcement Learning | https://arxiv.org/abs/2303.11366 | arXiv paper | Demonstrates verbal feedback and episodic memory as a lightweight improvement loop without model updates. |
| RSI-007 | Language Agents as Optimizable Graphs / GPTSwarm | https://arxiv.org/abs/2402.16823 | arXiv paper / framework | Treats agent scaffolds as mutable computational graphs; relevant to optimizing agent architecture itself. |
| RSI-008 | Self-Taught Evaluators | https://arxiv.org/abs/2408.02666 | arXiv paper / Meta AI research | Studies evaluator improvement from synthetic data; useful but risky precedent for self-evaluation. |
| RSI-009 | Faster sorting algorithms discovered using deep reinforcement learning / AlphaDev | https://www.nature.com/articles/s41586-023-06004-9 | Nature paper / Google DeepMind system | AI-discovered low-level algorithms adopted into real software libraries; strong real-world optimization precedent. |
| RSI-010 | Discovering faster matrix multiplication algorithms with reinforcement learning / AlphaTensor | https://www.nature.com/articles/s41586-022-05172-4 | Nature paper / Google DeepMind system | Algorithm discovery as search over computational procedures; includes hardware-specific optimization lessons. |
| RSI-011 | Self-Rewarding Language Models | https://arxiv.org/abs/2401.10020 | arXiv paper / Meta AI research | Important for understanding self-judgment, evaluator drift, and the risks of model-generated reward. |
| RSI-012 | Agent-as-a-Judge: Evaluate Agents with Agents | https://arxiv.org/abs/2410.10934 | arXiv paper | Agentic evaluation of agentic systems; relevant to scalable feedback but should not replace deterministic sensors. |

## Intake Notes

- Google DeepMind's AlphaEvolve, FunSearch, AlphaDev, and AlphaTensor form the strongest evaluator-grounded discovery cluster.
- STOP, GPTSwarm, Voyager, Reflexion, Self-Taught Evaluators, and Self-Rewarding Language Models form the strongest self-improving-agent cluster.
- `AI Agents That Matter` should be treated as a methodology guardrail for all agent claims.
- The corpus should distinguish self-improvement of code, scaffolds, skills, evaluators, and memory from self-improvement of model weights.
- The central recurring lesson is that improvement requires a trusted feedback signal. LLM self-judgment is useful but weaker than deterministic tests, environment feedback, or independently validated sensors.
