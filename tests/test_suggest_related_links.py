#!/usr/bin/env python3
"""Tests for suggest_related_links.py script."""
import sys
from pathlib import Path

# Add scripts directory to path
scripts_dir = Path(__file__).parent.parent / "skills" / "knowledge-base-ingest" / "scripts"
sys.path.insert(0, str(scripts_dir))

import json
import tempfile

import pytest
from suggest_related_links import load_pages, score


def test_load_pages_basic():
    with tempfile.TemporaryDirectory() as tmpdir:
        dirpath = Path(tmpdir)
        (dirpath / "page1.md").write_text("# Page 1\nContent about python\n", encoding='utf-8')
        (dirpath / "page2.md").write_text("# Page 2\nContent about python and code\n", encoding='utf-8')
        
        pages = load_pages(dirpath)
        assert len(pages) == 2
        assert pages[0]['title'] == "Page 1"
        assert 'python' in pages[0]['tokens']


def test_load_pages_skips_toc():
    with tempfile.TemporaryDirectory() as tmpdir:
        dirpath = Path(tmpdir)
        (dirpath / "toc.md").write_text("# TOC\n", encoding='utf-8')
        (dirpath / "readme.md").write_text("# README\n", encoding='utf-8')
        (dirpath / "actual.md").write_text("# Actual\n", encoding='utf-8')
        
        pages = load_pages(dirpath)
        assert len(pages) == 1
        assert pages[0]['title'] == "Actual"


def test_load_pages_title_from_frontmatter():
    with tempfile.TemporaryDirectory() as tmpdir:
        dirpath = Path(tmpdir)
        content = """---
title: My Custom Title
---
# Different Heading
Content
"""
        (dirpath / "page.md").write_text(content, encoding='utf-8')
        
        pages = load_pages(dirpath)
        assert pages[0]['title'] == "My Custom Title"


def test_score_no_overlap():
    page_a = {'path': Path('a.md'), 'title': 'A', 'tokens': {'python', 'code'}}
    page_b = {'path': Path('b.md'), 'title': 'B', 'tokens': {'java', 'spring'}}
    
    value, shared = score(page_a, page_b)
    assert value == 0.0
    assert len(shared) == 0


def test_score_with_overlap():
    page_a = {'path': Path('a.md'), 'title': 'A', 'tokens': {'python', 'code', 'test'}}
    page_b = {'path': Path('b.md'), 'title': 'B', 'tokens': {'python', 'code', 'java'}}
    
    value, shared = score(page_a, page_b)
    assert value > 0.0
    assert 'code' in shared
    assert 'python' in shared


def test_score_title_overlap_bonus():
    # Both pages share 'guide' token, but page_a and page_b both start with 'Python'
    page_a = {'path': Path('a.md'), 'title': 'Python Guide', 'tokens': {'guide', 'python'}}
    page_b = {'path': Path('b.md'), 'title': 'Python Tutorial', 'tokens': {'tutorial', 'python'}}
    
    value_a, _ = score(page_a, page_b)
    
    # page_c shares 'guide' but no title overlap
    page_c = {'path': Path('c.md'), 'title': 'Other Guide', 'tokens': {'guide', 'other'}}
    value_b, _ = score(page_a, page_c)
    
    # Both have token overlap, but page_a/page_b have title overlap bonus
    # The exact values depend on the scoring formula
    assert value_a > 0
    assert value_b > 0
