<!--
Generated from a preserved DOCX source; wording is retained from the source.
Source: sources/original-docx/6. Hardening linux.docx
Git blob SHA: d6f761544e05ccddb4c0269b3d58e059d5bbcad7
-->

## Corpus status (living layer)

**Last reconciled:** 2026-06-24
**Confidence:** Partly Supported for external-threat hardening; distinct from organism self-mutation law (Chapter 06)
**Read with:** [Chapter 06](06-mutation-safety-and-permission-law.md) (inverted threat: self-mutation), [Chapter 05](05-measurement-daemon-and-natural-language-shell.md) (agent containment), [Chapter 20](20-market-and-viability.md) living layer (TEE claims)

### Authoritative for

- Defense-in-depth checklist leads: firewall, SSH, IDS, supply-chain awareness for operator hosts
- DePIN weight-copying / subnet attack context as background

### Superseded or narrowed

- **TEE/bus attestation as oracle solution** — see Chapter 20 living layer; prefer Chapters 01–11 non-TEE confirmation stack for CursiveOS.
- Deployment recommendations remain **Unvalidated** until `experiments/security-hardening-validation-plan.md` runs on target hardware.

### Open until experiment/hardware

- Tiered hardening baseline per platform; immune-sensor prototype (Chapter 01 / pipeline)

---


## Reinforced research (2026-06-24)

- **Threat model split:** This chapter = external attackers; Ch06 = organism self-mutation — complementary, not interchangeable.
- **CIS Benchmarks / STIG:** Linux hardening baselines (2024–2025) — operational checklist for DePIN fleet hosts.
- **TEE overclaims:** Ch20 living layer — TDX bus integrity insufficient for operator physical-access oracle; use Ch01–11 confirmation stack.
- **Agent containment:** Ch05 layered sandbox — external prompt injection must not gain daemon write path.
- **Immune sensors:** Ch01 backlog — detect correlated fake confirmations across fleet (prototype).

# Security and Hardening

## Corpus integration notes (2026-06-24)

Targeted narrowing for the DOCX import below. External-threat hardening is distinct from organism self-mutation law (Ch06).

1. **TEE / attestation as DePIN oracle:** Import may cite TEE — **Disproven** for operator physical-access bus attacks (Ch20 living layer; VALIDATION). Prefer Ch01–11 population confirmation + Ch11 fingerprints.
2. **Bittensor PyPi / weight-copying:** Real supply-chain incidents (2024–2025) — background for immune-sensor backlog (Ch01); not a complete CursiveOS defense.
3. **CIS/STIG checklists:** Operational leads — run `experiments/security-hardening-validation-plan.md` before fleet-wide defaults.
4. **Agent + mining convergence:** Ch05 containment required; prompt injection must not reach daemon sensor writes.
5. **Subnet attack tables:** Market-context only; verify current counts before external citation.

## Hardening Linux servers for crypto mining and AI agent infrastructure in 2026

**Defense-in-depth is no longer optional for mining rigs and AI inference nodes.**

> **Corpus inline (2026-06-24):** External-threat hardening (this import) ≠ organism self-mutation law (**Ch06**). TEE/bus attestation **Disproven** as CursiveOS oracle (Ch20); use Ch01–11 population confirmation + Ch11 fingerprints.

 The convergence of cryptojacking campaigns, DePIN supply chain attacks (Bittensor's $8M PyPi incident), [The Block](https://www.theblock.co/post/303547/bittensor-exploit) and increasingly sophisticated exploitation of GPU-enabled servers demands a layered security posture spanning kernel, network, access control, monitoring, and decentralized trust verification. This guide synthesizes the most current 2025–2026 hardening practices across five critical domains: kernel hardening, firewall configuration, SSH access control, intrusion detection, and DePIN subnet security. The threat landscape has shifted — attackers now target not just the software stack but the entire trust chain, from kernel modules through package managers to consensus weight manipulation. [Bittensor](https://docs.learnbittensor.org/concepts/weight-copying-in-bittensor)

---

### Kernel hardening that won't kill your hashrate

Modern Linux kernels ship with powerful self-protection features, but they require explicit activation — and careful tuning for GPU-intensive workloads. The goal is maximizing exploit resistance while preserving the low-latency memory access that mining and AI inference demand.

**Sysctl parameters** form the first layer. Place a hardening configuration in `/etc/sysctl.d/99-hardening.conf` [Linux Audit](https://linux-audit.com/system-hardening/linux-hardening-with-sysctl/) covering three domains. For kernel self-protection: set `kernel.kptr_restrict=2` (hide kernel pointers), `kernel.dmesg_restrict=1`, [github](https://madaidans-insecurities.github.io/guides/linux-hardening.html) `kernel.unprivileged_bpf_disabled=1` with `net.core.bpf_jit_harden=2` (eBPF is a major attack surface), [github](https://madaidans-insecurities.github.io/guides/linux-hardening.html) `kernel.yama.ptrace_scope=2` (restrict cross-process debugging), and `kernel.randomize_va_space=2` for full ASLR. [WafaTech Blogs](https://wafatech.sa/blog/linux/linux-security/fine-tuning-linux-server-security-essential-sysctl-parameters-for-kernel-hardening/) For network hardening: enable SYN flood protection with `net.ipv4.tcp_syncookies=1`, [Sysadmin](https://www.sysadmin.md/hardening-existing-linux-server-via-sysctl-parameters.html) disable IP forwarding and ICMP redirects, enable reverse path filtering (`rp_filter=1`), and log martian packets. [nixCraft](https://www.cyberciti.biz/faq/linux-kernel-etcsysctl-conf-security-hardening/) For mining/AI-specific memory tuning: configure `vm.nr_hugepages` based on your thread count (critical for XMRig/RandomX performance and AI model loading), set `vm.swappiness=10`, and enable `fs.protected_hardlinks=1` and `fs.protected_symlinks=1`.

Boot parameters via GRUB should include `slab_nomerge init_on_alloc=1 init_on_free=1 page_alloc.shuffle=1 pti=on lockdown=integrity module.sig_enforce=1 iommu=force`. The `iommu=force` parameter is particularly important for systems with GPUs to prevent DMA attacks. [Madaidan's Insecurities](https://madaidans-insecurities.github.io/guides/linux-hardening.html) The `init_on_alloc` and `init_on_free` parameters [DoHost](https://dohost.us/index.php/2025/11/09/disabling-kernel-module-loading-after-boot-for-extreme-security/) add marginal overhead but prevent data leakage between allocations.

**Kernel module restrictions** dramatically reduce attack surface. Create `/etc/modprobe.d/server-hardening.conf` [Linux Audit](https://linux-audit.com/kernel/kernel-hardening-disable-and-blacklist-linux-modules/) to disable approximately 40 unnecessary modules including legacy network protocols (DCCP, SCTP, RDS, TIPC), wireless and Bluetooth stacks, USB storage, and FireWire/Thunderbolt (DMA attack vectors). Use `install <module> /bin/false` rather than just `blacklist`, as blacklisting only prevents auto-loading. [OneUptime](https://oneuptime.com/blog/post/2026-03-04-blacklist-kernel-module-rhel-9/view) After all required modules are loaded at boot — NVIDIA drivers, network modules — lock further loading by setting `kernel.modules_disabled=1` [Linux Audit](https://linux-audit.com/kernel/kernel-hardening-disable-and-blacklist-linux-modules/) via a systemd service that runs after `nvidia-persistenced.service`. For NVIDIA proprietary drivers under `module.sig_enforce=1`, sign DKMS-built modules with a Machine Owner Key (MOK) enrolled in UEFI, or use distribution-packaged pre-signed drivers.

**LKRG (Linux Kernel Runtime Guard) reached v1.0.0 in September 2025**, signaling production readiness. [Help Net Security](https://www.helpnetsecurity.com/2025/09/08/linux-kernel-runtime-guard-lkrg-1-0-0-released/) LKRG performs runtime integrity checking of kernel code and metadata, detects unauthorized privilege escalation, monitors that CPU security features (SMEP, SMAP) remain enabled, and validates that SELinux/AppArmor enforcement hasn't been tampered with. [Linux Journal](https://www.linuxjournal.com/content/inside-linux-kernel-runtime-guard-lkrg-new-layer-kernel-integrity-protection) Mining community reports confirm "minimal impact on hashrates." [Hive OS](https://hiveon.com/forum/t/linux-kernel-runtime-guard-lkrg-rig-security/46930) It works on kernels 3.10 through 6.17-rc4 [Ipfire](https://lists.ipfire.org/hyperkitty/list/development@lists.ipfire.org/thread/CDFCGIE2AKSPN6SUNZYC5EO465SIZCJV/) and is available pre-installed in Rocky Linux from CIQ with UEFI Secure Boot signing. [Lkrg](https://lkrg.org/)

**OpenPaX**, announced by Edera in 2025, provides an open-source alternative to grsecurity's PaX memory protections under GPLv2. [Phoronix](https://www.phoronix.com/news/Edera-OpenPaX-Announced) Grsecurity itself remains commercial-only, [Privacy Guides](https://www.privacyguides.org/articles/2022/04/22/linux-system-hardening/) [Grsecurity](https://grsecurity.net/) supporting kernels 5.15, 6.6, and 6.18, with reported 70–100% native performance for compute-bound tasks — but GPU driver compatibility at higher security levels requires testing.

For mandatory access control, **AppArmor 4.0** (Ubuntu 24.04+) [Markaicode](https://markaicode.com/ubuntu-server-hardening-2025/) and **SELinux** (RHEL/Rocky/Alma, plus openSUSE which switched to SELinux in February 2025) [Command Linux](https://commandlinux.com/statistics/selinux-and-apparmor-adoption-statistics-in-production-environments/) are the two primary options. Custom profiles should restrict mining software to only its binary, configuration files, hugepage access, GPU device nodes, and network sockets — explicitly denying shell execution, SSH key access, and sensitive file reads. Generate profiles using `aa-genprof` (AppArmor) or `audit2allow` (SELinux) in learning mode, then enforce. [DoHost](https://dohost.us/index.php/2025/10/05/beyond-dac-why-selinux-and-apparmor-are-essential-for-modern-linux-security/) Modern kernels support multiple LSMs simultaneously: boot with `lsm=landlock,lockdown,yama,integrity,apparmor` to stack complementary protections.

**Seccomp profiles** restrict syscall access per process. [DevOps Cube](https://devopscube.com/seccomp-in-kubernetes/) Generate profiles by tracing syscalls with `strace -c -f` during normal operation, or use SlimToolkit for containerized workloads. [GitHub](https://github.com/topics/seccomp-profile) Mining software (XMRig) requires `mmap` with `PROT_EXEC` for JIT-compiled RandomX code and `MAP_HUGETLB` for hugepage allocation. AI inference workloads need additional `ioctl` syscalls for CUDA/ROCm operations and `mmap`/`munmap` for multi-gigabyte model loading. Start with `SCMP_ACT_LOG` to audit before switching to `SCMP_ACT_ERRNO`. [DevOps Cube](https://devopscube.com/seccomp-in-kubernetes/) For systemd-managed services, use `SystemCallFilter=@system-service @io-event @network-io` with explicit denials for `@mount @swap @reboot @raw-io @module`.

---

### Firewall architecture: nftables, egress control, and DDoS resilience

**nftables is the unambiguous standard for 2025–2026.** All major distributions use it as the default backend, [Medium](https://medium.com/@ihouelecaurcy/the-complete-nftables-guide-modern-linux-firewall-mastery-79fb86894d5c) and even `iptables` commands now typically route through the `iptables-nft` compatibility layer. For mining and AI workloads, nftables offers O(log n) lookups [Medium](https://medium.com/@ihouelecaurcy/the-complete-nftables-guide-modern-linux-firewall-mastery-79fb86894d5c) via sets (versus iptables' O(n) linear processing), atomic rule updates without race conditions, native set support replacing external `ipset`, and unified IPv4/IPv6 handling. [Medium](https://medium.com/@ihouelecaurcy/the-complete-nftables-guide-modern-linux-firewall-mastery-79fb86894d5c)

A production firewall for mining and AI servers requires three key design principles: **strict ingress filtering, aggressive egress filtering, and intelligent rate limiting**. On ingress, drop all traffic by default (policy drop), [Red Hat](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/8/html/securing_networks/getting-started-with-nftables_securing-networks) accept only established/related connections, restrict SSH to trusted management IPs, and never expose AI inference ports (Ollama 11434, vLLM 8000) to the public internet. Mining is typically outbound-only — most setups need zero inbound mining rules.

Egress filtering is where mining servers diverge sharply from typical configurations. **Restrict outbound connections exclusively to known mining pool IPs and required service endpoints.** Maintain a dynamically-updated nftables named set of pool IPs, resolved via a cron script that runs `dig +short` against pool domains every 15 minutes. Block all other outbound traffic. This prevents compromised servers from connecting to unauthorized pools (cryptojacking callbacks), exfiltrating AI model weights, or communicating with command-and-control infrastructure.

Common mining ports to whitelist include **3333 and 4444** (Stratum TCP), **3443** (Stratum SSL), [Bitcoinminingpoolsoftware](https://www.bitcoinminingpoolsoftware.com/bitcoin-mining-pool-url-list.html) and **443** (SSL, increasingly used by pools to bypass restrictive firewalls). For AI inference, bind services to localhost or trusted subnets only — ports 11434 (Ollama), 8000 (vLLM), and 8080 (LocalAI) should never be internet-accessible without authentication.

Rate limiting protects both SSH and API endpoints. For SSH, use nftables dynamic sets to allow a maximum of 4 new connections per minute per source IP. [OneUptime](https://oneuptime.com/blog/post/2026-03-20-rate-limit-ipv6-nftables/view) For AI inference APIs, rate limit to 30–100 requests per minute per source depending on the endpoint's expected throughput. Mining pool connections are persistent (Stratum keeps connections alive), so rate-limit only new connections, not established traffic.

For DDoS mitigation, implement a prerouting chain at priority -150 that drops invalid packets, rejects new non-SYN TCP packets, filters Christmas tree and null packets, and blocks connections with bogus TCP MSS values. [Arch Linux Forums](https://bbs.archlinux.org/viewtopic.php?id=289072) Use dynamic blacklist sets with automatic escalation — IPs exceeding 5 new connections per minute get added to a 4-hour blacklist. [fraggod](https://blog.fraggod.net/2025/01/16/nftables-rate-limiting-against-low-effort-ddos-attacks.html) Tune connection tracking with `nf_conntrack_max=524288` and reduce TCP timeout values.

**CrowdSec has emerged as the recommended replacement for Fail2ban** in 2025–2026 deployments. Written in Go, it processes over 10,000 log lines per second versus Fail2ban's Python-based engine. Its key differentiator is collaborative threat intelligence — when one CrowdSec instance detects an attacker, that IP is shared across the network for proactive blocking. [AZDIGI](https://azdigi.com/en/blog/cong-cu/crowdsec-on-linux-vps-next-generation-ids-to-replace-fail2ban) CrowdSec's nftables bouncer uses IP sets (handling millions of IPs efficiently) versus Fail2ban's individual firewall rules. Install with `crowdsec-firewall-bouncer-nftables` and add the `crowdsecurity/linux` and `crowdsecurity/sshd` collections. [AZDIGI](https://azdigi.com/en/blog/cong-cu/crowdsec-on-linux-vps-next-generation-ids-to-replace-fail2ban)

Network segmentation should isolate mining, AI inference, and management into separate VLANs with strict inter-zone rules. Only the management VLAN should have SSH access to mining and AI VLANs. On single-server deployments, Linux network namespaces provide equivalent isolation — run mining software in a dedicated namespace with its own network stack and restricted egress.

---

### SSH access control: from keys to certificates to zero trust

The SSH attack surface on mining servers is particularly attractive to adversaries because compromised access means direct control over mining revenue. A 2025–2026 SSH hardening strategy spans five layers: authentication method, configuration hardening, access architecture, brute-force protection, and visibility reduction.

**Ed25519-SK (FIDO2 hardware-backed) keys represent the highest practical security tier.** The private key never leaves the hardware device (YubiKey 5 Series, Security Key Series), and the `-O verify-required` flag enforces both PIN and physical touch for every authentication. Generate with `ssh-keygen -t ed25519-sk -O resident -O verify-required`. [Yubico](https://developers.yubico.com/SSH/Securing_SSH_with_FIDO2.html) Maintain two hardware keys (primary and backup) since FIDO2 keys cannot be cloned. For environments that can't use hardware keys, standard Ed25519 keys remain the gold standard — faster and more secure than RSA-4096 at a fraction of the key size.

The `sshd_config` hardening profile should disable password authentication entirely, [nixCraft](https://www.cyberciti.biz/tips/linux-unix-bsd-openssh-server-best-practices.html) restrict access to named users/groups, set `LoginGraceTime 30`, `MaxAuthTries 3`, and `MaxStartups 10:30:60`. Kill idle sessions with `ClientAliveInterval 300` and `ClientAliveCountMax 2`. Disable all forwarding (X11, TCP, agent, tunnel). For cryptographic hardening per sshaudit.com's 2025 recommendations, prioritize `sntrup761x25519-sha512@openssh.com` for post-quantum key exchange, `chacha20-poly1305@openssh.com` for ciphers, [Sshaudit](https://www.sshaudit.com/hardening_guides.html) and set `RequiredRSASize 3072`. Filter DH moduli with `awk '$5 >= 3071'` to remove weak groups.

**For fleets exceeding 10 servers, SSH certificates eliminate the N×M key management problem.** Instead of distributing public keys to every server, a Certificate Authority signs short-lived certificates (8–24 hours) that servers trust automatically. Teleport (CNCF project) provides the most comprehensive solution: SSO integration, session recording, RBAC, and automatic certificate issuance. Smallstep's step-ca offers a lighter-weight self-hosted CA with OIDC-based authentication. Even OpenSSH's native CA capabilities (`ssh-keygen -s`) work for smaller deployments — sign user keys valid for 8 hours with restricted principals.

Bastion host architecture places a single hardened SSH gateway in the public subnet with all mining rigs and AI servers on private subnets accepting connections only from the bastion's IP. Use OpenSSH's `ProxyJump` directive [Red Hat](https://www.redhat.com/en/blog/ssh-proxy-bastion-proxyjump) in `~/.ssh/config` for transparent multi-hop access. For Ansible-managed mining fleets, set `ansible_ssh_common_args='-o ProxyJump=admin@bastion:2222'` in inventory variables. [Jeff Geerling](https://www.jeffgeerling.com/blog/2022/using-ansible-playbook-ssh-bastion-jump-host/)

**fwknop (Single Packet Authorization) adds a pre-authentication layer** that renders SSH completely invisible to port scanners. A single encrypted, HMAC-authenticated, non-replayable UDP packet opens the firewall for the source IP for a 30-second window. The server presents zero attack surface to anyone without the SPA credentials — no port responds, making zero-day exploitation impossible without the knock sequence. Use HMAC mode for replay protection and maintain fallback access methods (console/IPMI) for operational resilience.

---

### Intrusion detection tuned for mining and AI workloads

Effective intrusion detection for mining and AI infrastructure requires correlation across three signal types: host-level behavior, network traffic patterns, and file integrity. The recommended stack combines **Wazuh** (host IDS/SIEM), **Suricata** (network IDS), **Falco** (runtime behavioral detection), and multi-layer file integrity monitoring.

**Wazuh** (evolved from the OSSEC fork) serves as the centralized security platform. Deploy agents on all mining rigs and AI servers — each agent requires approximately 1 CPU core, 1 GB RAM, and 10 GB disk. Configure custom rules to monitor for known cryptominer process names (xmrig, minerd, cpuminer, ethminer), connections to mining pool ports, wallet address changes in configuration files, and hashrate drops (potential hash hijacking). Wazuh's Active Response capability can automatically block threats when rules trigger. Map detections to MITRE ATT&CK T1496 (Resource Hijacking) for standardized threat categorization.

**Suricata** provides network-level visibility through deep packet inspection. Deploy on a network tap or mirrored switch port. Write custom rules to detect Stratum protocol traffic (`content:"mining.subscribe"`), connections to common mining pool ports, and known mining software HTTP user agents. The default ET Open ruleset, pulled automatically by `suricata-update`, covers broad threats; supplement with custom rules for your specific environment. Suricata's JSON logs (`eve.json`) feed directly into Wazuh for correlated analysis.

**Falco** (CNCF graduated project) operates at the kernel level via eBPF, monitoring syscalls in real-time with minimal performance overhead. Create custom rules to detect cryptocurrency mining processes by name and command-line arguments (e.g., `proc.cmdline contains "stratum+tcp"`), outbound connections to mining pool ports from containers, [OneUptime](https://oneuptime.com/blog/post/2026-01-25-falco-runtime-security/view) shell spawning in production containers, and unauthorized access to sensitive files. Route alerts through Falcosidekick to Slack, PagerDuty, or your SIEM. For active blocking capabilities rather than just detection, add **Tetragon** (Cilium/Isovalent) as a complementary eBPF-based enforcement layer.

File integrity monitoring should operate at three tiers. **Real-time detection** via osquery's inotify-based `file_events` monitoring [HowtoForge](https://www.howtoforge.com/tutorial/how-to-setup-file-integrity-monitoring-fim-using-osquery-on-linux-server/) covers mining binaries, AI model files, SSH authorized_keys, wallet configurations, and crontab entries. **Periodic baseline verification** via AIDE nightly runs provides comprehensive change detection [DoHost](https://dohost.us/index.php/2025/11/30/implementing-file-integrity-monitoring-fim-aide-ossec-introduction/) that catches anything missed by real-time monitoring. **Centralized aggregation** through Wazuh's FIM module consolidates alerts across the fleet. [Perlod](https://perlod.com/tutorials/file-integrity-monitoring-server/)

For centralized logging, Grafana Loki offers up to 90% less storage than the ELK stack by indexing only labels and metadata. Collect logs with Promtail or Fluent Bit agents, query with LogQL, and visualize alongside Prometheus metrics in Grafana dashboards. Key patterns to monitor include GPU utilization anomalies (unexpected high usage outside scheduled mining), hashrate deviation from baselines, unusual outbound data transfers (potential model exfiltration), and power consumption spikes correlating with unknown network connections.

Anomaly detection for cryptojacking on legitimate mining operations focuses on unexpected deviation from known baselines: sustained CPU/GPU usage during off-hours, connections to unwhitelisted pool ports, DNS queries to known mining pool domains outside your approved list, and process names that don't match your deployed software. A 2024 IEEE paper demonstrated 80% cryptojacking detection rates using GPU load and VRAM consumption pattern analysis.  (arXiv)

### AI model supply chain: malicious weights as a code-execution and measurement-integrity surface

The line above ("verify AI model hashes before loading") names one control but does
not characterize the attack surface it defends. For CursiveOS this surface is
not optional background: the local stack **pulls and runs external model weights**
(Ollama, `llama.cpp`/GGUF, Hugging Face — see [Chapter 10](10-local-llm-inference-runtime-architecture.md)
and the Arc B70 agent in [Chapter 18](18-local-agent-arc-b70.md)), and a fleet that
distributes models or presets across contributors inherits everyone's model-pull
risk. A poisoned model is two threats at once: a **host-compromise vector** (code
execution during load or inference) and a **measurement-integrity vector** (a model
that recognizes the benchmark harness and games the score — the Goodhart problem of
[Chapter 08](08-population-confirmation-and-fleet-statistics.md) and the reward-hacking
literature digested in [Chapter 03](03-rsi-literature-and-organism-synthesis.md), arriving
through the weights rather than through the optimizer).

**The format is the first decision.** Legacy PyTorch checkpoints (`.bin`, `.pt`,
`.ckpt`) are Python **pickle** streams, and deserializing a pickle (`torch.load`)
can execute arbitrary code embedded in the checkpoint's `__reduce__` hooks — credential
theft, environment-variable exfiltration, payload download, or a reverse shell, all
during load and before a single token is generated. [Hugging Face — Pickle Scanning](https://huggingface.co/docs/hub/en/security-pickle)
`safetensors` was designed to remove this: it stores only tensor data plus the
metadata needed to map them, so loading a `.safetensors` file does not run any Python
reconstruction logic. A May 2023 Trail of Bits audit commissioned by Hugging Face,
EleutherAI, and Stability AI found **no critical flaw leading to arbitrary code
execution**, fixed a polyglot-file validation gap, and the format subsequently became
the Transformers default. [EleutherAI — Safetensors audited as really safe](https://blog.eleuther.ai/safetensors-security-audit/)
[Hugging Face — Safetensors security audit](https://huggingface.co/blog/safetensors-security-audit)

**Scanners are necessary but not sufficient — the same lesson as prompt injection.**
In February 2025 ReversingLabs found malicious PyTorch models on Hugging Face
("nullifAI") that compressed the archive with 7z instead of the default ZIP so that
`torch.load` would not auto-load them, and placed the reverse-shell payload at the
*start* of the pickle stream so it executed before deserialization hit the deliberately
broken tail — evading **picklescan**, the primary open-source pickle scanner. Hugging
Face removed the models within roughly 24 hours, after downloads had already occurred.
[ReversingLabs — Malicious ML models on Hugging Face](https://www.reversinglabs.com/blog/rl-identifies-malware-ml-model-hosted-on-hugging-face)
[The Hacker News (2025-02)](https://thehackernews.com/2025/02/malicious-ml-models-found-on-hugging.html)
This mirrors [Chapter 05](05-measurement-daemon-and-natural-language-shell.md)'s
prompt-injection boundary: content filtering will not catch every malicious artifact,
so the defense has to be format choice plus impact containment, not detection alone.

**The loader is an attack surface independent of the weights.** Two classes matter:

- *Inference-runtime parsers.* `llama.cpp`'s GGUF parser is memory-unsafe C/C++ doing
  insufficient validation on attacker-controlled tensor and metadata fields. Databricks
  (2024) reported multiple memory-corruption bugs where a crafted key/value length
  (e.g. an enormous or negative size) yields an undersized allocation followed by an
  out-of-bounds write — exploitable for code execution merely by loading a crafted GGUF.
  [Databricks — GGML GGUF file-format vulnerabilities](https://www.databricks.com/blog/ggml-gguf-file-format-vulnerabilities)
  This is an ongoing class: **CVE-2025-53630** (High; published 2025-07-10, fixed at
  commit `26a48ad`) is an integer overflow in `gguf_init_from_file_impl` leading to a
  heap out-of-bounds read/write, with follow-on advisories patching bypasses of the
  first fix. [llama.cpp advisory GHSA-vgg9-87g3-85w8](https://github.com/ggml-org/llama.cpp/security/advisories/GHSA-vgg9-87g3-85w8)
- *Model servers.* Ollama's **CVE-2024-37032** ("Probllama", Wiz, disclosed 2024-05-05,
  fixed in 0.1.34 on 2024-05-07, CVSS 8.8) was a path-traversal in digest validation:
  a rogue model registry could drive `/api/pull` to overwrite arbitrary files and reach
  RCE. Wiz found 1,000+ exposed Ollama instances; Docker deployments were worst because
  the API server defaulted to root and bound to all interfaces. [Wiz — Probllama (CVE-2024-37032)](https://www.wiz.io/blog/probllama-ollama-vulnerability-cve-2024-37032)

**Trusting a name is not trusting an artifact.** Palo Alto Unit 42 (2025) documented
**model namespace reuse**: when a Hugging Face author account is deleted, its `author/model`
namespace can be re-registered by anyone, so a pipeline that fetches by name silently
pulls an attacker's replacement. Unit 42 demonstrated reverse-shell RCE this way against
Google Vertex AI Model Garden and Microsoft Azure AI Foundry's catalogs; after the
February 2025 report Google added daily scans for orphaned models. [Unit 42 — Model Namespace Reuse](https://unit42.paloaltonetworks.com/model-namespace-reuse/)
The defensive consequence is direct: **pin by content hash, never by name.**

#### CursiveOS implications

| Threat | Concrete vector | CursiveOS control | Cross-ref |
| --- | --- | --- | --- |
| Pickle deserialization RCE | `.bin`/`.pt`/`.ckpt` executes on `torch.load` | Prefer `safetensors`; refuse pickle on the daemon path | Ch05 risk tiers |
| Scanner evasion | nullifAI-style broken/repacked pickle beats picklescan | Treat scan as advisory, not a gate; rely on format + sandbox | Ch05 injection boundary |
| Loader memory corruption | crafted GGUF → OOB write in `llama.cpp` | Pin runtime versions; run load+inference in the untrusted-code sandbox | Ch10, Ch05 (gVisor/Firecracker) |
| Model-server RCE | Probllama-style path traversal via rogue registry | Pin Ollama version; bind localhost; never root/0.0.0.0 in Docker | Ch10, Ch16 egress rules |
| Namespace/name swap | deleted-account namespace re-registered | Pin model by sha256 digest; record digest in CursiveRoot evidence | Ch11 identity, Ch08 |

Design rules that follow for the organism:

1. **Format over scanning.** Default to `safetensors`/verified GGUF on any path that
   feeds the measurement daemon; do not let a pickle checkpoint load inside the trusted
   process. Scanners (picklescan and successors) are a tripwire, not a boundary.
2. **The loader is untrusted-input code.** GGUF and pickle parsers process
   attacker-controlled bytes, so model load and inference belong in the risk-tiered
   sandbox of [Chapter 05](05-measurement-daemon-and-natural-language-shell.md)
   (gVisor/Firecracker), exactly as for untrusted downloaded code. Pin and track
   `llama.cpp`/Ollama versions against their security advisories — the weights and the
   runtime are separate supply chains.
3. **Pin artifacts by content hash, not by name.** Fetch and verify models by sha256
   digest, and record that digest in the CursiveRoot run evidence. This defeats
   namespace reuse and makes a swapped model *invalidate the run* rather than silently
   poison fitness — extending [Chapter 11](11-hardware-identity-and-anti-spoofing.md)'s
   identity logic from hardware to weights.
4. **Even successful model RCE must not reach measurement truth.** This is the
   [Chapter 06](06-mutation-safety-and-permission-law.md) boundary again: a compromised
   inference process may corrupt a host it is sandboxed on, but it must not hold the
   daemon's write path — it cannot rewrite sensor outputs, mark a bad preset good, or
   submit false CursiveRoot evidence. A model that games its own benchmark is then a
   bounded measurement-quality problem (Ch08 confirmation, the Ch01 immune-sensor
   backlog), not a fleet-wide compromise.

This deepens the single "verify AI model hashes before loading" control into a
characterized surface and maps it onto the daemon/shell split; it does not change the
existing DePIN/package supply-chain guidance below, which remains the authority for
PyPI/dependency and consensus-layer threats.

### GPU memory isolation: shared accelerators as a cross-tenant leakage and measurement-integrity surface

[Chapter 14](14-gpu-and-accelerator-tuning.md) actively recommends **sharing one
physical GPU** across workloads — Single Root I/O Virtualization via
`i915-sriov-dkms` (up to 7 Virtual Functions on consumer Intel Arc), AMD MxGPU/GIM,
and NVIDIA MIG — with the explicit example of "one VF [handling] Plex transcoding
while another handles LLM inference" and "concurrent mining and LLM workloads on a
single physical GPU." That chapter treats multiplexing purely as a throughput and
density win. It never states the security precondition: **co-residency on a GPU is a
trust boundary**, and most consumer-grade sharing mechanisms do *not* enforce memory
isolation across that boundary. This section adds the missing isolation analysis and
maps it onto the CursiveOS daemon/shell split and fleet model. It does not retract
Chapter 14's tuning guidance; it constrains *when* multiplexing is safe.

**LeftoverLocals proves the leak is real for LLM workloads.** In January 2024,
Trail of Bits (Tyler Sorensen) disclosed **LeftoverLocals** (**CVE-2023-4969**): GPUs
that do not clear **local/shared memory** between kernel executions let a second,
co-resident process read whatever a prior process left behind. The proof of concept
is roughly **10 lines of OpenCL**, and the headline demonstration is exactly the
CursiveOS workload — on an **AMD Radeon RX 7900 XT** running `llama.cpp`, an attacker
process recovered on the order of **181 MB per query**, enough to **reconstruct
another user's LLM responses with high accuracy**. Affected vendors per the
coordinated disclosure include **AMD, Apple, Qualcomm, and Imagination**; **NVIDIA and
Arm devices were reported not affected**. Disclosure ran through **CERT/CC (VU#446598)**
from September 2023 to the January 16, 2024 publication, and vendor remediation is
generational — newer parts get driver/firmware fixes while older devices may stay
vulnerable. The structural mitigation is to **clear local memory after use** (or
deploy the vendor patch), which is *not* something an organism gets for free from the
multiplexing knobs Chapter 14 enables.
[Trail of Bits — LeftoverLocals](https://blog.trailofbits.com/2024/01/16/leftoverlocals-listening-to-llm-responses-through-leaked-gpu-local-memory/)
[CERT/CC VU#446598](https://kb.cert.org/vuls/id/446598)
[AMD security bulletin AMD-SB-6010](https://www.amd.com/en/resources/product-security/bulletin/amd-sb-6010.html)
[BleepingComputer — LeftoverLocals](https://www.bleepingcomputer.com/news/security/amd-apple-qualcomm-gpus-leak-ai-data-in-leftoverlocals-attacks/)

**Not all GPU sharing is equal — only hardware partitioning isolates memory.** The
sharing mechanism determines whether co-residency is exploitable at all:

- *NVIDIA MIG (Multi-Instance GPU).* Partitions one GPU into up to seven instances,
  each with **separate, isolated paths through the entire memory system** — on-chip
  crossbar ports, L2 cache banks, memory controllers, and DRAM address buses assigned
  uniquely per instance — giving fault isolation and memory-bandwidth QoS. This is the
  only one of Chapter 14's options that provides a **hardware** memory boundary, and
  it exists only on data-center-class NVIDIA parts.
  [NVIDIA — Multi-Instance GPU](https://www.nvidia.com/en-us/technologies/multi-instance-gpu/)
- *Time-slicing.* Rapidly context-switches the whole GPU between workloads. **No memory
  isolation**; tenants can interfere through memory contention and scheduling delay.
- *MPS (Multi-Process Service).* Runs kernels from multiple processes concurrently in a
  **shared memory space with no fault isolation** — a rogue process can read or corrupt
  another process's GPU memory. Suitable only for *mutually trusting* cooperative
  workloads.
  [Kubenatives — MIG vs Time-Slicing vs MPS](https://www.kubenatives.com/p/mig-vs-time-slicing-vs-mps-which)
  [OpenMetal — MIG vs Time-Slicing](https://openmetal.io/resources/blog/mig-vs-time-slicing-gpu-sharing/)
- *SR-IOV vGPU (the consumer Chapter 14 path).* A vGPU's framebuffer is carved from the
  physical framebuffer at creation and held exclusively until the vGPU is destroyed
  ([NVIDIA vGPU User Guide](https://docs.nvidia.com/vgpu/16.0/grid-vgpu-user-guide/index.html)).
  Framebuffer partitioning is not the same as a guarantee that VRAM is **scrubbed on
  teardown/reallocation**, and the `i915-sriov-dkms` consumer path Chapter 14 relies on
  is community-maintained and unofficial — its cross-VF scrubbing behavior is **not
  documented as a security boundary** [unverified]. Treat consumer SR-IOV partitioning
  as a *resource* mechanism, not an *isolation* guarantee, until proven otherwise on the
  specific hardware.

**GPU isolation failures are a class, not a one-off.** Independently of LeftoverLocals,
**GPU.zip** (IEEE S&P 2024; UT Austin, CMU, UW, UIUC) showed that *software-transparent*
hardware graphical compression leaks pixel data across origins — a cross-origin
SVG-filter pixel-stealing PoC reconstructed a Wikipedia username through Chrome at
**97% accuracy in ~30 min (Ryzen iGPU)** and **98.3% in ~215 min (Intel iGPU)**, with
**all tested GPUs (AMD, Apple, Arm, Intel, Qualcomm iGPUs and one NVIDIA dGPU)
affected** and no vendor patches as of disclosure. GPU.zip is a browser-side side
channel, not a headless-inference leak, so it does **not** directly threaten the
measurement daemon; it is cited only as evidence that GPU microarchitectural state
crosses trust boundaries in more than one way, so "the card is shared but the driver
looks fine" is not a sufficient isolation argument.
[BleepingComputer — GPU.zip](https://www.bleepingcomputer.com/news/security/modern-gpus-vulnerable-to-new-gpuzip-side-channel-attack/)
[GPU.zip project page](https://www.hertzbleed.com/gpu.zip/)

#### CursiveOS implications

For CursiveOS the shared GPU is **two risks at once**, mirroring the supply-chain
section's structure: a **confidentiality** risk (a co-tenant reads another organism's
weights, prompts, or activations from leaked VRAM/local memory) and a
**measurement-integrity** risk (a co-tenant observes or perturbs a benchmark sharing
the card, so a fitness number reflects contention rather than the preset under test —
the Goodhart/[Chapter 08](08-population-confirmation-and-fleet-statistics.md)
confirmation problem and the [Chapter 01](01-seed-organism-and-sensor-array.md)
immune-sensor backlog, arriving through the hardware rather than the optimizer). This
matters most where a contributor runs the harness on a multi-tenant cloud GPU or
co-resides two organisms on one local card — precisely the density scenario Chapter 14
promotes.

| Threat | Concrete vector | CursiveOS control | Cross-ref |
| --- | --- | --- | --- |
| Cross-process VRAM leak | LeftoverLocals (CVE-2023-4969) reads leftover local memory of a co-resident LLM | Sole-tenant GPU during measurement; pin/patch driver; clear-on-free | Ch14 multiplexing, Ch10 runtime |
| No-isolation sharing | Time-slicing/MPS let a rogue tenant read or perturb GPU memory | Forbid untrusted co-tenancy; require MIG hardware partitioning if sharing is unavoidable | Ch14 SR-IOV/MxGPU/MIG |
| Consumer SR-IOV scrub gap | `i915-sriov-dkms` VF teardown scrubbing undocumented [unverified] | Treat as resource split, not isolation; verify per hardware before trusting | Ch14 i915-sriov-dkms |
| Contention-as-noise | Co-tenant load inflates/deflates the measured delta | Record GPU tenancy + isolation mode in run evidence; reject shared-GPU runs for selection | Ch08 confirmation, Ch00 validity |
| Stale driver on fleet | Leak-vulnerable GPU stack on a contributor machine | Flag run for immune sensor; do not pool with patched-fleet data | Ch01 immune sensor, Ch11 identity |

Design rules that follow for the organism:

1. **Measurement runs get sole tenancy, or hardware-partitioned tenancy.** The
   benchmark that writes fitness truth should own the GPU for the duration of the run,
   or run inside a MIG instance with a hardware memory boundary. Co-residing an
   untrusted workload on a time-sliced or MPS-shared card during measurement violates
   both confidentiality and [Chapter 00](00-benchmark-schema-and-measurement-validity.md)
   measurement validity.
2. **GPU sharing mode is part of the fitness key.** Hardware-scoped fitness
   ([Chapter 01](01-seed-organism-and-sensor-array.md)) already keys on hardware; add
   the **tenancy/isolation mode** (sole / MIG / time-sliced / MPS / SR-IOV-VF) to the
   recorded evidence in CursiveRoot. A shared-GPU number is not comparable to a
   sole-tenant number and must not be pooled across the two.
3. **Pin and track the GPU stack against leak-class advisories.** Extend the
   supply-chain section's version-pinning rule from the model runtime to the **GPU
   driver/firmware**: record the driver version, check it against LeftoverLocals-class
   advisories, and flag a run on a vulnerable, unpatched stack for the
   [Chapter 01](01-seed-organism-and-sensor-array.md) immune sensor rather than silently
   trusting it.
4. **A GPU-side leak must still not reach measurement truth.** This is the
   [Chapter 06](06-mutation-safety-and-permission-law.md) boundary once more: even if a
   co-tenant reads or perturbs an organism's GPU memory, it must not hold the daemon's
   write path — it cannot rewrite sensor outputs or submit false CursiveRoot evidence.
   A shared-GPU leak is then a bounded confidentiality + measurement-quality problem
   (handled by sole-tenancy and Ch08 confirmation), not a fleet-wide compromise.

**Retrieval caveats.** LeftoverLocals figures (181 MB/query, RX 7900 XT, ~10 lines of
OpenCL, affected/unaffected vendor list, CVE-2023-4969, CERT/CC VU#446598 timeline) and
the AMD bulletin status were retrieved via web-search summaries of the Trail of Bits
blog, CERT/CC, AMD-SB-6010, and BleepingComputer; the primary Trail of Bits, CERT, and
AMD pages returned HTTP 403 to direct fetch in this pass, so they are **[needs
full-text confirmation]** for any externally quoted artifact. MIG/time-slicing/MPS
isolation properties and the NVIDIA vGPU framebuffer-allocation behavior were retrieved
at vendor-page / summary level. GPU.zip accuracy/timing figures are as the cited
secondary sources state them. None of these results are locally reproduced on CursiveOS
hardware; the consumer `i915-sriov-dkms` scrubbing question is explicitly marked
**[unverified]** and is a candidate for the Chapter 14 GPU capability probe
(`experiments/gpu-accelerator-tuning-validation-plan.md`).

DePIN subnet security: validating trust in decentralized infrastructure

Protecting against malicious submissions in DePIN networks requires addressing threats across four layers: work validation, identity/Sybil resistance, workload sandboxing, and supply chain integrity. Bittensor's $8M PyPi supply chain attack in July 2024 — where a malicious package version stole unencrypted coldkeys — remains the canonical case study, demonstrating that protocol-level security means nothing if the software distribution channel is compromised.  (The Block)  (Mitrade)

DePIN networks use domain-specific Proof of Physical Work (PoPW) mechanisms. Filecoin employs Proof-of-Replication and Proof-of-Spacetime for storage verification.  (Frontiers) Bittensor uses Yuma Consensus where validators independently score miners' AI outputs with stake-weighted consensus determining rewards.  (Gate.com)  (Bittensor) Gensyn's Verde protocol uses optimistic verification with dispute resolution. The 2025 landscape shows convergence toward a modular confidential stack combining Fully Homomorphic Encryption, Zero-Knowledge ML proofs, and Trusted Execution Environments.  (PANews) For practical deployment in the next 3–5 years, TEE-based verification (teeML) via projects like Phala Network, Marlin, and Aizel offers the best balance of security and overhead  (Substack) (less than 30%).

Bittensor's recently deployed Yuma Consensus 3 (YC3) addresses several known attack vectors.  (MEXC) Weight copying attacks — where validators replicate others' publicly visible weights instead of performing independent evaluation — are mitigated by Commit Reveal v4, which uses time-lock encryption to hide weight submissions for configurable tempos.  (Bittensor) The clipping mechanism reduces outlier weight settings exceeding the consensus benchmark.  (MEXC) However, a 2025 arXiv analysis found that "stake strongly predicts earnings while performance scores are only weakly rewarded," suggesting continued opportunities for incentive gaming.  (arXiv)

Sybil resistance in DePIN combines economic, hardware, and reputation barriers. Bittensor requires TAO stake for registration with dynamically fluctuating costs, limits subnets to 256 UIDs  (Bittensor) with competitive deregistration, and uses validator/miner trust scores.  (Bittensor) EdenDID (published 2025 in Springer) introduces the first "trinity-bound" identity system that uniquely binds human user, wallet address, and physical device through edge-based video recognition and computational power verification.  (Springer) IoTeX's DePIN Infrastructure Modules provide hardware attestation for connected devices.

For sandboxing untrusted workloads received from DePIN networks, standard Docker containers are insufficient — shared-kernel isolation is too easily escaped.  (Bunnyshell) Firecracker microVMs represent the gold standard: hardware-enforced isolation via KVM with dedicated kernels per workload, ~125ms boot times, and ~5 MiB memory overhead per VM.  (Northflank)  (Stealthcloud) Used by AWS Lambda  (Stealthcloud) and reportedly approximately 50% of Fortune 500 companies for AI agent workloads.  (Bunnyshell) gVisor provides acceptable isolation for partially-trusted compute-heavy workloads  (Stealthcloud) with 10–30% I/O overhead.  (Northflank) A defense-in-depth architecture layers compute isolation (Firecracker) with strict network egress controls,  (Shayon Mukherjee) resource limits (CPU, memory, disk, time), content-hash verification for binary allow/denylists,  (Bunnyshell) ephemeral execution (destroy sandboxes after use), and anomaly monitoring.  (Stealthcloud)

TEE technology offers hardware-rooted trust but is not invulnerable. Phala Network leads with 30,000+ deployed TEE devices  (Phala) and GPU TEE integration via NVIDIA Confidential Compute. However, Georgia Tech and Purdue researchers demonstrated TEE.Fail in 2025 — a practical DDR5 memory-bus interposition attack (costing under $1,000) that extracted ECDSA private keys from SGX enclaves, forged TDX attestations, and broke NVIDIA Confidential Computing attestation.  (Bleeping Computer)  (CyberSecureFox) The attack requires physical hardware access, making it material in colocation facilities and supply chain scenarios.  (CyberSecureFox) TEEs should be treated as one layer of defense-in-depth, not a sole trust anchor.

Supply chain protection demands multiple controls: verify all package checksums and signatures before installation (the Bittensor PyPi attack exploited unverified packages),  (Mitrade) pin exact dependency versions with lockfiles, build from source when possible, use Sigstore/cosign for container image verification, verify AI model hashes before loading, and never perform key decryption in environments with network access to untrusted code. Bittensor's coldkey/hotkey architecture (coldkeys hold funds offline, hotkeys handle daily operations) with proxy wallets introduced in 2025 provides economic compartmentalization — combined with the new announce-and-execute coldkey swap workflow with mandatory delays, unauthorized fund movement becomes significantly harder.  (Bittensor)

Conclusion: a unified hardening posture for 2026

The security landscape for mining and AI infrastructure has matured significantly. Three developments define the 2025–2026 era. First, LKRG 1.0.0 and OpenPaX bring kernel runtime protection to production without grsecurity's commercial licensing, closing a long-standing gap for operators who need exploit detection without subscription fees.  (Linux Journal) Second, CrowdSec's collaborative threat intelligence model has displaced Fail2ban as the recommended brute-force protection, offering community-sourced IP reputation that individual-server tools cannot match.  (AZDIGI) Third, DePIN security has moved beyond protocol design into practical operational concerns — the Bittensor supply chain attack proved that $8M can be lost not through consensus manipulation but through a single malicious package upload.  (The Block)  (Rivanorth)

The key architectural insight is that mining and AI servers occupy an unusual threat position: they must maintain high-performance access to GPUs and network resources while defending against adversaries who are financially motivated and technically sophisticated. Every hardening decision involves a performance trade-off. Kernel lockdown with MOK-signed NVIDIA modules, seccomp profiles that permit JIT compilation, and firewall egress rules that whitelist specific pool IPs represent the careful balance required. The operators who will lose funds in 2026 are those treating security as a checkbox rather than a continuously monitored, layered architecture spanning kernel through consensus.
