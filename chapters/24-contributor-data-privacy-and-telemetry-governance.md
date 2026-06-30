## Corpus status (living layer)

**Last reconciled:** 2026-06-26
**Confidence:** **Supported** as a research direction (a contributor network that pays for on-host measurement needs an explicit data-governance posture, and on-device aggregation is the defensible default); **Unvalidated** as a deployed pipeline (no consent flow, minimisation schema, or local-DP/federated-analytics implementation exists yet); the **re-identification risk of the hardware fingerprint** (Ch11) is **Supported** against the device-fingerprinting record
**Read with:** [Chapter 08](08-population-confirmation-and-fleet-statistics.md) (fleet statistics need cross-machine data — the central tension), [Chapter 11](11-hardware-identity-and-anti-spoofing.md) (the fingerprint is a high-entropy identifier by design), [Chapter 02](02-bitcoin-native-economics-and-proof-of-useful-optimization.md) (the BTC wallet links a pseudonymous machine to a financial identity), [Chapter 05](05-measurement-daemon-and-natural-language-shell.md) / [Chapter 06](06-mutation-safety-and-permission-law.md) (what the daemon may read and exfiltrate), [Chapter 00](00-benchmark-schema-and-measurement-validity.md) (the structured-output record that becomes the transmitted payload), [Chapter 16](16-security-and-hardening.md) (host hardening)

### Authoritative for

- The distinction between **what is measured on-host** (Ch00) and **what may leave the contributor's machine**, and why the corpus never drew that line
- The structural conflict between **the central collector** (project operators) and **the contributors it collects from** — the same conflict RAPPOR was built to resolve
- Why the **hardware fingerprint** (Ch11), a deliberately unique key, is also the corpus's largest re-identification surface, and how the **BTC payout** (Ch02) compounds it
- The menu of **privacy-preserving telemetry** techniques (data minimisation, pseudonymisation, local differential privacy, federated analytics) and which ones the Ch08 fleet-statistics model can actually adopt

### Open until experiment/hardware

- A **data-flow inventory**: an enumerated list of every field that leaves the host, its purpose, and its retention — the minimum artifact for a consent notice
- A measured **utility cost of local DP / federated analytics** on the existing fleet-statistics estimators (CV, medians, hardware-scoped fitness) before any privacy mechanism gates the pipeline
- Whether **on-device aggregation** can satisfy the Ch08 N-rule and CV escalation without ever transmitting a raw per-run record

---

## Reinforced research (2026-06-26)

- **Central-collector conflict:** Erlingsson, Pihur, Korolova — "RAPPOR: Randomized Aggregatable Privacy-Preserving Ordinal Response" (ACM CCS 2014, pp. 1054–1067) — crowdsourced statistics where "the only people who could run the database are the developers — the very same people against whom individual responses should be protected." Local differential privacy randomises **on the device** before transmission, so the operator never holds a true per-contributor record.
- **Fingerprint re-identification:** Eckersley — "How Unique Is Your Web Browser?" (PETS 2010, Panopticlick, 470,161 browsers) — 83.6–94.2% of browser fingerprints were unique, carrying **≥18.1 bits of entropy**. The Ch11 fingerprint (CPU model, board, GPU PCI IDs, microcode) is at least as identifying, so an "anonymous" run keyed by it is re-identifiable.
- **Differential privacy without a real budget is theatre:** Tang, Korolova, Bai, Wang, Liu — "Privacy Loss in Apple's Implementation of Differential Privacy on macOS 10.12" (arXiv:1709.02753, 2017) — per-item ε ≈ 1–2 looks safe, but the **budget renews daily** (~16/day), so cumulative leakage grows with every day of opt-in; transparency of the chosen ε is itself a governance requirement.
- **Aggregate without raw exfiltration:** Kairouz et al. — "Advances and Open Problems in Federated Learning" (arXiv:1912.04977, 2021) and Google's Federated Analytics — "each client's raw data is stored locally and not exchanged"; only "focused updates intended for immediate aggregation" leave the device. Maps directly onto Ch08: compute CV/medians/fitness **over** the fleet without ever centralising a per-run row.
- **Legal baseline:** EU GDPR — Art. 4(1) personal data, Art. 4(5) pseudonymisation, Art. 5(1)(c) **data minimisation**, Recital 26 (pseudonymous data is still personal; the test is re-identification *risk*), Art. 6 lawful basis. A paid contributor on identifiable hardware is almost certainly a data subject, not an anonymous node.

# Contributor Data Privacy and Telemetry Governance

Status: First research-synthesis pass (2026-06-26). The corpus has a rigorous
theory of **what to measure** on a contributor's machine (Ch00 schema, Ch01
sensors, Ch08 fleet statistics) and a rigorous theory of **what may mutate** it
(Ch06 permission law), but no theory of **what may leave it**. This chapter
draws that missing line: it argues that a network paying Bitcoin for on-host
measurement is a personal-data processor, not an anonymous mesh; it shows that
the Ch11 fingerprint and the Ch02 payout together make "anonymous telemetry"
false; and it surveys the privacy-preserving aggregation techniques (minimisation,
local DP, federated analytics) that could let the Ch08 statistics survive without
centralising raw per-contributor records.

## Why this chapter exists

CursiveOS runs as an unprivileged daemon on **other people's personal and
business machines** and pays them in BTC for useful optimization (Ch02). Every
existing chapter treats the telemetry as a measurement problem; none treats it as
a *disclosure* problem. Yet the corpus has independently built two facts that make
disclosure unavoidable: Ch11 deliberately constructs a **stable, unique hardware
key** (so confirmations are independent), and Ch02 binds each machine to a **BTC
wallet** (so contributors are paid). A stable unique key plus a financial
identity plus a stream of behavioural telemetry is, under any modern privacy
regime, **identifiable personal data** — not the "anonymous fleet node" the rest
of the corpus tacitly assumes. The project needs a governance layer before it
ships a collector, not after.

| Claim | Status |
| --- | --- |
| The corpus specifies what is measured (Ch00) but never what may be transmitted | **Validated** (no data-flow inventory, consent notice, or minimisation rule anywhere in the corpus) |
| The Ch11 fingerprint makes "anonymous" runs re-identifiable | **Supported** (Eckersley: ≥18 bits for a *browser*; hardware IDs are richer) |
| A central collector is structurally adversarial to the contributors it collects from | **Validated** (RAPPOR's founding premise) |
| Fleet statistics (Ch08) and raw-record privacy are in direct tension | **Validated** (cross-machine estimators need cross-machine data) |
| On-device aggregation can resolve most of that tension | **Supported** (federated analytics; local DP) |

## 1. What actually leaves the machine

The first deliverable is not a technique; it is an **inventory**. Ch00's
structured output — benchmark channels, governor/EPP state, `power_source`,
hardware fingerprint, anomaly flags, wallet — is the literal payload that would be
transmitted, but the corpus never separates "fields the daemon reads to make a
local decision" from "fields the collector needs to see." GDPR Art. 5(1)(c) frames
the question precisely: data must be *adequate, relevant, and limited to what is
necessary*. Each transmitted field must justify itself against a purpose.

| Field class (from Ch00/Ch11/Ch02) | Plausible collector purpose | Minimisation move |
| --- | --- | --- |
| Benchmark deltas (cold-start, sustained, net) | fleet fitness, confirmation | transmit **bucketed/aggregated**, not raw per-run |
| Hardware fingerprint (CPU/board/GPU/microcode) | independence (Ch08), hardware-scoping | transmit a **salted hardware-*class*** token, not the raw key |
| Governor/EPP/kernel/config state | confound control, reproducibility | needed; low identifiability alone |
| `power_source` / energy domain (Ch23) | perf/watt comparability | needed; low identifiability |
| BTC wallet / payout address (Ch02) | payment | the **strongest linker**; segregate from telemetry store |

The point of the table is that most fitness-relevant signal is **aggregate** and
most identifying signal is **incidental** to the measurement — exactly the
profile that minimisation and on-device aggregation are designed for.

| Claim | Status |
| --- | --- |
| A field-by-field data-flow inventory is the prerequisite artifact | **Supported** (GDPR Art. 5/30 framing) |
| Most fitness signal is aggregate; most identifying signal is incidental | **Supported** (Ch00/Ch08 estimators are population-level) |

## 2. The re-identification surface the corpus already built

Ch11 §6 notes "re-identification from hash alone low risk for coarse fields" and
labels it **Partly Supported** — but that judgement was made for the *anti-spoofing*
goal, not the *privacy* goal, and it predates the payout linkage. Eckersley's
Panopticlick result is the calibration: a *browser*, exposing far less than a
host, already yields ≥18.1 bits of entropy and is unique 83.6–94.2% of the time.
A fingerprint built from CPU model, motherboard, GPU PCI IDs, and microcode is a
**stronger** identifier, and Ch08 *wants* it to be — independence requires
distinctness. Privacy and population-confirmation therefore pull in opposite
directions on the very same field. The resolution is not to weaken the local key
but to transmit a **derived, salted hardware-class token** for fleet use while the
raw key stays on-device, so the collector can scope fitness by hardware class
(Ch08 §5) without holding a fleet-wide re-identification index.

| Claim | Status |
| --- | --- |
| The fingerprint is a high-entropy re-identifier, not a coarse field | **Supported** (Eckersley; hardware IDs ⊃ browser IDs) |
| Independence (Ch08/Ch11) and privacy pull on the same field oppositely | **Validated** (distinctness is required *and* dangerous) |
| Transmitting a salted hardware-*class* token preserves scoping without the index | **Supported** (pseudonymisation, GDPR Art. 4(5)) |

## 3. Privacy-preserving telemetry: the menu, and what Ch08 can use

| Technique | What it gives | Cost / caveat | Fit for CursiveOS |
| --- | --- | --- | --- |
| **Data minimisation** (Art. 5) | transmit fewer/coarser fields | none; pure win | adopt first — bucket deltas, drop raw rows |
| **Pseudonymisation** (Art. 4(5)) | salted class token vs raw key | still personal data; re-link possible | adopt for the fingerprint (§2) |
| **Local differential privacy** (RAPPOR) | per-device randomisation; operator never sees true value | needs large N; **budget must not silently renew** (Tang et al.) | candidate for opt-in usage/feature stats, not per-run fitness |
| **Federated analytics** (Kairouz) | aggregate estimators with raw data staying on-device | infra complexity; secure aggregation needed | best structural fit for Ch08 CV/medians |
| **Central plaintext collection** | trivial estimators | maximal disclosure; RAPPOR's anti-pattern | the default to avoid |

The Ch08 statistics the project actually needs — within-machine CV, cross-machine
medians, hardware-scoped fitness, the N-rule — are **population aggregates**. That
is precisely the class federated analytics was built to compute "without raw data
leaving the device." Local DP fits the looser questions (how many machines run
config X, feature-adoption counts) where N is large and per-record truth is
unnecessary. The Tang et al. finding is the governance guardrail: a privacy budget
that **renews each day** leaks cumulatively (~16/day in Apple's case), so any DP
deployment must publish ε, account it **globally and non-renewing per contributor**,
and treat the chosen ε as an auditable parameter, not an implementation detail.

| Claim | Status |
| --- | --- |
| Ch08's estimators are aggregates suited to federated analytics | **Supported** (population-level by construction) |
| Local DP fits coarse high-N counts, not per-run fitness | **Supported** (RAPPOR utility regime) |
| A renewing DP budget defeats the guarantee | **Validated** (Tang et al., arXiv:1709.02753) |

## 4. As a CursiveOS governance layer

| Design choice | Recommendation | Status |
| --- | --- | --- |
| Ship a transmitted-field inventory + retention before any collector | yes — prerequisite | **Unvalidated** (not built) |
| Default to on-device aggregation; transmit aggregates, not raw runs | yes | **Supported** (federated analytics) |
| Segregate the BTC payout store from the telemetry store | yes — break the strongest linker | **Supported** (Ch02 linkage risk) |
| Transmit a salted hardware-*class* token, keep raw fingerprint local | yes | **Supported** (§2) |
| Make participation opt-in with a plain-language data notice | yes — paid contributor = data subject | **Supported** (GDPR Art. 6) |
| Use local DP for per-run fitness | no — N too small, fitness needs the true delta | **Unvalidated** |
| Publish and globally account the DP ε if DP is used at all | yes | **Validated** (Tang et al.) |

The honest near-term posture mirrors Ch23's stance on energy: the *direction* is
defensible and should shape the schema now (minimise, segregate, aggregate
on-device), but no privacy mechanism should gate the pipeline until its **utility
cost on the Ch08 estimators is measured** — a DP/federated estimator that inflates
the CV past the Ch08 0.15 gate would trade a real measurement capability for a
privacy property the network might achieve more cheaply by minimisation alone.

## 5. Open research gaps / experiments

1. **Data-flow inventory:** enumerate every field in the Ch00 transmitted payload,
   its purpose, identifiability, and retention — the minimum artifact for a consent
   notice and for Ch06's exfiltration boundary.
2. **Federated-analytics utility test:** reproduce the Ch08 CV/median/fitness
   estimators under secure aggregation on ≥2 tester machines; measure the accuracy
   loss vs centralised plaintext before adopting.
3. **Salted hardware-class token:** design and test a derived token that preserves
   Ch08 hardware-scoping and Ch11 independence inputs without a fleet-wide
   re-identification index.
4. **Payout/telemetry segregation:** specify the store boundary that keeps the
   Ch02 wallet from linking to the per-machine telemetry record.
5. **DP budget accounting (if DP is used):** a global, non-renewing per-contributor
   ε ledger, with the Tang et al. failure mode as the explicit anti-pattern.

## 6. Citations

| Source | Contribution |
| --- | --- |
| Erlingsson, Pihur, Korolova — "RAPPOR" (ACM CCS 2014) | local DP for crowdsourced stats; the central-collector conflict |
| Eckersley — "How Unique Is Your Web Browser?" (PETS 2010, Panopticlick) | ≥18.1 bits of fingerprint entropy; 83.6–94.2% unique → re-identification |
| Tang, Korolova, Bai, Wang, Liu — "Privacy Loss in Apple's Implementation of Differential Privacy" (arXiv:1709.02753, 2017) | per-item vs cumulative ε; renewing budget leaks; ε transparency |
| Kairouz et al. — "Advances and Open Problems in Federated Learning" (arXiv:1912.04977, 2021); Google Federated Analytics | aggregate estimators with raw data staying on-device |
| EU GDPR — Art. 4(1)/4(5)/5(1)(c)/6, Recital 26 | personal data, pseudonymisation, data minimisation, lawful basis, re-identification test |
| Chapter 00 §3; Chapter 08 §5; Chapter 11 §6; Chapter 02 | the transmitted payload, fleet estimators, fingerprint re-identification note, wallet linkage |

## Research questions answered

| Question | Answer |
| --- | --- |
| Does the corpus say what may leave a contributor's machine? | No — it specifies measurement, not disclosure (**Validated** gap) |
| Are "anonymous" fleet runs actually anonymous? | No — the Ch11 fingerprint plus the Ch02 wallet re-identify them (**Supported**) |
| Can fleet statistics survive without centralising raw records? | Largely yes — they are aggregates suited to federated analytics (**Supported**) |
| Is local DP a drop-in for per-run fitness? | No — N is too small and fitness needs the true delta (**Unvalidated**) |
| What is the safe default posture now? | Minimise, segregate payout from telemetry, aggregate on-device; measure utility cost before any mechanism gates the pipeline (**Supported**) |
