# Maintaining the Research Corpus

## Goal

Build a research library that is easy to expand, difficult to corrupt, and
useful for technical and strategic decisions. Preserve what the team received,
organize what it means, and mark what has actually been verified.

## Organizational Method

The corpus uses a source-to-decision pipeline:

1. **Intake**: add original files as immutable source masters.
2. **Normalize**: convert source material into a readable Markdown chapter or
   append it to the appropriate existing topic.
3. **Register**: record the original file, chapter destination, hash, import
   date, and coverage check in `sources/source-register.md`.
4. **Verify**: check material claims against primary sources, recording the
   verification date, links, and whether the claim is supported, disputed, or
   still uncertain.
5. **Synthesize**: extract findings that affect CursiveOS experiments,
   architecture, security, positioning, or economics.
6. **Decide**: when research becomes a project decision, create a dated
   decision record that cites the verified findings.

## Topic Architecture

Use a small stable set of chapters rather than one file per research session:

| Chapter Area | Belongs Here |
| --- | --- |
| First principles and strategy | Core thesis, differentiation, moat, roadmap reasoning |
| Market and viability | Market size, audiences, competitors, ecosystem conditions |
| Linux kernel optimization | Kernel, scheduler, networking, memory, and OS tuning |
| GPU and accelerator tuning | GPU drivers, frequency/power behavior, hardware-specific optimization |
| AI-guided tuning | Agents, automated experimentation, models, optimization algorithms |
| Security and hardening | Threats, attestation, identity, endpoint and server defense |
| Tokenomics and incentives | Rewards, DePIN comparisons, economics, anti-gaming incentives |

Create a new chapter only when a subject has its own sustained research stream
and cannot be understood cleanly inside an existing chapter.

## Source Preservation Rules

- Never edit or replace a file in `sources/original-docx/`.
- For new original material, keep the original filename unless it creates a
  collision; when it does, prefix the file with the intake date.
- Record a Git blob SHA or SHA-256 hash before converting a source.
- Keep imported wording intact in an initial conversion. Add commentary in
  separately labeled sections, not by overwriting source claims.
- Do not delete a superseded source. Mark its status and link to the replacement.

## Markdown Standards

- Use descriptive filenames in lowercase with hyphens.
- Use a single `#` title and orderly `##` / `###` headings for authored
  additions.
- Put dates in ISO form: `YYYY-MM-DD`.
- Use Markdown tables only where they improve comparison or provenance.
- Use plain links for cited web sources, favoring primary sources.
- Clearly label content as `Source Import`, `Verified Finding`, `Hypothesis`,
  `Recommendation`, `Disputed`, or `Superseded` where that distinction matters.

## Verification Standard

For a claim to be considered verified, record:

| Field | Requirement |
| --- | --- |
| Claim | Specific statement being tested |
| Status | `supported`, `partially supported`, `disputed`, or `unverified` |
| Checked on | Absolute date of verification |
| Evidence | Primary-source URLs, official documentation, repository data, or reproducible benchmark output |
| Implication | Why it matters for CursiveOS, if it does |

Time-sensitive market, product, pricing, project-status, and software-version
claims should never be treated as current without a recent verification date.

## Expansion Workflow

When a team member contributes research:

1. Commit the original source document and update the source register.
2. Convert or integrate it into the relevant chapter.
3. Run `tools/convert_docx_sources.py` for DOCX source conversions.
4. Review generated Markdown for heading readability and table rendering.
5. Add dated verification sections for claims that will drive near-term work.
6. Submit the change for review with a short summary of new evidence and open
   questions.

## Decision Records

As the corpus becomes operational, add a `decisions/` directory. Each decision
record should state the decision, date, owner, evidence used, alternatives
considered, experiments required, and conditions that would reverse it. This
keeps the research corpus from becoming a collection of interesting facts that
never translate into accountable work.
