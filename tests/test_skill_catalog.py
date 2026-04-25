#!/usr/bin/env python3
"""Tests for scripts/skill_catalog.py."""

import sys
from pathlib import Path

scripts_dir = Path(__file__).parent.parent / "scripts"
sys.path.insert(0, str(scripts_dir))

# fmt: off
from skill_catalog import capability_areas, render_skill_table, skill_names  # noqa: E402
# fmt: on


def test_skill_names_come_from_catalog_in_expected_order():
    names = skill_names()
    assert names[0] == "knowledge-base-kit-guide"
    assert names[-1] == "work-journal"
    assert len(names) == 10


def test_render_skill_table_uses_catalog_content():
    table = render_skill_table(language="zh")
    assert "| 3 | `knowledge-base-ingest` | Ingest | 长文档导入与结构化重组 |" in table


def test_capability_areas_are_unique_and_ordered():
    areas = capability_areas()
    assert areas == [
        "Onboarding / Orchestration",
        "Ingest",
        "Maintenance",
        "Audit",
        "Project management",
        "Team coordination",
        "Delivery audit",
        "Working profile",
        "Work journal",
    ]
