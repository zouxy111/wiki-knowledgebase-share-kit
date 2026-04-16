#!/usr/bin/env python3
"""Tests for extract_terms.py script."""
import sys
from pathlib import Path

# Add scripts directory to path
scripts_dir = Path(__file__).parent.parent / "skills" / "knowledge-base-ingest" / "scripts"
sys.path.insert(0, str(scripts_dir))

import tempfile
from collections import Counter, defaultdict

import pytest
from extract_terms import collect_terms, normalize


def test_normalize_basic():
    assert normalize("  Hello World  ") == "Hello World"
    assert normalize("term:") == "term"
    assert normalize("term,") == "term"
    assert normalize("term，") == "term"


def test_normalize_chinese():
    assert normalize("  中文术语  ") == "中文术语"


def test_collect_terms_from_file():
    with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as f:
        f.write("# Term1\n")
        f.write("Some content about **Term2**.\n")
        f.write("Mentions `Term3` in code.\n")
        f.write("《Term4》 in quotes.\n")
        f.flush()
        
        counter = Counter()
        sources = defaultdict(set)
        collect_terms(Path(f.name), counter, sources)
        
        assert "Term1" in counter
        assert "Term2" in counter
        assert "Term3" in counter
        assert "Term4" in counter
        
        f.close()
        Path(f.name).unlink()


def test_collect_terms_scores():
    with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as f:
        f.write("# ImportantTerm\n")
        f.write("## ImportantTerm\n")
        f.flush()
        
        counter = Counter()
        sources = defaultdict(set)
        collect_terms(Path(f.name), counter, sources)
        
        assert counter["ImportantTerm"] >= 4
        f.close()
        Path(f.name).unlink()


def test_collect_terms_from_directory():
    with tempfile.TemporaryDirectory() as tmpdir:
        dirpath = Path(tmpdir)
        (dirpath / "file1.md").write_text("# Term1\nContent\n", encoding='utf-8')
        (dirpath / "file2.md").write_text("## Term2\nContent\n", encoding='utf-8')
        
        counter = Counter()
        sources = defaultdict(set)
        # Only collect .md files, not the directory itself
        for md_file in dirpath.glob("*.md"):
            collect_terms(md_file, counter, sources)
        
        assert "Term1" in counter
        assert "Term2" in counter
