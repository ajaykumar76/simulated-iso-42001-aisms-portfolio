#!/usr/bin/env python3
"""Cross-register integrity checks for the fictional ISO/IEC 42001 portfolio."""
import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "iso42001"

def load(relative):
    with (BASE / relative).open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))

def norm(value):
    value = re.sub(r"[^a-z0-9]+", "", (value or "").casefold())
    return {
        "candidatesummaries": "candidatesummarygenerator",
        "candidatesummary": "candidatesummarygenerator",
        "candidateranking": "candidaterankingengine",
        "cvextraction": "cvextractionassistant",
        "analytics": "recruitmentanalytics",
    }.get(value, value)

def main():
    errors = []
    p = {
        "systems": "03-AI-System-Inventory/AI_System_Inventory.csv",
        "risks": "04-AI-Risk-Assessment/AI_Risk_Assessment_Register.csv",
        "impact1": "05-AI-Impact-Assessment/AI_Impact_Assessment_Register.csv",
        "treatments": "06-Risk-Treatment/AI_Risk_Treatment_Plan.csv",
        "impact2": "16-AI-Impact-Assessment/AI_Impact_Assessment_Register.csv",
        "controls": "09-Control-Mapping/ISO42001_Control_Mapping.csv",
        "evidence": "10-Control-Evidence/AI_Control_Evidence_Tracker.csv",
        "checklist": "11-Internal-Audit/AI_Internal_Audit_Checklist.csv",
        "findings": "11-Internal-Audit/AI_Audit_Findings_Register.csv",
        "capa": "11-Internal-Audit/AI_Audit_CAPA_Cross_Reference.csv",
        "ncr": "12-NCR-CAPA/AI_NCR_CAPA_Register.csv",
    }
    try:
        d = {key: load(path) for key, path in p.items()}
    except (OSError, csv.Error, UnicodeError) as exc:
        print(f"ERROR: unable to load register: {exc}")
        return 1

    def ids(key, column):
        return {(r.get(column) or "").strip() for r in d[key] if (r.get(column) or "").strip()}

    risk_ids = ids("risks", "Risk ID")
    control_ids = ids("controls", "Control ID")
    finding_ids = ids("findings", "Finding ID")
    system_names = {norm(r.get("AI system")) for r in d["systems"]}

    for key in ("risks", "impact1", "impact2", "treatments"):
        for row in d[key]:
            system = norm(row.get("System"))
            if system and system not in {"all", "allsystems"} and system not in system_names:
                errors.append(f"{p[key]}: unknown system reference {row.get('System')!r}")

    for row in d["risks"]:
        rid = row.get("Risk ID", "")
        try:
            likelihood, impact, score = int(row["Likelihood"]), int(row["Impact"]), int(row["Score"])
            expected = "Low" if score <= 4 else "Medium" if score <= 9 else "High" if score <= 15 else "Critical"
            if not (1 <= likelihood <= 5 and 1 <= impact <= 5) or score != likelihood * impact:
                errors.append(f"{rid}: score arithmetic or 1-5 bounds invalid")
            if row.get("Rating") != expected:
                errors.append(f"{rid}: expected illustrative rating {expected}")
        except (KeyError, TypeError, ValueError):
            errors.append(f"{rid}: invalid risk score")

    treatment_by_id = {r.get("Risk ID"): r for r in d["treatments"]}
    for row in d["risks"]:
        treatment = treatment_by_id.get(row.get("Risk ID"))
        if not treatment:
            errors.append(f"{row.get('Risk ID')}: missing treatment record")
        elif treatment.get("Rating") != row.get("Rating"):
            errors.append(f"{row.get('Risk ID')}: treatment rating differs from risk register")

    links = [
        ("treatments", "Risk ID", risk_ids),
        ("impact1", "Related risk ID", risk_ids),
        ("impact2", "Related risk ID", risk_ids),
        ("evidence", "Control ID", control_ids),
        ("checklist", "Control ID", control_ids),
        ("capa", "Finding ID", finding_ids),
        ("ncr", "Finding ID", finding_ids),
    ]
    for key, column, valid in links:
        for row in d[key]:
            value = (row.get(column) or "").strip()
            if value and value not in valid:
                errors.append(f"{p[key]}: {column} {value} has no matching record")

    finding_by_id = {r.get("Finding ID"): r for r in d["findings"]}
    for key in ("capa", "ncr"):
        for row in d[key]:
            finding = finding_by_id.get(row.get("Finding ID"))
            if not finding:
                continue
            if row.get("Severity") and row.get("Severity") != finding.get("Severity"):
                errors.append(f"{p[key]}: severity mismatch for {row.get('Finding ID')}")
            action = row.get("Corrective action") or row.get("Action")
            if action and action != finding.get("Action"):
                errors.append(f"{p[key]}: corrective action mismatch for {row.get('Finding ID')}")

    if errors:
        print("Cross-register validation failed:")
        for error in errors:
            print("ERROR:", error)
        return 1
    print("Cross-register validation passed: systems, risk scores, treatments, impact links, control links and CAPA/NCR links.")
    print("This is a data-integrity check only; it does not establish implementation, audit assurance or conformity.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
