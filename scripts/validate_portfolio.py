#!/usr/bin/env python3
"""Validate CSV hygiene in this simulated ISO 42001 portfolio.

This checks file integrity only. It does not assess whether controls operate,
whether evidence is sufficient, or whether the portfolio conforms to ISO 42001.
"""
from __future__ import annotations

import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKIP_DIRS = {".git", ".venv", "venv", "__pycache__", "node_modules"}


def csv_files() -> list[Path]:
    return sorted(
        p for p in ROOT.rglob("*.csv")
        if not any(part in SKIP_DIRS for part in p.relative_to(ROOT).parts)
    )


def validate(path: Path) -> list[str]:
    issues: list[str] = []
    try:
        with path.open("r", encoding="utf-8-sig", newline="") as handle:
            rows = list(csv.reader(handle))
    except (OSError, UnicodeError, csv.Error) as exc:
        return [f"{path.relative_to(ROOT)}: cannot read CSV ({exc})"]

    rel = path.relative_to(ROOT)
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

    expected_width = len(header)
    for line_no, row in enumerate(rows[1:], start=2):
        if not row or all(not cell.strip() for cell in row):
            continue
        if len(row) != expected_width:
            issues.append(
                f"{rel}:{line_no}: expected {expected_width} columns, found {len(row)}"
            )

    return issues


def main() -> int:
    files = csv_files()
    if not files:
        print("No CSV files found; nothing to validate.")
        return 0

    issues: list[str] = []
    for path in files:
        issues.extend(validate(path))

    if issues:
        print("CSV validation found issues:")
        for issue in issues:
            print(f"- {issue}")
        return 1

    print(f"CSV structure check passed for {len(files)} file(s).")
    print("Note: this is a file-format check, not an audit or control-effectiveness assessment.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
