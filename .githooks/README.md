# Corpus guardrail hooks

Git hooks that protect the corpus from automated-agent damage. Created after
the 2026-06-16 incident, where an automated contributor (Grok) replaced the
entire 352-line Chapter 03 with a one-line LLM placeholder
(`# [full new content would go here but for brevity]`) and committed it with
no validation.

## Enable (once per clone — required for the automation host too)

```bash
git config core.hooksPath .githooks
```

That is the only setup step. Hooks are version-controlled here, so every clone
that runs the command gets them.

## What they block

- **`pre-commit`** — staged content containing lazy-elision placeholders
  ("full content would go here", "for brevity", "rest of the chapter
  unchanged", etc.).
- **`commit-msg`** — any tracked `.md` that loses >40% of its lines in one
  commit (silent full-file shrinkage).

## Overrides

- Intentional large rewrite: start the commit message with `REWRITE:` (or set
  `CORPUS_REWRITE=1`).
- True emergency bypass of all hooks: `git commit -n`.

## For the automation (Grok)

The host running automated corpus edits must run the enable command once. Prefer
**append/section-scoped edits** over full-file rewrites — "deepen this chapter"
operations are what triggered the incident. If a rewrite is genuinely needed,
emit the complete file and use the `REWRITE:` message prefix so the shrink guard
is satisfied by intent rather than bypassed blindly.
