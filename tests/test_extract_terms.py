from __future__ import annotations

from collections import Counter, defaultdict

from tests.helpers import load_module


def test_extract_terms_filters_generic_chinese_headings(tmp_path):
    extract_terms = load_module(
        "test_extract_terms_module",
        "skills/knowledge-base-ingest/scripts/extract_terms.py",
    )
    path = tmp_path / "sample.md"
    path.write_text(
        "# 概述\n\n## 真正术语\n\n《目录》\n\n**关键概念**\n",
        encoding="utf-8",
    )

    counter = Counter()
    sources = defaultdict(set)
    extract_terms.collect_terms(path, counter, sources)

    assert "概述" not in counter
    assert "目录" not in counter
    assert "真正术语" in counter
    assert "关键概念" in counter
