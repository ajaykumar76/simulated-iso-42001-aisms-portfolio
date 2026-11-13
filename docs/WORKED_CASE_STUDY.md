# ISO/IEC 42001:2023 — Worked Case Study

**Project:** MaltaAI Solutions Ltd. (fictional)  
**System context:** AI-assisted recruitment SaaS  
**Artifact status:** Simulated learning material  
**Prepared:** 13 November 2026

> **Simulation notice:** All organisations, systems, roles, risks, scores, dates, examples and evidence references in this document are fictional or illustrative. This is not a real client engagement, operational AIMS, independent audit, certification assessment, legal opinion or proof of conformity. No control should be represented as implemented in a real environment based on this case study.

## 1. Purpose

This case study demonstrates an evidence-led way to reason about AI governance using ISO/IEC 42001:2023 as a management-system reference. It focuses on scope, intended use, affected parties, risk and impact assessment, treatment ownership, supplier governance, human oversight, audit evidence and corrective action.

It is a narrative learning aid. It does not replace the underlying registers, and its illustrative IDs must not be silently merged into the project's source CSVs.

## 2. Scenario and proposed AIMS scope

**Organisation:** MaltaAI Solutions Ltd. (fictional Malta-based recruitment software provider).

**Business context:** The company supplies recruitment software to small and medium-sized employers. The service uses AI-assisted functions to extract information from CVs, compare candidate profiles against job criteria, generate summaries and recommend ranked shortlists for human review. Related functions may include a recruitment chatbot and analytics.

**Proposed scope:** Governance of the design, procurement, configuration, deployment, monitoring and retirement of the AI-assisted recruitment service, including relevant personnel, third-party providers, data flows, supporting IT services and decisions made by customer users.

**Boundaries:** This exercise does not claim that the model is technically validated, that legal compliance has been established, or that certification has occurred. A real organisation would need to approve its scope, interfaces, roles and applicable obligations.

## 3. Intended use and affected parties

**Intended use:** Assist recruiters by organising application information and suggesting candidate-job matches. The system is not intended to make final hiring decisions without meaningful human review.

**Potentially affected parties:**
- Job applicants and candidates
- Recruiters and HR decision-makers
- Employer customers
- The AI system provider and relevant suppliers
- Data processors and other service providers
- Regulators and other interested parties

Applicants could be disadvantaged if ranking logic, training data, proxy variables or operational practices create unjustified disparities. Recruiters could also over-rely on generated summaries or rankings.

**Assumptions requiring validation in a real engagement:** the precise model and vendor; data sources and lawful basis; deployment locations; customer configuration options; whether special-category data are processed; human-review practices; supplier/subprocessor arrangements; and the legal classification and obligations applicable to each specific use.

## 4. Review method and evidence discipline

Audit criteria should be drawn from the applicable ISO/IEC 42001 requirements, approved AIMS documents, contracts, policies and relevant obligations. Before any real audit, agree objectives, scope, criteria, sampling, reporting and independence arrangements.

Potential evidence sources include:
- Approved policies, role assignments and management decisions
- AI system inventory and lifecycle records
- Risk and impact assessments
- Supplier due diligence and contract terms
- Data-flow and model/system documentation
- Validation and monitoring results
- Human-review instructions and decision records
- Incident tickets, escalation records and lessons learned
- Training records, change approvals and management-review minutes

Use explicit evidence statuses such as **Not requested**, **Requested**, **Received**, **Verified**, **Not verified**, and **Not applicable (with rationale)**. A document existing is not proof that a control operates. Interview statements may require corroboration. Samples should record the population, selection method, date and limitations.

## 5. Illustrative risk scenarios

For this exercise only, use likelihood (L) and impact (I) scores from 1 to 5, multiplied to produce an illustrative score. Example bands: 1–4 Low, 5–9 Moderate, 10–15 High, 16–25 Critical. These are invented project criteria, not prescribed ISO/IEC 42001 scoring bands. A real organisation must approve and calibrate its own method.

| Illustrative ID | Scenario | Example rating | Example treatment direction |
|---|---|---:|---|
| R-EX-01 | Candidate ranking disadvantages an underrepresented group due to data or proxy features | L4 × I5 = 20 Critical | Restrict or pause use pending representative evaluation; document limitations; define monitoring and escalation |
| R-EX-02 | Recruiters over-rely on AI recommendations and fail to independently review candidates | L4 × I4 = 16 Critical | Require meaningful human review, reviewer training, override capability and recorded rationale |
| R-EX-03 | A supplier changes model behaviour or subprocessors without timely notice | L3 × I4 = 12 High | Contractual change/incident notification, periodic supplier review, change assessment and exit planning |
| R-EX-04 | Applicant personal data are retained too long or exposed to unauthorised users | L3 × I5 = 15 High | Data minimisation, access control, retention schedule, deletion checks and privacy/security review |
| R-EX-05 | Inaccurate AI output is presented to recruiters as authoritative | L3 × I4 = 12 High | Define intended-use limits, communicate uncertainty, validate outputs, monitor errors and enable escalation |

A score is not self-explanatory. Each record should explain the scenario, causes, consequences, existing controls, scoring rationale, risk owner and decision criteria. Do not copy these example scores into a master register without reconciling them with the project's approved method and existing risk IDs.

## 6. Example treatment actions

| Example action | Linked example risk | Fictional accountable role | Closure evidence to seek |
|---|---|---|---|
| AT-EX-01 | R-EX-01 | AI Governance Lead | Approved evaluation protocol, results, limitations and authorised deployment decision |
| AT-EX-02 | R-EX-02 | Recruitment Operations Lead | Human-review procedure, training records and sampled decision logs |
| AT-EX-03 | R-EX-03 | Vendor Manager | Due diligence, contract review, escalation contacts and supplier-change process |
| AT-EX-04 | R-EX-04 | Privacy/Security Lead | Data-flow and retention records, access review and deletion-test evidence |
| AT-EX-05 | R-EX-05 | AI Product Owner | Validation report, user guidance, monitoring thresholds and incident-escalation test |

Treatment records should include an accountable owner, target date, resources, implementation status, evidence reference and residual-risk decision. A proposed action is not an implemented control. A residual risk should not be marked accepted without an authorised, documented decision.

## 7. Proposed audit work program — not performed

The following are proposed test procedures, not completed tests:

| Test | Objective | Example procedure | Status |
|---|---|---|---|
| T-EX-01 | Roles and accountability | Inspect role assignments; interview owners; trace one risk to an owner and escalation path | Not Yet Tested — Simulated |
| T-EX-02 | AI inventory and intended purpose | Select one inventory item; compare purpose, provider, users, data and lifecycle status with system documentation | Not Yet Tested — Simulated |
| T-EX-03 | Risk and impact assessment | Trace one high/critical risk and one impact from identification through evaluation, treatment and approval | Not Yet Tested — Simulated |
| T-EX-04 | Human oversight | Inspect reviewer instructions; sample decision records; check review, override and escalation evidence | Not Yet Tested — Simulated |
| T-EX-05 | Supplier governance | Inspect due diligence and contract terms for data access, subprocessors, changes, incidents and exit arrangements | Not Yet Tested — Simulated |
| T-EX-06 | Monitoring and incidents | Inspect monitoring plan, thresholds and incident workflow; trace an available sample record | Not Yet Tested — Simulated |
| T-EX-07 | Documented information | Check version, approval, owner, review date and consistency between policy, register and tracker | Not Yet Tested — Simulated |
| T-EX-08 | Corrective action | Trace a finding through criterion, evidence, root cause, action, owner, due date and effectiveness check | Not Yet Tested — Simulated |

A completed workpaper would also record the criterion, population, sample, steps actually performed, evidence reference, factual result, conclusion, reviewer and date. Until genuine evidence is examined, status must remain not tested.

## 8. Example simulated finding

This is a hypothetical training example. It must not be confused with the project's actual finding IDs or represented as a real audit result.

| Field | Illustrative entry |
|---|---|
| Example ID | SIM-AIF-EX-01 |
| Fictional criterion | An approved oversight procedure requires documented human review before a consequential recruitment recommendation is acted upon |
| Hypothetical evidence | A hypothetical sample of 10 decisions contains no review record for 3 decisions |
| Careful statement | In the hypothetical sample, 3 of 10 decisions lacked the review record required by the fictional procedure. This alone does not prove that no review occurred; workflow logs and interviews would need corroboration |
| Potential impact | Recommendations may be acted upon without meaningful human scrutiny, increasing the risk of unfair or unsuitable candidate outcomes |
| Immediate correction | Where operationally appropriate, hold affected decisions for review and document the outcome |
| Corrective action | Investigate workflow design, training, access and accountability causes; change the process or system where justified |
| Closure verification | Inspect updated workflow configuration and training evidence; sample subsequent decisions and verify implementation and effectiveness |
| Status | Simulated example only — not a real finding or verified audit result |

## 9. Management review and possible indicators

A management review should be based on actual inputs and recorded decisions, not a blank template. Relevant inputs may include prior action status; changes in context and interested-party needs; AIMS performance; monitoring results; audit results; nonconformities and corrective actions; risk and impact assessment status; opportunities for improvement; and resource adequacy.

Possible indicators for the fictional recruitment service:
- Percentage of AI systems with a current named owner
- Percentage of high/critical risks with approved treatment plans
- Percentage of sampled human-review decisions with documented rationale
- Overdue supplier reviews
- Time to triage AI incidents
- Completion of role-based training
- Completion of scheduled monitoring

Targets must be justified and approved. Do not invent performance results.

## 10. Prioritised improvement backlog

1. **Traceability:** Link each requirement/control mapping to a named evidence item, test procedure, test status, result and reviewer.
2. **Risk logic:** Record scoring rationale, risk owner, existing controls, treatment owner, deadline, residual-risk assessment and authorised acceptance.
3. **Human oversight:** Define what reviewers inspect, when they can override, how overrides are logged, escalation routes and how reviewer competence is assessed.
4. **Impact assessment:** Identify affected groups, plausible harms, severity and likelihood, mitigations, consultation inputs where appropriate and residual impacts requiring a decision.
5. **Supplier governance:** Record provider identity, service boundaries, data access, subprocessors, change notification, incident cooperation, assurance evidence and exit arrangements.
6. **Incidents and monitoring:** Define AI incident examples, detection sources, triage criteria, escalation owners, evidence preservation, lessons learned and reassessment triggers.
7. **Governance approval:** Distinguish draft from approved documents; record approver, approval date, version, review date and change history.
8. **Audit quality:** Record sampling rationale, objective evidence, criteria, factual statements, finding rationale and closure verification. Keep proposed tests separate from verified tests.

## 11. Limitations and professional boundaries

This is a learning portfolio, not a certification audit. It does not establish that MaltaAI Solutions Ltd. exists, that the described AI system exists, that any control is implemented, that an AI system is safe or unbiased, or that legal obligations have been satisfied.

ISO/IEC 42001 is a management-system standard. Certification to a management-system standard does not, by itself, guarantee model accuracy, fairness, safety, privacy or legal compliance. Specific legal obligations and applicability must be assessed by qualified personnel against current authoritative sources.

## 12. Five-minute interview walkthrough

1. **Context and scope:** Explain the fictional recruitment SaaS use case, intended purpose and affected parties.
2. **Risk and impact:** Explain one concrete harm scenario, its scoring rationale and what evidence would validate the rating.
3. **Control design:** Explain human oversight, supplier governance and monitoring measures, including accountable owners.
4. **Audit testing:** Explain the criterion, evidence request, sample and test steps. State clearly that proposed tests were not performed.
5. **Finding and follow-up:** Explain the hypothetical finding, correction, root-cause analysis, residual risk and effectiveness verification.

## 13. Recruiter-facing evidence pack checklist

- [ ] One-page project summary and simulation disclaimer
- [ ] AIMS scope and interested-party/context summary
- [ ] AI inventory sample with owner, purpose, provider, data and lifecycle status
- [ ] Risk sample with scoring rationale, treatment, owner and residual-risk decision
- [ ] Impact assessment showing affected parties, plausible harm, mitigations and remaining impact
- [ ] Supplier due-diligence record and contract-control checklist
- [ ] Control-to-evidence mapping with test procedure and evidence status
- [ ] Simulated finding/CAPA record and separate closure-verification plan
- [ ] Management-review summary with proposed indicators clearly labelled
- [ ] README explaining assumptions, limitations, version and checks not performed

## 14. Reference note

Primary management-system reference: ISO/IEC 42001:2023, *Information technology — Artificial intelligence — Management system*. Use a legitimate copy of the standard and approved organisational criteria for clause-level mapping. This case study intentionally avoids inventing clause quotations or claiming that its illustrative tests cover every requirement.

- [ISO — ISO/IEC 42001:2023](https://www.iso.org/standard/81230.html)
- [European Commission — Regulatory framework for AI](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)
