# Chapter 06 Selected Sources

Date extracted: 2026-05-26  
Agent / reviewer: GPT-5.5 Thinking / ChatGPT  
Chapter: `chapters/06-security-and-hardening.md`  
Status: Selected high-priority extraction only. Full works-cited extraction remains open.

## Purpose

This file captures the first selected source extraction for Chapter 06. Security guidance ages quickly, so every source in this chapter should be rechecked before it becomes operational policy.

## Selected Sources

| Source ID | Title | Author / Organization | URL / DOI / Repo | Source Type | Date Published / Updated | Date Accessed | Used In | Claims Supported | Reliability Tier | Validation Status | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-06-001 | Kernel Self-Protection Project: Recommended Settings | KSPP / Linux kernel community | https://kernsec.org/wiki/index.php/Kernel_Self_Protection_Project/Recommended_Settings | primary/community kernel hardening guidance | rolling | 2026-05-26 | Kernel sysctl and boot hardening section | Supports kernel hardening concepts such as pointer restrictions, dmesg restrictions, module restrictions, slab/usercopy/hardening options, lockdown-style controls | A/B | needs verification | Good source for hardening intent; distro support and performance impact must be checked per host. |
| SRC-06-002 | Linux Kernel sysctl documentation | Linux Kernel Documentation | https://docs.kernel.org/admin-guide/sysctl/kernel.html | primary documentation | rolling | 2026-05-26 | Sysctl hardening section | Documents many kernel sysctls such as dmesg restrictions, module behavior, ptrace restrictions, panic/sysrq behavior | A | needs verification | Use exact sysctl docs for each parameter before making a preset. |
| SRC-06-003 | nftables wiki / documentation | nftables project | https://wiki.nftables.org/wiki-nftables/index.php/Main_Page | project documentation | rolling | 2026-05-26 | Firewall architecture section | Supports nftables concepts such as tables, chains, sets, maps, atomic ruleset management, IPv4/IPv6 unification | A/B | needs verification | Validates nftables as a modern firewall framework, not every performance claim or rate-limit recipe. |
| SRC-06-004 | Red Hat: Getting started with nftables | Red Hat Documentation | https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/8/html/securing_networks/getting-started-with-nftables_securing-networks | vendor docs | RHEL 8 docs | 2026-05-26 | Firewall architecture section | Supports default-drop firewall design, nftables usage, and enterprise distro guidance | A | needs verification | Good operational baseline for RHEL-like systems. |
| SRC-06-005 | Yubico: Securing SSH with FIDO2 | Yubico | https://developers.yubico.com/SSH/Securing_SSH_with_FIDO2.html | vendor docs | rolling | 2026-05-26 | SSH access-control section | Supports OpenSSH FIDO2 security-key authentication with hardware-backed keys | A/B | needs verification | Good source for YubiKey/FIDO2 flow; should be paired with OpenSSH manpages. |
| SRC-06-006 | OpenSSH manual pages | OpenBSD / OpenSSH | https://man.openbsd.org/ssh-keygen | primary documentation | rolling | 2026-05-26 | SSH access-control section | Documents SSH key generation, certificate signing, and security-key options | A | needs verification | Primary source for exact OpenSSH options. |
| SRC-06-007 | Wazuh Documentation | Wazuh | https://documentation.wazuh.com/current/index.html | project documentation | rolling | 2026-05-26 | Intrusion detection section | Supports Wazuh as endpoint/security monitoring platform with FIM, rules, active response, and centralized detection | A/B | needs verification | Validate resource overhead claims separately. |
| SRC-06-008 | Suricata Documentation | OISF / Suricata | https://docs.suricata.io/ | project documentation | rolling | 2026-05-26 | Network IDS section | Supports Suricata as network IDS/IPS with EVE JSON logging and rules | A/B | needs verification | Good source for capability, not custom mining rule effectiveness. |
| SRC-06-009 | Falco Documentation | CNCF / Falco | https://falco.org/docs/ | project documentation | rolling | 2026-05-26 | Runtime detection section | Supports Falco runtime detection using kernel events/eBPF and custom rules | A/B | needs verification | Validate performance overhead and production deployment mode per host. |
| SRC-06-010 | Firecracker Documentation | Firecracker project / AWS | https://firecracker-microvm.github.io/ | project documentation | rolling | 2026-05-26 | DePIN sandboxing section | Supports Firecracker microVM isolation and lightweight virtual machine model | A/B | needs verification | Exact boot-time and memory-overhead numbers must be checked against current docs/benchmarks. |
| SRC-06-011 | gVisor Documentation | Google / gVisor project | https://gvisor.dev/docs/ | project documentation | rolling | 2026-05-26 | Workload sandboxing section | Supports gVisor as a container sandbox/runtime providing an application-kernel boundary | A/B | needs verification | Performance overhead depends heavily on syscall/I/O pattern. |
| SRC-06-012 | Bittensor exploit reporting | The Block / Bittensor ecosystem | https://www.theblock.co/post/303547/bittensor-exploit | news/reporting | 2024-07 | 2026-05-26 | DePIN supply-chain section | Supports Bittensor/PyPI supply-chain incident as a case study | C | needs verification | Need official postmortem or project statement if available; news source is useful but not enough for root-cause claims. |
| SRC-06-013 | Sigstore Cosign Documentation | Sigstore | https://docs.sigstore.dev/cosign/overview/ | project documentation | rolling | 2026-05-26 | Supply-chain protection section | Supports container/image signing and verification with cosign | A/B | needs verification | Useful for supply-chain guidance. |
| SRC-06-014 | TEE.Fail research | Academic/security researchers | https://teefail.github.io/ | research project | 2025 | 2026-05-26 | TEE caveats section | Supports claim that TEEs can be attacked and should not be sole trust anchor | B | needs verification | Verify against paper and vendor responses before making strong operational claims. |

## Extraction Caveats

- Several Chapter 06 sources are blogs, vendor marketing, or news articles. These should be demoted unless corroborated by primary documentation, official postmortems, or reproducible tests.
- Security claims should include freshness dates because recommendations can change quickly.
- Operational firewall and SSH settings should be validated against the exact distro, network topology, and access model before deployment.
