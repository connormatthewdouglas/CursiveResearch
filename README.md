# CursiveResearch

Private living research corpus for the CursiveOS team.

## Start Here

Read [INDEX.md](INDEX.md) for the chapter library, [VALIDATION.md](VALIDATION.md)
for the current confidence level of important claims, and [CHANGELOG.md](CHANGELOG.md)
for material edits. See [methodology/maintaining-the-corpus.md](methodology/maintaining-the-corpus.md)
when adding or reorganizing research.

## Purpose

This repository collects research and working conclusions that inform CursiveOS
decisions. Chapters are living documents: they should be corrected directly as
understanding improves. Confidence is tracked separately so a readable chapter
does not imply that every claim has been proven.

## Repository Layout

| Path | Purpose |
| --- | --- |
| `chapters/` | Living research chapters organized by topic. Direct edits are expected when guidance changes. |
| `CHANGELOG.md` | Required dated record of meaningful chapter, methodology, and evidence changes. |
| `VALIDATION.md` | Compact status register for claims that affect implementation or decisions. |
| `sources/original-docx/` | Preserved original Word documents. Treat these as immutable input snapshots. |
| `sources/` | Source links and provenance records where they are useful. |
| `experiments/` | Plans and results for tests worth keeping or repeating. |
| `methodology/` | Lightweight rules for maintaining this corpus. |
| `validation/` | Legacy detailed validation records and optional deep-dive notes. |
| `tools/` | Repeatable conversion and integrity-checking utilities. |

## Working Rule

Preserve the uploaded originals, but do not freeze the chapters. When research
changes what the project should do:

1. Edit the relevant chapter so it gives the current best guidance.
2. Add a dated entry to `CHANGELOG.md` explaining what changed and why.
3. Update `VALIDATION.md` when the change depends on an important tested or
   still-uncertain claim.

Long evidence notes and benchmark logs are optional. Create them only when the
detail will matter again.

## Confidentiality

Private team material. Do not publish, redistribute, or copy material outside
approved project channels without authorization.

## Initial Import Status

The initial Word documents were converted into topical Markdown chapters. The
original DOCX files remain the intake record. The chapters may now be revised as
living research; unvalidated imported claims should remain marked as such in
`VALIDATION.md` when they influence current work.
