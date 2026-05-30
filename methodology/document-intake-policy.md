# Document Intake Policy

Status: Supporting detail. Start with
[../CORPUS_WORKFLOW.md](../CORPUS_WORKFLOW.md) for the current simplified
workflow.

## Default Posture

When a contributor provides a research document, the default is **substantial incorporation**.

The corpus should absorb most useful, non-overlapping research from the document. Do not reduce a rich document to a tiny abstract unless the material is mostly duplicate, low-confidence, outside scope, or better suited for the main `CursiveOS` implementation repo.

## Intake Rule

For each uploaded research document:

1. Preserve the original source file or intake record.
2. Compare the document against existing chapters.
3. Add most useful non-overlapping content to the relevant chapter or create a new chapter.
4. Keep strong definitions, taxonomies, frameworks, source leads, caveats, and research conclusions.
5. Merge overlapping material instead of duplicating it.
6. Mark unsupported but important claims as unvalidated when they could shape decisions.
7. Record the intake in `CHANGELOG.md`.
8. Update `RESEARCH_PIPELINE.md` when the document answers or creates research gaps.

## What to Compress or Omit

Compress or omit material only when it is:

- already covered with equal or better clarity;
- weakly supported or speculative without useful framing;
- outside the research corpus scope;
- an implementation/spec detail that belongs in the main `CursiveOS` repo;
- better represented as a summary than copied directly.

## Desired Outcome

A new document should make the corpus meaningfully smarter.

The goal is not to archive everything verbatim. The goal is to convert research packets into durable, readable, source-aware corpus knowledge that future agents can use without rereading the original document from scratch.
