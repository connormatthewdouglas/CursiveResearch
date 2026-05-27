# Peer-Reviewed / Published Research Sources: Recursive Self-Improvement

Date extracted: 2026-05-27  
Scope: foundational papers and systems for recursive self-improvement, self-improving agents, evolutionary coding agents, verifier-guided discovery, open-ended evolution, and agent evaluation.

## Purpose

This file records the current source set for the recursive self-improvement research intake. It does not mirror paper contents. It preserves links and source-level notes so the corpus can maintain structured summaries without copying full papers.

## Source Set

| ID | Source | Link | Type | Why It Matters | Current Confidence |
| --- | --- | --- | --- | --- | --- |
| RSI-001 | AlphaEvolve: A coding agent for scientific and algorithmic discovery | https://arxiv.org/abs/2506.13131 | arXiv white paper / Google DeepMind system | Evolutionary coding agent using LLM-generated code changes and automated evaluators; directly relevant to mutation-selection loops. | High as research lead; individual performance claims need source-level validation. |
| RSI-002 | Mathematical discoveries from program search with large language models / FunSearch | https://www.nature.com/articles/s41586-023-06924-6 | Nature paper / Google DeepMind system | LLM proposes programs; evaluator selects useful candidates; clear precedent for evaluator-grounded discovery. | High. |
| RSI-003 | Self-Taught Optimizer (STOP): Recursively Self-Improving Code Generation | https://arxiv.org/abs/2310.02304 | arXiv / OpenReview / codebase | Directly studies a scaffold that improves itself using a fixed LLM; important for bounded RSI and sandbox concerns. | High. |
| RSI-004 | AI Agents That Matter | https://arxiv.org/abs/2407.01502 | arXiv paper | Guardrail paper for agent evaluation quality, cost, overfitting, benchmark validity, and fake progress. | High. |
| RSI-005 | Voyager: An Open-Ended Embodied Agent with Large Language Models | https://arxiv.org/abs/2305.16291 | arXiv paper / open-source agent | Shows skill-library accumulation, automatic curriculum, environment feedback, and executable memory. | High. |
| RSI-006 | Reflexion: Language Agents with Verbal Reinforcement Learning | https://arxiv.org/abs/2303.11366 | arXiv paper | Demonstrates verbal feedback and episodic memory as a lightweight improvement loop without model updates. | High as pattern; limited as final verifier. |
| RSI-007 | Language Agents as Optimizable Graphs / GPTSwarm | https://arxiv.org/abs/2402.16823 | arXiv paper / framework | Treats agent scaffolds as mutable computational graphs; relevant to optimizing agent architecture itself. | Medium-high. |
| RSI-008 | Self-Taught Evaluators | https://arxiv.org/abs/2408.02666 | arXiv paper / Meta AI research | Studies evaluator improvement from synthetic data; useful but risky precedent for self-evaluation. | Medium-high; requires skepticism. |
| RSI-009 | Faster sorting algorithms discovered using deep reinforcement learning / AlphaDev | https://www.nature.com/articles/s41586-023-06004-9 | Nature paper / Google DeepMind system | AI-discovered low-level algorithms adopted into real software libraries; strong real-world optimization precedent. | High. |
| RSI-010 | Discovering faster matrix multiplication algorithms with reinforcement learning / AlphaTensor | https://www.nature.com/articles/s41586-022-05172-4 | Nature paper / Google DeepMind system | Algorithm discovery as search over computational procedures; includes hardware-specific optimization lessons. | High. |
| RSI-011 | Self-Rewarding Language Models | https://arxiv.org/abs/2401.10020 | arXiv / ICML 2024 paper / Meta AI research | Important for understanding self-judgment, evaluator drift, and the risks of model-generated reward. | Medium-high; risk literature as much as capability literature. |
| RSI-012 | Agent-as-a-Judge: Evaluate Agents with Agents | https://arxiv.org/abs/2410.10934 | arXiv paper | Agentic evaluation of agentic systems; relevant to scalable feedback but should not replace deterministic sensors. | Medium. |
| RSI-013 | Gödel Agent: A Self-Referential Framework for Agents Recursively Self-Improvement | https://arxiv.org/abs/2410.04444 | arXiv / conference-style preprint | Runtime self-modification via memory inspection and monkey patching; useful for understanding risk of in-situ self-modification. | Medium-high as research lead; safety claims require careful review. |
| RSI-014 | Polaris: A Gödel Agent Framework for Small Language Models through Experience-Abstracted Policy Repair | https://arxiv.org/abs/2603.23129 | arXiv preprint | Attempts bounded self-modification for small models via compact validated code patches and error abstraction. | Medium-high as research lead. |
| RSI-015 | Evolving Programmatic Skill Networks | https://arxiv.org/abs/2601.03509 | arXiv preprint | Extends skill libraries into compositional program graphs with reflection, maturity gating, and rollback-like validation. | Medium-high. |
| RSI-016 | Darwin Gödel Machine: Open-Ended Evolution of Self-Improving Agents | https://arxiv.org/abs/2505.22954 | arXiv preprint | Open-ended self-improving agents; relevant to organism/evolution framing. | Medium; needs direct review. |
| RSI-017 | CodeEvolve: an open-source evolutionary framework for algorithmic discovery and optimization | https://arxiv.org/abs/2510.14150 | arXiv preprint / open-source framework | Open-source AlphaEvolve-style system; useful if the corpus wants runnable reference architecture. | Medium; newer and needs review. |
| RSI-018 | Process-Based Self-Rewarding Language Models | https://arxiv.org/abs/2503.03746 | arXiv preprint | Step-wise/process reward version of self-rewarding loop, especially for reasoning. | Medium; risk of evaluator drift remains. |
| RSI-019 | Noise-to-Meaning Recursive Self-Improvement | https://arxiv.org/abs/2505.02888 | arXiv preprint | Mathematical framing of recursive feedback and complexity growth. | Medium; theoretical. |
| RSI-020 | Safety Must Precede the Deployment of Open-Ended AI | https://arxiv.org/abs/2502.04512 | arXiv preprint | Safety framing for open-ended systems and autonomous discovery. | Medium-high as safety context. |
| RSI-021 | TerraLingua: Emergence and Analysis of Open-endedness in LLM Ecologies | https://arxiv.org/abs/2603.16910 | arXiv preprint | Open-endedness in LLM ecologies; useful for organism/evolution framing. | Medium; needs review. |
| RSI-022 | Evolutionary Computation and Large Language Models: A Survey of Methods, Synergies, and Applications | https://arxiv.org/abs/2505.15741 | arXiv survey | Survey connecting evolutionary computation and LLMs. | Medium-high; useful orientation. |

## Intake Notes

- Google DeepMind's AlphaEvolve, FunSearch, AlphaDev, and AlphaTensor form the strongest evaluator-grounded discovery cluster.
- STOP, GPTSwarm, Voyager, Reflexion, Gödel Agent, Polaris, PSN, Self-Taught Evaluators, and Self-Rewarding Language Models form the strongest self-improving-agent cluster.
- `AI Agents That Matter` should be treated as a methodology guardrail for all agent claims.
- The corpus should distinguish self-improvement of code, scaffolds, skills, evaluators, policies, memory, and model weights.
- The central recurring lesson is that improvement requires a trusted feedback signal. LLM self-judgment is useful but weaker than deterministic tests, environment feedback, or independently validated sensors.
- Sources marked as preprints, secondary sources, or newer systems should be treated as research leads until source-level validation is complete.
