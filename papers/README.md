# Peer Research Paper Library

This directory stores papers and deep paper extractions for the CursiveResearch
corpus.

## Goal

Keep fewer papers with more useful detail.

It is better to deeply preserve and extract a handful of important,
rights-cleared papers than to intake one hundred papers as shallow summaries
that future agents cannot use.

## Folder Standard

Use this layout:

```text
papers/<field>/<paper-slug>/
  README.md
  paper.md              # only when full text is rights-cleared
  paper.pdf             # only when storage rights are clear and binary import is useful
  deep-extraction.md
  claims-and-results.md
  figures-and-tables.md
```

Only create the files that are useful. A cornerstone paper should usually have a
deep extraction. A rights-cleared paper may also have full text.

## Full-Text Rule

Full verbatim paper text may be stored here only when one of these is true:

- the paper is licensed for redistribution, such as CC BY, CC BY-SA, CC0,
  public domain, or another explicit compatible license;
- the paper text is released under a permissive software/documentation license;
- the authors or publisher grant permission;
- the team owns the rights or provides a rights-cleared copy.

When full text is stored, preserve attribution and license information in the
paper folder `README.md`.

If rights are unclear or restrictive, do not store the full text. Store:

- citation and links;
- license/access notes;
- deep paraphrased extraction;
- claims/results inventory;
- figure/table descriptions in our own words.

## What “Fair Use” Means Here

Do not treat “fair use” as permission to mirror a full paper. Fair use can be
context-dependent and uncertain. The corpus policy is stricter and cleaner:

```text
rights-cleared -> full text allowed
not rights-cleared -> extraction and citation only
```

Short quoted excerpts may be used when needed for commentary, but long verbatim
reproduction belongs only in rights-cleared paper folders.

## Importance Levels

| Level | Treatment |
| --- | --- |
| Cornerstone | Paper folder, source metadata, deep extraction, claims/results, figure/table inventory; full text if rights-cleared. |
| Important | Paper folder or source entry; structured extraction focused on method, claims, results, limitations, and transfer. |
| Supporting | Source list entry plus concise structured note. |
| Lead Only | Link, citation, and one reason it may matter later. |

## Deep Extraction Template

Use this for cornerstone papers and important papers where shallow summaries
would destroy the value.

```markdown
# <Paper Title> — Deep Extraction

Source: <link>
Authors / Lab: <authors or organization>
Year / Venue: <year, venue, preprint status>
Corpus Status: supported | unvalidated | partially validated | speculative
Extraction Type: cornerstone | important | supporting | lead-only
Rights Status: full-text allowed | extraction only | unknown

## 1. Paper Map

| Paper Section | What It Covers | Why It Exists In The Paper |
| --- | --- | --- |

## 2. Author's Core Claims

| Claim | Where It Appears | Evidence Used By Authors | Extraction Confidence |
| --- | --- | --- | --- |

## 3. System / Method Architecture

Describe the algorithm, agent loop, system, experimental setup, or theoretical
mechanism. Use plain text diagrams when helpful.

## 4. Key Mechanisms Inventory

| Mechanism | What It Does | Inputs | Outputs | Why It Matters |
| --- | --- | --- | --- | --- |

## 5. Experimental Setup

Capture tasks, datasets/environments, baselines, models, compute assumptions,
metrics, repetitions/holdouts, and ablations where available.

| Experiment | Task/Environment | Baseline | Metric | What It Tests |
| --- | --- | --- | --- | --- |

## 6. Results Inventory

| Result | Metric | Comparison | Author Interpretation | Caveat |
| --- | --- | --- | --- | --- |

## 7. Figures and Tables Inventory

Describe figures/tables in our own words. Do not copy large tables unless the
rights-cleared full-text rule allows it and the table is needed.

| Figure/Table | What It Shows | Important Takeaway | Should Corpus Recreate/Summarize? |
| --- | --- | --- | --- |

## 8. Limitations Stated By Authors

## 9. Limitations Inferred By Corpus

## 10. Failure Modes and Safety Concerns

## 11. What Transfers To Software Organisms

## 12. What Does Not Transfer

## 13. CursiveOS / Corpus Implications

Research implications only. Do not write implementation specs here.

## 14. Open Questions

## 15. Extraction Coverage Notes

- All major claims extracted: yes/no
- All experiments extracted: yes/no
- All figures/tables inventoried: yes/no
- Source-level validation complete: yes/no
- Sections intentionally skipped or compressed: <list and why>

## 16. Source Reliability

Assess whether this is peer reviewed, a preprint, a technical report, official
repo, blog post, or secondary source.
```

## Extraction Quality Test

A useful paper extraction lets a future agent answer:

1. What did the paper actually do?
2. What sections did the paper contain?
3. What did the authors claim?
4. What was measured?
5. What improved?
6. Who or what judged improvement?
7. What experiments and baselines were used?
8. What limitations did the authors admit?
9. What limitations do we infer?
10. What should the corpus learn?
11. What should the corpus not overclaim?
12. What was intentionally omitted or compressed?

## Current Paper Areas

| Area | Purpose |
| --- | --- |
| `recursive-self-improvement/` | RSI, self-improving agents, verifier-grounded discovery, agent memory, and open-ended evolution. |
| `agent-evaluation/` | Benchmarks and evaluation methods for software agents, computer-use agents, OS agents, and grounded task success. |
| `software-engineering-agents/` | Agent-computer interfaces, software-fixing agents, repository navigation, and code-editing workflows. |

Add new areas as the corpus grows.
