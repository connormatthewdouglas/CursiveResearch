# Validation Note: Chapter 08 Firmware and BIOS Control

Date checked: 2026-05-26
Agent / reviewer: GPT-5.5 Thinking / ChatGPT
Scope: `chapters/08-firmware-and-bios-control.md`
Status: supported with minor caveats
Source IDs: SRC-08-001, SRC-08-002, SRC-08-003, SRC-08-004, SRC-08-005

## Summary

Chapter 08's core architectural claim is supported: firmware/BIOS/UEFI control should be modeled as a separate, slower, reboot-staged mutation layer rather than as ordinary live OS tuning. The strongest evidence comes from primary sources: Linux kernel documentation for `efivarfs`, Linux ABI documentation for `firmware-attributes`, the UEFI 2.10 Runtime Services specification, the Redfish BIOS schema, and the flashrom manual.

The chapter should remain marked as platform-validation-required because support is highly hardware/vendor-specific. The sources validate the existence and shape of the control surfaces, not universal availability on every motherboard or safety of automated mutation.

## Claims Checked

| Claim ID | Claim | Status | Evidence | Notes / Required Rewrite |
| --- | --- | --- | --- | --- |
| CL-08-001 | Linux exposes UEFI variables through `efivarfs`, usually mounted at `/sys/firmware/efi/efivars`, and variables can be created, deleted, and modified through it. | supported | SRC-08-001 | Linux docs explicitly say `efivarfs` was created for EFI variables; variables can be created/deleted/modified; typical mount path is shown. |
| CL-08-002 | Non-standard UEFI variable deletion can trigger severe firmware bugs, including failure to POST. | supported | SRC-08-001 | Linux docs warn that removing non-standard UEFI variables can cause firmware to fail to POST; immutable default behavior is a mitigation, not a full prevention. |
| CL-08-003 | UEFI Runtime Services include variable services such as `GetVariable`, `GetNextVariableName`, `SetVariable`, and `QueryVariableInfo`, and variables are usually persistent across boots. | supported | SRC-08-003 | UEFI spec lists these as runtime variable services and states persistent storage is required in most cases, though storage may be limited. |
| CL-08-004 | Linux `firmware-attributes` exposes machine-readable firmware attribute paths and includes support for pending reboot / reset / save-settings style semantics on supported platforms. | supported with caveat | SRC-08-002 | ABI docs list `/sys/class/firmware-attributes/*/attributes/*/`, authentication, `pending_reboot`, `reset_bios`, and `save_settings`. Exact attribute availability is vendor/firmware-specific. |
| CL-08-005 | Redfish BIOS resources model BIOS attributes, attribute registries, settings resources, and typically require system reset before changes take effect. | supported | SRC-08-004 | Redfish BIOS schema says BIOS changes typically require reset and clients may modify the resource identified by `@Redfish.Settings`; attributes are manufacturer-specific and tied to an attribute registry. |
| CL-08-006 | `flashrom` can detect, read, write, verify, and erase flash chips, including BIOS/EFI/coreboot/firmware images, using internal or external programmers. | supported | SRC-08-005 | flashrom manual directly states these capabilities and lists internal and many external programmer classes. |
| CL-08-007 | Raw firmware flashing should remain lab/research mode rather than a default product backend. | recommendation, supported by risk evidence | SRC-08-001, SRC-08-005 | flashrom docs recommend backup before writing and warn write/erase verification requires recovery means; `efivarfs` docs show firmware bugs can break POST. Keep as project policy. |
| CL-08-008 | Firmware mutation should be staged and then tested after reboot/cold boot, not treated as ordinary live tuning. | supported | SRC-08-003, SRC-08-004 | UEFI variables are runtime-writable, but many BIOS settings are vendor resources and Redfish BIOS changes typically require reset. Chapter's reboot-cycle model is appropriate. |

## Corrections / Caveats to Carry Forward

- Do not imply every BIOS menu setting is exposed through `efivarfs` or `firmware-attributes`. `efivarfs` is UEFI variable storage, not a universal BIOS setting API.
- `firmware-attributes` is a useful Linux abstraction, but support is vendor/platform-specific.
- Redfish BIOS support is strongest on server/BMC platforms; consumer boards may lack it entirely.
- `flashrom` validates a capability path, not a safety guarantee. Board support, descriptor locks, signed firmware, ME/PSP protections, and recovery tooling still determine practical feasibility.

## Implications for CursiveOS

- `CursiveFirmware` is a valid architecture layer.
- The first implementation should prioritize read-only discovery and boot-target control before mutation.
- Server boards with BMC/Redfish remain the best research platform for firmware-level self-optimization.
- CursiveRoot should record firmware state and pending-reboot state so benchmark deltas can be interpreted correctly.

## Follow-up

- Build a `cursive-firmware-probe` prototype for one Linux host.
- Validate `firmware-attributes` behavior on one Dell/Lenovo/HP system and one server/BMC platform.
- Add exact Redfish request/response examples after testing against real hardware.
- Add an experiment note once a BIOS setting is staged, rebooted, and measured.
