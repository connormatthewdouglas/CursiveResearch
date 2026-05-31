# Firmware Control Surfaces: Selected Sources

Intake date: `2026-05-30`

Purpose: source-backed grounding for Chapter 08's claim that firmware/BIOS
control can be modeled as a practical, mostly reboot-staged mutation layer.
This is not a complete vendor survey. It is a first pass over primary interfaces
that CursiveOS can inspect before any platform-specific adapter work.

## Sources Reviewed

| Source | Type | Key Takeaway for CursiveOS |
| --- | --- | --- |
| Linux kernel `efivarfs` documentation | Kernel filesystem documentation | UEFI variables are available through `/sys/firmware/efi/efivars`; variables can be created, deleted, and modified, but non-standard variable deletion has caused firmware failures severe enough to prevent POST on some machines. Use for boot-state inspection and carefully bounded boot-target workflows, not arbitrary BIOS mutation. |
| Linux kernel `/sys/class/firmware-attributes` ABI | Kernel ABI documentation | Supported platforms expose firmware configuration attributes under sysfs. Attributes can include current values, defaults, possible values, type metadata, modifiers, authentication state, reset behavior, and `pending_reboot`. This is the strongest Linux-native path for machine-readable BIOS settings. |
| DMTF Redfish `Bios` schema | Out-of-band management schema | Redfish BIOS resources expose manufacturer-specific BIOS attributes and an attribute registry. BIOS changes commonly go through the `@Redfish.Settings` resource and typically require system reset before taking effect. This is the preferred control plane for server-class recovery-capable experiments. |
| DMTF Redfish `Settings` schema | Out-of-band management schema | Redfish operations can declare apply timing such as immediate, on reset, maintenance-window start, in maintenance window on reset, update-start, or target reset. CursiveOS should preserve apply-time semantics instead of collapsing all changes into a generic "reboot required" flag. |
| DMTF Redfish `AttributeRegistry` schema | Out-of-band management schema | Attribute registries describe attribute type, allowed values, read-only state, reset requirements, and dependencies. CursiveOS should ingest these as constraints before allowing an agent to propose a firmware mutation. |
| fwupd UEFI Capsule plugin documentation | Firmware update tooling documentation | UEFI capsule updates are staged while the OS is running but generally applied after reboot through a bootloader/EFI path. fwupd can inventory and stage firmware version changes, but it is a version-update path rather than a generic BIOS-setting interface. |

## Practical Extraction

### 1. Boot Variables Are Real but Narrow

`efivarfs` is useful for reading and carefully modifying UEFI variables,
especially boot-related state. It is not a schema for every BIOS menu item. The
kernel documentation's POST-failure warning should be treated as a design
constraint: CursiveOS should never let a language-model shell freely delete or
write arbitrary UEFI variable files.

Corpus implication:

- allow read-only inventory by default;
- allow boot-target mutation only through a typed adapter;
- preserve known-good boot entries before mutation;
- treat non-standard variable deletion as high risk.

### 2. Firmware Attributes Are the Best Linux-Native BIOS Path

The Linux firmware-attributes ABI is directly aligned with the CursiveFirmware
idea because it converts vendor BIOS settings into typed sysfs objects. Its
metadata is also operationally important: allowed values, dependencies,
authentication, and pending reboot state should be captured before mutation.

Corpus implication:

- `cursive-firmware-probe` should inspect `/sys/class/firmware-attributes`;
- mutation proposals should include attribute type, legal values,
  authentication requirement, and whether a reboot is pending;
- Lenovo bulk-save behavior and vendor authentication should be handled by
  platform adapters rather than hidden inside generic shell commands.

### 3. Redfish Is the Server-Class Gold Path

Redfish separates host control from host survival. BIOS settings, attribute
registries, pending settings, reset operations, power cycling, and health
telemetry can be managed through the BMC even when the host OS is unhealthy.

Corpus implication:

- prefer Redfish/BMC systems for firmware mutation experiments;
- model Redfish setting changes as pending proposals with explicit apply-time;
- use Redfish attribute-registry metadata to block invalid or read-only changes;
- pair every staged mutation with a recovery boot or rollback path.

### 4. fwupd Belongs in Inventory and Version Mutation

fwupd matters because firmware version is part of the phenotype. A benchmark
result taken before and after a BIOS, embedded controller, NVMe, NIC, or GPU
firmware update is not comparable unless the firmware state is recorded.

Corpus implication:

- inventory fwupd devices in Phase 0;
- record firmware versions in CursiveRoot;
- treat firmware updates as explicit, high-impact mutations;
- do not confuse fwupd with live tuning or arbitrary BIOS configuration.

## Suggested Source URLs

- Linux `efivarfs`: https://docs.kernel.org/filesystems/efivarfs.html
- Linux firmware-attributes ABI: https://docs.kernel.org/admin-guide/abi-testing.html
- DMTF Redfish BIOS schema: https://redfish.dmtf.org/schemas/v1/Bios.json
- DMTF Redfish Settings schema: https://redfish.dmtf.org/schemas/v1/Settings.json
- DMTF Redfish AttributeRegistry schema: https://redfish.dmtf.org/schemas/v1/AttributeRegistry.json
- fwupd UEFI Capsule plugin: https://fwupd.github.io/libfwupdplugin/uefi-capsule-README.html
