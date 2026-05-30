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

## Current Paper Areas

| Area | Purpose |
| --- | --- |
| `recursive-self-improvement/` | RSI, self-improving agents, verifier-grounded discovery, agent memory, and open-ended evolution. |

Add new areas as the corpus grows.
