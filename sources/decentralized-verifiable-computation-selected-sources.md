# Decentralized / Verifiable Computation: Selected Sources

Intake date: `2026-06-24`

Purpose: source-backed grounding for [Chapter 03d](../chapters/03d-verifying-decentralized-computation.md),
which surveys how prior systems verify computation produced by untrusted, paid,
remote machines — the "untrusted evaluator" frontier named in
[Chapter 03c](../chapters/03c-alphaevolve-decentralized-evolution-mapping.md) §5.
This is a first prior-art pass, not a complete survey of verifiable computation.
It deliberately captures each system's **verification mechanism**, not its token
or marketing claims.

## Sources Reviewed

| Source | Type | Citation | Key takeaway for CursiveOS |
| --- | --- | --- | --- |
| Sarmenta, *Sabotage-tolerance mechanisms for volunteer computing systems* | Peer-reviewed journal | Future Generation Computer Systems 18(4):561–572, 2002 | Voting, **spot-checking**, blacklisting/backtracking, and **credibility-based fault tolerance** (per-worker probability-of-correctness, escalate redundancy only where credibility is low). The canonical replication+spot-check toolkit; maps onto Ch08's N-rule/CV escalation. |
| Anderson, *BOINC: A Platform for Volunteer Computing* | Preprint / platform paper | arXiv:1903.01699, 2019 (+ BOINC `JobReplication` wiki) | **Persistent redundant computing**: run each job on ≥2 hosts, an app-specific **validator** finds a **quorum** of equivalent results and designates a **canonical** one. Validators may accept results "within specified tolerances" — early admission that exact-match breaks under hardware variation. |
| Teutsch & Reitwiessner, *A scalable verification solution for blockchains* (Truebit) | Preprint / protocol whitepaper | arXiv:1908.04756, 2017/2019 | **Verification game**: Solver posts result; Challenger triggers a **binary-search/bisection** dispute over the execution trace adjudicated by a cheap on-chain **referee** in O(log n). Solves the **verifier's dilemma** via **forced errors** + **jackpot** payouts. The reference *optimistic* design. |
| Kang et al. (Gensyn), *Verde: Verification via Refereed Delegation for Machine Learning Programs* | Preprint | arXiv:2502.19405, 2025 (+ gensyn.ai/articles/verde) | **Refereed delegation**: correct result guaranteed if ≥1 of N providers is honest; disputes resolved by bisection over the ML compute graph + neutral referee. Depends on **RepOps** (Reproducible Operators) to force bitwise reproducibility across heterogeneous hardware — the precondition CursiveOS lacks. |
| *Confidential VMs Explained: An Empirical Analysis of AMD SEV-SNP and Intel TDX* | Peer-reviewed (SIGMETRICS) | Proc. ACM Meas. Anal. Comput. Syst., 2025 | TEE remote attestation as a hardware-rooted alternative to re-execution: Intel **TDX** (SEAM mode) and AMD **SEV-SNP** encrypt/integrity-protect VM memory and emit signed attestation quotes. Strengthens Ch11 hardware identity but is not a full verification answer alone. |
| Sun et al., *SoK: A cloudy view on trust relationships of CVMs* | Peer-reviewed SoK | arXiv:2503.08256, 2025 | Documents where confidential VMs **fall short** in public cloud (trust relationships, side channels). Reason to treat TEE attestation as an *input* to credibility, not a guarantee. |
| Ethereum L2 fraud-proof vs. validity-proof literature | Technical reference / explainer | (optimistic rollup vs zk-rollup comparisons; e.g. ethereum.org, Cyfrin) | The **optimistic (fraud-proof) vs. validity (zk-proof)** axis: optimistic = cheap, delayed finality via challenge window; validity = immediate, cryptographic, high prover cost. The organizing axis for the whole design space. |
| Bittensor **Yuma Consensus** documentation | Project documentation | docs.learnbittensor.org / discoverbittensor.com | **Consensus over subjective scores**: validators score miners, scores aggregated **stake-weighted**, validators deviating from the **median are clipped** to penalize collusion. The only surveyed family tolerating non-reproducible, subjective fitness — and the most Goodhart-exposed. |

## Practical Extraction

### 1. The space is one axis: optimistic vs. validity

Every technique is a point between "assume correct, check only on challenge"
(spot-checking, Truebit, Verde, optimistic rollups) and "prove/verify up front"
(BOINC quorum, TEE attestation, zk validity proofs). Optimistic trades latency
for cost; validity trades cost for immediate finality. **Both ends assume a
single checkable right answer.**

### 2. CursiveOS cannot inherit the strong techniques

- **No bitwise reproducibility** → exact-match replication and bisection disputes
  do not apply; Verde's RepOps has no analog for live-hardware timing
  distributions. Only **statistical** ("within tolerance") verification survives.
- **No global ground truth** (hardware-scoped fitness, Ch08) → planted
  spot-checks / forced errors have no reusable known answer across the fleet.
- **Partly subjective fitness** → only stake-weighted consensus (Bittensor)
  copes, and it imports the Goodhart/reward-hacking risk (Skalse et al.,
  `papers/recursive-self-improvement/reward-hacking-skalse-2022/`).

### 3. The realistic CursiveOS stack is the weak end of the space

Replication-with-tolerance + credibility scoring (≈ Ch08 N-rule/CV) as the base,
TEE attestation (Ch11) to cheaply raise single-reporter credibility so redundancy
is spent only where needed, and stake-weighted consensus quarantined behind
anti-Sybil economics (Ch02/Ch11/Ch12) for irreducibly subjective channels.
Interactive disputes and zk proofs are tracked, not adopted.

## Suggested Source URLs

- Sarmenta (2002): https://www.sciencedirect.com/science/article/abs/pii/S0167739X01000772
- BOINC (Anderson 2019): https://arxiv.org/abs/1903.01699 ; replication: https://github.com/BOINC/boinc/wiki/JobReplication
- Truebit (Teutsch & Reitwiessner): https://arxiv.org/abs/1908.04756
- Verde (Gensyn 2025): https://arxiv.org/abs/2502.19405 ; https://www.gensyn.ai/articles/verde
- Confidential VMs Explained (SIGMETRICS 2025): https://dl.acm.org/doi/10.1145/3700418
- SoK on CVM trust (2025): https://arxiv.org/abs/2503.08256
- Bittensor Yuma Consensus: https://docs.learnbittensor.org/learn/yuma-consensus
