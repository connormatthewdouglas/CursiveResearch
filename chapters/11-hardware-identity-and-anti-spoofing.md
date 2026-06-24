## Corpus status (living layer)

**Last reconciled:** 2026-06-24
**Confidence:** Partly Supported — fingerprint v2 in production; SMBIOS/PCI stability **Supported** in literature; immune-sensor enforcement **Unvalidated**
**Read with:** [Chapter 01](01-seed-organism-and-sensor-array.md) (independence, immune sensors), [Chapter 08](08-population-confirmation-and-fleet-statistics.md) (effective N), [Chapter 02](02-bitcoin-native-economics-and-proof-of-useful-optimization.md) (wallet independence), [Chapter 16](16-security-and-hardening.md) (host hardening)

### Authoritative for

- Hardware fingerprint signal inventory and spoofing surface
- Population-confirmation independence requirements
- What CursiveRoot can trust without TEE attestation

### Superseded or narrowed

- TEE/bus attestation as sole oracle (Ch02 **Disproven** for operator physical-access model)
- SMBIOS alone as strong identity — spoofable in VMs and via firmware tools

### Open until experiment/hardware

- Immune-sensor correlation graph on live fleet
- TPM-backed fingerprint extension experiment (pipeline backlog)
- GPU VBIOS version stability across driver updates

---


## Reinforced research (2026-06-24)

- Corpus reorganized to strategic order 00-22; see [INDEX.md](../INDEX.md).
- Paper library: **25** peer intakes in papers/ (extraction-only unless rights-cleared).
- Credible external sources: Linux kernel docs, arXiv 2024-2026 preprints, DMTF/UEFI/Red Hat/ESnet where applicable â€” details in chapter body and sources/.

# Hardware Identity and Anti-Spoofing

Status: First research-synthesis pass (2026-06-24). Catalogs identity signals
(SMBIOS/DMI, PCI IDs, GPU VBIOS, TPM, kernel/microcode) for CursiveRoot
fingerprinting, maps spoofing attacks, and ties identity to population
confirmation (Chapters 01, 18).
Use it for: designing fingerprint v2+, immune sensors, and Sybil-resistant
tester independence without governance votes.

## Why this chapter exists

Chapter 01 requires **distinct hardware fingerprints** for independent
confirmations — alongside distinct wallets and anomaly profiles. Chapter 00 shows
fingerprint v2 (CPU model, board, GPU PCI IDs) already keys `machines` and
`machine_aliases` in CursiveRoot. The corpus lacked a dedicated treatment of
which signals are stable, which are spoofable, and how immune sensors should
react when identity is plausible but behavior is correlated.

## 1. Identity goals in CursiveOS

| Goal | Not the goal |
| --- | --- |
| Stable machine key across kernel updates | global KYC |
| Detect clone farms and VM sprawl | fingerprint as moral identity |
| Scope fitness to hardware class | unspoofable proof without cost |
| Feed population confirmation independence | TEE-gated oracle |

| Claim | Status |
| --- | --- |
| Fingerprint is for statistical independence, not legal identity | **Supported** (Ch01/11) |
| Perfect anti-Sybil without economics is impossible | **Supported** |
| Layered signals beat any single field | **Supported** |

## 2. Signal inventory

### 2.1 SMBIOS / DMI (firmware tables)

SMBIOS (System Management BIOS) exposes manufacturer, product, serial, UUID,
board asset tag, chassis type via ACPI tables read by the kernel and userspace
tools (`dmidecode`, `/sys/class/dmi/id/*`).

| Field | Stability | Spoofability |
| --- | --- | --- |
| `system-uuid` | high on bare metal | VM templates clone; editable in QEMU/VMware |
| `product-name` / `board-name` | high | nested ESXi customization ([William Lam, 2024](https://williamlam.com/2024/05/customizing-smbios-strings-hardware-manufacturer-and-vendor-for-nested-esxi.html)) |
| `serial-number` | medium | `dmidecode` kernel interfaces patched/overridden ([Schlomo, 2023](https://schlomo.schapiro.org/2023/01/overriding-patching-linux-system-serial.html)) |
| BIOS version/date | medium | flash updates change; may match fleet images |

DMTF SMBIOS specification remains the normative reference for field semantics
([DMTF SMBIOS](https://www.dmtf.org/standards/smbios)).

| Claim | Status |
| --- | --- |
| SMBIOS useful for coarse hardware class | **Supported** |
| SMBIOS sufficient alone for Sybil resistance | **Disproven** |
| `/sys/class/dmi/id` matches dmidecode on bare metal | **Supported** with OEM quirks |

### 2.2 CPU identity

| Signal | Source | Notes |
| --- | --- | --- |
| Model name | `/proc/cpuinfo`, CPUID | stable until CPU swap |
| Microcode revision | `/sys/devices/system/cpu/cpu0/microcode/version` | Ch01 cites microcode in fingerprint |
| Core count / cache topology | sysfs | VM may hide host topology |

| Claim | Status |
| --- | --- |
| Microcode in fingerprint helps detect post-boot updates | **Supported** |
| CPUID-level spoofing in VMs common | **Supported** |

### 2.3 GPU — PCI IDs and VBIOS

| Signal | Source | Notes |
| --- | --- | --- |
| PCI vendor:device | `lspci -nn`, sysfs | strong for dGPU class (e.g. Arc 8086:56a0) |
| Subsystem IDs | PCI config | board partner variation |
| VBIOS version | `nvidia-smi`, Intel tools, sysfs where exposed | Ch01 immune context |
| Driver binding | `drm`, `i915`, `xe` | changes with distro, not card swap |

Chapter 00 founder rig: Ryzen 7 5700 + Arc A750 fingerprint `3e6b165ddf112a75`;
laptop i5-11300H `42e7c7257af11f46` — empirically separable classes.

| Claim | Status |
| --- | --- |
| PCI IDs stable for fingerprint v2 | **Supported** (production schema) |
| GPU VBIOS in fingerprint spec | **Supported** (Ch01); logging **Unvalidated** fleet-wide |
| Same PCI ID ⇒ same performance class | **Unvalidated** (VRAM bins, power limits differ) |

### 2.4 TPM and measured boot (optional hardening)

TPM 2.0 provides device-unique endorsement key (EK) and PCR quotes over boot
state. Useful as **additive** cost to Sybil, not Phase 0 requirement.

| Approach | Benefit | Limitation |
| --- | --- | --- |
| TPM EK hash in fingerprint | raises clone cost | VMs may use virtual TPM; privacy concerns |
| PCR policy | detects boot chain tamper | drifts with kernel updates |
| Remote attestation | strong integrity | operator threat model ≠ cloud tenant (Ch02) |

| Claim | Status |
| --- | --- |
| TPM optional for CursiveOS Phase 0 | **Supported** (Ch02 living layer) |
| TPM replaces population confirmation | **Disproven** |
| TPM + fingerprint reduces VM farm ease | **Supported** as defense-in-depth |

### 2.5 Kernel, distro, and software surface

| Signal | Role |
| --- | --- |
| `uname -r` | drift tracking; alias mapping in CursiveRoot |
| Distro ID + version | preset compatibility |
| CursiveOS preset version | phenotype, not genotype |
| Sensor suite version | measurement comparability |

Fingerprint v2 intentionally **survives kernel updates** via `machine_aliases`
(Ch00) — identity is hardware-anchored, not kernel-anchored.

## 3. Fingerprint construction (v2 and beyond)

Current v2 (from production notes): hash over CPU model, board, GPU PCI ids.

Proposed v3 layers:

```text
hardware_core = hash(cpu_model, board_product, gpu_pci_ids, system_uuid?)
firmware_layer = hash(bios_version, gpu_vbios?, microcode)
trust_layer = optional(tpm_ek_pub_hash)
behavior_layer = NOT in fingerprint — immune sensors only
```

| Claim | Status |
| --- | --- |
| v2 separates founder desktop vs laptop | **Validated** |
| Adding UUID improves uniqueness | **Supported**; **Unvalidated** spoof resistance |
| behavior in fingerprint causes churn | **Supported** design rule |

## 4. Spoofing attack catalog

| Attack | Mechanism | Detection angle |
| --- | --- | --- |
| VM fleet | cloned SMBIOS + PCI passthrough | UUID collision, timing, hypervisor CPU flags, missing OEM quirks |
| SMBIOS editor | `SmbiosChanger`-class tools | inconsistent DMI vs ACPI vs EFI |
| GPU passthrough fraud | consumer GPU in cloud slice | thermal/power telemetry mismatch |
| Kernel patch | override DMI sysfs | integrity monitoring; outlier vs physical class |
| Wallet splitting | many wallets, one host | payout graph + timing correlation |
| Measurement replay | submit old JSON | signed bundles, nonces, hub attestation of run logs |

Open-source SMBIOS mutation tools exist ([Acrozi/SmbiosChanger](https://github.com/Acrozi/SmbiosChanger)) — treat DMI as **hint**, not proof.

| Claim | Status |
| --- | --- |
| Immune sensors required for determined adversary | **Supported** (Ch01) |
| Fingerprint-only stops casual duplication | **Supported** |
| Economic cost (BTC payouts, Fast tier) adds Sybil friction | **Supported** (Ch02) |

## 5. Population confirmation linkage

Chapter 18: independent confirmations require distinct fingerprints **and**
wallets **and** anomaly profiles. Hardware identity feeds:

| Stage | Identity use |
| --- | --- |
| Registration | assign `machine_id`, alias on kernel bump |
| Confirmation counting | reject same `hardware_core` as second independent N |
| Hardware-scoped fitness | cluster by `hardware_core` + performance covariance |
| Immune downgrade | correlated deltas across "distinct" cores → effective N − k |

| Claim | Status |
| --- | --- |
| Same fingerprint cannot count twice toward N | **Supported** (spec) |
| Distinct fingerprints with correlated anomalies collapse | **Unvalidated** (immune sensors planned) |
| Wallet independence without hardware independence insufficient | **Supported** |

## 6. Stability vs privacy

Operators may resist raw serial upload. Fingerprinting should use **hashed**
stable fields with minimal reversible PII.

| Practice | Rationale |
| --- | --- |
| Publish `hardware_fingerprint_hash` only | Ch01 open-data stance |
| No disk serials in default fingerprint | privacy + swap noise |
| Opt-in TPM enhancement | advanced testers |

| Claim | Status |
| --- | --- |
| Hashed fingerprint in CursiveRoot | **Supported** (Ch01) |
| Re-identification from hash alone low risk for coarse fields | **Partly Supported** |

## 7. Linux tooling reference

| Tool | Reads |
| --- | --- |
| `dmidecode` | SMBIOS tables |
| `/sys/class/dmi/id/*` | kernel-exposed DMI |
| `lspci -nn` | PCI IDs |
| `readlink /sys/class/drm/card*/device` | GPU topology |
| `tpm2_getcap` / `tpm2_readpublic` | TPM EK (if present) |

Cloud instance detection heuristics (systemd `systemd-detect-virt`, hypervisor
flags) belong in **immune sensors**, not genesis fingerprint, to avoid false
exclusion of legitimate VMs used for testing — unless policy later forbids VMs.

## 8. CursiveOS implications

1. **Keep v2** for Phase 0; design v3 with optional UUID + microcode + VBIOS in detail bundle.
2. **Immune sensor: DMI consistency check** — cross-validate dmidecode vs sysfs.
3. **Immune sensor: confirmation graph** — flag wallets sharing hardware_core timing patterns.
4. **Do not** rely on TEE attestation for operator-hosted rigs (Ch02).
5. **Record** `virt_detected` label separately; let policy decide eligibility.
6. **Hardware-scoped promotion** uses fingerprint cluster, not marketing "works everywhere."

## 9. Open research gaps

1. Quantify VM spoof success rate against v2/v3 fingerprints in red-team exercise.
2. GPU VBIOS collection daemon for Intel/NVIDIA/AMD uniformly.
3. TPM opt-in pilot — privacy review + support burden.
4. Correlate SMBIOS class with Ch00 performance clusters (automatic taxonomy).
5. Immune-sensor false-positive budget when downgrading effective N.
6. Cross-check wallet graph with Lightning/BTC payout reuse (Ch02 integration).

## 10. Citations

| Source | Contribution |
| --- | --- |
| DMTF SMBIOS specification | field semantics |
| Chapter 01 sensor-array | independence, immune families |
| Chapter 00 machines schema | fingerprint v2 in production |
| Chapter 18 | effective confirmations |
| Schlomo (2023) DMI override | spoofing surface |
| William Lam (2024) nested ESXi SMBIOS | virtualization customization |
| Linux `dmidecode(8)`, `lspci(8)` | operational inventory |

## Research questions answered

| Question | Answer |
| --- | --- |
| What is hardware fingerprint for? | Independence + hardware-scoped fitness, not KYC |
| Is SMBIOS trustworthy? | Useful, spoofable — layer other signals |
| Are PCI GPU IDs enough? | Good class anchor; add microcode/VBIOS for v3 |
| Does this replace population stats? | No — complements Ch08 confirmation math |