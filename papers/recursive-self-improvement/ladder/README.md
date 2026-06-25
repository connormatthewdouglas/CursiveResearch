# LADDER: Self-Improving LLMs Through Recursive Problem Decomposition

**Authors**: Toby Simonds, Akira Yoshiyama (Tufa Labs)
**Year / Venue**: 2025, arXiv:2503.00735v3 [cs.LG]
**License**: CC BY 4.0 (rights-cleared for full text storage)
**Corpus Status**: Cornerstone paper for test-time / curriculum-style recursive self-improvement

## Why This Paper Matters to CursiveOS

LADDER provides one of the cleanest demonstrated examples of **bounded, verifiable recursive self-improvement** using only the model's own capabilities plus a simple numerical verifier. It constructs an autonomous difficulty gradient through recursive variant generation and then applies reinforcement learning (GRPO) on those variants.

Key transferable lessons:
- Models can bootstrap their own training data by recursively decomposing hard problems into solvable sub-problems.
- Verifiable rewards (here: numerical integration correctness) enable safe, grounded improvement loops without human labels.
- Test-Time Reinforcement Learning (TTRL) shows how the same mechanism can be applied at inference time for micro-adaptation.
- Dramatic gains on hard math benchmarks (Llama 3B: 1% → 82%; 7B model beats GPT-4o and approaches o1 on MIT Integration Bee) using only self-generated curriculum + RL.

This directly supports CursiveOS themes of:
- Proposer / verifier separation (model proposes variants; verifier is deterministic math check).
- Persistent skill / capability accumulation without weight updates in the base model.
- Test-time / runtime adaptation loops that are safe because they stay within verifiable domains.

It fills a gap in the current corpus between STOP (scaffold self-improvement) and pure evolutionary search (AlphaEvolve-style). LADDER shows a practical middle path: autonomous curriculum construction + grounded RL.

## Source
- arXiv: https://arxiv.org/abs/2503.00735
- HTML version: https://arxiv.org/html/2503.00735v3
- PDF: https://arxiv.org/pdf/2503.00735

Full PDF and agent-readable PDF text extraction are stored in `paper.pdf` and `paper.md` (rights-cleared). Deep extraction and claims inventory are in the sibling files.
