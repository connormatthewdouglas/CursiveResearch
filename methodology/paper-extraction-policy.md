# Paper Extraction Policy

Status: Supporting detail. Start with
[../CORPUS_WORKFLOW.md](../CORPUS_WORKFLOW.md) and
[../papers/README.md](../papers/README.md) for the current simplified workflow
and full-text storage rule.

## Purpose

The research corpus should not become a link farm. When a paper is important, the corpus should extract enough structure, methods, findings, limitations, and implications that a future agent can understand why the paper matters without rereading the full paper from scratch.

The goal is **high-density research memory**, not minimal summaries.

## Core Principle: Low-Discretion Extraction First

The extractor should not be the sole judge of what matters.

For important papers, first preserve a neutral map of what the paper itself contains. Only after that should the extractor add interpretation, ranking, and corpus relevance.

Every deep extraction should separate:

1. **Paper-faithful extraction** — what the paper says, does, measures, claims, and concludes.
2. **Corpus synthesis** — what we think it means for software organisms, CursiveOS, agents, benchmarks, hardware, or optimization.
3. **Extractor judgment** — what seems important, weak, overclaimed, or transferable.

This prevents an agent from silently discarding details because it guessed they were not important.

## Copyright Boundary

Do not mirror full papers or copy long paper sections verbatim into the repo
unless the paper is rights-cleared under the rule in `papers/README.md`.

Allowed and encouraged:

- full paper text in `papers/` when redistribution rights are clear;
- detailed paraphrase;
- structured notes;
- method reconstruction in our own words;
- tables of claims, mechanisms, experiments, and limitations;
- short quotations when genuinely useful and properly attributed;
- figure/table descriptions in our own words;
- extracted metrics and experimental results with source attribution;
- implications for the corpus.

Avoid:

- copying full abstracts, introductions, methods, or result sections verbatim
  when rights are unclear or restrictive;
- copying large tables wholesale;
- turning the repo into a paper mirror;
- losing the distinction between source text and corpus synthesis.

## Default Extraction Depth

For high-value papers, use a **deep extraction**, not a paragraph summary.

A useful target is roughly:

- 1-3 pages of structured notes for normal papers;
- 3-6 pages for cornerstone papers;
- more only when the paper is foundational and the extraction is mostly original synthesis.

Optimize for useful information, not small file size.

## Required Deep Extraction Structure

For cornerstone papers, use this structure.

```markdown
# <Paper Title> — Deep Extraction

Source: <link>
Authors / Lab: <authors or organization>
Year / Venue: <year, venue, preprint status>
Corpus Status: supported | unvalidated | partially validated | speculative
Extraction Type: cornerstone | important | supporting | lead-only

## 1. Paper Map

List the paper's actual sections and what each section does.

| Paper Section | What It Covers | Why It Exists In The Paper |
| --- | --- | --- |

## 2. Author's Core Claims

Extract the paper's major claims in neutral language before adding our judgment.

| Claim | Where It Appears | Evidence Used By Authors | Extraction Confidence |
| --- | --- | --- | --- |

## 3. System / Method Architecture

Describe the system, algorithm, agent loop, experimental setup, or theoretical mechanism.

Use diagrams in text when useful:

candidate generator
-> evaluator
-> selection
-> archive
-> next candidate

## 4. Key Mechanisms Inventory

List the important mechanisms the paper introduces or uses. Do not include only the mechanisms that seem immediately relevant to CursiveOS; preserve the paper's mechanism set first.

| Mechanism | What It Does | Inputs | Outputs | Why It Matters |
| --- | --- | --- | --- | --- |

## 5. Experimental Setup

Extract the actual experimental design:

- tasks;
- datasets/environments;
- baselines;
- models;
- compute assumptions if available;
- evaluation metrics;
- repetitions/holdouts if available;
- ablations if available.

| Experiment | Task/Environment | Baseline | Metric | What It Tests |
| --- | --- | --- | --- | --- |

## 6. Results Inventory

Extract reported results with numbers when available. Include caveats and uncertainty.

| Result | Metric | Comparison | Author Interpretation | Caveat |
| --- | --- | --- | --- | --- |

## 7. Figures and Tables Inventory

Do not copy figures/tables wholesale. Describe each important figure/table and what information it contains.

| Figure/Table | What It Shows | Important Takeaway | Should Corpus Recreate/Summarize? |
| --- | --- | --- | --- |

## 8. Limitations Stated By Authors

List the limitations the authors explicitly acknowledge.

## 9. Limitations Inferred By Corpus

List limitations or risks the paper does not fully handle.

## 10. Failure Modes and Safety Concerns

Extract any failure modes, negative results, instability, safety caveats, or misuse concerns.

## 11. What Transfers To Software Organisms

Explain what the corpus should learn from the paper.

## 12. What Does Not Transfer

Explain what should not be generalized.

## 13. CursiveOS / Corpus Implications

Research implications only. Do not write implementation specs.

## 14. Open Questions

List questions this paper leaves unresolved.

## 15. Extraction Coverage Notes

State what was extracted deeply and what was not.

Examples:

- All major claims extracted: yes/no.
- All experiments extracted: yes/no.
- All figures/tables inventoried: yes/no.
- Source-level validation complete: yes/no.
- Sections intentionally skipped or compressed: <list and why>.

## 16. Source Reliability

Assess whether this is peer reviewed, a preprint, a technical report, official repo, blog post, or secondary source.
```

## Paper Importance Levels

| Level | Extraction Depth |
| --- | --- |
| Cornerstone | Full deep extraction using the complete template. Must include paper map, claim inventory, experiment inventory, result inventory, figure/table inventory, and coverage notes. |
| Important | Use most of the template; focus on method, claims, results, limitations, and transfer analysis. |
| Supporting | Shorter structured note with relevance and key claims. |
| Lead Only | Link plus one paragraph explaining why it may matter later. |

## Minimum Bar for Cornerstone Papers

A cornerstone paper should usually get:

- paper section map;
- author's major claim inventory;
- architecture/mechanism explanation;
- evaluator/fitness analysis;
- experimental setup;
- reported results table;
- figure/table inventory;
- limitations/failure modes;
- transfer/non-transfer analysis;
- direct research implications;
- extraction coverage notes.

For the recursive self-improvement chapter, cornerstone papers include at least:

- AlphaEvolve;
- FunSearch;
- STOP;
- AI Agents That Matter;
- Voyager;
- AlphaDev or AlphaTensor depending on the research question.

## Figure and Table Handling

Do not copy figures wholesale unless licensing clearly permits and the file is needed.

Instead:

- describe the figure in our own words;
- extract the conceptual flow;
- recreate only simple original diagrams as corpus synthesis;
- attribute the source;
- inventory the figure/table so future agents know what existed even if it was not fully recreated.

For tables:

- do not copy large tables verbatim;
- extract the fields that matter;
- reframe them around corpus questions;
- record if a table was omitted and why.

## Anti-Overfiltering Rule

For cornerstone papers, do not only extract what appears immediately useful to CursiveOS.

Preserve:

- all major claims;
- all experiments;
- all headline results;
- all stated limitations;
- all major mechanisms;
- all important figures/tables as descriptions;
- any negative or null results;
- any safety, cost, compute, scaling, or reproducibility caveats.

Then add a separate section explaining what is most relevant to CursiveOS.

## Extraction Quality Test

A paper extraction is good if a future agent can answer:

1. What did the paper actually do?
2. What sections did the paper contain?
3. What did the authors claim?
4. What was measured?
5. What improved?
6. Who or what judged improvement?
7. What experiments and baselines were used?
8. What results were reported?
9. What limitations did the authors admit?
10. What limitations do we infer?
11. What should the corpus learn?
12. What should the corpus not overclaim?
13. What was intentionally omitted or compressed from the extraction?

If the extraction cannot answer those questions, it is too shallow.
