# ISO/IEC 42001:2023 Portfolio — Template Guide

This guide explains how to complete the blank CSV templates in this repository. The templates are intentionally blank: do not treat headers or example guidance as completed records, implemented controls, approvals, or audit evidence.

## Recommended completion sequence

1. **Define context and scope** — document the fictional organisation, interested parties, intended purpose, AIMS boundaries, interfaces, and exclusions.
2. **Inventory AI systems** — assign stable IDs (for example, AI-001) and record intended purpose, affected persons, lifecycle stage, data inputs, outputs, human oversight, limitations, and owner.
3. **Assess impacts** — complete an impact assessment for each relevant system/use context and affected stakeholder group. Record consultation, severity, likelihood, reversibility, safeguards, and escalation.
4. **Assess AI risks** — use a documented scoring method. Each risk statement should connect a cause or hazard to a plausible consequence for the organisation, individuals, or society.
5. **Plan treatment** — link each treatment action to one or more risk IDs, assign an accountable owner and due date, and leave implementation status pending until there is evidence.
6. **Record suppliers** — identify provider/deployer roles, services, dependencies, data access, contractual safeguards, change notification, monitoring, and exit considerations.
7. **Map controls to evidence** — record the control objective, implementation status, evidence reference, evidence owner, review date, and verification outcome. A document existing is not proof that a control operates effectively.
8. **Conduct a simulated internal review** — record criterion, objective evidence, finding, severity rationale, root cause, correction, corrective action, and effectiveness check. Keep simulated findings clearly labelled.
9. **Review and approve** — record who reviewed and approved each decision, the date, and the supporting reference. If no approval occurred, use a value such as `Pending` or `Not approved`.

## Template field conventions

- Use stable IDs consistently across files: `AI-001`, `AIR-001`, `AIA-001`, `TRT-001`, `SUP-001`, `EVD-001`, and `FND-001`.
- Use ISO dates: `YYYY-MM-DD`.
- Use controlled status values consistently (for example: `Draft`, `Pending Review`, `Approved`, `In Progress`, `Implemented - Evidence Pending`, `Verified`, `Closed`).
- Use `Not Assessed`, `Not Applicable` (with a rationale), or `Pending` rather than guessing missing values.
- Keep inherent risk, treatment progress, residual risk, acceptance, and approval as separate fields. Do not lower residual risk merely because a treatment is planned.
- Store evidence references, not confidential personal data. Use fictional or sanitised evidence in this public portfolio.

## Minimum traceability checks before publication

- Every risk references a valid AI system ID.
- Every treatment references an existing risk ID.
- Every impact assessment references an existing AI system ID and identifies affected stakeholders.
- Every supplier record identifies the AI system or service relationship it supports.
- Every control/evidence record has a unique ID and identifies the related system, risk, or treatment where relevant.
- Every finding references a criterion and, where applicable, a control, risk, or AI system.
- Closed findings have a documented effectiveness check and closure approval; otherwise they remain open.
- No record is labelled approved, implemented, verified, or closed without supporting evidence.

## Scope and disclaimer

This is a learning aid for a fictional case study. It is not a complete implementation guide, legal assessment, accredited audit, certification assessment, or proof of conformity with ISO/IEC 42001:2023 or the EU AI Act. Consult the official standard and applicable legal sources for authoritative requirements.
