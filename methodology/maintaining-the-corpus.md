# Maintaining the Research Corpus

## Goal

Build a research library that is easy to expand, difficult to corrupt, and
useful for technical and strategic decisions. Preserve what the team received,
organize what it means, extract the sources it relies on, and mark what has
actually been verified.

The corpus should not become a pile of impressive-sounding claims. It should
become a traceable evidence system: source master -> extracted source -> claim
validation -> finding -> decision.

## Organizational Method

The corpus uses a source-to-decision pipeline:

1. **Intake**: add original files as immutable source masters.
2. **Normalize**: convert source material into a readable Markdown chapter or
   append it to the appropriate existing topic.
3. **Register source masters**: record the original file, chapter destination,
   hash, import date, and coverage check in `sources/source-register.md`.
4. **Extract cited sources**: pull URLs, papers, repos, standards, docs,
   benchmark articles, vendor pages, and internal benchmark artifacts into
   `sources/extracted-source-index.md` with stable `SRC-*` IDs.
5. **Verify claims**: check material claims against primary sources, official
   documentation, upstream repos, reproducible benchmark output, or strong
   secondary sources. Record status, date, agent/reviewer, and evidence.
6. **Log validation work**: update `validation/validation-ledger.md` every time
   a chapter, section, or claim group is checked.
7. **Synthesize findings**: extract findings that affect CursiveOS experiments,
   architecture, security, positioning, or economics.
8. **Decide**: when research becomes a project decision, create a dated
   decision record that cites the verified findings.

## Topic Architecture

Use a small stable set of chapters rather than one file per research session:

| Chapter Area | Belongs Here |
| --- | --- |
| Research master / snapshot | Historical repo state, mixed source imports, transitional summaries |
| First principles and strategy | Core thesis, differentiation, moat, roadmap reasoning |
| Market and viability | Market size, audiences, competitors, ecosystem conditions |
| Linux kernel optimization | Kernel, scheduler, networking, memory, and OS tuning |
| GPU and accelerator tuning | GPU drivers, frequency/power behavior, hardware-specific optimization |
| AI-guided tuning | Agents, automated experimentation, models, optimization algorithms |
| Security and hardening | Threats, attestation, identity, endpoint and server defense |
| Tokenomics and incentives | Rewards, DePIN comparisons, economics, anti-gaming incentives |
| Firmware and BIOS control | UEFI, BIOS settings, BMC/Redfish, boot control, firmware mutation |

Create a new chapter only when a subject has its own sustained research stream
and cannot be understood cleanly inside an existing chapter.

## File Responsibilities

| File / Directory | Responsibility |
| --- | --- |
| `sources/original-docx/` | Immutable source masters. Do not edit. |
| `sources/source-register.md` | Provenance and conversion coverage for source masters. |
| `sources/extracted-source-index.md` | Canonical list of external sources cited by the corpus. |
| `chapters/` | Human-readable research chapters. May contain imported text, original synthesis, verification sections, and recommendations. |
| `validation/validation-ledger.md` | Log of what was fact checked, when, by whom/what agent, and with what status. |
| `validation/notes/` | Optional detailed validation notes for chapters, sections, or claim clusters. |
| `decisions/` | Future decision records based on verified findings. |
| `tools/` | Repeatable conversion, extraction, and integrity utilities. |

## Source Preservation Rules

- Never edit or replace a file in `sources/original-docx/`.
- For new original material, keep the original filename unless it creates a
  collision; when it does, prefix the file with the intake date.
- Record a Git blob SHA or SHA-256 hash before converting a source.
- Keep imported wording intact in an initial conversion. Add commentary in
  separately labeled sections, not by overwriting source claims.
- Do not delete a superseded source. Mark its status and link to the replacement.
- Do not treat source-master provenance as evidence validation. A DOCX being
  imported only proves that the corpus preserved the submitted document; it does
  not prove the claims inside it.

## Extracted Source Rules

Each external source should receive a stable source ID in
`sources/extracted-source-index.md`.

Recommended format:

```text
SRC-<chapter-number>-<three-digit-sequence>
```

Examples:

```text
SRC-03-001
SRC-05-014
SRC-08-003
```

When extracting sources:

- Prefer canonical URLs: official documentation, upstream repos, standards,
  paper DOI/arXiv pages, vendor docs, or reproducible benchmark artifacts.
- Resolve converted bracket citations like `[1]` or `[66†L75-L83]` back to real
  sources where possible.
- Record date accessed.
- Assign a reliability tier.
- List the exact chapter/section where the source is used.
- Summarize which claim(s) the source is supposed to support.
- Mark extraction separately from validation.

## Reliability Tiers

| Tier | Source Type | Use |
| --- | --- | --- |
| A | Primary sources: official docs, standards, kernel docs, vendor docs, upstream repos, reproducible internal benchmarks | Preferred basis for verified technical claims. |
| B | Peer-reviewed papers, arXiv/preprints with code, reputable technical publications, high-quality benchmark labs | Strong evidence, but check methodology and date. |
| C | News articles, market analysis, blog posts, ecosystem commentary, exchange/crypto explainers | Useful for context; avoid using alone for technical decisions. |
| D | Forums, unsourced claims, social media, speculative reports, AI-generated research docs without source verification | Leads only; not decision-grade. |

## Markdown Standards

- Use descriptive filenames in lowercase with hyphens.
- Use a single `#` title and orderly `##` / `###` headings for authored
  additions.
- Put dates in ISO form: `YYYY-MM-DD`.
- Use Markdown tables only where they improve comparison or provenance.
- Use plain links for cited web sources, favoring primary sources.
- Clearly label content as `Source Import`, `Original Synthesis`, `Verified
  Finding`, `Hypothesis`, `Recommendation`, `Disputed`, or `Superseded` where
  that distinction matters.
- Avoid quietly rewriting imported claims. Append corrections or supersession
  notes instead.

## Verification Standard

For a claim to be considered verified, record:

| Field | Requirement |
| --- | --- |
| Claim ID | Stable identifier, e.g. `CL-03-001`. |
| Claim | Specific statement being tested. |
| Status | `supported`, `partially supported`, `disputed`, `unverified`, `stale`, or `superseded`. |
| Checked on | Absolute date of verification. |
| Agent / Reviewer | Model, tool, or human reviewer who checked it. |
| Evidence | Source IDs plus primary-source URLs, official documentation, repository data, or reproducible benchmark output. |
| Implication | Why it matters for CursiveOS, if it does. |
| Required Change | Any wording correction, narrowing, or follow-up experiment. |

Time-sensitive market, product, pricing, project-status, and software-version
claims should never be treated as current without a recent verification date.

## Validation Workflow

For each chapter:

1. Identify material claims that affect architecture, experiments, security,
   economics, positioning, or roadmap decisions.
2. Extract all cited external sources into `sources/extracted-source-index.md`.
3. Assign reliability tiers.
4. Check claims against primary sources first.
5. If only secondary sources exist, mark the claim as lower-confidence.
6. Record a validation pass in `validation/validation-ledger.md`.
7. Add detailed notes under `validation/notes/` when the verification work is too
   detailed for the ledger.
8. Update the chapter with a dated `Verified Finding`, `Correction`, or
   `Superseded` section when needed.

## Validation Note Template

Use this structure for detailed notes:

```markdown
# Validation Note: <chapter or claim group>

Date checked: YYYY-MM-DD
Agent / reviewer: <name>
Scope: <specific section, claim group, or chapter>
Status: supported | partially supported | disputed | unverified | stale
Source IDs: SRC-XX-001, SRC-XX-002

## Claims Checked

| Claim ID | Claim | Status | Evidence | Notes / Required Rewrite |
| --- | --- | --- | --- | --- |
| CL-XX-001 | ... | supported | SRC-XX-001 | ... |

## Implications for CursiveOS

- ...

## Follow-up

- ...
```

## Expansion Workflow

When a team member contributes research:

1. Commit the original source document and update the source register.
2. Convert or integrate it into the relevant chapter.
3. Run `tools/convert_docx_sources.py` for DOCX source conversions.
4. Review generated Markdown for heading readability and table rendering.
5. Extract cited sources into the source index.
6. Add dated verification sections for claims that will drive near-term work.
7. Update the validation ledger.
8. Submit the change for review with a short summary of new evidence and open
   questions.

## Decision Records

As the corpus becomes operational, add a `decisions/` directory. Each decision
record should state the decision, date, owner, evidence used, alternatives
considered, experiments required, and conditions that would reverse it. This
keeps the research corpus from becoming a collection of interesting facts that
never translate into accountable work.
