# Import the reviewed MaltaAI ISO 42001 source archive into this repository.
# Run from the local clone of ajaykumar76/simulated-iso-42001-aisms-portfolio.
[CmdletBinding()]
param(
    [Parameter(Mandatory = $false)]
    [string]$ArchivePath
)

$ErrorActionPreference = "Stop"

function Fail([string]$Message) {
    Write-Error $Message
    exit 1
}

$repoRoot = (Get-Location).Path
if (-not (Test-Path (Join-Path $repoRoot ".git"))) {
    Fail "Run this script from the root of your cloned GitHub repository."
}

if (-not $ArchivePath) {
    $candidates = @(
        (Join-Path $repoRoot "MaltaAI-Governance-GitHub-Ready.zip"),
        (Join-Path $HOME "Downloads/MaltaAI-Governance-GitHub-Ready.zip"),
        (Join-Path $HOME "Desktop/MaltaAI-Governance-GitHub-Ready.zip")
    )
    $ArchivePath = $candidates | Where-Object { Test-Path $_ } | Select-Object -First 1
}
if (-not $ArchivePath -or -not (Test-Path $ArchivePath -PathType Leaf)) {
    Fail "Cannot find MaltaAI-Governance-GitHub-Ready.zip. Pass its full path using -ArchivePath."
}

$branch = (git branch --show-current).Trim()
if ($branch -ne "main") {
    Fail "Current branch is '$branch'. Switch to main before importing."
}
$workingTree = git status --porcelain
if ($workingTree) {
    Fail "Working tree is not clean. Commit, stash or otherwise resolve existing changes before importing; this script will not touch them."
}
$remote = (git remote get-url origin 2>$null)
if (-not $remote -or $remote -notmatch "ajaykumar76/simulated-iso-42001-aisms-portfolio") {
    Fail "The origin remote does not point to ajaykumar76/simulated-iso-42001-aisms-portfolio."
}
if (Test-Path (Join-Path $repoRoot "iso42001")) {
    Fail "An iso42001 folder already exists. No files were overwritten. Review/merge it manually first."
}

$temp = Join-Path ([System.IO.Path]::GetTempPath()) ("maltaai-import-" + [guid]::NewGuid())
New-Item -ItemType Directory -Path $temp | Out-Null
try {
    Expand-Archive -LiteralPath (Resolve-Path $ArchivePath) -DestinationPath $temp
    $source = Join-Path $temp "iso42001"
    if (-not (Test-Path $source -PathType Container)) {
        Fail "Archive does not contain the expected iso42001 folder."
    }
    $files = @(Get-ChildItem -LiteralPath $source -File -Recurse)
    if ($files.Count -lt 40) {
        Fail "Only $($files.Count) files found. Expected at least 40; refusing import."
    }
    $required = @(
        "03-AI-System-Inventory/AI_System_Inventory.csv",
        "04-AI-Risk-Assessment/AI_Risk_Assessment_Register.csv",
        "05-AI-Impact-Assessment/AI_Impact_Assessment_Register.csv",
        "06-Risk-Treatment/AI_Risk_Treatment_Plan.csv",
        "08-Data-and-Supplier-Governance/AI_Data_and_Supplier_Register.csv",
        "09-Control-Mapping/ISO42001_Control_Mapping.csv",
        "10-Control-Evidence/AI_Control_Evidence_Tracker.csv",
        "11-Internal-Audit/AI_Audit_Findings_Register.csv",
        "12-NCR-CAPA/AI_NCR_CAPA_Register.csv",
        "16-AI-Impact-Assessment/AI_Impact_Assessment_Register.csv"
    )
    foreach ($relative in $required) {
        if (-not (Test-Path (Join-Path $source $relative) -PathType Leaf)) {
            Fail "Required source record is missing: $relative"
        }
    }

    Copy-Item -LiteralPath $source -Destination (Join-Path $repoRoot "iso42001") -Recurse
    git add -- iso42001
    git diff --cached --quiet
    if ($LASTEXITCODE -eq 0) {
        Fail "No new files were staged; check the archive and repository state."
    }

    Write-Host "Imported $($files.Count) source files into iso42001/." -ForegroundColor Green
    Write-Host "Review the staged file list before committing:"
    git status --short
    $approval = Read-Host "Type PUBLISH to commit and push these files to GitHub"
    if ($approval -cne "PUBLISH") {
        git reset -- iso42001
        Remove-Item -LiteralPath (Join-Path $repoRoot "iso42001") -Recurse -Force
        Fail "Import cancelled. The newly copied iso42001 folder was removed; existing repository files were not changed."
    }

    git commit -m "Import completed simulated ISO 42001 portfolio records"
    if ($LASTEXITCODE -ne 0) { Fail "Commit failed. Review git status; files remain in your local working tree." }
    git push origin main
    if ($LASTEXITCODE -ne 0) { Fail "Push failed. Your local commit remains; resolve the Git error and push again." }
    Write-Host "Published. Verify the iso42001 folder on GitHub." -ForegroundColor Green
}
finally {
    if (Test-Path $temp) { Remove-Item -LiteralPath $temp -Recurse -Force }
}
