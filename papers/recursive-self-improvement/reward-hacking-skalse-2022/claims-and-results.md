# Defining and Characterizing Reward Hacking — Claims and Results Inventory

Source: https://arxiv.org/abs/2209.13085 | NeurIPS 2022 | Extraction only

Grounded in the folder's `deep-extraction.md` (Skalse, Howe, Krasheninnikov & Krueger). This is a **theoretical** paper over finite MDPs; "results" are proofs and counterexamples, not benchmarks. No RSI catalog ID is assigned to this paper in the corpus.

## Headline Claims

| # | Claim | Evidence Type | Extraction Confidence |
| --- | --- | --- | --- |
| 1 | Reward hacking: optimizing an imperfect proxy R_proxy leads to poor performance on the true reward R_true | Formal definition + MDP counterexamples | High |
| 2 | A proxy is "unhackable" iff increasing expected proxy return can never decrease expected true return | Definition + proofs | High |
| 3 | Over all stochastic policies, two rewards are unhackable only if one of them is constant | Theory (§5.1), via linearity in visit counts | High |
| 4 | Non-trivial unhackable pairs do exist for deterministic policies and finite stochastic sets | §5.2 construction + conditions | High |
| 5 | Natural simplifications (omitting features or fine details) often produce hackable proxies | Cleaning-robot counterexample | High |

## Result Categories

| Category | Reported Outcome | Notes |
| --- | --- | --- |
| Stochastic policy space | Unhackability requires one reward to be constant | Very strong/conservative condition |
| Finite / deterministic policies | Non-trivial unhackable pairs always exist | Real agents often approximate stochastic |
| "Simplification" attempts | Frequently hackable | Safe only if omitted terms are not jointly more important than shared ones |

## What Not To Overclaim

- Purely theoretical over finite MDPs with a toy 3-room cleaning robot — no LLM agents, no noisy continuous channels (tok/s, power, network). The proofs do not hand you a construction rule for multi-channel CursiveOS fitness.
- The paper says *when* optimizing a proxy is safe, not *how* to build a good proxy.
- Direct corpus relevance: it formally explains the Ch00/Ch22 Goodhart exposure — over-optimizing one weighted fitness channel can collapse true organism fitness even after early proxy gains (phase transition). Mitigation is hardware scoping + per-channel population-confirmation gates (Ch08), not a single optimized benchmark.
