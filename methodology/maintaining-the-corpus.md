# Maintaining the Research Corpus

## Goal

Maintain research that is easy to read, easy to correct, and honest about what
has and has not been confirmed. The corpus is a working tool for building
CursiveOS, not an archival publication workflow.

## Core Rules

1. Preserve supplied originals in `sources/original-docx/`; do not edit those
   files after intake.
2. Treat `chapters/` as living documents. Directly correct or improve chapter
   guidance when new evidence or deployment experience changes the answer.
3. Record meaningful edits in root `CHANGELOG.md`, including the reason and the
   confidence level of the evidence behind the change.
4. Track only important decision-driving claims in root `VALIDATION.md`.
5. Use deeper notes, source tables, or experiment logs only when they are useful
   for repeating a test, investigating risk, or defending a consequential
   decision.

## File Responsibilities

| File / Directory | Responsibility |
| --- | --- |
| `chapters/` | Current readable research and practical guidance. Editable. |
| `CHANGELOG.md` | Required dated record of material edits and their reasons. |
| `VALIDATION.md` | Current validation state for important claims. Keep compact. |
| `sources/original-docx/` | Immutable submitted source snapshots. |
| `sources/source-register.md` | Provenance record for imported source files when needed. |
| `sources/` | Bibliographies or selected source lists that improve research quality. Optional for routine edits. |
| `experiments/` | Repeatable test plans and results that affect decisions. |
| `validation/` | Existing detailed historical records or optional future deep dives; not part of the normal workflow. |
| `decisions/` | Optional records for significant adopted project decisions. |

## Validation Labels

Use these labels in `VALIDATION.md` and, where useful, in a chapter:

| Status | Meaning |
| --- | --- |
| `Unvalidated` | Collected research, proposal, or imported claim that has not been checked enough to rely on. |
| `Supported` | Checked against credible evidence or an initial local observation, but not established broadly enough for a firm conclusion. |
| `Validated` | Confirmed sufficiently for the explicitly stated project decision or deployment scope. |
| `Disproven` | Checked and found wrong or inapplicable for the stated scope. |
| `Superseded` | Previously useful guidance replaced because the environment or conclusion changed. |

A local validation is allowed to be narrow. For example, confirming the context
minimum in the installed Hermes build validates that deployment fact; it does
not validate every performance claim about Hermes or the Arc B70.

## Routine Edit Workflow

When new research or local experience changes a chapter:

1. Edit the chapter directly to make its guidance current and clear.
2. Add an entry to `CHANGELOG.md` describing the changed guidance, why it
   changed, and any important limitation.
3. If the change affects implementation, security, spending, or a project
   decision, add or update one concise row in `VALIDATION.md`.
4. Add links to useful evidence in the changelog or validation row. Do not
   create additional tracking documents unless their detail will be used.

A spelling fix or formatting cleanup does not need a changelog entry. A changed
recommendation, changed technical fact, new risk, or new experiment outcome does.

## Importing New Research

When a contributor provides a document or research package:

1. Save the original file under `sources/original-docx/` and record provenance
   in `sources/source-register.md` when a durable intake record is needed.
2. Convert or integrate the material into the relevant chapter.
3. Mark important claims as `Unvalidated` in `VALIDATION.md` if they might shape
   actual work before being checked.
4. Add a changelog entry describing what was imported and where it landed.

The original file preserves what was received. The Markdown chapter is allowed
to evolve after import; it does not need to preserve outdated wording.

## When To Validate

Validate a claim when it may affect:

- implementation direction or agent configuration;
- safety, security, permissions, or unattended execution;
- hardware/software purchases or deployment commitments;
- reported performance or comparisons used to choose a stack;
- current product, market, pricing, or software-version facts.

Prefer official documentation, source code, upstream repositories, and repeatable
local observations. A single local check may validate a narrow configuration
fact, but an unstable performance claim generally remains `Supported` until
repeated under controlled conditions.

## Evidence Depth

Use the least documentation that preserves understanding:

| Situation | Normal Documentation |
| --- | --- |
| Chapter wording or recommendation changes | Chapter edit plus `CHANGELOG.md` entry. |
| Important fact checked for current work | Add/update a `VALIDATION.md` row. |
| Reproducible measurement or troubleshooting session worth retaining | Add an experiment result and link it from `VALIDATION.md` or `CHANGELOG.md`. |
| High-risk or contested decision | Optional detailed note or decision record. |

Do not require source IDs, claim IDs, reliability tiers, or separate validation
notes for normal research maintenance. They may be used selectively when they
make a difficult decision clearer.

## Existing Detailed Records

Earlier work created `sources/extracted-source-index.md`,
`validation/validation-ledger.md`, and detailed notes under `validation/notes/`.
These files remain useful historical evidence, but they are no longer mandatory
steps or the primary status view. New readers should start with `VALIDATION.md`
and `CHANGELOG.md`.

## Decision Records

For a significant adopted decision, an optional record under `decisions/` may
state the decision, date, evidence, alternatives, risks, and reversal triggers.
Do this when it improves accountability, not as a prerequisite for improving a
chapter.
