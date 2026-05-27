# Security Hardening Validation Plan

Date created: 2026-05-26
Linked chapter: `chapters/06-security-and-hardening.md`
Status: Proposed validation plan; not yet executed.

## Purpose

Validate Chapter 06's security guidance before converting any recommendations into CursiveOS deployment policy. Security advice must be current, distro-aware, workload-aware, and tested against the specific mutation depth CursiveOS allows.

## Core Principle

CursiveOS security must scale with mutation depth.

A system that only edits service config needs one security model. A system that can change sysfs, scheduler policies, GPU runtime controls, firmware settings, or run untrusted DePIN workloads needs a much stricter model.

## Policy Tiers

| Tier | Use Case | Minimum Controls |
| --- | --- | --- |
| Baseline | Single trusted home-lab node | SSH keys, firewall default deny, local-only model APIs, update discipline, basic logs |
| Hardened | Internet-reachable management or multi-node rack | FIDO2/SSH certs, nftables egress policy, Wazuh/Falco/Suricata where appropriate, signed artifacts, host inventory |
| High-assurance | DePIN/mining revenue, untrusted jobs, remote agents | microVM/gVisor isolation, strict egress, file/model hash verification, immutable logs, policy-gated mutations |
| Lab-only | Kernel/eBPF/GPU/firmware mutation research | isolated network, out-of-band recovery, sacrificial hardware, explicit rollback plan |

## Validation Tracks

### 1. Exposed Surface Inventory

Capture:

```text
open_listening_ports
publicly_reachable_services
ssh_config_summary
model_api_bind_addresses
firewall_default_policy
outbound_destinations
running_containers_or_vms
loaded_kernel_modules
active_LSMs
secure_boot_state
installed_agent_tools
```

### 2. SSH Access Validation

Validate:

- password login disabled where appropriate;
- root login disabled or restricted;
- FIDO2-backed keys tested for admin accounts;
- backup access path exists;
- SSH certificate flow tested for fleets;
- bastion/ProxyJump flow documented where used.

### 3. Firewall and Egress Validation

Test:

- default-drop ingress;
- only expected management ingress allowed;
- AI inference APIs are not public unless explicitly authenticated and intended;
- egress rules match actual workload needs;
- DNS/IP allowlist behavior is stable enough for the deployment;
- emergency access is not accidentally blocked.

### 4. Monitoring and Detection Validation

Evaluate Wazuh, Suricata, Falco, AIDE/osquery, Loki/Prometheus/Grafana, or equivalent stack according to deployment tier.

Metrics:

```text
CPU_overhead
RAM_overhead
storage_growth_per_day
alert_volume
false_positive_rate
missed_detection_rate_if_tested
mean_time_to_alert
operator_action_required
```

### 5. Sandbox Isolation Validation

Classify workloads:

| Workload Type | Suggested Isolation |
| --- | --- |
| trusted local service | service user + systemd sandboxing |
| trusted containerized tool | hardened container |
| semi-trusted agent tool | gVisor/Kata/container sandbox with tight policy |
| untrusted DePIN job | Firecracker or equivalent microVM |
| kernel/GPU/firmware mutation test | isolated lab host only |

Validate that isolation matches risk before deployment.

### 6. Supply-Chain Validation

Require evidence for:

```text
package_source
package_signature_or_hash
container_image_digest
model_file_hash
model_source_url
lockfile_present
dependency_update_policy
artifact_signing_policy
```

Model files should never be treated as opaque trusted blobs without source and hash tracking.

### 7. Agent-Action Audit and Rollback

Every privileged agent action should record:

```text
action_id
agent_identity
user_or_policy_approval
command_or_mutation
before_state
after_state
rollback_method
result
logs
fitness_or_security_check
```

## Promotion Rules

A Chapter 06 recommendation can become CursiveOS policy only if:

- source-backed by primary or strong documentation;
- tested on the target distro/kernel/deployment type;
- performance overhead is measured when relevant;
- failure and lockout cases are tested;
- rollback or break-glass access is documented;
- the validation ledger is updated.

## Immediate CursiveOS Security Baseline

Recommended starting baseline:

1. Model and agent APIs bind to localhost by default.
2. SSH uses keys, no passwords.
3. Firewall defaults to deny inbound.
4. Privileged mutations require an allowlist and logging.
5. Untrusted jobs do not run directly on the host.
6. Model files and containers are hashed before execution/use.
7. Benchmark and mutation artifacts are tied to host and firmware state.

## Follow-up

Create a future `security/cursiveos-hardening-baseline.md` that turns validated recommendations into tiered implementation profiles.
