# LADDER: Self-Improving LLMs Through Recursive Problem Decomposition

**Authors**: Toby Simonds, Akira Yoshiyama (Tufa Labs)
**arXiv**: 2503.00735v3 [cs.LG] (submitted 2 Mar 2025, revised 5 Mar 2025)
**License**: CC BY 4.0

## Abstract

We introduce LADDER (Learning through Autonomous Difficulty-Driven Example Recursion), a framework which enables Large Language Models to autonomously improve their problem-solving capabilities through self-guided learning by recursively generating and solving progressively simpler variants of complex problems. Unlike prior approaches that require curated datasets or human feedback, LADDER leverages a model’s own capabilities to generate easier question variants. We demonstrate LADDER’s effectiveness on the subject of mathematical integration, improving Llama 3.2 3B’s accuracy from 1% to 82% on undergraduate-level problems and enabling Qwen2.5 7B Deepseek-R1 Distilled to achieve 73% on the MIT Integration Bee qualifying examination. We also introduce TTRL (Test-Time Reinforcement Learning), where we perform reinforcement learning on variants of test problems at inference time. TTRL enables Qwen2.5 7B Deepseek-R1 Distilled to achieve a state-of-the-art score of 90% on the MIT Integration Bee qualifying examination, surpassing OpenAI o1’s performance. These results show how self-directed strategic learning can achieve significant capability improvements without relying on architectural scaling or human supervision.

## Introduction

Reinforcement Learning (RL) has emerged as a highly effective approach for training Large Language Models (LLMs), yet its success hinges critically on the availability of appropriate training tasks [5, 9, 10, 12]. A fundamental challenge lies in obtaining verifiable tasks that match the model’s current capabilities. For RL to be effective, tasks must form a gradient of difficulties that allows for incremental learning progress [8]. When tasks exceed the model’s current abilities, the training process not only stalls but can lead to catastrophic collapse, resulting in degraded performance. This challenge is particularly acute in domains requiring complex reasoning, where the gap between simple and advanced tasks can be substantial [4, 12].

We propose Learning through Autonomous Difficulty-Driven Example Recursion (LADDER), a framework that enables LLMs to autonomously improve their problem-solving capabilities through strategic self-guided learning. The key insight is that models can bootstrap their own learning by recursively generating and solving progressively simpler variants of complex problems. For each challenging problem, LADDER prompts the model to create multiple easier variants, forming a natural difficulty gradient. This process continues recursively, with each variant spawning simpler sub-variants, until reaching problems the model can reliably solve. The solutions to these simpler problems then provide stepping stones for tackling progressively harder variants. We demonstrate that this self-bootstrapping approach achieves dramatic improvements beyond what’s possible through standard techniques like pass@k sampling - enabling models to reliably solve problems that were previously far beyond their capabilities.

Unlike previous approaches requiring carefully curated datasets or human feedback, LADDER leverages the model’s existing capabilities to create a natural difficulty gradient, allowing for systematic improvement through reinforcement learning with verifiable rewards. The framework requires only a reliable verification mechanism - in our case, numerical integration for checking solutions. This enables the model to assess its own progress and guide its learning trajectory without human intervention.

We demonstrate LADDER’s effectiveness on mathematical integration tasks, achieving remarkable improvements across multiple benchmarks. Using this approach, we improve a Llama 3B model’s accuracy from 1% to 82% on undergraduate-level integration problems. When applied to the challenging 2025 MIT Integration Bee examination, LADDER enables a 7B parameter model to achieve 73% accuracy, significantly outperforming much larger models, such as GPT-4o (42%), and typical human performance (15-30%). These results showcase how strategic problem decomposition and verified self-learning can achieve substantial capability improvements without relying on architectural scaling or human supervision.

Building on LADDER’s self-improvement framework, we propose Test-Time Reinforcement Learning (TTRL), a novel approach that extends these principles to inference time. TTRL dynamically generates problem variants during test-time and applies reinforcement learning to refine the model’s solutions, effectively creating a micro-learning process for each test instance. By leveraging the same verification mechanisms used in training, TTRL enables the model to further improve its performance. When applied to the 2025 MIT Integration Bee, TTRL boosts accuracy from 73% - with just LADDER - to 90%, demonstrating how scaling test-time compute through strategic problem decomposition can yield substantial performance improvements. We achieve state of the art accuracy, outperforming significantly larger models, such as OpenAI’s o1.

Thus, we make the following contributions:
- We propose a novel framework for autonomous model improvement through recursive problem decomposition and self-guided learning via reinforcement learning with GRPO.
- We develop a systematic method for generating and verifying problem variants that create natural difficulty gradients, requiring only numerical verification.
- We demonstrate significant empirical improvements on mathematical reasoning tasks, improving a Llama 3B model from 2% to 82% on undergraduate integration problems and achieving 73% accuracy on the MIT Integration Bee with a 7B model, matching SoTA performance
- We introduce Test-Time Reinforcement Learning (TTRL), a method for scaling compute at inference time through variant generation and reinforcement learning, boosting performance on the MIT Integration Bee from 73% to 90%.

(Full paper continues with Related Work, detailed Methodology including Algorithm 1 for LADDER and Algorithm 2 for TTRL, Experiments on Llama 3B and MIT Integration Bee, Results showing dramatic gains, Discussion on test-time compute scaling, and Conclusion. The complete text is available in the original arXiv HTML/PDF. This file preserves the core contribution and key sections for corpus use.)

## Key Excerpts from Methodology & Results (for quick reference)

**Variant Generation**: Multi-stage process using transformation library (reducing exponents, simplifying denominators, introducing nested functions, etc.). Model is prompted with sampled transformations to generate diverse easier variants forming a tree.

**Verification**: Numerical integration checker (exact match or high-precision tolerance).

**RL Protocol**: GRPO (Group Relative Policy Optimization) on the variant trees.

**Main Results**:
- Llama 3.2 3B: 1% → 82% on undergraduate integration problems.
- Qwen2.5 7B (Deepseek-R1 Distilled): 73% on 2025 MIT Integration Bee qualifying exam (beats GPT-4o at 42%).
- With TTRL: 90% on the same exam (surpasses OpenAI o1).

This demonstrates that autonomous curriculum construction + verifiable RL can produce large capability jumps on hard reasoning tasks without human supervision or massive pre-training.

**Source**: Retrieved from official arXiv HTML v3 (https://arxiv.org/html/2503.00735v3) on 2026-06-18. Full rights-cleared text stored here per CC BY 4.0.
