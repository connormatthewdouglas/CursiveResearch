## Corpus status (living layer)

**Last reconciled:** 2026-06-24
**Confidence:** Partly Supported — rule structure from main repo (Ch01); per-channel CV behavior **Validated** on one machine (Ch00 §5 item 7); fleet-scale calibration **Unvalidated**
**Read with:** [Chapter 01](01-seed-organism-and-sensor-array.md) (N-rule, CV threshold, independence), [Chapter 00](00-benchmark-schema-and-measurement-validity.md) (noise floor, per-channel CV), [Chapter 02](02-bitcoin-native-economics-and-proof-of-useful-optimization.md) (fitness gates payouts), [Chapter 11](11-hardware-identity-and-anti-spoofing.md) (independence inputs)

### Authoritative for

- Formalizing population confirmation as a statistical decision problem, not a vote
- Per-channel confirmation escalation keyed to measured CV
- Hardware-scoped fitness as the fleet analogue of subgroup analysis

### Superseded or narrowed

- Treating a single global N across all sensor channels — Ch00 noise floor argues against this (**Supported**)
- Using CV ≤ 0.15 as a calibrated constant before variance-bearing detail bundles ship fleet-wide (**Unvalidated**)

### Open until experiment/hardware

- Multi-machine calibration of N-rule and CV thresholds
- Immune-sensor prototypes for correlated confirmations (Ch01 backlog)
- Sequential testing policy for candidate screens (this chapter proposes; not implemented)

---


## Reinforced research (2026-06-24)

- Corpus reorganized to strategic order 00-22; see [INDEX.md](../INDEX.md).
- Paper library: **25** peer intakes in papers/ (extraction-only unless rights-cleared).
- Credible external sources: Linux kernel docs, arXiv 2024-2026 preprints, DMTF/UEFI/Red Hat/ESnet where applicable â€” details in chapter body and sources/.

# Population Confirmation and Fleet Statistics

Status: First research-synthesis pass (2026-06-24). Grounds Chapter 01's
population-confirmation architecture in fleet-variance evidence from Chapter 00
and in standard statistical practice for multiple comparisons and sequential
decision-making.
Use it for: designing CursiveRoot acceptance logic, calibrating confirmation
counts, and avoiding false fleet truth as the tester pool grows.

## Why this chapter exists

Chapter 01 specifies *what* must be confirmed before a local measurement becomes
fleet truth: independent machines, wallets, anomaly profiles, an N-confirmation
rule, and CV-based escalation. Chapter 00 supplies the first empirical variance
data — and immediately complicates the story: channels differ radically in
repeatability. The corpus lacked a statistical layer connecting those pieces:
how many confirmations, for which channel, under what independence assumptions,
without drowning in false positives as the organism tests many candidates.

This chapter is that layer. It is not a governance proposal. It is a measurement
statistics specification for a sensor-driven organism.

## 1. The confirmation problem in one sentence

A candidate variant should be promoted only when enough **independent** hosts
produce **consistent signed deltas** on **valid sensors**, with **variance-aware**
confidence — not when one loud machine or one high-variance channel declares victory.

| Concept | Chapter 01 term | Statistical analogue |
| --- | --- | --- |
| Independent host | distinct fingerprint + wallet + anomaly profile | independent strata / blocking factor |
| Repeat measurement | counterbalanced paired runs | paired comparison / crossover design |
| Fleet agreement | N confirmations | replication count / meta-analytic consensus |
| Noisy channel | CV > 0.15 → N+2 | heterogeneity triggers more data |
| Bad global win | hardware compatibility gate | subgroup / scope restriction |

## 2. The N-confirmation rule (specified vs calibrated)

Chapter 01 defines:

```text
N = max(1, min(5, floor(sqrt(fleet_size))))
if CV > 0.15: required_confirmations = N + 2
```

Where `fleet_size` is active testers in the last 30 days.

| Claim | Status | Notes |
| --- | --- | --- |
| N grows sublinearly with fleet size, capped at 5 | **Supported** | Main-repo sensor-array spec; practical bootstrap during Phase 0 (N=1) |
| sqrt scaling balances cost vs coverage | **Unvalidated** | Reasonable heuristic; no fleet A/B against fixed-N or log-N alternatives |
| CV > 0.15 is the right escalation breakpoint | **Partly Supported** | Network CV 0.192 on Stardust triggered escalation empirically (Ch00); other channels differ |
| One global N for all channels | **Disproven** as default | Ch00 §5 item 7: cold-start CV 0.002 vs network 0.192 vs idle-power artifact |

**CursiveOS implication:** store `required_confirmations` **per channel per hardware class**, not as a single scalar per variant. The formula can remain the baseline; the channel's rolling fleet CV should modulate it.

## 3. Fleet variance: what the first noise floor taught

Chapter 00 measured six identical v0.9 full-tests on one machine (Stardust):

| Channel | Mean delta | Std | CV | Confirmation posture |
| --- | --- | --- | --- | --- |
| Cold-start | −50.8% | 0.1 | **0.002** | ~1 confirmation sufficient on same hardware class |
| Network | 707% | 136 | **0.192** | Escalate; never quote precise magnitude |
| Sustained (single-stream) | −0.45% | 0.51 | sign-unstable | Not selection-grade until benchmark changes |
| Idle power (production path) | 4.02 W | 3.32 | **0.83** | Artifact of post-benchmark sampling; settled probe CV ≈ 0.01 |

| Claim | Status |
| --- | --- |
| Cold-start is the most repeatable selection channel today | **Validated** (2026-06-16, one machine) |
| Network requires CV escalation under current harness | **Validated** (same session) |
| Idle-power CV 0.83 in full-test was sampling artifact | **Validated** (Phase D settled probe) |
| Per-channel confirmation counts beat one global N | **Supported** (Ch00 inference; not yet implemented in hub) |

**CursiveOS implication:** the analyzer should compute rolling per-channel CV from `run_detail_bundles` variance, not from collapsed `runs` scalars. Until detail bundles ship on every run, CV-based escalation is under-informed (**Unvalidated** at fleet scale).

## 4. Hardware-scoped fitness

Chapter 01's hardware compatibility gate becomes statistically concrete when the
fleet is heterogeneous:

| Observation | Hardware scope | Action |
| --- | --- | --- |
| Desktop Arc −51% cold-start | `3e6b165ddf112a75` class | Promote cold-start benefit as **scoped**, not universal |
| Laptop i5-11300H ~0% same presets | `42e7c7257af11f46` class | Do not pool with desktop cohort |
| v0.9c ≡ v0.8 on both for cold-start | global parent replacement | Safe merge; benefit label stays scoped |

This is subgroup analysis without a human committee: if effect sign or magnitude
differs materially across fingerprint clusters, the variant earns fitness only in
the clusters where regression gates pass and confirmation completes.

| Claim | Status |
| --- | --- |
| Same preset can be globally safe but locally beneficial | **Validated** (v0.9c screen, two machines) |
| Pooling heterogeneous hardware inflates false discovery | **Supported** (standard stats + Ch00 laptop/desktop split) |
| Automatic cluster definition from fingerprint v2 | **Unvalidated** | Needs clustering policy + minimum cluster size |

## 5. Independence, immune sensors, and correlated "distinct" hosts

Chapter 01 requires distinct fingerprints, wallets, and anomaly profiles. Immune
sensors exist to collapse suspiciously correlated confirmations into one effective
source.

| Threat | Immune signal | Statistical failure mode |
| --- | --- | --- |
| VM farm with cloned SMBIOS | fingerprint collision / implausible diversity | pseudo-replication |
| Wallet splitting | shared payout graph | inflated effective N |
| Coordinated preset timing | synchronized deltas across hosts | unmodeled correlation |
| Goodhart on one channel | network-weighted fitness | proxy hacking (Ch00 §4, Skalse et al.) |

| Claim | Status |
| --- | --- |
| Independence is necessary for N to mean "replications" | **Supported** |
| Immune sensors can enforce effective-N downgrade | **Unvalidated** (planned, not deployed) |
| Wallet + fingerprint independence is sufficient | **Unvalidated** | Sybil economics need Ch02 + Ch21 |

**CursiveOS implication:** CursiveRoot should store `effective_confirmations` alongside raw confirmations when immune sensors fire, analogous to down-weighting correlated studies in meta-analysis.

## 6. Multiple comparisons: many candidates, many sensors

Every cycle the organism risks testing many variants across many channels. That
is a **multiple comparisons** problem: if each test uses α = 0.05 independently,
false wins accumulate.

Standard mitigations (not yet wired into CursiveOS):

| Method | Role for CursiveOS | Citation anchor |
| --- | --- | --- |
| Benjamini–Hochberg FDR | control expected fraction of false discoveries across active screens | Benjamini & Hochberg, *JRSS-B*, 1995 |
| Family-wise error (Bonferroni / Holm) | conservative gate when a false merge is costly | Holm, *Scand J Stat*, 1979 |
| Pre-registration of primary endpoints | genesis sensor suite as declared primary channels | clinical-trials analogue; reduces p-hacking surface |
| Hierarchical testing | regression gates first, performance second | aligns with Ch01 sensor families |

| Claim | Status |
| --- | --- |
| Uncorrected per-candidate testing will eventually accept noise | **Supported** (statistical theory + Ch00 sustained channel) |
| FDR control should apply at the **variant × channel × hardware-class** family | **Unvalidated** | Design recommendation |
| Regression gates reduce but do not eliminate multiplicity | **Supported** |

**CursiveOS implication:** the hub analyzer should log an explicit **comparison family** per acceptance decision so later audits can apply FDR or Holm retroactively during calibration.

## 7. Sequential testing and early stopping

Contributors naturally want to stop testing once a delta "looks good." That is
sequential analysis. Naive peeking inflates false positives unless the design
accounts for repeated looks.

| Approach | Fit for CursiveOS | Status |
| --- | --- | --- |
| Fixed plan: counterbalanced repeats, predeclared N | matches current paired benchmark ethos | **Supported** (Ch01/00) |
| SPRT / sequential probability ratio | efficient but needs effect-size priors per channel | **Unvalidated** |
| Alpha spending (Lan–DeMets) | if hub allows adaptive "one more machine" | **Unvalidated** |
| Always-invalid: stop when p < 0.05 on any peek | reject for acceptance | **Supported** |

Practical rule for Phase 0–1:

```text
declare channel + hardware class + minimum runs up front
-> complete counterbalanced pairs per host
-> only then evaluate against confirmation counter
-> optional "one more host" uses pre-registered escalation (CV or immune), not discretionary peeking
```

## 8. CV as heterogeneity gauge, not a p-value

Coefficient of variation (CV = σ/μ) is used in Chapter 01 as a cheap
heterogeneity trigger. It is not a hypothesis test.

| Strength | Limitation |
| --- | --- |
| scale-free across magnitude | unstable when μ ≈ 0 (sustained near-zero deltas) |
| easy to compute from per-pass arrays | confounded if σ mixes noise types (Ch00 order/cache) |
| interpretable for operators | threshold 0.15 is a starting constant, not derived |

| Claim | Status |
| --- | --- |
| CV > 0.15 usefully flagged network on Stardust | **Validated** |
| CV alone should gate acceptance without confidence intervals | **Unvalidated** | Prefer CI on paired delta + CV escalation |
| Log-scale or robust dispersion needed for ratio-like network deltas | **Unvalidated** | Open methods gap |

## 9. CursiveOS implications (implementation checklist)

1. **Per-channel confirmation state** in CursiveRoot: `required`, `raw`, `effective`, `cv_rolling`, `hardware_class`.
2. **Variance-bearing uploads** on every run (Ch00 §3 item 2) before fleet CV calibration.
3. **Hardware-scoped promotion labels** on any variant whose benefit is class-specific.
4. **Comparison-family metadata** for FDR/Holm audits as candidate volume grows.
5. **Immune-sensor downgrade** of effective N when correlation detected.
6. **Do not gate** on sustained single-stream or mishandled idle power until Ch00 fixes are validated in production path across machines.

## 10. Open research gaps

1. Calibrate sqrt-N rule against 3+ independent machines with ground-truth variants.
2. Derive channel-specific CV breakpoints from fleet data, not a single 0.15.
3. Specify minimum hardware-class sample size before scoped promotion.
4. Implement immune-sensor correlation graph → effective N.
5. Choose FDR vs Holm policy for multi-variant cycles and document α.
6. Run cold-start counterbalance experiment (Ch00 §5 item 9) before treating magnitude as fleet-confirmed.

## 11. Citations and source anchors

| Source | Use in this chapter |
| --- | --- |
| Main `CursiveOS` `docs/architecture/sensor-array.md` | N-rule, CV escalation, independence |
| Chapter 01 / 16 | Architecture + noise floor |
| Benjamini & Hochberg (1995) | FDR control across screens |
| Holm (1979) | Step-down FWER |
| Lan & DeMets (1983) | alpha spending for sequential looks |
| Skalse et al., NeurIPS 2022 (Ch00 §4.1) | proxy/fitness hacking theory |
| Wasserstein & Lazar (2016) ASA statement | avoid mechanical p < 0.05 without context |

## Research questions answered

| Question | Answer |
| --- | --- |
| What does N mean? | Independent hardware confirmations per channel/class, not votes |
| Is CV ≤ 0.15 final? | No — starting heuristic; channel-specific calibration required |
| Can one machine confirm cold-start today? | On Arc desktop class, yes for repeatability; fleet independence still needed |
| How avoid false wins with many tests? | Predeclare families; regression first; FDR/Holm; no discretionary peeking |