# Extracted Source Index

Status: Scaffold created 2026-05-26. Source extraction is not complete.

Purpose: this file is the canonical index of external sources cited by the research corpus. The existing `source-register.md` tracks provenance of imported DOCX/source-master files. This file tracks the sources cited inside those research documents and inside later project-authored synthesis.

## Source ID Format

Use stable IDs so chapters, validation notes, and decision records can cross-reference the same source without duplicating URLs.

Recommended format:

```text
SRC-<chapter-number>-<three-digit-sequence>
```

Examples:

```text
SRC-03-001
SRC-05-014
SRC-08-003
```

If a source supports multiple chapters, keep the first ID assigned and list every chapter that uses it.

## Source Record Schema

Each source should eventually have this information:

| Field | Meaning |
| --- | --- |
| Source ID | Stable corpus identifier. |
| Title | Human-readable title. |
| Author / Organization | Prefer the primary organization or paper authors. |
| URL / DOI / Repo | Canonical location. |
| Source type | `primary documentation`, `paper`, `official repo`, `benchmark article`, `news/reporting`, `forum/community`, `vendor docs`, `internal benchmark`, or `other`. |
| Date published / updated | Absolute date if known. |
| Date accessed | When the corpus agent checked it. |
| Used in | Chapter and section where cited. |
| Claims supported | Short summary of what the source is being used to support. |
| Reliability tier | `A`, `B`, `C`, or `D` under the methodology. |
| Validation status | `not extracted`, `extracted`, `needs verification`, `verified`, `partially verified`, `disputed`, or `superseded`. |
| Notes | Any caveats, staleness risks, or replacement sources. |

## Reliability Tiers

| Tier | Source Type | Notes |
| --- | --- | --- |
| A | Primary sources: official docs, standards bodies, kernel docs, vendor docs, upstream repos, reproducible internal benchmarks | Preferred for verified claims. |
| B | Peer-reviewed papers, arXiv/preprints with code, reputable technical publications, high-quality benchmark labs | Useful but still check methodology and date. |
| C | News articles, market analysis, blog posts, ecosystem commentary, exchange/crypto explainers | Good for context; avoid using alone for technical truth. |
| D | Forums, unsourced claims, social media, speculative reports, AI-generated research docs without source verification | Use only as leads until verified elsewhere. |

## Extraction Queue

| Chapter | Priority | Why | Extraction Status | Validation Status |
| --- | --- | --- | --- | --- |
| `chapters/08-firmware-and-bios-control.md` | P0 | New architecture layer; small enough to fully validate first | Extracted below | Needs verification pass |
| `chapters/03-linux-kernel-optimization.md` | P0 | Contains near-term technical tuning claims and version-sensitive kernel claims | Not started | Not started |
| `chapters/05-ai-guided-tuning.md` | P0 | Directly informs autonomous tuning architecture | Not started | Not started |
| `chapters/06-security-and-hardening.md` | P1 | Security claims are high-impact and time-sensitive | Not started | Not started |
| `chapters/04-gpu-and-accelerator-tuning.md` | P1 | Hardware-specific claims require platform validation | Not started | Not started |
| `chapters/01-first-principles-and-strategy.md` | P1 | Strategic claims need evidence, but fewer external technical dependencies | Not started | Not started |
| `chapters/02-market-and-viability.md` | P2 | Market/project claims stale quickly and need broad verification | Not started | Not started |
| `chapters/07-tokenomics-and-incentives.md` | P2 | Economics claims require current protocol docs and market data | Not started | Not started |
| `chapters/00-research-master.md` | P3 | Mixed snapshot; should be split into source-backed claims or superseded by later chapters | Not started | Not started |

## Extracted Sources

### Chapter 08 — Firmware and BIOS Control

| Source ID | Title | Author / Organization | URL / DOI / Repo | Source Type | Date Published / Updated | Date Accessed | Used In | Claims Supported | Reliability Tier | Validation Status | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-08-001 | efivarfs - a filesystem for UEFI variables | Linux Kernel Documentation | https://docs.kernel.org/filesystems/efivarfs.html | primary documentation | Unknown / rolling kernel docs | 2026-05-26 | `08-firmware-and-bios-control.md` §3.1 | Linux exposes UEFI variables through `efivarfs`; variables may be created/deleted/modified; non-standard deletion can trigger firmware issues | A | needs verification | Good primary source. Should be checked against currently targeted kernel versions. |
| SRC-08-002 | Linux ABI testing documentation: firmware attributes | Linux Kernel Documentation | https://www.kernel.org/doc/html/latest/admin-guide/abi-testing.html | primary documentation | Unknown / rolling kernel docs | 2026-05-26 | `08-firmware-and-bios-control.md` §3.2 | `/sys/class/firmware-attributes` exposes firmware settings, value types, current values, defaults, dependencies, and reboot state on supported systems | A | needs verification | Need exact section anchors or copied path references in future verification notes. |
| SRC-08-003 | UEFI Specification 2.10: Runtime Services | UEFI Forum | https://uefi.org/specs/UEFI/2.10/08_Services_Runtime_Services.html | standard / primary documentation | UEFI 2.10 | 2026-05-26 | `08-firmware-and-bios-control.md` §3.1 | UEFI defines runtime services, including variable services available to the OS under firmware rules | A | needs verification | Primary spec; should cite specific services in validation notes. |
| SRC-08-004 | Redfish Standards | DMTF | https://www.dmtf.org/standards/redfish | standard / primary documentation | Rolling standard | 2026-05-26 | `08-firmware-and-bios-control.md` §3.4 | Redfish is a standard out-of-band management API useful for inventory, power/reset, and BIOS-related management | A | needs verification | Future pass should add Redfish BIOS schema/resource docs specifically, not just standards landing page. |
| SRC-08-005 | flashrom classic CLI manual | flashrom project | https://flashrom.org/classic_cli_manpage.html | official project documentation | Unknown / rolling docs | 2026-05-26 | `08-firmware-and-bios-control.md` §3.6 | `flashrom` can read, write, verify, erase, and detect firmware flash chips using internal or external programmers | A | needs verification | Good source for capabilities, not for safety or platform support claims. |

## Pending Extraction Notes

- Many imported chapters contain inline links but not a clean bibliography. Each chapter needs a pass that extracts every URL, paper, repo, vendor doc, and benchmark article into this index.
- Bracketed numeric citations like `[1]`, `[2]`, or converted citation artifacts must be resolved back to actual references where possible. If the original DOCX has a bibliography that failed conversion, recover it from the preserved source master.
- Source extraction and claim validation are separate tasks. A source being listed here does not mean the claim has been validated.
