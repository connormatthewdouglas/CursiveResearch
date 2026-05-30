# CursiveResearch

Living research corpus for the CursiveOS team.

## Start Here

Read [CORPUS_WORKFLOW.md](CORPUS_WORKFLOW.md) first when adding or reorganizing
research. Use [INDEX.md](INDEX.md) for the chapter library,
[RESEARCH_PIPELINE.md](RESEARCH_PIPELINE.md) for the active research queue,
[VALIDATION.md](VALIDATION.md) for important claim status, and
[CHANGELOG.md](CHANGELOG.md) for material edits.

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
| `CORPUS_WORKFLOW.md` | Primary workflow for uploads, papers, corrections, experiments, and minimum recordkeeping. |
| `RESEARCH_PIPELINE.md` | Active queue of new research, knowledge gaps, and experimental lift. Start here when deciding what to research next. |
| `chapters/` | Living research chapters organized by topic. Direct edits are expected when research conclusions change. |
| `papers/` | Peer-research paper library. Full verbatim text is allowed only for rights-cleared papers. |
| `CHANGELOG.md` | Required dated record of meaningful chapter, workflow, and evidence changes. |
| `VALIDATION.md` | Compact status register for claims that affect implementation or decisions. |
| `sources/original-docx/` | Preserved original Word documents. Treat these as immutable input snapshots. |
| `sources/` | Source links, bibliographies, and provenance records where they improve research quality. |
| `experiments/` | Plans and results for tests worth keeping or repeating. Experimental outputs may later become specs or scripts in the main `CursiveOS` repo. |
| `validation/notes/` | Legacy detailed validation records and optional future deep-dive notes. |
| `tools/` | Repeatable conversion and integrity-checking utilities. |

## Working Rule

Preserve uploaded originals and rights-cleared full papers, but do not freeze
the chapters. When research changes what the project should believe:

1. Edit the relevant chapter so it gives the current best research guidance.
2. Add a dated entry to `CHANGELOG.md` explaining what changed and why.
3. Update `VALIDATION.md` when the change depends on an important tested or
   still-uncertain claim.
4. Update `RESEARCH_PIPELINE.md` when the change creates, resolves, or reprioritizes
   research questions.

Long evidence notes and benchmark logs are optional. Create them only when the
detail will matter again.

## Paper Rule

The corpus may store full verbatim papers under `papers/` when the license or
permission clearly allows redistribution. Otherwise, store citations, links,
metadata, and deep paraphrased extractions. Do not use “fair use” as a blanket
reason to mirror whole papers.

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

## Sensitivity

Treat this as sensitive project research even if repository visibility changes.
Do not redistribute copied papers, uploaded source packets, or internal notes
outside approved project channels without authorization.

## Initial Import Status

The initial Word documents were converted into topical Markdown chapters. The
original DOCX files remain the intake record. The chapters may now be revised as
living research; unvalidated imported claims should remain marked as such in
`VALIDATION.md` when they influence current work.
