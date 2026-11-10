# Portfolio Release-Readiness Checklist

**Status: draft — source records have not yet been reconciled against this checklist.**

This checklist is a quality gate for the fictional MaltaAI Solutions Ltd. learning exercise. It is not evidence of an implemented or certified AI management system.

## 1. Source record inventory

- [ ] Confirm the final set of source files and their version/date.
- [ ] Exclude backup copies, temporary exports, local caches, secrets and personal data from publication.
- [ ] Retain one clearly named current version of each record.
- [ ] Document any intentionally retained historical version and why it is needed.
- [ ] Do not infer that a file is complete merely because it exists.

## 2. Resolve duplicate or overlapping subject areas

The local project directory listing supplied for review showed both `05-AI-Impact-Assessment` and `16-AI-Impact-Assessment`.

- [ ] Compare the files and record IDs in both folders before changing either.
- [ ] Determine whether one folder contains distinct assessment types, newer revisions or duplicate copies.
- [ ] Preserve unique material and document any merge or retirement decision.
- [ ] Update all README links and cross-references after the decision.

Do not delete, rename or merge either folder based on its name alone.

## 3. Identifier and traceability checks

Check that identifiers are unique and consistently referenced across:

- AI system inventory
- AI risk register
- AI impact assessments
- Risk treatment plan
- AI governance policies and procedures
- Supplier / third-party AI register
- Control mapping and evidence register
- Internal audit checklist
- Findings and corrective-action records
- Management review and final report

For each relationship, verify that the referenced ID exists. Record unresolved references as open issues rather than silently changing IDs.

## 4. Risk and impact quality

- [ ] Publish the risk scoring scale and calculation method.
- [ ] Check every score against its likelihood and impact values.
- [ ] Keep inherent risk, treatment status and residual risk separate.
- [ ] Record the rationale and source for each rating.
- [ ] Identify affected stakeholders and plausible positive and negative impacts.
- [ ] Document intended purpose, foreseeable misuse, limitations and human oversight.
- [ ] Do not claim that human oversight is effective based only on a yes/no field.
- [ ] Do not mark risk treatment complete without evidence and review.

## 5. Supplier, control and evidence checks

- [ ] Link suppliers to the AI systems and services they support.
- [ ] Record supplier assessment status and unresolved dependencies.
- [ ] Distinguish control design from implementation and operating effectiveness.
- [ ] Give each evidence item a unique ID, owner/source, date, related control and review status.
- [ ] Do not use planned documents as evidence of implementation.
- [ ] Redact personal, confidential and security-sensitive information.

## 6. Audit, corrective action and management review

- [ ] Make the audit checklist traceable to defined criteria and records.
- [ ] Label all findings as simulated.
- [ ] Link each finding to its evidence, requirement/criterion, root-cause analysis and corrective action where applicable.
- [ ] Keep open, closed and effectiveness-verified states distinct.
- [ ] Do not mark corrective action effective without a documented verification step.
- [ ] Ensure management-review outputs are presented as simulated decisions, not actual management approval.

## 7. Reproducibility and publication

- [ ] Run the project's validation script from a clean copy of the project.
- [ ] Review validation output; do not rely solely on an old saved results file.
- [ ] Correct errors and investigate warnings.
- [ ] Confirm relative links work from a fresh Git clone.
- [ ] Ensure README counts match the actual published records.
- [ ] Include a concise final report listing scope, methods, results, limitations and unresolved issues.
- [ ] Confirm that all content is fictional and safe to publish.

## Publication rule

Until the checks above are completed, describe this repository as a **simulated portfolio in progress**. Do not claim ISO/IEC 42001 conformity, certification, a completed professional audit, an operational AIMS or verified legal classification under the EU AI Act.
