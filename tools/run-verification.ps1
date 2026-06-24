# Contract-driven corpus verification. Exits non-zero if contract fails; only then writes scratch evidence.
param(
    [string]$RepoRoot = (Split-Path $PSScriptRoot -Parent),
    [string]$ScratchDir = $env:CORPUS_VERIFY_SCRATCH
)

$ErrorActionPreference = 'Stop'
if (-not $ScratchDir) {
    $ScratchDir = Join-Path $env:TEMP 'grok-goal-corpus-verify'
}
New-Item -ItemType Directory -Force -Path $ScratchDir | Out-Null

$contractPath = Join-Path $PSScriptRoot 'verification-contract.json'
if (-not (Test-Path $contractPath)) {
    Write-Error "Missing contract: $contractPath"
    exit 2
}
$contract = Get-Content $contractPath -Raw | ConvertFrom-Json

function Fail([string]$msg) {
    Write-Host "CONTRACT FAIL: $msg" -ForegroundColor Red
    @(
        "VERIFICATION CONTRACT FAILED",
        "Time: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')",
        "Contract: $contractPath",
        "Reason: $msg"
    ) | Set-Content (Join-Path $ScratchDir 'verification-contract-fail.txt') -Encoding UTF8
    exit 1
}

# --- Markdown hygiene lint (regression guards) ---
# Fails verification if any tracked .md file contains: (a) double-encoded UTF-8
# mojibake, (b) a citation-export span artifact, or (c) a collapsed GFM table.
# Prints the offending file:line for every hit before failing.
if (-not $contract.markdown_hygiene_lint -or $contract.markdown_hygiene_lint.enabled) {
    Push-Location $RepoRoot
    $trackedMd = @(git ls-files '*.md')
    Pop-Location
    $reMoji1 = [regex]'â€'          # 'â€' double-encoded UTF-8 signature
    $reMoji2 = [regex]'[ÃÂ]\S'      # stray Ã/Â immediately followed by a non-space char
    $reSpan  = [regex]'\[span_\d+\]\((?:start|end)_span\)'
    $lintHits = New-Object System.Collections.Generic.List[string]
    foreach ($rel in $trackedMd) {
        $full = Join-Path $RepoRoot $rel
        if (-not (Test-Path $full)) { continue }
        $lineNo = 0
        foreach ($line in (Get-Content $full -Encoding UTF8)) {
            $lineNo++
            if ($reMoji1.IsMatch($line) -or $reMoji2.IsMatch($line)) {
                $lintHits.Add("mojibake        ${rel}:${lineNo}: $($line.Trim())")
            }
            if ($reSpan.IsMatch($line)) {
                $lintHits.Add("span-artifact   ${rel}:${lineNo}: $($line.Trim())")
            }
            # Collapsed table: a separator-marker line that also carries data cells.
            if ($line -match ':---' -and $line -match '[0-9A-Za-z]') {
                $lintHits.Add("collapsed-table ${rel}:${lineNo}: $($line.Trim())")
            }
        }
    }
    if ($lintHits.Count -gt 0) {
        Write-Host "MARKDOWN HYGIENE LINT FAILURES ($($lintHits.Count)):" -ForegroundColor Red
        $lintHits | ForEach-Object { Write-Host "  $_" }
        Fail "Markdown hygiene lint found $($lintHits.Count) issue(s): mojibake / span-artifact / collapsed-table"
    }
    Write-Host "MARKDOWN HYGIENE LINT: clean ($($trackedMd.Count) tracked .md files)"
}

# --- Live counts ---
$chapters = Get-ChildItem (Join-Path $RepoRoot 'chapters\*.md') | Sort-Object Name
$paperDirs = Get-ChildItem (Join-Path $RepoRoot 'papers') -Recurse -Directory |
    Where-Object { $_.Parent.Name -in @('agent-evaluation','recursive-self-improvement','software-engineering-agents') } |
    Sort-Object Name

if ($chapters.Count -ne $contract.chapters_total) {
    Fail "Chapter count $($chapters.Count) != $($contract.chapters_total)"
}
if ($paperDirs.Count -ne $contract.papers_total) {
    Fail "Paper count $($paperDirs.Count) != $($contract.papers_total)"
}

# --- Sample coverage ---
$req = $contract.sample_requirements
foreach ($f in $contract.sample_chapters) {
    if (-not (Test-Path (Join-Path $RepoRoot "chapters\$f"))) {
        Fail "Sample chapter missing: $f"
    }
}
if ($contract.sample_chapters -notcontains $req.early_docx_import) {
    Fail "Early DOCX sample missing: $($req.early_docx_import)"
}
$has1415 = $false
foreach ($f in $req.one_of_14_15) {
    if ($contract.sample_chapters -contains $f) { $has1415 = $true }
}
if (-not $has1415) {
    Fail "Neither Ch14 nor Ch15 in sample_chapters"
}
$newCount = 0
foreach ($f in $req.new_chapters_from_08_12) {
    if ($contract.sample_chapters -contains $f) { $newCount++ }
}
if ($newCount -lt $req.min_new_chapter_samples) {
    Fail "New chapter samples $newCount < $($req.min_new_chapter_samples)"
}

# --- Marker counts ---
$chapterGlob = Join-Path $RepoRoot 'chapters\*.md'
$living = (Select-String -Path $chapterGlob -SimpleMatch $contract.markers.living_layer -AllMatches).Count
$reinforced = (Select-String -Path $chapterGlob -SimpleMatch $contract.markers.reinforced_research -AllMatches).Count
$integration = (Select-String -Path $chapterGlob -SimpleMatch $contract.markers.corpus_integration -AllMatches).Count

$exp = $contract.marker_expectations
if ($living -ne $exp.all_chapters_living_layer) {
    Fail "living_layer=$living expected $($exp.all_chapters_living_layer)"
}
if ($reinforced -ne $exp.all_chapters_reinforced) {
    Fail "reinforced=$reinforced expected $($exp.all_chapters_reinforced)"
}
if ($integration -ne $exp.docx_chapters_integration) {
    Fail "corpus_integration=$integration expected $($exp.docx_chapters_integration) (all docx import chapters)"
}

# Per-docx chapter integration check
foreach ($num in $contract.docx_import_chapters) {
    $file = Get-ChildItem (Join-Path $RepoRoot "chapters\$num-*.md") -ErrorAction SilentlyContinue | Select-Object -First 1
    if (-not $file) { Fail "DOCX chapter file not found for prefix $num" }
    $content = Get-Content $file.FullName -Raw
    if ($content -notlike "*$($contract.markers.corpus_integration)*") {
        Fail "$($file.Name) missing corpus integration notes"
    }
}

# Inline markers inside preserved import bodies (required chapters)
$inlineCount = 0
foreach ($num in $contract.inline_required_chapters) {
    $file = Get-ChildItem (Join-Path $RepoRoot "chapters\$num-*.md") -ErrorAction SilentlyContinue | Select-Object -First 1
    if (-not $file) { Fail "Inline-required chapter not found: $num" }
    $content = Get-Content $file.FullName -Raw
    if ($content -notlike "*$($contract.markers.corpus_inline)*") {
        Fail "$($file.Name) missing inline corpus notes in import body"
    }
    $inlineCount += ([regex]::Matches($content, [regex]::Escape($contract.markers.corpus_inline))).Count
}
if ($inlineCount -lt $contract.marker_expectations.docx_chapters_inline_minimum) {
    Fail "Inline marker count $inlineCount < $($contract.marker_expectations.docx_chapters_inline_minimum)"
}

# --- Acceptance gates (plan criteria 1-2) ---
if ($contract.acceptance_gates) {
    $gates = $contract.acceptance_gates
    $mergedPath = Join-Path $RepoRoot "chapters\$($gates.merged_rsi_file)"
    if (-not (Test-Path $mergedPath)) {
        Fail "Merged RSI file missing: $($gates.merged_rsi_file)"
    }
    $deletedRsi = Join-Path $RepoRoot "chapters\$($gates.deleted_rsi_file)"
    if (Test-Path $deletedRsi) {
        Fail "Deleted RSI file still present: $($gates.deleted_rsi_file)"
    }
    $splitGap = Join-Path $RepoRoot "chapters\$($gates.split_gap_file)"
    $splitBacklog = Join-Path $RepoRoot "chapters\$($gates.split_backlog_file)"
    if (-not (Test-Path $splitGap)) { Fail "Split gap file missing: $($gates.split_gap_file)" }
    if (-not (Test-Path $splitBacklog)) { Fail "Split backlog file missing: $($gates.split_backlog_file)" }
    $deletedGap = Join-Path $RepoRoot "chapters\$($gates.deleted_combined_gap_file)"
    if (Test-Path $deletedGap) {
        Fail "Combined gap file still present: $($gates.deleted_combined_gap_file)"
    }

    foreach ($origFile in $gates.original_chapter_files) {
        $origPath = Join-Path $RepoRoot "chapters\$origFile"
        if (-not (Test-Path $origPath)) {
            Fail "Original chapter file missing: $origFile"
        }
        $origContent = Get-Content $origPath -Raw
        $reinforcedIdx = $origContent.IndexOf($contract.markers.reinforced_research)
        if ($reinforcedIdx -lt 0) {
            Fail "$origFile missing reinforced research block"
        }
        $bodyAfterReinforced = $origContent.Substring($reinforcedIdx)
        $inlineInBody = ([regex]::Matches($bodyAfterReinforced, [regex]::Escape($contract.markers.corpus_inline))).Count
        if ($inlineInBody -lt $gates.min_corpus_inline_per_original) {
            Fail "$origFile has $inlineInBody corpus inline below reinforced block; need >= $($gates.min_corpus_inline_per_original)"
        }
    }
}

# --- Contract passed: emit evidence ---
$scriptPath = $PSCommandPath
$contractHash = (Get-FileHash $contractPath -Algorithm SHA256).Hash
$scriptHash = (Get-FileHash $scriptPath -Algorithm SHA256).Hash
Push-Location $RepoRoot
$gitHead = (git rev-parse HEAD 2>$null)
Pop-Location
Write-Host "CONTRACT PASS: chapters=$($chapters.Count) papers=$($paperDirs.Count) living=$living reinforced=$reinforced integration=$integration"

# Step 1: corpus structure
$sb = New-Object System.Text.StringBuilder
[void]$sb.AppendLine('CORPUS STRUCTURE EVIDENCE')
[void]$sb.AppendLine("Generated: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')")
[void]$sb.AppendLine("Contract: $contractPath")
[void]$sb.AppendLine("Chapter count: $($chapters.Count)")
[void]$sb.AppendLine("Paper folder count: $($paperDirs.Count)")
[void]$sb.AppendLine('')
[void]$sb.AppendLine('CHAPTERS:')
foreach ($c in $chapters) { [void]$sb.AppendLine("  $($c.Name)") }
[void]$sb.AppendLine('')
[void]$sb.AppendLine('PAPERS:')
foreach ($p in $paperDirs) { [void]$sb.AppendLine("  $($p.Name)") }
$sb.ToString() | Set-Content (Join-Path $ScratchDir 'corpus-structure.txt') -Encoding UTF8

# Step 2: index
Copy-Item (Join-Path $RepoRoot 'INDEX.md') (Join-Path $ScratchDir 'index-check.txt') -Force

# Step 3: chapter samples (from contract)
$sb2 = New-Object System.Text.StringBuilder
[void]$sb2.AppendLine('CHAPTER SAMPLES EVIDENCE')
[void]$sb2.AppendLine("Generated: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')")
[void]$sb2.AppendLine("Producer: $scriptPath")
[void]$sb2.AppendLine("Contract: $contractPath")
[void]$sb2.AppendLine("Contract sample_chapters ($($contract.sample_chapters.Count)): $($contract.sample_chapters -join ', ')")
[void]$sb2.AppendLine("New chapter samples (min $($req.min_new_chapter_samples)): $($req.new_chapters_from_08_12 -join ', ')")
[void]$sb2.AppendLine('')
foreach ($f in $contract.sample_chapters) {
    $path = Join-Path $RepoRoot "chapters\$f"
    [void]$sb2.AppendLine(('=' * 72))
    [void]$sb2.AppendLine("FILE: $f")
    [void]$sb2.AppendLine(('=' * 72))
    [void]$sb2.AppendLine('--- head -100 ---')
    Get-Content $path -TotalCount 100 | ForEach-Object { [void]$sb2.AppendLine($_) }
    [void]$sb2.AppendLine('')
    [void]$sb2.AppendLine('--- Select-String markers ---')
    Select-String -Path $path -Pattern 'living layer|Reinforced research|2026|papers/|Corpus integration|Corpus inline' |
        ForEach-Object { [void]$sb2.AppendLine("$($_.LineNumber): $($_.Line.Trim())") }
    [void]$sb2.AppendLine('')
}
$sb2.ToString() | Set-Content (Join-Path $ScratchDir 'chapter-samples.txt') -Encoding UTF8

# Step 4: papers
$sb3 = New-Object System.Text.StringBuilder
[void]$sb3.AppendLine('PAPER INTAKE EVIDENCE')
[void]$sb3.AppendLine("Generated: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')")
[void]$sb3.AppendLine("Total: $($paperDirs.Count)")
[void]$sb3.AppendLine('')
foreach ($p in $paperDirs) {
    $files = (Get-ChildItem $p.FullName -File | Sort-Object Name | ForEach-Object { $_.Name }) -join ', '
    [void]$sb3.AppendLine("$($p.Name): $files")
}
[void]$sb3.AppendLine('')
[void]$sb3.AppendLine('EXAMPLE TREES:')
foreach ($slug in $contract.paper_example_slugs) {
    $dir = $paperDirs | Where-Object { $_.Name -eq $slug } | Select-Object -First 1
    if ($dir) {
        [void]$sb3.AppendLine("")
        [void]$sb3.AppendLine("papers/.../$slug/")
        Get-ChildItem $dir.FullName -File | Sort-Object Name | ForEach-Object {
            [void]$sb3.AppendLine("  $($_.Name)")
        }
    }
}
$sb3.ToString() | Set-Content (Join-Path $ScratchDir 'paper-intake-evidence.txt') -Encoding UTF8

# Step 5: changelog
Get-Content (Join-Path $RepoRoot 'CHANGELOG.md') -TotalCount 55 |
    Set-Content (Join-Path $ScratchDir 'changelog-evidence.txt') -Encoding UTF8

# Step 6: supporting
$sb4 = New-Object System.Text.StringBuilder
[void]$sb4.AppendLine('SUPPORTING UPDATES EVIDENCE')
[void]$sb4.AppendLine("Generated: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')")
[void]$sb4.AppendLine('')
[void]$sb4.AppendLine('--- CORPUS_WORKFLOW ---')
Select-String -Path (Join-Path $RepoRoot 'CORPUS_WORKFLOW.md') -Pattern 'Preserved Import|Cohesion Pass' |
    ForEach-Object { [void]$sb4.AppendLine($_.Line.Trim()) }
[void]$sb4.AppendLine('')
[void]$sb4.AppendLine('--- VALIDATION.md (first 70 lines) ---')
Get-Content (Join-Path $RepoRoot 'VALIDATION.md') -TotalCount 70 | ForEach-Object { [void]$sb4.AppendLine($_) }
[void]$sb4.AppendLine('')
[void]$sb4.AppendLine('--- RESEARCH_PIPELINE.md ---')
Select-String -Path (Join-Path $RepoRoot 'RESEARCH_PIPELINE.md') -Pattern 'Status \(2026-06-24\)|Chapter 17 now' |
    ForEach-Object { [void]$sb4.AppendLine($_.Line.Trim()) }
$sb4.ToString() | Set-Content (Join-Path $ScratchDir 'supporting-updates.txt') -Encoding UTF8

# Changed files + input records
Push-Location $RepoRoot
$prevEap = $ErrorActionPreference
$ErrorActionPreference = 'Continue'
$sb5 = New-Object System.Text.StringBuilder
[void]$sb5.AppendLine('CHANGED_FILES EVIDENCE')
[void]$sb5.AppendLine("Generated: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')")
[void]$sb5.AppendLine('')
[void]$sb5.AppendLine('INPUT RECORDS (verification harness):')
[void]$sb5.AppendLine("  ScriptPath: $scriptPath")
[void]$sb5.AppendLine("  ScriptSHA256: $scriptHash")
[void]$sb5.AppendLine("  ContractPath: $contractPath")
[void]$sb5.AppendLine("  ContractSHA256: $contractHash")
[void]$sb5.AppendLine("  GitHEAD: $gitHead")
[void]$sb5.AppendLine("  ScratchDir: $ScratchDir")
[void]$sb5.AppendLine("  RepoRoot: $RepoRoot")
[void]$sb5.AppendLine("  SampleChapters: $($contract.sample_chapters -join ', ')")
[void]$sb5.AppendLine("  InlineRequired: $($contract.inline_required_chapters -join ', ')")
[void]$sb5.AppendLine("  InlineCount: $inlineCount")
[void]$sb5.AppendLine('')
[void]$sb5.AppendLine('Recent commits:')
git log -5 --oneline | ForEach-Object { [void]$sb5.AppendLine("  $_") }
[void]$sb5.AppendLine('')
$baseline = $contract.acceptance_gates.goal_baseline_commit
if ($baseline) {
    [void]$sb5.AppendLine("MODIFIED FILES (git diff --name-status $baseline..HEAD):")
    $diffRange = "${baseline}..HEAD"
    $diffNames = git diff --name-status $diffRange 2>$null
    if ($diffNames) {
        $diffNames | ForEach-Object { [void]$sb5.AppendLine("  $_") }
    } else {
        [void]$sb5.AppendLine('  (no committed changes since baseline)')
    }
    [void]$sb5.AppendLine('')
}
[void]$sb5.AppendLine('Uncommitted (git diff --name-only):')
$uncommitted = git diff --name-only 2>$null
$untracked = git ls-files --others --exclude-standard 2>$null
if ($uncommitted) {
    $uncommitted | ForEach-Object { [void]$sb5.AppendLine("  M $_") }
}
if ($untracked) {
    $untracked | ForEach-Object { [void]$sb5.AppendLine("  ?? $_") }
}
if (-not $uncommitted -and -not $untracked) {
    [void]$sb5.AppendLine('  (clean)')
}
$ErrorActionPreference = $prevEap
Pop-Location
$sb5.ToString() | Set-Content (Join-Path $ScratchDir 'changed-files-evidence.txt') -Encoding UTF8

"MARKER COUNTS: living_layer=$living reinforced=$reinforced corpus_integration=$integration corpus_inline=$inlineCount chapters=$($chapters.Count) papers=$($paperDirs.Count)" |
    Set-Content (Join-Path $ScratchDir 'marker-counts.txt') -Encoding UTF8

@{
    generated = (Get-Date -Format 'yyyy-MM-dd HH:mm:ss')
    scriptPath = $scriptPath
    scriptSHA256 = $scriptHash
    contractPath = $contractPath
    contractSHA256 = $contractHash
    gitHEAD = $gitHead
    repoRoot = $RepoRoot
    scratchDir = $ScratchDir
    sampleChapters = $contract.sample_chapters
    newChapterSamples = $req.new_chapters_from_08_12
    inlineRequired = $contract.inline_required_chapters
    counts = @{
        chapters = $chapters.Count
        papers = $paperDirs.Count
        living = $living
        reinforced = $reinforced
        integration = $integration
        inline = $inlineCount
    }
    pass = $true
} | ConvertTo-Json -Depth 5 | Set-Content (Join-Path $ScratchDir 'input-records.json') -Encoding UTF8

@(
    'VERIFICATION CONTRACT PASSED',
    "Time: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')",
    "Producer: $scriptPath",
    "Chapters: $($chapters.Count)",
    "Papers: $($paperDirs.Count)",
    "Living: $living",
    "Reinforced: $reinforced",
    "Integration: $integration",
    "Inline: $inlineCount",
    "Samples: $($contract.sample_chapters -join ', ')"
) | Set-Content (Join-Path $ScratchDir 'verification-contract-pass.txt') -Encoding UTF8

Write-Host "Evidence written to $ScratchDir"
exit 0