# Paper Extraction Policy

Status: Active corpus policy.

## Purpose

The research corpus should not become a link farm. When a paper is important, the corpus should extract enough structure, methods, findings, limitations, and implications that a future agent can understand why the paper matters without rereading the full paper from scratch.

The goal is **high-density research memory**, not minimal summaries.

## Copyright Boundary

Do not mirror full papers or copy long paper sections verbatim into the repo.

Allowed and encouraged:

- detailed paraphrase;
- structured notes;
- method reconstruction in our own words;
- tables of claims, mechanisms, experiments, and limitations;
- short quotations when genuinely useful and properly attributed;
- figure/table descriptions in our own words;
- extracted metrics and experimental results with source attribution;
- implications for the corpus.

Avoid:

- copying full abstracts, introductions, methods, or result sections verbatim;
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

## Extraction Template

For each important paper, extract:

```markdown
## <Paper Title>

Source: <link>
Authors / Lab: <authors or organization>
Year / Venue: <year, venue, preprint status>
Corpus Status: supported | unvalidated | partially validated | speculative

### Why This Paper Matters

Explain why this source is worth corpus space.

### Core Thesis

State the paper's central claim in plain language.

### System / Method Architecture

Describe the system, algorithm, agent loop, experimental setup, or theoretical mechanism.

Use diagrams in text when useful:

candidate generator
-> evaluator
-> selection
-> archive
-> next candidate

### Key Mechanisms

List the important mechanisms the paper introduces or uses.

| Mechanism | What It Does | Why It Matters |
| --- | --- | --- |

### Experimental Setup

Extract the actual experimental design:

- tasks;
- datasets/environments;
- baselines;
- models;
- compute assumptions if available;
- evaluation metrics;
- repetitions/holdouts if available.

### Reported Results

Summarize the important reported results with numbers when available.

| Result | Metric | Comparison | Caveat |
| --- | --- | --- | --- |

### Limitations and Failure Modes

What the paper admits, what it does not test, and what could fail.

### What Transfers to Software Organisms

Explain what the corpus should learn from the paper.

### What Does Not Transfer

Explain what should not be generalized.

### CursiveOS / Corpus Implications

Research implications only. Do not write implementation specs.

### Open Questions

List questions this paper leaves unresolved.

### Source Reliability

Assess whether this is peer reviewed, a preprint, a technical report, official repo, blog post, or secondary source.
```

## Paper Importance Levels

| Level | Extraction Depth |
| --- | --- |
| Cornerstone | Full deep extraction using the complete template. |
| Important | Use most of the template; focus on method/results/limitations. |
| Supporting | Shorter structured note with relevance and key claims. |
| Lead Only | Link plus one paragraph explaining why it may matter later. |

## Minimum Bar for Cornerstone Papers

A cornerstone paper should usually get:

- architecture/mechanism explanation;
- evaluator/fitness analysis;
- experimental setup;
- reported results table;
- limitations/failure modes;
- transfer/non-transfer analysis;
- direct research implications.

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
- attribute the source.

For tables:

- do not copy large tables verbatim;
- extract the fields that matter;
- reframe them around corpus questions.

## Extraction Quality Test

A paper extraction is good if a future agent can answer:

1. What did the paper actually do?
2. What was measured?
3. What improved?
4. Who or what judged improvement?
5. What are the limitations?
6. What should the corpus learn?
7. What should the corpus not overclaim?

If the extraction cannot answer those questions, it is too shallow.
