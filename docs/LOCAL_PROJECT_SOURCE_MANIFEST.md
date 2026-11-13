# Local ISO/IEC 42001 Project — Source Manifest and Import Status

**Status: source import pending.** This manifest records the contents of the reviewed GitHub-ready archive. It does not mean those files have been published to this repository.

The fictional case study is MaltaAI Solutions Ltd., an AI recruitment SaaS provider. The reviewed archive `MaltaAI-Governance-GitHub-Ready.zip` contains a selected 50-file working set under `iso42001/`, including 25 CSV files. The archive was structurally checked before publication; the source records are still absent from the GitHub tree.

## Reviewed source inventory

| Record set | Archive count | GitHub publication status |
|---|---:|---|
| AI system/use-case inventory | 5 | Not imported |
| AI risk assessment register | 10 | Not imported |
| Impact assessment — folder 05 | 8 | Not imported |
| Impact assessment — folder 16 | 8 | Not imported; kept separate |
| AI risk treatment plan | 10 | Not imported |
| Data and supplier register | 5 | Not imported |
| ISO/IEC 42001 control mapping | 14 | Not imported |
| AI control evidence tracker | 15 | Not imported |
| Internal audit checklist | 15 | Not imported |
| Simulated audit findings | 6 | Not imported |
| Audit/CAPA cross-reference | 6 | Not imported |
| NCR/CAPA register | 6 | Not imported |
| Management review action register | 6 | Not imported |

The five described AI functions are CV extraction, candidate ranking, candidate summaries, recruitment chatbot and recruitment analytics. Additional archive files cover organisational context, AIMS scope, governance policies, synthetic fairness testing, supplier due diligence, stakeholder impacts and safeguards, audit walkthrough, management review and final reporting.

## Simulated finding summary

The source archive contains six simulated audit findings. The previously supplied topic and severity summary is:

| Finding ID | Topic | Severity |
|---|---|---|
| AIF-001 | Roles and responsibilities | High |
| AIF-002 | Residual-risk assessment | Critical |
| AIF-003 | Supplier oversight | High |
| AIF-004 | Human oversight | Critical |
| AIF-005 | Documentation | Medium |
| AIF-006 | Incident management | High |

These labels are scenario data, not independently validated audit conclusions. The underlying finding descriptions, criteria, objective evidence, root causes, corrective actions, owners and verification statuses must be reviewed in the source records before any claim of closure or effectiveness.

## Archive review and backup handling

The prepared archive contains 50 selected files and excludes 22 backup or duplicate-version entries found in the 71-entry original archive. Both impact-assessment registers are retained because they are separate source folders; they must not be merged or treated as duplicates solely because their filenames match.

The archive's bundled validator reported 20 configured count checks and zero issues. Independent parsing found all 25 CSV files readable as UTF-8 CSV. These are structural checks only, not an independent audit or proof of the accuracy of the records.

## Import and reconciliation requirements

When the archive is imported:

- Preserve original source values before making corrections.
- Compare the two impact-assessment folders record by record; retain both unless a documented source review establishes otherwise.
- Confirm exact AI system, risk, impact assessment, treatment, supplier, control, evidence, checklist and finding IDs.
- Reconcile risk scoring against the documented methodology and retain rationale for every score change.
- Check that treatments reference valid risk IDs; do not reduce residual risk merely because a treatment is planned.
- Distinguish planned, implemented, collected, reviewed and verified evidence statuses.
- Preserve finding wording and severity rationale from the source; do not invent objective evidence or claim closure.
- Run the repository validator and resolve all structural errors before publication.

## Publication rule

Until the source files are imported and reconciled, this GitHub repository remains a **template-based portfolio in progress**. This manifest is an inventory of the reviewed archive, not evidence that the source records are present in GitHub, that an AIMS has been implemented, or that an audit or certification has occurred.
