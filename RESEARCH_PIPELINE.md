# Research Pipeline

Status: Active research queue for the CursiveResearch corpus.  
Purpose: help agents and contributors see what foundational research is missing, which knowledge gaps remain, and which experiments can produce evidence for the corpus.

## Boundary

This repository is a **research corpus**, not the implementation specification for CursiveOS.

- Use this repo to collect papers, technical literature, external systems, operating-system knowledge, hardware behavior, economics research, security research, and general scientific grounding.
- Use the main `CursiveOS` repo for organism specs, implementation plans, product architecture, roadmap, scripts, schemas, and executable design.
- If a research item becomes a concrete build task, it should graduate into the main `CursiveOS` repo as a spec, issue, experiment script, or implementation artifact.

The pipeline is intentionally trifurcated:

1. **New Research** — foundational literature and external systems to add to the corpus.
2. **Knowledge Gaps** — conceptual gaps the corpus should answer more deeply.
3. **Experimental Lift** — physical/local experiments proposed by corpus chapters or needed to convert research claims into evidence.

---

# 1. New Research

New Research items are not implementation specs. They are literature and source-gathering targets that should deepen the corpus before we make implementation decisions.

## P0 — Recursive Self-Improvement and Self-Improving Agents

### Why this matters

CursiveOS is explicitly about self-improving software. The corpus needs a deeper literature base around recursive self-improvement, self-modifying agents, evolutionary coding agents, self-play, verifier/updater loops, metacognition, and agent evaluation.

### Research targets

| Topic | Starting Sources | What to extract |
| --- | --- | --- |
| Gödel-style self-referential agents | `Gödel Agent: A Self-Referential Agent Framework for Recursive Self-Improvement` | Self-modification loop, objective definition, verifier/fitness function, failure modes, limits. |
| Self-Taught Optimizer / recursive code improvement | `Self-Taught Optimizer (STOP): Recursively Self-Improving Code Generation` | How scaffolds improve themselves, what safety rails are required, what constitutes improvement. |
| Evolutionary coding agents | Google DeepMind `AlphaEvolve`; open-source AlphaEvolve-style systems such as OpenEvolve | Mutation/selection loop, evaluation functions, algorithm discovery, relation to CursiveOS variants. |
| Long-horizon agent skill accumulation | `Voyager: An Open-Ended Embodied Agent with Large Language Models` | Skill library, curriculum, environment feedback, persistent capability accumulation. |
| Self-rewarding and self-judging models | `Self-Rewarding Language Models`; `Agent-as-a-Judge` | Whether agents can evaluate their own outputs, where self-evaluation fails, how to prevent evaluator drift. |
| Metacognitive self-improvement | `Truly Self-Improving Agents Require Intrinsic Metacognitive Learning` | Self-assessment, planning, evaluation, and division of responsibility between human and agent. |
| Test-time self-improvement | `Test-time Recursive Thinking` and related self-consistency/verification work | Candidate generation, self-verification, no-training improvement, limits of self-feedback. |
| Agent evaluation quality | `AI Agents That Matter` and agent benchmark criticism | How to avoid fake progress, benchmark overfitting, and agent demos that do not transfer. |

### Desired corpus output

**Status (2026-06-24):** Delivered as merged Chapter 03 (`03-rsi-literature-and-organism-synthesis.md`, former Ch03+Ch04)
(critical synthesis) + **25 papers** under `papers/`. Remaining work: source-level
validation of individual RSI claims and graduation of experiment plans.

It should answer:

- What forms of self-improvement are actually demonstrated in current literature?
- Which loops require ground-truth/verifiable rewards?
- Which loops depend on LLM self-judgment and therefore risk drift?
- What is the analog of mutation, verifier, evaluator, archive, and selection pressure in CursiveOS?
- How does CursiveOS avoid letting the local shell agent corrupt the measurement loop?

## P0 — Firmware, BIOS, and Agent-Operable Control Surfaces

### Why this matters

Chapter 17 now includes a first source-backed control-surface matrix and
`sources/firmware-control-surfaces-selected-sources.md` records the primary
interfaces reviewed. The remaining work is a platform/vendor matrix and real
hardware probing, not another abstract pass over the idea.

### Research targets

| Topic | Starting Sources | What to extract |
| --- | --- | --- |
| UEFI runtime variables | UEFI spec, Linux `efivarfs`, `efibootmgr`, `efivar` docs | Which variables are standardized, which are vendor-specific, what can be changed safely, what needs reboot. |
| Linux firmware attributes | Linux `/sys/class/firmware-attributes` documentation | Supported vendors, attribute types, pending reboot semantics, real examples. |
| Redfish BIOS settings | DMTF Redfish BIOS schema and vendor BMC docs | BIOS attribute registry, pending settings resource, reset-required state, auth model. |
| fwupd / LVFS / UEFI capsule updates | fwupd docs, LVFS docs, UEFI capsule update docs | Firmware update path from OS, reboot staging, failure modes, supported hardware. |
| SMBIOS / DMI read-only inventory | DMTF SMBIOS docs, `dmidecode` | What inventory can be trusted, what is spoofable, how to use it for hardware fingerprints. |
| Vendor BIOS tools | Dell Command Configure, Lenovo WMI/firmware attributes, HP BIOS Configuration Utility, Supermicro/IPMI tools | Practical setting coverage by vendor. |
| Open firmware path | coreboot, EDK2/TianoCore, OpenBMC | What changes when firmware is open and buildable rather than vendor-locked. |
| Firmware observability/security | UEFI bootkit detection, Peacock-style runtime observability, measured boot/TPM | How to observe firmware mutation safely and detect corruption. |

### Desired corpus output

Further expand **Firmware and BIOS Control** only when new platform-specific
evidence is available.

The next useful output should be a tested matrix like:

| Setting Class | Examples | Interface | Apply Time | Standardized? | Risk | CursiveOS Use |
| --- | --- | --- | --- | --- | --- | --- |
| Boot order | Boot#### variables | UEFI variable / Redfish | reboot | partly | medium | controlled boot testing |
| Secure Boot | enable/disable, keys | UEFI / vendor / Redfish | reboot | partly | high | security state capture |
| Virtualization | SVM/VT-x/IOMMU | vendor BIOS / Redfish | reboot | vendor-specific | high | lab tuning only |
| Power profile | performance/efficiency | firmware-attributes / Redfish | reboot or runtime | vendor-specific | medium | workload profile |
| PCIe settings | ASPM, bifurcation, resizable BAR | BIOS / Redfish | reboot | vendor-specific | high | GPU/rack experiments |
| Fan/thermal | fan curves, thermal mode | BMC/vendor | runtime/reboot | vendor-specific | medium | thermal stability |

## P0 — Software Organisms, Autopoiesis, and Evolutionary Systems

### Why this matters

The biological framing is non-negotiable for the project, but the corpus needs more foundational research beyond metaphor. We need literature that distinguishes living systems, autopoiesis, cybernetics, evolutionary algorithms, artificial life, and self-maintaining computational systems.

### Research targets

| Topic | Starting Sources | What to extract |
| --- | --- | --- |
| Autopoiesis | Maturana and Varela; later artificial life critiques | What makes a system self-producing vs merely automated. |
| Cybernetics and viable systems | Stafford Beer / Viable System Model | Sensor/control loops, recursion, viable organization, governance-free feedback. |
| Artificial life | Langton, Tierra, Avida, open-ended evolution literature | Conditions for open-ended evolution and why most systems plateau. |
| Evolutionary computation | Genetic programming, novelty search, quality-diversity algorithms | Mutation/selection/archive mechanisms relevant to CursiveOS. |
| Digital ecosystems | Software ecosystems, open-source community evolution | How forks, contributions, and platform ecology evolve. |
| Goodhart and measurement | Goodhart's Law, proxy gaming, benchmark overfitting | How sensors can be corrupted by optimization pressure. |

### Desired corpus output

Create or expand a chapter on **Software Organisms and Open-Ended Evolution**.

It should separate:

- metaphor;
- structural analogy;
- measurable organism properties;
- implementation consequences for CursiveOS.

Status (2026-06-22): a first literature pass landed as Chapter 03 §"Biological
and Artificial-Life Foundations of the Organism Framing" — autopoiesis
(Maturana & Varela), cybernetics/VSM + Ashby's Law (Beer), artificial life
(Langton, Tierra, Avida/Lenski 2003), and open-ended evolution (novelty search,
MAP-Elites, POET), with the metaphor/analogy/property/consequence separation
requested above. Remaining: a dedicated standalone chapter if the topic grows,
deeper open-ended-evolution and quality-diversity reading, and source-level
extraction of the cornerstone ALife papers.

## P1 — Local Agent Architecture and Safety Literature

### Why this matters

Chapter 15 now includes a first source-backed external safety pass, and
`sources/local-agent-safety-selected-sources.md` records the reviewed material.
The corpus also ingested rights-cleared full-text paper folders for SWE-bench,
SWE-agent, and OSWorld. The daemon/shell split is supported by the literature;
the next research pass should go deeper on specific memory systems, terminal
agent benchmark design, and concrete containment prototypes.

### Research targets

| Topic | Starting Sources | What to extract |
| --- | --- | --- |
| Agent safety and prompt injection | OWASP LLM/agent risks, recent agent security papers | Tool-use risk, privilege boundaries, indirect prompt injection. |
| Human-in-the-loop command execution | CLI agent UX, command preview systems, reversible ops | Confirmation UX patterns and failure modes. |
| Agent memory systems | MemGPT, Mem0, MemOS, long-term memory papers | What memory belongs in shell vs daemon vs CursiveRoot. |
| Agent benchmarks | SWE-bench, SWE-agent, OSWorld, WebArena, AgentBench, AI Agents That Matter | Which evaluations map to terminal/OS operation; SWE-bench, SWE-agent, and OSWorld already have full rights-cleared paper folders. |
| Sandboxing and least privilege | gVisor, Firecracker, namespaces, seccomp, Landlock | Containment for unattended tool execution. |

### Desired corpus output

Further expand Chapter 15 when new evidence changes shell memory, tool policy,
confirmation UX, or containment guidance. If the topic grows beyond shell
safety, split out a dedicated **Local Agent Safety and Operator Interfaces**
chapter.

## P1 — Hardware Optimization Foundations

### Why this matters

The existing chapters contain many optimization leads. We need more foundational systems knowledge around why the knobs work, not just which knobs exist.

### Research targets

| Topic | Starting Sources | What to extract |
| --- | --- | --- |
| Power-state latency | CPU C-states, GPU P-states, PCIe ASPM, residency counters | Wake latency, idle-power tradeoffs, measurement methods. |
| Linux scheduler fundamentals | CFS/EEVDF, PREEMPT_RT, sched_ext, SCHED_DEADLINE | Which workloads benefit from which scheduling model. |
| Memory pressure | zram, PSI, THP, hugepages, NUMA balancing | When memory tuning helps inference and when it hurts. |
| Network transport | BBR, CUBIC, fq, BDP, buffer autotuning | Why loopback WAN simulation shows large deltas and what it does not prove. |
| GPU runtime stacks | SYCL, Vulkan, OpenVINO, Level Zero, ROCm, CUDA | How runtime overhead, kernel cache, and driver maturity affect local agents. |

### Desired corpus output

Expand Chapters 07/04/09 with explanatory foundations, not just tuning recipes.

**Status (2026-06-25):** the **energy** strand is now partially served by new
**Chapter 23 (Energy Efficiency and Performance-per-Watt)** — RAPL domains/accuracy,
the PLATYPUS root-only privilege collision, and MLPerf Power / SPECpower perf-per-watt
methodology, framed as a candidate fitness channel (proof of useful optimization,
Ch02). Remaining: a measured fleet CV for energy-per-task, a domain-labeled
`power_source`/`energy_domain` schema, a least-privilege `setuid` energy-reader
prototype, and wall-meter calibration before any fitness weight. Power-state latency,
scheduler, and GPU-runtime strands remain open.

## P1 — Arc B70 and Intel AI Stack Research

### Why this matters

Arc B70 may be a strong workstation-tier CursiveOS accelerator, but the corpus still needs better independent grounding.

### Research targets

| Topic | Starting Sources | What to extract |
| --- | --- | --- |
| Arc Pro B70 architecture | Intel docs, board vendor docs, independent reviews | Memory, ECC, bandwidth, XMX, power, driver stack. |
| OpenVINO GenAI | Intel docs and model support matrix | Tool calling, structured generation, cache behavior, model support. |
| llama.cpp SYCL/Vulkan | upstream docs/issues/benchmarks | Backend maturity, model support, quant support, B70-specific behavior. |
| Multi-GPU Intel scaling | oneAPI/Level Zero docs, community benchmarks | Whether multiple B70s scale for local agents or just batch workloads. |
| Model selection | Qwen, Gemma, Llama, Mistral, Hermes-style local agents | Tool-call reliability per watt, context behavior, JSON validity. |

### Desired corpus output

Expand Chapter 18 from imported research into a durable Intel local-agent research chapter.

## P2 — Economics, Forks, and Knowledge Commons

### Why this matters

CursiveOS moved away from tokenomics, but its Bitcoin-native economic layer still raises foundational questions.

### Research targets

| Topic | Starting Sources | What to extract |
| --- | --- | --- |
| Open-source contribution economics | OSS maintainership, funding models, contributor retention | How durable contribution incentives work without governance tokens. |
| Fork obligations | licenses, contributor license agreements, Bitcoin-anchored ledgers | Whether fork obligation inheritance is legal, technical, social, or reputational. |
| Proof-of-work vs proof-of-useful-work | Bitcoin, DePIN, Filecoin, Render, Helium, Bittensor | Why proof of useful optimization differs from hardware ownership or token staking. |
| Anti-Sybil economics | web-of-trust, staking, proof-of-personhood, hardware identity | How to resist fake contributors/testers without governance. |

### Desired corpus output

Chapter 02 already has the internal model. Add external grounding so the model knows what it is borrowing from and rejecting.

---

# 2. Knowledge Gaps

Knowledge Gaps are questions the corpus should answer with research synthesis before they become implementation specs.

## P0 Knowledge Gaps

| Gap | Why It Matters | Best Next Action |
| --- | --- | --- |
| What kinds of recursive self-improvement are real today versus theoretical? | Prevents CursiveOS from overclaiming self-improvement. | Literature review across STOP, Gödel Agent, AlphaEvolve, Voyager, self-rewarding models, metacognition, and agent evaluation. |
| Which firmware/BIOS settings are actually agent-operable across real hardware? | Determines whether the BIOS-control layer is practical or mostly server/BMC-only. | Build a vendor/interface matrix from UEFI, Redfish, firmware-attributes, fwupd, Dell/Lenovo/HP/Supermicro docs. |
| What makes a software system an organism rather than an automation pipeline? | Protects the core theoretical framing from becoming vibes. | Research autopoiesis, cybernetics, artificial life, open-ended evolution, and Goodhart. |
| How should CursiveOS handle hardware-scoped truth? | Prevents one-machine wins from becoming harmful global presets. | Synthesize benchmark statistics, fleet confirmation, hardware fingerprinting, and transfer learning. **Prior-art pass delivered (2026-06-24):** Chapter 03d surveys decentralized-computation verification (replication/spot-checking, dispute games, TEE attestation, zk proofs, stake-weighted consensus) and shows hardware-scoped fitness can use only the statistical/credibility-weighted end. Remaining: adversarial test of whether Ch08 confirmation behaves as a sabotage-tolerance layer. |
| What should the local shell agent remember? | Memory can help UX but can also create privacy/security risks. | Research agent memory systems and define what belongs outside CursiveRoot truth. |

## P1 Knowledge Gaps

| Gap | Why It Matters | Best Next Action |
| --- | --- | --- |
| When does network tuning transfer from simulation to real distributed workloads? | Current network deltas are strong but isolated. | Research BBR/BDP literature and compare to real P2P/mining/inference traffic patterns. |
| What is the right evaluation stack for OS-operating agents? | The natural-language shell needs benchmarks beyond chat quality. | Survey OSWorld, SWE-bench, AgentBench, WebArena, terminal-agent evaluations. |
| How do current agent systems fail under privilege? | Root-capable agents are dangerous. | Initial synthesis delivered in Chapter 06 (Mutation Safety and Permission Law): least-privilege model, OWASP Excessive Agency, mutation-class → containment matrix. Remaining: deeper prompt-injection/tool-attack survey and a class-0 containment prototype. |
| Which hardware identity signals are stable enough for population confirmation? | Spoofing resistance depends on hardware fingerprints. | Research SMBIOS/DMI, GPU VBIOS, TPM, attestation, kernel version, microcode. |
| What is the strongest non-token incentive model for open infrastructure contributors? | Layer 5 is novel and needs external grounding. | Research OSS funding, bounty systems, revenue share, credit systems, Bitcoin payments. |

## P2 Knowledge Gaps

| Gap | Why It Matters | Best Next Action |
| --- | --- | --- |
| Can fork obligation inheritance be enforced or only signaled? | Chapter 02 depends on it conceptually. | Legal/technical literature review. |
| Can CursiveOS become workload-native without privacy leakage? | Workload classification could be invasive. | Research local-only classification and privacy-preserving telemetry. |
| Can open firmware meaningfully improve self-optimization? | Coreboot/OpenBMC may unlock deeper control but narrow hardware. | Research supported boards and server platforms. |
| How should CursiveOS distinguish substrate compounding from capital compounding? | Important to the biological/economic thesis. | Research knowledge commons, institutional memory, software ecosystem growth. |

---

# 3. Experimental Lift

Experimental Lift items are tests proposed by the corpus. These belong in `experiments/` as plans/results or in the main `CursiveOS` repo when they become executable scripts. They should not replace foundational research.

## Existing Experiment Plans / Proposed Experiments

| Experiment | Source Chapter(s) | Purpose | Current Status | Next Action |
| --- | --- | --- | --- | --- |
| Arc B70 local-agent benchmark | Chapter 18 | Validate B70 runtime/model/tool-call claims. | Plan exists. | Run on target B70 hardware; compare SYCL, Vulkan, OpenVINO, model families, tool-call reliability. |
| Kernel inference optimization benchmark | Chapter 07 | Test sched_ext, PREEMPT_RT, zram, fscrypt, kernel versions against inference workloads. | Plan exists. | Implement runner and collect local results. |
| AI-guided tuning loop validation | Chapter 15 | Test whether bounded agent tuning beats defaults/random/heuristics. | Superseded by sharper plan below (`proposer-vs-random-tuning-experiment.md` tests CH05-BM-002 directly). | Use the proposer-vs-random experiment as the canonical instance. |
| Proposer vs random search (sharpened) | Chapter 15/16/10 | Single powered, falsifiable test of CH05-BM-002: does the LLM proposer beat random search over the same allowlist at equal budget, scored only on the cold-start channel? | Proposed (`experiments/proposer-vs-random-tuning-experiment.md`). | Build the arm driver in main repo; run on Stardust with n=3 cold-start confirmations; check H1 (peak fitness) and H2 (drops the inert decoy knob). |
| GPU/accelerator tuning validation | Chapter 03 | Probe device-specific controls and test power/clock/SR-IOV/hugepage/IO claims. | Plan exists. | Start with read-only hardware capability probe. |
| Security hardening validation | Chapter 22 | Validate firewall, SSH, monitoring, sandbox, supply-chain controls. | Plan exists. | Convert into tiered hardening baseline only after testing. |
| Firmware/BIOS capability probe | Chapter 06 | Discover which BIOS/firmware settings are observable/changeable on target hardware. | Proposed. | Build read-only matrix first: efivarfs, firmware-attributes, Redfish, fwupd, vendor tools. |
| Seed organism parent-vs-candidate screen | Chapter 01 / main repo | Run parent-vs-candidate screens via the one-paste seed session (current: v0.9c-cpu-retained parent, v0.10-zram candidate). | In progress in main repo (seed-session script + screen-verdict analyzer shipped 2026-06-11). | Repeat and counterbalance before any acceptance; confirm v0.9c on second machine; screen v0.10-zram. |
| Cold-start order / page-cache confound | Chapter 22 / 10 | Test whether the −51% Arc cold-start win is partly a baseline-first / tuned-second or warm-page-cache artifact. | Proposed (`experiments/cold-start-order-cache-confound-plan.md`). | Run three-arm counterbalance + cache-control on Stardust (~1 afternoon); harden or downgrade cold-start as a selection channel per pre-registered thresholds. |
| Idle-power selection-channel validation | Chapter 22 / 10 | Test whether the 2026-06-16 harness idle-power fix (settle + more samples) makes idle power a selection-usable channel (CV ≤ 0.15) in the production full-test path across hardware. | Proposed (`experiments/idle-power-selection-channel-validation-plan.md`). | Run on Stardust + second machine; ship `power_source` field as a side effect; decide whether idle power can gate selection. |
| Real-path network A/B | Chapter 22 | Bound how much of the loopback CUBIC-vs-BBR signal transfers to a real LAN/WAN path. | Done (2026-06-16): whole win is BBR; buffer stack ~0% on ≤1GbE. | High-BDP (>1Gbit/high-latency WAN) path still untested before any buffer claim. |
| Cold-start mechanism + hardware-scoping predictor | Chapter 22 / 10 | Isolate which single CPU knob (governor/EPP/C-state) carries the −51% desktop cold-start win, and test whether a cheap idle-exit pre-probe predicts which machines benefit. | Proposed (`experiments/cold-start-mechanism-and-hardware-scoping-plan.md`). | Run 2³ factorial on desktop; run pre-probe vs preset-gain across all tester machines. |
| Cold-start model/runtime transfer | Chapter 00 / 10 | Test whether the validated cold-start preset gain survives a change of model, quantization, or runtime on one machine — does the fitness key need a `(model × quant × backend)` dimension, or is the idle-exit saving model-portable? | Proposed (`experiments/cold-start-model-runtime-transfer-plan.md`). | Run ~6-cell config matrix on Stardust with v0.9c preset held fixed; separate absolute-saving (ms) from percentage gain; decide cold-start fitness key. |
| Power-source normalization | Chapter 22 | Make idle-power data comparable across machines. | Proposed (main repo build task). | Record `power_source`/method in structured results; only pool cross-machine power data after the field exists. |
| Every-run detail bundles | Chapter 22 | Get per-pass variance into CursiveRoot for all runs, not just seed-path runs. | Proposed (main repo build task). | Upload `run_detail_bundles` from the plain benchmark path; then calibrate CV/N rules on variance-bearing data. |
| Concurrent inference throughput benchmark | Chapter 22 / action plan parking lot | Measure requests/sec under parallel load, where scheduler tweaks should actually show. | Proposed. | Add a concurrency benchmark mode before claiming scheduler-tweak inference value. |
| Memory-pressure sensor noise floor | Chapter 01 (Open Gap #6) / 00 / 08 | Measure the CV of the new `benchmark-memory-pressure-v0.1.sh` refault-time probe across reps + machines; gate it into fitness as a fifth channel only if CV ≤ 0.15, then re-screen the inconclusive `candidate-v0.10-zram`. | Proposed (`experiments/memory-pressure-sensor-noise-floor-plan.md`). | Run Z/D/N conditions ×10 on Stardust + the i5-11300H; check H1 (CV ≤ 0.15), H2 (zram mm_stat engages), H3 (regime discrimination), then H4 (zram re-screen). |
| Population confirmation calibration | Chapter 01 | Test N-confirmation rule and CV threshold as fleet grows. | Proposed. | Use tester fleet data; calibrate CV <= 0.15 and N rule. |
| Immune sensor prototype | Chapter 01/11 | Detect spoofing, correlated machines, fake benchmark farms, curator self-dealing. | Proposed. | Start with anomaly profiles and measurement correlation. |
| Measurement daemon prototype | Chapter 15 / main repo | Implement deterministic sensor execution, local queue, signed submission, scoped helper. | Specified, not implemented. | Build in main repo; corpus can research daemon patterns and failure modes. |
| Natural-language shell UX experiment | Chapter 15 | Test command preview, read/write/root modes, confirmation boundaries. | Proposed. | Prototype UI in main repo; corpus should research prior agent UX/safety. |
| Signed preset update channel | Chapter 15 / roadmap | Test staged signed presets, local regression, rollback, divergence reporting. | Proposed. | Build after daemon prototype. |
| Local agent containment test | Chapter 18/12 | Ensure unattended execution cannot mutate host/repo without approval. | Existing local risk found. | Keep mutating automation disabled until containment/approval boundary exists. |
| CursiveRoot schema pressure test | Chapter 01/11 | Validate whether database can represent raw runs, sensor outputs, confirmation sets, fitness, and payout links. | Proposed. | Main repo spec/implementation task; corpus should research evidence schemas. |
| Metabolic sensor simulation | Chapter 02 | Simulate current/lifetime split under contributor histories and attack scenarios. | Proposed. | Run synthetic contributor simulations before real payment. |
| Fork obligation research/prototype | Chapter 02 | Explore Bitcoin anchoring, fork visibility, legal/social enforcement. | Proposed. | Treat as research-heavy before implementation. |

## Experimental Lift Rule

When a question requires trial and error on real hardware or the actual CursiveOS system, put it here or under `experiments/`. Do not let experimental questions crowd out the core research queue.

The corpus should ask:

```text
What does existing knowledge say?
What does our system need to test for itself?
What evidence would change our mind?
```

Then the implementation repo should answer:

```text
What script, daemon, schema, UI, or release artifact do we build?
```
