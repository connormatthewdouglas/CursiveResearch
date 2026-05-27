# Chapter 07 Selected Sources

Date extracted: 2026-05-26  
Agent / reviewer: GPT-5.5 Thinking / ChatGPT  
Chapter: `chapters/07-tokenomics-and-incentives.md`  
Status: Selected high-priority extraction only. Full citation resolution remains open.

## Purpose

This file captures the first protocol-source extraction for Chapter 07. Tokenomics claims should be based on official docs, governance proposals, and current dashboards wherever possible.

## Selected Sources

| Source ID | Title | Author / Organization | URL / DOI / Repo | Source Type | Date Published / Updated | Date Accessed | Used In | Claims Supported | Reliability Tier | Validation Status | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-07-001 | Helium Network Token | Helium Documentation | https://docs.helium.com/tokens/hnt-token/ | official protocol docs | 2026 page | 2026-05-26 | Helium section | Supports HNT, burn-and-mint equilibrium, max supply, halving schedule, and net emissions | A | verified | Good protocol source. Refresh before economic decisions. |
| SRC-07-002 | Data Credit | Helium Documentation | https://docs.helium.com/tokens/data-credit/ | official protocol docs | 2026 page | 2026-05-26 | Helium section | Supports Data Credits as non-transferable USD-pegged usage credits created by burning HNT | A | verified | Good support for stable customer pricing model. |
| SRC-07-003 | Render Network Tokenomics | Render Knowledge Base | https://know.rendernetwork.com/the-render-network/tokenomics | official/project docs | rolling | 2026-05-26 | Render section | Supports Render tokenomics overview, burn-and-mint equilibrium framing, and user/job payment mechanics | A/B | needs verification | Need governance-source cross-check for exact emission parameters. |
| SRC-07-004 | Render Network RNPs repository | Render Network / GitHub | https://github.com/rendernetwork/RNPs | official governance repo | rolling | 2026-05-26 | Render section | Governance source for Render proposals including RNP-006/RNP-018 when available | A | needs verification | Need exact proposal file extraction before validating emission amounts. |
| SRC-07-005 | Bittensor Dynamic TAO | Bittensor Documentation | https://docs.bittensor.com/learn/dynamic-tao | official protocol docs | rolling | 2026-05-26 | Bittensor section | Supports Dynamic TAO/dTAO concepts, subnet market mechanics, and flow/value allocation concepts | A | needs verification | Need exact docs fetch/line validation later. |
| SRC-07-006 | Bittensor Emissions | Bittensor Documentation | https://docs.bittensor.com/learn/emissions | official protocol docs | rolling | 2026-05-26 | Bittensor section | Supports Bittensor emissions model and subnet incentive mechanics | A | needs verification | Need exact current emission schedule and YC3/current rules check. |
| SRC-07-007 | io.net tokenomics / IO token docs | io.net Documentation | https://docs.io.net/docs/tokenomics | official/project docs | rolling | 2026-05-26 | io.net section | Intended source for IO token, supplier rewards, and burn mechanics | A/B | needs verification | Search/fetch was unreliable in this pass; must verify URL/current docs before relying. |
| SRC-07-008 | Hivemapper HONEY tokenomics | Hivemapper Documentation | https://docs.hivemapper.com/honey-token/honey-tokenomics | official/project docs | rolling | 2026-05-26 | Hivemapper section | Intended source for HONEY tokenomics, burn/mint, and contributor rewards | A/B | needs verification | Must verify exact docs and MIP-15 source before use. |
| SRC-07-009 | Render BME overview and analysis | Render project/community docs | https://rendernetwork.com/ | project docs / project site | rolling | 2026-05-26 | Render section | Project context for Render marketplace and AI/render workloads | B | needs verification | Use only as supporting context; governance docs are stronger. |
| SRC-07-010 | DePIN sustainability analysis | Market/sector analysis sources | pending | secondary analysis | rolling | 2026-05-26 | cross-protocol conclusions | Supports broad claim that pure emissions without demand is fragile | C | not extracted | Needs concrete source resolution from original numbered citations. |

## Validation Caveats

- Official docs validate mechanics, not whether the economics “worked.”
- Current dashboards and on-chain data are needed for burn/revenue/emissions analysis.
- Governance proposals can supersede docs; protocol-specific claims should cite proposal IDs and dates.
- CursiveOS token design should not be finalized from this chapter until anti-gaming and benchmark-verification mechanics are specified.
