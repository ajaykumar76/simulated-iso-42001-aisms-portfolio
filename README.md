# Simulated ISO/IEC 42001:2023 AI Management System (AIMS) Portfolio

**Project status: portfolio in progress — source project records have not yet been published.**

An educational, simulated AI Management System case study for **MaltaAI Solutions Ltd.**, a fictional provider of AI-enabled recruitment software. The portfolio is intended to demonstrate how an organisation could structure AI governance, risk management, impact assessment, supplier oversight, human oversight, monitoring and internal review using ISO/IEC 42001:2023 as a reference.

> **Important:** This is an independent learning project. It is not a real client engagement, accredited audit, certification assessment, legal opinion, or proof of conformity with ISO/IEC 42001. All organisations and scenario records are fictional. Templates in this repository are blank working templates, not completed evidence.

## Scenario

The fictional recruitment platform includes these AI-enabled functions:

- CV and application data extraction
- Candidate ranking and matching
- Candidate summaries
- Recruitment chatbot
- Recruitment analytics

Because the scenario concerns employment and recruitment, the project treats potential effects on applicants, fairness, transparency, privacy, human oversight and the consequences of AI-assisted decisions as key topics for assessment. A risk classification must be based on the system's actual intended purpose and applicable legal requirements; this portfolio does not make a binding EU AI Act classification.

## What is currently in this repository

| Path | Purpose | Status |
|---|---|---|
| `templates/AI_System_Inventory_Template.csv` | Record AI systems, intended purpose, lifecycle and human oversight | Blank template |
| `templates/AI_Risk_Register_Template.csv` | Record AI risks, scoring rationale, owners and treatment | Blank template |
| `templates/AI_Impact_Assessment_Template.csv` | Record affected stakeholders and potential impacts | Blank template |
| `templates/Risk_Treatment_Plan_Template.csv` | Track treatment actions, owners, due dates and status | Blank template |
| `templates/Supplier_Register_Template.csv` | Record AI-related suppliers and oversight | Blank template |
| `templates/Control_Evidence_Register_Template.csv` | Map controls to evidence and verification status | Blank template |
| `templates/Audit_Findings_CAPA_Template.csv` | Record simulated audit findings and corrective actions | Blank template |

The author has previously described a local working project containing an AI inventory, 10 risk records, 8 impact assessments, 10 treatment records, 5 supplier records, 14 control/evidence records, 15 audit checklist items and 6 simulated findings. **Those local records are not included in this GitHub repository yet**, so the counts above are not independently verifiable here and are not presented as published deliverables.

## Template completion guide

See [`docs/TEMPLATE_COMPLETION_GUIDE.md`](docs/TEMPLATE_COMPLETION_GUIDE.md) for field conventions, recommended completion order, traceability checks and publication safeguards.

## Suggested workflow

1. Define organisational context, intended purpose, AIMS scope, boundaries and interested parties.
2. Inventory each AI system and document its lifecycle, intended use, limitations and human oversight.
3. Identify affected stakeholders and assess potential impacts.
4. Identify AI risks, document scoring criteria and rationale, assign owners and determine treatment.
5. Record supplier dependencies and proportionate oversight activities.
6. Map applicable requirements and controls to evidence; distinguish planned, implemented, tested and approved states.
7. Plan monitoring, incident handling, internal review and corrective action.
8. Reconcile identifiers and statuses across all registers before publishing a final report.

Use the blank CSV files in `templates/` as starting points. Add completed, fictional example records only after reviewing the underlying source material and checking that IDs, scoring, owners, statuses and cross-references agree.

## Data integrity rules

- Use unique, stable IDs across the inventory, risk register, impact assessments, treatment plan, supplier register and evidence register.
- Keep inherent risk, residual risk and acceptance decisions distinct.
- Document the scoring scale and the reason for each likelihood and impact rating.
- Do not mark a treatment as implemented or a control as effective without supporting evidence.
- Distinguish proposed, in progress, implemented, verified and approved.
- Record human oversight as an actual process with defined authority, not merely a yes/no field.
- Do not treat a blank field as proof that a control or process does not exist.
- Do not include personal data, confidential information, credentials or unredacted operational evidence.

## Limitations

- MaltaAI Solutions Ltd. is fictional.
- All scenario data and any future example findings are simulated.
- The blank templates do not demonstrate that an AIMS has been implemented or is operating effectively.
- No formal audit, certification or conformity assessment has been performed.
- The repository does not provide legal advice or a definitive EU AI Act classification.
- Any risk acceptance or management approval must be supported by an explicitly documented decision in the simulated case study.

## References

- [ISO — ISO/IEC 42001:2023 Artificial intelligence management system](https://www.iso.org/standard/81230.html)
- [European Commission — Regulatory framework for AI](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)
- [GitHub Docs — About README files](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)

## Next publication steps

- [ ] Publish the reviewed local AI inventory and source registers.
- [ ] Reconcile risk IDs, system IDs, owners, scores and statuses across all records.
- [ ] Verify all calculations and document the scoring methodology.
- [ ] Add completed fictional impact assessments and supplier records.
- [ ] Link each claimed control to a specific evidence item and verification status.
- [ ] Publish the audit checklist, simulated findings and corrective-action records.
- [ ] Add a final report that clearly states scope, limitations, unresolved issues and approval status.
- [ ] Test all relative links from a clean clone.

**Portfolio owner:** [ajaykumar76](https://github.com/ajaykumar76)
