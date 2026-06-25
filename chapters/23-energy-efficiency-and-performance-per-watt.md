## Corpus status (living layer)

**Last reconciled:** 2026-06-25
**Confidence:** **Supported** as a research direction (energy-per-task is the most defensible operationalization of "useful optimization"); **Unvalidated** as a deployed fitness channel; the privilege collision (RAPL is root-only post-PLATYPUS) is **Validated** against kernel/CVE record
**Read with:** [Chapter 00](00-benchmark-schema-and-measurement-validity.md) (`read_watts`, idle-power channel, `power_source` gap), [Chapter 02](02-bitcoin-native-economics-and-proof-of-useful-optimization.md) (proof of useful optimization), [Chapter 06](06-mutation-safety-and-permission-law.md) (least privilege), [Chapter 05](05-measurement-daemon-and-natural-language-shell.md) (daemon execution), [Chapter 08](08-population-confirmation-and-fleet-statistics.md) (hardware-scoped fitness, CV), [Chapter 14](14-gpu-and-accelerator-tuning.md) / [Chapter 18](18-local-agent-arc-b70.md) (GPU power)

### Authoritative for

- The distinction between **idle power as a penalty** (current schema) and **energy-per-task / performance-per-watt under load** as a positive, work-normalized fitness signal
- Which on-host energy interfaces exist, what they actually measure, and how trustworthy each is
- Why reading host energy collides with the unprivileged-daemon containment model

### Open until experiment/hardware

- A measured perf/watt noise floor (CV) on the tester fleet before any fitness weight
- A `power_source` + `energy_domain` + `power_method` record in structured output (extends Ch00 §3) so energy is comparable at all
- Whether dynamic (idle-subtracted) energy-per-task survives thermal/DVFS confounds across machines

---

## Reinforced research (2026-06-25)

- **RAPL accuracy:** Khan, Hirki, Niemi, Nurminen, Ou, "RAPL in Action: Experiences in Using RAPL for Power Measurements" (ACM ToMPECS 3(2), 2018) — RAPL energy is highly correlated with wall-plug power and accurate enough for server energy monitoring without external meters, with caveats (driver support, non-atomic register updates, timing jitter).
- **RAPL domains:** Weaver, "Reading RAPL energy measurements from Linux" — `package`, `PP0/cores`, `DRAM`, and `psys` (whole-SoC, Skylake+) zones; domains are hierarchical and `psys` is the closest on-die proxy for platform power.
- **Privilege collision:** Lipp et al., PLATYPUS (CVE-2020-8694 / CVE-2020-8695, 2020) — RAPL power side channel; mitigation restricts `energy_uj` to root, and the unprivileged AMD `amd_energy` hwmon path was removed in Linux 5.13 (commit `9049572fb`).
- **Standardized perf/watt:** MLPerf Power (arXiv:2410.12032) measures **samples/joule**; SPECpower_ssj2008 reports **ssj_ops/watt** — both define energy efficiency as work / energy, the framing this chapter imports.
- **GPU power caveats:** Yang et al., "Part-time Power Measurements: nvidia-smi's Lack of Attention" (arXiv:2312.02741) — NVML reports time-averaged power on a coarse update period, dropping a large fraction of the signal on A100/H100 and lagging real draw.

# Energy Efficiency and Performance-per-Watt as a Fitness Channel

Status: First research-synthesis pass (2026-06-25). The genesis fitness schema
rewards **speed** (cold-start, sustained, network) and applies an **idle-power
penalty** (Ch00 §2.2). It never measures **work per joule under load**. This
chapter argues that energy-per-task is the single most defensible operationalization
of CursiveOS's "proof of useful optimization" thesis (Ch02), surveys what can be
measured on-host and how much to trust it, and documents why reading host energy
collides with the unprivileged-daemon containment model (Ch05/Ch06).

## Why this chapter exists

CursiveOS's economic layer pays for *useful* optimization. "Useful" needs a
hardware-grounded, Goodhart-resistant definition. Pure throughput is gameable and
machine-specific; the project already learned (Ch00 §5) that a single scalar
"network delta" blends mechanisms and that idle power is the *least* comparable
channel. Energy-per-task — joules to complete a fixed unit of work — has three
properties the existing channels lack:

1. **It is monotone with the real externality.** Electricity is an actual cost
   borne by the contributor and the planet; lowering joules-per-task is a win that
   maps directly onto the thing Layer 5 is supposed to reward (Ch02).
2. **It is work-normalized**, so unlike idle watts it can survive cross-machine
   comparison *if* the work unit and the measurement domain are pinned.
3. **It resists the speed-only Goodhart.** A mutation that raises clocks to win
   cold-start but burns 2× the energy looks good on the current schema and bad on
   perf/watt — exactly the trade the organism should be able to see.

| Claim | Status |
| --- | --- |
| Current schema measures idle power as a penalty, never load energy-per-task | **Validated** (Ch00 §2.2 `read_watts`; fitness idle-power term) |
| Energy-per-task is the most defensible "useful optimization" signal | **Supported** (maps to real cost; standardized by MLPerf Power/SPECpower) |
| Perf/watt is ready to gate selection today | **Unvalidated** (no fleet CV; privilege + domain gaps below) |

## 1. What "energy" can actually be read on-host

`read_watts` (Ch00 §2.2) already walks a priority chain: Intel RAPL package energy
→ AMD powercap → GPU hwmon energy → hwmon instantaneous power → none. The hidden
problem is that these sources measure **different volumes of silicon**, so an
unlabeled watt figure is not comparable even on one machine.

| Interface | What it measures | Domain coverage | Trust |
| --- | --- | --- | --- |
| Intel RAPL `package` | one CPU package (cores + uncore) | no DRAM, no dGPU | high vs plug (RAPL in Action) |
| Intel RAPL `psys` | whole SoC (Skylake+) | closest on-die wall proxy | high but rarely exposed |
| Intel RAPL `DRAM` | memory controller energy | DRAM only | model-dependent |
| AMD RAPL (`core`/`package`) | cores / package via MSR | no DRAM, no `psys` | partial; coarser than Intel |
| GPU `hwmon energy*_input` | dGPU board energy counter | GPU only | good where present (Ch00 §5 item 7, A750) |
| NVML / `nvidia-smi` power | time-averaged board power | GPU only | **lossy** — see §3 |

Key facts that the harness must encode, not assume:

- RAPL domains are **hierarchical and overlapping**: `psys` ⊇ `package` ⊇ `cores`;
  `package` excludes DRAM. Summing `package` + `DRAM` + dGPU approximates platform
  energy; using `package` alone undercounts a GPU-bound inference run badly.
- **RAPL is not wall power.** Ch00 §2.2 already flags this; psys narrows the gap but
  is absent on many desktop SKUs. The economic argument ultimately cares about wall
  watts, so cross-machine energy claims need an external-meter calibration sample.

| Claim | Status |
| --- | --- |
| An unlabeled watt reading is not comparable across `package`/`psys`/GPU domains | **Validated** (RAPL domain hierarchy; Weaver) |
| `package`-only energy undercounts GPU-bound inference | **Supported** (domain coverage) |
| RAPL correlates well with plug power for CPU-bound server work | **Supported** (RAPL in Action) |

## 2. The privilege collision (why this is a Ch06 problem, not just Ch00)

After **PLATYPUS** (CVE-2020-8694/8695, 2020) showed RAPL energy is a power side
channel that leaks AES keys and defeats KASLR, the Linux mitigation **restricted
`/sys/class/powercap/intel-rapl/.../energy_uj` to root**, and the unprivileged AMD
`amd_energy` hwmon driver was **removed in Linux 5.13**. This directly contradicts
the corpus's containment model: Ch05/Ch06 want the measurement daemon to run with
**least privilege**, but the most accurate energy interface now requires either
root, a `setuid`/capability-scoped helper, or a relaxed `perf_event_paranoid` — each
of which widens the attack surface the daemon is supposed to minimize.

| Option for reading energy unprivileged | Cost |
| --- | --- |
| Run daemon as root | violates Ch06 least-privilege; worst case |
| Narrow `setuid` energy-reader helper | smallest surface; must be audited, rate-limited, read-only |
| Relax `perf_event_paranoid` / loosen `energy_uj` perms | re-opens the PLATYPUS side channel for any local code |
| Skip RAPL; use only what is world-readable | loses CPU energy on modern kernels |

| Claim | Status |
| --- | --- |
| RAPL `energy_uj` is root-only on mitigated kernels | **Validated** (PLATYPUS mitigation) |
| AMD `amd_energy` unprivileged path removed in 5.13 | **Validated** (commit `9049572fb`) |
| Energy sensing forces a measurement-vs-containment trade for the daemon | **Supported** (Ch05/Ch06) |
| A narrow read-only `setuid` energy helper is the least-bad path | **Supported** (smallest delegated capability) |

## 3. Measurement methodology and confounds

Energy-per-task only means something when the **work unit is fixed** and the
**confounds are controlled**. Borrowing from MLPerf Power (samples/joule) and
SPECpower (ssj_ops/watt):

- **Fixed-work, not fixed-time.** Measure joules to finish N tokens / N benchmark
  ops, not watts during a time window — otherwise a slower-but-cooler config looks
  "efficient" while doing less.
- **Dynamic vs total energy.** Report both total energy and **idle-subtracted
  (dynamic) energy** so a machine with a heavy idle floor is judged on the work it
  added, paralleling the idle-power penalty Ch00 already isolates.
- **Thermal / DVFS confound.** A cold run boosts then throttles; energy-per-task
  drifts with junction temperature and governor. Require warm-up to steady state and
  log governor/EPP, mirroring the Ch00 cold-start ordering and page-cache controls.
- **Sampling artifacts.** NVML averages over a coarse window and drops up to ~75% of
  the signal on A100/H100, lagging real draw (arXiv:2312.02741) — exactly the class
  of artifact that produced the bogus idle-power CV 0.83 (Ch00 §5 item 7) before the
  settle-and-resample fix. Prefer **energy counters** (`energy_uj`, `energy*_input`)
  integrated over the task to instantaneous power polling.

| Claim | Status |
| --- | --- |
| Energy efficiency = work / energy (samples/joule, ops/watt) | **Validated** (MLPerf Power, SPECpower) |
| Fixed-work integration beats fixed-time power averaging | **Supported** |
| Instantaneous power polling (esp. NVML) is artifact-prone | **Validated** (arXiv:2312.02741) |
| Perf/watt needs warm-up + governor logging like cold-start | **Supported** (Ch00 confound parallel) |

## 4. As a CursiveOS fitness channel

| Design choice | Recommendation | Status |
| --- | --- | --- |
| Add `energy_per_task_j` (total + dynamic) per benchmark channel | yes, behind `power_source`/`energy_domain` labels | **Unvalidated** |
| Weight perf/watt in fitness now | no — measure CV first (Ch08 ≤ 0.15 gate) | **Unvalidated** |
| Use perf/watt as a Goodhart counterweight to speed channels | yes, conceptually | **Supported** |
| Compare energy across machines without a domain label + meter sample | no | **Validated** (domain non-comparability) |
| Hardware-scope perf/watt wins like every other channel | yes | **Supported** (Ch08) |

The honest near-term role mirrors idle power (Ch00 §2.2): **directionally useful,
not yet selection-grade.** It should first ride alongside existing channels as an
observed-only field, accumulate a fleet CV, and only then earn a weight — and even
then as a *per-hardware* signal, never a global preset, per Ch08.

## 5. Open research gaps / experiments

1. **Perf/watt noise floor:** integrate energy over the existing benchmark suite on
   ≥2 tester machines; compute CV against the Ch08 0.15 gate before any weight.
2. **Domain-labeled schema:** ship `power_source`, `energy_domain`
   (`package`/`psys`/`pkg+dram+gpu`), and `power_method` (counter vs poll) — the
   minimum to make any energy number comparable (extends Ch00 §3).
3. **Setuid energy-reader prototype:** smallest read-only helper that gives the
   unprivileged daemon RAPL without re-opening PLATYPUS (Ch06 containment).
4. **Wall-meter calibration:** one external-meter sample per hardware class to bound
   the RAPL-vs-wall gap before cross-machine energy economics (Ch02).
5. **Energy-per-token inference channel:** joules per 1000 tokens for the local
   runtime (Ch10/Ch18), the most product-relevant efficiency metric.

## 6. Citations

| Source | Contribution |
| --- | --- |
| Khan, Hirki, Niemi, Nurminen, Ou — "RAPL in Action" (ACM ToMPECS 3(2), 2018) | RAPL accuracy vs plug power; caveats |
| Weaver — "Reading RAPL energy measurements from Linux" | domain hierarchy (package/PP0/DRAM/psys) |
| Lipp et al. — PLATYPUS (CVE-2020-8694/8695, 2020) | RAPL side channel → root-only `energy_uj` |
| Linux kernel — powercap docs; `amd_energy` removal (5.13, `9049572fb`) | unprivileged AMD energy path withdrawn |
| MLPerf Power (arXiv:2410.12032) | samples/joule; SPEC-approved meters for edge |
| SPECpower_ssj2008 (SPEC) | ssj_ops/watt server efficiency standard |
| "16 Years of SPEC Power" (arXiv:2411.07062) | x86 perf/watt efficiency trends |
| Yang et al. — nvidia-smi power measurement (arXiv:2312.02741) | NVML averaging/sampling loss |
| Chapter 00 §2.2, §5 item 7 | `read_watts` chain; idle-power channel; sampling artifact |

## Research questions answered

| Question | Answer |
| --- | --- |
| What is the strongest hardware-grounded "useful optimization" signal? | Energy-per-task (work / joules), monotone with real cost (**Supported**) |
| Does the current schema measure it? | No — only idle power as a penalty (**Validated**) |
| Can the unprivileged daemon read host energy? | Not RAPL without root/helper since PLATYPUS (**Validated**) |
| Is perf/watt comparable across machines as-is? | No — domain + wall-meter labeling required first (**Validated**) |
| Should it gate selection today? | No — observe-only until a fleet CV clears the Ch08 gate (**Unvalidated**) |
