# Validation Note: Chapter 02 Market and Viability

Date checked: 2026-05-26
Agent / reviewer: GPT-5.5 Thinking / ChatGPT
Scope: targeted validation of highest-impact Chapter 02 claims
Status: partially verified, but market numbers remain date-sensitive
Source IDs: SRC-02-001 through SRC-02-010 in `sources/chapter-02-selected-sources.md`

## Summary

Chapter 02 remains useful as a positioning and viability document, but it should not be treated as current truth without date-stamped market data. The broad thesis is supported: crypto mining has become industrial and margin-sensitive; miners are increasingly exploring AI/HPC infrastructure; DePIN networks create non-hash compute demand; and OS/network/kernel tuning can matter for latency-sensitive distributed compute.

The weak points are specific numeric claims and project-state claims. Bitcoin difficulty, network hashrate, hashprice, ASIC specs, Bittensor subnet counts, io.net status, and DePIN reward structures must be checked against current data sources whenever used.

## Claims Checked

| Claim ID | Claim | Status | Evidence | Notes / Required Rewrite |
| --- | --- | --- | --- | --- |
| CL-02-001 | Bitcoin mining is now dominated by specialized ASIC infrastructure and margin-sensitive industrial operators. | supported as direction | SRC-02-001, SRC-02-002, SRC-02-003 | Keep, but avoid overclaiming that all mining is industrial or centralized. |
| CL-02-002 | Current Bitcoin difficulty/hashrate values in the imported chapter are safe to reuse. | stale / requires refresh | SRC-02-001; live dashboards required | Always refresh current values before use. Do not cite stale February 2026 numbers without date context. |
| CL-02-003 | Miners are pivoting toward AI/HPC compute because mining margins are pressured. | partially supported | SRC-02-002, SRC-02-003 | Supported by current reporting. For decision-grade claims, add public company filings and hashprice data. |
| CL-02-004 | DePIN/AI networks increase the relevance of OS-level optimization beyond traditional mining. | supported as direction | SRC-02-002, SRC-02-003, Chapters 05/09 | Keep as strategic thesis; quantify with network/project-specific data later. |
| CL-02-005 | Linux has many tunable parameters and static best-practice tuning is insufficient for all hardware/workloads. | supported by corpus | Chapters 03/04/05/09 | Strong thesis, now backed by technical chapters. |
| CL-02-006 | KconfigTune-style AI tuning can deliver 19.92% gains and should be treated as CursiveOS baseline expectation. | unverified / overbroad | source extraction pending | Treat as literature lead only until original paper/methodology is extracted. |
| CL-02-007 | LLM-generated heuristics can discover useful low-level optimizations. | partially supported | Chapter 05 PolicySmith/SemaTune sources | Supported as research direction, not specific 23% Bittensor improvement. |
| CL-02-008 | BBR can outperform loss-based CUBIC on high-BDP/lossy links. | supported as direction | SRC-02-007, SRC-02-008 | Keep with caveats. Exact imported numbers like 2700x require original source and reproduction. |
| CL-02-009 | Socket buffer sizing should consider bandwidth-delay product. | supported | SRC-02-006, SRC-02-008 | Keep as mechanism; values should be derived per link/workload. |
| CL-02-010 | CursiveOS should standardize globally on BBRv3. | unverified / too strong | SRC-02-006, SRC-02-007 | Better wording: evaluate BBR/BBRv3 where kernel support and workload fit; do not universalize. |
| CL-02-011 | Intel Arc sysfs frequency/power claims are validated by Chapter 02 alone. | unverified here | Chapters 04 and 09 | Defer to GPU/local-agent validation. |
| CL-02-012 | C-state tuning improves latency but raises power use. | plausible / needs target testing | source extraction pending | Good benchmark candidate; do not promote universal C-state disablement. |

## Required Corpus Changes

- Date every market number.
- Separate market positioning from technical tuning recommendations.
- Defer Intel Arc and GPU-driver claims to Chapters 04 and 09.
- Defer AI-guided tuning claims to Chapter 05.
- Replace universal networking prescriptions with evaluated options.
- Add a current market appendix only when building an external pitch or roadmap.

## Implications for CursiveOS

Chapter 02 should be used as a strategic framing document, not an operational source. Its strongest validated insight is that CursiveOS should not position itself only as a mining optimizer. The stronger positioning is:

```text
Linux optimization layer for latency-, power-, and throughput-sensitive decentralized compute and local AI infrastructure.
```

That positioning survives even if mining margins, Bittensor subnet counts, or token prices change.

## Follow-up

- Extract original sources for KconfigTune, AlphaEvolve, BBR benchmark numbers, C-state latency numbers, and Intel Arc claims.
- Add current mining dashboard sources if market positioning work continues.
- Create a decision record on whether CursiveOS prioritizes miners, DePIN operators, local AI home-rack users, or all three in sequence.
