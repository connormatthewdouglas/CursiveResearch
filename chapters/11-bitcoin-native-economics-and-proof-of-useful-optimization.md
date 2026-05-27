# Bitcoin-Native Economics and Proof of Useful Optimization

Status: Current project architecture imported from the main `CursiveOS` repo. This chapter supersedes token-first assumptions in the earlier tokenomics research when discussing CursiveOS's own economic design.

## Why this chapter exists

The research corpus previously contained a broad tokenomics chapter comparing DePIN incentive systems. That was useful for learning, but the main CursiveOS repo now contains a more specific and more opinionated economic design: **Layer 5 Economics v3.3**.

The live CursiveOS design is not a token model. It is Bitcoin-native, contributor-fitness-based, and sensor-driven.

This chapter turns that design into corpus guidance.

## Core conclusion

CursiveOS should not launch a custom token by default.

The current architecture uses:

```text
users pay in BTC
-> monthly cycle revenue is split by metabolic sensor
-> contributors are paid in BTC
-> payouts are weighted by measured fitness
-> testers receive Fast tier access, not lifetime revenue
-> no governance token, no voting, no treasury pool
```

This is a major departure from the imported DePIN-tokenomics research. Chapter 07 remains useful for comparison, but CursiveOS's current design should be evaluated as a Bitcoin-native revenue distribution organism, not as another emissions-based DePIN network.

## Layer 5 Summary

The main repo specifies:

| Parameter | Current v3.3 Design |
| --- | --- |
| Base asset | Bitcoin |
| Custom token | None |
| Yield/staking pool | None |
| Revenue distribution | Direct per-cycle distribution |
| User paid tier | Fast tier, target $2/month settled in BTC |
| Free tier | Stable tier |
| Contributor compensation | Current-cycle stream + lifetime stream |
| Tester compensation | Free Fast tier access |
| Tester lifetime fitness | None |
| Governance | None |
| Founder cut | None; founder is paid as normal contributor |
| Claim window | Two years per accrual |
| Fork obligations | Forks inherit ledger obligations if they carry the genome forward |

## Roles

### Users

Users run CursiveOS. Stable tier is free. Fast tier is paid and functions as both revenue and selection signal.

### Testers

Testers provide measurement coverage by running benchmarks on their hardware. They are compensated with Fast tier access, not lifetime revenue share.

This is an important anti-gaming choice: testers produce measurement flow, not durable genome improvements. Paying testers lifetime compensation would make fake measurement farms more dangerous.

### Contributors

Contributors submit variants: code, sensors, presets, benchmark methods, tooling, or other changes. Accepted variants earn lifetime fitness proportional to measured improvement.

A person can be a user, tester, and contributor simultaneously, but the roles are economically distinct.

## Revenue Flow

At each cycle close:

```text
Fast tier revenue R is collected
-> metabolic sensor outputs split s_current and s_lifetime
-> current-cycle stream pays contributors whose variants merged this cycle
-> lifetime stream pays all contributors weighted by cumulative lifetime fitness
-> accruals are recorded against contributor wallets
```

If a cycle has zero revenue, nothing is distributed and no state is affected.

## Fitness Ledger

When a variant is accepted, its measured fitness is recorded in an append-only lifetime ledger.

Fitness is:

- measured by the sensor array;
- weighted by confidence;
- tied to hardware contexts and sensor versions;
- non-negative for merged variants;
- permanent once validly earned.

Superseding a contribution can change what the current genome runs, but it does not erase fitness that was valid when measured.

This is the core of **Proof of Useful Optimization**.

## Proof of Useful Optimization

CursiveOS does not reward raw submissions, benchmark spam, governance participation, token staking, or popularity.

It rewards:

```text
a proposed change
-> measured on real hardware
-> confirmed by sensors
-> passing regression gates
-> producing positive fitness
-> merged into the organism
```

This is the useful-work primitive missing from many DePIN systems. The proof is not “I own hardware” or “I performed a task once.” The proof is “my contribution improved the organism under measurement.”

## Metabolic Sensor

The split between current-cycle and lifetime streams is not fixed and not voted on. It is controlled by a metabolic sensor measuring contributor dynamics.

The main signal is merge velocity stratified by contributor history:

```text
new_weight(n) = 1 / (1 + n)
returning_weight(n) = 1 - new_weight(n)
```

Where `n` is a contributor's prior merge count. First-time contributors count as fully new; established contributors gradually shift toward returning weight.

The ratio of new-weighted to returning-weighted fitness controls whether the organism needs more recruitment or more retention.

Genesis split:

```text
20% current-cycle
80% lifetime
```

This is lifetime-favored because bootstrap work creates long-lived substrate. As new contributors arrive and produce accepted work, the sensor can shift toward current-cycle rewards.

## No Governance

The v3.3 economics design explicitly removes governance.

No voting. No appeals. No contributor legislature. No token-weighted control. No one-person-one-vote fiction.

Merge value is decided by sensors. Economic distribution follows measured fitness.

This is consistent with the biological architecture: organisms do not vote on whether a mutation helped; the environment selects.

## No Pool

Earlier economics explored a staked/yielding pool. The current design removes it.

The reason is important: CursiveOS compounds in substrate, not stored capital.

The compounding assets are:

- CursiveRoot measurement data;
- sensor array coverage;
- accepted presets and code;
- validated hardware/workload knowledge;
- the contributor lifetime ledger.

A treasury pool would add financial machinery and attack surface without improving the organism's actual substrate.

## Fork Obligation Inheritance

Forks are allowed. But a fork that carries forward the CursiveOS genome inherits obligations attached to prior measured contributions.

The ledger is Bitcoin-anchored so a fork cannot invisibly erase who is owed. A fork that honors obligations is legitimate. A fork that repudiates them is visibly parasitic.

This is one of the most distinctive parts of the design and deserves further legal/technical research.

## Relationship to Chapter 07

Chapter 07 remains useful for DePIN comparison, but it no longer describes CursiveOS's preferred design.

The practical update is:

```text
Do not design CursiveOS as a token network unless v3.3 fails under implementation pressure.
Start from Bitcoin-native direct revenue distribution.
Use tokenomics research only as comparison and cautionary material.
```

## Current limits

- v3.3 is specified, not deployed for real payments.
- Phase 0 has no accepted mutation or real payout report yet.
- The metabolic sensor has no meaningful data until there is more than one contributor.
- Fork obligation inheritance needs implementation, wallet binding, and likely legal analysis.
- Fitness scoring must be hardened against benchmark fraud, hardware spoofing, and Goodharting.

## Research questions answered

| Research Question | Current Answer |
| --- | --- |
| Should CursiveOS launch a token? | Not by default. Current design is Bitcoin-native with no custom token. |
| How are contributors paid? | In BTC, from monthly cycle revenue, weighted by measured fitness. |
| How are testers paid? | Fast tier access, not lifetime fitness. |
| What is proof of useful optimization? | Sensor-confirmed, regression-safe, positive-fitness merged contribution. |
| How is governance avoided? | Sensors replace votes and appeals. |
| What compounds? | CursiveRoot, sensors, accepted code, and lifetime fitness ledger — not a treasury pool. |

## Open research gaps

1. Formalize wallet binding and anti-Sybil identity for contributors and testers.
2. Define exact BTC payment and claim mechanics.
3. Implement and simulate the metabolic sensor across artificial contributor histories.
4. Research fork obligation enforcement and legal framing.
5. Add a CursiveOS-specific anti-gaming economics chapter focused on fake benchmark farms and hardware spoofing.

## Source anchors from main CursiveOS repo

- `docs/specs/layer5-economics-v3.3.md` — single source of truth for current economics.
- `white-paper.md` v2.4 — summary of Layer 5 in the technical white paper.
- `docs/architecture/sensor-array.md` — sensor/fitness source for economic distribution.
- `docs/architecture/biological-architecture.md` — rationale for metabolism, substrate compounding, and no-governance design.
