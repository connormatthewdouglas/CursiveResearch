# Cold-Start Order / Page-Cache Confound Test

Date created: 2026-06-23
Linked chapters: `chapters/00-benchmark-schema-and-measurement-validity.md` (§2.3, §5 item 7),
`chapters/01-seed-organism-and-sensor-array.md` (evidence / confirmation model)
Linked VALIDATION rows: "Chapter 22 / cold-start is hardware-scoped" (Validated),
"Chapter 22 / measurement noise floor" (Validated)
Status: Proposed; not yet executed. Single-machine, ~1 afternoon of run time.

## Why this experiment

Cold-start latency is currently the organism's **only selection-grade channel**.
The 2026-06-16 noise floor (§5 item 7) put cold-start at CV **0.002** — "the
project's most reliable signal" — while network is too noisy to quote (CV 0.192),
and sustained and idle-power are at or below their own noise. Every live selection
decision recorded so far (v0.9b ablation, v0.9c promotion as global parent, the
hardware-scoped −51% Arc win) rests on the cold-start delta.

But the benchmark measures that delta with a **fixed internal order**: within each
run the **baseline condition runs first, the tuned condition second** (Chapter 22
§2.3, §5 item 1). The same section also records that **"page-cache state strongly
affects model load: the first cold-start of a session reads from disk, later ones
from cache. Not recorded."** Putting those two facts together exposes an untested
confound:

> If model-load TTFT is sensitive to OS page-cache / dentry state, the
> *second* condition in every pair inherits a warm cache from the first and gets
> a systematic latency advantage **independent of which preset it is testing.**
> Because the tuned preset is always second, part of the measured "tuned is
> faster" delta could be a run-order artifact rather than a preset effect.

The 2026-06-16 six-run noise floor does **not** rule this out: all six runs were
the same v0.9 preset and all six used the same baseline-first/tuned-second order,
so they measure *repeatability of the confounded quantity*, not the confound. CV
0.002 across identically-ordered runs is exactly what an order artifact would also
produce. The pipeline's seed-organism row already says the right thing —
**"Repeat and counterbalance before any acceptance"** — but that counterbalancing
has never been run on the one channel everything depends on.

This experiment is the cheapest way to either harden the corpus's most-trusted
signal or discover that the current selection basis is partly confounded.

## Hypothesis

**H0 (null / hoped-for):** The cold-start delta is a true preset effect. Under
order counterbalancing and page-cache control, the tuned-minus-baseline cold-start
delta on the Arc desktop stays within measurement noise of the originally reported
−51% (i.e. |Δ_counterbalanced − Δ_fixed-order| is small relative to the CV-0.002
noise floor).

**H1 (falsifier):** A material part of the −51% is a run-order / warm-cache
artifact. When condition order is counterbalanced and/or the page cache is reset
between conditions, the cold-start delta shrinks meaningfully (operational
threshold below), and the residual order effect is statistically distinguishable
from zero.

H1 is falsifiable and pre-registered: it predicts a specific, measurable shrinkage
direction and an order main-effect that the current fixed-order design cannot see.

## Method

Run on the founder rig already characterized in Chapter 22 (Ryzen 7 5700 + Arc
A750, fingerprint `3e6b165ddf112a75`) so results are directly comparable to the
existing −51% and CV-0.002 numbers. Use the existing harness
(`cursiveos-full-test-v1.x`) cold-start phase as the measurement primitive; only
the **scheduling around it** changes. No new presets — compare the existing v0.8
(or v0.9c) tuned preset against its baseline, exactly as in the live screen.

Three arms, each a set of paired baseline/tuned cold-start measurements:

| Arm | Order within each pair | Page cache between conditions | Purpose |
| --- | --- | --- | --- |
| A — Replicate | baseline → tuned (current fixed order) | left as-is (current behavior) | Reproduce the live −51% under today's protocol; anchor. |
| B — Counterbalanced | alternate B→T and T→B across pairs (ABBA / randomized) | left as-is | Isolate the run-order main effect with cache behavior unchanged. |
| C — Cache-controlled | counterbalanced | drop caches + reload model to a **known cold** state before *every* condition (`sync; echo 3 > /proc/sys/vm/drop_caches`, optionally evict the model file) | Remove the warm-cache asymmetry entirely. |

- **≥ 12 pairs per arm** (24 cold-start measurements/arm). The CV-0.002 floor means
  effects of a few percent are detectable with this N; record raw per-call TTFT and
  load duration, not just the collapsed delta.
- **Record the §3 phase context every condition**: page-cache hot/cold for the model
  file, governor, AC/battery, CPU/GPU temp at phase start, GPU freq. The whole point
  is to convert "mystery variance" into attributable variance, per Chapter 22 §3.
- Keep everything else fixed: same model + quantization + ollama version (record
  them — §2.3 notes they are not in `runs` columns), same ambient conditions, no
  other load. Insert the existing settle delay before idle/cold capture.
- Reversibility unchanged: presets reverted at run end as today.

### What each arm tells you

- **A vs B** isolates the **run-order main effect** with nothing else changed. If
  B's delta ≈ A's delta, order is not driving the result. If B shrinks, order
  matters and the fixed-order protocol is biased.
- **B vs C** isolates the **page-cache mechanism** specifically. If C ≈ B, the order
  effect (if any) is not cache-mediated; if C shrinks relative to B, warm cache is
  the mechanism — which directly implicates the §2.3 "first reads disk, later from
  cache" pathway.

## Success criteria

Pre-registered decision rule (founder rig, Arc-desktop hardware class only):

| Outcome | Condition | Corpus action |
| --- | --- | --- |
| **Confound rejected (H0 upheld)** | Counterbalanced + cache-controlled delta within ±5 percentage points of Arm A's delta, and the fitted order main-effect is not distinguishable from zero (CI overlaps 0). | Promote cold-start from "reliable repeatable signal" to **order-robust** signal. Add page-cache state to the recorded schema and keep the cheaper fixed-order protocol with a documented justification. |
| **Partial confound** | 5–20 pp of the delta attributable to order/cache. | Keep cold-start as a selection channel but **require counterbalanced pairs** before any acceptance; correct the magnitude of the −51% / v0.9c claims to the cache-controlled value; flag affected VALIDATION rows. |
| **Confound dominates (H1)** | >20 pp attributable to order/cache, order effect clearly ≠ 0. | Treat all prior fixed-order cold-start deltas (including the v0.9c global-parent promotion) as **not decision-grade**; re-screen under arm C; raise a `VALIDATION.md` "Flagged for Review" row on the cold-start claims. |

Thresholds are in **percentage points of the cold-start delta**, chosen against the
existing −51% headline; refine once arm A's variance is in hand. Report effect sizes
with confidence intervals, not just pass/fail.

## Expected outcome

Best prior from the corpus is that **the bulk of the −51% survives** — the v0.9b/v0.9c
complementary ablation (§5 item 1) already attributed the Arc cold-start win to a
specific CPU-side mechanism (governor / C-state / EPP), which is a real preset effect,
not a cache trick. So Arm A ≈ Arm B ≈ Arm C is the most likely result, and the
valuable deliverable is then a **defensible "order-robust" label** plus the
page-cache field added to the schema.

The non-trivial risk worth the afternoon: model **load** TTFT is exactly the kind of
disk-bound quantity §2.3 warns is cache-sensitive, and it always runs second in the
tuned condition. If even 10–15 pp of the delta is warm-cache, that silently inflates
every fixed-order screen and the founding global-parent promotion was made on a
partly confounded number. Either way the corpus ends with its most important channel
on firmer footing than "repeatable under one fixed order."

## Boundary

This is a measurement-validity experiment for the corpus, not an implementation spec.
The counterbalancing/cache-control scheduling and the new page-cache schema field
graduate to the main `CursiveOS` repo as harness build tasks once the design is
confirmed here (normal `RESEARCH_PIPELINE.md` graduation rule). Results worth keeping
land in `experiments/results/` and update Chapter 22 §5 + the relevant VALIDATION rows.
