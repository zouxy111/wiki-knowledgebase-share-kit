from __future__ import annotations

from tests.helpers import load_module


def test_coverage_map_round_trips_escaped_pipe_cells(tmp_path):
    split_markdown = load_module(
        "test_split_markdown_for_coverage",
        "skills/knowledge-base-ingest/scripts/split_markdown.py",
    )
    verify = load_module(
        "test_verify_ingest_coverage_module",
        "skills/knowledge-base-ingest/scripts/verify_ingest_coverage.py",
    )

    manifest = [
        {
            "index": 1,
            "file": "001-a|b.md",
            "title": "Topic | A",
            "start_line": 1,
            "end_line": 10,
            "word_count": 12,
            "level": 2,
            "breadcrumb": ["Topic | A"],
        }
    ]
    split_markdown.write_coverage_map(manifest, tmp_path)

    rows = verify.parse_coverage_table(tmp_path / "coverage-map.md")
    assert rows == [
        {
            "index": "001",
            "file": "001-a|b.md",
            "title": "Topic | A",
            "lines": "1-10",
            "words": "12",
            "status": "unread",
            "target pages": "",
            "notes": "",
        }
    ]
