#!/usr/bin/env python3
"""Tests for split_markdown.py script."""
import sys
from pathlib import Path

# Add scripts directory to path
scripts_dir = Path(__file__).parent.parent / "skills" / "knowledge-base-ingest" / "scripts"
sys.path.insert(0, str(scripts_dir))

import pytest
from split_markdown import (
    Chunk,
    Heading,
    choose_level,
    count_words,
    find_headings,
    slugify,
    split_range,
)


def test_slugify_basic():
    assert slugify("Hello World") == "hello-world"
    assert slugify("  Padded  ") == "padded"
    assert slugify("Special!@#$%Chars") == "special-chars"


def test_slugify_empty():
    assert slugify("") == "section"
    assert slugify("   ") == "section"


def test_slugify_chinese():
    # Chinese characters should be filtered out by NON_SLUG_RE
    # resulting in empty string which becomes 'section'
    assert slugify("中文标题") == "section"


def test_find_headings_simple():
    lines = [
        "# Main Title\n",
        "Some content\n",
        "## Section 1\n",
        "Content here\n",
        "### Subsection 1.1\n",
        "More content\n",
    ]
    headings = find_headings(lines)
    assert len(headings) == 3
    assert headings[0].level == 1
    assert headings[0].title == "Main Title"
    assert headings[1].level == 2
    assert headings[1].title == "Section 1"
    assert headings[2].level == 3
    assert headings[2].title == "Subsection 1.1"


def test_find_headings_breadcrumb():
    lines = [
        "# Main\n",
        "## Section\n",
        "### Subsection\n",
    ]
    headings = find_headings(lines)
    assert headings[2].breadcrumb == ["Main", "Section", "Subsection"]


def test_choose_level_exists():
    headings = [Heading(0, 1, "H1", ["H1"]), Heading(1, 2, "H2", ["H1", "H2"])]
    assert choose_level(headings, 2) == 2
    assert choose_level(headings, 1) == 1


def test_choose_level_fallback():
    headings = [Heading(0, 2, "H2", ["H2"]), Heading(1, 3, "H3", ["H2", "H3"])]
    assert choose_level(headings, 1) == 2


def test_count_words_english():
    lines = ["Hello world this is a test\n"]
    # \b\w+\b matches 6 words: Hello, world, this, is, a, test
    assert count_words(lines) == 6


def test_count_words_empty():
    assert count_words([]) == 0


def test_split_range_simple():
    lines = [
        "## Chapter 1\n",
        "Content 1\n",
        "## Chapter 2\n",
        "Content 2\n",
    ]
    headings = find_headings(lines)
    chunks = split_range(lines, headings, 2, 0, len(lines), 1800)
    assert len(chunks) == 2
    assert chunks[0].title == "Chapter 1"
    assert chunks[1].title == "Chapter 2"


def test_split_range_with_preamble():
    lines = [
        "Preamble text\n",
        "More preamble\n",
        "## Chapter 1\n",
        "Content\n",
    ]
    headings = find_headings(lines)
    chunks = split_range(lines, headings, 2, 0, len(lines), 1800)
    assert len(chunks) == 1
    assert chunks[0].title == "Chapter 1"


def test_chunk_structure():
    chunk = Chunk(
        title="Test",
        level=2,
        slug="test",
        lines=["line1\n", "line2\n"],
        start_line=1,
        end_line=3,
        word_count=5,
        breadcrumb=["Parent", "Test"],
    )
    assert chunk.word_count == 5
    assert len(chunk.lines) == 2
