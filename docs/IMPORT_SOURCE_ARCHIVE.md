# Import the completed MaltaAI source records

The reviewed archive is a 50-file simulated ISO/IEC 42001 portfolio working set. It is not the blank-template pack.

## One-time import (Windows PowerShell)

1. Download **MaltaAI-Governance-GitHub-Ready.zip** from your ChatGPT Library to your computer.
2. Open PowerShell and enter your local clone. If you do not have a clone yet, run:

   ```powershell
   cd $HOME
   git clone https://github.com/ajaykumar76/simulated-iso-42001-aisms-portfolio.git
   cd simulated-iso-42001-aisms-portfolio
   ```

   If you already have the clone, change into that repository folder instead.
3. Pull the latest repository changes so the import script is present:

   ```powershell
   git switch main
   git pull origin main
   ```

4. Run the importer, adjusting the ZIP path if it is not in Downloads:

   ```powershell
   .\scripts\import_source_archive.ps1 -ArchivePath "$HOME\Downloads\MaltaAI-Governance-GitHub-Ready.zip"
   ```

5. The importer checks the repository, archive structure, required source records and CSV/repository validation before staging. Review the staged list. Type `PUBLISH` only if the list is correct; the script then commits and pushes to `main`.

## Safety checks

The importer refuses to overwrite an existing `iso42001/` folder, refuses a dirty working tree, checks the branch and origin remote, and validates the copied source tree before staging. If validation fails, it removes only the newly copied `iso42001/` folder and does not create a commit. If push fails after a successful commit, the local commit remains and can be pushed after resolving the Git error.

## What gets imported

The archive's `iso42001/` directory is imported intact, including both distinct impact assessment registers, evidence records, audit/CAPA records, supplier governance, management review, final report and the project's own validator. Backup copies excluded from the prepared working set are not reintroduced.

## Limitations

This is a file import and structural validation, not an audit. The records describe a fictional organisation and simulated work. Review and reconcile source IDs, scoring, statuses and cross-references before presenting the portfolio as complete. A successful GitHub Actions run does not establish ISO/IEC 42001 conformity, legal compliance or control effectiveness.
