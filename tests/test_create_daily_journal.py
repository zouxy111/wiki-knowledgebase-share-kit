from __future__ import annotations

from datetime import date

from tests.helpers import load_module


def test_create_daily_journal_quotes_project_safely(tmp_path):
    journal = load_module(
        "test_create_daily_journal_module",
        "skills/work-journal/scripts/create_daily_journal.py",
    )
    target = date(2026, 4, 21)
    path = journal.create_journal_file(
        tmp_path,
        target,
        'Project "Alpha"\nnext-line',
    )

    text = path.read_text(encoding="utf-8")
    assert 'projects: ["Project \\"Alpha\\"\\nnext-line"]' in text
