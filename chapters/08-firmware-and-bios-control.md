# Firmware and BIOS Control

Original research note authored from CursiveOS design discussion on 2026-05-26.

Status: Original synthesis; requires platform validation. This chapter is not a DOCX import. It should be treated as a working research chapter until individual claims are verified on target hardware.

## 1. Executive Summary

The recent CursiveOS architecture revelation is simple but important: a truly self-optimizing compute system cannot stop at userspace, services, sysctl, drivers, and kernel parameters. Some of the highest-leverage performance and reliability decisions are made before the operating system exists. Firmware initializes DRAM, enumerates PCIe, exposes CPU and device capabilities, configures Secure Boot state, defines boot targets, constructs ACPI/SMBIOS/UEFI tables, and decides which hardware topology Linux receives.

Therefore, CursiveOS should eventually include a firmware control layer. The correct design is not an agent blindly opening BIOS menus. The correct design is a controlled subsystem, here named `CursiveFirmware`, that can discover firmware capabilities, stage firmware mutations, reboot into a trial state, measure the result, and record the outcome in CursiveRoot.

The core conclusion:

> The OS is not the full organism. The machine is the organism. Linux is the cortex; firmware is the developmental layer; the BMC or external controller is the autonomic nervous system; CursiveRoot is memory; benchmarks are fitness signals.

## 2. Why BIOS/UEFI Control Matters

CursiveOS currently focuses on OS-visible optimization: sysctl, kernel boot parameters, GPU sysfs controls, scheduler selection, networking, memory pressure, and reversible benchmarked presets. That layer is necessary, but it is not the deepest control surface.

Firmware-level settings can determine:

- memory speed, timings, ECC behavior, and training results;
- PCIe bifurcation, link width, device enumeration, and MMIO aperture sizing;
- Resizable BAR and above-4G decoding behavior;
- virtualization exposure, IOMMU behavior, SR-IOV readiness, and TPM/Secure Boot state;
- boot target, boot order, one-time rescue boot, and firmware setup entry;
- CPU C-state policy, turbo behavior, package power policy, and fan/thermal defaults on some platforms;
- GPU and accelerator visibility before the kernel driver loads.

If CursiveOS is meant to optimize the whole compute organism, firmware is not optional. It is simply a deeper, slower, riskier mutation layer.

## 3. Control Surfaces Available From Linux or Adjacent Control Planes

### 3.1 UEFI Runtime Variables

Modern systems generally use UEFI rather than legacy BIOS. UEFI exposes runtime services, including variable services, that remain accessible after the OS has booted. Linux exposes UEFI variables through `efivarfs`, typically mounted at `/sys/firmware/efi/efivars`. The Linux kernel documentation states that variables can be created, deleted, and modified with `efivarfs`, while also warning that non-standard variable deletion can trigger firmware bugs severe enough to prevent POST on some machines. [Linux efivarfs documentation](https://docs.kernel.org/filesystems/efivarfs.html)

This gives CursiveOS a real first control surface:

```bash
mount -t efivarfs none /sys/firmware/efi/efivars
ls /sys/firmware/efi/efivars
```

Useful scope:

- read platform UEFI variables;
- inspect boot-related state;
- stage or modify standard variables where supported;
- integrate with bootloader tools such as `efibootmgr`;
- support next-boot and rescue-boot workflows.

Limitations:

- UEFI variables are not equivalent to arbitrary BIOS menu settings;
- many vendor settings are hidden behind proprietary interfaces;
- some variables are authenticated, immutable, or locked by firmware policy;
- incorrect writes can break boot behavior.

### 3.2 Linux `firmware-attributes` Sysfs Interface

Linux includes a `firmware-attributes` sysfs interface designed for systems management software to configure firmware options on supported systems. The kernel ABI documentation describes `/sys/class/firmware-attributes/*/attributes/*/` as a way to expose configuration options, including attribute type, current value, default value, possible values, dependencies, authentication, and pending reboot state. The same documentation says `current_value` can be read and written to update a firmware attribute. [Linux firmware-attributes ABI](https://www.kernel.org/doc/html/latest/admin-guide/abi-testing.html)

This interface is extremely important for CursiveOS because it turns BIOS settings into machine-readable files.

Conceptual workflow:

```bash
ls /sys/class/firmware-attributes/
find /sys/class/firmware-attributes -maxdepth 4 -type f | sort
cat /sys/class/firmware-attributes/*/attributes/*/current_value
```

Mutation example shape:

```bash
cat /sys/class/firmware-attributes/thinklmi/attributes/SecureBoot/current_value
echo Disable | sudo tee /sys/class/firmware-attributes/thinklmi/attributes/SecureBoot/current_value
```

Important details from the ABI:

- attributes may be enumeration, integer, string, or vendor-specific types;
- some settings have dependency rules and value modifiers;
- some platforms expose `pending_reboot` to indicate that a reboot is required;
- Dell, Lenovo, and HP expose vendor-specific extensions;
- BIOS administrator password or certificate authentication may be required;
- some changes explicitly require reboot before taking effect.

For CursiveOS this should become a primary adapter:

```text
cursive-firmware-sysfs
```

### 3.3 Vendor BIOS Tools

Many enterprise and business-class systems expose BIOS configuration through vendor tools or WMI/LMI interfaces. Dell Command Configure, Lenovo ThinkLMI, HP management interfaces, and server vendor tools should be treated as platform adapters rather than special cases embedded in the core agent.

Recommended adapter pattern:

```text
cursive-firmware-dell
cursive-firmware-lenovo
cursive-firmware-hp
cursive-firmware-supermicro
```

The core CursiveFirmware API should not care whether a setting is written through sysfs, WMI, a vendor CLI, Redfish, or another backend. It should expose a normalized mutation contract and let platform adapters implement the actual writes.

### 3.4 BMC / IPMI / Redfish

For rack systems, the cleanest route is out-of-band management through a Baseboard Management Controller. Redfish is especially relevant because it models system inventory, BIOS attributes, boot override, power state, thermal data, and pending configuration through a network API.

The strategic advantage is survival. If the host OS fails to boot after a firmware mutation, the BMC can still power-cycle the machine, change boot target, expose remote console, or apply a recovery profile. This is much closer to the CursiveOS organism model than consumer desktop BIOS hacking.

CursiveOS should strongly prefer server-class boards with BMC/Redfish for serious self-optimization research.

Desired capabilities:

- read current BIOS attributes;
- stage pending BIOS attributes;
- set one-time boot target;
- reset/power-cycle host;
- collect thermal, fan, voltage, and hardware health data;
- expose serial-over-LAN or remote console;
- recover from failed host boot.

Recommended adapter:

```text
cursive-firmware-redfish
```

### 3.5 Firmware Update and Capsule Flow

`fwupd` and LVFS-style firmware update flows are not arbitrary BIOS mutation layers, but they matter for controlled firmware version management. Firmware version itself is a phenotype. A CursiveOS node should know the current BIOS/UEFI version, embedded controller firmware, NVMe firmware, GPU firmware, NIC firmware, and update availability.

Initial scope:

- inventory firmware devices;
- hash and record versions;
- warn when firmware version changes between benchmark runs;
- optionally stage firmware updates under explicit policy;
- record post-update fitness deltas.

### 3.6 Raw Flash Access: `flashrom` and External SPI Programmers

If the research mode accepts bricking risk, the direct path to firmware control is raw firmware image read/write. `flashrom` is an open-source utility used to detect, read, write, verify, and erase flash chips such as BIOS/UEFI SPI flash. It can be used in-system where supported or with external programmers. [flashrom documentation](https://flashrom.org/classic_cli_manpage.html)

Conceptual workflow:

```bash
sudo flashrom -p internal -r backup-known-good.bin
sha256sum backup-known-good.bin
sudo flashrom -p internal -w candidate.bin
sudo flashrom -p internal -v candidate.bin
```

External workflow:

```text
external programmer -> SOIC clip -> read SPI flash -> patch image -> write image -> verify -> boot trial
```

Recommended adapter:

```text
cursive-firmware-flashrom
```

This should be treated as a research backend, not a default product backend. It is valuable for firmware mutation experiments, coreboot workflows, and recovery drills.

### 3.7 KVM / BIOS UI Automation

An agent can technically operate firmware setup screens through PiKVM, BMC remote console, or another keyboard/video/mouse control layer. This would allow BIOS menu manipulation on systems without machine-readable BIOS APIs.

However, this is a brittle fallback:

- BIOS menus differ by vendor and version;
- timing is unreliable;
- screenshots require vision interpretation;
- one wrong keypress changes the wrong setting;
- there is no stable schema or dependency graph.

Recommended adapter:

```text
cursive-firmware-kvm-ui
```

This should be classified as a compatibility hack, not the core path.

### 3.8 Coreboot / Open Firmware

Coreboot-supported systems offer the cleanest long-term research path for firmware-level self-optimization because the firmware is more inspectable and modifiable. The drawback is board-specific support and reliance on platform blobs for many modern systems.

CursiveOS should track coreboot as a research backend, especially for sacrificial lab hardware and future reproducible firmware experiments.

Recommended adapter:

```text
cursive-firmware-coreboot
```

### 3.9 Practical Control-Surface Matrix

The source-backed picture is less mystical and more useful than "an agent can
change BIOS." Firmware control is a set of uneven interfaces with different
failure modes, apply times, schemas, and recovery paths.

| Control Surface | Examples | Interface | Apply Time | Standardization | Risk | CursiveOS Use |
| --- | --- | --- | --- | --- | --- | --- |
| UEFI variables | Boot entries, `BootOrder`, `BootNext`, OS indications | `efivarfs`, boot manager tools | Next boot or firmware-dependent | UEFI standard plus vendor-specific variables | Medium to high; arbitrary writes can harm boot | Boot inventory, rescue boot, benchmark image selection |
| Linux firmware attributes | Secure Boot toggles, virtualization flags, boot/device settings, vendor BIOS attributes | `/sys/class/firmware-attributes` | Often reboot-staged; `pending_reboot` may expose state | Kernel ABI with vendor-specific providers | Medium to high; authentication and dependencies matter | Best Linux-native BIOS-setting adapter where available |
| Redfish BIOS attributes | BIOS attribute registry, pending settings, reset-to-default request | BMC Redfish API, `@Redfish.Settings` | Usually on reset or scheduled maintenance window | DMTF schema; attribute names remain implementation-specific | Medium; safer because recovery can be out-of-band | Preferred server/workstation control plane for serious mutation trials |
| Attribute registries | Legal values, read-only state, reset requirement, dependency rules | Redfish `AttributeRegistry` | Metadata only | DMTF schema; contents vendor/product-specific | Low for reads; high if ignored before mutation | Constraint source for mutation proposal validation |
| Firmware update capsules | BIOS/UEFI, EC, device firmware versions | fwupd / LVFS / UEFI capsule flow | Staged from OS, applied through reboot path | UEFI capsule standards plus vendor metadata | High; changes firmware version, not just a setting | Version inventory and deliberate firmware-version mutation |
| Raw flash | SPI BIOS image read/write/verify | flashrom or external programmer | Power-cycle/reflash | Chip/programmer-specific | Very high; lab only | Sacrificial hardware, recovery drills, coreboot research |
| KVM/BIOS UI automation | Consumer BIOS menu navigation | PiKVM, BMC remote console, vision/key input | Reboot/manual UI timing | Not standardized | High; brittle and hard to audit | Fallback compatibility experiment, not core product path |

Two design rules fall out of the sources:

1. The adapter must preserve interface semantics. Redfish apply-time, sysfs
   pending-reboot state, authentication, dependencies, and read-only metadata
   are not optional decoration; they are safety constraints.
2. The shell agent should propose firmware mutations, not execute raw firmware
   writes. A deterministic adapter should validate the proposal against the
   interface metadata and CursiveRoot policy before staging any change.

## 4. Runtime Mutation vs Reboot-Staged Mutation

A key design correction: firmware control is usually not live tuning. It is staged mutation followed by reboot and measurement.

| Setting class | Live from OS? | Usually requires reboot? | Notes |
| --- | --- | --- | --- |
| Boot order / next boot target | Sometimes | Applies on next boot | UEFI variables and boot manager tooling are the easiest entry point. |
| Firmware attributes | Sometimes writable live | Usually yes | Many settings are staged and applied after reboot. |
| Secure Boot policy / keys | Restricted | Usually yes | Often authenticated and dangerous to automate. |
| Virtualization / IOMMU exposure | Rarely | Yes | CPU/chipset features are exposed early. |
| Memory speed / timings / ECC | No | Yes, often cold boot | DRAM training happens before Linux. |
| PCIe bifurcation / link topology | No | Yes | PCIe enumeration occurs before OS handoff. |
| Resizable BAR / MMIO aperture | No or limited | Yes | Address map is built during boot. |
| NUMA/interleaving policy | No or limited | Yes | Firmware exposes topology to the kernel. |
| Fan curves / power policy | Sometimes | Platform-dependent | BMC/EC may allow live updates. |
| CPU governor / frequency scaling | Yes | No | This remains OS-level tuning. |
| GPU clocks / power limits | Yes | No or driver reset | Driver/firmware-specific sysfs or vendor tooling. |

Conclusion: firmware mutation should be modeled as a reproductive cycle, not a live feedback loop.

```text
mutate firmware config
reboot or cold boot
develop new hardware/software phenotype
measure fitness
accept or roll back
record result
```

## 5. Physical and Architectural Limits

### 5.1 DRAM Training Happens Before the OS Exists

Memory frequency, timings, voltage behavior, channel topology, and ECC behavior are determined during firmware initialization. If the system fails memory training, Linux never boots. CursiveOS cannot fix that from inside the failed host OS. Recovery requires firmware fallback, BMC, dual BIOS, or external SPI restore.

### 5.2 PCIe Topology Is Established Before Linux Receives Devices

PCIe bifurcation, lane width, device enumeration, MMIO windows, and some BAR decisions are made during boot. Linux can rescan parts of PCIe, but it cannot reliably create a topology the firmware never exposed.

### 5.3 Some Settings Are Latched at Reset

Certain CPU, chipset, and device settings are sampled only at reset or power-on. Warm reboot may not be enough; some changes require full power removal. CursiveOS should distinguish:

```text
no reboot required
warm reboot required
cold boot required
power drain required
external flash required
```

### 5.4 Firmware Flash Is Protected

Modern platforms may use signed update capsules, SPI descriptor locks, rollback protection, Intel Boot Guard, AMD PSP validation, TPM/Secure Boot policy, and vendor keys. These are security boundaries, not mere software inconvenience. In research mode, some can be bypassed with external programming; in product mode, they must be respected.

### 5.5 The Machine Contains Hidden Controllers

The OS is not sovereign. The embedded controller, BMC, Intel ME, AMD PSP, GPU firmware, NIC firmware, SSD firmware, and power controllers all act as subordinate computers with their own rules. CursiveOS should inventory these as organs in the organism, not ignore them.

## 6. Proposed Subsystem: `CursiveFirmware`

`CursiveFirmware` is the proposed firmware mutation layer for CursiveOS.

It should expose a normalized control plane:

```text
Discover -> Propose -> Validate -> Stage -> Reboot -> Measure -> Accept/Rollback -> Ledger
```

### 6.1 Core Responsibilities

- Detect firmware control backends available on a host.
- Inventory firmware, BIOS, UEFI, BMC, bootloader, and hardware topology state.
- Normalize firmware attributes into a schema.
- Let agents propose firmware mutations without direct write access.
- Validate proposals against platform capability, dependency rules, and known-dangerous combinations.
- Stage pending settings through the safest available backend.
- Coordinate reboot, cold boot, or rescue boot.
- Run post-boot health checks and benchmarks.
- Commit or roll back state.
- Record every mutation and outcome in CursiveRoot.

### 6.2 Adapter Layout

```text
cursive-firmware-uefi       # efivarfs, boot entries, next boot target
cursive-firmware-sysfs      # /sys/class/firmware-attributes
cursive-firmware-redfish    # BMC/Redfish BIOS config and host reset
cursive-firmware-dell       # Dell Command Configure / Dell-specific sysfs
cursive-firmware-lenovo     # ThinkLMI / Lenovo firmware attributes
cursive-firmware-hp         # HP firmware attributes / SPM
cursive-firmware-fwupd      # firmware inventory and version updates
cursive-firmware-flashrom   # raw flash read/write for lab mode
cursive-firmware-kvm-ui     # PiKVM/BMC remote-console BIOS UI fallback
cursive-firmware-coreboot   # coreboot parameter and image workflows
```

### 6.3 Mutation Contract

Firmware mutations should be expressed as structured proposals, not shell commands.

```json
{
  "target_layer": "firmware",
  "backend": "redfish|firmware-attributes|uefi|flashrom|kvm-ui|coreboot",
  "setting": "ResizableBAR",
  "current_value": "Disabled",
  "proposed_value": "Enabled",
  "reason": "Increase GPU-visible memory aperture for local inference workloads",
  "expected_effect": "Improved model load or GPU memory mapping behavior",
  "risk_class": "medium",
  "requires": ["reboot"],
  "rollback": {
    "setting": "ResizableBAR",
    "value": "Disabled"
  },
  "fitness_test": [
    "boot_success",
    "gpu_enumeration",
    "llama_cpp_prefill_benchmark",
    "thermal_stability_10m"
  ]
}
```

### 6.4 Fitness Gates

A firmware mutation should not be accepted merely because the system boots.

Minimum acceptance gates:

- POST success;
- bootloader reached;
- kernel reached;
- network reachable;
- storage mounted;
- GPU and accelerators enumerated;
- CursiveOS agent heartbeat restored;
- no new critical kernel errors;
- benchmark delta meets threshold;
- no thermal or power regression beyond policy.

## 7. Firmware Mutation and the CursiveOS Organism Model

This layer strengthens the biological framing:

| CursiveOS concept | Firmware-layer analog |
| --- | --- |
| Mutation | Pending BIOS/UEFI/firmware config change |
| Development | Reboot, hardware initialization, OS handoff |
| Phenotype | Resulting hardware topology and runtime behavior |
| Fitness | Boot health, benchmarks, thermals, stability, energy efficiency |
| Memory | CursiveRoot mutation ledger and hardware fingerprint history |
| Immune response | Rollback, rescue boot, BMC restore, known-good firmware image |
| Autonomic nervous system | BMC, IPMI, Redfish, PiKVM, smart PDU |
| Genetic boundary | Firmware image, UEFI variables, boot chain, signed capsules |

This also clarifies the hierarchy of mutation depth:

```text
userspace/service mutation
OS/sysctl mutation
kernel/module mutation
driver/sysfs mutation
bootloader/kernel-command-line mutation
firmware/BIOS setting mutation
firmware image mutation
hardware topology mutation
```

Each deeper layer is more powerful, less portable, slower to test, and more dangerous.

## 8. Minimum Viable `CursiveFirmware`

The first implementation should not start with raw firmware flashing. It should start with discovery and boot control.

### Phase 0: Read-Only Inventory

Collect:

```text
UEFI vs legacy boot mode
BIOS vendor/version/date
motherboard vendor/model/revision
Secure Boot state
TPM state
boot entries and boot order
kernel command line
IOMMU state
Resizable BAR exposure
above-4G decoding evidence
PCIe topology
GPU BAR sizes
memory speed/ECC status
BMC/Redfish availability
firmware-attributes availability
fwupd device inventory
```

### Phase 1: Boot Target Control

Implement:

```text
read boot entries
set one-time boot target
boot into rescue image
boot into benchmark image
restore normal boot target
record boot outcome
```

### Phase 2: Firmware Attribute Mutation

On supported platforms:

```text
read firmware attributes
classify safe/unsafe settings
stage one low-risk setting
reboot
measure
record outcome
revert
```

Good first candidates:

- boot order;
- virtualization flags;
- fan profile if exposed;
- power profile if exposed;
- Resizable BAR only on sacrificial hardware;
- above-4G decoding only on sacrificial hardware.

### Phase 3: Redfish/BMC Control

For server hardware:

```text
read BIOS attributes via BMC
stage pending setting
power-cycle host
watch host heartbeat
set rescue boot on failure
record BMC health telemetry
```

### Phase 4: Lab-Only Raw Flash Backend

For sacrificial boards:

```text
dump known-good firmware
hash and store image
modify image or flash candidate
verify write
boot trial
restore on failure with external programmer
```

## 9. Hardware Recommendations for Research

Best first target: server or workstation board with BMC/Redfish.

Why:

- machine-readable control plane;
- remote power cycling;
- BIOS pending settings;
- remote console;
- recovery without relying on host OS;
- better fit for rack-scale CursiveOS.

Best hacker target: coreboot-supported board.

Why:

- open firmware research path;
- inspectable firmware image;
- better long-term reproducibility.

Best cheap target: old business desktop or ThinkPad-class machine.

Why:

- likely to expose WMI/LMI firmware attributes;
- cheap enough for destructive testing;
- good platform for early `firmware-attributes` adapter.

Worst target: consumer gaming motherboard.

Why:

- rich BIOS UI but poor machine-readable control;
- inconsistent vendor tooling;
- likely forces brittle PiKVM menu automation.

## 10. Research Backlog

1. Build a `cursive-firmware-probe` script that inventories UEFI, SMBIOS, boot entries, firmware attributes, fwupd devices, PCIe topology, GPU BAR sizes, and BMC availability.
2. Add `firmware_state_hash` to CursiveRoot so benchmark deltas can be tied to firmware state.
3. Define a normalized firmware attribute schema.
4. Build a safe boot-target controller using UEFI boot entries.
5. Build a Redfish proof-of-concept on one BMC-equipped board.
6. Build a sysfs firmware-attributes proof-of-concept on one Lenovo/Dell/HP business system.
7. Add mutation ledgers for reboot-required settings.
8. Define failure states: failed POST, failed bootloader, failed kernel, failed agent heartbeat, failed benchmark.
9. Design a rescue profile: known-good firmware state + rescue boot target + network recovery.
10. Build a lab-only flashrom recovery drill using sacrificial hardware and an external SPI programmer.

## 11. CursiveRoot Schema Additions

Proposed future fields:

```text
firmware_vendor
firmware_version
firmware_date
firmware_state_hash
uefi_boot_mode
secure_boot_state
tpm_present
tpm_enabled
bmc_present
redfish_available
firmware_attributes_available
boot_order_hash
last_firmware_mutation_id
pending_reboot_required
post_boot_health_status
rescue_boot_available
known_good_firmware_profile_id
```

Firmware mutation record:

```json
{
  "mutation_id": "fwmut_2026_05_26_001",
  "host_fingerprint": "...",
  "firmware_state_before": "sha256:...",
  "firmware_state_after": "sha256:...",
  "backend": "firmware-attributes",
  "setting": "ExampleSetting",
  "old_value": "Disabled",
  "new_value": "Enabled",
  "requires_reboot": true,
  "boot_result": "success",
  "fitness_delta": {
    "cold_start_pct": 0.0,
    "sustained_pct": 0.0,
    "network_pct": 0.0,
    "energy_pct": 0.0
  },
  "decision": "accepted|reverted|quarantined"
}
```

## 12. Strategic Implication

The firmware layer changes the CursiveOS roadmap. The project is not merely building better Linux presets. It is moving toward a whole-machine optimization organism.

The near-term product should still remain OS-first because OS-level mutation is easier, safer, and immediately testable. But the long-term architecture should reserve a formal place for firmware mutation. Otherwise CursiveOS will eventually hit a ceiling: it can tune the phenotype Linux receives, but it cannot change the developmental process that creates that phenotype.

The blunt recommendation:

> Do not rewrite the OS to force BIOS control. Build a firmware-control abstraction that uses UEFI variables, Linux firmware attributes, vendor tools, Redfish/BMC, and lab-only raw flash workflows where available.

This creates a path from practical system tuning to true self-optimizing hardware/software organisms without collapsing the project into ad hoc BIOS hacking.

## 13. References

- Linux Kernel Documentation: `efivarfs` UEFI variable filesystem — https://docs.kernel.org/filesystems/efivarfs.html
- Linux Kernel ABI: `/sys/class/firmware-attributes/*/attributes/*/` — https://www.kernel.org/doc/html/latest/admin-guide/abi-testing.html
- UEFI Specification 2.10: Runtime Services — https://uefi.org/specs/UEFI/2.10/08_Services_Runtime_Services.html
- DMTF Redfish Specification / BIOS resources — https://www.dmtf.org/standards/redfish
- flashrom classic CLI manual — https://flashrom.org/classic_cli_manpage.html
