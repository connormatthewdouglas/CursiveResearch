# Benchmark Schema and Measurement Validity

Status: First assessment pass (2026-06-11), grounded in the actual main-repo
harness (`cursiveos-full-test-v1.4.sh`, wrapper v1.4.1), the live CursiveRoot
schema (`runs`, `run_detail_bundles`, `seed_bundles`, `machines`,
`machine_aliases`), and 77 production run rows from 5 machines.
Use it for: deciding what the current numbers do and do not prove, and what
the measurement layer should collect next.

## Why this chapter exists

The organism's entire truth model (Chapter 10) reduces to: *sensor result +
schema validity + confidence + gates + population confirmation = evidence*.
That chain is only as strong as the measurement at its base. The corpus had
research on sensors, evidence, and Goodhart risk, but no assessment of what
the deployed benchmark suite actually measures, how trustworthy each channel
is, and where the schema silently discards information. This chapter is that
assessment.

## 1. What the suite measures today

| Channel | Method | Stored in `runs` | Detail available |
| --- | --- | --- | --- |
| Network throughput | iperf3 over **loopback** with `tc netem` (50ms RTT, 0.5% loss); compares **CUBIC baseline vs BBR-tuned**; 5 passes | baseline/tuned/delta (single values) | per-pass rates, retransmits, RTT in logs → `run_detail_bundles` when the seed path runs |
| Cold-start latency | GPU idle → first token; load duration, TTFT | baseline/tuned/delta | per-call GPU-before frequency, load, TTFT in logs |
| Sustained inference | warm model steady-state tok/s via Ollama | baseline/tuned/delta | per-pass rate, TTFT, CPU/GPU classification in logs |
| Idle power | median of up to 5 × 1-second readings per condition | baseline/tuned/delta watts | raw sample arrays in result JSON |
| Stability | dmesg errors, throttle events, stability flag | counts + flag in notes/columns | summary log |
| Identity | hardware fingerprint v2 (CPU model, board, GPU PCI ids) | `machine_id` joins `machines`/`machine_aliases` | — |

Strengths worth keeping: reversibility (presets reverted at run end), repeat
passes inside the network benchmark, median-with-raw-samples for power,
processor classification for sustained inference, fingerprint-keyed identity
that survives kernel updates, and append-only audit bundles. This is already
better instrumentation than most hobby benchmarking.

## 2. Validity assessment per channel

### 2.1 Network (+450–900% headline) — real effect, narrow scope

The measured delta is real *within the emulation*, but three scope limits
must travel with the number:

1. **It is substantially a congestion-control comparison.** The benchmark
   labels sides "Baseline (CUBIC)" vs "Tuned (BBR)". Under random 0.5% loss,
   CUBIC interprets loss as congestion and collapses its window; BBR ignores
   random loss by design. A large CUBIC-vs-BBR gap under lossy netem is the
   *expected, well-documented* behavior of the algorithms, not a discovery
   about this hardware. Much of the +500% is attributable to one sysctl
   (`net.ipv4.tcp_congestion_control=bbr`).
2. **Loopback is not a NIC.** The path never touches a physical adapter,
   driver queue, interrupt coalescing, or offload engine. netem-on-loopback
   demonstrates transport-stack behavior, not end-to-end network performance.
3. **Single emulated condition.** One RTT/loss point (50ms/0.5%) cannot
   support a general "WAN transfer" claim; BBR-vs-CUBIC outcomes vary
   strongly with loss model, buffer depth, and competing flows.

**Correct claim:** "under emulated lossy-WAN transport conditions, the tuned
stack (chiefly BBR) sustains 5–9× the throughput of default CUBIC." Claims
about real mining-pool, P2P, or inference-API traffic remain unvalidated
(this matches the existing P1 gap in `RESEARCH_PIPELINE.md`).

### 2.2 Idle power — the least comparable channel

`read_watts` selects, in priority order: Intel RAPL package energy → AMD
powercap → GPU hwmon energy counter → hwmon instantaneous power →
turbostat. Consequences:

- **Different machines report different physical quantities** (CPU package
  vs GPU-only vs platform), and **the chosen source is not recorded in the
  structured result** — it only appears in stderr guard logs. Cross-machine
  comparisons of `power_idle_*_w` (e.g. Vega's +3.2W vs the README's ~+14W)
  may compare package power to GPU power without anyone knowing.
- Five back-to-back 1-second samples taken immediately after benchmark
  activity bias the "idle" reading upward (C-state settling, fan/VRM tails).
- RAPL/package power is not wall power; the economic argument ("idle power
  cost") ultimately cares about wall watts.

The idle-power *penalty term* in fitness is therefore directionally useful
on a single machine (same source, same session) but is not yet fleet-grade
evidence. This matters because the entire v0.9-network-efficient screen
hypothesis is "keep network, recover the idle-power cost."

### 2.3 Cold-start and sustained inference — honest but under-described

- Order is fixed (baseline first, tuned second) within a session; thermal
  and cache state drift in one direction. The project already requires
  counterbalanced repeats before acceptance — correct, keep it.
- Page-cache state strongly affects model load: the first cold-start of a
  session reads from disk, later ones from cache. Not recorded.
- Sustained tok/s is single-stream only; scheduler tweaks mostly pay off
  under concurrency, which is unmeasured (acknowledged in the action plan).
- The Ollama model, quantization, and version are recorded only in
  benchmark context, not in `runs` columns, so cohort medians can silently
  mix models across time.

### 2.4 Schema observations

- `sample_counts` in the result JSON hardcodes `network: 1` although the
  network benchmark performs 5 internal passes — under-reporting evidence.
- `runs` collapses each channel to three scalars; variance lives only in
  detail logs and reaches CursiveRoot only via the seed path
  (`run_detail_bundles`). The plain benchmark path uploads no variance, so
  the analyzer's cross-session CV mixes measurement noise with real drift.
- No structured fields for: power source, AC/battery state, governor in
  effect during baseline, model/quant, page-cache state, netem verification,
  per-phase timestamps, ambient/package temperature at phase start.
- `notes` is a parseable-by-regex string carrying load-bearing data
  (`hw:`, `stability:`, `kernel:`) — workable, but fragile as schema.

## 3. What to collect next (ranked by decision value per effort)

1. **`power_source` + method in structured output** (trivial: the guard log
   already knows). Unblocks legitimate cross-machine power comparison.
2. **Promote per-pass arrays into `run_detail_bundles` on every run**, not
   only the seed path: network per-pass Mbit/retransmits/RTT, sustained
   per-pass tok/s, cold per-call TTFT/load. Gives the analyzer real
   within-session variance → honest confidence instead of `0.5` constants.
3. **Phase context snapshot** (cheap sysfs reads at each phase start):
   CPU package temp, GPU temp/freq, load average, AC/battery, governor,
   page-cache hot/cold for the model file. Converts "mystery variance" into
   attributable variance.
4. **Model identity columns** (`model`, `quantization`, `ollama_version`,
   `gpu_offload_layers`) in `runs` or detail bundles.
5. **Concurrent-throughput benchmark** (parking-lot item; this is where
   scheduler tweaks should show, and where the inference story for miners/
   fleet operators actually lives).
6. **One real-path network A/B** (two machines on a real LAN/WAN, or one
   machine against a real internet endpoint, CUBIC vs BBR with and without
   the rest of the stack) to bound how much of the loopback signal
   transfers. A single afternoon of evidence would upgrade or correctly
   demote the headline claim.
7. **netem verification**: assert the qdisc was applied and record it; a
   silently failed `tc` command currently produces a plausible-looking but
   meaningless network comparison.

Items 1–4 and 7 are main-repo build tasks (graduate via the normal rule);
items 5–6 are experiments (`experiments/` plans exist or should be added).

## 4. Goodhart exposure

Because fitness currently weights network 0.40, the cheapest way to "win"
fitness is to keep finding transport-emulation gains. The suite should not
let one synthetic channel dominate selection: hardware-scoped fitness,
the idle-power penalty, and (future) concurrency results are the natural
counterweights. This instantiates the corpus's standing Goodhart concern
(Chapter 10/15) in the one place it is currently concrete.

## 5. Empirical follow-ups (2026-06-12)

The 2026-06-12 sessions on the rebuilt founder rig (Ryzen 7 5700 + Arc A750,
fingerprint `3e6b165ddf112a75`) executed this chapter's program and produced
three results worth recording:

1. **Attribution by complementary ablation works.** v0.9b (GPU frequency pin
   only — pin *verified active at 2000 MHz* via the new phase-context
   telemetry) produced zero cold-start improvement; v0.9c (full v0.8 minus
   the GPU pin) retained the full −51% cold-start win with equivalent
   network and package power. Conclusion: the Arc cold-start win is
   CPU-side (governor/C-state/EPP), and the GPU pin is dead weight. This is
   the project's first clean two-sided attribution and validates the
   telemetry-first methodology: without phase context, v0.9b's null result
   would have been indistinguishable from a failed preset apply.
2. **The power-source warning (§2.2) was confirmed in production.** The rig
   reports RAPL CPU-package only; v0.9b pinned a discrete A750 at 2000 MHz
   idle and the meter read +0.0W. GPU-side power remains invisible until a
   GPU hwmon channel is added.
3. **Metric split implemented** (main repo): the legacy CUBIC-vs-BBR netem
   number is now labeled *transport resilience* (algorithm selection), and a
   new stack-delta benchmark holds BBR constant and toggles only the
   CursiveOS buffer/qdisc tuning — the number attributable to the project's
   own work. netem application is now verified before measurement (item 7
   of §3). Public iperf3 endpoints proved unreliable for real-path testing;
   a LAN endpoint remains the practical path.

4. **Stack-delta result corrects the §2.1 assumption (2026-06-13).** Running
   the new stack-delta benchmark on the founder rig (loopback, ~50ms RTT /
   ~0.5% loss equivalent, **BBR on both sides**, netem verified) gave:
   - BBR + host-default buffers: **395.5 Mbit/s**
   - BBR + CursiveOS buffer/qdisc tuning: **1367.5 Mbit/s**
   - **Stack delta: +245.8%** attributable to our tuning *beyond* the
     algorithm swap.

   Decomposing the legacy ~+800% total (untuned CUBIC ~150 → fully tuned
   ~1367 Mbit/s ≈ 9×): the CUBIC→BBR swap alone is ~2.6× (+160%), and the
   buffer/qdisc tuning on top of BBR is ~3.5× (+246%); 2.6 × 3.5 ≈ 9×. So
   §2.1's original framing ("much of the +500% is attributable to one sysctl,
   bbr") was **wrong on the magnitude split** — on a high-BDP path the buffer
   tuning is the *larger* multiplicative factor. BBR is still necessary (it
   lets the enlarged windows be used without CUBIC's loss-collapse), but the
   project's own tuning does more of the lifting than first assumed.

   **Caveat that still holds:** this is loopback. netem manufactures a
   high bandwidth-delay product, and default Linux buffers genuinely cap the
   window below that BDP — a real and well-understood mechanism. But the
   *magnitude* only transfers to real paths whose BDP actually exceeds
   default buffer sizing (high-bandwidth, high-latency links). On low-BDP
   paths (LAN, modest internet) the stack delta should approach zero. The
   real-path A/B is still required to bound transfer; the mechanism is sound,
   the magnitude is path-dependent.

5. **Cold-start optimization is hardware-scoped (2026-06-13, second machine).**
   The same presets were run on a second machine (i5-11300H laptop, new v2
   fingerprint `42e7c7257af11f46`). Cold-start results diverge sharply by
   hardware:

   | Machine | v0.8 cold-start | v0.9c cold-start |
   | --- | --- | --- |
   | Ryzen 7 5700 + Arc A750 (desktop) | −51% | −51% |
   | i5-11300H (laptop) | ~0% (−0.1, −6.3) | +0.4% |

   Crucially, the phase-context telemetry **rules out the obvious confounds**:
   on the laptop the governor did change `powersave → performance`, the
   machine was on **AC power** (`ac_online: 1`), and the preset applied
   cleanly. The laptop genuinely does not benefit from the cold-start tuning
   that gives the Arc desktop −51%. (The laptop's own May run showed −29%,
   so its small benefit is also unstable across conditions.) This is the
   project's **first empirical instance of hardware-scoped fitness** — the
   exact scenario Chapter 10's evidence model anticipates: a variant that
   helps one hardware class must not be promoted as a global gain. It also
   demonstrates the payoff of the §3 telemetry additions: without governor
   and AC state in the record, "laptop doesn't benefit" would be
   indistinguishable from "tweak didn't stick / ran on battery."

   Implication for v0.9c: on **both** machines v0.9c ≡ v0.8 (laptop: both
   ~0 cold; desktop: both −51%), so dropping the GPU pin costs nothing
   anywhere — v0.9c remains a safe global parent replacement. But the
   cold-start *benefit* it carries is desktop-Arc-specific and must be
   labeled as such, not as a universal CursiveOS result.

## 6. What this changes for decisions

- Marketing/README numbers should keep the "WAN simulation" qualifier
  prominently; "network throughput +5xx%" without scope is overclaiming.
- The v0.9 screen verdict logic (analyzer) is sound, but its power term
  inherits §2.2's comparability limits — fine for same-machine screens,
  not for cross-machine pooling.
- Population confirmation (N rule, CV ≤ 0.15) should be calibrated only on
  variance-bearing data (item 2 above); calibrating on collapsed scalars
  will set thresholds on noise of unknown origin.
