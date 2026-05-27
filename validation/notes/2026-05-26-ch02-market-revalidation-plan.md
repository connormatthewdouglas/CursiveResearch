# Revalidation Plan: Chapter 02 Market and Viability

Date created: 2026-05-26
Agent / reviewer: GPT-5.5 Thinking / ChatGPT
Scope: `chapters/02-market-and-viability.md`
Status: revalidation required before use

## Why This Chapter Needs Revalidation

Chapter 02 contains highly time-sensitive claims about Bitcoin mining difficulty, network hash rate, ASIC efficiency, Bittensor subnet status, DePIN market conditions, BBR performance, Intel Arc driver behavior, and profitability logic. These claims can become stale quickly and should not be used in external materials or roadmap decisions without fresh sources.

## Claims to Revalidate

| Claim Group | Required Source Type | Notes |
| --- | --- | --- |
| Bitcoin network hash rate and difficulty | Mining data dashboards / Bitcoin network data | Use dated values only. |
| ASIC efficiency comparisons | Manufacturer specs and independent reviews | Avoid using rumored models or stale hardware names. |
| Bittensor active subnet count and reward mechanics | Official Bittensor docs / chain data / governance docs | Chapter numbers may now be stale. |
| io.net and DePIN project status | Official docs, dashboards, governance posts | Check operational status, not just marketing. |
| BBR/BBRv3 claims | Linux kernel/networking docs, Google BBR docs, papers | Separate BBRv1/v2/v3 and kernel availability. |
| Socket buffer defaults and BDP recommendations | Linux docs, distro defaults, controlled benchmarks | Use current distro defaults. |
| Intel Arc sysfs and driver claims | Intel docs, Linux kernel/Mesa docs, local hardware probe | Link to Chapter 09 and Chapter 04 validation. |
| C-state latency and power tradeoffs | CPU vendor docs and local benchmarks | Do not generalize across platforms. |
| Profitability conclusions | Current token prices, electricity assumptions, hardware costs | Always date assumptions. |

## Minimum Revalidation Output

1. Extract official/current sources into `sources/extracted-source-index.md` as `SRC-02-*`.
2. Mark each market number with date checked.
3. Split durable architecture claims from volatile market claims.
4. Add a validation note with supported, stale, disputed, and unverified claim groups.
5. Produce a short decision memo: whether CursiveOS should still prioritize miners, DePIN operators, local agents, or home-rack AI compute first.

## Recommendation

Do not use Chapter 02 as current truth. Treat it as a research backlog for market positioning and viability until fresh data is collected.
