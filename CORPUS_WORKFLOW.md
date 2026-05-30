# Corpus Workflow

Status: Primary workflow for adding and maintaining research.

This file is the front door. The older methodology files remain as supporting
detail, but new contributors and agents should start here.

## Operating Principle

The corpus should preserve source material, make important research easy to
read, and avoid compressing rich work into nothing.

Default behavior:

```text
preserve the source
-> place it in the right library
-> integrate useful non-overlapping content into chapters
-> extract deeply for important papers
-> record only the process details that future agents will actually need
```

## Repository Map

| Location | Use |
| --- | --- |
| `INDEX.md` | Human reading path through the chapter library. |
| `RESEARCH_PIPELINE.md` | Active queue of missing research, knowledge gaps, and experiments. |
| `VALIDATION.md` | Compact status of claims that can affect decisions. |
| `CHANGELOG.md` | Required dated record of meaningful corpus changes. |
| `chapters/` | Living topic chapters. Edit these when the corpus learns. |
| `papers/` | Peer-research paper library. Full text is allowed only for rights-cleared papers. |
| `sources/original-docx/` | Original uploaded Word documents and source snapshots. |
| `sources/intake/` | Intake records for uploaded research packets. |
| `sources/` | Bibliographies, source lists, and provenance records. |
| `experiments/` | Research experiment plans and results worth retaining. |
| `methodology/` | Supporting policy details. |
| `validation/` | Historical detailed validation notes; optional for new work. |

## Intake Decision Tree

### 1. Uploaded Document Or Research Packet

Use this for `.docx`, `.md`, `.pdf`, copied notes, chat exports, or team research
packets.

1. Preserve the original in the closest source folder:
   - Word docs: `sources/original-docx/`
   - Research packet markdown: `sources/intake/`
   - Other original formats: create a clear folder under `sources/original/`
2. Add or update a source/register note only when provenance matters later.
3. Read against existing chapters.
4. Add useful non-overlapping content to the relevant chapter.
5. Keep strong definitions, taxonomies, frameworks, caveats, source leads, and
   research conclusions.
6. Compress only when material is duplicate, low-confidence, outside scope, or
   better suited for the main `CursiveOS` implementation repo.
7. Mark decision-driving uncertainty in `VALIDATION.md`.
8. Record the import in `CHANGELOG.md`.

### 2. Peer Research Paper

Use this for papers, preprints, technical reports, and academic/research-lab
publications.

1. Check the license or permission status.
2. If full text is rights-cleared, store it in `papers/<field>/<paper-slug>/`.
3. If full text is not rights-cleared, store metadata and a deep extraction
   instead of the paper text.
4. Add the paper to the relevant source list.
5. Integrate the lesson into the relevant chapter.
6. Use the deep extraction template for cornerstone or important papers.

See [papers/README.md](papers/README.md) for the full-text rule.

### 3. New Fact Or Correction

Use this for a corrected claim, new source, changed project state, or validation
finding.

1. Edit the relevant chapter directly.
2. Add a changelog entry if the change is meaningful.
3. Update `VALIDATION.md` if the claim affects implementation, spending,
   safety, security, performance, or product direction.
4. Add a deeper note only if future agents will need the full evidence trail.

### 4. Experiment Or Local Observation

Use this for benchmark plans, test runs, local debugging, hardware probes, or
repeatable observations.

1. Put plans/results in `experiments/`.
2. Link important outcomes from `VALIDATION.md` or `CHANGELOG.md`.
3. Graduate executable scripts, schemas, or build tasks to the main `CursiveOS`
   repo.

## Paper Storage Rule

The corpus may store full verbatim paper text only when one of these is true:

- the paper is under a license that permits copying and redistribution, such as
  CC BY, CC BY-SA, CC0, public domain, MIT/BSD/Apache-style text release, or
  another explicit compatible license;
- the authors/publisher provide explicit permission;
- the user/team owns the rights or provides a rights-cleared copy for internal
  corpus use.

Otherwise, do not mirror the full paper. Store a citation, link, metadata, and a
deep paraphrased extraction.

Do not use “fair use” as a blanket reason to copy whole papers. Fair use is a
legal defense, not a clean corpus policy.

## Extraction Depth

Avoid two bad extremes:

- link hoarding with no usable research memory;
- tiny summaries that erase the paper.

For important papers, extract enough that a future agent can answer:

- What did the paper do?
- What did it claim?
- What was measured?
- What improved?
- What judged improvement?
- What experiments, baselines, and metrics were used?
- What failed or remained limited?
- What transfers to CursiveOS/software organisms?
- What should not be overclaimed?

## Chapter Editing Rule

Chapters are living documents. They do not need to preserve every old sentence
forever because the source folders preserve the input record.

When integrating new material:

- keep useful frameworks and detail;
- merge overlapping content instead of duplicating it;
- label uncertainty where it matters;
- do not rewrite research into implementation specs;
- graduate concrete build work to the main `CursiveOS` repo.

## Minimal Required Recordkeeping

For most meaningful research changes, do only this:

1. Update the chapter or paper folder.
2. Update `CHANGELOG.md`.
3. Update `VALIDATION.md` only for decision-driving claims.
4. Update `RESEARCH_PIPELINE.md` only if priorities changed.

That is enough. Extra ledgers, notes, and source tables are optional when they
help preserve evidence or repeat a consequential result.
