# Experiment Proposal: Does Ch08 Confirmation Actually Tolerate Sabotage?

Date created: 2026-06-26
Linked chapters: `chapters/08-population-confirmation-and-fleet-statistics.md`,
`chapters/03d-verifying-decentralized-computation.md`,
`chapters/03c-alphaevolve-decentralized-evolution-mapping.md`,
`chapters/00-benchmark-schema-and-measurement-validity.md`,
`chapters/11-hardware-identity-and-anti-spoofing.md`,
`chapters/02-bitcoin-native-economics-and-proof-of-useful-optimization.md`
Answers: RESEARCH_PIPELINE §2 P0 Knowledge Gap "How should CursiveOS handle
hardware-scoped truth?" — the remaining "adversarial test of whether Ch08
confirmation behaves as a sabotage-tolerance layer."
Status: Proposed; not yet executed.

## 0. Why this experiment, why now

Chapter 03c names CursiveOS's #1 unsolved frontier in one sentence: the
AlphaEvolve loop is validated, but it assumes a **single trusted evaluator**,
and CursiveOS must replace that evaluator with an **untrusted, noisy,
economically-incentivized, hardware-heterogeneous fleet**. Chapter 03d then
surveys the external prior art and reframes Ch08's N-rule + per-channel CV
escalation + hardware-scoped pooling as CursiveOS's *de facto*
**sabotage-tolerance layer**, giving it a literature lineage (Sarmenta's
credibility-based fault tolerance, FGCS 2002; BOINC's quorum/validator model,
Anderson 2019). Chapter 03d §5 ends with the explicit next move:

> "test whether Ch08's statistical confirmation actually behaves like a
> sabotage-tolerance layer under adversarial, hardware-scoped conditions."

That test does not exist. The twelve plans in `experiments/` are all
physical/hardware-tuning experiments (cold-start, network, memory-pressure,
firmware, GPU). **Not one of them puts an adversary in the loop.** Yet the
moment Layer 5 (Ch02) attaches real BTC to measured fitness, the confirmation
rule stops being a statistics question and becomes a security boundary: a
contributor is now *paid to lie*. Sarmenta's whole field exists because that
incentive is real. The corpus has reasoned about this by analogy (Ch03d §5,
Ch08 §5 immune sensors, the Skalse Goodhart warning) but has **never measured
the rule's actual error rates under attack**.

This is cheap to answer and expensive to leave open. The experiment is a
**simulation/replay** seeded by already-measured corpus constants — no new
hardware, no fleet, no real money at risk. It can run before a single saboteur
ever joins the real fleet, which is exactly when you want the answer.

## 1. Hypotheses (falsifiable)

The rule under test is Chapter 08 §2 as written:

```text
N = max(1, min(5, floor(sqrt(fleet_size))))
if CV > 0.15: required_confirmations = N + 2
promote a variant to fleet truth (per channel, per hardware class) only when
required_confirmations independent hosts produce consistent signed deltas
```

plus the Ch08 §5 immune-sensor option: collapse suspiciously correlated
"distinct" hosts into `effective_confirmations < raw_confirmations`.

**H1 (accept-bad / false promotion).** With the immune-sensor downgrade
**disabled**, there exists a saboteur fleet fraction *f* ≤ 0.34 at which the
Ch08 rule promotes a genuinely inert ("decoy") variant to fleet truth on the
**low-noise cold-start channel** (CV 0.002) at a rate > 5% over repeated cycles.
*(0.34 = the canonical Byzantine one-third; the rule should not fail below it.)*

**H0a (null for H1).** No such *f* ≤ 0.34 exists; the rule holds false promotion
≤ 5% up to a one-third saboteur fraction without immune downgrade.

**H2 (immune-sensor value).** Enabling the Ch08 §5 effective-N downgrade against
a **correlated Sybil cluster** (cloned anomaly profile / synchronized deltas)
reduces the false-promotion rate of H1 by a pre-registered, meaningful margin
(≥ 50% relative reduction at the worst *f* found in H1).

**H3 (high-noise channel is softer).** The same saboteur fraction *f* produces a
**strictly higher** false-promotion rate on the **network channel** (CV 0.192,
which triggers N+2 escalation) than on cold-start — i.e. CV escalation helps but
does not equalize the two channels, because a noisier channel gives a liar more
cover. *(If false, CV escalation is doing more work than expected — also
informative.)*

**H4 (reject-good / false rejection — the other Sarmenta failure).** A saboteur
strategy of reporting fake *null/negative* deltas can suppress a genuinely good,
hardware-scoped variant (the validated desktop cold-start −51% win) below its
promotion threshold at a saboteur fraction *f* ≤ 0.34. *(Sabotage tolerance is
two-sided: a rule that never accepts a lie but is trivially griefed into
rejecting every real win is also broken.)*

## 2. What this experiment is, precisely

A **Monte-Carlo simulation of the Ch08 confirmation rule**, not a hardware run.
Each trial:

1. instantiates a synthetic fleet of `fleet_size` hosts split across ≥2
   hardware classes (desktop Arc-class, laptop i5-class — the two real classes
   in Ch00/Ch08 §4);
2. draws each honest host's per-channel delta from the **empirically measured**
   distributions (see §3), respecting hardware scope (desktop sees −51%
   cold-start, laptop sees ~0%);
3. injects a saboteur fraction *f* using one of the attack models in §4;
4. runs the exact Ch08 promotion rule (per channel, per hardware class, with N,
   CV escalation, and optional effective-N downgrade);
5. records whether the rule's verdict matches ground truth (the variant is
   inert by construction for H1–H3, genuinely good for H4).

Sweep *f* ∈ {0, 0.05, 0.10, …, 0.50} and `fleet_size` ∈ {4, 9, 16, 25, 100}
(the N-rule's `floor(sqrt)` breakpoints), ≥ 10,000 trials per cell. Output is a
**false-promotion / false-rejection curve vs saboteur fraction**, per channel,
per attack model, with and without immune downgrade — the same characterization
Sarmenta (2002) produced for voting, spot-checking, and credibility, now
computed for CursiveOS's actual rule.

## 3. Seeding the simulation from measured corpus constants (not guesses)

The point of doing this *now* is that the corpus already measured the inputs the
simulation needs — so the result is grounded, not a toy:

| Parameter | Value | Source |
| --- | --- | --- |
| Cold-start within-machine CV | 0.002 | Ch00 §5 / VALIDATION "noise floor", 6× v0.9 on Stardust |
| Network within-machine CV | 0.192 | same; triggers the N+2 escalation branch |
| Cold-start effect size (desktop Arc class) | −51% | VALIDATION "cold-start is hardware-scoped", 2 machines |
| Cold-start effect size (laptop i5 class) | ~0% | same — the hardware-scope split is real, not assumed |
| N-rule + CV breakpoint | `max(1,min(5,floor(sqrt(fleet))))`, CV>0.15→N+2 | Ch08 §2 (verbatim from main-repo sensor-array spec) |
| Effective-N downgrade trigger | correlated fingerprint / wallet / synchronized timing | Ch08 §5; Ch11 independence inputs |

Honest hosts draw from `Normal(effect_for_their_class, CV·|effect|)`, truncated
sanely. The two CVs differ by ~100×, so the experiment is not a uniform-noise
abstraction — it inherits the corpus's real finding that *channels are not
interchangeable*, which is the whole reason Ch08 went per-channel.

## 4. Attack models (each maps to a corpus-named threat)

| # | Attack | Corpus anchor | Ground truth |
| --- | --- | --- | --- |
| A1 | **Independent liars** — *f* hosts report a fake winning delta for an inert variant, each with its own fingerprint/wallet | Ch03d §2.1 Sarmenta saboteurs; Ch08 §6 "uncorrected testing accepts noise" | variant is inert → any promotion is false |
| A2 | **Sybil cluster** — *f* hosts share a cloned anomaly profile / synchronized delta timing (pseudo-replication) | Ch08 §5 "VM farm with cloned SMBIOS"; Ch11 fingerprint independence | inert → promotion is false; tests immune downgrade (H2) |
| A3 | **Goodhart gamer** — saboteurs inflate the **network** channel (highest fitness weight, noisiest) while the variant is inert elsewhere | Ch03d §2.5 / §4 Skalse et al.; Ch08 §5 "proxy hacking" | inert → tests whether the noisy high-weight channel is the soft target (H3) |
| A4 | **Griefer** — *f* hosts report fake null/negative deltas to **suppress** the real desktop cold-start win | Sarmenta's reject-good failure mode (Ch03d §2.1) | variant is genuinely good → any rejection is false (H4) |

Each attack is run across the full *f* / `fleet_size` sweep. A1/A4 stress the
base rule; A2 isolates the immune-sensor contribution; A3 stresses CV escalation
on the money channel.

## 5. Success criteria (pre-registered)

| Outcome | Decision |
| --- | --- |
| **H0a holds** — false promotion ≤ 5% up to *f* = 0.34 on cold-start, even without immune downgrade | Ch08's base rule **is** a genuine sabotage-tolerance layer on a low-noise channel up to the Byzantine third. Upgrade Ch03d §5 claim #1 and the Ch08 living layer from "approximates" → **Supported by simulation**. Record the break-even *f* as the documented tolerance bound. |
| **H1 holds** — some *f* ≤ 0.34 already promotes the decoy | The base N-rule is **not** sabotage-tolerant alone; the immune-sensor downgrade (Ch08 §5) is **load-bearing, not optional**. Block any BTC-gating (Ch02) on a fleet until effective-N is implemented and re-tested. Add a VALIDATION row. |
| **H2 holds** | Immune downgrade earns its place; specify the correlation-graph → effective-N policy (Ch08 §10 gap #4) as a prerequisite for payout, with the measured margin as its acceptance bar. |
| **H2 fails** (downgrade barely helps vs A2) | Fingerprint/wallet/anomaly independence is **insufficient** against a competent Sybil (the Ch08 §5 / Ch11 "Unvalidated" rows confirmed negatively); escalate to the Ch02/Ch11/Ch12 anti-Sybil economics before fleet payout. |
| **H3 holds** | The highest-weight network channel is the soft target. Recommend capping noisy-channel fitness weight or requiring extra confirmations on high-CV channels before they can gate payout (sharpens Ch08 §2 / the open BBR-weight flag in VALIDATION). |
| **H4 holds** | Confirmation is griefable: a minority can deny honest contributors their validated wins (and Ch02 income). Flag as a denial-of-fitness vector; pair with the Ch02 metabolic-sensor simulation already in the pipeline. |

Promotion of any corpus claim follows the existing rule: a simulation result is
**"Supported by simulation,"** never "Validated" — that label is reserved for the
live multi-machine fleet calibration (Ch08 §10 gap #1). This experiment bounds
the rule's *theoretical* sabotage tolerance under measured noise; it does not
prove the live fleet behaves identically.

## 6. Feasibility

- **No hardware, no fleet, no money at risk.** Pure Monte-Carlo over the Ch08
  rule, seeded by §3 constants already in CursiveRoot/VALIDATION. Runnable on
  one laptop in an afternoon; the dominant cost is writing the rule
  implementation faithfully.
- **Build (graduates to main `CursiveOS` per the workflow boundary):** a
  `confirmation-rule` module that the simulator and the live hub analyzer can
  **share** — so the thing tested is the thing deployed, not a paraphrase. This
  is a feature, not overhead: it forces Ch08 §2/§5 to become executable.
- **Optional replay extension (stronger, still cheap):** instead of fully
  synthetic honest hosts, **replay real `run_detail_bundles`** from CursiveRoot
  (the desktop/laptop cold-start runs already stored) as the honest population
  and inject only the synthetic saboteurs. This grounds the honest distribution
  in real per-pass variance rather than a fitted Normal, at the cost of a
  CursiveRoot read path. Recommended as a second pass once the synthetic version
  draws the curves.

## 7. Expected outcome (pre-registered honest guess)

Given the measured ~100× CV gap between channels and the corpus's own caution,
the most likely result is **mixed and channel-dependent**: H0a holds on
cold-start (CV 0.002 is so tight that independent liars must fabricate an
obviously-out-of-distribution delta to move a quorum, which the consistency
check resists up to a high *f*), while **H1/H3 hold on the network channel**,
where CV 0.192 gives a liar enough cover that escalation to N+2 is not enough at
moderate *f*. H2 (immune downgrade) most likely helps against the A2 Sybil
cluster but **H2 fails or is marginal** against a sophisticated A2 that also
diversifies timing — confirming the Ch08 §5 / Ch11 "independence is necessary
but not sufficient" rows *negatively*, which is itself decision-changing. H4
(griefing) likely holds at low *f*, since suppressing a win needs only enough
fake nulls to deny quorum, not to win one.

If that pattern holds, the headline for the operators is concrete: **cold-start
is safe to gate fitness on under attack; the network channel is not, until its
weight is capped or its confirmation count raised; and effective-N is mandatory,
not optional, before any BTC touches the fleet.** That directly informs Ch02
payout sequencing and the Ch08 §10 open gaps.

## 8. What would change our mind

Per the corpus rule ("What evidence would change our mind?",
RESEARCH_PIPELINE §3):

- A clean **H0a-holds-everywhere** result (even the network channel resists a
  one-third saboteur fraction) would upgrade Ch03d §5's "Ch08 approximates a
  sabotage-tolerance layer" to a Supported, quantified claim and lower the
  urgency of the immune-sensor build — the base rule would already carry the
  load.
- A clean **H1-holds-at-low-*f*** result (decoy promoted below, say, *f* = 0.15
  on cold-start) would be a red flag on the whole confirmation design and should
  **halt** any Ch02 fleet-payout planning until the rule is redesigned — exactly
  the kind of failure that is catastrophic to discover *after* real money is
  attached rather than in simulation now.
