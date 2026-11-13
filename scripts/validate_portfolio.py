#!/usr/bin/env python3
"""Validate repository hygiene for the simulated ISO/IEC 42001 portfolio.

Checks are structural only. They do not establish implementation, effectiveness,
legal compliance, audit quality, or conformity with ISO/IEC 42001.
"""
from __future__ import annotations

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
REQUIRED_SOURCE_FILES = (
    "03-AI-System-Inventory/AI_System_Inventory.csv",
    "04-AI-Risk-Assessment/AI_Risk_Assessment_Register.csv",
    "05-AI-Impact-Assessment/AI_Impact_Assessment_Register.csv",
    "06-Risk-Treatment/AI_Risk_Treatment_Plan.csv",
    "08-Data-and-Supplier-Governance/AI_Data_and_Supplier_Register.csv",
    "09-Control-Mapping/ISO42001_Control_Mapping.csv",
    "10-Control-Evidence/AI_Control_Evidence_Tracker.csv",
    "11-Internal-Audit/AI_Audit_Findings_Register.csv",
    "12-NCR-CAPA/AI_NCR_CAPA_Register.csv",
    "16-AI-Impact-Assessment/AI_Impact_Assessment_Register.csv",
)


def csv_files() -> list[Path]:
    return sorted(
        p for p in ROOT.rglob("*.csv")
        if not any(part in SKIP_DIRS for part in p.relative_to(ROOT).parts)
    )


def validate_csv(path: Path) -> list[str]:
    issues: list[str] = []
    rel = path.relative_to(ROOT)
    try:
        with path.open("r", encoding="utf-8-sig", newline="") as handle:
            rows = list(csv.reader(handle))
    except (OSError, UnicodeError, csv.Error) as exc:
        return [f"{rel}: cannot read CSV ({exc})"]

    if not rows:
        return [f"{rel}: file is empty"]
    header = rows[0]
    if not header or all(not cell.strip() for cell in header):
        return [f"{rel}: header row is empty"]

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
    text = readme.read_text(encoding="utf-8")
    for raw in re.findall(r"!?\[[^\]]*\]\(([^)]+)\)", text):
        target = raw.strip().split()[0].strip("<>")
        if not target or target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        target = unquote(target.split("#", 1)[0])
        if not target:
            continue
        if not (ROOT / target).resolve().is_relative_to(ROOT.resolve()):
            issues.append(f"README.md: link escapes repository: {raw}")
        elif not (ROOT / target).exists():
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
    if len(source_files) < 40:
        issues.append(f"iso42001/: found {len(source_files)} files; expected at least 40 reviewed source files")
    for relative in REQUIRED_SOURCE_FILES:
        if not (source / relative).is_file():
            issues.append(f"iso42001/: required source file missing: {relative}")
    return issues, warnings


def main() -> int:
    files = csv_files()
    issues: list[str] = []
    warnings: list[str] = []

    present_templates = {p.name for p in (ROOT / "templates").glob("*.csv")} if (ROOT / "templates").exists() else set()
    for missing in sorted(REQUIRED_TEMPLATES - present_templates):
        issues.append(f"templates/: required template missing: {missing}")

    for path in files:
        issues.extend(validate_csv(path))
    issues.extend(validate_readme_links())
    source_issues, source_warnings = validate_source_tree()
    issues.extend(source_issues)
    warnings.extend(source_warnings)

    if issues:
        print("Portfolio validation failed:")
        for issue in issues:
            print(f"ERROR: {issue}")
        return 1

    print(f"CSV structure checks passed for {len(files)} file(s).")
    print("README local-link checks passed.")
    print("Required template inventory check passed.")
    for warning in warnings:
        print(f"NOTICE: {warning}")
    print("These checks do not assess control implementation, evidence sufficiency, audit conclusions, legal compliance, or ISO/IEC 42001 conformity.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
