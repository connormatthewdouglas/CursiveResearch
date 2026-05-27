# CursiveResearch

Private living research corpus for the CursiveOS team.

## Start Here

Read [INDEX.md](INDEX.md) for the chapter library, [RESEARCH_PIPELINE.md](RESEARCH_PIPELINE.md)
for the active research queue, [VALIDATION.md](VALIDATION.md) for the current confidence
level of important claims, and [CHANGELOG.md](CHANGELOG.md) for material edits. See
[methodology/maintaining-the-corpus.md](methodology/maintaining-the-corpus.md) when
adding or reorganizing research.

## Purpose

This repository collects **general research** that informs CursiveOS: papers,
technical literature, external systems, hardware behavior, software-organism theory,
agent research, operating-system knowledge, economics, and security foundations.

This repository is **not** the implementation specification for CursiveOS. Concrete
organism specs, product architecture, scripts, schemas, runnable experiments,
roadmap execution, and implementation plans belong in the main `CursiveOS` repo.

Chapters are living research documents: they should be corrected directly as
understanding improves. Confidence is tracked separately so a readable chapter
does not imply that every claim has been proven.

## Repository Layout

| Path | Purpose |
| --- | --- |
| `RESEARCH_PIPELINE.md` | Active queue of new research, knowledge gaps, and experimental lift. Start here when deciding what to research next. |
| `chapters/` | Living research chapters organized by topic. Direct edits are expected when research conclusions change. |
| `CHANGELOG.md` | Required dated record of meaningful chapter, methodology, and evidence changes. |
| `VALIDATION.md` | Compact status register for claims that affect implementation or decisions. |
| `sources/original-docx/` | Preserved original Word documents. Treat these as immutable input snapshots. |
| `sources/` | Source links, bibliographies, and provenance records where they improve research quality. |
| `experiments/` | Plans and results for tests worth keeping or repeating. Experimental outputs may later become specs or scripts in the main `CursiveOS` repo. |
| `methodology/` | Lightweight rules for maintaining this corpus. |
| `validation/` | Legacy detailed validation records and optional deep-dive notes. |
| `tools/` | Repeatable conversion and integrity-checking utilities. |

## Working Rule

Preserve the uploaded originals, but do not freeze the chapters. When research
changes what the project should believe:

1. Edit the relevant chapter so it gives the current best research guidance.
2. Add a dated entry to `CHANGELOG.md` explaining what changed and why.
3. Update `VALIDATION.md` when the change depends on an important tested or
   still-uncertain claim.
4. Update `RESEARCH_PIPELINE.md` when the change creates, resolves, or reprioritizes
   research questions.

Long evidence notes and benchmark logs are optional. Create them only when the
detail will matter again.

## Research vs Specs

Use this repo for:

- papers and literature reviews;
- foundational theory;
- external technical references;
- source-backed research synthesis;
- open questions and research gaps;
- experiment plans/results that inform the corpus.

Use the main `CursiveOS` repo for:

- implementation specs;
- product architecture;
- schemas and APIs;
- runnable scripts and daemons;
- release roadmap execution;
- issues, PRs, and build tasks.

When research becomes a concrete build decision, graduate it into the main
`CursiveOS` repo and leave a research trail here.

## Confidentiality

Private team material. Do not publish, redistribute, or copy material outside
approved project channels without authorization.

## Initial Import Status

The initial Word documents were converted into topical Markdown chapters. The
original DOCX files remain the intake record. The chapters may now be revised as
living research; unvalidated imported claims should remain marked as such in
`VALIDATION.md` when they influence current work.
