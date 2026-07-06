# Research Changelog

This file records meaningful changes to research guidance, validation status,
and corpus process. It is intended to be readable without reconstructing a
chain of supporting documents.

## 2026-07-06 (evening) - Laptop GPU inference enabled: 5x sustained token generation

Changed:
- **VALIDATION.md**: new Validated row — the laptop's CPU-bound sustained channel was a driver problem, not a hardware limit: the GTX 1650 ran nouveau, which ollama cannot use. Installing the Canonical-signed nvidia-580 driver (Secure Boot untouched) took tinyllama from 33.4 to ~166 tok/s (100% GPU) and enabled phi3 at ~25 tok/s (81% offload, 4 GiB VRAM limit). Stability probe clean; one unexplained reboot during the very first phi3 load is flagged as a watch item.

Reason:
- This is an environment change on a founder measurement machine: the sustained channel becomes real on the laptop (no more cpu-bound void), and all pre-change laptop sustained/cold-start magnitudes become CPU-era history that must not be compared across the boundary. Stardust remains CPU-bound pending an Intel Arc backend (ipex-llm / llama.cpp SYCL) — the laptop's 5x quantifies the value of that experiment.

## 2026-07-06 (later) - Evidence-gate + config-drift fixes verified live; pagecluster0 null confirmed cross-machine

Changed:
- **VALIDATION.md**: evidence-gate row updated to Validated (fixed) — honest hardware flags now void only their channel (CursiveOS `d69587a`); the same post-mortem exposed and fixed rig-local config drift (both founder rigs still ran retired network=0.40 weights, the source of Stardust's phantom −0.1198 fitness; `config_version` auto-heal verified live). Loop-closure row updated: laptop screen through the fixed gate → inconclusive 0.50 / fitness −0.0023 / sustained voided; pagecluster0 null confirmed on both machines and retired.

Reason:
- The cycle-5 defect pair is closed with live cross-machine evidence; the corpus record should show the verified fix, the corrected interpretation of Stardust's fitness number, and the knob retirement.

## 2026-07-06 - Cycle 5: first fully autonomous loop closure + evidence-gate finding

Changed:
- **VALIDATION.md**: two new rows. (1) Autonomous loop closure Validated on one machine — proposer-materialized v0.13-pagecluster0 went enqueue → daemon claim → screen → upload → trust-spine rows with zero founder screen steps; candidate neutral on all weighted channels (honest null for the pre-registered page-cluster hypothesis). (2) Evidence gate bug Validated — the hardened gate fraud-rejects honest founder-rig runs because `sustained_inference_cpu_bound` voids the whole bundle instead of the sustained channel; contradicts the pre-registered V honest-control bar.

Reason:
- Cycle 5 is the first loop iteration where the organism proposed, coordinated, and measured its own experiment; both the closure and the gate defect belong in the corpus record before the gate fix lands.

## 2026-07-06 - Three red-team flags resolved (Mesa 260%, AlphaEvolve 23%, Ch15 truncation)

Changed:
- **chapters/20-market-and-viability.md**: living layer gains two "Superseded or narrowed (do not cite externally)" rows — AlphaEvolve "23% for Bittensor nodes" (Google-internal TPU training-kernel result, never Bittensor/Arc) and Mesa 26.1 "for miners … 260%" (single DX11 game trace from a depth-buffer graphics fix; not a compute path).
- **chapters/14-gpu-and-accelerator-tuning.md**: living layer "Superseded or narrowed" gains the Mesa 260% narrowing (graphics-only; real Arc compute gains ≤~40% best-case OpenCL).
- **chapters/15-ai-guided-tuning.md**: the end-of-file truncation is now confirmed to exist in the preserved source DOCX itself (unpacked blob a17532ea ends at the identical `AutoOS → TAO` fragment). A corpus note at the truncation point records this; the import is faithful and the partial row stays.
- **VALIDATION.md**: the three corresponding flag rows are resolved/deleted; three closure rows added to Current High-Impact Claims (AlphaEvolve Disproven-as-attributed, Mesa Disproven-as-compute-magnitude, Ch15 truncation Validated-at-source).

Reason:
- These were the remaining escalated red-team flags actionable without new hardware experiments. The BBR single-flow/default-preset flag remains open — it is gated on the Ch09 multi-flow fairness/retransmit experiment (Gap #3/#5) and a human decision on default-preset/public copy.

## 2026-06-30 - Corpus retrieval synonym/anchor fallback

Changed:
- **tools/corpus_retrieval.py**: added default `--expand auto` search fallback for non-raw queries: stopword trimming, lexical variants, singular/plural/suffix variants, and a rare-anchor fallback when strict terms do not co-occur.
- **tests/test_corpus_retrieval.py**: added regression coverage proving a founder-risk query can recover the founder-as-normal-contributor passage while `--expand never` remains strict.
- **docs/corpus-retrieval.md**: documented fallback behavior, `--explain`, `--expand never`, and added the founder-risk transition to the query cookbook/audit scope.

Reason:
- Exact keywords are brittle. The retrieval CLI should help agents recover corpus concepts even when a user's phrasing differs from the corpus wording, without immediately adding embeddings or requiring a hand-curated synonym list.

## 2026-06-30 - Corpus retrieval polish: filters, audit, canonical verification

Changed:
- **tools/corpus_retrieval.py**: added `--path` and `--heading` search filters, `index --if-stale`, `status --changed-only`, and a built-in `audit` command for known high-value retrieval queries.
- **tests/test_corpus_retrieval.py**: expanded focused coverage for filters, status/index ergonomics, and retrieval audit behavior.
- **tools/run-verification.ps1**: made retrieval self-test, focused unittests, index/status check, and audit part of canonical corpus verification.
- **docs/corpus-retrieval.md / CORPUS_WORKFLOW.md**: added query cookbook examples and updated the normal corpus-maintenance habit to use `index --if-stale` plus `status --changed-only`.

Reason:
- The first retrieval spine was usable; this pass makes it harder for agents to forget, easier to narrow searches, and guarded by the same verification path as the rest of the corpus.

## 2026-06-30 - Repo-native corpus retrieval spine

Changed:
- **tools/corpus_retrieval.py**: added a local SQLite FTS5 retrieval CLI with Markdown-section chunking, cited `path:start-end` search results, JSON output for agents, status/staleness checks, and a self-test.
- **docs/corpus-retrieval.md**: documented the retrieval workflow, including how agents should index/search/show passages and avoid committing generated cache data.
- **CORPUS_WORKFLOW.md / README.md**: made retrieval refresh and representative search visible in the normal corpus-maintenance path after adding or materially editing corpus Markdown.
- **tests/test_corpus_retrieval.py** and `.gitignore`: added focused regression coverage and ignored generated `.cursive-research-rag/` indexes.

Reason:
- CursiveResearch is the grounding corpus for CursiveOS agents. A small repo-native retrieval layer lets agents cite local evidence before making implementation claims, while keeping generated indexes rebuildable instead of turning the corpus into a heavier RAG platform.

## 2026-06-30 - Branch sweep: pending Claude corpus work + Windows verification fix

Changed:
- **Merged pending Claude corpus branches into main**: Chapter 16 shared-GPU isolation, Chapter 24 contributor data privacy / telemetry governance, Ch08 sabotage-tolerance simulation plan, Mesa 26.1 Arc compute/mining red-team challenge, and Flagged-for-Review triage escalations.
- **tools/run-verification.ps1**: made mojibake-regex literals ASCII-only so the canonical verification script runs under Windows PowerShell 5.1 when the repo file is UTF-8 without a BOM.

Reason:
- These remote branches contained decision-driving corpus/security/privacy work that was not on `main`, and the verification script itself needed a small portability fix before the normal documented command could verify the merge on this Windows host.

## 2026-06-27 - Concurrency sensor noise-floor gates: H1/H2 pass, H3 blocked

Changed:
- **experiments/concurrency-inference-sensor-noise-floor-plan.md**: results table + blocked status (H3 null: 0% v0.8 vs v0.12 on Stardust).
- **VALIDATION.md**: new concurrency inference sensor row (repeatable, not discriminative for memory-class stack).
- **Chapter 01**: concurrency paragraph — CV validated, weight stays 0, next axis = scheduler tweak.
- **RESEARCH_PIPELINE.md**: concurrency rows updated to H1/H2 pass / H3 blocked.

Reason:
- Founder-fleet H1/H2/H3 runs complete on Stardust + laptop; concurrency is measurement-grade but cannot gate selection on current parent stack.

## 2026-06-26 - Cycle 3 closed: v0.11 accepted, parent promoted to v0.12

Changed:
- **VALIDATION.md**: v0.11 row updated to accepted/closed cycle 3 (confidence 0.875, three confirmations).
- **Chapter 01**: living layer records cycle-3 accept and v0.12 parent promotion; concurrency sensor named as next gap.
- **RESEARCH_PIPELINE.md**: cycle-3 screen row closed; concurrency inference sensor kickoff row added.
- **experiments/concurrency-inference-sensor-noise-floor-plan.md**: new pre-registered plan for parallel-stream tok/s probe.

Reason:
- CursiveOS HANDOVER documents cycle 3 accept and v0.12 promotion; corpus must match so agents do not re-run confirmation work.

## 2026-06-26 - Drift cleanup: v0.11 memory channel is current, validated, and integrated

Changed:
- **INDEX.md**: reconciled the chapter count with the tracked corpus and verification contract: 26 chapter files (00–23 logical slots plus 03c/03d inserts), not 25.
- **tools/verification-contract.json**: marker expectations now match the actual 26 living-layer / reinforced chapter files.
- **Chapter 01**: moved the memory-pressure section out of stale "prototype / not wired" language. It now records the validated v0.2 sensor, harness/fitness integration, and the cycle-3 v0.11 screen result: v0.11 vs v0.9 fitness **+0.0954**, memory **+75.4%**, cold-start **−0.5%**, sustained **0.0%**, idle **−0.1%**, network **−24%** gate-only loopback noise, single-screen confidence 0.50.
- **experiments/memory-pressure-sensor-noise-floor-plan.md**: marked the pre-registered plan completed and attached the measured results rather than leaving it as proposed/unvalidated.

Reason:
- The corpus and main repo had crossed the measurement boundary, but some navigation and experiment-plan text still described the memory channel as future work. This cleanup keeps agents pointed at the current real result: zram alone is neutral under `swappiness=0`; v0.11 (`v0.9 + zram + swappiness=60`) is the active cycle-3 candidate needing confirmation/promotion.
## 2026-06-26 - Chapter 16: GPU memory isolation for shared accelerators

Changed:
- **`chapters/16-security-and-hardening.md`**: added one additive section, **"GPU
  memory isolation: shared accelerators as a cross-tenant leakage and
  measurement-integrity surface"** (inserted after the AI-model-supply-chain section,
  before the DePIN section; no existing content rewritten — file 258 → 395 lines, all
  prior `##`/`#` headers intact). It fills a real gap: [Chapter 14](chapters/14-gpu-and-accelerator-tuning.md)
  actively recommends sharing one physical GPU (SR-IOV `i915-sriov-dkms` up to 7 VFs,
  AMD MxGPU/GIM, NVIDIA MIG) for concurrent mining + LLM inference, but never states
  that co-residency is a trust boundary or that most consumer sharing modes provide no
  memory isolation. The section characterizes the surface (**LeftoverLocals /
  CVE-2023-4969** — co-resident process reads another LLM's leaked GPU local memory,
  ~181 MB/query on RX 7900 XT + llama.cpp; AMD/Apple/Qualcomm/Imagination affected,
  NVIDIA/Arm not), contrasts isolation by sharing mode (MIG hardware memory boundary
  vs time-slicing/MPS no isolation vs consumer SR-IOV scrub gap **[unverified]**),
  notes **GPU.zip** (IEEE S&P 2024) as a separate isolation-failure class, and maps it
  onto the daemon/shell split with a CursiveOS-implications table + design rules
  (sole-tenant/MIG measurement runs; tenancy in the fitness key; pin/track GPU driver
  vs leak advisories; keep leaks off the Ch06 daemon write path).
- **`VALIDATION.md`**: added one decision-driving claims-table row ("Chapter 16 /
  shared-GPU isolation", **Supported**) — sole-tenancy/MIG for measurement runs,
  record GPU tenancy/isolation mode in CursiveRoot evidence, do not pool shared-GPU
  runs with sole-tenant runs for selection.

Reason:
- Chapter 14's GPU-multiplexing guidance had no security precondition, and Chapter 16
  (security) had no GPU-isolation content at all. Because CursiveOS contributors may run
  the fitness harness on multi-tenant cloud GPUs or co-reside two organisms on one local
  card, a shared GPU is simultaneously a confidentiality risk (a co-tenant reads weights/
  prompts/activations) and a measurement-integrity risk (a co-tenant perturbs a benchmark
  sharing the card) — the Goodhart/Ch08 confirmation and Ch01 immune-sensor problem
  arriving through hardware rather than the optimizer. Maps to RESEARCH_PIPELINE P1
  "Hardware Optimization Foundations / GPU runtime stacks" and the security chapter, and
  bridges Ch14↔Ch16. The section is additive and over-claim-guarded: every external
  figure is marked retrieval-caveated (primary Trail of Bits/CERT/AMD pages returned 403;
  search-summary level) and the consumer `i915-sriov-dkms` scrub question is marked
  **[unverified]**, deferred to the Ch14 GPU capability probe.

Sources: Trail of Bits — LeftoverLocals (CVE-2023-4969, blog.trailofbits.com 2024-01-16);
CERT/CC VU#446598; AMD-SB-6010; BleepingComputer LeftoverLocals coverage; NVIDIA
Multi-Instance GPU technology page + vGPU User Guide; Kubenatives / OpenMetal MIG-vs-
time-slicing-vs-MPS comparisons; GPU.zip (hertzbleed.com/gpu.zip, IEEE S&P 2024) via
BleepingComputer. All retrieved at search-summary / vendor-page level this pass; not
locally reproduced.
## 2026-06-26 - Red-team challenge: Mesa 26.1 "260%" reframed as an Intel Arc compute/mining uplift (Ch14 + Ch20)

Changed:
- **`VALIDATION.md`**: added a "Flagged for Review" row (red-team) challenging the reuse of the third-party "up to 260%" Mesa 26.1 figure as (a) a "specific **compute** scenarios" boost in Chapter 14 and (b) a "**for miners** … 260%" uplift shipped as a default in Chapter 20. No chapter text was edited (challenge-only, per CORPUS_WORKFLOW §3).
- **`validation/notes/2026-06-26-ch14-ch20-mesa-260pct-arc-compute-mining-misattribution-redteam-challenge.md`**: full evidence note.

Finding:
- The 260% is a **single DirectX 11 game trace** (NBA 2K23, 4K Ultra) produced as a side effect of Mesa 26.1's HiZ-CCS depth-buffer **graphics-corruption** fix on Intel Alchemist/Meteor Lake GPUs — Linux-only, Windows-untested, and explicitly non-generalized per the corpus's own cited sources (TechPowerUp Works-cited #32; Wccftech #35). A depth-buffer resolve lives in the 3D rasterization path and has no mechanism to raise GPGPU **compute** (oneAPI/OpenCL/SHA-256) throughput, so re-labeling it a "compute" (Ch14) or "miners" (Ch20) gain is a category error. The on-point Arc compute measurement (Phoronix *Xe vs i915*, Linux 6.19) shows ≤~40% best-case OpenCL and "minimal" elsewhere — roughly an order of magnitude below 260% — and the corpus's own sources #16/#62–#64 already note Arc compute on Linux is under-delivered.

Reason:
- Intel Arc is CursiveOS's primary documented GPU (Arc A750 in Ch00, B70 in Ch18), so 260% is the sole quantified magnitude behind the Arc GPU-tuning differentiator, and Ch20 elevates it to a contributor default and investor-facing market copy. This is the same misattributed-magnitude failure mode as the 2026-06-24 AlphaEvolve "23% for Bittensor" flag. The challenge does not dispute the real (graphics) result — only its reuse as a compute/mining number. Per the flag, any first-party Arc GPU-tuning magnitude must be earned on the Ch00 harness for the actual workload (cf. CH05-BM-002, Ch08 hardware-scoped fitness) before it ships as a default or a public claim.

Sources: TechPowerUp #345740 (single NBA 2K23 DX11 trace); Wccftech Mesa-260% report; Phoronix *Intel Xe vs. i915 … Linux 6.19* (OpenCL ≤~40%); Ch20 Works-cited #16/#62–#64; internal `2026-06-24-ch20-alphaevolve-23pct-bittensor-overstatement-challenge.md`, Ch00/Ch08/Ch15.
## 2026-06-26 - Experiment plan: adversarial sabotage-tolerance test of Ch08 confirmation

Changed:
- **experiments/**: added `sabotage-tolerance-confirmation-simulation-plan.md`, a
  pre-registered, falsifiable plan that answers the explicit open item left by
  Chapter 03d §5 and the RESEARCH_PIPELINE §2 P0 knowledge gap ("adversarial test
  of whether Ch08 confirmation behaves as a sabotage-tolerance layer"). It is a
  Monte-Carlo simulation of the **exact Ch08 §2 rule** (N = max(1,min(5,floor(sqrt(fleet)))),
  CV>0.15→N+2, hardware-scoped pooling, optional Ch08 §5 effective-N downgrade),
  **seeded by already-measured corpus constants** — Ch00 per-channel CVs
  (cold-start 0.002, network 0.192) and the hardware-scoped −51% / ~0% cold-start
  split — so the error curves are grounded, not a toy. It sweeps saboteur fraction
  f and fleet_size across four corpus-anchored attack models (independent liars,
  Sybil cluster, Goodhart gamer on the high-weight network channel, and a griefer
  that suppresses a real win), with pre-registered accept-bad / reject-good
  thresholds (Sarmenta's two-sided failure modes; Byzantine one-third bound).
- **RESEARCH_PIPELINE.md**: updated the P0 "hardware-scoped truth" knowledge-gap
  row to mark the adversarial test as delivered-as-plan, and added a row to the
  Experimental Lift table.

Reason:
- The corpus has reasoned about confirmation-under-attack only by analogy (Ch03d
  Sarmenta/BOINC lineage, Ch08 §5 immune sensors, the Skalse Goodhart warning) and
  has never measured the rule's actual error rates with an adversary in the loop —
  yet all twelve existing experiment plans are physical hardware-tuning runs with
  no saboteur. The moment Layer 5 (Ch02) attaches real BTC to measured fitness, the
  confirmation rule becomes a security boundary (a contributor is paid to lie), and
  the cheap time to find that the rule accepts a one-third lie — or is trivially
  griefed into rejecting honest wins — is in simulation now, not after money is on
  the fleet. The plan is pure Monte-Carlo (no hardware, no fleet, no funds at risk),
  shares its rule implementation with the live hub analyzer so the thing tested is
  the thing deployed, and yields "Supported by simulation" bounds that gate Ch02
  payout sequencing and the Ch08 §10 open calibration gaps.

Sources / anchors: Sarmenta (FGCS 2002, sabotage-tolerance); Anderson (BOINC,
arXiv:1903.01699); Skalse et al. (NeurIPS 2022, reward hacking); Ch00 noise-floor
data; Ch08 N-rule + immune sensors; Ch03c/03d decentralized-evaluator framing.
## 2026-06-26 - New Chapter 24: Contributor Data Privacy and Telemetry Governance

Changed:
- **New chapter `24-contributor-data-privacy-and-telemetry-governance.md`** (native, full living layer + reinforced research). Closes a standing corpus gap: the corpus rigorously specifies **what to measure** on a contributor's machine (Ch00 schema, Ch01 sensors, Ch08 fleet statistics) and **what may mutate** it (Ch06 permission law), but never **what may leave it**. The chapter: (1) argues a network that pays BTC (Ch02) for on-host measurement on other people's machines is a personal-data processor, not an anonymous mesh; (2) shows the corpus already built its own re-identification surface — the Ch11 fingerprint is a deliberately unique high-entropy key (calibrated against Eckersley's ≥18.1-bit Panopticlick result) and the Ch02 wallet links it to a financial identity, so "anonymous telemetry" is false; (3) reframes the privacy↔fleet-statistics tension via RAPPOR's central-collector conflict; (4) surveys the mitigation menu (data minimisation, pseudonymisation/salted hardware-*class* token, local DP, federated analytics) and argues the Ch08 estimators are population aggregates well-suited to federated analytics, with local DP reserved for coarse high-N counts; (5) imports the Tang et al. macOS-DP finding (a renewing privacy budget leaks cumulatively) as the governance guardrail; (6) recommends an observe-and-measure posture: minimise + segregate payout from telemetry + aggregate on-device now, but measure the utility cost on the Ch08 estimators (CV/median/fitness) before any privacy mechanism gates the pipeline.
- **INDEX.md**: added the Chapter 24 row, bumped the header to "27 files: 00–24 logical slots plus 03c/03d inserts," and noted 24 as a cross-cutting native chapter linking Ch08/11/02/05/06.
- **tools/verification-contract.json**: `chapters_total` 26→27, `native_chapters` += "24", `all_chapters_living_layer` 26→27, `all_chapters_reinforced` 26→27.

Reason:
- The DePIN model runs on contributors' personal/business hardware and pays them, which makes telemetry a *disclosure* problem, not just a measurement problem — yet no chapter drew the transmitted-vs-read line, named a consent/legal basis, or reckoned with the re-identification risk the Ch11 fingerprint and Ch02 payout jointly create. The chapter is deliberately Unvalidated as a deployed pipeline: minimisation is a free win, but federated analytics / local DP must have their accuracy cost on the Ch08 0.15 CV gate measured before they gate selection, lest the network trade a real measurement capability for a privacy property it could reach more cheaply.

Sources: Erlingsson, Pihur, Korolova "RAPPOR" (ACM CCS 2014); Eckersley "How Unique Is Your Web Browser?" (PETS 2010, Panopticlick); Tang et al. "Privacy Loss in Apple's Implementation of Differential Privacy on macOS 10.12" (arXiv:1709.02753, 2017); Kairouz et al. "Advances and Open Problems in Federated Learning" (arXiv:1912.04977, 2021) + Google Federated Analytics; EU GDPR Art. 4/5/6 + Recital 26.

## 2026-06-25 - Cornerstone full-text repair: FunSearch, LADDER, DGM, Open-Endedness

Changed:
- **Full-text storage repaired for CC BY 4.0 cornerstone papers**:
  - `papers/recursive-self-improvement/funsearch/`: added Nature Open Access / CC BY 4.0 `paper.pdf` and full PDF-derived `paper.md`.
  - `papers/recursive-self-improvement/ladder/`: replaced the partial abstract/core-excerpt `paper.md` with full PDF-derived text and added `paper.pdf`.
  - `papers/recursive-self-improvement/darwin-godel-machine/`: added `paper.pdf` and full `paper.md` from arXiv:2505.22954v3.
  - `papers/recursive-self-improvement/open-endedness-icml-2024/`: added `paper.pdf` and full `paper.md` from arXiv:2406.04268v1.
- **Metadata repaired** in folder READMEs, `deep-extraction.md`, `claims-and-results.md`, `sources/source-register.md`, `sources/peer-reviewed-rsi-selected-sources.md`, and `papers/TIER-RECONCILIATION.md` so agents no longer believe these cornerstone folders are abstract-only.
- **New audit artifact**: `papers/FULL-TEXT-AUDIT-2026-06-25.md` maps cornerstone full-text status, source/license basis, remaining rights constraints, and strategic next actions.

Reason:
- CursiveResearch is becoming the project-alignment/spec corpus for multiple agents and future specialized models. Cornerstone papers cannot remain summaries-of-summaries when rights-cleared full text is available; the corpus needs source-preserving, auditable, agent-readable paper bodies before strategic extraction/model-training decisions.
## 2026-06-25 - New Chapter 23: Energy Efficiency and Performance-per-Watt as a Fitness Channel

Changed:
- **New chapter `23-energy-efficiency-and-performance-per-watt.md`** (native, full living layer + reinforced research). Addresses a standing corpus gap: energy appears only as the **idle-power penalty** (Ch00 §2.2), never as a positive **energy-per-task / performance-per-watt under load** signal — yet that is the most defensible operationalization of Ch02's "proof of useful optimization." The chapter: (1) argues work-per-joule is monotone with the real electricity externality, work-normalized, and Goodhart-resistant vs speed-only channels; (2) tabulates what `read_watts` actually reads (RAPL `package`/`psys`/`DRAM`, AMD core/package, GPU hwmon, NVML) and why unlabeled watts are non-comparable across domains; (3) documents the **privilege collision** — since PLATYPUS (CVE-2020-8694/8695) `energy_uj` is root-only and the unprivileged AMD `amd_energy` path was removed in Linux 5.13, contradicting the Ch05/Ch06 least-privilege daemon, with a least-bad `setuid` read-only helper proposed; (4) imports MLPerf Power (samples/joule) and SPECpower (ssj_ops/watt) methodology and the fixed-work / dynamic-energy / thermal-DVFS / sampling-artifact confounds; (5) recommends observe-only adoption until a fleet CV clears the Ch08 0.15 gate.
- **INDEX.md**: added the Chapter 23 row, bumped the header to "25 files, 00–23 logical slots," and noted 23 as a cross-cutting native chapter linking Ch00/02/06.
- **tools/verification-contract.json**: `chapters_total` 24→25, `native_chapters` += "23", `all_chapters_living_layer` 24→25, `all_chapters_reinforced` 24→25.
- **RESEARCH_PIPELINE.md**: marked the P1 "Power-state latency / Memory pressure" energy strand and the idle-power experiments as partially served by Chapter 23 (energy-as-fitness framing now exists; measurement/experiments remain open).

Reason:
- The economic thesis pays for *useful* optimization but the fitness schema had no work-normalized efficiency channel — only a machine-specific idle-power penalty. Energy-per-task is the cleanest hardware-grounded definition of "useful" and a built-in counterweight to the speed-only Goodhart (a clock-boost mutation that wins cold-start while burning 2× energy should be visible as a loss). The chapter is deliberately Unvalidated as a deployed channel: the PLATYPUS privilege restriction and RAPL domain non-comparability are real blockers that must be solved (labeled schema + setuid helper + wall-meter calibration) before any fitness weight.

Sources: Khan et al. "RAPL in Action" (ACM ToMPECS 2018); Weaver "Reading RAPL energy measurements from Linux"; Lipp et al. PLATYPUS (CVE-2020-8694/8695); Linux powercap docs + `amd_energy` removal (5.13, `9049572fb`); MLPerf Power (arXiv:2410.12032); SPECpower_ssj2008; "16 Years of SPEC Power" (arXiv:2411.07062); Yang et al. nvidia-smi power measurement (arXiv:2312.02741).
## 2026-06-25 - Memory-pressure sensor noise-floor experiment plan

Changed:
- **experiments/**: added `memory-pressure-sensor-noise-floor-plan.md`, a pre-registered, falsifiable plan to measure the CV of the `benchmark-memory-pressure-v0.1.sh` refault-time probe before it can gate selection.
- **RESEARCH_PIPELINE.md**: added the experiment to the Experimental Lift table.

Reason:
- The probe is built but `Unvalidated` (no hardware noise floor). The plan runs the same gate every other channel cleared on 2026-06-16: H1 within-machine CV ≤ 0.15 on Stardust + the i5-11300H, plus H2 (zram `mm_stat` engagement) and H3 (zram/disk-swap/no-swap discrimination) as validity checks so a quiet channel is not mistaken for a discriminating one. Only on H1–H3 pass does it integrate the probe as a weighted fifth fitness channel and re-screen the inconclusive `candidate-v0.10-zram` (H4). This is the cheapest experiment in the queue (instrument already exists) and the one that unblocks the entire zram / memory-class thread.
## 2026-06-25 - Red-team challenge: unscoped "switch to BBR" headline / default preset

Changed:
- **VALIDATION.md**: added a "Flagged for Review" (red-team) row challenging the
  unscoped promotion of the single-flow CUBIC→BBR win to a Validated public claim,
  a fleet default preset, and the 0.40 network fitness driver.
- **validation/notes/2026-06-25-ch09-bbr-default-overstatement-redteam-challenge.md**:
  new red-team challenge note.

Reason:
- The corpus's CUBIC→BBR decomposition (real-path A/B, +1875% single flow, buffer
  stack ≈0%) is sound and is **not** disputed. What is challenged is the *scope*:
  every BBR measurement is a single iperf3 flow in isolation, yet the result is
  promoted to the canonical "switch to BBR" public/marketing line (VALIDATION
  "Chapter 00 / network headline"), a default preset for loss-prone workloads
  (Ch09 §7), and the highest-weighted fitness channel (0.40). Peer-reviewed
  multi-flow evidence contradicts an unscoped default: BBRv1 (the in-tree
  `tcp_bbr`) takes a roughly fixed bottleneck share (~40%) regardless of how many
  CUBIC flows it competes with (Ware et al., IMC 2019) and inflicts high
  retransmit loss in shallow buffers + RTT-unfairness (Hock et al., ICNP 2017) —
  Google built BBRv2/v3 specifically to fix this. A system-wide
  `tcp_congestion_control` change also has off-host blast radius (competing /
  neighbor traffic), making it a Chapter 06 mutation-safety concern. The
  challenge does not edit the Validated rows; it recommends scoping the claim to
  "single flow in isolation" and running Ch09 Gap #3/#5 (multi-flow fairness +
  ≥3-path confirmation) before any default-preset or marketing use.
## 2026-06-25 - AI model supply-chain security section (Ch16)

Changed:
- **Chapter 16** (`16-security-and-hardening.md`): added a `### AI model supply chain: malicious weights as a code-execution and measurement-integrity surface` subsection (additive, inserted after the IDS subsection / before the DePIN subnet-security block). It deepens the chapter's single existing control ("verify AI model hashes before loading") into a characterized attack surface for the local model-pull path (Ollama, `llama.cpp`/GGUF, Hugging Face — Ch10/Ch18) and maps it onto the daemon/shell split. Covers: pickle `torch.load` RCE vs `safetensors` safe-by-design (Trail of Bits audit, May 2023); scanner evasion (ReversingLabs "nullifAI" picklescan bypass, 2025-02); loader RCEs (Wiz Probllama CVE-2024-37032; Databricks GGUF parser bugs + llama.cpp CVE-2025-53630); and Unit 42 model namespace reuse. Adds a threat→control table and four organism design rules (format over scanning; loader = untrusted-input code → Ch05 sandbox; pin by sha256 digest not name → Ch11/Ch08; model RCE must not reach the Ch06 daemon write path). No existing content removed; chapter 152→258 lines.
- **VALIDATION.md**: new claims-table row "Chapter 16 / model supply chain" (Supported — external CVEs/incidents strong; CursiveOS controls not implemented).

Reason:
- Closes part of the P1 "Local Agent Architecture and Safety" pipeline item ("deeper prompt-injection/tool-attack survey") on the supply-chain axis specifically. A poisoned model is a dual threat for CursiveOS — host compromise during load/inference and Goodhart-style measurement gaming through the weights — and the corpus previously had only a one-line mention. The section is research synthesis with concrete daemon/shell implications, not an implementation spec; all claims trace to retrieved primary/secondary sources (HF/EleutherAI safetensors audit, ReversingLabs, Wiz, Databricks, llama.cpp GHSA-vgg9-87g3-85w8, Unit 42). It does not alter the existing DePIN/package supply-chain guidance, which remains authoritative for PyPI/dependency and consensus-layer threats.

## 2026-06-25 - zram needs swappiness>0; v0.11 swappiness-aware variant

Changed:
- **VALIDATION.md**: new row "Chapter 01 / zram needs swappiness > 0" (Validated).

Reason:
- Wiring the memory channel into the full harness (v1.4.5) and screening v0.10-zram surfaced a real result: zram does NOTHING under memory pressure while v0.9's `vm.swappiness=0` is set. On Stardust, v0.9 and v0.10-zram BOTH throttle to the probe cap (v0.10's zram is touched — ratio 55× — but the kernel won't swap to it). v0.11 (= v0.9 + zram + swappiness=60) drops to 10.86 s vs the capped 45 s — >4× faster, zram peak 648 MiB. So v0.10-zram correctly screens neutral and the actual improvement is the swappiness-aware v0.11. New artifacts: presets/cursiveos-presets-v0.11-zram-swappiness.sh + variant + probe per-rep timeout (bounds swappiness=0 throttle stalls). The tradeoff (swapping could evict model weights) is being checked by a full multi-channel v0.9-vs-v0.11 screen.

## 2026-06-25 - Memory-pressure sensor cross-machine confirmed + probe v0.2

Changed:
- **Chapter 01** + **VALIDATION.md**: added Stardust (Ryzen 7 5700 / 64 GB) confirmation to the memory-pressure sensor row; probe ref bumped to v0.2.

Reason:
- Cross-machine validation cleared the "second machine first" gate. Stardust: zram 11.56 s (CV 0.003) vs disk-swapfile 24.27 s — ~2× faster, low-noise, matching the laptop's direction. Key result: zram peak_orig ~647 MiB on BOTH the 16 GB laptop and 64 GB desktop, proving the cgroup ceiling (not total RAM) fixes the pressure regime — Chapter 08 comparability demonstrated directly. Absolute times are hardware-scoped (different disk-swap/CPU/governor); the within-machine zram-vs-disk delta is the portable signal. Probe v0.2 (CursiveOS `d4bbc90`) adds a background peak sampler that fixes the v0.1 engagement proof (endpoint read freed zram between reps → 0). Sensor is ready to integrate as a weighted 5th channel (provisional weight 0.10).

## 2026-06-25 - Memory-pressure sensor VALIDATED on laptop

Changed:
- **Chapter 01** + **VALIDATION.md**: memory-pressure sensor prototype row upgraded Unvalidated → **Validated** with the laptop result.

Reason:
- Counterbalanced hardware run (i5-11300H, WS 1024M/ceiling 384M, 5 reps/order) cleared the noise-floor gate. zram refault = 5.779 s median in BOTH orders (CV 0.006/0.019, cold-start tier); disk-swapfile baseline 13.9–14.1 s (CV 0.116/0.193). zram is 2.4× faster + 6–30× steadier; identical median across orders rules out warmup. The comparison is zram-swap vs the laptop's existing /swapfile (the realistic case). The sensor can now see what the genesis suite could not. Next: integrate as a lower-is-better 5th fitness channel; fix v0.2 mm_stat engagement proof (endpoint read frees zram between reps).

## 2026-06-25 - Memory-pressure sensor prototype (5th channel)

Changed:
- **Chapter 01**: added a "Prototype (2026-06-25)" paragraph under Performance Sensors describing `benchmark-memory-pressure-v0.1.sh` (CursiveOS `99e6996`) and updated Open Gap #6 to "prototype built; noise floor + integration pending".
- **VALIDATION.md**: new row "Chapter 01 / memory-pressure sensor prototype" (Unvalidated — built + statically validated, no hardware noise floor yet).

Reason:
- Close the design half of the memory-pressure gap exposed by cycle 2. The probe creates deterministic pressure via a cgroup-v2 `memory.high` ceiling and times faulting a fixed compressible working set back in; lower median = better. It is RAM-size-independent (laptop/desktop comparability), throttles rather than OOM-kills (safe unattended), engages zram even under v0.9 `swappiness=0` (cgroup-forced reclaim), and proves engagement via `/sys/block/zram0/mm_stat` (auditable). Prototype only — logs locally, not wired into fitness until a measured noise floor clears the same gate every other channel passed.

## 2026-06-25 - Cycle-2 zram inconclusive + memory-pressure sensor gap

Changed:
- **Chapter 01** (`01-seed-organism-and-sensor-array.md`): added a "Known coverage gap — no memory-pressure sensor" note under Performance Sensors, grounded in the cycle-2 `candidate-v0.10-zram` inconclusive screen; added Open Research Gap #6 (memory-pressure sensor + swappiness-aware variant).
- **VALIDATION.md**: two new rows — "Chapter 01 / zram cycle-2 screen" (Unvalidated, inconclusive: fitness ≈ +0.0136, confidence 0.50, single screen) and "Chapter 01 / memory-pressure sensor gap" (Supported).

Reason:
- Honest record of the organism's first *added* optimization (cycle 2). zram's benefit lives in a channel the genesis suite does not measure, so the screen correctly read neutral and only proved safe apply/revert + non-regression — pre-registered in the variant hypothesis. Treat zram as an unscreened lead, not a rejected one. Marginal deltas vs v0.9 (cold-start +0.11%, idle power −1.75%, network −3.77% gate-only, sustained +0.06%) are all inside the measured noise floor. The verdict bundle initially did not reach CursiveRoot because of the `seed_bundles` RLS upsert bug (fixed same day, CursiveOS `c65c5ef`, merge-duplicates → ignore-duplicates); it was then regenerated from the surviving CursiveRoot run data and uploaded (fitness +0.0136 supersedes an earlier in-session −0.0257 figure that could not be reproduced from stored data).
## 2026-06-25 - Ch15: Classical Autotuning Baselines (what the proposer must beat)

Changed:
- **Chapter 15 (`15-ai-guided-tuning.md`):** added one additive section,
  `## Classical autotuning baselines: what the proposer must beat (2026-06-25)`,
  inserted after the native `## Reinforced research` block and before the DOCX
  import (no existing content rewritten; 132 → 245 lines, all prior headers
  intact). Grounds the black-box-optimization baselines the corpus's load-bearing
  test **CH05-BM-002** (`experiments/proposer-vs-random-tuning-experiment.md`)
  compares against: random search (Bergstra & Bengio 2012, *JMLR* — low effective
  dimensionality; beats grid search at a fraction of compute), Bayesian
  optimization (Snoek *et al.* 2012, *NeurIPS* — GP surrogate, kernel-fragile),
  OpenTuner (Ansel *et al.*, PACT 2014 — ensemble + AUC-Bandit meta-technique,
  up to ~2.8× [needs full-text]), Hyperband (Li *et al.* 2017, *JMLR* — bandit +
  successive halving), and Google Vizier (Golovin *et al.*, KDD 2017 — productionized
  GP-bandit service). Includes a baseline→CursiveOS-implication table. Explicitly
  does **not** upgrade CH05-BM-002 (still Unvalidated); the architectural takeaway
  is to treat the LLM proposer as one arm in an OpenTuner-style portfolio judged
  by the external measurement daemon (Ch05/Ch06).
- **VALIDATION.md:** added a "Flagged for Review" row — Ch15's DOCX import is
  truncated mid-table at `| **AutoOS → TAO:*` (final timeline row cut off). Flagged,
  not edited.

Reason:
- Fills a real gap: the chapter surveyed LLM-driven tuners but never grounded the
  classical baselines those tuners (and CursiveOS's proposer) must beat to justify
  their compute. Without that grounding, a one-line baseline or chance over a small
  allowlist can masquerade as a proposer "win" — the exact failure mode that sank
  the "+246% network tuning" result. Maps to RESEARCH_PIPELINE P0 ("what RSI is real
  today vs theoretical") and P1 ("right evaluation stack for OS-operating agents").
- Sources retrieved at abstract/publisher-summary level via web search; OpenTuner
  specifics from secondary summaries (PACT PDF 403) and marked [needs full-text].
  No numbers locally reproduced.
## 2026-06-24 - New Chapter 03d: Verifying Decentralized Computation (untrusted-evaluator prior art)

Changed:
- **New chapter `03d-verifying-decentralized-computation.md`:** source-backed external
  survey of how prior systems verify computation done by untrusted, paid, remote
  machines — directly answering the frontier Ch03c §5 names ("decentralizing the
  evaluator is the unsolved hard part"). Surveys five verification families with
  canonical citations: redundant execution + statistical spot-checking
  (Sarmenta 2002; BOINC, arXiv:1903.01699), interactive dispute / refereed
  delegation (Truebit, arXiv:1908.04756; Gensyn Verde, arXiv:2502.19405), TEE
  remote attestation (Intel TDX / AMD SEV-SNP; SIGMETRICS-2025 + SoK arXiv:2503.08256),
  cryptographic validity proofs (zk-SNARK/STARK), and consensus over subjective
  scores (Bittensor Yuma Consensus). Organizes the space on the **optimistic vs.
  validity** axis and argues — with explicit disanalogies — that CursiveOS's
  hardware-scoped, non-reproducible, partly-subjective fitness can inherit only
  the **statistical, credibility-weighted, attestation-assisted** end (reframing
  Ch08 as the de-facto sabotage-tolerance layer), and must reject exact replication,
  bisection disputes, and zk proofs. Includes living layer + reinforced research.
- **New sources digest `sources/decentralized-verifiable-computation-selected-sources.md`:**
  per-source extraction and citation list for the seven source families above.
- **Counts:** `INDEX.md` (reading list + table) and `tools/verification-contract.json`
  updated — chapters_total 24→25, all_chapters_living_layer 24→25,
  all_chapters_reinforced 24→25, native_chapters += 03d. `source-register.md` and
  `RESEARCH_PIPELINE.md` updated.

Reason:
- The corpus repeatedly named evaluator decentralization as its #1 unsolved frontier
  (Ch03c) and touched its faces in Ch08/11/02/12, but never assembled the external
  computer-science prior art on the general problem. This chapter fills that gap and,
  crucially, keeps the corpus honest by showing which well-known techniques do **not**
  transfer to noisy, hardware-scoped benchmark fitness.

## 2026-06-24 - Tier Reconciliation (4 Cornerstone Claims) + AlphaEvolve Decentralization Chapter (03c)

Changed:
- **Depth-tier reconciliation:** added `papers/TIER-RECONCILIATION.md` listing every
  folder audited against the depth-tier policy. Closed the **4 cornerstone gaps**
  by adding `claims-and-results.md` (grounded in each paper's `deep-extraction.md`,
  mirroring funsearch): `map-elites`, `open-endedness-icml-2024`, `poet`,
  `reward-hacking-skalse-2022`. The **11 important** folders missing a claims
  inventory are flagged-only (decision pending), not fixed.
- **New chapter `03c-alphaevolve-decentralized-evolution-mapping.md`:** maps the
  AlphaEvolve (RSI-001, arXiv:2506.13131, CC BY-NC-ND — paraphrase only) verifier-
  grounded loop onto a decentralized BTC-paid contributor fleet. Splits results
  into externally verifiable (48-mult matmul = ceiling, not expectation) vs
  proprietary Google-infra; includes a mapping table and an equally prominent
  disanalogies section (Sybil Ch11, Goodhart/Skalse, hardware-scoped fitness Ch08,
  mutation safety Ch06, economic attack surface Ch02/12). Thesis: the loop is
  validated at industrial scale; decentralizing the evaluator is the unsolved hard
  part. Inherits the Ch20 "Bittensor 23%" Unvalidated flag (no upgrade).
- **Counts:** `INDEX.md` (reading list + table) and `tools/verification-contract.json`
  updated — chapters_total 23→24, all_chapters_living_layer 23→24,
  all_chapters_reinforced 23→24, native_chapters += 03c.

Reason:
- Last pass documented the depth-tier policy but never enumerated the gaps; this
  closes the cornerstone tier and records the rest. The AlphaEvolve chapter gives
  the corpus an honest, hype-free mapping of the strongest industrial RSI result
  onto CursiveOS's decentralized design — foregrounding what it does *not* prove.

## 2026-06-24 - Paper-Library Audit: Reflexion Intake, os-r1→tune-agent Rename, Depth-Tier Policy

Changed:
- **Reflexion intake completed** (`papers/recursive-self-improvement/reflexion/`): added
  `deep-extraction.md`, `claims-and-results.md`, and `figures-and-tables.md`,
  grounded in the local full text `paper.md` (arXiv:2303.11366, CC BY 4.0). No
  `[needs full-text]` markers — every number traces to a section/table.
- **Folder rename** `os-r1` → `tune-agent` to match the paper's v2 title
  (TuneAgent, arXiv:2508.12551; same paper formerly titled OS-R1, GitHub
  `LHY-24/OS-R1`). Updated all old-*path* references in `papers/README.md`,
  `chapters/03`, `chapters/13`, `chapters/15`, and the folder's own
  `deep-extraction.md`. Display name "OS-R1" left intact in prose where the
  corpus still uses the v1 name.
- **papers/README.md**: documented the **Extraction depth tiers** policy
  (cornerstone/important require `claims-and-results.md`; routine papers get
  `deep-extraction.md` only) and a **two-axis labeling convention** note
  (Extraction Confidence = fidelity to the paper; corpus taxonomy = validation
  for CursiveOS — kept separate).
- **Confidence-label normalization**: `claims-and-results.md` for alphaevolve,
  darwin-godel-machine, and funsearch now use the column header
  "Extraction Confidence" (values unchanged; no conflation with corpus taxonomy).

Reason:
- Content audit: finish an incomplete intake from local full text, fix a
  folder/paper naming mismatch, and make extraction depth + confidence labeling
  an intentional, documented policy rather than an accidental one.
## 2026-06-24 - New Experiment Plan: Cold-Start Model/Runtime Transfer

Changed:
- **Added `experiments/cold-start-model-runtime-transfer-plan.md`** — falsifiable
  plan testing whether the validated cold-start preset gain (−51% on Stardust)
  survives a change of model, quantization, or runtime on the *same* machine.
  Separates absolute idle-exit saving (ms, predicted model-invariant) from the
  reported percentage gain (predicted to dilute as model-load grows). Single
  machine, existing harness + cold-start sensor, ~6-cell config matrix; no new
  infrastructure.
- `RESEARCH_PIPELINE.md` — added the plan to the Experimental Lift table.

Reason:
- The cold-start channel (CV 0.002) drives every acceptance-grade selection
  decision, but every cold-start number on record was measured against one
  inference configuration. The corpus has tested cross-*machine* transfer
  (hardware-scoping plan) but never the orthogonal cross-*model/runtime* axis.
  Outcome decides whether the CursiveRoot fitness key must include
  `(model × quantization × backend)` or whether one preset serves a machine's
  whole model zoo. Grounded in Ch00 §2.3/§5.1 (CPU idle-exit mechanism; page-cache
  load dominance) and Ch10's open OpenVINO/SYCL parity-matrix task.
## 2026-06-24 - Red-Team Flag: Ch20 AlphaEvolve "23% on Bittensor nodes" Overstatement

Changed:
- **VALIDATION.md** — added a "Flagged for Review" row (red-team) for
  `chapters/20-market-and-viability.md` § "LLM-Integrated Heuristic Discovery".
- **validation/notes/2026-06-24-ch20-alphaevolve-23pct-bittensor-overstatement-challenge.md** —
  new adversarial-review note (challenge only; original claim not edited).

Reason:
- Adversarial corpus review. The chapter's claim that LLM-guided evolutionary
  tuning yields "training and inference times for Bittensor nodes by up to 23%"
  is the only quantified evidence for the product's core "AI-Guided Kernel
  Tuning" differentiator, yet it misattributes AlphaEvolve's published result:
  the 23% was a Google-internal Gemini *training*-kernel speedup on TPUs
  (≈1% end-to-end training time), never evaluated on Bittensor or Intel Arc,
  and uncited. It also contradicts the corpus's own open proposer-vs-random
  experiment (CH05-BM-002), which has not shown the LLM proposer beats random
  search at all. Flagged, not edited (preserved-DOCX import; red-team rule).
- External evidence: AlphaEvolve (DeepMind, 2025), arXiv:2506.13131 — 23% Gemini
  training kernel (~1% total training time), 32.5% FlashAttention kernel, 0.7%
  Borg compute recovery, all on Google's own TPU/data-center stack.

## 2026-06-24 - Structural Org: Ch03+Ch04 Merge, Ch07 Split, Inline Body Reinforcement

Changed:
- **Merged Ch03+Ch04** → `chapters/03-rsi-literature-and-organism-synthesis.md` (Part A literature digest + Part B organism framework); deleted `04-foundations-of-software-organisms-rsi-critical-synthesis.md`.
- **Split Ch07** → `07-main-repo-gap-closure.md` (Gaps 1–5) + `07b-research-backlog-and-pipeline.md` (backlog/pipeline); deleted `07-main-repo-gap-closure-and-research-backlog.md`.
- **Inline reinforcement:** `sources/reinforcement-manifest.json` + `tools/apply-reinforcement-manifest.ps1`; Corpus inline blocks inserted in body paragraphs of all 18 original chapter files (below reinforced headers).
- **Verification gates:** `tools/verification-contract.json` `acceptance_gates` (baseline commit, merge/split file checks, per-original inline minimum); `run-verification.ps1` emits `MODIFIED FILES` from `git diff`.
- `INDEX.md`, `sources/corpus-organization-decisions-2026-06-24.md`, `REINFORCEMENT_LOG.md`, `RESEARCH_PIPELINE.md` updated for merge/split.

Reason:
- Skeptic gap closure: execute RSI overlap merge (not document-only), split multi-topic Ch07, auditable in-body reinforcement on every original chapter, honest changed-files evidence.

## 2026-06-24 - Inline DOCX Reinforcement + Verification Harness Fix

Changed:
- **Ch14, Ch19:** `> **Corpus inline (2026-06-24):**` blocks inserted **inside** preserved
  DOCX import paragraphs (sched_ext/SchedCP; TCP §2.1/§2.2 narrowing).
- `tools/verification-contract.json`: inline marker gate for Ch14+Ch19; `input-records.json` output.
- `tools/run-verification.ps1`: SHA256 input records, inline checks, producer path in samples.
- `implementer/run-verification.ps1`: stub delegates to canonical `tools/run-verification.ps1`.

Reason:
- Verification skeptic gaps: script/contract mismatch, missing Ch10 in stale scratch script,
  inline body reinforcements required alongside integration-note headers.

## 2026-06-24 - Verification Contract + Full DOCX Integration Notes

Changed:
- `tools/verification-contract.json` + `tools/run-verification.ps1` — contract-driven
  verification (exits non-zero before writing evidence if counts/markers/samples fail).
- Sample list now includes **two** new chapters (Ch08 + Ch10) per plan step 3.
- `## Corpus integration notes` added to all DOCX-import chapters: Ch16, Ch18–Ch22
  (Ch13–15 already had them); total integration blocks = 9.
- `REINFORCEMENT_LOG.md` — per-chapter audit table (reviewed, gaps, location, sources).

Reason:
- Structural fix per goal strategy: bind verification to explicit contract; make
  DOCX reinforcement auditable without editing preserved import paragraphs.

## 2026-06-24 - Body-Level Corpus Integration (Ch13–15)

Changed:
- **Chapters 13–15:** added `## Corpus integration notes (2026-06-24)` inside chapter
  bodies (between title and DOCX import) with targeted narrowing rules, paper
  intake cross-refs, and harness/VALIDATION constraints — not header-only blocks.
- **Chapter 15:** expanded reinforced block (SchedCP, OS-R1, SemaTune, verifier
  pattern); fixed mojibake in reinforced bullets.

Reason:
- Verification requirement: reinforcements must appear inside pre-existing chapter
  bodies, including mandatory Ch14/Ch15 samples.

## 2026-06-24 - Full Chapter Reinforcement Pass (Living Layers + Topic Sources)

Changed:
- **Chapters 00–07, 17–18:** added `## Corpus status (living layer)` and topic-specific
  `## Reinforced research (2026-06-24)` with credible citations (papers/, OWASP,
  DMTF Redfish, BBR, sequential testing, etc.).
- **Chapters 08–12, 14, 16, 21, 22:** replaced generic 3-bullet reinforced boilerplate
  with topic-specific external sources and corpus cross-links.
- **Chapter 03:** added `## Corpus paper library cross-links` table mapping all 25
  paper intakes to CursiveOS lessons.
- **Chapter 13:** fixed mojibake in reinforced block; added BBR preset cross-ref.

Reason:
- Verification gap closure: every chapter now has living layer + credible reinforced
  additions per acceptance criterion 1; Ch03 integrates paper library per criterion 4.

## 2026-06-24 - Strategic Corpus Reorganization + 5 New Chapters + 25 Papers

Changed:
- **Chapter renumbering (23 chapters, strategic order 00–22):** measurement and
  organism architecture first (00–08), literature and platform depth (09–18),
  historical DOCX imports last (19–22). See `INDEX.md` for the full map.
- **Five new chapters:** 08 Population Confirmation & Fleet Statistics; 09
  Network Transport & Congestion Control; 10 Local LLM Inference Runtime; 11
  Hardware Identity & Anti-Spoofing; 12 Open-Source Funding & Contributor
  Incentives.
- **Paper library:** 18 new peer intakes → **25 total** under `papers/` per
  `CORPUS_WORKFLOW.md` (extraction-only unless rights-cleared).
- All 23 chapters: `## Corpus status (living layer)` + topic-specific
  `## Reinforced research (2026-06-24)` (not generic boilerplate); Ch03 gained
  paper-library cross-link table for 25 intakes.
- `INDEX.md`: full 00–22 table, cohesive reading path, paper count.
- `VALIDATION.md`: chapter numbers aligned (measurement rows → Ch00; daemon →
  Ch05; firmware → Ch17); added Ch08/09/11 rows.
- `README.md`, `CORPUS_WORKFLOW.md`, `papers/README.md`: onboarding and paper
  inventory updated.
- Cross-reference repair across chapters, experiments, sources, validation notes.

Reason:
- Goal pass: review and reinforce the corpus, close high-value gaps with new
  chapters, intake peer papers to target count, and order chapters for
  measurement-first agent onboarding.

## 2026-06-24 - Early Chapter Cohesion + Workflow Upgrades

Changed:
- `CORPUS_WORKFLOW.md`: added **Preserved Import + Living Reconciliation** rule,
  cohesion-pass checklist, and proposed workflow upgrades table (living layers,
  measurement-first reading path, flag→reconcile→delete, experiment graduation).
- Chapters **00–07**: each gained a `## Corpus status (living layer)` section
  cross-linking Ch10–17 and marking superseded import passages (do-not-cite
  externally) without deleting DOCX intake text.
- **Chapter 19**: reconciled §2.1/§2.2 and Research-master network canon with
  Validated Chapter 22 (BBR win, not buffer ceiling; hardware-scoped magnitude).
- **Chapter 20**: reconciled TDX bus-hardening and Covenant-72B overclaims via
  living layer; noted TAO-OS → CursiveOS rename.
- **Chapter 21**: explicit Superseded-by-Chapter-11 banner for product economics.
- `INDEX.md`: added cohesive reading path for new agents; refreshed confidence
  labels for Ch00–07.
- `VALIDATION.md`: cleared three resolved Flagged-for-Review rows; added
  Disproven high-impact rows for Ch01 TCP example and Ch02 TDX/Covenant claims.
- `sources/extracted-source-index.md`: refreshed extraction queue for Ch00–07,
  Ch16, Ch17.

Reason:
- Early imported chapters were cohesive as intake snapshots but diverged from
  measurement-validated truth (Ch16) and red-team evidence. Living layers preserve
  audit history while giving agents a single authoritative guide — no external
  testing required for this reconciliation pass.

## 2026-06-23 - Corpus Cleanup Pass

Changed:
- `RESEARCH_PIPELINE.md` §3 Experimental Lift: added rows for the cold-start
  order/page-cache confound test and the idle-power selection-channel validation
  plan (both were merged without pipeline entries); updated the seed-organism
  screen row to reflect current parent/candidate work (v0.9c, v0.10-zram).
- `VALIDATION.md`: consolidated the duplicate Chapter 19 TCP-buffer flags
  (2026-06-22 broad + 2026-06-23 narrow) into a single row referencing both
  evidence notes.
- `CHANGELOG.md`: restored the orphan Goodhart subsection entry (missing `##`
  header from a prior union merge); backfilled the missing order-cache confound
  entry; fixed section spacing in recent entries.
- `chapters/07-main-repo-gap-closure-and-research-backlog.md`: repo is public,
  not private.
- `chapters/00-benchmark-schema-and-measurement-validity.md` §2.3, §5, §6: linked
  the open fixed-order/page-cache confound to
  `experiments/cold-start-order-cache-confound-plan.md`; softened cold-start
  from "acceptance-grade" to "repeatable but not yet order-robust."
- `VALIDATION.md`: added Chapter 22 cold-start order-robustness row (Supported).

Reason:
- Post-consolidation hygiene pass: close workflow gaps left by the 11-branch
  merge, remove redundant validation rows, and cross-link the highest-leverage
  open measurement question (cold-start order confound) where the corpus already
  names the risk.

## 2026-06-23 - Experiment Proposed: Cold-Start Order / Page-Cache Confound

Changed:
- Added `experiments/cold-start-order-cache-confound-plan.md`: a pre-registered
  test of whether the −51% Arc cold-start win is partly a baseline-first /
  tuned-second run-order or warm-page-cache artifact. Three arms (replicate,
  counterbalanced, cache-controlled); pre-registered decision thresholds.
- Linked from Chapter 22 §2.3 and §5 (cleanup pass).

Reason:
- Cold-start is the only selection-grade channel (CV 0.002), yet every paired
  screen runs baseline then tuned and does not record page-cache state. Repeatable
  under one fixed order ≠ order-robust. This is the cheapest falsifier before any
  further acceptance decision rests on cold-start magnitude.

## 2026-06-20 - Experiment Proposed: Proposer vs Random Search

Added:
- `experiments/proposer-vs-random-tuning-experiment.md`: a single falsifiable,
  properly-powered experiment to test the project's load-bearing untested claim
  (CH05-BM-002) — does the LLM proposer beat blind random search over the same
  allowlist at equal budget? Uses cold-start as the only fitness channel (the
  one solid enough to drive selection per the 2026-06-16 noise floor, CV 0.002),
  seeds the allowlist with a validated-inert decoy knob (the v0.8 GPU pin) to
  catch Goodhart/knob-hoarding, and pre-registers an honest null (C ≈ B is the
  likely, and still decision-changing, outcome).
- RESEARCH_PIPELINE §3 Experimental Lift: new row pointing the AI-guided tuning
  validation at this sharper, runnable instance.

Reason:
- The corpus has empirically grounded its measurement layer (Chapter 22) but has
  never tested whether the *proposer*, not just the knobs, creates value. The
  recent network result (the whole win was one sysctl) and the inert GPU pin
  show exactly the failure mode this would catch. The 2026-06-16 noise floor is
  the missing input that finally makes the test powered and worth running.

## 2026-06-20 - Adversarial Review: Flagged Chapter 20 TDX Bus-Attack Claim

Changed:
- Filed a "Flagged for Review" item in `VALIDATION.md` against Chapter 20's
  claim that "TDX, built for the DDR5 era, is hardened against physical bus-level
  attacks" (and the attestation table's "Bus Attack Resistance: Hardened
  (DDR5)"). Original chapter wording left untouched (it is a preserved DOCX
  import; resolved via flag, not in-place edit).
- Added `validation/notes/2026-06-20-ch02-tdx-bus-attack-resistance-challenge.md`
  with the full challenge and external citations.

Reason:
- This is a decision-driving security claim: the chapter recommends an SGX → TDX
  + NVIDIA CC migration as the answer to the DePIN "oracle problem." External
  evidence contradicts the "hardened" property for the relevant threat model.
  **TEE.Fail** (Oct 2025, Georgia Tech + Purdue) is a practical **DDR5**
  memory-bus interposer that extracts keys and **forges remote attestation
  against Intel SGX/TDX, AMD SEV-SNP, and NVIDIA CC** — defeating *both*
  recommended successors on the exact bus called "hardened." **Battering RAM**
  (2025, ~$50 DDR4 interposer) breaks SGX/SEV-SNP and its authors expect DDR5
  interposers to follow; Intel's TDX mitigation ("integrity mode") is not the
  default posture. Intel and AMD explicitly place physical-access attacks
  **out of threat model** — which is exactly the DePIN model (a node operator
  with physical access to its own DRAM bus). For that model the claim is
  effectively Disproven; the oracle problem must rest on the project's own
  non-TEE defenses (population confirmation, fingerprint cross-checks, anomaly
  detection, economic slashing), not on TEE bus integrity.

## 2026-06-20 - Containment Primitive Characterization for Unattended Execution

Changed:
- Chapter 15: added a "Containment Primitive Characterization" subsection
  (additive, after "Risk-Based Execution Tiers") that turns the previously
  named-only sandboxing primitives into a property-level selector. Characterizes
  namespaces+cgroups, seccomp-BPF, Landlock, bubblewrap, gVisor, and Firecracker
  by the boundary each enforces, what it does NOT contain alone, setup
  privilege, cost, and best CursiveOS role — plus the sharp edges (seccomp
  cannot dereference pointers; Landlock capability is kernel-version-scoped;
  unprivileged user namespaces are themselves attack surface; gVisor trades
  syscall cost/compat for a smaller host-kernel surface; Firecracker is the only
  hardware-enforced guest boundary here). Ends with a layered selector and the
  reminder that containment protects the host but does NOT grant the shell write
  access to organism truth.
- `sources/local-agent-safety-selected-sources.md`: added a dated "Containment
  Primitive Deep-Dive Sources" table with the retrieved facts and URLs (kernel
  seccomp/Landlock docs, Phoronix, bubblewrap, gVisor platform/systrap, and
  Firecracker spec).
- VALIDATION.md: added a Chapter 15 claims-table row stating that containment
  primitive choice should follow input-trust/blast-radius and that no single
  primitive is a complete sandbox.

Reason:
- Directly answers Chapter 15 Open Research Gap #4 ("build risk-based
  containment for unattended tool execution") and RESEARCH_PIPELINE P1
  "Sandboxing and least privilege" / P0 knowledge gap "How do current agent
  systems fail under privilege?". The prior chapter text only listed these
  primitives; the corpus lacked a property-level basis for choosing among them
  before enabling unattended host mutation.

## 2026-06-21 - Cold-Start Mechanism + Hardware-Scoping Experiment Proposed

Changed:
- Added `experiments/cold-start-mechanism-and-hardware-scoping-plan.md`: a
  falsifiable experiment plan targeting the corpus's most-trusted signal
  (cold-start, within-machine CV 0.002). Two hypotheses: (H1) the −51% desktop
  win is carried by a single CPU idle-exit knob, tested by a 2³ factorial over
  governor / EPP / C-state limit on the Ryzen 7 5700 + Arc A750 desktop; (H2) a
  cheap preset-free idle-exit pre-probe (cold TTFT − warm TTFT) predicts which
  machines benefit, tested across all available tester machines.
- Added the plan to RESEARCH_PIPELINE.md Experimental Lift; marked the real-path
  network A/B row Done (it had been completed on 2026-06-16 but the pipeline row
  still read "Proposed").

Reason:
- Cold-start currently drives selection (`chapters/16` §5.7), yet its mechanism
  is only half-isolated (CPU-side, but no single knob — §5.1) and its hardware
  scoping is unexplained (−51% desktop vs ~0% laptop — §5.5). The standing
  VALIDATION instruction is "build hardware-scoped fitness before any fleet-wide
  preset claim"; this experiment is the cheapest path to both the causal knob
  and a predictor, reusing the factorial-decomposition discipline that already
  paid off on the network thread (§5.6).

## 2026-06-21 - Red-Team Flag: Covenant-72B "GPT-4-class" Claim Overstated (Chapter 20)

Changed:
- Flagged (did **not** edit) the Chapter 20 claim that Covenant-72B's 67.1 MMLU
  is "competitive with early GPT-4-class models" and demonstrates that
  "decentralized compute can achieve data-center-level results." Added a row to
  the `VALIDATION.md` "Flagged for Review" table and a full evidence note at
  `validation/notes/2026-06-21-ch02-covenant-72b-gpt4-class-overstatement-challenge.md`.
- External evidence: GPT-4 (2023) scored 86.4% on MMLU (OpenAI GPT-4 Technical
  Report); GPT-3.5 ~70-75%; Llama-2-70B ~68.9% (Llama 2 paper). Covenant-72B's
  67.1 sits ~19 points below GPT-4, at the Llama-2-70B / GPT-3.5 tier — which is
  also the model's *own* reported peer set (LLaMA-2-70B 65.6, LLM360 K2 65.5,
  both 2023-era open base models). The "GPT-4-class / data-center-level" framing
  is therefore overstated.

Reason:
- Adversarial corpus review. The Covenant-72B benchmark is the chapter's only
  concrete model-quality figure and is load-bearing for its market-viability
  thesis, so overstating its comparison class overstates the opportunity. The
  underlying decentralized-training achievement (72B model, 1.1T tokens, ~70
  commodity-hardware contributors) is real and not in dispute; only the GPT-4
  comparison is challenged. Per the red-team task and CORPUS_WORKFLOW.md, the
  preserved-DOCX claim was not edited in place — only flagged with external
  evidence. (For contrast, the chapter's "BBR ... 2700x faster than CUBIC"
  figure was checked and found to be Google's own published benchmark, so it was
  not flagged.)

## 2026-06-22 - Experiment Plan: Idle-Power Selection-Channel Validation

Changed:
- Added `experiments/idle-power-selection-channel-validation-plan.md`. A
  pre-registered, falsifiable plan to test whether the 2026-06-16 harness
  idle-power fix (settle delay + more samples) actually makes idle power a
  selection-usable channel (CV ≤ 0.15 per Chapter 01) in the **production
  full-test path** and across hardware — not just in the one-off Phase-D probe
  on the Arc A750 desktop where it was demonstrated.

Reason:
- Chapter 22 §5 items 7–8 left a tension on the record: idle power was CV ≈ 0.83
  in the production noise floor but CV ≈ 0.01 in a bespoke probe. Chapter 01's
  confirmation rule and the live v0.9 screen's power term both depend on which
  is true in the path operators actually run, on more than one machine. The plan
  also ships the §3 item-1 `power_source` field as a side effect and keeps the
  §2.2 cross-machine pooling bar explicit (H3).

## 2026-06-22 - Red-Team Flag: Ch01 Static-Buffer "Universal Gap" Thesis Overstated

Changed:
- Flagged `chapters/19-first-principles-and-strategy.md` §2.1/§2.2 in
  `VALIDATION.md` (Flagged for Review) as an overstated, load-bearing claim,
  **without editing the chapter text**. The chapter frames a static 212KB TCP
  buffer default ("appropriate for 1990s modem speeds") as the universal
  OS-level bottleneck and "foundational opportunity," and its in-chapter
  assessment marks the wording canon for verbatim white-paper reuse while
  citing +454–616% network deltas as the proof point.
- Added `validation/notes/2026-06-22-ch01-buffer-default-overstatement-challenge.md`
  with the full external-evidence challenge and suggested reconciliation.

Challenge (external + internal evidence):
- Linux receive-buffer autotuning (Dynamic Right-Sizing) has been on by default
  since kernel 2.4.17/2.6.7 (~2004): the operative `tcp_rmem` default is ~87KB
  and grows automatically toward the path BDP. The 212992 figure is the
  `net.core.rmem_max` ceiling, not an applied per-connection default — so
  "defaults to 212KB" misdescribes the stack. The "1990s modem" parenthetical
  is also inverted (a 208KB buffer is ~30s of data for a 56kbps modem).
- The large, real network win is the buffer-independent CUBIC→BBR
  congestion-control swap (BBR literature: the advantage holds across bandwidths
  and is "due to the fundamental algorithm design rather than buffer-specific
  behavior"; it is a one-line sysctl any operator can set).
- The corpus's own **Validated** Chapter 22 real-path A/B already found the
  CursiveOS buffer/qdisc stack adds ~0% (−0.7%) on ordinary ≤1GbE links, with
  the loopback "+246%" called a non-transferable artifact. That validated
  correction was never reconciled with the still-canon Chapter 19 thesis.

Reason:
- §2.1/§2.2 is an irreducible first principle that the moat/flywheel thesis
  (Chapters 19, 02, 11) and the project's headline performance numbers rest on,
  and it is slated for verbatim white-paper reuse. If the real lever is a
  portable one-line BBR swap and autotuning already covers ordinary links, the
  "universal, structurally inherent" gap — and the defensibility argument built
  on it — is materially smaller than the foundational chapter asserts. Flagged
  rather than edited per CORPUS_WORKFLOW.md §3 because the wording is canon
  headed into an outward-facing document and the reconciliation is a maintainer
  decision.

## 2026-06-22 - New Chapter 06: Mutation Safety and Permission Law

Changed:
- Added `chapters/06-mutation-safety-and-permission-law.md`, the source-backed
  "permission law" the corpus had flagged as the #1 missing expansion
  (Chapter 07 Gap 2 / "What Should Be Added Next"). It binds the existing
  seven-class mutation taxonomy to the *specific* enforcement primitive that
  makes each gate real (capabilities, seccomp, Landlock, systemd sandboxing,
  polkit-mediated escalation, firmware staging) and states the core rule:
  required privilege rises with blast radius and the authorizer shifts from the
  deterministic daemon (low classes) to a human (high classes); the
  probabilistic shell never applies a mutation directly.
- Grounded the chapter in external literature: Saltzer & Schroeder (least
  privilege, fail-safe defaults, separation of privilege) and OWASP LLM Top 10
  2025 LLM06 (Excessive Agency → separate decision from execution), plus
  kernel.org / man-page / freedesktop primary docs for the containment
  mechanisms. Added `sources/chapter-17-selected-sources.md` (7 sources).
- Updated `INDEX.md` (Chapter 06 row), and marked the gap addressed in
  `RESEARCH_PIPELINE.md` (P0 knowledge gap "How do current agent systems fail
  under privilege?") and Chapter 07 Gap 2.

Reason:
- Chapter 22 hardens the host against external attackers; nothing consolidated
  the inverted threat — the organism's own self-improvement loop mutating the
  host under a probabilistic agent. This closes the highest-value, well-sourced
  research gap and moves the corpus from "we have the pieces" to a single
  enforceable rulebook for self-mutation.

## 2026-06-22 - Chapter 03: Autopoiesis / Artificial-Life Grounding of the Organism Framing

Changed:
- Chapter 03: added section "Biological and Artificial-Life Foundations of the
  Organism Framing" (additive, inserted after "What Remains Speculative"). It
  grounds the corpus's "organism" language in autopoiesis (Maturana & Varela,
  1972/1980), cybernetics (Beer's Viable System Model 1972; Ashby's Law of
  Requisite Variety), and artificial life (Langton's "life as it could be";
  Tierra, Ray 1990; Avida, with Lenski/Ofria/Pennock/Adami, Nature 423:139–144,
  2003 on incremental evolution of complex features). It then covers the
  open-ended-evolution literature — novelty search (Lehman & Stanley 2011),
  Quality-Diversity / MAP-Elites (Mouret & Clune, arXiv:1504.04909, 2015), and
  POET (Wang et al., arXiv:1901.01753, 2019) — and adds a table separating
  metaphor / structural analogy / measurable property / implementation
  consequence for each biological term.

Reason:
- Closes the explicit "artificial life and open-ended evolution" follow-up
  flagged at the end of Chapters 03 and 15, and addresses RESEARCH_PIPELINE.md
  P0 item "Software Organisms, Autopoiesis, and Evolutionary Systems" and the P0
  knowledge gap "What makes a software system an organism rather than an
  automation pipeline?" Key takeaways for CursiveOS: today the system is closer
  to allopoietic (automation reaching toward organism properties), not
  autopoietic; the "genome" should be a diverse, stepping-stone-structured
  archive (MAP-Elites-style) rather than a champion changelog; fitness must
  reward stepping stones (Avida/EQU) or capabilities will not evolve; sensor/
  verifier variety must match mutation variety (Ashby); and indefinite
  open-ended improvement is unproven even in purpose-built ALife systems, so
  plateaus should be expected and designed for. Sources cited are those actually
  retrieved via web search (2026-06-22); no full-text paper mirroring.

## 2026-06-23 - Red-Team Flag: Chapter 19 §2.1 TCP-buffer claim challenged

Changed:
- VALIDATION.md "Flagged for Review": added a flag against
  `chapters/19-first-principles-and-strategy.md` §2.1, the First Principle #1
  flagship example "TCP socket buffers default to 212KB (appropriate for 1990s
  modem speeds)." The original claim was **not** edited.
- Added `validation/notes/2026-06-23-ch01-2.1-tcp-buffer-claim-redteam-challenge.md`
  with the full challenge and external citations.

Reason:
- The claim is wrong on both halves. 212 KB is `net.core.rmem_max` (the ceiling
  on *manually* set `SO_RCVBUF`), not the default; ordinary sockets use
  `tcp_rmem` autotuning up to ~4–6 MB, on by default since the 2.6.x series
  (~2004). And a 212 KB window supports ~17 Mbit/s at 100 ms RTT and ~1.7 Gbit/s
  on a LAN — hundreds to tens-of-thousands of times a 56 kbit/s modem, not
  "modem speeds." Sources: Linux `tcp(7)` man page, Red Hat RHEL 10 TCP-tuning
  guide, ESnet Fasterdata.
- This matters because §2.1 is the corpus's most load-bearing technical sentence:
  it is named "the foundational opportunity CursiveOS exploits" and the chapter's
  Research-master note canonizes it as "rock-solid"/"now canon"/"quoted verbatim."
  The corpus's own Validated Chapter 22 network A/B (2026-06-16) already
  contradicts it — "default-buffer autotuning already covers the ~6 MB BDP,"
  buffer tuning adds ~0%, and the real network win is CUBIC→BBR.
- Scope is narrow: First Principle #1 stays Supported in general (governor/GPU
  examples are sounder); only the TCP-buffer example is challenged.

## 2026-06-16 - Noise Floor Measured + GPU Power Now Visible

Changed:
- Chapter 22 §5 item 7 + VALIDATION: first per-channel within-machine noise
  floor (6 identical v0.9 runs on Stardust). Cold-start CV 0.002 (rock-solid),
  network CV 0.192 (above 0.15 escalation threshold; range 602–970%), sustained
  sign-unstable (signal<noise), idle-power(CPU) CV 0.83 (near-random). Argues
  for per-channel confirmation counts and against gating on sustained-single-
  stream or idle power as currently measured.
- GPU-side power sensor (wrapper v1.4.3) confirmed working on the Arc A750
  (~37 W idle via hwmon energy counter); total power (CPU+GPU ≈ 55 W) now
  measurable — the §2.2 blindspot is closed on this hardware.

Reason:
- Closes the 2026-06-16 hardware sprint. The noise floor is the empirical input
  Chapter 01's population-confirmation model lacked; it also explains why power
  and sustained deltas have swung wildly across past runs. Cold-start is the one
  channel solid enough to drive selection today.

## 2026-06-16 - Real-Path A/B Overturns the Stack-Delta Magnitude

Changed:
- Chapter 22 §5 item 6 + VALIDATION: the real-path network A/B finally ran
  (Stardust → 2nd machine over real 1GbE, netem 50ms + 0.5% loss). Result:
  CUBIC 43.1, BBR 851.1, BBR+our-stack 845.0 Mbit/s. The whole real-world win
  is the CUBIC→BBR swap (+1875%); our buffer/qdisc stack adds ~0% (−0.7%).
- This corrects the 2026-06-13 loopback decomposition ("+246% from our tuning"):
  that is a loopback BDP artifact and does not transfer to ordinary ≤1GbE
  links, where default-buffer autotuning already covers the ~6 MB BDP. The
  loopback stack-delta benchmark is mechanism-only, not a user magnitude.
- Network VALIDATION claim moved Supported → Validated with the narrower,
  honest scope (the win is BBR; buffers untested-and-likely-irrelevant below
  >1Gbit/high-latency WAN).

Reason:
- The real-path experiment did its job: it falsified the magnitude transfer of
  the project's own buffer tuning. Better to know the headline is "BBR" than to
  credit ourselves with a loopback artifact. Part of the 2026-06-16 hardware
  sprint (also: v0.9 parent promotion, GPU power sensor, parsimony fitness).

## 2026-06-16 - Corpus Guardrail Hooks + Chapter 03 Restore + Gödel Extraction

Changed:
- **Restored Chapter 03**, which an automated contributor (Grok) had wiped to
  a one-line placeholder (`# [full new content would go here but for brevity]`)
  in commit 3b71797 while claiming to "deepen" it. Restored to the last-good
  state (8b427e7, 352 lines), preserving Grok's two genuinely useful additions
  (Goodhart/proxy-optimization subsection, Karpathy autoresearch case study).
- **Added `.githooks/` corpus guardrails** (enable with
  `git config core.hooksPath .githooks`): `pre-commit` blocks lazy-elision
  placeholder text; `commit-msg` blocks any tracked markdown losing >40% of its
  lines without a `REWRITE:` prefix (the rule that would have caught the
  Chapter 03 wipe). Both tested: placeholder and shrink correctly blocked,
  `REWRITE:` override correctly allowed.
- **Completed the Gödel Agent paper entry** with `deep-extraction.md`
  (previously only a README stub). Grounded in the arXiv abstract; specifics
  that need the full-text body are flagged, not guessed.

Reason:
- Audit of Grok's automated corpus additions found the content useful but the
  process unguarded — a single rewrite destroyed a chapter with no validation.
  The hooks let automated contribution continue safely; the daily encrypted
  backup remains the last-resort net.

## 2026-06-16 - Chapter 03 Goodhart's Law Deep-Dive (Grok)

Changed:
- Added a substantial new subsection to Chapter 03 (`chapters/04-foundations-of-software-organisms-rsi-critical-synthesis.md`) on Goodhart's Law, reward hacking mechanisms, benchmark overfitting, and robust fitness design patterns specifically for software organisms and CursiveOS measurement/selection loops.
- Synthesized from recent literature (including reward hacking taxonomy in large models, ICLR 2024 Goodhart in RL empirical work, agent exploit examples in coding/tool-use benchmarks, and existing corpus coverage in Chapters 03 and 16).
- The section provides taxonomy of how Goodhart manifests in recursive self-improvement loops, concrete CursiveOS-relevant examples (network sim vs real-path, hardware-scoped cold-start, power measurement artifacts, benchmark gaming), and actionable mitigation patterns (multi-objective fitness bundles, independent confirmation, holdouts, negative memory, canary/rollback, sandbox structured feedback, rotating tests, cost/reliability gates).
- Directly addresses P0 pipeline item on Goodhart and measurement under software organisms research targets, and supports current Phase 0 benchmark validity and candidate screening work.
- Updated `VALIDATION.md` with related decision-driving claims on fitness design and confirmation rules (if applicable after review).
- No new full paper folders created (synthesis from multiple sources; rights-cleared papers already in corpus used as reference where relevant). 

Reason:
- The existing brief mention of Goodharting in Chapter 03 failure modes was high-level. A deeper, CursiveOS-mapped treatment with taxonomy, recent empirical examples, and concrete design recommendations provides immediate value for the organism's sensor array, fitness function, metabolic sensor, and confirmation logic. This is one of the most actionable research gaps for the current empirical validation phase and future Layer 5 implementation.
- Follows CORPUS_WORKFLOW.md fast path for important claim synthesis and chapter editing (living document). No single paper full-text intake required.

## 2026-06-13 - Cold-Start Optimization Is Hardware-Scoped (Second Machine)

Changed:
- Chapter 22 §5 item 5 + VALIDATION: second-machine run (i5-11300H laptop)
  shows the cold-start optimization gives ~0% there vs −51% on the Arc A750
  desktop. Phase-context telemetry confirms the governor changed to
  performance on AC power, so it is a genuine hardware difference, not a
  failed apply. First empirical instance of hardware-scoped fitness
  (Chapter 01). v0.9c ≡ v0.8 on both machines, so it remains a safe global
  parent replacement; the cold-start benefit is desktop-Arc-specific.

Reason:
- The second-machine confirmation for v0.9c surfaced a larger finding: the
headline cold-start gain does not transfer across hardware classes. The
telemetry added the day before is what made the result trustworthy rather
than ambiguous.

## 2026-06-13 - Stack-Delta Result Corrects Network Attribution

Changed:
- Chapter 22 §5 item 4 + VALIDATION: the stack-delta benchmark (BBR held
  constant, only CursiveOS buffer/qdisc tuning toggled) measured +245.8% on
  the founder rig (BBR-only 395.5 → BBR+our-stack 1367.5 Mbit/s, netem
  verified). Decomposing the ~+800% legacy total: CUBIC→BBR ≈ 2.6×, our
  buffer tuning ≈ 3.5×. This corrects the earlier "mostly just BBR"
  assumption — on a high-BDP path the project's own tuning is the larger
  factor. Loopback caveat retained; real-path A/B still pending.

Reason:
- The user asked whether the network gains are real or manufactured textbook
results. Splitting the metric (algorithm swap vs our stack) and holding BBR
constant gave an honest, decomposable answer that happens to be more
favorable to the project than the conservative prior assumption — while
keeping the loopback magnitude caveat explicit.

## 2026-06-12 - Chapter 22 Empirical Follow-Ups

Changed:
- Added §5 to Chapter 22 recording the v0.9b/v0.9c complementary ablation on
  the rebuilt founder rig: the Arc cold-start win (−51%) is CPU-side; the GPU
  frequency pin contributes nothing (verified active via phase telemetry) and
  leaves the lineage. v0.9c is the first real acceptance candidate.
- Recorded production confirmation of the §2.2 power-source warning (RAPL
  package-only meter read +0.0W while a discrete GPU idled pinned at 2000MHz).
- Recorded the metric split shipped in the main repo: "transport resilience"
  (CUBIC-vs-BBR, algorithm selection) vs "stack delta" (BBR constant, only
  CursiveOS tuning toggled), with netem verification.

Reason:
- The chapter's program was executed within 24 hours of being written; the
results both validated the methodology critique and produced the project's
first clean attribution. Single-screen results still require reversed-order
and second-machine confirmation before acceptance.

## 2026-06-11 - Benchmark Schema and Measurement Validity Assessment

Changed:
- Added Chapter 22 (`chapters/00-benchmark-schema-and-measurement-validity.md`):
  a first assessment of the deployed benchmark suite and CursiveRoot schema,
  grounded in the actual harness code (wrapper v1.4.1), the live schema, and
  77 production run rows.
- Key findings: the network headline delta is substantially a CUBIC-vs-BBR
  congestion-control comparison under loopback netem (real within the
  emulation, unproven for real paths); idle-power readings mix physically
  different sources (RAPL package vs GPU hwmon vs turbostat) without
  recording which, so cross-machine power comparison is not yet valid;
  per-pass variance reaches CursiveRoot only via the seed path; several
  cheap context fields (power source, temps, AC/battery, model identity,
  netem verification) would convert mystery variance into attributable
  variance.
- Updated `VALIDATION.md` with two decision-driving claims (network scope,
  idle-power comparability) and `RESEARCH_PIPELINE.md` experimental lift
  items (real-path network A/B, power-source normalization, every-run
  detail bundles).
- Updated `INDEX.md` reading path.

Reason:
- The organism's truth model is only as strong as its measurement layer, and
the corpus had no chapter assessing what the deployed suite actually proves.
The assessment was performed alongside live work on the main repo (machine
identity v2, screen-verdict analyzer) so the findings reference the current
implementation, not an idealized one.

## 2026-05-31 - Ingested Rights-Cleared Agent Evaluation Papers

Changed:
- Added full rights-cleared paper folders for SWE-bench, SWE-agent, and OSWorld.
- Stored each paper's arXiv PDF and a full text extraction in `paper.md` because
  all three arXiv pages carry CC BY 4.0 license links.
- Added `README.md`, `deep-extraction.md`, and `claims-and-results.md` for each
  paper.
- Updated Chapter 15 so the natural-language shell research incorporates
  lessons from execution-based software benchmarks, agent-computer interfaces,
  and VM-backed real-computer agent evaluation.
- Updated `papers/README.md`, `VALIDATION.md`, and `sources/source-register.md`
  so the new paper areas and rights-cleared intake are discoverable.

Reason:
- The corpus should preserve fewer, more useful papers deeply when rights allow
full copying. These papers are directly relevant to CursiveOS because the
natural-language shell should be evaluated as controlled computer operation,
not as chat quality.

## 2026-05-31 - Added Local Agent Safety Research Pass

Changed:
- Added `sources/local-agent-safety-selected-sources.md` as a detailed
  selected-source digest for prompt injection, agentic skills, tool authority,
  memory boundaries, sandboxing, and operator confirmation.
- Expanded Chapter 15 with an external safety research section covering
  prompt-injection boundaries, tool/skill authority, risk-based execution tiers,
  shell memory risk, and concrete confirmation UX.
- Updated `INDEX.md`, `RESEARCH_PIPELINE.md`, `VALIDATION.md`, and
  `sources/source-register.md` to reflect the new research pass.

Reason:
- The natural-language shell is a major planned CursiveOS interface, and the
existing daemon/shell split needed external grounding. Current agent-safety
research supports the project's instinct: the shell can translate intent, but
deterministic policy, sandboxing, and the measurement daemon must hold the real
authority.

## 2026-05-30 - Added Firmware Control-Surface Research Pass

Changed:
- Added `sources/firmware-control-surfaces-selected-sources.md` as a selected
  primary-source digest for firmware/BIOS control interfaces.
- Expanded Chapter 06 with a practical control-surface matrix covering UEFI
  variables, Linux firmware attributes, Redfish BIOS attributes, Redfish
  attribute registries, fwupd capsule updates, raw flash, and KVM/BIOS UI
  automation.
- Updated `VALIDATION.md` so the firmware-interface claim reflects the new
  source-backed review.
- Updated `RESEARCH_PIPELINE.md` to mark the abstract firmware-control gap as
  partially filled and steer the next pass toward platform-specific evidence.

Reason:
- The corpus needed a useful open-ended research addition that did not add fake
test material or compress source detail away. Firmware control is a P0 research
gap with immediate value for deciding how a whole-machine optimization organism
can safely observe and stage deeper mutations.

## 2026-05-30 - Reduced Infrastructure Docs

Changed:
- Removed the redundant `methodology/` docs after merging their surviving rules
  into `CORPUS_WORKFLOW.md` and `papers/README.md`.
- Removed the retired `validation/README.md` and `validation/validation-ledger.md`
  active-workflow wrappers.
- Updated README and validation links so the active process is rooted in
  `CORPUS_WORKFLOW.md`.
- Left research chapters, source lists, papers, experiments, validation notes,
  and original source files untouched.

Reason:
- The corpus should have as few process files as possible. The active
infrastructure is now the root workflow, reading index, research pipeline,
validation status, changelog, and the paper-library README.

## 2026-05-30 - Streamlined Corpus Workflow and Added Rights-Cleared Paper Library Rule

Changed:
- Added `CORPUS_WORKFLOW.md` as the primary front-door workflow for uploads,
  papers, corrections, experiments, and minimum recordkeeping.
- Added `papers/README.md` to define the peer-research paper library structure.
- Updated `README.md`, `INDEX.md`, and methodology files so contributors start
  from the simplified workflow instead of juggling overlapping process docs.
- Clarified that full verbatim paper text belongs in `papers/` only when the
  paper is rights-cleared by license, permission, public-domain status, or team
  ownership.
- Preserved the deeper document-intake and paper-extraction policies as
  supporting detail rather than deleting their guidance.

Reason:
- The corpus should favor fewer, deeper, more usable research records over broad
shallow intake. Rights-cleared papers can be stored fully so future agents do
not lose source detail. Non-rights-cleared papers should still receive deep
paraphrased extraction rather than being compressed into useless summaries.

## 2026-05-27 - Added Paper Extraction Policy

Changed:
- Added `methodology/paper-extraction-policy.md`.
- Defined a deeper extraction standard for important papers so the corpus captures methods, mechanisms, experiments, results, limitations, and implications rather than only links and short summaries.
- Added a reusable extraction template for cornerstone, important, supporting, and lead-only papers.

Reason:
- The corpus should optimize for useful research memory, not small file size. Important papers should be deeply paraphrased and structured so future agents can understand what was done, what was measured, what improved, who judged improvement, what failed, and what the corpus should learn without mirroring copyrighted papers verbatim.

## 2026-05-27 - Properly Incorporated Software Organisms RSI Research Packet

Changed:
- Added `chapters/04-foundations-of-software-organisms-rsi-critical-synthesis.md`.
- Added Chapter 03 to `INDEX.md`.
- Promoted more of the uploaded `Software Organisms_ Self-Improvement Research.md` into the corpus as a dedicated critical-synthesis chapter rather than leaving it only as an intake note plus Chapter 03 expansion.
- Preserved the uploaded document's stronger software-organism framing: what is demonstrated, what remains speculative, what is overhyped, layered taxonomy of self-improvement loops, verifier/fitness framing, sandboxing-as-feedback, runtime self-modification risks, maturity-aware gating, multi-objective fitness, and adopt/avoid/caution guidance.

Reason:
- The corpus intake policy now favors substantial incorporation of useful non-overlapping research. The first intake pass compressed the document too aggressively. Chapter 03 keeps Chapter 03 as the paper/system digest while preserving the uploaded document's broader conceptual and organism-specific synthesis.

## 2026-05-27 - Added Document Intake Policy

Changed:
- Added `methodology/document-intake-policy.md`.
- Made the default document-intake posture explicit: substantially incorporate useful non-overlapping research rather than reducing rich documents to tiny summaries.
- Clarified when to merge, omit, or compress uploaded research material.

Reason:
- Future agents need a clear standing rule: when the user provides a research document, most useful material should make it into the corpus unless it overlaps existing coverage, is low-confidence, is outside scope, belongs in the implementation repo, or is better represented as a summary.

## 2026-05-27 - Ingested Software Organisms Self-Improvement Research Packet

Changed:
- Added `sources/intake/software-organisms-self-improvement-research-intake.md`.
- Expanded `chapters/03-peer-reviewed-research-recursive-self-improvement-and-agentic-evolution.md` using the uploaded `Software Organisms_ Self-Improvement Research.md` document.
- Expanded `sources/peer-reviewed-rsi-selected-sources.md` with additional systems and papers from the intake packet, including Gödel Agent, Polaris, Programmatic Skill Networks, Darwin Gödel Machine, CodeEvolve, Process-Based Self-Rewarding, Noise-to-Meaning RSI, TerraLingua, and open-ended AI safety research.
- Strengthened Chapter 03's taxonomy, verifier/fitness discussion, sandboxing section, failure-mode table, and software-organism lessons.

Reason:
- The uploaded document provided a richer research synthesis than the initial Chapter 03 seed. The corpus now captures the document's strongest findings as compressed research memory while avoiding verbatim mirroring of the full uploaded text.

Caveat:
- Some numeric claims and newer/preprint sources in the uploaded packet still require source-level validation before they become decision-driving claims.

## 2026-05-27 - Added Peer-Reviewed Research Digest for Recursive Self-Improvement

Changed:
- Added `chapters/03-peer-reviewed-research-recursive-self-improvement-and-agentic-evolution.md`.
- Added `sources/peer-reviewed-rsi-selected-sources.md` with the initial paper/source set.
- Added Chapter 03 to `INDEX.md`.
- Framed the new chapter as a structured digest of published research rather than an implementation spec or verbatim paper archive.

Reason:
- The corpus needs compressed research memory from high-value papers and systems so future agents can learn core findings without rereading entire papers verbatim. The first intake focuses on evaluator-grounded discovery, recursive scaffold improvement, agent memory, self-evaluation risks, and agent benchmark discipline.

## 2026-05-27 - Added Research Pipeline and Reasserted Research/Spec Boundary

Changed:
- Added root `RESEARCH_PIPELINE.md` as the agent-facing queue for future corpus work.
- Trifurcated the pipeline into `New Research`, `Knowledge Gaps`, and `Experimental Lift`.
- Populated `New Research` with foundational literature targets including recursive self-improvement, agent-operable firmware/BIOS control surfaces, software-organism theory, local-agent safety, hardware optimization foundations, Arc B70/Intel AI stack research, and Bitcoin-native contributor economics.
- Populated `Knowledge Gaps` with conceptual questions that need synthesis before implementation decisions.
- Populated `Experimental Lift` with proposed experiments from existing chapters and validation plans.
- Updated `README.md` to make clear that this repository is a research corpus, while concrete organism specs and implementation artifacts belong in the main `CursiveOS` repo.
- Updated `methodology/maintaining-the-corpus.md` so future agents start from `RESEARCH_PIPELINE.md` and maintain the research/spec boundary.

Reason:
- The previous gap list leaned too far toward implementation specs. The corpus should stay focused on foundational knowledge: papers, literature, hardware/OS research, agent safety, software-organism theory, and external systems. Experiments still matter, but they belong in the experimental lift lane or the main implementation repo when they become executable work.

## 2026-05-27 - Added Main Repo Gap Closure Synthesis

Changed:
- Added `chapters/07-main-repo-gap-closure-and-research-backlog.md`.
- Mapped earlier research gaps against the current main `CursiveOS` architecture.
- Clarified which gaps are already answered by the seed organism, sensor array,
  Layer 5 economics, and agent architecture.
- Reframed the highest-value next research targets as implementation-level specs:
  mutation safety law, CursiveRoot schema, shell implementation, signed preset
  update channel, and fork obligation/Bitcoin ledger research.
- Updated `INDEX.md` so Chapter 07 is part of the reading path.

Reason:
- The corpus had just absorbed major main-repo architecture in Chapters 01-12, but
needed a synthesis layer explaining what that architecture closes and what still
needs research. The project has moved from basic discovery questions toward
implementation specification questions.

## 2026-05-27 - Integrated Missing Architecture from Main CursiveOS Repo

Changed:
- Added `chapters/01-seed-organism-and-sensor-array.md` from the current main
  `CursiveOS` repo architecture.
- Added `chapters/02-bitcoin-native-economics-and-proof-of-useful-optimization.md`
  from Layer 5 Economics v3.3.
- Added `chapters/05-measurement-daemon-and-natural-language-shell.md` from the
  main repo agent architecture.
- Updated `INDEX.md` so the new chapters are first-class corpus entries.
- Marked Chapter 21's tokenomics research as comparison material superseded for
  CursiveOS's own design by the Bitcoin-native v3.3 architecture in Chapter 02.

Reason:
- The research corpus had validation and external research, but it had not fully
absorbed the live architecture already specified in the main `CursiveOS` repo.
That left important research gaps around the seed organism, evidence model,
sensor array, proof of useful optimization, economic metabolism, measurement
daemon, and natural-language shell trust boundary.

Evidence and confidence:

| Finding | Status | Evidence |
| --- | --- | --- |
| The seed organism is a Phase 0 loop built from reversible presets, paired measurement, CursiveRoot submission, sensor evaluation, and candidate selection. | Supported as current project architecture | Main `CursiveOS` `README.md`, `white-paper.md`, `docs/architecture/sensor-array.md`, and `ROADMAP.md`. |
| The current CursiveOS economics design is Bitcoin-native and does not use a custom token, pool, voting, or governance. | Supported as current project architecture | Main `CursiveOS` `docs/specs/layer5-economics-v3.3.md` and `white-paper.md`. |
| The measurement daemon and natural-language shell must remain separate trust domains. | Supported as current project architecture | Main `CursiveOS` `docs/architecture/agent-architecture.md`. |
| The natural-language shell is planned, not implemented. | Supported | Main `CursiveOS` `docs/architecture/agent-architecture.md` and `ROADMAP.md`. |

## 2026-05-26 - Simplified the Corpus Workflow

Changed:
- Made chapters living research documents that may be edited directly as the
  project learns more.
- Made this changelog the required record for material research edits.
- Added `VALIDATION.md` as the compact status page for important claims.
- Replaced the required source-index/ledger/note pipeline with optional deep
  evidence records only when useful.
- Retired `validation/validation-ledger.md` as an active workflow document; it
  now points readers to the compact status page and retained supporting notes.
- Retained original uploaded documents as immutable intake snapshots.

Reason:
- The previous method made a straightforward operational correction difficult to
follow. The project needs clear current guidance, a detailed edit history, and
a visible distinction between confirmed and uncertain claims, without mandatory
paperwork for every correction.

## 2026-05-26 - Chapter 18 Hermes Context and Tooling Guidance

Changed:
- Recorded that the current local Hermes deployment cannot use an approximately
  8k configured context window: its inspected implementation enforces a 64,000
  token minimum and the active configuration uses 65,536.
- Updated the Arc B70 benchmark plan so current Hermes testing keeps its required
  context window and instead varies active prompt, tool-schema, and history
  payload size.
- Documented the local risk that unattended execution currently reaches the
  host through a local terminal backend; the observed mutating repo-hygiene cron
  task was paused.

Evidence and confidence:

| Finding | Status | Evidence |
| --- | --- | --- |
| Current Hermes build requires at least 64,000 configured tokens and is configured for 65,536. | Validated for the inspected local deployment | Local Hermes source and `~/.hermes/config.yaml` inspection on 2026-05-26. |
| Reducing active tool/schema payload may improve responsiveness. | Supported, not validated | Initial tool-envelope diagnostic observations; uncontrolled cache state and no repeated benchmark. |
| Basic structured tool calls can be returned through the current OVMS/parser path. | Supported, not broadly validated | Initial local calls for `read_file`, `skills_list`, and `session_search`. |
| Current unattended execution is sufficiently contained for host mutation. | Disproven for the inspected setup | Local terminal backend and observed scheduled repository mutation. |

Supporting detail retained for reference:
- `experiments/results/2026-05-26-hermes-ovms-tool-envelope-smoke-test.md`
- `validation/notes/2026-05-26-ch09-local-hermes-deployment-inspection.md`
- `experiments/arc-b70-local-agent-benchmark-plan.md`

Note: before the workflow was simplified, Chapter 18 was first edited in a way
that treated its imported wording as immutable, then restored with a dated
correction appendix. That appendix remains an accurate record of the Hermes
finding; future chapter improvements may directly rewrite guidance while being
recorded here.

## 2026-05-26 - Chapter 18 Imported

Changed:
- Added `chapters/18-local-agent-arc-b70.md` from the uploaded Arc B70 local
  agent research document.
- Preserved the submitted document under `sources/original-docx/` and recorded
  its provenance in the existing source records.

Validation status:
- Most imported hardware, runtime-performance, model-selection, and tool-calling
claims were not validated at import time. Important current claims are tracked
in `VALIDATION.md`.
