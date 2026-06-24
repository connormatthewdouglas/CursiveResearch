# Atomic org: merge Ch03+Ch04, split Ch07 -> 07 + 07b
param(
    [string]$RepoRoot = (Split-Path $PSScriptRoot -Parent)
)

$ErrorActionPreference = 'Stop'
$chapters = Join-Path $RepoRoot 'chapters'

$ch03Path = Join-Path $chapters '03-peer-reviewed-research-recursive-self-improvement-and-agentic-evolution.md'
$ch04Path = Join-Path $chapters '04-foundations-of-software-organisms-rsi-critical-synthesis.md'
$mergedPath = Join-Path $chapters '03-rsi-literature-and-organism-synthesis.md'
$ch07Path = Join-Path $chapters '07-main-repo-gap-closure-and-research-backlog.md'
$ch07aPath = Join-Path $chapters '07-main-repo-gap-closure.md'
$ch07bPath = Join-Path $chapters '07b-research-backlog-and-pipeline.md'

if (-not (Test-Path $ch03Path)) { throw "Missing $ch03Path" }
if (-not (Test-Path $ch04Path)) { throw "Missing $ch04Path" }
if (-not (Test-Path $ch07Path)) { throw "Missing $ch07Path" }

# --- Merge Ch03 + Ch04 ---
$ch03 = Get-Content $ch03Path -Raw
$ch04 = Get-Content $ch04Path -Raw

$livingLayer = @'
## Corpus status (living layer)

**Last reconciled:** 2026-06-24
**Confidence:** Structured digest Supported; organism framework Supported; individual paper claims require source-level validation per intake
**Read with:** [Chapter 00](00-benchmark-schema-and-measurement-validity.md), [Chapter 05](05-measurement-daemon-and-natural-language-shell.md), [Chapter 06](06-mutation-safety-and-permission-law.md), `papers/README.md`

### Authoritative for
- Demonstrated vs speculative RSI claims in current literature (Part A)
- Software-organism definitions, metabolism/sensing/selection framing, failure modes (Part B)
- Verifier/fitness/archive framing and 25-paper library cross-links

### Superseded or narrowed
- Unbounded RSI / fast-takeoff narratives — not supported by cited literature
- Imported performance magnitudes without Ch00 harness validation

### Open until experiment/hardware
- Source-level validation of each P0 paper claim against full text
- Formal mapping from organism taxonomy to Ch06 mutation classes
- Graduation of proposer-vs-random experiment (`experiments/proposer-vs-random-tuning-experiment.md`)

---

## Reinforced research (2026-06-24)

- **2024–2025 agent evaluation:** Kapoor et al., *AI Agents That Matter* — `papers/agent-evaluation/ai-agents-that-matter/`; corpus P0 guardrail for Ch05 shell evaluation.
- **Evolutionary code discovery:** Google DeepMind AlphaEvolve (2025) — `papers/recursive-self-improvement/alphaevolve/`; LLM+evolution with external verifier mirrors CursiveRoot selection.
- **Darwin Gödel Machine:** Sakana AI (2025) — `papers/recursive-self-improvement/darwin-godel-machine/`; open-ended code evolution with empirical gates.
- **Open-endedness without collapse:** Lehman et al., ICML 2024 — `papers/recursive-self-improvement/open-endedness-icml-2024/`; utility constraints required for CursiveOS selection.
- **OS-agent realism:** OSWorld (NeurIPS 2024) — `papers/agent-evaluation/osworld/`; VM-backed computer-use tasks for shell benchmark design.
- **Measurement-grounded fitness:** Chapter 00 validity assessment — stack-delta decomposition and hardware-scoped cold-start are live instances of organism fitness tests.

---

'@

# Extract Ch03 body (from first # heading)
$ch03BodyStart = $ch03.IndexOf("# Peer-Reviewed Research:")
if ($ch03BodyStart -lt 0) { $ch03BodyStart = $ch03.IndexOf("# Peer-Reviewed Research") }
$ch03Body = $ch03.Substring($ch03BodyStart)
$ch03Body = $ch03Body -replace 'See \[Chapter 04\]\(04-foundations-of-software-organisms-rsi-critical-synthesis\.md\) for organism-framing synthesis beyond this digest\.', 'Part B below preserves the uploaded organism framework synthesis (formerly Chapter 04).'

# Extract Ch04 body
$ch04BodyStart = $ch04.IndexOf("# Foundations of Software Organisms:")
if ($ch04BodyStart -lt 0) { $ch04BodyStart = $ch04.IndexOf("# Foundations of Software Organisms") }
$ch04Body = $ch04.Substring($ch04BodyStart)
$ch04Body = $ch04Body -replace 'Status: Substantial intake synthesis from uploaded research document.*?\r?\n\r?\n', "Status: Part B of merged Chapter 03 (formerly standalone Chapter 04). `r`n`r`n"
$ch04Body = $ch04Body -replace 'This chapter complements Chapter 03\. Chapter 03 is the paper/system digest; this chapter preserves', 'This section preserves'
$ch04Body = $ch04Body -replace 'Related digest: `chapters/03-peer-reviewed-research-recursive-self-improvement-and-agentic-evolution\.md`\r?\n\r?\n', ''
$ch04Body = $ch04Body -replace '> \*\*Corpus inline \(2026-06-24\):\*\* Paper-level evidence lives in \*\*Chapter 03\*\* \(digest \+ 25 `papers/` intakes\)\. This chapter preserves the uploaded \*\*framework\*\* \(definitions, ALife lessons\)\. Merge analysis: complementary roles — not merged \(`sources/corpus-organization-decisions-2026-06-24\.md`\)\. Live fitness examples: Ch00 stack-delta \+ hardware-scoped cold-start\.\r?\n\r?\n', ''

$mergedTitle = @'
# RSI Literature and Organism Synthesis

Status: **Merged chapter (2026-06-24)** — combines peer-reviewed literature digest (formerly Ch03) and software-organism critical synthesis (formerly Ch04). Preserves both intake blocks; deduplicates navigation only.

---

## Part A — Peer-Reviewed Literature Digest

'@

$partBSeparator = @'

---

## Part B — Software Organism Critical Synthesis

'@

$merged = $livingLayer + $mergedTitle + ($ch03Body -replace '^# Peer-Reviewed Research: Recursive Self-Improvement and Agentic Evolution\r?\n\r?\nStatus: Structured research digest\.[^\r\n]*\r?\n\r?\nSource list:[^\r\n]*\r?\nIntake record:[^\r\n]*\r?\n\r?\n', '') + $partBSeparator + ($ch04Body -replace '^# Foundations of Software Organisms: Recursive Self-Improvement Critical Synthesis\r?\n\r?\n', '')

Set-Content -Path $mergedPath -Value $merged -Encoding UTF8 -NoNewline
Remove-Item $ch03Path -Force
Remove-Item $ch04Path -Force
Write-Host "Merged -> $mergedPath; deleted Ch03/Ch04 originals"

# --- Split Ch07 ---
$ch07 = Get-Content $ch07Path -Raw
$splitMarker = '## What Should Be Added Next'
$idx = $ch07.IndexOf($splitMarker)
if ($idx -lt 0) { throw "Split marker not found in Ch07" }

$living07 = @'
## Corpus status (living layer)

**Last reconciled:** 2026-06-24
**Confidence:** Current synthesis Supported; backlog priorities evolve with main-repo releases
**Read with:** [Chapter 07b](07b-research-backlog-and-pipeline.md), [Chapter 01](01-seed-organism-and-sensor-array.md), [Chapter 06](06-mutation-safety-and-permission-law.md), `RESEARCH_PIPELINE.md`

### Authoritative for
- Which original five gaps are closed vs open in main `CursiveOS` repo (Gaps 1–5)
- Boundary: research here; runnable scripts graduate to main repo

### Superseded or narrowed
- "Repo is private" — public as of 2026-06-23 cleanup

### Open until experiment/hardware
- See Ch07b for pipeline experimental lift items

---

## Reinforced research (2026-06-24)

- **Gap closure status:** Ch01/02/05/06 document main-repo architecture; Ch08/09/10/11/12 close fleet-stats, network, LLM runtime, identity, and OSS-funding gaps.
- **RSI literature:** Ch03 merged digest + 25 paper intakes — pipeline P0 RSI targets substantially delivered.
- **Measurement priority:** Ch00 §3 schema gaps (`power_source`, `page_cache_state`) remain highest-leverage open items for fleet truth.

---

'@

$living07b = @'
## Corpus status (living layer)

**Last reconciled:** 2026-06-24
**Confidence:** Current synthesis Supported; priorities tracked in `RESEARCH_PIPELINE.md`
**Read with:** [Chapter 07](07-main-repo-gap-closure.md), [RESEARCH_PIPELINE.md](../RESEARCH_PIPELINE.md), [Chapter 00](00-benchmark-schema-and-measurement-validity.md)

### Authoritative for
- Next research targets after gap-closure pass (schema, shell spec, signed presets, fork obligation)
- Experimental lift queue: cold-start confound, proposer test, idle-power channel

### Superseded or narrowed
- Discovery-phase gaps — superseded by Ch07 gap-closure answers

### Open until experiment/hardware
- All items in RESEARCH_PIPELINE §3 Experimental Lift

---

## Reinforced research (2026-06-24)

- **Proposer falsifier:** `experiments/proposer-vs-random-tuning-experiment.md` (CH05-BM-002) — highest-leverage Ch15 validation.
- **Cold-start confound:** `experiments/cold-start-order-cache-confound-plan.md` — blocks acceptance-grade fleet claims.
- **Signed preset channel:** Transition 2 heart — deep spec still open; links Ch06 regression gates.

---

'@

$header07 = @'
# Main Repo Gap Closure

Status: Gap-closure synthesis (split from former Ch07, 2026-06-24). Research backlog → [Chapter 07b](07b-research-backlog-and-pipeline.md).

'@

$header07b = @'
# Research Backlog and Pipeline

Status: Backlog and pipeline priorities (split from former Ch07, 2026-06-24). Gap status → [Chapter 07](07-main-repo-gap-closure.md).

'@

# Extract body from original (after reinforced block)
$bodyStart = $ch07.IndexOf('# Main Repo Gap Closure')
$body = $ch07.Substring($bodyStart)
$body = $body -replace '^# Main Repo Gap Closure and Research Backlog\r?\n\r?\nStatus:[^\r\n]*\r?\n\r?\n', ''

$partA = $body.Substring(0, $body.IndexOf($splitMarker))
$partB = $body.Substring($body.IndexOf($splitMarker))

$ch07a = $living07 + $header07 + $partA.TrimEnd()
$ch07b = $living07b + $header07b + $partB.TrimStart()

Set-Content -Path $ch07aPath -Value $ch07a -Encoding UTF8 -NoNewline
Set-Content -Path $ch07bPath -Value $ch07b -Encoding UTF8 -NoNewline
Remove-Item $ch07Path -Force
Write-Host "Split -> $ch07aPath + $ch07bPath; deleted Ch07 original"

exit 0