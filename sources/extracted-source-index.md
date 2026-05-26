# Extracted Source Index

Status: First validation pass started 2026-05-26. Source extraction is incomplete across the full corpus.

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
| `chapters/08-firmware-and-bios-control.md` | P0 | New architecture layer; small enough to fully validate first | Extracted below | Supported with minor caveats |
| `chapters/09-local-agent-arc-b70.md` | P0 | Immediate local-agent and hardware-planning impact | Selected high-priority sources extracted below | Partially verified; hardware/software architecture supported, performance/model claims need reproduction |
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
| SRC-08-001 | efivarfs - a filesystem for UEFI variables | Linux Kernel Documentation | https://docs.kernel.org/filesystems/efivarfs.html | primary documentation | Unknown / rolling kernel docs | 2026-05-26 | `08-firmware-and-bios-control.md` §3.1 | Linux exposes UEFI variables through `efivarfs`; variables may be created/deleted/modified; non-standard deletion can trigger firmware issues | A | verified | Validates `efivarfs` capability and firmware-risk caveat. |
| SRC-08-002 | Linux ABI testing documentation: firmware attributes | Linux Kernel Documentation | https://www.kernel.org/doc/html/latest/admin-guide/abi-testing.html | primary documentation | Unknown / rolling kernel docs | 2026-05-26 | `08-firmware-and-bios-control.md` §3.2 | `/sys/class/firmware-attributes` exposes firmware settings, value types, current values, defaults, dependencies, and reboot state on supported systems | A | verified | Support is vendor/platform-specific; do not imply universal availability. |
| SRC-08-003 | UEFI Specification 2.10: Runtime Services | UEFI Forum | https://uefi.org/specs/UEFI/2.10/08_Services_Runtime_Services.html | standard / primary documentation | UEFI 2.10 | 2026-05-26 | `08-firmware-and-bios-control.md` §3.1 | UEFI defines runtime services, including variable services available to the OS under firmware rules | A | verified | Validates runtime variable services, not arbitrary BIOS menu access. |
| SRC-08-004 | Redfish BIOS Schema / Redfish Standards | DMTF | https://redfish.dmtf.org/schemas/v1/Bios.v1_2_0.json | standard / primary documentation | Redfish schema v1.2.0 | 2026-05-26 | `08-firmware-and-bios-control.md` §3.4 | Redfish BIOS resources include attributes, registries, settings resources, and reset-required semantics | A | verified | Stronger than generic Redfish landing page. BIOS attributes are manufacturer-specific. |
| SRC-08-005 | flashrom classic CLI manual | flashrom project | https://flashrom.org/classic_cli_manpage.html | official project documentation | Unknown / rolling docs | 2026-05-26 | `08-firmware-and-bios-control.md` §3.6 | `flashrom` can read, write, verify, erase, and detect flash chips using internal or external programmers | A | verified | Validates capability path, not safety or board support. |

### Chapter 09 — Local Agent Setup for Arc B70

Selected high-priority sources only. Full source extraction for all 39 works cited remains open.

| Source ID | Title | Author / Organization | URL / DOI / Repo | Source Type | Date Published / Updated | Date Accessed | Used In | Claims Supported | Reliability Tier | Validation Status | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-09-001 | Intel Arc Pro B70 Review | Puget Systems | https://www.pugetsystems.com/labs/articles/intel-arc-pro-b70-review/ | benchmark article | 2026 | 2026-05-26 | `09-local-agent-arc-b70.md` hardware profile | Independent workstation/AI review and hardware context for Arc Pro B70 | B | needs verification | Use to validate performance context, but prefer Intel/vender docs for raw specifications. |
| SRC-09-002 | Intel Arc Pro B70 Specs | TechPowerUp GPU Database | https://www.techpowerup.com/gpu-specs/arc-pro-b70.c4388 | benchmark/spec database | 2026 | 2026-05-26 | `09-local-agent-arc-b70.md` hardware table | GPU specs such as memory, bandwidth, clocks, FP32, and board power | B | needs verification | Good spec aggregator; not primary. Cross-check against Intel and board vendors. |
| SRC-09-003 | llama.cpp for SYCL | ggml-org / llama.cpp | https://github.com/ggml-org/llama.cpp/blob/master/docs/backend/SYCL.md | official repo documentation | Rolling | 2026-05-26 | `09-local-agent-arc-b70.md` backend stack | SYCL backend targets Intel GPUs, uses oneAPI/Level Zero, supports Intel Arc family, and documents build/install commands | A | verified | Verified for Intel Arc family and B580 listed device. Does not by itself validate B70-specific throughput. |
| SRC-09-004 | llama.cpp Function Calling | ggml-org / llama.cpp | https://github.com/ggml-org/llama.cpp/blob/master/docs/function-calling.md | official repo documentation | Rolling | 2026-05-26 | `09-local-agent-arc-b70.md` tool-calling section | `llama-server --jinja` supports OpenAI-style function calling and native/generic handlers | A | verified | Supports general function-calling claims; does not validate Qwen 3.5/3.6 parser-fix claims. |
| SRC-09-005 | Release Notes for Intel Distribution of OpenVINO Toolkit 2025.3 | Intel | https://www.intel.com/content/www/us/en/developer/articles/release-notes/openvino/2025-3.html | vendor docs | 2025.3 release | 2026-05-26 | `09-local-agent-arc-b70.md` OpenVINO backend | OpenVINO 2025.3 includes tool-guided generation / XGrammar support, GGUF preview support, Qwen3 support, and key-cache compression changes | A | verified | Supports OpenVINO feature claims for 2025.3; validate 2026.1 separately when cited. |
| SRC-09-006 | Qwen3.6-35B-A3B: Agentic Coding Power, Now Open to All | Qwen | https://qwen.ai/blog?id=qwen3.6-35b-a3b | primary model announcement | 2026 | 2026-05-26 | `09-local-agent-arc-b70.md` model-selection section | Existence and intended positioning of Qwen3.6-35B-A3B model | A | needs verification | Page fetch was sparse in current pass; recheck model card/Hugging Face/ModelScope for exact active-parameter and tool-calling details. |
| SRC-09-007 | Intel Arc Pro B70 Benchmarks & Performance Data | PMZFX GitHub repository | https://github.com/PMZFX/intel-arc-pro-b70-benchmarks | benchmark repo | Rolling | 2026-05-26 | `09-local-agent-arc-b70.md` SYCL/Vulkan and model benchmark claims | B70-specific local benchmark data including backend/model results | B | needs verification | Critical source for performance tables; must inspect methodology, commit date, driver version, command lines, and reproducibility. |
| SRC-09-008 | Intel's Arc Pro B70 workstation GPU with 32GB of VRAM gets tested in games | Tom's Hardware | https://www.tomshardware.com/pc-components/gpus/intels-arc-pro-b70-workstation-gpu-with-32gb-of-vram-gets-tested-in-games-roughly-twice-as-fast-as-arc-b580-on-average-beats-rtx-5060-ti-in-some-titles | news/reporting | 2026-05 | 2026-05-26 | `09-local-agent-arc-b70.md` hardware/performance context | Confirms B70 reported as 32GB ECC GDDR6 and summarizes third-party MLPerf Client results | C | partially verified | Useful as current reporting, but should not be the sole basis for engineering claims. |
| SRC-09-009 | Intel launches the Arc Pro B70 graphics card based on Big Battlemage | PC Gamer | https://www.pcgamer.com/hardware/graphics-cards/intel-launches-the-arc-pro-b70-graphics-card-based-on-the-big-battlemage-gpu-weve-been-waiting-for-forever-but-its-for-ai-not-gaming/ | news/reporting | 2026 | 2026-05-26 | `09-local-agent-arc-b70.md` hardware/performance context | Reports B70 32GB GDDR6, 256-bit bus, 608 GB/s, 32 Xe2 cores, 256 XMX engines, 367 INT8 TOPS, $949 | C | partially verified | Useful corroboration; replace with Intel product page if/when available. |

## Pending Extraction Notes

- Many imported chapters contain inline links but not a clean bibliography. Each chapter needs a pass that extracts every URL, paper, repo, vendor doc, and benchmark article into this index.
- Bracketed numeric citations like `[1]`, `[2]`, or converted citation artifacts must be resolved back to actual references where possible. If the original DOCX has a bibliography that failed conversion, recover it from the preserved source master.
- Source extraction and claim validation are separate tasks. A source being listed here does not mean the claim has been validated.
- Chapter 09 has a full works-cited list in the chapter body. Only the most important sources were normalized in the first pass. Community sources, Reddit posts, Medium articles, and third-party setup guides should be demoted unless corroborated by primary docs or reproducible tests.
