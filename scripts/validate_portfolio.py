#!/usr/bin/env python3
"""Structural validation for the simulated ISO/IEC 42001 portfolio.

This checks repository hygiene and selected archive inventory counts only. It
does not establish implementation, effectiveness, audit quality, legal
compliance, or conformity with ISO/IEC 42001.
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
SKIP_DIRS = {".git", ".venv", "venv", "__pycache__", "node_modules"}
REQUIRED_TEMPLATES = {
    "AI_System_Inventory_Template.csv",
    "AI_Risk_Register_Template.csv",
    "AI_Impact_Assessment_Template.csv",
    "Risk_Treatment_Plan_Template.csv",
    "Supplier_Register_Template.csv",
    "Control_Evidence_Register_Template.csv",
    "Audit_Findings_CAPA_Template.csv",
}
# Expected data rows (excluding the CSV header) in the reviewed 50-file archive.
EXPECTED_SOURCE_ROWS = {
    "03-AI-System-Inventory/AI_System_Inventory.csv": 5,
    "04-AI-Risk-Assessment/AI_Risk_Assessment_Register.csv": 10,
    "05-AI-Impact-Assessment/AI_Impact_Assessment_Register.csv": 8,
    "06-Risk-Treatment/AI_Risk_Treatment_Plan.csv": 10,
    "08-Data-and-Supplier-Governance/AI_Data_and_Supplier_Register.csv": 5,
    "09-Control-Mapping/ISO42001_Control_Mapping.csv": 14,
    "10-Control-Evidence/AI_Control_Evidence_Tracker.csv": 15,
    "11-Internal-Audit/AI_Internal_Audit_Checklist.csv": 15,
    "11-Internal-Audit/AI_Audit_Findings_Register.csv": 6,
    "11-Internal-Audit/AI_Audit_CAPA_Cross_Reference.csv": 6,
    "12-NCR-CAPA/AI_NCR_CAPA_Register.csv": 6,
    "13-Management-Review/AI_Management_Review_Action_Register.csv": 6,
    "16-AI-Impact-Assessment/AI_Impact_Assessment_Register.csv": 8,
}


def csv_files() -> list[Path]:
    return sorted(
        p for p in ROOT.rglob("*.csv")
        if not any(part in SKIP_DIRS for part in p.relative_to(ROOT).parts)
    )


def read_csv(path: Path) -> tuple[list[list[str]] | None, str | None]:
    try:
        with path.open("r", encoding="utf-8-sig", newline="") as handle:
            return list(csv.reader(handle)), None
    except (OSError, UnicodeError, csv.Error) as exc:
        return None, str(exc)


def validate_csv(path: Path) -> list[str]:
    rows, error = read_csv(path)
    rel = path.relative_to(ROOT)
    if error:
        return [f"{rel}: cannot read CSV ({error})"]
    assert rows is not None
    if not rows:
        return [f"{rel}: file is empty"]
    header = rows[0]
    if not header or all(not cell.strip() for cell in header):
        return [f"{rel}: header row is empty"]

    issues: list[str] = []
    normalized = [cell.strip().casefold() for cell in header]
    if any(not cell for cell in normalized):
        issues.append(f"{rel}: header contains a blank column name")
    duplicates = sorted({name for name in normalized if name and normalized.count(name) > 1})
    if duplicates:
        issues.append(f"{rel}: duplicate column name(s): {', '.join(duplicates)}")

    for line_no, row in enumerate(rows[1:], start=2):
        if not row or all(not cell.strip() for cell in row):
            continue
        if len(row) != len(header):
            issues.append(f"{rel}:{line_no}: expected {len(header)} columns, found {len(row)}")
    return issues


def validate_readme_links() -> list[str]:
    readme = ROOT / "README.md"
    if not readme.is_file():
        return ["README.md is missing"]
    issues: list[str] = []
    content = readme.read_text(encoding="utf-8")
    for raw in re.findall(r"!?\[[^\]]*\]\(([^)]+)\)", content):
        target = raw.strip().split()[0].strip("<>")
        if not target or target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        target = unquote(target.split("#", 1)[0])
        if not target:
            continue
        resolved = (ROOT / target).resolve()
        if not resolved.is_relative_to(ROOT.resolve()):
            issues.append(f"README.md: link escapes repository: {raw}")
        elif not resolved.exists():
            issues.append(f"README.md: broken local link: {raw}")
    return issues


def validate_source_tree() -> tuple[list[str], list[str]]:
    source = ROOT / "iso42001"
    warnings: list[str] = []
    issues: list[str] = []
    if not source.exists():
        warnings.append("iso42001/ source records are not published yet; only templates and documentation are being checked.")
        return issues, warnings
    if not source.is_dir():
        return ["iso42001 exists but is not a directory"], warnings

    source_files = [p for p in source.rglob("*") if p.is_file()]
    if len(source_files) < 50:
        issues.append(f"iso42001/: found {len(source_files)} files; expected at least 50 files in the reviewed working set")

    for relative, expected_rows in EXPECTED_SOURCE_ROWS.items():
        path = source / relative
        if not path.is_file():
            issues.append(f"iso42001/: required source file missing: {relative}")
            continue
        rows, error = read_csv(path)
        if error:
            issues.append(f"iso42001/{relative}: cannot read CSV ({error})")
            continue
        assert rows is not None
        actual_rows = sum(1 for row in rows[1:] if row and any(cell.strip() for cell in row))
        if actual_rows != expected_rows:
            issues.append(f"iso42001/{relative}: expected {expected_rows} data rows, found {actual_rows}")
    return issues, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate the simulated ISO/IEC 42001 portfolio.")
    parser.add_argument(
        "--require-source",
        action="store_true",
        help="Fail unless the complete reviewed iso42001/ source project is present.",
    )
    args = parser.parse_args()

    files = csv_files()
    issues: list[str] = []
    warnings: list[str] = []

    template_dir = ROOT / "templates"
    present_templates = {p.name for p in template_dir.glob("*.csv")} if template_dir.exists() else set()
    for missing in sorted(REQUIRED_TEMPLATES - present_templates):
        issues.append(f"templates/: required template missing: {missing}")

    for path in files:
        issues.extend(validate_csv(path))
    issues.extend(validate_readme_links())
    source_issues, source_warnings = validate_source_tree()
    issues.extend(source_issues)
    warnings.extend(source_warnings)
    if args.require_source and not (ROOT / "iso42001").is_dir():
        issues.append("iso42001/: required source project is absent; publish the reviewed source records before this CI check can pass.")

    if issues:
        print("Portfolio validation failed:")
        for issue in issues:
            print(f"ERROR: {issue}")
        return 1

    print(f"CSV structure checks passed for {len(files)} file(s).")
    print("README local-link checks passed.")
    print("Required template inventory check passed.")
    if (ROOT / "iso42001").is_dir():
        print(f"Reviewed source inventory checks passed ({len(EXPECTED_SOURCE_ROWS)} register row-count checks).")
    for warning in warnings:
        print(f"NOTICE: {warning}")
    print("These checks do not assess control implementation, evidence sufficiency, audit conclusions, legal compliance, or ISO/IEC 42001 conformity.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
