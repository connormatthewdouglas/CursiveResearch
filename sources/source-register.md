# Source Register

## Initial Import

Import date: `2026-05-26`

Original DOCX files are preserved under `sources/original-docx/`. Markdown
chapters were generated from these sources without intentionally rewriting
their wording. Conversion verification checked each non-empty source paragraph
and table cell group for retention in its generated chapter.

| Source Master | Git Blob SHA | Markdown Chapter | Retained Blocks |
| --- | --- | --- | ---: |
| `Research Master.docx` | `081d0d5e31f2f3f8d3230e9c8db0ece7e50456f1` | `chapters/00-research-master.md` | 33 |
| `CursiveOS_First_Principles_Report.docx` | `20ff2bd8016cff5bb1b905d37720430a5ab0e360` | `chapters/01-first-principles-and-strategy.md` | 122 |
| `1. TAO-OS Research and Viability Report.docx` | `728366a746ea6ecf1f7488f1f6e39dc6666df303` | `chapters/02-market-and-viability.md` | 200 |
| `2. Linux kernel optimizations.docx` | `e54cb50b4cfaa93aedbf07f50f4a5dbd7bf8c51e` | `chapters/03-linux-kernel-optimization.md` | 67 |
| `3. GPU Kernel Tweaks for Mining_AI.docx` | `726912342c92bec12771ffcf36db5ecf8231033d` | `chapters/04-gpu-and-accelerator-tuning.md` | 176 |
| `5. ai guided tuning_.docx` | `a17532ea3758c27bfd182795d517aee2b80be108` | `chapters/05-ai-guided-tuning.md` | 39 |
| `6. Hardening linux.docx` | `d6f761544e05ccddb4c0269b3d58e059d5bbcad7` | `chapters/06-security-and-hardening.md` | 50 |
| `4. Tokenomics_.docx` | `839c8733a30a682416ec0858c75e229ebc51131b` | `chapters/07-tokenomics-and-incentives.md` | 145 |

## Pending Intake

| Date Added | Source | Intended Action | Status | Notes |
| --- | --- | --- | --- | --- |
| `2026-05-26` | Google Doc: `https://docs.google.com/document/d/1kXXy5JjOHHk9dayoQARA2f6ZhzR80DLf-1PeXuTkHqA/edit?usp=drivesdk` | Import as new source master, convert/integrate into relevant chapter, extract cited sources, update validation ledger | Pending content access | Google Drive connector unavailable in current agent environment; public fetch failed. Need exported DOCX/Markdown/TXT/PDF, pasted contents, or accessible share/export link. |

## Conversion Coverage

| Check | Result |
| --- | --- |
| Source files processed | 8 of 8 |
| Tables detected and converted | 14 |
| Images, tracked changes, comments, hyperlinks, footnotes, or endnotes detected | None |
| Non-empty text/table blocks retained in Markdown | 832 of 832 |

## Integrity Policy

The source masters are the lossless record. If a Markdown conversion is ever
corrected, renamed, summarized, or superseded, preserve its original DOCX and
record the change here so the corpus remains auditable.
