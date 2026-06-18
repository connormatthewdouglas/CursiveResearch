# LADDER Claims and Results Summary

**Paper**: LADDER: Self-Improving LLMs Through Recursive Problem Decomposition (Simonds & Yoshiyama, 2025)

## Core Claims

1. LLMs can autonomously generate their own training curriculum by recursively creating easier variants of hard problems.
2. With only a deterministic verifier (numerical integration), this self-generated curriculum + GRPO RL produces large capability improvements on hard math tasks.
3. The same mechanism can be applied at test time (TTRL) for additional gains without permanent model updates.
4. These gains are achieved without human feedback, curated datasets, or architectural scaling.

## Key Quantitative Results

| Setting | Model | Baseline | LADDER Result | LADDER + TTRL | Notes |
| --- | --- | --- | --- | --- | --- |
| Undergraduate integration problems | Llama 3.2 3B | ~1-2% | 82% | - | Dramatic lift on previously near-impossible tasks |
| 2025 MIT Integration Bee qualifying exam | Qwen2.5 7B (Deepseek-R1 Distilled) | GPT-4o ~42%, human 15-30% | 73% | 90% | Beats GPT-4o; approaches/surpasses o1 with TTRL |

## Why These Results Matter for CursiveOS

- Demonstrates that **verifier-grounded recursive loops** can produce real, measurable self-improvement.
- Shows the power of **autonomous difficulty gradients** (curriculum without human design).
- TTRL provides a pattern for safe **test-time / runtime adaptation**.
- Reinforces that the quality of the verifier is the limiting factor for safe self-improvement.

**Source**: arXiv 2503.00735v3, CC BY 4.0.
