# Research Changelog

This file records meaningful changes to research guidance, validation status,
and corpus process. It is intended to be readable without reconstructing a
chain of supporting documents.

## 2026-06-25 - Cycle-2 zram inconclusive + memory-pressure sensor gap

Changed:
- **Chapter 01** (`01-seed-organism-and-sensor-array.md`): added a "Known coverage gap — no memory-pressure sensor" note under Performance Sensors, grounded in the cycle-2 `candidate-v0.10-zram` inconclusive screen; added Open Research Gap #6 (memory-pressure sensor + swappiness-aware variant).
- **VALIDATION.md**: two new rows — "Chapter 01 / zram cycle-2 screen" (Unvalidated, inconclusive: fitness ≈ −0.0257, confidence 0.50, single screen) and "Chapter 01 / memory-pressure sensor gap" (Supported).

Reason:
- Honest record of the organism's first *added* optimization (cycle 2). zram's benefit lives in a channel the genesis suite does not measure, so the screen correctly read neutral and only proved safe apply/revert + non-regression — pre-registered in the variant hypothesis. Treat zram as an unscreened lead, not a rejected one. Note: the bundle did not reach CursiveRoot because of the `seed_bundles` RLS upsert bug, fixed the same day (CursiveOS `c65c5ef`, merge-duplicates → ignore-duplicates).

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
