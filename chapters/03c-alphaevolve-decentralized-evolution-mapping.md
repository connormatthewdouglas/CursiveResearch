## Corpus status (living layer)

**Last reconciled:** 2026-06-24
**Confidence:** AlphaEvolve's verifier-grounded evolution loop is **Validated at industrial scale** (Google DeepMind white paper, RSI-001); mapping it onto a *decentralized* reward system that outsources compute and tokens is **Unvalidated** (architecture only) and in parts **Speculative**. The 48-multiplication matrix result is a **ceiling demonstration**, not a CursiveOS expectation.
**Read with:** [Chapter 00](00-benchmark-schema-and-measurement-validity.md) (measurement validity), [Chapter 02](02-bitcoin-native-economics-and-proof-of-useful-optimization.md) (BTC contributor economics), [Chapter 06](06-mutation-safety-and-permission-law.md) (mutation safety on live Linux), [Chapter 08](08-population-confirmation-and-fleet-statistics.md) (population confirmation), [Chapter 11](11-hardware-identity-and-anti-spoofing.md) (Sybil / anti-spoofing), [Chapter 12](12-open-source-funding-and-contributor-incentives.md) (incentives), [Chapter 20](20-market-and-viability.md) (Bittensor market flag), `papers/recursive-self-improvement/alphaevolve/`

### Authoritative for

- Mapping the AlphaEvolve loop (LLM mutation → external evaluator → evolutionary archive) onto a decentralized CursiveOS reward system
- Separating AlphaEvolve's *externally verifiable* result (one matrix-multiplication algorithm) from its *proprietary, locally unverifiable* infrastructure claims
- The disanalogies that make a single trusted evaluator fundamentally different from an untrusted, noisy, heterogeneous sensor fleet

### Superseded or narrowed (do not cite externally)

- "AlphaEvolve proves CursiveOS will work" — **Disproven as framing**. AlphaEvolve validates the *loop*; it does not solve evaluator decentralization, which is the actual CursiveOS hard part.
- The Ch20 import "reduce training and inference times for Bittensor nodes by up to 23%" — **Unvalidated** imported magnitude, not a CursiveOS-measured result (consistent with the Ch20 living-layer flag).
- Any expectation that CursiveOS organisms will produce Strassen-class algorithmic breakthroughs — **Speculative**.

### Open until experiment/hardware

- Whether a noisy, hardware-scoped sensor fleet (Ch08) can serve as a multi-evaluator equivalent to AlphaEvolve's deterministic checkers
- Sybil- and Goodhart-resistance of decentralized fitness once real tokens are at stake (Ch11 / Ch02 / Ch12)
- Open-tool reproduction (CodeEvolve, RSI-017) of the loop on public OS/kernel benchmarks rather than proprietary simulators

---

## Reinforced research (2026-06-24)

- **AlphaEvolve (RSI-001):** Google DeepMind, arXiv:2506.13131 — `papers/recursive-self-improvement/alphaevolve/`; **CC BY-NC-ND 4.0**, so this chapter paraphrases only and stores no full text. Industrial-scale, verifier-grounded evolutionary coding agent.
- **FunSearch (RSI-002) lineage:** `papers/recursive-self-improvement/funsearch/` — the canonical "LLM proposes, verifier disposes" pattern AlphaEvolve extends.
- **Reward hacking (Skalse et al., NeurIPS 2022):** `papers/recursive-self-improvement/reward-hacking-skalse-2022/` — the Goodhart formalism explaining why a decentralized *proxy* reward is attackable at scale.
- **Population confirmation (Ch08):** the fleet-statistics machinery that would have to stand in for AlphaEvolve's single trusted evaluator.

---

## 1. What AlphaEvolve Is, and Its Loop

AlphaEvolve (Google DeepMind, 2025; RSI-001) is an evolutionary coding agent: a large language model proposes edits to a program, one or more **external evaluators** score each candidate for correctness and performance, and an evolutionary outer loop keeps the strongest lineages in an archive and iterates. It is the industrial-scale descendant of FunSearch (RSI-002) and sits in the DeepMind discovery lineage (AlphaDev → FunSearch → AlphaEvolve). Paraphrased from the extraction; the white paper is CC BY-NC-ND, so no full text is reproduced here.

The loop, in the corpus's own terms:

```
seed program / algorithm
    → LLM proposes code edits (the mutation operator)
    → evaluator(s) score candidates: correctness AND performance
    → evolutionary selection keeps diverse high performers in an archive
    → iterate
```

The load-bearing property — the one CursiveOS actually wants — is the **separation of proposer from judge**: the LLM never decides acceptance; a deterministic, trusted evaluator does. This is the same boundary CursiveOS draws between its probabilistic shell/proposer and its deterministic measurement daemon (Ch05/Ch06). **Confidence: Supported** that this pattern is the right one; the AlphaEvolve paper is strong evidence it works *when the evaluator is trustworthy*.

## 2. Results, Split by Verifiability

The corpus must not blur a checkable mathematical result with proprietary infrastructure marketing. They have very different evidentiary weight.

### 2.1 Externally verifiable — a *ceiling*, not an expectation

- **4×4 complex matrix multiplication in 48 scalar multiplications.** Reported as the first improvement over the Strassen-class barrier in this setting in 56 years. This is a discrete, **independently checkable** claim: the algorithm either uses 48 multiplications and is correct, or it does not. **Confidence: High *if* independently verified** (the corpus has not re-derived it).
- **Why it is a ceiling, not a forecast:** it demonstrates that verifier-grounded evolution *can* reach genuinely novel, provably correct results given a clean deterministic checker and large compute. It says nothing about what a decentralized fleet tuning live Linux can expect. Treat it as proof the loop *has headroom*, never as a CursiveOS deliverable. **Confidence: Validated** (as an existence proof of the loop's ceiling).

### 2.2 Proprietary / Google-infrastructure — not locally verifiable

- Datacenter scheduling efficiency gains, hardware-accelerator simplification, and a self-referential speedup of AlphaEvolve's own LLM training. Each is an **internal Google deployment** with sparse public detail. **Confidence: Unvalidated** — marked **[needs full-text]** in the extraction; the evaluators, baselines, and compute budgets are proprietary and not reproducible locally.
- **The Ch20 "Bittensor 23%" figure** belongs in this bucket. Chapter 20's DOCX import claims AlphaEvolve-style semantic mutation can "reduce training and inference times for Bittensor nodes by up to 23%." Per the Ch20 living layer, this is an **Unvalidated** imported magnitude, not a CursiveOS harness measurement. This chapter inherits that flag verbatim and does not upgrade it.

**Takeaway:** exactly one AlphaEvolve result is independently checkable, and it is a math micro-problem. Everything attractive to a decentralized-infrastructure pitch is proprietary and unverified.

## 3. The Mapping: AlphaEvolve → a Decentralized CursiveOS Reward System

Framing question for this chapter: *what does AlphaEvolve look like mapped onto a Linux repo with a decentralized reward system that outsources compute and tokens?* The structural correspondences:

| AlphaEvolve component | CursiveOS decentralized analogue | Confidence in the mapping |
| --- | --- | --- |
| **Single trusted evaluator** (deterministic correctness + performance checker) | **Untrusted, noisy, heterogeneous sensor fleet** — many contributor machines reporting hardware-scoped measurements (Ch08) | **Unvalidated** — this is the central substitution and the hardest one; a fleet is not a clean checker |
| **Central orchestrator** (maintains population, selects parents, runs the loop) | **CursiveRoot submission + population confirmation** (Ch08): N-rule, per-channel CV escalation, hardware-scoped fitness | **Supported** as architecture; fleet-scale calibration **Unvalidated** |
| **Google-owned compute** (proprietary clusters run the search) | **BTC-paid contributor compute** (Ch02): independent operators supply machines; fitness-gated Bitcoin payouts, no token emission | **Unvalidated** — economics specified (Ch02), real payments not deployed |
| **LLM mutation operator** (proposes code edits) | Proposer/shell suggests reversible presets; **only the measurement daemon writes sensor truth** (Ch05) | **Supported** — same proposer/judge boundary |
| **Evolutionary archive** (lineage of strong candidates) | MAP-Elites-structured preset archive across hardware niches (RSI-028; CodeEvolve CVT variant) | **Supported** direction; descriptor design open |

The mapping is *structurally clean* — every AlphaEvolve box has a CursiveOS counterpart. That cleanliness is exactly what makes it dangerous to oversell, because the single substitution in row one (trusted evaluator → untrusted fleet) is where all the difficulty concentrates.

## 4. Disanalogies — Why the Map Breaks (read this as carefully as §3)

AlphaEvolve runs inside one organization's trust boundary with deterministic checkers. A decentralized reward system that outsources compute and tokens violates almost every precondition that made AlphaEvolve safe. These are not footnotes; they are the reason the project is hard.

- **Sybil attacks (Ch11).** AlphaEvolve's evaluator cannot be spoofed; a contributor fleet can. Fake or cloned nodes can manufacture confirmations and harvest tokens. Population confirmation only means something if independence is real, which requires hardware fingerprints and anti-spoofing (Ch11). **Confidence: Unvalidated** that fleet independence can be enforced under adversarial economics.
- **Goodhart at fleet scale (Skalse et al., NeurIPS 2022).** AlphaEvolve optimizes against a *trusted* objective. The moment fitness is a decentralized **proxy** with money attached, the formal reward-hacking results apply: over-optimizing one weighted channel can collapse true organism fitness, and the failure can be a sudden phase transition rather than gradual. A single trusted evaluator dodges this; a paid fleet invites it. **Confidence: Supported** that this risk is real and structural.
- **Hardware-scoped fitness (Ch08).** AlphaEvolve's checkers are environment-independent (a 48-mult algorithm is 48 mults everywhere). CursiveOS fitness is hardware-specific and noisy — the same preset helps one machine and hurts another. There is no global ground truth to evolve against, only per-niche, variance-bearing evidence requiring N-rule and CV escalation. **Confidence: Partly Supported** (single-machine CV validated, Ch00 §5; fleet calibration **Unvalidated**).
- **Mutation safety on live Linux (Ch06).** AlphaEvolve mutates code in a sandbox; a CursiveOS organism mutates a running operating system (sysctl, scheduler/eBPF, GPU power, firmware). Class 4–6 mutations can crash or brick a contributor's machine. The loop must be wrapped in staged rollback and permission law (Ch06) that AlphaEvolve simply does not need. **Confidence: Supported** that this is mandatory and not yet implemented.
- **Economic attack surface (Ch02 / Ch12).** AlphaEvolve has no payout to game. A token/BTC reward creates incentives to fake work, collude, or grief competitors. Funding and incentive design (Ch12) and sensor-gated BTC payouts (Ch02) become part of the *security* surface, not just the economics. **Confidence: Unvalidated** — payout rails not deployed; attack modeling open.

## 5. Thesis

**The loop is validated at industrial scale; decentralizing the evaluator is the unsolved hard part.**

AlphaEvolve is strong, honest evidence that *propose-mutate-evaluate-evolve* produces real, sometimes provably-correct improvements — when a trusted, deterministic evaluator anchors selection. CursiveOS wants to keep that loop while replacing the one component that made it trustworthy (a single owned evaluator) with the one thing AlphaEvolve never had to handle (an untrusted, noisy, economically-incentivized, hardware-heterogeneous fleet). Nothing in the AlphaEvolve paper addresses that substitution.

So this chapter is explicitly **not** an argument that "AlphaEvolve proves CursiveOS works." It is the opposite: AlphaEvolve retires the question of whether the *loop* is viable and isolates the real research frontier — Sybil-resistant, Goodhart-resistant, hardware-scoped, mutation-safe, economically-hardened decentralization of the evaluator. That frontier is where Chapters 02, 06, 08, 11, and 12 do their work, and it is **Unvalidated** until the fleet exists and is measured.
