# Validation Note: Chapter 06 Security and Hardening

Date checked: 2026-05-26
Agent / reviewer: GPT-5.5 Thinking / ChatGPT
Scope: targeted validation of highest-impact Chapter 06 claims
Status: partially verified, with safety-critical caveats
Source IDs: SRC-06-001 through SRC-06-014 in `sources/chapter-06-selected-sources.md`

## Summary

Chapter 06 has the right strategic instinct: CursiveOS systems that control GPUs, local agents, firmware, kernels, and DePIN/mining workloads need defense-in-depth. The broad categories are well chosen: kernel hardening, firewalling, SSH access control, monitoring/IDS, sandboxing, supply-chain protection, and DePIN trust validation.

However, the chapter is currently too confident in several places. Security guidance must be treated as deployment-specific and date-sensitive. Some claims rely on blogs, vendor marketing, or news reporting. The chapter should be rewritten around policy tiers and validation gates rather than one universal hardening recipe.

## Claims Checked

| Claim ID | Claim | Status | Evidence | Notes / Required Rewrite |
| --- | --- | --- | --- | --- |
| CL-06-001 | Kernel hardening sysctls and boot flags are important for exposed GPU/AI/mining nodes. | supported as direction | SRC-06-001, SRC-06-002 | Specific flags must be tested per distro/kernel/driver. Do not ship one universal preset. |
| CL-06-002 | `kernel.modules_disabled=1` is a strong post-boot hardening measure. | supported with caveat | SRC-06-002 | Good for locked-down nodes after all modules are loaded; dangerous for machines needing DKMS/GPU driver reloads or dynamic hardware. |
| CL-06-003 | `module.sig_enforce=1` plus MOK-signed DKMS modules is suitable for GPU nodes. | partially supported | SRC-06-001; distro-specific docs pending | Concept is sound but operationally fragile. Needs distro and driver validation. |
| CL-06-004 | nftables is the preferred modern Linux firewall framework. | supported | SRC-06-003, SRC-06-004 | Supported, but `iptables-nft` compatibility and distro defaults vary. |
| CL-06-005 | Strict egress allowlisting is valuable for mining/AI servers. | supported with operational caveat | SRC-06-003, SRC-06-004 | Good principle, but allowlisting pool IPs by cron DNS resolution is fragile. Prefer controlled DNS, proxying, explicit endpoint management, or service-specific egress policy where possible. |
| CL-06-006 | AI inference ports such as local model APIs should not be exposed publicly without authentication. | supported | general security principle; source index needs API-specific docs | Strong policy. Keep. |
| CL-06-007 | CrowdSec has categorically displaced Fail2ban. | overbroad / preference, not fact | source extraction still pending | CrowdSec is useful, but this should be phrased as a candidate/recommendation, not an industry fact. Fail2ban remains viable in simpler deployments. |
| CL-06-008 | FIDO2-backed SSH keys are a high-security option. | supported | SRC-06-005, SRC-06-006 | Hardware-backed SSH keys are appropriate for admin access. Keep with backup-key/fallback guidance. |
| CL-06-009 | SSH certificates are valuable for fleets. | supported | SRC-06-006 | Good recommendation for multi-host fleets. Need operational CA plan. |
| CL-06-010 | SPA/fwknop makes SSH zero-day exploitation impossible. | overbroad / unsafe wording | source extraction pending | SPA can hide a service from unauthenticated scanners, but it does not make zero-day exploitation impossible. Rewrite. |
| CL-06-011 | Wazuh, Suricata, Falco, and file integrity monitoring are relevant to mining/AI nodes. | supported as architecture | SRC-06-007, SRC-06-008, SRC-06-009 | Good layered monitoring stack, but overhead and operational complexity need deployment testing. |
| CL-06-012 | Docker containers are insufficient for untrusted DePIN workloads. | partially supported but needs nuance | SRC-06-010, SRC-06-011 | Shared-kernel containers are weaker than microVMs, but hardened containers can still be acceptable for trusted/low-risk tasks. Use risk tiers. |
| CL-06-013 | Firecracker/gVisor are strong sandbox candidates. | supported | SRC-06-010, SRC-06-011 | Good candidates. Exact overhead, boot time, and compatibility must be tested. |
| CL-06-014 | TEEs are useful but not sufficient as a sole trust anchor. | supported | SRC-06-014 | Keep. This is strategically important for CursiveOS/DePIN trust. |
| CL-06-015 | Supply-chain controls such as lockfiles, signatures, hashes, and model verification are required. | supported | SRC-06-012, SRC-06-013 | Strong CursiveOS policy direction. Need implementable checklist. |

## Required Corpus Changes

### Recommended Chapter 06 wording changes

- Replace absolute claims with policy levels: baseline, hardened, high-assurance, lab-only.
- Replace “CrowdSec has displaced Fail2ban” with “CrowdSec is a strong candidate for collaborative brute-force and reputation-based blocking; Fail2ban remains acceptable for simple hosts.”
- Replace “fwknop makes zero-day exploitation impossible” with “SPA can hide SSH from unauthenticated scanners and reduce exposed attack surface, but must not be treated as a complete defense.”
- Replace “Docker is insufficient” with “shared-kernel containers are not sufficient for untrusted arbitrary workloads; trusted/low-risk workloads may use hardened containers, while untrusted DePIN workloads should use microVM or stronger isolation.”
- Add explicit performance testing for kernel hardening, LSM, seccomp, and monitoring overhead.
- Add a CursiveOS-specific supply-chain section for model hashes, tool permissions, agent action logs, and signed benchmark artifacts.

## Implications for CursiveOS

CursiveOS needs a security model that matches mutation depth:

| Mutation Layer | Minimum Security Model |
| --- | --- |
| userspace/service settings | allowlist, rollback, logging |
| sysctl/sysfs tuning | root mediation, schema validation, before/after state capture |
| GPU power/runtime tuning | device-specific allowlist, telemetry, crash recovery |
| kernel/scheduler/eBPF | signed/allowlisted artifacts, verifier checks, isolated test host first |
| firmware/BIOS/BMC | out-of-band recovery, staged changes, human or policy approval gates |
| untrusted DePIN work | microVM or stronger sandbox, network egress controls, ephemeral state |

## Suggested Security Validation Plan

Create `experiments/security-hardening-validation-plan.md` with tests for:

1. Baseline exposed-surface inventory.
2. SSH/FIDO2/certificate access flow.
3. Firewall ingress/egress policy validation.
4. Container vs microVM sandbox isolation decision tree.
5. Monitoring stack overhead and signal quality.
6. Supply-chain verification for packages, containers, and model files.
7. Agent-action audit logs and rollback enforcement.

## Follow-up

- Extract all Chapter 06 sources into canonical source index or keep this selected file until merged.
- Add official docs for OpenSSH, nftables, Wazuh, Suricata, Falco, Firecracker, gVisor, Sigstore, and Bittensor postmortems where available.
- Build a CursiveOS-specific hardening baseline instead of importing generic Linux hardening wholesale.
- Revisit Chapter 06 after the first local-agent deployment architecture is known.
