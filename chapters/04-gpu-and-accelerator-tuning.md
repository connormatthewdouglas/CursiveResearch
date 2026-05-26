<!--
Generated from a preserved DOCX source; wording is retained from the source.
Source: sources/original-docx/3. GPU Kernel Tweaks for Mining_AI.docx
Git blob SHA: 726912342c92bec12771ffcf36db5ecf8231033d
-->

# GPU and Accelerator Tuning

## Comprehensive Systems Optimization for Heterogeneous Workloads: Kernel Tuning, Power Scaling, and GPU Multiplexing in 2026

The operational landscape of 2026 is characterized by a profound shift toward localized high-performance computing, driven by the dual demands of decentralized cryptographic validation and local large language model (LLM) inference. The Linux kernel, serving as the primary orchestration layer for these workloads, has undergone significant architectural evolution to accommodate the distinct resource profiles required by these tasks. While cryptographic mining emphasizes sustained, high-throughput compute cycles and memory bandwidth, LLM inference is characterized by extreme sensitivity to tail latency, requiring rapid "Time to First Token" (TTFT) and consistent inter-token latency (ITL). To optimize a single system for these often-conflicting objectives, a nuanced application of reversible kernel tweaks is necessary. This report evaluates the state of kernel-level performance tuning, focusing on the hardware-specific optimizations for AMD Polaris and Intel Arc architectures, the implementation of Single Root I/O Virtualization (SR-IOV) for GPU multiplexing, and the critical adjustments to the memory subsystem through hugepage management and Non-Uniform Memory Access (NUMA) balancing.

### Architectural Evolution of the Linux Kernel in 2026

By 2026, the Linux kernel has transitioned from a static resource manager into an extensible, AI-augmented infrastructure. This transformation is rooted in the maturation of eBPF (extended Berkeley Packet Filter), which has enabled the introduction of the sched_ext framework. This framework allows for the dynamic loading of CPU schedulers from userspace, effectively ending the era of the "one-size-fits-all" scheduling policy represented by the legacy Completely Fair Scheduler (CFS) and its successor, the Earliest Eligible Virtual Deadline First (EEVDF) scheduler. For practitioners in 2026, kernel tuning is no longer restricted to static sysctl modifications; it involves the deployment of specialized scheduling policies that can distinguish between background throughput-oriented tasks, such as mining, and foreground interactive tasks, such as LLM inference.

The integration of AI into the kernel control plane is another hallmark of the 2026 ecosystem. Subsystems now utilize machine-learning-informed advice to manage power states and resource distribution, ensuring that performance is maintained without compromising system determinism. Furthermore, the emergence of "Agentic OS" frameworks, such as SchedCP, allows Large Language Model agents to autonomously analyze workloads and synthesize eBPF programs to optimize the system in real-time. These advancements provide the foundation for the specific hardware and memory tweaks detailed in the following sections.

### Power Scaling and Undervolting Techniques for Heterogeneous GPU Arrays

The economic viability of high-performance computing in 2026 is inextricably linked to power efficiency. For the AMD RX 580—a Polaris-architecture "tank" that remains popular in 2026 for its 8GB VRAM and affordability—and the more modern Intel Arc series, the default power profiles are often suboptimal for the specialized demands of mining and inference. Undervolting remains the primary mechanism for reducing thermal throttling and extending hardware longevity, particularly for used mining cards that may be showing signs of silicon degradation.

#### AMD Polaris Optimization: The RX 580 Refined

The RX 580 architecture relies on a discrete set of power states (P-states) that govern the relationship between clock frequency and voltage. In the 2026 kernel environment, the amdgpu driver provides granular control via the sysfs interface, provided the operator enables the correct feature mask at boot. The recommended parameter for 2026 is amdgpu.ppfeaturemask=0xfffd7fff. While the more aggressive 0xffffffff mask is available, it has been documented to cause visual artifacts and instability on certain 500-series cards.

| P-State | Frequency (MHz) | Default Voltage (mV) | Optimized Voltage (mV) | Logic and Stability Notes |
| --- | --- | --- | --- | --- |
| State 0 | 300 | 750 | 750 | Minimum idle floor; usually not modified. |
| State 1 | 600 | 769 | 769 | Low-load transition state. |
| State 2 | 900 | 906 | 860 | Balanced state for light inference background. |
| State 3 | 1145 | 1125 | 880 | Significant undervolt target for efficient mining. |
| State 6 | 1300 | 1150 | 1000 | High-performance threshold for LLM prefill. |
| State 7 | 1366 | 1150 | 1060 | Peak compute state; maximum undervolt ceiling. |

To apply these tweaks reversibly, the operator must first set the power level to manual. The following commands illustrate a typical 2026 optimization workflow for an RX 580 identified as card0. If a system utilizes an integrated GPU, the RX 580 may appear as card1.

```bash
# Enable manual power management
echo "manual" | sudo tee /sys/class/drm/card0/device/power_dpm_force_performance_level

# Adjust core clock and voltage for the peak performance state (State 7)
# Syntax: "s <state> <mhz> <mv>"
echo "s 7 1340 1060" | sudo tee /sys/class/drm/card0/device/pp_od_clk_voltage

# Adjust memory clock for high-bandwidth states
# Syntax: "m <state> <mhz> <mv>"
echo "m 1 2000 900" | sudo tee /sys/class/drm/card0/device/pp_od_clk_voltage

# Commit the changes to the GPU firmware
echo "c" | sudo tee /sys/class/drm/card0/device/pp_od_clk_voltage
```

Stability testing in 2026 involves monitoring the /sys/kernel/debug/dri/0/amdgpu_pm_info file. It is critical to note that core voltage cannot be set lower than the memory voltage. If an operator attempts to set a core voltage below the memory floor, the driver will either reject the command or revert to a stable default. For systems plagued by instability at high P-states, a safer alternative is to restrict the GPU to lower clock states using the pp_dpm_sclk interface, which effectively clamps the power draw without requiring precise voltage tuning.

```bash
# Restrict the GPU to States 0 through 5 to maximize efficiency
echo "0 1 2 3 4 5" | sudo tee /sys/class/drm/card0/device/pp_dpm_sclk
```

To revert all changes and restore factory defaults, the command echo "r" | sudo tee /sys/class/drm/card0/device/pp_od_clk_voltage is used.

#### Intel Arc and the Xe Driver Ecosystem

For Intel Arc GPUs (Alchemist and Battlemage), the 2026 landscape is dominated by the xe kernel driver, which has replaced the legacy i915 driver for discrete graphics. While the xe driver has matured significantly, offering up to a 260% performance boost in specific compute scenarios via Mesa 26.1 updates, manual voltage control remains more restricted compared to the AMD ecosystem. Direct undervolting is often impossible via the standard sysfs paths as the voltage parameters are typically read-only to prevent catastrophic hardware failure.

Optimization for Intel Arc in 2026 focuses on power limit overrides and frequency clamping. The LACT utility provides a robust interface for these modifications. Furthermore, modern Intel kernels support an experimental recovery mechanism that can restore GPU functionality after a fatal error without requiring a full system reboot, which is essential for maintaining uptime in mining rigs.

| Feature | Intel Kernel Parameter / Command | Practical Application |
| --- | --- | --- |
| Fatal Error Recovery | i915.enable_fatal_error_recovery=1 | MSI-based recovery and SBR reset after crashes. |
| Power Limit Override | lact power-limit <watts> | Cap power to reduce thermals during long-running tasks. |
| Frequency Clamping | echo <mhz> >.../freq_max | Limit peak clock to stay within efficient V/F curve. |
| Hardware Probe | xe.force_probe=<pci-id> | Required for early-access Battlemage/Celestial support. |

For legacy Intel integration, the intel-undervolt tool remains the standard for applying offsets to CPU and GPU planes via MSR 0x150. However, it is not compatible with the newer Battlemage (Xe2) architectures. The following LaTeX deconstruction of a typical Intel MSR write illustrates the complexity of these low-level tweaks:

To revert these Intel-specific tweaks, a system reboot is the most reliable method as MSR registers and xe parameters are reset during the hardware initialization phase.

### GPU Multiplexing and Virtualization via Custom Kernel Modules

The requirement to run concurrent mining and LLM workloads on a single physical GPU has led to the widespread adoption of Single Root I/O Virtualization (SR-IOV) and Multi-Instance GPU (MIG) technologies in 2026. While NVIDIA's MIG provides the most robust isolation, the community-driven SR-IOV modules for Intel and AMD have democratized GPU partitioning for consumer hardware.

#### Intel SR-IOV: The i915-sriov-dkms Solution

The i915-sriov-dkms module is the primary vehicle for GPU multiplexing on Intel Arc and UHD hardware in 2026. This module allows a single physical GPU (Physical Function, or PF) to expose up to seven Virtual Functions (VFs), which can be passed through to individual virtual machines or containers. This is particularly advantageous for home labs where one VF may handle Plex transcoding while another handles LLM inference.

Configuration Workflow:

Boot Parameters: The host must be booted with intel_iommu=on iommu=pt i915.enable_guc=3 i915.max_vfs=7.

VF Creation: After the module is loaded, VFs are created by writing to the sriov_numvfs path in sysfs.

```bash
# Create 7 virtual functions for the Intel GPU on bus 00:02
echo 7 | sudo tee /sys/devices/pci0000:00/0000:00:02.0/sriov_numvfs

# Verify successful creation
lspci -nnk | grep -i "VGA"
```

Stability in this environment requires that the same DKMS module be installed on both the host and the guest systems. In 2026, a frequent failure point is the interaction with UEFI Secure Boot, which requires the module to be manually signed or for Secure Boot to be disabled entirely. Reversion is accomplished by echoing 0 to the same path, which removes all VFs and returns the full compute resources to the host OS.

#### AMD MxGPU and the GIM Module

For AMD hardware, specifically the Instinct and Pro lines, the GPU-IOV Module (GIM) provides the necessary virtualization layer. While officially supporting MI300-series and Pro V-series cards, community effort in 2026 has extended this to certain high-end consumer cards through the MxGPU-Virtualization project. GIM is responsible for GPU IOV initialization, VF configuration, and "world switching" scheduling.

The setup requires blacklisting the standard amdgpu driver on the host if the GPU is intended for exclusive VM use, utilizing the modprobe.blacklist=amdgpu iommu=on amd_iommu=on boot parameters. The removal of this virtualization layer involves unloading the gim driver and restoring the standard amdgpu module: sudo modprobe -r gim && sudo modprobe amdgpu.

### Memory Subsystem Optimization for LLM Throughput

In the context of 2026 LLM inference, the GPU is frequently starved by the narrow pipe of memory bandwidth during the token generation phase. While a 70B parameter model may fit into the VRAM of a multi-GPU cluster, the efficiency with which the kernel handles the translation between virtual and physical addresses can determine whether the model reaches its theoretical throughput.

#### Hugepages: Reducing TLB Pressure and Latency

Standard 4KB memory pages are inefficient for the massive contiguous memory regions required by LLMs and mining buffers. By increasing the page size to 2MB or 1GB, the system can achieve a 20-40% reduction in memory access latency.

| Page Size | TLB Coverage | Ideal Workload | Configuration Command |
| --- | --- | --- | --- |
| 4KB (Standard) | 256KB - 4MB | General desktop use | Default |
| 2MB (Huge) | 128MB - 8GB | Quantized LLMs, Gaming | hugepages=4096 |
| 1GB (Gigantic) | 16GB - 1TB+ | Frontier LLMs (70B+), Large Mining Buffers | hugepagesz=1G hugepages=16 |

Explicit hugepages must be pre-allocated at boot to ensure the kernel can find enough contiguous physical memory before fragmentation occurs. Transparent Huge Pages (THP), while easier to manage, often introduce unpredictable latency spikes during the "khugepaged" defragmentation cycles. For deterministic inference, practitioners in 2026 typically disable THP (transparent_hugepage=never) and use explicitly allocated pages.

To revert hugepage allocations at runtime, the operator can write 0 to the nr_hugepages file, though this will fail if any applications are still holding the memory.

```bash
# Attempt runtime deallocation of 2MB hugepages
echo 0 | sudo tee /proc/sys/vm/nr_hugepages

# Flush page cache and reclaim memory
sudo sync && echo 3 | sudo tee /proc/sys/vm/drop_caches
```

#### NUMA Balancing and Data Locality

In 2026, high-core-count processors often utilize multi-die or multi-socket topologies, creating a Non-Uniform Memory Access (NUMA) environment. When an LLM inference task spans across NUMA nodes, the latency penalty for accessing remote memory can be severe: 100-200ns for local access vs 200-400ns for remote access.

The automatic NUMA balancing feature in the Linux kernel is designed to optimize this by moving tasks closer to their data. However, for pinned AI workloads, this background scanning can introduce unwanted overhead.

2026 Performance Recommendations:

Disable Automatic Balancing: Use sysctl -w kernel.numa_balancing=0 to prevent the kernel from moving memory segments during an active inference pass.

Static Pinning: Use numactl --cpunodeb[span_87](start_span)[span_87](end_span)ind=0 --membind=0 to ensure that both the execution threads and the model weights are strictly co-located on a single NUMA node.

Interleaving for Initialization: During the initial loading of massive weight files, memory interleaving (numactl --interleave=all) can utilize the aggregate bandwidth of all memory channels before the model is partitioned for inference.

### Extensible Scheduling with sched-ext and BPF

The most significant advancement for dual-workload systems in 2026 is the sched_ext framework. This allows operators to bypass the general-purpose scheduler and load specialized BPF programs that can prioritize LLM inference tokens while allowing mining tasks to consume every spare CPU cycle.

#### Optimized Schedulers for 2026 Workloads

The scx project provides several production-ready schedulers that can be swapped at runtime.

| Scheduler | Core Innovation | Mining/Inference Impact |
| --- | --- | --- |
| scx_layered | Multi-tier resource partitioning | Isolates inference threads from mining interrupts. |
| scx_lavd | Autopilot and Autopower | Dynamically shifts power budget to active inference nodes. |
| scx_rusty | User-space hybrid | High-interactivity for agentic systems under heavy load. |
| scx_cake | 4-Tier deficit tracking | Prioritizes short-burst inference over bulk mining jobs. |

The scx_cake scheduler uses an EWMA (Exponentially Weighted Moving Average) of task runtime to classify processes. A game render or LLM token thread typically runs for 2-8ms, landing in the high-priority Tier 2, while a background mining process running for 8ms+ is demoted to Tier 3. This ensures that the system remains responsive even when the CPU is 100% utilized by cryptographic tasks.

To deploy a specialized scheduler, the system must have a kernel built with CONFIG_SCHED_CLASS_EXT=y. The deployment is fully reversible: terminating the scheduler process or using the scxctl stop command immediately restores the default kernel behavior.

```bash
# Start scx_flash in Gaming mode for low-latency inference
sudo scxctl start --sched flash --mode gaming

# Switch to scx_cosmos for a more balanced multi-socket workload
sudo scxctl switch --sched cosmos --mode auto

# Revert to default kernel scheduler (immediate)
sudo scxctl stop
```

### Storage and I/O Optimization for NVMe Arrays

While often overlooked, the I/O scheduler plays a critical role in 2026 systems, particularly when weight streaming or rapid context caching is required. For high-performance NVMe SSDs, the consensus has shifted from the legacy "none" (no-op) scheduler to more intelligent, token-based systems under mixed-load conditions.

#### The Kyber vs None Debate

The "none" scheduler is the baseline, offering the lowest CPU overhead by passing requests directly to the NVMe firmware. This is ideal for dedicated inference nodes where I/O contention is non-existent. However, for systems running a blockchain node alongside an LLM, the kyber scheduler is superior. kyber implements read and write target latencies, preventing high-bandwidth write operations from blocking low-latency model reads.

| Scheduler | Target Workload | Advantage |
| --- | --- | --- |
| none | Dedicated model servers | Maximum raw IOPS for weight loading. |
| kyber | Cloud-native / Mixed load | 99.3% lower P99 latency under interference. |
| mq-deadline | Legacy SSDs / Database | Stable performance for small-block random I/O. |
| bfq | Desktop Interactivity | Best responsiveness at the cost of high CPU overhead. |

To apply these changes reversibly, the operator can modify the scheduler at runtime via sysfs:

```bash
# Switch NVMe device to Kyber for mixed-load inference
echo kyber | sudo tee /sys/block/nvme0n1/queue/scheduler

# Increase the request queue depth for deep-context models
echo 1024 | sudo tee /sys/block/nvme0n1/queue/nr_requests
```

### Advanced Network Integration and RDMA for 2026 Clusters

As models continue to scale beyond the capacity of a single GPU, the 2026 infrastructure relies on high-performance interconnects such as 200 GbE RoCE (RDMA over Converged Ethernet) and 3.2 Tbps InfiniBand. These technologies support GPUDirect RDMA, allowing data to move directly from one GPU's memory to another's across the network, completely bypassing the CPU and the kernel's networking stack.

For the kernel, this necessitates tweaks to the SoftIRQ balancing and interrupt processing logic. Disaggregated inference setups—where the prefill phase is handled by a compute-heavy node and the decode phase by a memory-bandwidth-heavy node—require the kernel to maintain low interrupt latency to avoid stalling the pipeline.

```bash
# Enable Jumbo Frames for RoCE (MTU 9000)
sudo ip link set dev eth0 mtu 9000

# Optimize TCP Receive/Send buffers for large weight transfers
sudo sysctl -w net.ipv4.tcp_rmem="4096 87380 8388608"
sudo sysctl -w net.ipv4.tcp_wmem="4096 87380 8388608"
```

### Stability Monitoring and Emergency Recovery Protocols

The aggressive nature of kernel tuning in 2026 demands a rigorous approach to monitoring and recovery. Stability is not a binary state but a managed risk profile that fluctuates with workload intensity and ambient temperature.

#### Real-Time Telemetry

Operators are encouraged to utilize a stack involving nvtop, intel_gpu_top, and Prometheus exporters to track metrics such as GPU junction temperature, power draw, and memory translation overhead. For the RX 580, particular attention should be paid to the fan speed and PWM control, as settings can sometimes revert to default after several minutes of heavy load if the feature masks are inconsistent.

#### The 2026 Recovery Toolkit

In the event of a system hang or a kernel panic induced by an unstable tweak, the following reversible actions are standardized:

Boot-Time Blacklisting: If an unstable undervolt or SR-IOV configuration prevents booting, use the module_blacklist=amdgpu,i915,xe parameter at the GRUB menu to gain shell access and revert configuration files.

SysRq Interventions: The SysRq-S sequence is the emergency kill switch for any BPF scheduler, instantly returning the system to a known-good state without requiring a hard reset.

MSR Reset: For Intel Arc Alchemist cards, any undervolts applied via intel-undervolt or wrmsr are lost upon an S3 sleep cycle or reboot, providing a built-in safety net for aggressive tuning.

Cleaning the Memory Slate: To resolve "stuck" hugepages after an application crash, the operator must manually unmount the hugetlbfs and clear the mapping directory before re-allocating.

### Comprehensive Implementation Table for 2026 Tweak Reversibility

| Optimization Layer | Reversibility Command / Action | Stability Risk | Recovery Mode | | :--- | :--- | :--- | :--- | | AMD Undervolting | echo "r" >.../pp_od_clk_voltage | Core crash / Kernel panic | Reboot / module_blacklist. | | Intel Power Caps | Terminate LACT or intel-undervolt | Thermal throttling | Automatic thermal reset. | | GPU Multiplexing | echo 0 >.../sriov_numvfs | System lockup on VF detach | SysRq-B or module_blacklist. | | Hugepages | echo 0 > /proc/sys/vm/nr_hugepages | Out-of-Memory (OOM) | sync && drop_caches. | | NUMA Balancing | echo 1 > /proc/sys/kernel/numa_balancing | Memory migration latency | Runtime sysctl restore. | | BPF Scheduling | sudo scx[span_50](start_span)[span_50](end_span)ctl stop | Thread starvation | SysRq-S. | | NVMe I/O | echo none >.../queue/scheduler | Latency spikes under load | Runtime sysfs restore. |

### Conclusion and Strategic Recommendations

The optimization of Linux systems for the combined tasks of crypto-mining and LLM inference in 2026 represents the pinnacle of heterogeneous systems engineering. The transition from static kernel parameters to dynamic, BPF-driven orchestration has created a system that is both more powerful and more complex to manage. For practitioners utilizing the AMD RX 580, success depends on leveraging the maturity of the amdgpu driver's manual power controls, utilizing specific feature masks to bypass the limitations of legacy firmware while respecting the monotonicity of the voltage curve.

For Intel Arc users, the focus shifts toward the xe driver's advanced recovery mechanisms and the community-driven SR-IOV modules, which allow consumer-grade hardware to punch well above its weight class in multi-tenant environments. In all scenarios, the memory subsystem remains the ultimate bottleneck. The move toward 1GB gigantic pages and strict NUMA affinity is no longer an optional optimization but a fundamental requirement for the large-scale models of 2026.

The emergence of "Agentic OS" frameworks like SchedCP suggests that the future of system optimization will be characterized by autonomous, real-time adjustments that transcend human manual tuning. Until these systems reach full maturity, the commands, stability notes, and reversal strategies provided in this report offer a definitive toolkit for any professional seeking to maintain the delicate balance between high-throughput compute and low-latency interaction in the 2026 Linux ecosystem. Consistent benchmarking using tools like cachyos-benchmarker and schbench is recommended before and after applying any tier of these tweaks to ensure that optimization goals are met without introducing secondary instabilities.

##### Works cited

1. LLM Inference Benchmarking - Measure What Matters | DigitalOcean, https://www.digitalocean.com/blog/llm-inference-benchmarking 2. Lowest Latency AI Inference Provider for Open-Source LLMs (2026 Engineering Guide), https://www.gmicloud.ai/blog/lowest-latency-ai-inference-provider-for-open-source-llms-2026-engineering-guide 3. Looking Ahead: What 2026 Holds for the Linux Ecosystem, https://www.linuxjournal.com/content/looking-ahead-what-2026-holds-linux-ecosystem 4. Extensible Scheduler Class - The Linux Kernel documentation, https://docs.kernel.org/scheduler/sched-ext.html 5. Towards Agentic OS: An LLM Agent Framework for Linux Schedulers - arXiv, https://arxiv.org/html/2509.01245v1 6. Sched-ext scheduler, what is it,which one is the best for performance or should I leave it at default : r/linux_gaming - Reddit, https://www.reddit.com/r/linux_gaming/comments/1rasppd/schedext_scheduler_what_is_itwhich_one_is_the/ 7. [2509.01245] Towards Agentic OS: An LLM Agent Framework for Linux Schedulers - arXiv, https://arxiv.org/abs/2509.01245 8. My RX 580 is Old but Still Going Strong : r/RigBuild - Reddit, https://www.reddit.com/r/RigBuild/comments/1qdg3so/my_rx_580_is_old_but_still_going_strong/ 9. Building a Poverty-Spec AI Cluster: Repurposing RX 580s for Local LLMs - SitePoint, https://www.sitepoint.com/poverty-spec-ai-cluster-rx-580-local-llm/ 10. Question - "Undervolting" rx 580 - Tom's Hardware Forum, https://forums.tomshardware.com/threads/undervolting-rx-580.3892322/ 11. HOWTO undervolt the AMD RX 4XX and RX 5XX GPUs ..., https://linuxreviews.org/HOWTO_undervolt_the_AMD_RX_4XX_and_RX_5XX_GPUs 12. Undervolting AMD RX 580 on Linux? : r/linux_gaming - Reddit, https://www.reddit.com/r/linux_gaming/comments/ebdkfe/undervolting_amd_rx_580_on_linux/ 13. Undervolting RX580 via Corectrl : r/linux_gaming - Reddit, https://www.reddit.com/r/linux_gaming/comments/gbqe0e/undervolting_rx580_via_corectrl/ 14. strongtz/i915-sriov-dkms: dkms module of Linux i915 driver ... - GitHub, https://github.com/strongtz/i915-sriov-dkms 15. Intel Xe Linux Driver Will No Longer Block D3cold For All Battlemage GPUs - Phoronix, https://www.phoronix.com/news/Intel-Battlemage-D3cold-Again 16. Intel Arc "Alchemist" Linux Driver Update Can Yield Up to 260% Performance Boost, https://www.techpowerup.com/345740/intel-arc-alchemist-linux-driver-update-can-yield-up-to-260-performance-boost 17. Is undervolting on linux possible? : r/IntelArc - Reddit, https://www.reddit.com/r/IntelArc/comments/1rmhsjh/is_undervolting_on_linux_possible/ 18. [Linux] INTEL PLEASE HERE ME: bring support to linux for fancontrol and overclocking please : r/IntelArc - Reddit, https://www.reddit.com/r/IntelArc/comments/1o008ge/linux_intel_please_here_me_bring_support_to_linux/ 19. Releases · ilya-zlobintsev/LACT - GitHub, https://github.com/ilya-zlobintsev/LACT/releases 20. Q1 2026 Support Thread – Use this for ALL Intel Arc GPU support questions (install, crashes, performance, games, AV1 encoding, multi-monitor, etc.) - Reddit, https://www.reddit.com/r/IntelArc/comments/1q35q34/q1_2026_support_thread_use_this_for_all_intel_arc/ 21. Release Notes: LTS — Intel® software for general purpose GPU capabilities documentation, https://dgpu-docs.intel.com/releases/LTS-release-notes.html 22. Undervolting CPU - ArchWiki, https://wiki.archlinux.org/title/Undervolting_CPU 23. README.md - mihic/linux-intel-undervolt - GitHub, https://github.com/mihic/linux-intel-undervolt/blob/master/README.md 24. NVIDIA vGPU for Compute — NVIDIA AI Enterprise, https://docs.nvidia.com/ai-enterprise/release-7/7.1/infra-software/vgpu.html 25. Intel's forgotten iGPU feature is perfect for your home lab - XDA Developers, https://www.xda-developers.com/intels-forgotten-igpu-feature-is-perfect-for-your-home-lab/ 26. The GPU Capacity Crisis: Why Enterprises Are Rethinking Where AI Runs in 2026, https://vexxhost.com/blog/gpu-capacity-crisis-ai-infrastructure-2026/ 27. Intel Gen 12 vGPU (SR-IOV) on Proxmox - GitHub, https://github.com/Upinel/PVE-Intel-vGPU 28. CubeLine/i915-sriov-dkms - Gitee, https://gitee.com/715568485/i915-sriov-dkms 29. amd/MxGPU-Virtualization - GitHub, https://github.com/amd/MxGPU-Virtualization 30. ok but what about literally every other MxGPU-capable GPU · Issue #1 - GitHub, https://github.com/amd/MxGPU-Virtualization/issues/1 31. AMD Publishes Open-Source GIM Driver For GPU Virtualization, Radeon "In The Roadmap", https://www.phoronix.com/news/AMD-GIM-Open-Source 32. Did the AI boom ruin any future for GPU Splitting / SR-IOV on consumer hardware? - Reddit, https://www.reddit.com/r/hardware/comments/1liv2zd/did_the_ai_boom_ruin_any_future_for_gpu_splitting/ 33. MxGPU-Virtualization/README.md at staging - GitHub, https://github.com/amd/MxGPU-Virtualization/blob/staging/README.md 34. Getting started with Virtualization - Instinct™ Docs, https://instinct.docs.amd.com/projects/virt-drv/en/mainline-8.2.0.k/userguides/Getting_started_with_MxGPU.html 35. Why Your LLM Is Slow: The Memory Bottleneck Nobody Talks About | by Sunil Kumawat, https://medium.com/@Sunil_Kumawat/why-your-llm-is-slow-the-memory-bottleneck-nobody-talks-about-015ce03a5b63 36. 7 Best GPU for LLM in 2026 (Including Local LLM Setups) - Fluence Network, https://www.fluence.network/blog/best-gpu-for-llm/ 37. Which AI Inference Platform is Fastest for Open-Source Models? (2026 Engineering Guide), https://www.gmicloud.ai/blog/which-ai-inference-platform-is-fastest-for-open-source-models-2026-engineering-guide 38. How to Configure Hugepages as a Resource for High-Performance Workloads - OneUptime, https://oneuptime.com/blog/post/2026-02-09-hugepages-resource-high-performance/view 39. Benchmarking transparent versus 1GiB static huge page performance in Linux virtual machines | Red Hat Developer, https://developers.redhat.com/blog/2021/04/27/benchmarking-transparent-versus-1gib-static-huge-page-performance-in-linux-virtual-machines 40. Memory Management: NUMA, Huge Pages, and Memory Compactio... - Anshad Ameenza, https://anshadameenza.com/blog/technology/2025-01-22-memory-management-numa-huge-pages-compaction/ 41. How to Add Custom Kernel Parameters for Performance Tuning via ..., https://oneuptime.com/blog/post/2026-03-04-custom-kernel-parameters-performance-grub2-rhel-9/view 42. How to Tune Memory and NUMA Performance on RHEL - OneUptime, https://oneuptime.com/blog/post/2026-03-04-tune-memory-numa-performance-rhel-9/view 43. disable transparent hugepages - Unix & Linux Stack Exchange, https://unix.stackexchange.com/questions/99154/disable-transparent-hugepages 44. linux - Hugepages seems to be stuck - Server Fault, https://serverfault.com/questions/912449/hugepages-seems-to-be-stuck 45. scx/OVERVIEW.md at main · sched-ext/scx - GitHub, https://github.com/sched-ext/scx/blob/main/OVERVIEW.md 46. Deep Dive into NUMA Optimization on Linux Systems, https://linuxgd.medium.com/deep-dive-into-numa-optimization-on-linux-systems-e4c0aa8e82b1 47. Automatic Non-Uniform Memory Access (NUMA) balancing | System Analysis and Tuning Guide | SLES 15 SP7 - SUSE Documentation, https://documentation.suse.com/sles/15-SP7/html/SLES-all/cha-tuning-numactl.html 48. sched-ext/scx: sched_ext schedulers and tools - GitHub, https://github.com/sched-ext/scx 49. 01 Background & current upstream status 02 Latest and greatest features 03 What do we still need? - Linux Kernel Developers' bpfconf 2025, https://bpfconf.ebpf.io/bpfconf2024/bpfconf2024_material/Sched_Ext_-_What_s_New_&_What_s_Missing.pdf 50. eBPF Tutorial: Introduction to the BPF Scheduler - DEV Community, https://dev.to/yunwei37/ebpf-tutorial-introduction-to-the-bpf-scheduler-5101 51. sched-ext Tutorial | CachyOS, https://wiki.cachyos.org/configuration/sched-ext/ 52. OOLinux IO Schedulers Explained: BFQ, MQ-Deadline & Kyber | by Majidbasharat - Medium, https://medium.com/@majidbasharat21/linux-io-schedulers-explained-bfq-mq-deadline-kyber-ef94609b11a4 53. "None" scheduler for NVMe SSD? - Issues & Assistance - CachyOS Forum, https://discuss.cachyos.org/t/none-scheduler-for-nvme-ssd/13632 54. How to Tune the Linux I/O Scheduler (mq-deadline, bfq, none) on RHEL - OneUptime, https://oneuptime.com/blog/post/2026-03-04-tune-linux-io-scheduler-mq-deadline-bfq-none-rhel-9/view 55. Milestone1 Action Plan - MD | PDF - Scribd, https://www.scribd.com/document/999565342/Milestone1-Action-Plan-md 56. How to Tune I/O Schedulers (mq-deadline, bfq, none) on Ubuntu - OneUptime, https://oneuptime.com/blog/post/2026-03-02-how-to-tune-io-schedulers-on-ubuntu/view 57. BFQ, Multiqueue-Deadline, or Kyber? Performance Characterization of Linux Storage Schedulers in the NVMe Era - Massivizing Computer Systems, https://atlarge-research.com/pdfs/2024-io-schedulers.pdf 58. How to Run Your Own Local LLM — 2026 Edition — Version 1 | by Thomas Cherickal, https://thomascherickal.medium.com/how-to-run-your-own-local-llm-2026-edition-version-1-7ec6fe654c03 59. 6 Production-Tested Optimization Strategies for High-Performance LLM Inference - BentoML, https://www.bentoml.com/blog/6-production-tested-optimization-strategies-for-high-performance-llm-inference 60. Linux Ubuntu with arc b570 : r/IntelArc - Reddit, https://www.reddit.com/r/IntelArc/comments/1quxlit/linux_ubuntu_with_arc_b570/ 61. How to remove i915-sriov-dkms · Issue #173 - GitHub, https://github.com/strongtz/i915-sriov-dkms/issues/173 62. [SOLVED] Segfault with i915-sriov-dkms on Guest Shutdown / Applications & Desktop Environments / Arch Linux Forums, https://bbs.archlinux.org/viewtopic.php?id=306282 63. Free Up Linux Memory WITHOUT Reboot! (Instant RAM & Swap Cleanup) - YouTube, https://www.youtube.com/watch?v=VYkxmzIpcOc 64. Sched-Ext: The BPF extensible scheduler class - Linux Plumbers Conference, https://lpc.events/event/18/contributions/1667/contribution.pdf
