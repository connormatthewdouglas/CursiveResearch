# Research Changelog

This file records meaningful changes to research guidance, validation status,
and corpus process. It is intended to be readable without reconstructing a
chain of supporting documents.

## 2026-05-26 - Simplified the Corpus Workflow

Changed:

- Made chapters living research documents that may be edited directly as the
  project learns more.
- Made this changelog the required record for material research edits.
- Added `VALIDATION.md` as the compact status page for important claims.
- Replaced the required source-index/ledger/note pipeline with optional deep
  evidence records only when useful.
- Retired `validation/validation-ledger.md` as an active workflow document; it
  now points readers to the compact status page and retained supporting notes.
- Retained original uploaded documents as immutable intake snapshots.

Reason:

The previous method made a straightforward operational correction difficult to
follow. The project needs clear current guidance, a detailed edit history, and
a visible distinction between confirmed and uncertain claims, without mandatory
paperwork for every correction.

## 2026-05-26 - Chapter 09 Hermes Context and Tooling Guidance

Changed:

- Recorded that the current local Hermes deployment cannot use an approximately
  8k configured context window: its inspected implementation enforces a 64,000
  token minimum and the active configuration uses 65,536.
- Updated the Arc B70 benchmark plan so current Hermes testing keeps its required
  context window and instead varies active prompt, tool-schema, and history
  payload size.
- Documented the local risk that unattended execution currently reaches the
  host through a local terminal backend; the observed mutating repo-hygiene cron
  task was paused.

Evidence and confidence:

| Finding | Status | Evidence |
| --- | --- | --- |
| Current Hermes build requires at least 64,000 configured tokens and is configured for 65,536. | Validated for the inspected local deployment | Local Hermes source and `~/.hermes/config.yaml` inspection on 2026-05-26. |
| Reducing active tool/schema payload may improve responsiveness. | Supported, not validated | Initial tool-envelope diagnostic observations; uncontrolled cache state and no repeated benchmark. |
| Basic structured tool calls can be returned through the current OVMS/parser path. | Supported, not broadly validated | Initial local calls for `read_file`, `skills_list`, and `session_search`. |
| Current unattended execution is sufficiently contained for host mutation. | Disproven for the inspected setup | Local terminal backend and observed scheduled repository mutation. |

Supporting detail retained for reference:

- `experiments/results/2026-05-26-hermes-ovms-tool-envelope-smoke-test.md`
- `validation/notes/2026-05-26-ch09-local-hermes-deployment-inspection.md`
- `experiments/arc-b70-local-agent-benchmark-plan.md`

Note: before the workflow was simplified, Chapter 09 was first edited in a way
that treated its imported wording as immutable, then restored with a dated
correction appendix. That appendix remains an accurate record of the Hermes
finding; future chapter improvements may directly rewrite guidance while being
recorded here.

## 2026-05-26 - Chapter 09 Imported

Changed:

- Added `chapters/09-local-agent-arc-b70.md` from the uploaded Arc B70 local
  agent research document.
- Preserved the submitted document under `sources/original-docx/` and recorded
  its provenance in the existing source records.

Validation status:

Most imported hardware, runtime-performance, model-selection, and tool-calling
claims were not validated at import time. Important current claims are tracked
in `VALIDATION.md`.
