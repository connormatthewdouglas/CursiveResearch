# Insert Corpus inline blocks after anchor lines per sources/reinforcement-manifest.json
param(
    [string]$RepoRoot = (Split-Path $PSScriptRoot -Parent),
    [string]$ManifestPath = (Join-Path (Split-Path $PSScriptRoot -Parent) 'sources\reinforcement-manifest.json')
)

$ErrorActionPreference = 'Stop'
$manifest = Get-Content $ManifestPath -Raw | ConvertFrom-Json
$marker = $manifest.inline_marker_prefix
$applied = 0
$skipped = 0

foreach ($entry in $manifest.chapters) {
    $path = Join-Path $RepoRoot "chapters\$($entry.file)"
    if (-not (Test-Path $path)) {
        Write-Error "Chapter file missing: $($entry.file)"
    }
    $content = Get-Content $path -Raw -Encoding UTF8
    $norm = $content -replace "`r`n", "`n"
    $anchorNorm = ($entry.anchor -replace "`r`n", "`n").Trim()

    if ($entry.skip_if_inline_present -and $content -like "*$marker*") {
        Write-Host "SKIP (inline exists): $($entry.file)"
        $skipped++
        continue
    }

    if (-not $entry.anchor -or -not $entry.inline) {
        Write-Error "Entry $($entry.id) missing anchor or inline"
    }

    if ($content -like "*$($entry.inline)*") {
        Write-Host "SKIP (exact inline): $($entry.file)"
        $skipped++
        continue
    }

    if ($norm -notlike "*$anchorNorm*") {
        Write-Error "Anchor not found in $($entry.file): $($entry.anchor)"
    }

    $replacement = "$anchorNorm`n`n$($entry.inline)`n"
    $newNorm = $norm.Replace($anchorNorm, $replacement)
    $newContent = $newNorm -replace "`n", "`r`n"
    if ($newContent -eq $content) {
        Write-Error "Replace produced no change for $($entry.file)"
    }

    [System.IO.File]::WriteAllText($path, $newContent, [System.Text.UTF8Encoding]::new($false))
    Write-Host "APPLIED: $($entry.file) anchor=$($entry.id)"
    $applied++
}

Write-Host "Manifest complete: applied=$applied skipped=$skipped"
exit 0