# Simulated ISO/IEC 42001:2023 AI Management System Portfolio

[![Portfolio checks](https://github.com/ajaykumar76/simulated-iso-42001-aisms-portfolio/actions/workflows/validate.yml/badge.svg?branch=main)](https://github.com/ajaykumar76/simulated-iso-42001-aisms-portfolio/actions/workflows/validate.yml)

**Project:** MaltaAI Solutions Ltd. — fictional AI recruitment SaaS.  
**Status:** Reconstructed simulated portfolio; review and improvement in progress.

## Provenance and limitations

The most recent uploaded archive contained the repository scaffold, not the user's local project source. The files under iso42001/ were therefore reconstructed as illustrative records. They are not recovered copies of the original local project. Review and substantiate them before presenting them as personal project evidence. They do not establish operational implementation, actual audit execution, control effectiveness, certification, legal compliance or conformity with ISO/IEC 42001.

The scenario includes CV extraction, candidate ranking, candidate summaries, a recruitment chatbot and recruitment analytics. Candidate ranking may influence employment-related decisions. A human recruiter is intended to retain final decision authority; this portfolio does not prove that oversight operates in practice or determine a definitive EU AI Act classification.

## Repository contents

- iso42001/: simulated inventory, AI risk register, two distinct impact-assessment views, treatments, supplier register, control mapping, evidence tracker, proposed audit checklist, simulated findings, CAPA/NCR and management-review actions.
- templates/: blank starter templates.
- docs/WORKED_CASE_STUDY.md: narrative walkthrough with proposed audit procedures and limitations.
- docs/CONTENT_AUDIT_AND_LIMITATIONS.md: known content-quality gaps and review plan.
- scripts/validate_portfolio.py: CSV, inventory, score-band and cross-register integrity checks.

All treatment actions are pending; residual-risk approvals are not approved; evidence is not provided or verified; audit procedures are not performed; findings and corrective actions are open; management actions are not approved.

## Validation

Run: python scripts/validate_portfolio.py --require-source

GitHub Actions runs the same check. A passing result confirms structural and selected cross-register consistency only. It does not establish the accuracy of assumptions, completeness of ISO/IEC 42001 requirements, implementation, effectiveness, audit quality, legal compliance or conformity.

## Recommended review sequence

1. Review scope, intended purposes, affected parties and lifecycle boundaries.
2. Approve a documented likelihood/impact methodology and scoring rationale.
3. Validate each risk and impact scenario, affected group, safeguard and residual impact.
4. Build a requirement-level control mapping from a legitimate copy of the standard; do not invent clause references.
5. Link each control to a defined requirement, owner, evidence item, test procedure and result.
6. Keep proposed tests separate from completed tests; never invent audit evidence or closure.
7. Review the two impact-assessment views as separate perspectives.
8. Record unresolved limitations and obtain review before presenting the portfolio.

## References

- [ISO/IEC 42001:2023 — ISO](https://www.iso.org/standard/81230.html)
- [European Commission — AI regulatory framework](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)

**Portfolio owner:** [ajaykumar76](https://github.com/ajaykumar76)
