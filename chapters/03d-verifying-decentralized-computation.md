## Corpus status (living layer)

**Last reconciled:** 2026-06-24
**Confidence:** This chapter is a **source-backed external survey** of how prior systems verify computation done by untrusted, paid, remote machines. The prior art is **Validated as real engineering** (deployed in volunteer computing, blockchain rollups, decentralized ML, and confidential-computing hardware). Its **applicability to CursiveOS's hardware-scoped, noisy benchmark fitness is Partly Supported at best** — three structural disanalogies (non-determinism, no global ground truth, subjective fitness) break the strongest techniques. Nothing here is a CursiveOS-measured result.
**Read with:** [Chapter 03c](03c-alphaevolve-decentralized-evolution-mapping.md) (this chapter answers the frontier 03c names), [Chapter 00](00-benchmark-schema-and-measurement-validity.md) (measurement validity, CV), [Chapter 08](08-population-confirmation-and-fleet-statistics.md) (N-rule, hardware-scoped fitness — CursiveOS's current "verification" layer), [Chapter 11](11-hardware-identity-and-anti-spoofing.md) (Sybil / attestation inputs), [Chapter 02](02-bitcoin-native-economics-and-proof-of-useful-optimization.md) + [Chapter 12](12-open-source-funding-and-contributor-incentives.md) (economics that turn verification into a security surface), [Chapter 06](06-mutation-safety-and-permission-law.md) (mutation safety on live Linux)

### Authoritative for

- The design space of **verifying outsourced/decentralized computation**: redundant execution + spot-checking, interactive dispute / refereed delegation, hardware attestation, cryptographic validity proofs, and consensus over subjective scores.
- The **optimistic vs. validity** axis as the organizing principle for the whole space, and where CursiveOS sits on it.
- Why the strongest replication- and proof-based techniques **do not directly transfer** to hardware-scoped, variance-bearing benchmark fitness, and which weaker techniques are the realistic fit.

### Superseded or narrowed (do not cite externally)

- Do **not** cite this chapter as evidence that CursiveOS *has* solved decentralized verification. It surveys prior art and maps it; it claims no implemented CursiveOS mechanism.
- Per-system marketing magnitudes (token-network throughput, "global supercomputer" claims) are **Unvalidated** and deliberately omitted; only the verification *mechanism* of each system is load-bearing here.

### Open until experiment/hardware

- Whether RepOps-style bitwise reproducibility (Verde) is even achievable for an OS-tuning benchmark, or whether CursiveOS is permanently confined to statistical (not exact-match) verification.
- Whether a Bittensor-style stake-weighted median over contributor scores can resist collusion once real BTC is at stake (Ch02/Ch11/Ch12) — the only surveyed family that tolerates subjective, non-reproducible fitness, and the one most exposed to Goodhart (Skalse et al.).
- Whether TEE attestation (Ch11) can bind a *measurement* to *specific hardware* tightly enough to make spot-checking credible without full replication.

---

## Reinforced research (2026-06-24)

- **Frontier source:** [Chapter 03c](03c-alphaevolve-decentralized-evolution-mapping.md) §5 — "the loop is validated at industrial scale; decentralizing the evaluator is the unsolved hard part." This chapter is the prior-art survey 03c implies but does not contain.
- **Goodhart anchor:** `papers/recursive-self-improvement/reward-hacking-skalse-2022/` (Skalse et al., NeurIPS 2022) — formalizes why any decentralized *proxy* reward with money attached is attackable; bounds how much the consensus-over-subjective-scores family (Bittensor) can be trusted.
- **Sources digest:** [`sources/decentralized-verifiable-computation-selected-sources.md`](../sources/decentralized-verifiable-computation-selected-sources.md) — full citation list and per-source extraction.

---

## 1. Why this chapter exists

Chapter 03c isolates CursiveOS's actual research frontier in one sentence: the AlphaEvolve loop is validated, but it assumes a **single trusted evaluator**, and CursiveOS must replace that evaluator with an **untrusted, noisy, economically-incentivized, hardware-heterogeneous fleet**. Chapters 08 (population confirmation), 11 (hardware identity), and 02/12 (economics) each work one face of that problem, but the corpus had never assembled the **external computer-science prior art** on the general question: *how do you trust a computational result produced by a machine you do not control and that is paid to lie?*

That question is decades old and has a real literature. This chapter surveys it as a design space, then maps it back onto CursiveOS — honestly, including where the prior art simply does not apply. **Confidence: Supported** that this is the right framing; the mappings carry their own labels.

## 2. The design space: five families of verification

### 2.1 Redundant execution + statistical spot-checking

The oldest answer is **do the work more than once and compare**. Sarmenta's *sabotage-tolerance* work for volunteer computing (Future Generation Computer Systems, 2002) is the canonical treatment: **voting** (run each task on ≥2 machines, accept on a quorum) reduces error exponentially with redundancy but doubles cost and fails when saboteurs are numerous; **spot-checking** (occasionally hand a worker a task with a known answer) reduces error roughly linearly for only a small overhead; and **credibility-based fault tolerance** combines them by maintaining a per-worker probability-of-correctness and a per-result confidence, escalating redundancy only where credibility is low. **blacklisting** and backtracking remove and unwind detected saboteurs.

BOINC (Anderson, arXiv:1903.01699) productionized exactly this: *persistent redundant computing* runs each job on two or more hosts, a per-application **validator** compares outputs, looks for a **quorum** of equivalent results, designates one as **canonical**, and spawns more instances until quorum is reached. Crucially, BOINC validators are *application-specific* and can accept results that "agree within specified tolerances" — an early acknowledgment that floating-point and hardware variation break exact-match comparison. **Confidence: Validated** as deployed engineering (millions of hosts over two decades).

### 2.2 Interactive dispute / refereed delegation

Replication is wasteful when the honest case is the common case. The **optimistic** family instead assumes results are correct, posts them cheaply, and only runs an expensive **dispute resolution game** when someone challenges. Truebit (Teutsch & Reitwiessner, *A scalable verification solution for blockchains*, arXiv:1908.04756) is the reference design: a **Solver** posts a result; a **Challenger** who disagrees plays a **verification game** — a binary search (bisection) over the computation's execution trace that narrows disagreement to a single instruction, which a cheap on-chain **referee** ("supreme court") then settles in O(log n). Truebit's sharpest contribution is economic: the **verifier's dilemma** (why check work if checking is unpaid?) is solved with **forced errors** (the protocol occasionally requires the Solver to post a wrong answer) plus a **jackpot** that pays verifiers who catch them, making diligent checking rational.

Gensyn's **Verde** (arXiv:2502.19405) adapts this to machine learning as **refereed delegation**: a client delegates to several untrusted compute providers and is guaranteed the correct result *if at least one is honest*; disagreements are resolved by a bisection dispute over the ML compute graph adjudicated by a neutral referee. Verde's key enabling trick is **RepOps (Reproducible Operators)**, a library that forces a fixed floating-point operation order so an ML program is **bitwise reproducible across different hardware** — without which "did you get the same answer?" is undefined. **Confidence: Validated** as a mechanism; note the dependency on reproducibility, which §3 shows CursiveOS lacks.

### 2.3 Hardware attestation (trusted execution environments)

A different answer: don't re-run the work, **prove it ran untampered on real hardware**. Intel TDX (via the SEAM processor mode) and AMD SEV-SNP encrypt and integrity-protect a VM's memory and state from the host OS and hypervisor, and back it with **remote attestation** — a hardware-rooted signed quote that lets a remote party verify the environment before trusting its output. This converts "trust the operator" into "trust the silicon vendor's root of trust." It is real and shipping, but a 2025 SoK (arXiv:2503.08256) and the SIGMETRICS-2025 measurement study ("Confidential VMs Explained") document that public-cloud confidential VMs still rest on awkward trust relationships and side-channel caveats. **Confidence: Supported** as an input to verification (it strengthens Ch11 hardware identity), **not** a complete answer on its own.

### 2.4 Cryptographic validity proofs

The strongest guarantee: attach a succinct cryptographic proof (zk-SNARK/STARK) that the computation was performed correctly, verifiable in milliseconds without re-execution and without trusting any hardware. This is the **validity-proof** end of the spectrum used by zk-rollups. The cost is on the prover side — generating proofs for arbitrary computation is expensive and, for large heterogeneous workloads like OS benchmarking, currently impractical. **Confidence: Validated** cryptographically; **Unvalidated/likely impractical** for CursiveOS-class workloads in the near term.

### 2.5 Consensus over subjective scores

When there is **no objective ground truth** to replicate or prove — only opinions about quality — the remaining option is to aggregate many evaluators and punish outliers. Bittensor's **Yuma Consensus** (see `docs.learnbittensor.org`) is the live example: validators score miners, scores are aggregated **weighted by stake**, and validators whose scores deviate too far from the stake-weighted **median are clipped** (lose influence/reward), which is meant to make collusion economically irrational and reward honest, consistent evaluation. This is the only surveyed family that tolerates *subjective, non-reproducible* judgments — and exactly because it optimizes a **proxy with money attached**, it is the family most exposed to the reward-hacking results of Skalse et al. (Ch00 §4.1; `reward-hacking-skalse-2022`). **Confidence: Partly Supported**; collusion-resistance under real stake is **Unvalidated**.

## 3. The organizing axis, and where CursiveOS sits

Every family above is a point on one axis — **optimistic vs. validity**:

| | Optimistic (assume correct, check on challenge) | Validity (prove/verify up front) |
| --- | --- | --- |
| **Examples** | Spot-checking (Sarmenta), Truebit, Verde, optimistic rollups | BOINC quorum (replication), TEE attestation, zk validity proofs |
| **Up-front cost** | low | high (replication, proving, or attestation) |
| **Finality** | delayed (challenge window) | immediate |
| **Best when** | honest case common, disputes rare, *answers are checkable* | adversaries common, or no time for disputes |

The rollup literature states the trade cleanly: fraud-proof (optimistic) systems are cheap but accept a challenge-window delay; validity-proof (zk) systems give immediate, cryptographically-guaranteed finality at high prover cost. **Both ends assume the computation has a single right answer that a referee or a proof can pin down.** That assumption is precisely what CursiveOS lacks.

## 4. Why most of the prior art does not transfer to CursiveOS

The corpus must not adopt these techniques by analogy without naming the disanalogies (the same discipline Ch03c applies to AlphaEvolve):

- **Non-determinism / no bitwise reproducibility.** Replication (BOINC) and dispute games (Truebit, Verde) ultimately compare answers. Verde needs **RepOps** to make ML bitwise-reproducible before disputes mean anything. A CursiveOS fitness measurement is a *timing distribution on live hardware* — governor state, thermals, page cache, and contending processes all move it (Ch00 §5 CV). There is no RepOps for "milliseconds to cold-start an inference server." Exact-match verification is off the table; only **statistical** verification (does the reported distribution match a re-measured distribution within tolerance?) is possible — closer to BOINC's "agree within tolerance" validator than to a proof. **Confidence: Supported.**
- **No global ground truth (hardware-scoped fitness).** Spot-checking and forced errors require a *known correct answer* to plant. CursiveOS fitness is **per-niche**: the same preset helps one machine and hurts another (Ch08, Ch03c §4). A "known answer" only exists relative to a specific hardware profile, so a spot-check task cannot be blindly reused across the fleet. This weakens the cheapest optimistic technique. **Confidence: Supported.**
- **Subjective/proxy fitness invites Goodhart.** The one family that tolerates non-reproducible, subjective evaluation — consensus-with-median-clipping (Bittensor) — is, by Skalse et al., the one whose proxy reward can be gamed or collapsed once real money is attached, and whose failure can be a sudden phase transition rather than gradual drift. **Confidence: Supported** that the risk is structural.
- **Mutation safety is orthogonal but mandatory.** None of these systems mutate a *running operating system*; they verify sandboxed compute. CursiveOS verification must sit on top of Ch06 permission law and staged rollback, which the prior art neither provides nor needs. **Confidence: Supported.**

## 5. What this implies for CursiveOS (synthesis, not spec)

The realistic verification stack for a decentralized CursiveOS fleet is a **hybrid that borrows the weak, statistical techniques and rejects the strong, exact ones**:

1. **Replication-with-tolerance + credibility**, in the spirit of BOINC validators and Sarmenta credibility scores, is the natural base layer — and it is essentially what Ch08's N-rule + per-channel CV escalation + hardware-scoped pooling already approximate. This chapter reframes Ch08 as CursiveOS's *de facto* sabotage-tolerance layer and gives it a literature lineage.
2. **TEE attestation (Ch11)** can raise the credibility of a single reporter cheaply enough that spot-checking/replication can be reserved for low-credibility or high-stakes results — the Sarmenta optimization of "spend redundancy only where credibility is low."
3. **Stake-weighted consensus (Bittensor-style)** is the only option when a channel is irreducibly subjective, but it must be quarantined behind the Skalse/Goodhart warning and the Ch02/Ch11/Ch12 anti-Sybil work before any BTC payout depends on it.
4. **Interactive dispute and zk validity proofs** are, for now, **out of reach** for OS-tuning workloads (no reproducibility, impractical proving) and should be tracked, not adopted.

**Thesis:** the prior art has solved verification of decentralized computation *for problems with a checkable right answer*. CursiveOS's evaluation has **no checkable right answer** — it is hardware-scoped, noisy, and partly subjective — so it cannot inherit the strong techniques (proofs, exact replication, planted spot-checks) and is confined to the **statistical, credibility-weighted, attestation-assisted** end of the space. That is a narrower and harder regime than any surveyed system operates in, which is exactly why Ch03c calls evaluator decentralization the unsolved part. The next move is empirical: test whether Ch08's statistical confirmation actually behaves like a sabotage-tolerance layer under adversarial, hardware-scoped conditions (RESEARCH_PIPELINE §2 Knowledge Gaps; experiments under `experiments/`).
