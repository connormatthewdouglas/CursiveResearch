# Revalidation Plan: Chapter 07 Tokenomics and Incentives

Date created: 2026-05-26
Agent / reviewer: GPT-5.5 Thinking / ChatGPT
Scope: `chapters/07-tokenomics-and-incentives.md`
Status: protocol-level revalidation required before use

## Why This Chapter Needs Revalidation

Chapter 07 is strategically useful but not decision-grade. Tokenomics change through governance proposals, emissions schedules, burns, token migrations, oracle mechanics, and project revenue. The chapter uses numbered citations that need to be resolved into canonical protocol docs, governance proposals, dashboards, and current data.

## Protocols / Models to Revalidate

| Protocol / Project | Claims to Verify | Preferred Sources |
| --- | --- | --- |
| Helium | Data Credits, burn-and-mint, HNT emissions, net emissions, subscriber revenue burn policy | Helium docs, HIPs, dashboards, treasury/burn data |
| Render | Burn-and-Mint Equilibrium, RNP-006/RNP-018, emissions schedule, job-payment burns | Render docs, RNPs, on-chain data, governance forum |
| io.net | Incentive Dynamic Engine, USD-denominated rewards, burn percentage, supplier payout mechanics | io.net docs, token docs, governance, dashboards |
| Bittensor | TAO emissions, subnet alpha mechanics, flow-based emissions/Taoflow, subnet caps, YC3, commit-reveal | Bittensor docs, chain data, governance posts, subnet docs |
| Hivemapper | HONEY burn/mint, MIP-15, weekly emissions, consumption rewards | Hivemapper docs, MIPs, dashboards |
| Grass | contributor economics, airdrop mechanics, bandwidth marketplace demand | Grass docs, token docs, dashboard if available |
| Newer DePINs | newer incentive models after original import | official docs and credible analysis |

## Design Questions for CursiveOS

Before making a token/economic design decision, separate these questions:

1. What should customers pay in: fiat, stable credits, native token, or hybrid?
2. What should contributors receive: cash/stable, native token, points, allocation rights, or hybrid?
3. What is the emissions budget and cap?
4. What makes rewards demand-linked instead of pure inflation?
5. How are benchmark submissions verified and anti-gamed?
6. How do we prevent Sybil/fake benchmark spam?
7. How are early contributors rewarded before a token launch?
8. What non-token incentive alternatives exist?

## Minimum Revalidation Output

1. Extract official protocol sources as `SRC-07-*` records.
2. Resolve numbered citations in Chapter 07.
3. Mark each protocol claim as current, stale, disputed, or unverified.
4. Create a comparison table separating customer pricing, contributor payouts, burn mechanics, emissions, and anti-gaming.
5. Create a CursiveOS decision record only after protocol facts are verified.

## Provisional Takeaway

The broad strategic direction remains plausible: avoid pure inflation, tie rewards to verified value, consider stable/user-friendly pricing, and ensure contributor rewards do not exceed real demand forever. But no CursiveOS tokenomics decision should be made from Chapter 07 until current protocol sources are checked.
