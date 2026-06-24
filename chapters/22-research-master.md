<!--
Generated from a preserved DOCX source; wording is retained from the source.
Source: sources/original-docx/Research Master.docx
Git blob SHA: 081d0d5e31f2f3f8d3230e9c8db0ece7e50456f1
-->

## Corpus status (living layer)

**Last reconciled:** 2026-06-24
**Confidence:** Historical snapshot (March 2026); superseded for architecture and measurement
**Read with:** [INDEX.md](../INDEX.md) reading path; [Chapter 07](07-main-repo-gap-closure-and-research-backlog.md) for current gaps; Chapters 01–12 for organism, economics, and agent architecture

This file is a **point-in-time repo observation log** from March 2026. It is useful for understanding how the project looked during the TAO-OS → CursiveOS rebrand and early CursiveRoot schema work. It is **not** the current architecture spec.

### Use this chapter for

- Historical commit context and rebrand timeline
- Early kernel/GPU research leads (sched_ext, gpu_ext, Arc driver notes) as **leads to verify**, not validated claims

### Do not use this chapter for

- Current preset versions, harness behavior, or CursiveRoot schema — see main `CursiveOS` repo and Chapter 00
- Unscoped performance expectations (+5–15% inference claims) without harness validation
- Economics or incentive design — see Chapter 02

---


## Reinforced research (2026-06-24)

- **Historical scope only:** March 2026 repo snapshot during TAO-OS → CursiveOS rebrand — not current harness or schema truth.
- **Measurement canon migrated:** Network, noise-floor, and cold-start findings now authoritative in Ch00 + VALIDATION.md (not this import).
- **Architecture canon migrated:** Seed organism, economics, daemon/shell → Ch01, Ch02, Ch05; gap closure → Ch07.
- **Preserved value:** Early sched_ext, gpu_ext, Arc driver leads as *verify-before-claim* research items (Ch13, Ch14).
- **Do-not-cite:** Unscoped +5–15% inference expectations and pre-rebrand naming in external copy without living-layer check.

# Research Master

## Corpus integration notes (2026-06-24)

**Historical March 2026 snapshot only** — not current architecture, harness, or measurement canon.

1. **Preset versions / CursiveRoot schema:** See main `CursiveOS` repo + Ch00 for current harness truth — not this import.
2. **Network / cold-start magnitudes:** Migrated to Ch00 + VALIDATION.md — loopback figures are mechanism-only (Ch09).
3. **Economics / incentives:** Migrated to Ch01, Ch02, Ch05 — do not cite rebrand-era TAO-OS token assumptions.
4. **Kernel/GPU leads (sched_ext, gpu_ext):** Verify via Ch13/Ch14 + experiments before preset promotion.
5. **+5–15% inference claims:** **Unvalidated** — require Ch00 harness on target hardware class.

Block 1:

### GitHub Repo State – CursiveOS (formerly TAO-OS) – 26 March 2026

Repo URL: https://github.com/connormatthewdouglas/TAO-OS (now redirects / contains CursiveOS rebrand; official rename complete per commit e660e46).

Latest commits (last 5, reverse chrono):

- 2026-03-25: fa00576 – "rebrand: tao-forge → CursiveRoot everywhere + v0.8 preset bump with ROCm auto-enable"

- 2026-03-25: 04c34e1 – "script rename: cursiveos-full-test-v1.4.sh → v1.5 extended data collection (16 new fields + stability_flag)"

- 2026-03-24: e660e46 – "full rebrand TAO-OS → CursiveOS; white-paper v0.4.1 update; CursiveRoot schema v1.4"

- Earlier: hardware fingerprint hash enforcement + Supabase dashboard expansion.

README summary (excerpt): "CursiveOS is an AI-optimized, self-improving Linux distribution for crypto miners, local AI agents (Ollama, llama.cpp), and decentralized compute. Run benchmarks → data flows to CursiveRoot → AI generates better presets. Rebrand complete. Presets v0.8 live. Data flywheel active."

Main files/folders: cursiveos-full-test-v1.4.sh (now v1.5), presets/v0.8/, docs/ (white-paper.md, viability-report.md), supabase-schema.sql, CursiveRoot/ (data ingestion pipeline).

Open issues/PRs: None critical. One PR for "sched_ext GPU-awareness stub" (references Phoronix 2026-03-23).

Rebrand status: ForgeOS was temporary board name; final is CursiveOS per white-paper v0.4.1 and GitHub commits. Vision text now reads "CursiveRoot" for the self-improving data flywheel.

Block 2:

### 2026 Kernel & GPU Advances for CursiveOS (Fact-Checked March 26 2026)

**sched_ext GPU-awareness roadmap (Phoronix 23 Dec 2025 + 23 Mar 2026 updates):**

sched_ext (kernel 6.12+) now has explicit 2026 plans for GPU-aware scheduling and energy abstractions (Andrea Righi, NVIDIA). Key queued change for Linux 7.1 (merged for-next tree): SMT sibling prioritization for idle CPUs → 2–3% uplift on CPU-bound workloads. Broader roadmap includes GPU coordination (CPU-GPU task placement to reduce dispatch latency) and BPF hot-path optimizations. Meta is already deploying scx_lavd (sched_ext) on production servers for AI training fleets (LPC 2025 slides confirm 15% throughput gain via ML-predicted yield).

Direct CursiveOS tie-in: scx_rustland + scx_layered already in our preset stack; add GPU-awareness stub once 7.1 lands for inference/mining co-location.

**gpu_ext – eBPF for GPU UVM/scheduling (eunomia-bpf/github, active 2026):**

Direct sched_ext analog for GPU drivers. Enables eBPF-based GPU scheduling, UVM offloading, and CPU-GPU coordinated policies. Tested with bpftime runtime. Optional SCX_INCLUDE_DIR for sched_gpu_* binaries. Perfect low-overhead extension for our Intel Arc / AMD ROCm rigs.

**Intel Arc driver update (32.0.101.8626, 17 Mar 2026):**

Adds Shader Distribution Service (Mesa 26.1+ integration). Reduces first-load times up to 2× for large models (Black Myth: Wukong / Hogwarts Legacy traces). SLPC power_profile sysfs now defaults to 'base' with low-latency hints. Confirmed 260% compute uplift on Alchemist/Battlemage in specific workloads (Phoronix EOY 2025). SR-IOV now Pro-series only (B50/B60); consumer cards limited to 7 VFs via i915-sriov-dkms (no change for our A750 validation).

**AMD ROCm / RX 580 relevance:** v0.8 preset auto-enable confirmed; pairs with amdgpu.runpm=0 and pp_power_profile_mode=COMPUTE for cold-start wins on older Polaris cards.

**Data for CursiveRoot:** These patches map directly to our network/cold-start/sustained deltas. Expected: +5–15% inference tok/s on mixed workloads once integrated.

Block 3:

### AI-Guided Tuning Integration Hooks for CursiveRoot (Tied to Doc 5 Papers – 2026)

**OS-R1 / AutoOS priority (Lin/Chen papers):**

Use CursiveRoot JSON exports (hardware_fingerprint_hash + delta_pct fields) as RL observations. Reward = normalized (network_delta_pct * 0.4 + coldstart_delta_pct * 0.4 + sustained_delta_pct * 0.2) with rule-based validity (stability_flag=1). GRPO/PPO loop can ingest our 16 new v1.5 fields directly. Prototype effort: feed TAO/CursiveRoot metrics into verl library → generate preset diffs.

**SchedCP / PolicySmith extensions:**

MCP control plane consumes our eBPF telemetry (L3 cache misses, branch misses from hardware_fingerprint). Generate scx_* policies or NUMA/THP heuristics. Transactional BranchFS (first-commit-wins) aligns with our reversible preset design.

**Always-On LLM agent (Liargkovas NeurIPS 2025):**

Prompt template: "Recent CursiveRoot deltas: [paste last 5 runs]. Propose one reversible sysctl/sysfs change." Enforce MCP + commit/revert. Fits our "always-on" vision for Copper Autonomy Score.

**CursiveRoot schema extension recommendation (for future v1.6):**

Add fields: `sched_ext_policy_applied`, `gpu_svm_enabled`, `zram_writeback_batch_size`, `aes_ctr_throughput_mbps`. Enables direct training of Doc 5 models on our data flywheel.
