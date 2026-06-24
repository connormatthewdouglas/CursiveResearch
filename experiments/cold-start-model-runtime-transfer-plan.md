# Experiment Proposal: Does the Cold-Start Preset Gain Survive a Change of Model, Quantization, or Runtime?

Date created: 2026-06-24
Linked chapters: `chapters/00-benchmark-schema-and-measurement-validity.md` (§2.3, §5.1, §5.5, §5.7), `chapters/10-local-llm-inference-runtime-architecture.md` (§2, runs schema), `chapters/01-seed-organism-and-sensor-array.md`
Complements: `experiments/cold-start-mechanism-and-hardware-scoping-plan.md` (cross-*machine* transfer). This plan tests the orthogonal cross-*model/runtime* axis on a single machine.
Status: Proposed; not yet executed.

## 0. Why this experiment, why now

Cold-start latency is the project's single most trustworthy signal: within-machine
CV **0.002** on Stardust (Ch00 §5.7 / VALIDATION), versus network 0.192, sustained
sign-unstable, and idle-power usable only after the settle-sampling fix. Every
acceptance-grade selection decision the corpus can make today rides on this one
channel. Two validated facts about it are already on record:

1. **The win is hardware-scoped.** The v0.8/v0.9c cold-start preset gives **−51%**
   on the Ryzen 7 5700 + Arc A750 desktop and **~0%** on the i5-11300H laptop
   (Ch00 §5.5 / VALIDATION, "cold-start is hardware-scoped"). A separate plan
   (`cold-start-mechanism-and-hardware-scoping-plan.md`) isolates *which knob*
   and *which machines* carry it.

2. **The mechanism is CPU idle-exit, not GPU- or model-side.** Complementary
   ablation (Ch00 §5.1) showed the GPU frequency pin is ~0 W dead weight; the
   −51% is produced by CPU idle-exit knobs (governor / EPP / deep C-state).

There is a **third scoping axis the corpus has never tested and no plan covers:
the served model.** Every cold-start number on record was measured against one
inference configuration. But the cold-start sensor is defined as "GPU idle → first
token" (Ch00 §1; Ch10 §"Cold-start sensor"), and first-token latency is the sum of
**two** components that scale differently:

- an **idle-exit** component (wake the CPU package / dGPU out of deep idle) — the
  part the preset actually fixes, mechanistically model-*independent*; and
- a **model-load / first-compute** component (page-cache fault the weights, build
  the graph, run the first forward pass) — which depends heavily on model size,
  quantization, and runtime backend (Ch00 §2.3: "page-cache state strongly affects
  model load"; Ch10 §2: Q4_K_M vs Q8, Ollama/llama.cpp/OpenVINO/SYCL backends).

Because the reported fitness is a **percentage** delta, a constant idle-exit saving
will produce a *different percentage gain* depending on how large the model-load
component is. The corpus already records `model_id`, `quantization`, and `backend`
in detail bundles (Ch10 §3 / runs schema) but has **never varied them while holding
the machine and preset fixed.** Ch10 lists "OpenVINO/SYCL parity matrix on fleet
hardware" as an open task; this is the cold-start half of that question.

This matters now because the next architectural decision is the **fitness key**:
does CursiveRoot store a winning preset per `(hardware_class)`, or must it key on
`(hardware_class × model × quantization × backend)`? If the cold-start gain is
model-portable, one preset serves a machine's whole model zoo and the selection
space stays small. If it is not, the fitness surface multiplies and every
"hardware-scoped preset" claim silently inherits a hidden model scope.

## 1. Hypotheses (falsifiable)

**H1 (absolute-saving invariance — primary).** On Stardust, with the validated
v0.9c cold-start preset and the desktop's deep-idle state held fixed, the
**absolute** cold-start saving (baseline TTFT − tuned TTFT, in ms) is statistically
indistinguishable across served models/quantizations/runtimes, because it reflects
a model-independent idle-exit latency.

**H0 (null for H1).** The absolute saving varies materially (> the cold-start noise
floor, expressed in ms) across model/runtime configurations — i.e. the preset's
cold-start benefit is itself model- or backend-dependent, not a fixed idle-exit
constant.

**H2 (percentage-gain dilution — secondary, the architecturally decisive one).**
Even if H1 holds, the **percentage** cold-start gain shrinks monotonically as the
model-load component grows (larger model, higher-precision quant, heavier-init
backend), because a fixed idle-exit saving is a smaller fraction of a larger total
TTFT. Falsifiable prediction: rank configs by baseline model-load time; percentage
gain is negatively correlated with that rank (Spearman ρ < 0, resolvable given the
0.002 CV).

**H2-null.** Percentage gain is flat across configs (no correlation with model-load
weight). This would mean the gain is reported-percentage-portable and the fitness
key can ignore the model dimension entirely.

## 2. Fitness, channel, and what is held fixed

- **Channel:** cold-start only (CV 0.002; the one channel solid enough to decide,
  per Ch00 §5.7). Network, sustained, and idle power are recorded as telemetry/guard
  rails, never as the comparison signal — same discipline as
  `proposer-vs-random-tuning-experiment.md` §2.
- **Two fitness readouts, kept separate:** absolute saving (ms) for H1 and
  percentage delta for H2. Conflating them is the exact error the experiment exists
  to expose.
- **Held fixed:** machine (Stardust), preset (v0.9c — the validated winner minus the
  dead GPU pin, Ch00 §5.1), deep-idle settle protocol, and **page-cache state**.
  Page cache is a known cold-start confound (Ch00 §2.3;
  `cold-start-order-cache-confound-plan.md`): for every config, apply one fixed,
  documented policy (e.g. drop caches identically before each cold measurement so
  the load component is true disk+init, *or* pre-warm weights identically so the
  measured penalty is idle-exit only) and record `page_cache_state`. Run both
  policies if cheap — the gap between them *is* the model-load component and directly
  tests H2.
- **Varied (the only independent variable):** the inference configuration.

## 3. Configuration matrix (the independent variable)

Pick a small, diagnostic set that spans the model-load axis while staying within the
operator's existing local stack (Ch10 §2 table). Suggested ~6 cells:

| Cell | Model / size | Quant | Runtime / backend | Why it's in the matrix |
| --- | --- | --- | --- | --- |
| 1 | Small (≈3B) | Q4_K_M | Ollama/llama.cpp default | Light load component — upper bound on % gain |
| 2 | Mid (≈7–8B, the Hermes-class deployed model) | Q4_K_M | current production path (OVMS/Ollama) | The on-record reference config |
| 3 | Mid (≈7–8B) | Q8 | same backend as cell 2 | Isolates quantization at fixed model |
| 4 | Mid (≈7–8B) | Q4_K_M | llama.cpp **SYCL** | Isolates Intel-GPU backend on Arc |
| 5 | Mid (≈7–8B) | Q4_K_M | **OpenVINO** | Isolates Intel graph-runtime init cost |
| 6 | Large (≈13–14B) | Q4_K_M | best working Arc backend | Heavy load component — lower bound on % gain |

Cells 2↔3 isolate quantization; 2↔4↔5 isolate runtime/backend; 1↔2↔6 sweep model
size. Use only configs that already run on the host — this is a measurement design,
not a porting project. Drop any cell whose backend is not production-ready on the
fleet GPU (Ch10 flags SYCL-on-all-GPUs and OpenVINO>Vulkan-on-Arc as Unvalidated;
record a "did not run" rather than forcing it).

## 4. Protocol

Use the existing harness and cold-start sensor (Ch10 §"Cold-start sensor"; Ch00 §1).
No new measurement machinery — only a config-swap loop around the existing baseline-
vs-preset cold-start run.

1. For each cell, measure **baseline** (no preset) and **v0.9c preset** cold-start,
   ≥ 6 paired cold measurements each (CV 0.002 → 6 is ample; matches the noise-floor
   and mechanism plans).
2. Enforce the fixed deep-idle settle and the chosen `page_cache_state` policy
   identically in every cell.
3. **Counterbalance:** randomize cell order; interleave baseline/preset within a cell;
   interleave cells across sessions to absorb thermal/drift (the "repeat and
   counterbalance before acceptance" rule, RESEARCH_PIPELINE §3; Ch00 §5.9).
4. Verify the preset actually applied each time via phase-context telemetry — an
   unverified knob is indistinguishable from a failed apply (Ch00 §5.1 lesson).
5. Compute, per cell: baseline TTFT, tuned TTFT, **absolute saving (ms)**,
   **percentage delta**, and the baseline model-load component (warm-vs-cold split if
   both cache policies were run).

## 5. Required evidence per run

```text
run_id
date_time_utc
host_id / hardware_fingerprint          # Stardust, fixed
kernel_version
model_id
model_param_count
quantization                            # Q4_K_M | Q8 | ...
backend                                 # ollama | llama.cpp-sycl | openvino | ...
runtime_version                         # ollama_version / llama_cpp_commit / ov_version
preset_id                               # baseline | v0.9c
governor_applied, governor_verified
page_cache_state                        # warmed | dropped (held constant per cell)
cold_ttft_ms, warm_ttft_ms
model_load_ms                           # if warm/cold split available
cold_start_abs_saving_ms                # baseline_ttft − tuned_ttft
cold_start_delta_pct
n_paired_measurements
session_id, cell_order_index
```

This is the Ch10 runs schema (`model_id`, `quantization`, `backend`,
`page_cache_state`) plus an explicit `cold_start_abs_saving_ms`, so results are
CursiveRoot-ready and answer the fitness-key question directly.

## 6. Success criteria

| Outcome | Decision |
| --- | --- |
| Absolute saving (ms) flat across cells (H1 holds) **and** % gain falls with model-load weight (H2 holds, ρ < 0) | **Cold-start fitness key = `(hardware × preset)` in ms, not %.** Store the absolute idle-exit saving; treat the percentage as a derived, model-dependent display number. Architecturally clean: one preset serves a machine's whole model zoo; the apparent "−51%" is just the saving measured against a mid-weight model. Update Ch00 §2.3/§5 and the VALIDATION cold-start rows to scope the headline percentage to its model. |
| Absolute saving varies materially across cells (H1 falsified / H0) | **The preset's benefit is itself model- or backend-dependent.** Fitness key must include `(model, quant, backend)`; "hardware-scoped preset" claims silently carried a hidden model scope. Flag in VALIDATION; re-derive cold-start presets per backend class before any fleet preset claim. |
| % gain flat across cells (H2 falsified) | Gain is reported-percentage-portable; the model dimension can be ignored for selection. The strongest, simplest result for the architecture — but the least likely given the mechanism (see §7). |
| Backend cells (SYCL/OpenVINO) fail to run or diverge wildly | Records that the cold-start signal is not yet backend-portable on Arc; feeds Ch10's open OpenVINO/SYCL parity matrix rather than the fitness-key decision. |

Promotion follows the existing acceptance discipline (counterbalanced, preset apply
verified, beats noise floor, telemetry recorded) used by the seed-organism screen and
the proposer-vs-random plan.

## 7. Expected outcome (pre-registered honest guess)

Best guess, stated so it can be wrong: **H1 holds and H2 holds.** The −51% headline
is an artifact of measuring a roughly *constant* idle-exit saving against a
*mid-weight* model. Swap to a 3B model and the same absolute saving will read as a
larger percentage; swap to a 13B model and it will shrink toward the teens — not
because the preset got worse, but because the denominator grew. This mirrors the
corpus's repeated lesson that headline percentages are denominator games (the
loopback "+246%" BDP artifact, Ch00 §5.6; the cold-start order/cache confound,
§2.3). If instead the **absolute** saving itself moves with the model (H0), that is
the more surprising and more consequential result, because it means the idle-exit
story is incomplete and presets cannot be model-portable even on one machine.

## 8. Feasibility

- Hardware: Stardust only — already the noise-floor and mechanism reference machine.
- Models/runtimes: drawn from the operator's existing local stack (Ch18 Hermes-class
  deployment; Ch10 Ollama / llama.cpp / OpenVINO / SYCL). No new models need training
  or porting; skip any cell that does not already run.
- Harness: existing cold-start sensor + preset apply/revert + `run_detail_bundles`.
  New work is a thin config-swap loop and the `cold_start_abs_saving_ms` /
  `model_load_ms` emitter — graduates to the main `CursiveOS` repo per the workflow
  boundary. No kernel rebuild, no firmware, no generated code, no host mutation beyond
  the reversible allowlisted preset.
- Cost: ~one machine-day (6 cells × baseline+preset × ≥6 paired cold runs, plus
  counterbalancing sessions).

## 9. What would change our mind

Per RESEARCH_PIPELINE §3 ("What evidence would change our mind?"): a flat
**absolute** saving with a sliding **percentage** gain tells the project to store
cold-start fitness in milliseconds and stop quoting an unqualified "−51%," collapsing
the model dimension out of the fitness key. A model-dependent **absolute** saving
tells the opposite story — that the cold-start channel, the one signal the project
most trusts, carries a hidden model scope that must enter the selection key before
any cross-model preset claim. Either way, the result resolves the fitness-key fork
that the hardware-scoping plan alone cannot, and it does so on the cleanest channel
the corpus owns.

## 10. Boundaries

- This is an `experiments/` plan per CORPUS_WORKFLOW.md §4. The config-swap runner,
  harness emitter fields, and CursiveRoot schema additions belong in the main
  `CursiveOS` repo; this file is the design and the evidence bar.
- Read/measure-only except for the single reversible v0.9c preset; no firmware, no
  kernel build, no model fine-tuning.
- Outcomes update Ch00 §2.3/§5 (cold-start scope), Ch10 (model/runtime parity), and
  the VALIDATION.md cold-start rows; a confirmed model scope graduates into Chapter
  01's hardware-scoped-fitness work as an added key dimension.
