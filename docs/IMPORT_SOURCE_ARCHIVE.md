# Import the completed MaltaAI source records

The reviewed archive is a 50-file simulated ISO/IEC 42001 portfolio working set. It is not the blank-template pack.

## One-time import (Windows PowerShell)

1. Download the **MaltaAI-Governance-GitHub-Ready.zip** archive from your ChatGPT file/library attachment to your computer.
2. Clone the repository if you have not already:

   ```powershell
   git clone https://github.com/ajaykumar76/simulated-iso-42001-aisms-portfolio.git
   cd simulated-iso-42001-aisms-portfolio
   ```

3. Download or copy `scripts/import_source_archive.ps1` from this repository into the cloned repository's `scripts` folder.
4. Run from the repository root, passing the archive's full path:

   ```powershell
   .\scripts\import_source_archive.ps1 -ArchivePath "C:\Users\YOUR_USER\Downloads\MaltaAI-Governance-GitHub-Ready.zip"
   ```

5. Review the staged list. The script requires you to type `PUBLISH` before it commits and pushes.

The script refuses to overwrite an existing `iso42001/` folder, checks for the expected key registers, and verifies the Git remote and branch before copying. If push fails, the local commit remains and can be pushed after resolving the reported Git issue.

## What gets imported

The archive's `iso42001/` directory is imported intact, including both distinct impact assessment registers, evidence records, audit/CAPA records, supplier governance, management review, final report and the project's own validator. Backup copies excluded from the prepared working set are not reintroduced.

## Limitations

This script performs a file import, not an audit. The records describe a fictional organisation and simulated work. Review the staged files and reconcile the source IDs and cross-references before presenting the portfolio as complete.
