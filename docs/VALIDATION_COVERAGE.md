# Validation coverage and limitations

GitHub Actions runs two local validation scripts on pushes and pull requests to `main`.

## Automated checks

- CSV readability, header integrity, row widths, required templates and expected register row counts.
- Required record identifiers and duplicate identifiers in the primary validator's controlled registers.
- Risk arithmetic and the repository's illustrative rating bands.
- Risk-to-treatment rating consistency.
- AI system names in risk, treatment and impact records resolve to the inventory (with documented normalisation for concise labels).
- Impact assessments, evidence records, audit checklist items, CAPA and NCR records reference existing risk, control or finding identifiers.
- CAPA/NCR severity and corrective-action descriptions agree with the findings register.

## Limitations

These are data-integrity checks, not an audit opinion. They do not prove that a policy was approved, a control was implemented or operated, a supplier was assessed, a person was consulted, a system was tested, a risk was accepted, an audit was performed, or a legal obligation was met. They do not establish ISO/IEC 42001 conformity, certification readiness or EU AI Act compliance.

This is a fictional, simulated portfolio. Keep operational evidence, synthetic examples, proposed actions and unperformed work clearly distinguished. A passing CI result must never be presented as real-world assurance.
