<!--
Generated from a preserved DOCX source; wording is retained from the source.
Source: sources/original-docx/2. Linux kernel optimizations.docx
Git blob SHA: e54cb50b4cfaa93aedbf07f50f4a5dbd7bf8c51e
-->

# Linux Kernel Optimization

## Linux kernel optimizations that actually move the needle for GPU inference

**The most impactful 2025–2026 kernel changes for GPU inference on AMD Ryzen and Intel Arc come from three unexpected places: the crypto subsystem, the new extensible scheduler framework, and memory management plumbing.** Eric Biggers' sustained AES rewrite campaign [Phoronix](https://www.phoronix.com/news/3.3x-AES-CTR-AMD-Zen-5-Patches) delivers up to **3.3× faster encrypted model loading** on AMD Zen 5. [Phoronix](https://www.phoronix.com/forums/forum/phoronix/latest-phoronix-articles/1524195-new-linux-patches-yield-up-to-3-3x-faster-aes-ctr-performance-on-amd-zen-5-cpus) The sched_ext framework, merged in kernel 6.12, enables custom BPF schedulers that cut tail latency by 75%. And a quiet series of ZRAM and GPU shared virtual memory patches fundamentally change how inference workloads manage memory pressure. Together, these changes span kernels 6.10 through 7.0 and represent a step-function improvement for anyone running local LLM inference on consumer AMD or Intel hardware.

---

### 1. AES-CTR rewrite delivers 3.3× throughput on AMD Zen 5

**Kernel 6.15 (May 2025)** — Eric Biggers (Google) rewrote AES-CTR and AES-XCTR [Phoronix](https://www.phoronix.com/news/3.3x-AES-CTR-AMD-Zen-5-Patches) with new VAES-optimized code paths [Phoronix](https://www.phoronix.com/news/Linux-6.15-Crypto) in `arch/x86/crypto/aes-ctr-avx-x86_64.S`. This is the single largest crypto performance jump in recent kernel history and directly impacts inference pipelines that load models from encrypted storage (fscrypt uses AES-256-XTS for file contents, AES-256-CTS-CBC for filenames). [Linux Kernel](https://www.kernel.org/doc/html/next/filesystems/fscrypt.html)

The before-after numbers on long messages are striking. **AMD Zen 5** (Ryzen 9000, EPYC 9005) saw **+230% throughput — a 3.3× speedup** over the prior AES-CTR implementation. [Phoronix](https://www.phoronix.com/forums/forum/hardware/processors-memory/1524195-new-linux-patches-yield-up-to-3-3x-faster-aes-ctr-performance-on-amd-zen-5-cpus) [Phoronix](https://www.phoronix.com/forums/forum/phoronix/latest-phoronix-articles/1524195-new-linux-patches-yield-up-to-3-3x-faster-aes-ctr-performance-on-amd-zen-5-cpus) Other VAES-capable CPUs (Zen 3+, Intel Ice Lake+) also showed significant gains, though Zen 5's wider VAES pipelines extracted the most benefit. [Phoronix](https://www.phoronix.com/news/3.3x-AES-CTR-AMD-Zen-5-Patches) For a practical scenario — loading a 70B-parameter GGUF model from an fscrypt-encrypted ext4 filesystem on an NVMe drive — the decryption bottleneck effectively vanishes. The kernel now saturates NVMe bandwidth before hitting crypto throughput limits on modern AMD hardware.

This built on the **kernel 6.10** AES-XTS rewrite (same author), which delivered **+155% on AMD Zen 4** and **+151% on Intel Sapphire Rapids** for 4096-byte messages [Neowin](https://www.neowin.net/news/linux-vs-windows-aes-performance-to-be-intriguing-as-google-boosts-amd-and-intel/) — the primary cipher mode for dm-crypt/LUKS full-disk encryption. The cumulative effect across 6.10–6.16 means that encrypted model loading on kernel 7.0 is roughly **2–3× faster** than on kernel 6.9 for AMD Ryzen systems with VAES support.

| Kernel | Algorithm | Best CPU | Improvement |

|--------|-----------|----------|-------------|

| 6.10 | AES-XTS | AMD Zen 4 | **+155%** (10,868 MB/s) |

| 6.10 | AES-XTS | Intel Sapphire Rapids | **+151%** (12,176 MB/s) |

| 6.11 | AES-GCM | Modern Intel/AMD | **+162%** |

| 6.15 | AES-CTR | AMD Zen 5 | **+230%** (3.3×) |

| 6.19 | AES-GCM | AMD Zen 3 | **+74%** |

---

### 2. sched_ext enables purpose-built inference schedulers with 75% latency cuts

**Kernel 6.12 (November 2024)** marked a watershed moment for Linux scheduling: **sched_ext** merged into mainline, allowing BPF programs to implement complete scheduling policies at runtime. [WebProNews +3](https://www.webpronews.com/linux-6-19-upgrades-sched_ext-with-ebpf-fault-recovery-and-15-latency-boost/) For inference workloads, this is transformative — instead of relying on EEVDF's general-purpose heuristics, operators can deploy custom schedulers tuned specifically for GPU dispatch patterns.

The benchmark data from community sched_ext schedulers is compelling. **scx_rustland** (Andrea Righi) achieved **+77% requests/sec** over EEVDF on nginx and **+26% transactions/sec** on PostgreSQL. Most relevant for inference: **schbench 99.9th-percentile latency dropped from 9ms to 3.4ms** — a **75.5% reduction** in tail latency. An ML-based sched_ext scheduler presented at Open Source Summit NA 2025 demonstrated **10% kernel compilation speedup** with **77% fewer task migrations**, [LWN.net](https://lwn.net/Articles/1027096/) and the academic SchedCP project (LLM-driven scheduler policy) showed **2.11× P99 latency reduction** versus EEVDF baseline on schbench. [Linux Journal](https://www.linuxjournal.com/content/self-tuning-linux-kernels-how-llm-driven-agents-are-reinventing-scheduler-policies)

Kernel 6.12 also delivered three other inference-relevant scheduler changes. [Linux Kernel](https://docs.kernel.org/scheduler/sched-eevdf.html) **PREEMPT_RT finally merged** into mainline after 20 years, enabling hard real-time guarantees for latency-sensitive inference dispatch. [Linux Kernel Newbies](https://kernelnewbies.org/Linux_6.12) **Custom time slices via `sched_setattr()`** allow inference threads to request specific scheduling quanta (100µs–100ms). [heise online](https://www.heise.de/en/news/Linux-6-12-Scheduler-now-expandable-and-EEVDF-conversion-complete-9949941.html) And **SCHED_DEADLINE servers** replaced the older RT throttling mechanism, fixing starvation of normal tasks when real-time inference dispatch threads consume CPU. [Linux Kernel Newbies](https://kernelnewbies.org/Linux_6.12) [Linux Kernel Newbies](https://kernelnewbies.org/Linux_6.8)

The sched_ext roadmap for 2026 explicitly targets **GPU awareness** and **energy-aware scheduling abstractions**, [Phoronix](https://www.phoronix.com/news/sched-ext-future-plans-2026) which would allow BPF schedulers to coordinate CPU task placement with GPU workload submission — a direct fit for heterogeneous inference on AMD Ryzen APUs where CPU and GPU share a die.

---

### 3. ZRAM writeback batching cuts eviction time by 4× on memory-constrained setups

**Kernel 7.0 (February 2026)** brought two critical ZRAM improvements from Sergey Senozhatsky (Google) that transform memory management for inference workloads running on systems without enough RAM to hold both the model and the OS comfortably.

**Writeback bio batching** replaced single-page synchronous I/O with pooled, batched submissions to the backing device. A new sysfs attribute `writeback_batch_size` (default: 32 pages) controls the parallelism. [LWN.net](https://lwn.net/Articles/1047280/) Benchmark data from an earlier related patch by Pankaj Raghav showed **4GB writeback to NVMe completing in 15 seconds versus 68 seconds** — more than a **4× improvement**. [Patchew](https://patchew.org/linux/20230911133430.1824564-1-kernel@pankajraghav.com/) For inference, this means that when ZRAM evicts cold pages (OS caches, inactive application memory) to make room for model weights, the eviction completes dramatically faster, reducing stall time.

The companion patch, **compressed writeback**, allows ZRAM to write compressed data directly to the backing device without decompressing first. [Phoronix](https://www.phoronix.com/news/Linux-7.0-MM) Previously, every writeback page was decompressed → written → discarded, wasting CPU cycles and I/O bandwidth. [Linux Kernel](https://docs.kernel.org/admin-guide/blockdev/zram.html) The new path (enabled via `echo yes > /sys/block/zramX/compressed_writeback`) saves both CPU power and backing device bandwidth — particularly valuable on laptops and low-power inference rigs.

These build on the **kernel 6.12** custom compression backends overhaul, which introduced per-algorithm tuning via a new `algorithm_params` sysfs attribute. Pre-trained dictionaries for zstd, lz4, and lz4hc delivered **14.6% better compression** (zstd+dictionary) and **17.7% better** (lz4hc level 5+dictionary) on representative workloads. [LWN.net](https://lwn.net/Articles/981055/) A pending March 2026 patch from Gao Xu (HONOR) promises **50%+ performance improvement** for LZ4 dictionary compression by eliminating repeated `LZ4_loadDict()` overhead through a template stream mechanism. [Phoronix](https://www.phoronix.com/news/Linux-ZRAM-50p-Compress-Boost)

---

### 4. GPU shared virtual memory unifies CPU-GPU address spaces on Intel and AMD

The **drm_gpusvm framework** (Matthew Brost, Intel) represents the most significant HMM advancement for inference. Merged in kernel 6.15 for Intel Xe, [Phoronix](https://www.phoronix.com/news/Intel-Xe-SVM-For-Linux-6.15) with AMD prototyping adoption in March 2026, this DRM-level infrastructure provides unified shared virtual memory atop Linux HMM — meaning **CPU and GPU share identical virtual address pointers** with transparent page migration. [Phoronix](https://www.phoronix.com/news/AMDGPU-Experiment-DRM-GPUSVM)

For Intel Arc hardware, the practical impact is substantial. When switching from the i915 driver to Xe on Intel Arc A-series, Phoronix benchmarks showed **"dramatic" gains for OpenCL/GPU compute workloads**, [Phoronix](https://www.phoronix.com/review/intel-i915-xe-linux-2025) with secondary analysis suggesting **15–50% compute improvements**. [WebProNews](https://www.webpronews.com/intel-xe-driver-surpasses-i915-on-arc-alchemist-gpus-in-linux-6-19-tests/) Intel's Ultra Low Latency Scheduling (ULLS), enabled by default in Compute Runtime 25.13+ for Lunar Lake and extended to Battlemage, bypasses driver submission overhead entirely — delivering "much better kernel latency" according to Phoronix's November 2025 coverage. [Phoronix](https://www.phoronix.com/news/Intel-ULLS-Direct-Submit-Lunar) The **GPU SVM** eliminates explicit memory copy calls between CPU and GPU address spaces, which is the primary bottleneck when inference frameworks stage input tensors. [Phoronix](https://www.phoronix.com/news/Intel-Xe-SVM-For-Linux-6.15)

On the AMD side, the existing AMDKFD SVM (nearly 5000 lines of kernel code) works but uses driver-specific HMM integration. AMD engineers posted a **proof-of-concept SVM implementation using drm_gpusvm** on March 18, 2026, signaling convergence toward a unified framework. Meanwhile, **kernel 6.14 mainlined the AMDXDNA driver** for AMD Ryzen AI NPUs [It's FOSS +3](https://news.itsfoss.com/linux-kernel-6-14/) (10–55 TOPS depending on generation), giving AMD Ryzen AI 300 "Strix Point" laptops a dedicated inference accelerator with spatial/temporal scheduling of 2D compute tile arrays.

For **multi-device SVM** (merged in kernel 6.19/7.0 for Intel Xe), seamless memory sharing across up to 8 GPUs targets AI/LLM workloads. [WebProNews](https://www.webpronews.com/intel-boosts-xe-driver-with-multi-gpu-svm-in-linux-kernel-7-0-for-ai/) Intel's "Project Battlematrix" initiative packages this with vLLM container support and SR-IOV preparations for the Arc Pro B50 (16GB, **170 pTOPS**) and B60 (24GB, **197 pTOPS**). [Phoronix](https://www.phoronix.com/review/intel-arc-pro-b-series)

---

### 5. RADV Vulkan patches boost llama.cpp prompt processing by 13–20%

A targeted **Mesa 25.3** optimization by Valve developer Rhys Perry (3 patches to RADV, Mesa MR #37791) delivered measurable LLM inference improvements on AMD GPUs. The patches optimized compute unit mode when Local Data Share (LDS) memory is utilized — a pattern common in attention kernels.

Benchmarked on **AMD Strix Halo** (Ryzen AI Max+ 395 with Radeon 8060S integrated graphics), the before-after numbers for llama.cpp Vulkan backend inference tell a clear story:

| Model / Context | Old RADV | New RADV (Mesa 25.3) | Improvement |

|----------------|----------|---------------------|-------------|

| Llama 2 7B Q4_0, PP512 | 3,586 tok/s | 4,046 tok/s | **+13%** |

| gpt-oss-120b MXFP4, PP512 | 520.7 tok/s | 623.9 tok/s | **+20%** |

| gpt-oss-120b MXFP4, PP4096 | 437.2 tok/s | 526.3 tok/s | **+20%** |

| gpt-oss-120b MXFP4, PP16384 | 298.2 tok/s | 354.1 tok/s | **+19%** |

While this is a userspace Mesa change rather than a kernel patch, it rides on kernel-level enablement. The Xe driver on Intel Arc B580 showed comparable evolution: Phoronix's year-long compute benchmark comparison (December 2024 → November 2025) on the B580 documented **"nice GPU compute performance gains"** [Phoronix](https://www.phoronix.com/review/intel-b580-opengl-vulkan-eoy2025) [Phoronix](https://www.phoronix.com/review/intel-b580-compute-one-year/3) including up to **50% improvement** in SPECViewPerf workstation benchmarks and **20%+ Vulkan frame rate gains**. [WebProNews](https://www.webpronews.com/intel-arc-b580-gpu-hits-50-performance-boost-via-linux-optimizations-in-2025/)

---

### 6. TLB shootdown reduction and cache-aware scheduling target the memory wall

Two proposed kernel patches tackle the memory subsystem overhead that dominates GPU inference: **MIGRC** (Migration Read Copy) by Byungchul Park, and **cache-aware scheduling** led by Intel engineers.

MIGRC defers TLB flushes during page migration until source folios are actually reused, specifically for non-writable PTE entries. [LWN.net](https://lwn.net/Articles/970197/) On the XSBench workload, TLB shootdown interrupts **dropped over 90%** [LWN.net](https://lwn.net/Articles/970197/) (from ~1.3M to ~100K per CPU), with `tlb_flush.dtlb_thread` falling from 234M to 138M and runtime improving by **~5%**. [LWN.net](https://lwn.net/Articles/941875/) This directly benefits HMM-mediated page migration between CPU and GPU memory tiers during inference. A related commit by Huang Ying (`4d4b6d66db`) already avoids most shootdowns for hinting fault migrations in mainline. [LWN.net](https://lwn.net/Articles/970197/)

Cache-aware scheduling, tested on AMD EPYC Genoa and Intel Xeon 6 Granite Rapids, aggregates tasks sharing data to the same LLC domain. The headline result: **up to 44% time savings** on Hackbench workloads. [Phoronix](https://www.phoronix.com/news/Cache-Aware-Scheduling-Go) The v3 patches were posted in January 2026 and are targeting mainline in 2026. [Phoronix](https://www.phoronix.com/news/Cache-Aware-Scheduling-Linux-v3) For inference, this reduces cache bouncing when CPU-side preprocessing (tokenization, KV-cache management) shares data with GPU dispatch threads — a pattern common in vLLM and SGLang serving architectures.

---

### 7. Critical sysfs tunables for inference cold-start and jitter

Several new and existing sysfs parameters deserve attention for inference optimization. The most impactful, organized by subsystem:

- **`/sys/class/drm/cardX/device/slpc_power_profile`** (Intel Xe, kernel 6.15+): Controls the SLPC firmware power controller on Intel Arc GPUs. Setting `base` (default) keeps GPU frequency responsive for low-latency inference; `power_saving` disables waitboosting and uses conservative ramp-up [Blogger](https://portallinuxferramentas.blogspot.com/2025/09/intel-xe-driver-in-linux-618-introduces.html?m=1) — bad for cold-start but useful for batch processing

- **`amdgpu.runpm=0`** (AMD module parameter): Disables runtime power management for discrete AMD GPUs, **eliminating cold-start wake latency** entirely. Default `-1` (auto) [Linux Kernel](https://docs.kernel.org/gpu/amdgpu/module-parameters.html) can add hundreds of milliseconds to first inference call after idle [Linux Kernel](https://www.kernel.org/doc/html/v4.20/gpu/amdgpu.html)

- **`/sys/class/drm/cardX/device/pp_power_profile_mode`** (AMD): Setting to `COMPUTE` (mode 5) optimizes AMD GPU clock/power behavior for sustained compute throughput rather than gaming burst patterns [Gentoo Wiki](https://wiki.gentoo.org/wiki/AMDGPU)

- **`/sys/block/zramX/algorithm_params`** (kernel 6.12+): Enables per-algorithm tuning including compression level and pre-trained dictionaries [Patchew](https://patchew.org/linux/20240902105656.1383858-1-senozhatsky@chromium.org/20240902105656.1383858-24-senozhatsky@chromium.org/) — `echo "algo=zstd level=8" > algorithm_params` [Lwn](https://static.lwn.net/kerneldoc/admin-guide/blockdev/zram.html)

- **`/sys/block/zramX/writeback_batch_size`** (kernel 7.0): Controls writeback parallelism; default 32 pages, increase for NVMe-backed setups

- **`amdgpu.ttm_pages_limit`**: Overrides BIOS VRAM allocation on AMD APUs — community reports show **96GB → 120GB VRAM** per node on Strix Halo, enabling larger models to fit entirely in GPU-accessible memory

- **`rt_group_sched=0`** (kernel 6.16 boot parameter): Disables RT group scheduling at boot without recompilation, [Phoronix](https://www.phoronix.com/news/Linux-6.16-Scheduler) removing a friction point for deploying SCHED_FIFO inference dispatch threads

---

### 8. Whole-stack benchmarks quantify the cumulative kernel advantage

Phoronix's longitudinal benchmarks across 2025 provide the clearest picture of cumulative improvement. A **37% geometric mean improvement** was measured from Linux 5.15 LTS to 6.17 on dual AMD EPYC 7773X across diverse workloads (August 2025). [Phoronix](https://www.phoronix.com/review/linux-515-617-performance) More granularly, an AMD Ryzen AI 5 340 laptop showed **~8% geometric mean improvement** simply from upgrading Ubuntu 25.04/kernel 6.14 to Ubuntu 25.10/kernel 6.18 over six months. [Phoronix](https://www.phoronix.com/review/amd-krackan-point-2025) Intel Lunar Lake saw **~6% geo mean improvement** during 2025. [VideoCardz](https://videocardz.com/newz/two-years-after-launch-intel-meteor-lake-offers-93-of-original-performance-on-linux-tests-show)

For inference specifically, the carteakey.dev tuning guide documented that **running on Linux versus Windows yields +20% tokens per second** for local LLM inference, and that enabling XMP memory profiles (DDR5-6000 vs. 2000 MT/s default) **tripled token generation** from ~10 to ~30 tok/s on an i5-12600K. [Carteakey](https://carteakey.dev/blog/optimizing-gpt-oss-120b-local-inference/) The AMD developer blog demonstrated a 4-node Ryzen AI Max+ 395 cluster running the **1 trillion parameter Kimi K2.5** model via llama.cpp RPC [AMD](https://www.amd.com/en/developer/resources/technical-articles/2026/how-to-run-a-one-trillion-parameter-llm-locally-an-amd.html) — made possible by the `amdgpu.ttm_pages_limit` kernel parameter expanding each node from 96GB to 120GB VRAM.

The **Fair DRM Scheduler** (Tvrtko Ursulin, Igalia), currently at v9 patches targeting mainline in 2026, promises CFS-inspired virtual GPU time-based scheduling that prevents compute-heavy inference from starving interactive workloads. [Phoronix](https://www.phoronix.com/news/Fair-DRM-Scheduler-Post-RFC) And kernel 6.17's fix for **50-minute hibernation times** on servers with 8× MI300X GPUs (1.5TB total VRAM) addressed a practical deployment pain point for large-scale AMD inference infrastructure.

---

### Conclusion

The most actionable kernel changes for GPU inference fall into two tiers. **Tier 1** (upgrade your kernel immediately): the AES crypto rewrites in kernels 6.10–6.19 deliver 1.5–3.3× encrypted storage throughput with zero configuration; sched_ext in 6.12+ enables purpose-built inference schedulers; [heise online](https://www.heise.de/en/news/Linux-6-12-Scheduler-now-expandable-and-EEVDF-conversion-complete-9949941.html) [LWN.net](https://lwn.net/Articles/1027096/) and ZRAM improvements in 6.12/7.0 dramatically reduce memory pressure on RAM-constrained systems. **Tier 2** (requires configuration): Intel Xe SVM in 6.15+ with ULLS in the compute runtime transforms Arc GPU compute latency; AMD's `amdgpu.runpm=0` eliminates cold-start wake penalties; and the new `pp_power_profile_mode=COMPUTE` / `slpc_power_profile=base` sysfs controls optimize GPU power behavior for sustained inference rather than gaming bursts.

The trajectory is clear: kernels 6.14–7.0 represent the sweet spot for inference on AMD Ryzen and Intel Arc, with the convergence of GPU shared virtual memory (drm_gpusvm), extensible scheduling (sched_ext), and mature VAES crypto acceleration creating a fundamentally better substrate for local AI workloads than was available even 12 months ago.
