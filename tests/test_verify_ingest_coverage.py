#!/usr/bin/env python3
"""Tests for verify_ingest_coverage.py."""
import sys
from pathlib import Path

scripts_dir = Path(__file__).parent.parent / "skills" / "knowledge-base-ingest" / "scripts"
sys.path.insert(0, str(scripts_dir))

from verify_ingest_coverage import parse_coverage_table, validate_coverage


def test_parse_coverage_table_basic(tmp_path):
    coverage = tmp_path / "coverage-map.md"
    coverage.write_text(
        """# Source Coverage Map

| index | file | title | lines | words | status | target pages | notes |
|---|---|---|---|---:|---|---|---|
| 001 | 001-a.md | A | 1-10 | 100 | covered | pages/a.md |  |
""",
        encoding="utf-8",
    )
    rows = parse_coverage_table(coverage)
    assert rows == [
        {
            "index": "001",
            "file": "001-a.md",
            "title": "A",
            "lines": "1-10",
            "words": "100",
            "status": "covered",
            "target pages": "pages/a.md",
            "notes": "",
        }
    ]


def test_validate_coverage_passes_for_final_statuses():
    manifest = [
        {"file": "001-a.md", "title": "A"},
        {"file": "002-b.md", "title": "B"},
    ]
    coverage_rows = [
        {
            "file": "001-a.md",
            "status": "covered",
            "target pages": "pages/a.md",
            "notes": "",
        },
        {
            "file": "002-b.md",
            "status": "intentionally-omitted",
            "target pages": "",
            "notes": "Appendix duplicate kept only in overview",
        },
    ]
    assert validate_coverage(manifest, coverage_rows) == []


def test_validate_coverage_flags_incomplete_or_missing_rows():
    manifest = [
        {"file": "001-a.md", "title": "A"},
        {"file": "002-b.md", "title": "B"},
    ]
    coverage_rows = [
        {
            "file": "001-a.md",
            "status": "unread",
            "target pages": "",
            "notes": "",
        }
    ]
    problems = validate_coverage(manifest, coverage_rows)
    assert any("001-a.md: status is still incomplete" in problem for problem in problems)
    assert any("Missing coverage row for manifest file: 002-b.md" in problem for problem in problems)


def test_validate_coverage_requires_target_pages_for_covered_status():
    manifest = [{"file": "001-a.md", "title": "A"}]
    coverage_rows = [
        {
            "file": "001-a.md",
            "status": "covered",
            "target pages": "",
            "notes": "",
        }
    ]
    problems = validate_coverage(manifest, coverage_rows)
    assert any("requires target pages" in problem for problem in problems)
