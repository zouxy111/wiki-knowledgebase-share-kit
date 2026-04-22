from __future__ import annotations

import sys

from tests.helpers import load_module


def test_suggest_related_links_refuses_large_page_sets(tmp_path, monkeypatch, capsys):
    suggest = load_module(
        "test_suggest_related_links_module",
        "skills/knowledge-base-ingest/scripts/suggest_related_links.py",
    )
    for idx in range(3):
        (tmp_path / f"page-{idx}.md").write_text(
            f"# Page {idx}\n\nshared token {idx}\n", encoding="utf-8"
        )

    monkeypatch.setattr(
        sys,
        "argv",
        [
            "suggest_related_links.py",
            str(tmp_path),
            "--max-pages",
            "2",
        ],
    )

    assert suggest.main() == 1
    captured = capsys.readouterr()
    assert "Refusing to score 3 pages pairwise" in captured.err
