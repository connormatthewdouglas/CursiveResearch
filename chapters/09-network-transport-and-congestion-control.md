## Corpus status (living layer)

**Last reconciled:** 2026-06-24
**Confidence:** **Validated** for real ≤1GbE lossy-path claims (Ch00 §5 item 6); loopback stack-delta magnitude **Disproven** as transferable; high-BDP buffer benefit **Unvalidated**
**Read with:** [Chapter 00](00-benchmark-schema-and-measurement-validity.md) (measurement validity), [Chapter 13](13-linux-kernel-optimization.md) (sysctl presets), [Chapter 01](01-seed-organism-and-sensor-array.md) (network sensor), [Chapter 08](08-population-confirmation-and-fleet-statistics.md) (network CV escalation)

### Authoritative for

- Honest decomposition: CUBIC vs BBR vs buffer/qdisc stack
- Loopback+netem as transport-mechanism lab, not NIC proof
- Linux autotuning and BDP framing for preset design

### Superseded or narrowed

- "+246% from CursiveOS buffer tuning" as a user-facing WAN claim — loopback artifact (**Disproven** for ≤1GbE)
- "212 KB default buffers throttle modern links" — misstates autotuning (Ch01 living layer)

### Open until experiment/hardware

- Real high-BDP path (>1 Gbit and/or high-latency WAN) for buffer-stack retest
- Fleet confirmation of BBR-only win under production pool/P2P workloads

---


## Reinforced research (2026-06-24)

- **BBR under loss:** Cardwell et al., "BBR: Congestion-Based Congestion Control" (ACM Queue 2017); Linux `tcp_bbr` — explains CUBIC collapse vs BBR under 0.5% random loss (§2).
- **Validated decomposition:** Chapter 00 real-path A/B (2026-06-16): CUBIC 43.1 → BBR 851.1 Mbit/s on ≤1GbE; stack delta −0.7% (§5).
- **Loopback BDP artifact:** iperf3 loopback effective BDP can reach tens of MB — stack tuning magnitudes are mechanism-only, not NIC-transferable (§3).
- **ESnet tuning:** ESnet "Host Tuning" guidance — label tests `real-path` vs `loopback-emulation`; public iperf3 endpoints unreliable per Ch00 §3 item 7.
- **Fleet escalation:** Network CV 0.192 > 0.15 threshold — per-channel confirmation per Ch08 §4.

# Network Transport and Congestion Control

Status: First research-synthesis pass (2026-06-24), integrated with **Validated**
Chapter 00 findings (2026-06-12 through 2026-06-16). Grounds CursiveOS network
presets in TCP congestion control, bandwidth-delay product (BDP), and Linux
buffer autotuning — with explicit separation of algorithm swap vs stack tuning.
Use it for: preset design, benchmark interpretation, and public messaging scope.

## Why this chapter exists

CursiveOS's highest-weighted fitness channel (network, 0.40 in current schema)
sits on TCP behavior under loss. Chapter 00 proved the deployed benchmark mixes
three distinct mechanisms — congestion-control algorithm, buffer sizing, qdisc
— and that **loopback and real-path answers diverge**. The corpus needed a
transport chapter that states what Linux actually does, what BBR changes, and
what the project's measurements do and do not prove.

## 1. TCP stack layers relevant to CursiveOS

| Layer | Knobs CursiveOS touches | Measured by genesis sensor? |
| --- | --- | --- |
| Congestion control | `net.ipv4.tcp_congestion_control` (CUBIC vs BBR) | yes (legacy A/B) |
| Buffer limits | `net.core.rmem_max`, `wmem_max`, `tcp_rmem`/`tcp_wmem` | yes (stack-delta) |
| Autotuning | `tcp_moderate_rcvbuf`, per-socket dynamic buffers | implicit, often unlogged |
| Qdisc / fq | `fq`, `fq_codel`, pacing | partial in presets |
| Physical NIC | offloads, driver rings, IRQ coalescing | **no** in loopback harness |

| Claim | Status |
| --- | --- |
| Loopback iperf3 + netem measures kernel transport, not NIC | **Validated** (Ch00 §2.1) |
| netem on real egress exercises NIC + stack | **Validated** (2026-06-16 real-path) |
| Single scalar "network delta" blends multiple mechanisms | **Supported** |

## 2. Bandwidth-delay product (BDP)

BDP ≈ bottleneck_bandwidth × round_trip_time. The pipe needs enough in-flight
data to stay full. Linux **receive buffer autotuning** (`tcp_moderate_rcvbuf`,
since 2.6.x era) grows per-connection windows toward observed path capacity
within `rmem_max` ceilings.

Example at 1 Gbit/s, 50 ms RTT:

```text
BDP ≈ 1e9 bit/s × 0.05 s / 8 ≈ 6.25 MB
```

| Claim | Status |
| --- | --- |
| Default autotuning covers ~6 MB BDP on ≤1GbE / 50ms | **Validated** (Ch00 real-path: stack tuning ≈ 0%) |
| Loopback effective BDP can be tens of MB (memory-limited "link") | **Supported** (Ch00 §5 item 6 mechanism) |
| Larger static buffers help only when path BDP exceeds autotuned window | **Supported** (theory + loopback vs real split) |

**CursiveOS implication:** buffer/qdisc presets are **high-BDP insurance**, not
the default win on ordinary mining-rig LAN/WAN paths. Public copy should lead
with BBR under loss, not buffer ceilings.

## 3. BBR: model-based congestion control

BBR (Bottleneck Bandwidth and Round-trip propagation RTT), from Cardwell et al.
(Google, 2016), paces sending from estimated max bandwidth and min RTT rather
than treating loss as primary congestion signal.

| Behavior | CUBIC (loss-based) | BBR (model-based) |
| --- | --- | --- |
| Random loss | shrinks window | often ignores as non-congestive |
| Bufferbloat RTT | can overfill queues | min RTT + pacing discipline |
| Fairness with other flows | Reno/CUBIC friendly | documented caveats; use fq pacing |
| Deployment | Linux default varies by distro | `modprobe tcp_bbr`; sysctl switch |

Primary references:

- Cardwell et al., *BBR Congestion Control*, ACM Queue / IETF ICCRG drafts
  ([IETF draft archive](https://www.ietf.org/archive/id/draft-cardwell-iccrg-bbr-congestion-control-01.html))
- Linux `tcp(7)` — congestion-control names and socket options
  ([man7.org/linux/man-pages/man7/tcp.7.html](https://man7.org/linux/man-pages/man7/tcp.7.html))

| Claim | Status |
| --- | --- |
| BBR >> CUBIC under 0.5% random loss on tested paths | **Validated** (loopback + real 1GbE) |
| BBR win is largely a one-line sysctl | **Supported** |
| BBR replaces need for all CursiveOS buffer tuning on ≤1GbE | **Validated** for tested path |

## 4. Linux autotuning vs static sysctl ceilings

Operators often conflate:

- `net.core.rmem_max` — **ceiling** for receive buffers
- `net.ipv4.tcp_rmem` — min / default / **max** triple for TCP
- autotuned `SO_RCVBUF` — per-connection actual buffer during transfer

ESnet host-tuning guidance (2025–2026 revisions) emphasizes measuring the path,
then setting ceilings **above** expected BDP for high-throughput science networks
— not replacing autotuning with tiny static defaults.

| Source | Guidance |
| --- | --- |
| [ESnet Fasterdata — Linux host tuning](https://fasterdata.es.net/host-tuning/linux/) | BDP math, `rmem_max`/`wmem_max`, verify with iperf3 |
| Linux `tcp(7)` | `TCP_WINDOW_CLAMP`, autotuning behavior |
| Chapter 00 real-path A/B | autotuning already sufficient at ~6 MB BDP |

| Claim | Status |
| --- | --- |
| Import-era "212 KB default" misstates modern autotuning story | **Disproven** (Ch01/16 reconciliation) |
| Raising `rmem_max` helps high-BDP paths when autotune cap binds | **Supported** (theory); **Unvalidated** on CursiveOS fleet high-BDP |
| CursiveOS buffer stack adds ~0% on ≤1GbE 50ms lossy path | **Validated** |

## 5. Validated measurement decomposition (Chapter 00)

### 5.1 Loopback + netem (mechanism lab)

| Configuration | Throughput (founder rig, indicative) | Interpretation |
| --- | --- | --- |
| CUBIC + defaults | ~150 Mbit/s | loss collapse |
| BBR + defaults | ~395 Mbit/s | algorithm gain |
| BBR + CursiveOS stack | ~1367 Mbit/s | **large stack delta** |

| Claim | Status |
| --- | --- |
| Stack delta +246% on loopback with BBR held constant | **Validated** (loopback only) |
| Loopback magnitude transfers to ordinary ≤1GbE | **Disproven** |

### 5.2 Real path: Stardust → second machine, 1GbE, netem 50ms + 0.5% loss

| Configuration | Throughput | vs prior row |
| --- | --- | --- |
| CUBIC + host defaults | 43.1 Mbit/s | baseline |
| BBR + host defaults | 851.1 Mbit/s | **+1875%** algorithm |
| BBR + CursiveOS stack | 845.0 Mbit/s | **−0.7%** stack |

| Claim | Status |
| --- | --- |
| Entire real-world win is CUBIC→BBR under loss | **Validated** (2026-06-16) |
| Buffer/qdisc stack irrelevant on this path | **Validated** |
| Honest public claim = "enable BBR under lossy links" | **Supported** |

### 5.3 Metric split (implemented)

Chapter 00 recommends two labeled metrics:

| Label | What varies | Use |
| --- | --- | --- |
| Transport resilience | CUBIC vs BBR | algorithm selection evidence |
| Stack delta | BBR fixed; buffer/qdisc only | attributes project-specific tuning |

Both require **netem verification** before trust (Ch00 §3 item 7).

## 6. Noise, CV, and population confirmation

Six identical v0.9 runs on one host: network CV **0.192** (Ch00 §5 item 7),
above Chapter 01's 0.15 escalation threshold. Magnitude ranged 602–970%.

| Claim | Status |
| --- | --- |
| Network presence under loss is repeatable; magnitude is not precise | **Validated** |
| Fleet quotes must not use point estimates without variance | **Supported** |
| Per-channel confirmation escalation applies to network | **Supported** (Ch08) |

## 7. Preset and benchmark design implications

| Design choice | Recommendation | Status |
| --- | --- | --- |
| Default preset includes BBR on loss-prone workloads | yes | **Supported** |
| Market buffer tuning as universal WAN speedup | no on ≤1GbE | **Validated** |
| Keep stack-delta loopback test | yes, as **mechanism demo** only | **Supported** |
| Add real-path or high-BDP endpoint tests | required before buffer claims | **Unvalidated** |
| Record congestion algo + autotune snapshot in `runs` | schema gap | **Unvalidated** |

Suggested structured fields (extends Ch00 §3):

- `tcp_cc` (cubic/bbr/…)
- `rmem_max`, `wmem_max`, sampled `tcp_rmem`
- `autotune_observed_bytes` if obtainable from `ss -ti`
- `netem_verified`, `path_class` (loopback / lan / wan)

## 8. Workloads: mining, P2P, inference API

Genesis sensor uses iperf3 — a bulk throughput probe. Real fleet workloads may
be TLS-heavy, small-message bursty, or pool-stratum shaped.

| Workload | Transport sensitivity | Measured? |
| --- | --- | --- |
| Stratum / pool mining | loss + RTT on small messages | **Unvalidated** |
| P2P blockchain sync | bulk + parallel flows | **Unvalidated** |
| Local Ollama API | often loopback or LAN | partial (Ch05) |
| WAN model download | bulk TCP | **Unvalidated** on real WAN |

**CursiveOS implication:** BBR-under-loss evidence transfers to **bulk TCP over
lossy paths**. Stratum and API latency need separate sensors before fitness
weighting generalizes.

## 9. CursiveOS implications

1. **Fitness language:** credit BBR for validated real-path loss behavior; do not
   credit buffer stack magnitude on ordinary hardware.
2. **Goodhart:** network channel dominates fitness — pair with hardware-scoped
   rules and idle-power / cold-start counterweights (Ch00 §4).
3. **Marketing:** always qualify WAN simulation vs real NIC; cite algorithm where
   validated.
4. **Future presets:** consider `fq` + pacing with BBR; document interaction per
   ESnet and distro defaults.
5. **Experiments:** high-BDP path (10G+ or satellite RTT) to retest stack delta.

## 10. Open research gaps

1. High-BDP real-path A/B for buffer/qdisc stack (not loopback).
2. Stratum/pool-shaped microbenchmark sensor.
3. Concurrent multi-flow iperf or rrul — competition fairness under BBR.
4. Cross-distro default CC at install — detect and log.
5. Fleet-population confirmation of BBR-only benefit on ≥3 independent paths.
6. Public iperf3 endpoints proved unreliable (Ch00); maintain LAN reference pair.

## 11. Citations

| Source | Contribution |
| --- | --- |
| Cardwell, Cheng, et al. — BBR | model-based CC under loss |
| Linux `tcp(7)` | socket buffers, CC names |
| [ESnet Fasterdata Linux tuning](https://fasterdata.es.net/host-tuning/linux/) | BDP, sysctl practice |
| Chapter 00 §2.1, §5 items 4–7 | loopback vs real decomposition |
| RFC 5681 (TCP congestion control) | baseline loss-based semantics |
| Gettys, Nichols — bufferbloat | RTT inflation, fq_codel context |

## Research questions answered

| Question | Answer |
| --- | --- |
| What causes the big network delta? | Primarily CUBIC→BBR under loss (**Validated** on tested paths) |
| Do CursiveOS buffers matter on a 1GbE rig? | Not on validated 50ms+0.5% loss path |
| Is loopback enough? | Mechanism yes; magnitude no |
| What should ship in presets? | BBR for loss-prone classes; buffer stack as optional high-BDP profile |