# Red-Team Challenge: the unscoped "switch to BBR" headline and default-preset recommendation (Chapter 09 + Chapter 00 network headline)

- Date: 2026-06-25
- Reviewer: Adversarial-review agent (red team)
- Type: Adversarial corpus review. **Challenge only** — the original claims were
  **not** edited (see [CORPUS_WORKFLOW.md](../../CORPUS_WORKFLOW.md) §3 and the
  VALIDATION.md "Flagged for Review" table).
- Target files/sections:
  - `chapters/09-network-transport-and-congestion-control.md` §3 ("BBR replaces
    need for all CursiveOS buffer tuning on ≤1GbE" — **Validated**; "BBR win is
    largely a one-line sysctl" — **Supported**), §7 ("Default preset includes
    BBR on loss-prone workloads" — **Supported**), §9.1 ("credit BBR for
    validated real-path loss behavior").
  - `VALIDATION.md` rows "Chapter 00 / network headline" and "Chapter 09 / BBR
    vs buffer magnitude" — both **Validated**, with the action "Public claim =
    'switch to BBR'".
  - `CHANGELOG.md` 2026-06-16 ("Real-Path A/B Overturns the Stack-Delta
    Magnitude").

## The challenged claim

The corpus elevates a single, repeated instruction to **Validated/Supported**
status and makes it the canonical public-messaging line and a shipped default:

> "Public claim = 'switch to BBR' (real, large under loss)." (VALIDATION.md,
> Chapter 00 network headline, **Validated**)

> "BBR replaces need for all CursiveOS buffer tuning on ≤1GbE — **Validated** for
> tested path." / "Default preset includes BBR on loss-prone workloads — yes —
> **Supported**." (Chapter 09 §3, §7)

This is load-bearing. Network is the **highest-weighted fitness channel (0.40)**
in the current schema (Chapter 09, "Why this chapter exists"), so the
CUBIC→BBR finding both anchors the project's flagship networking marketing claim
*and* drives the dominant fitness term *and* is proposed as a system-wide preset
pushed to contributor machines.

## What is actually true (and not disputed)

This challenge does **not** dispute the corpus's measurement:

- On the real-path A/B (Stardust → second machine, 1GbE, netem 50 ms + 0.5 %
  loss), CUBIC ran 43.1 Mbit/s and BBR ran 851.1 Mbit/s (+1875 %), while the
  buffer/qdisc stack added −0.7 %. That decomposition is sound and the
  "credit BBR, not buffers, on ≤1GbE under loss" conclusion is correct.
- BBR's loss-tolerance under random (non-congestive) loss is real and is exactly
  why it beats loss-based CUBIC on a lossy path.

The single-flow result stands. The problem is the **scope** the corpus attaches
to it.

## Why the unscoped "switch to BBR" framing is overstated

Every BBR number in the corpus comes from a **single bulk iperf3 flow in
isolation**. The corpus then promotes that single-flow result to (a) a Validated
*public/marketing* headline, (b) a *default* preset for "loss-prone workloads,"
and (c) the dominant fitness channel — without measuring the one behavior that
matters most when many contributors run BBR on shared links: **how a BBR flow
treats the traffic it competes with.** The peer-reviewed literature on exactly
that question is unambiguous and unfavorable to an unscoped default.

1. **BBR is structurally unfair to loss-based traffic (CUBIC/Reno).** Ware,
   Mukerjee, Seshan & Sherry (ACM IMC 2019) show that when BBR competes with
   loss-based congestion control it becomes *window-limited by its in-flight cap*
   (~1.5–2×BDP), so **a single BBR flow claims a roughly fixed fraction of the
   bottleneck — about 40 % in their experiments — regardless of how many
   loss-based flows it competes against (they tested up to 16 CUBIC flows).**
   A BBR flow does not back off proportionally; it takes its share and the
   CUBIC flows divide the remainder. This is the opposite of the "harmless
   one-line sysctl" framing.

2. **BBR(v1) inflicts excessive packet loss and RTT-unfairness depending on
   buffer size.** Hock, Bless & Zitterbart (IEEE ICNP 2017, "Experimental
   Evaluation of BBR Congestion Control") report that BBR causes a **large
   volume of packet retransmissions/loss in shallow buffers** and exhibits
   **RTT-unfairness in larger buffers** (flows with different RTTs get very
   different shares). The corpus tested one buffer regime on one path; the
   harm modes are buffer- and competition-dependent and were never exercised.

3. **The version the corpus ships is the version with these problems.** Chapter
   09 §3 instructs `modprobe tcp_bbr` — the in-tree Linux module, which is
   **BBRv1-lineage**. Google's own team subsequently built **BBRv2 and BBRv3**
   specifically to reduce BBRv1's inter-flow unfairness, high retransmission
   rate, and loss-agnostic aggressiveness (documented in the IETF ICCRG BBR
   drafts and confirmed by independent BBRv2 evaluations, e.g. Drucker et al.,
   COMSNETS 2024; Nandagiri et al., 2020). Recommending a system-wide BBRv1
   default in 2026 without this distinction repeats a known, since-corrected
   mistake.

4. **This is also a Chapter 06 mutation-safety problem, not just a marketing
   problem.** `net.ipv4.tcp_congestion_control = bbr` is a **system-wide**
   setting: it changes how *all* of the host's TCP traffic behaves, including
   the operator's other applications and — on a shared link — their neighbors'
   flows. The corpus's safety model (Ch06) is built on bounding the blast radius
   of self-mutation, yet the BBR preset's true blast radius extends **off the
   measured host entirely** (to competing/co-resident flows), and the genesis
   harness has no sensor that can see it. A "+1875 %, just flip a sysctl"
   default understates that blast radius.

## The corpus already half-knows this — which is the point

Chapter 09 is not naive: §3 notes "Fairness with other flows | documented
caveats; use fq pacing," and §10 lists Gap #3 "Concurrent multi-flow iperf or
rrul — competition fairness under BBR" and Gap #5 "fleet-population confirmation
of BBR-only benefit on ≥3 independent paths." The challenge is precisely the
**mismatch** between status levels:

- the *benefit* (single-flow CUBIC→BBR win) is rated **Validated** and promoted
  to a public claim + default preset + dominant fitness channel **now**, while
- the *cost* (multi-flow unfairness, retransmit/loss inflicted on competing
  traffic, RTT-unfairness, BBRv1-vs-v2/v3) is demoted to an unprioritized
  "open gap."

A claim cannot be simultaneously "Validated enough to be the public headline and
a shipped default" and "its dominant real-world caveat is future work." For a
decentralized **fleet** — many machines, shared home/office uplinks, competing
flows — the caveat is not an edge case; it is the common case.

## Accurate restatement

A faithful, appropriately scoped version of the claim would read approximately:

> "On a **single bulk TCP flow** over a lossy ≤1GbE path, switching CUBIC→BBR
> recovers most of the throughput CUBIC loses to its loss-sensitivity (measured
> +1875 % on one real path; buffer/qdisc tuning adds ≈0 %). This is validated
> **for a single flow in isolation only.** BBRv1 (the in-tree `tcp_bbr` module)
> is documented to be unfair to competing loss-based flows and to inflict high
> retransmission loss in shallow buffers, so a system-wide BBR default must not
> be marketed or shipped to the fleet until multi-flow fairness/retransmit
> behavior is measured (Ch09 Gap #3); when BBR is used, pair it with `fq`
> pacing and prefer BBRv2/v3 where available."

That keeps the genuine, measured win while removing the unscoped "switch to BBR"
headline and the un-caveated default-preset recommendation.

## Impact / why this is the most consequential weak claim

- It sits on the **highest-weighted fitness channel (0.40)** and is the corpus's
  designated **public/marketing** networking line — so over-scoping it
  simultaneously inflates the project's external claim, the dominant selection
  signal, *and* a default shipped to every contributor.
- The contradicting evidence is **peer-reviewed and directly on point** (IMC
  2019, ICNP 2017), and is corroborated by BBR's own authors having built v2/v3
  to fix it — so the challenge is high-confidence and one-directional.
- It is the rare corpus claim whose error mode is **active harm to third
  parties** (degrading competing/neighbor traffic), which makes it a
  mutation-safety issue (Ch06), not merely an accuracy issue.
- By contrast, the corpus's *narrow* conclusion — "on ≤1GbE under loss, the win
  is CUBIC→BBR, not buffer tuning" — is correct and was **not** selected as the
  challenge. The challenge is only against the **unscoped promotion** of that
  conclusion to a public claim, a default preset, and a fitness driver.

## Suggested action (for a human/owner decision — not applied here)

1. Do **not** edit the Validated rows or Chapter 09 in place from this note.
2. Treat the unqualified "switch to BBR" public claim and the
   "default preset includes BBR" recommendation as **Supported only for a single
   flow in isolation; Unvalidated for fleet/multi-flow deployment** until
   Chapter 09 Gap #3 (concurrent multi-flow + retransmit/fairness) and Gap #5
   (≥3 independent paths) are run.
3. When Chapter 09 is next revised: add the inter-flow unfairness + shallow-buffer
   retransmit findings (IMC 2019, ICNP 2017) to §3/§7/§9, add the
   BBRv1-vs-BBRv2/v3 distinction, pair any BBR preset with `fq` pacing, and treat
   a system-wide `tcp_congestion_control` change as a Chapter 06 mutation whose
   blast radius includes off-host competing traffic.
4. Keep the validated single-flow decomposition exactly as is.

## External sources

- Ware, Mukerjee, Seshan, Sherry, *Modeling BBR's Interactions with Loss-Based
  Congestion Control*, ACM IMC 2019 — a single BBR flow takes a roughly fixed
  share (~40 %) of the bottleneck regardless of the number of competing
  loss-based flows (tested up to 16); BBR is window-limited by its in-flight cap
  under competition:
  - https://www.cs.cmu.edu/~rware/assets/pdf/ware-imc2019.pdf
  - https://conferences.sigcomm.org/imc/2019/presentations/p282.pdf
- Hock, Bless, Zitterbart, *Experimental Evaluation of BBR Congestion Control*,
  IEEE ICNP 2017 — excessive packet loss/retransmission in shallow buffers, RTT
  unfairness, and unfairness to loss-based flows:
  https://telematics.tm.kit.edu/publications/Files/595/2017-kit-icnp-bbr-authors-copy.pdf
- Scherrer et al., *Model-Based Insights on the Performance, Fairness, and
  Stability of BBR*, ACM IMC 2022 — model-level confirmation of BBR
  fairness/stability limitations:
  https://netsec.ethz.ch/publications/papers/scherrer_bbr_imc22.pdf
- Drucker et al., *BBR vs. BBRv2: A Performance Evaluation*, COMSNETS 2024 —
  BBRv2 reduces BBRv1's RTT-unfairness, aggressiveness in sub-1-BDP buffers, and
  retransmission rate:
  https://www3.cs.stonybrook.edu/~anshul/comsnets24_bbrbbrv2.pdf
- Cardwell et al., *BBR Congestion Control* (IETF ICCRG drafts) — the BBR
  authors' own v2/v3 work, created to address v1's coexistence/fairness behavior:
  https://www.ietf.org/archive/id/draft-cardwell-iccrg-bbr-congestion-control-01.html
- Internal corroboration: `CHANGELOG.md` 2026-06-16 real-path A/B; Chapter 09
  §3, §5.2, §7, §10; VALIDATION.md "Chapter 00 / network headline" and
  "Chapter 09 / BBR vs buffer magnitude".

## Caveat on this note

The single-flow CUBIC→BBR win measured by the corpus is real and is not in
dispute; this note challenges only the **unscoped promotion** of that result to a
public claim, a fleet default, and the dominant fitness channel without the
multi-flow fairness/retransmit measurement the corpus itself lists as an open
gap. The fleet-scale magnitude of the unfairness on CursiveOS's specific
hardware and links should be confirmed by running Chapter 09 Gap #3 before any
irreversible preset or marketing decision.
