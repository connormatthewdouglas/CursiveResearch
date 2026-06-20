# Experiment Proposal: Does the LLM Proposer Beat Random Search?

Date created: 2026-06-20
Linked chapters: `chapters/05-ai-guided-tuning.md`, `chapters/16-benchmark-schema-and-measurement-validity.md`, `chapters/10-seed-organism-and-sensor-array.md`
Sharpens: `experiments/ai-guided-tuning-loop-validation-plan.md` (claim CH05-BM-002)
Status: Proposed; not yet executed.

## 0. Why this experiment, why now

The central CursiveOS thesis is that a guided self-improvement loop creates
value (Chapters 01, 05, 10). The corpus has never tested the cheapest, most
load-bearing version of that claim: **that the intelligent proposer beats blind
random search over the same knobs under the same evaluation budget**
(`ai-guided-tuning-loop-validation-plan.md`, claim CH05-BM-002, still
"unverified locally").

Two recent corpus events make this both designable and urgent:

1. **The noise floor is now measured (2026-06-16, Chapter 16 / VALIDATION).**
   Six identical v0.9 runs on Stardust gave per-channel CV: cold-start **0.002**
   ("rock-solid"), network 0.192 (above the 0.15 escalation threshold;
   magnitude unreliable), sustained sign-unstable, idle-power 0.83 raw → ~0.01
   when sampled after settling. We finally know which channel can carry a
   selection decision and how many confirmation runs each needs. You cannot run
   a powered tuning experiment without this; now you can.

2. **The last "win" collapsed under scrutiny (Chapter 16 / VALIDATION).** The
   celebrated "+246% from our network tuning" turned out to be a loopback BDP
   artifact; the entire real-path win was a single well-known sysctl
   (`tcp_congestion_control=bbr`), and the buffer/qdisc stack added ~0%.
   Separately, the v0.8 GPU frequency pin was validated as ~0 W dead weight
   (parsimony, not power). These are exactly the conditions under which a
   proposer can *look* smart while a one-line baseline captures the whole
   effect — and inert knobs can accumulate. That is the failure mode this
   experiment is built to detect, echoing the proposer/verifier separation
   lesson from LADDER and the reward-hacking literature
   (`papers/recursive-self-improvement/`).

If the proposer cannot beat random search on a clean, verifiable channel on one
machine, no amount of fleet scale or economic layer fixes that. This is the
load-bearing brick; it is currently untested.

## 1. Hypothesis (falsifiable)

**H1 (primary).** On Stardust, given an identical allowlist of reversible knobs
and an identical evaluation budget of *K* candidate configurations, an
LLM proposer finds a configuration whose confirmed cold-start fitness exceeds
the best configuration found by uniform random search, by a margin larger than
the measured cold-start noise floor.

**H0 (null).** The LLM proposer's best confirmed cold-start fitness is less than
or equal to random search's, within the cold-start noise floor. (i.e. the
proposer adds no value over blind search at equal budget.)

**H2 (secondary, Goodhart guard).** The LLM proposer accumulates *fewer* inert
("decoy") knobs in its accepted configuration than random search does, when
both are scored by the same verifier.

## 2. Why cold-start is the only fitness channel here

Per the 2026-06-16 noise floor (Chapter 16 / VALIDATION), cold-start is the one
channel solid enough to drive selection today (CV 0.002). Therefore:

- **Fitness = cold-start latency delta** (GPU idle → first token), measured by
  the existing harness, lower is better.
- **Do not** use network (CV 0.192, magnitude unreliable), sustained
  (sign-unstable, signal < noise), or idle power (only usable after the new
  settle-sampling fix) as the fitness signal in this experiment. Record them as
  guardrail/telemetry only.

This keeps the verifier clean and deterministic — the precondition LADDER and
the reward-hacking paper both identify as the thing that makes a
self-improvement loop safe.

## 3. The allowlist (designed to be diagnostic, not just safe)

All knobs reversible, documented, allowlisted, and reverted between candidates
(the harness already reverts presets at run end — Chapter 16 §1). The allowlist
is deliberately seeded with three kinds of knob so the result is interpretable:

| Knob class | Examples (Stardust: Ryzen 7 5700 + Arc A750) | Expected effect on cold-start |
| --- | --- | --- |
| **Live lever** (≥1) | CPU governor `performance` on AC; GPU power/perf level | Plausibly real — governor change is the validated cold-start mechanism on the laptop (Chapter 16, hardware-scoped cold-start) |
| **Decoy / inert** (≥3) | v0.8 GPU frequency pin (`slpc_ignore_eff` + `rps_min 2000` + `rps_boost max`); other knobs validated as ~0-effect at idle | ~0 (validated dead weight) — present to detect Goodhart/knob-hoarding |
| **Neutral-to-risky** | zram on/off, THP madvise/never, a benign sysctl | Unknown; lets the proposer reason |

Including the *validated-inert* GPU pin is the point: a proposer that reasons
from telemetry should learn to drop it (as v0.9 did on parsimony grounds),
while random search will include it ~50% of the time. H2 measures exactly this.

## 4. Arms (same budget K each)

| Arm | Strategy | Tests |
| --- | --- | --- |
| A | Static default (no tuning) | Floor: improvement over doing nothing |
| B | Uniform random search over the allowlist | The real baseline for H1 |
| C | LLM proposer, one-shot, no memory | CH05-BM-002 — does intelligence beat random? |
| D | LLM proposer + CursiveRoot prior-run retrieval | CH05-BM-004 — does mutation memory help? |

Suggested K = 12–20 candidates per arm (small allowlist → modest budget). Each
arm gets the *identical* budget and the *identical* allowlist; only the proposal
strategy differs.

## 5. Confirmation, power, and protocol

- **Confirmation runs per candidate:** cold-start CV ≈ 0.002 means a few
  confirmation runs resolve differences far below the effect of interest. Use
  **n = 3** confirmation runs per candidate; the resolvable paired difference is
  well under 1%, while the cold-start effect previously seen on this hardware
  class is ~−51% (Chapter 16, hardware-scoped cold-start). The experiment is
  therefore over-powered for any decision-relevant effect — by design, so a null
  result is trustworthy, not just underpowered.
- **Ordering / counterbalancing:** randomize candidate order within each arm;
  interleave arms across sessions; revert presets between candidates (harness
  default). This mirrors the "repeat and counterbalance before any acceptance"
  rule already applied to the seed-organism screen (RESEARCH_PIPELINE).
- **Metadata per run:** reuse the evidence schema in
  `ai-guided-tuning-loop-validation-plan.md` (run_id, host_id, kernel_version,
  candidate_config_hash, agent_model, agent_prompt_hash, retrieval_context_hash,
  fitness_before/after, decision) so results are CursiveRoot-ready.
- **Single machine, single session class:** Stardust only. Cold-start is
  hardware-scoped (Chapter 16 / VALIDATION), so this experiment proves the loop
  on one machine; it does **not** claim fleet transfer. That is a deliberate
  scope boundary, not a limitation to be papered over.

## 6. Success criteria

| Outcome | Decision |
| --- | --- |
| C's best confirmed cold-start beats B's by > noise floor, and C beats A | H1 supported: the proposer adds value on a clean channel. Promote CH05-BM-002 from "unverified" toward "Locally reproduced." Proceed to memory (D) and harder channels. |
| C ≈ B (within noise), both beat A | **H0 not rejected.** The *knobs* matter but the *proposer* does not — value is in the allowlist, not the intelligence. This is the BBR situation again: re-scope Chapter 05 claims, and prefer a curated allowlist + cheap search over an LLM loop until a channel is found where reasoning pays. |
| Neither C nor B beats A meaningfully | The allowlist has no real cold-start lever on this hardware; redesign the allowlist before testing proposers. |
| C accumulates the inert GPU pin / decoy knobs as often as B (H2 fails) | Goodhart/knob-hoarding warning: the proposer is not reasoning from the verifier. Flag in VALIDATION; do not enable unattended tuning. |

A strategy is promoted only under the acceptance rules already in
`ai-guided-tuning-loop-validation-plan.md` §"Acceptance Rules" (typed proposals,
allowlisted targets, before/after recorded, reproducible, beats ≥2 baselines,
guardrails not regressed).

## 7. Expected outcome (pre-registered honest guess)

Given the corpus track record — the network "win" reduced to one sysctl, and
inert knobs surviving in v0.8 until a probe caught them — the most likely result
is **C ≈ B (H0 not rejected) on this small allowlist**: the live lever (governor)
is findable by both, and the proposer's edge, if any, shows up only as H2
(dropping decoy knobs) rather than as a higher peak fitness. That would itself
be a valuable, decision-changing finding: it would say the near-term value of
CursiveOS tuning is in a well-chosen reversible allowlist plus a clean verifier,
with the LLM earning its place as a *parsimony/explanation* engine before a
*peak-finding* one. The experiment is designed so that this null is informative
rather than ambiguous.

## 8. Feasibility

- Hardware: Stardust, already the noise-floor reference machine.
- Harness: existing full-test wrapper (cold-start channel, preset revert,
  `run_detail_bundles`); add a thin driver that loops candidates per arm.
- Verifier: deterministic cold-start measurement already deployed.
- New build (graduates to main `CursiveOS` repo per workflow): the arm driver
  (allowlist loader, random sampler, LLM proposer hook, CursiveRoot retrieval
  for arm D) and a results emitter. No kernel rebuild, no firmware, no host
  mutation beyond reversible allowlisted knobs (Phase 1 scope).

## 9. What would change our mind

Per the corpus's own rule ("What evidence would change our mind?",
RESEARCH_PIPELINE §3): a clean C > B result on cold-start would be the first
local evidence that the *loop* — not just the knobs — creates value, and would
justify extending to harder, less-clean channels (where the LADDER open
question about complex verifiers bites). A clean C ≈ B result would redirect
near-term effort from proposer sophistication to allowlist curation and verifier
quality.
