# Chapter 02 Selected Sources

Date extracted: 2026-05-26  
Agent / reviewer: GPT-5.5 Thinking / ChatGPT  
Chapter: `chapters/02-market-and-viability.md`  
Status: Selected high-priority extraction only. Full source extraction remains open.

## Purpose

This file captures the first selected source extraction for Chapter 02. The chapter contains many time-sensitive market and protocol claims, so sources should be refreshed before public use.

## Selected Sources

| Source ID | Title | Author / Organization | URL / DOI / Repo | Source Type | Date Published / Updated | Date Accessed | Used In | Claims Supported | Reliability Tier | Validation Status | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-02-001 | Bitcoin mining overview and difficulty mechanics | Investopedia | https://www.investopedia.com/terms/b/bitcoin-mining.asp | financial education / secondary | rolling | 2026-05-26 | Bitcoin mining context | Supports basic mining mechanics, ASIC dominance, 3.125 BTC post-2024 block subsidy, and 2,016-block difficulty adjustment | C | partially verified | Good for general explanation only; use network dashboards for current hashrate/difficulty. |
| SRC-02-002 | Bitcoin network has first quarterly hashrate drop since 2020 | Tom's Hardware | https://www.tomshardware.com/tech-industry/cryptomining/iran-conflict-forces-bitcoin-mining-operators-to-pivot-to-ai-infrastructure-btc-network-sees-the-first-quarterly-hashrate-drop-since-2020 | news/reporting | 2026-03-31 | 2026-05-26 | Miner-to-AI/HPC pivot context | Supports reported Q1 2026 hashrate drop and miner pivot toward AI/HPC infrastructure | C | partially verified | Useful market signal, not a primary dataset. Cross-check with Hashrate Index/CoinShares/financial reports. |
| SRC-02-003 | Bitcoin miners, now AI compute leaders, face profitability concerns | Investor's Business Daily / CoinShares reporting | https://www.investors.com/news/bitcoin-miner-profitability-hash-price-q1-2026-ai-pivot-wulf-corz-cifr-hut/ | news/reporting | 2026-03-26 | 2026-05-26 | Miner profitability and AI pivot | Supports hashprice stress, production-cost pressure, and listed miners pivoting to AI/HPC | C | partially verified | Useful for positioning; requires primary CoinShares/public company filings for decision-grade use. |
| SRC-02-004 | Expected Revenue, Risk, and Grid Impact of Bitcoin Mining | Cai et al. / arXiv | https://arxiv.org/abs/2512.20518 | paper/preprint | 2025-12-23 | 2026-05-26 | Mining economics framework | Supports first-principles model of mining expected revenue, risk, and profit probability from difficulty/hash trials | B | partially verified | Useful for modeling, not current market numbers. |
| SRC-02-005 | Bitcoin Under Stress: Measuring Infrastructure Resilience 2014-2025 | Wu and Neumueller / arXiv | https://arxiv.org/abs/2602.14372 | paper/preprint | 2026-02-16 | 2026-05-26 | P2P infrastructure / network resilience | Supports claim that Bitcoin and decentralized infrastructure depend on physical network topology and resilience | B | partially verified | Relevant context for network-latency claims; not specific to TAO/Bittensor. |
| SRC-02-006 | IP Sysctl | Linux Kernel Documentation | https://www.kernel.org/doc/html/latest/networking/ip-sysctl.html | primary documentation | rolling kernel docs | 2026-05-26 | TCP/socket/network tuning section | Supports existence and semantics of TCP congestion-control and networking sysctls | A | verified for mechanism | Does not validate exact CursiveOS values or performance uplift. |
| SRC-02-007 | BBR FAQ | Google BBR GitHub repository | https://github.com/google/bbr/blob/master/Documentation/bbr-faq.md | project documentation | rolling | 2026-05-26 | BBR section | Supports BBR as model-based congestion control and documents deployment caveats | A/B | needs verification | Use with kernel availability checks. Does not validate imported extreme speedup numbers. |
| SRC-02-008 | BBR: Congestion-Based Congestion Control | ACM Queue | https://queue.acm.org/detail.cfm?id=3022184 | technical article | 2016 | 2026-05-26 | BBR theory | Supports BBR design rationale: model bottleneck bandwidth and RTT rather than loss-only control | B | verified for background | Older but foundational; not BBRv3-specific. |
| SRC-02-009 | Helium Network Token | Helium Documentation | https://docs.helium.com/tokens/hnt-token/ | official protocol docs | 2026 page | 2026-05-26 | DePIN economics overlap | Supports Helium HNT, Data Credits, burn-and-mint, max supply schedule, and net emissions | A | verified | More relevant to Chapter 07 but useful market context. |
| SRC-02-010 | Data Credit | Helium Documentation | https://docs.helium.com/tokens/data-credit/ | official protocol docs | 2026 page | 2026-05-26 | DePIN economics overlap | Supports Data Credit USD peg, DC usage, HNT-to-DC conversion, and non-transferability | A | verified | More relevant to Chapter 07 but supports DePIN pricing conclusions. |

## Validation Caveats

- Chapter 02 should not use any single news article as decision-grade evidence.
- Market figures should always include exact date, data source, and measurement method.
- Technical network tuning claims should be separated from market positioning claims.
- Intel Arc and GPU claims should defer to Chapters 04 and 09.
