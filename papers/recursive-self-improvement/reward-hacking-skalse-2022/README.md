# Defining and Characterizing Reward Hacking — Skalse et al. (2022)

**Source**: https://arxiv.org/abs/2209.13085 (v2 2025-03-05)
**Authors**: Joar Skalse, Nikolaus H. R. Howe, Dmitrii Krasheninnikov, David Krueger
**Venue**: NeurIPS 2022 (peer-reviewed); arXiv:2209.13085v2
**Corpus Status**: Important (formal foundations for Goodhart/proxy risks in measurement and self-improvement loops)
**Rights Status**: arXiv non-exclusive distribution license — extraction and citation only; no full verbatim text stored.
**License Note**: Content here is a high-quality paraphrased deep extraction based on publicly retrieved abstract, introduction, examples, and conclusions from the arXiv page and PDF. No verbatim reproduction of substantial portions.

## Why This Paper Was Added

This paper provides the first formal definition of *reward hacking* (optimizing an imperfect proxy reward function leads to poor performance on the true reward) and conditions for *unhackable* proxies. It directly fills a gap in the corpus's treatment of Goodhart's Law, proxy optimization in agent evaluation/fitness functions, and measurement validity for recursive self-improvement (see RESEARCH_PIPELINE.md P0 RSI and Software Organisms sections, and Chapter 22 §4 Goodhart exposure).

It matters to CursiveOS because fitness functions, benchmark deltas, and self-improvement loops inherently use proxies. Formal conditions for when proxy optimization cannot degrade true performance are essential to avoid specification gaming in local agents, incentive design, and organism measurement.

**Integration**: Key lessons added as additive subsection in Chapter 22 (Benchmark Schema and Measurement Validity) after §4 Goodhart exposure. Paraphrased extraction stored here for future agents.

**Duplicate Check**: No prior coverage of this specific formal treatment or the Skalse et al. unhackability results in papers/, chapters, or source lists (confirmed via repo tree and content search equivalents). Gödel Agent and Reflexion cover self-referential RSI but not this proxy theory.

**Retrieved Source**: Full abstract, introduction, cleaning-robot example, related work, and conclusions retrieved directly via arXiv HTML/PDF tools on 2026-06-18. All specific claims, numbers, and quotes below are grounded in that retrieval; anything not retrieved is marked or omitted.
