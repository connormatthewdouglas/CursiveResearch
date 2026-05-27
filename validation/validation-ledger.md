# Legacy Research Validation Ledger

This file has been retired as an active workflow document.

The current validation status for claims that affect CursiveOS work is maintained
in [`../VALIDATION.md`](../VALIDATION.md). Material research and methodology
changes are recorded in [`../CHANGELOG.md`](../CHANGELOG.md).

## Why This Changed

The original ledger required readers to trace source IDs, validation passes, and
separate note files before they could understand a practical correction. The
corpus now uses a simpler rule: edit chapters as living documents, record
meaningful edits in the changelog, and track only decision-driving uncertainty
in the compact validation page.

## Historical Records Retained

Detailed validation notes already created remain under `validation/notes/`, and
experiment logs remain under `experiments/results/`. Earlier versions of this
ledger remain in Git history if the full validation-pass table is needed for an
audit.

For the Chapter 09 Hermes work that triggered this change, use:

- `../VALIDATION.md`
- `../CHANGELOG.md`
- `notes/2026-05-26-ch09-local-hermes-deployment-inspection.md`
- `../experiments/results/2026-05-26-hermes-ovms-tool-envelope-smoke-test.md`

No future routine chapter edit is required to update this legacy ledger.
