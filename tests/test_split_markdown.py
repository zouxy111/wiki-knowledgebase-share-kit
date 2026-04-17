#!/usr/bin/env python3
"""Tests for split_markdown.py script."""
import sys
from pathlib import Path

# Add scripts directory to path
scripts_dir = Path(__file__).parent.parent / "skills" / "knowledge-base-ingest" / "scripts"
sys.path.insert(0, str(scripts_dir))

from split_markdown import (
    Chunk,
    Heading,
    choose_level,
    count_words,
    find_headings,
    slugify,
    split_range,
    window_split_chunks,
    write_coverage_map,
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
    chunks = split_range(lines, headings, 2, 0, len(lines), 1800, 400)
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
    chunks = split_range(lines, headings, 2, 0, len(lines), 1800, 400)
    assert len(chunks) == 1
    assert chunks[0].title == "Chapter 1"


def test_split_range_falls_back_to_line_windows_for_oversized_section():
    lines = ["## Chapter 1\n"] + [f"Line {i}\n" for i in range(1, 11)]
    headings = find_headings(lines)
    chunks = split_range(lines, headings, 2, 0, len(lines), 9999, 4)
    assert len(chunks) == 3
    assert chunks[0].title == "Chapter 1 (Part 1)"
    assert chunks[1].title == "Chapter 1 (Part 2)"
    assert chunks[2].title == "Chapter 1 (Part 3)"


def test_window_split_chunks_handles_headingless_source():
    lines = [f"Line {i}\n" for i in range(1, 10)]
    chunks = window_split_chunks(
        lines,
        0,
        len(lines),
        base_title="Source",
        level=1,
        breadcrumb=["Source"],
        max_lines=4,
    )
    assert len(chunks) == 3
    assert chunks[0].title == "Source (Part 1)"
    assert chunks[1].start_line == 5
    assert chunks[2].end_line == 9


def test_write_coverage_map_contains_all_manifest_rows(tmp_path):
    manifest = [
        {
            "index": 0,
            "file": "000-preamble.md",
            "title": "Preamble",
            "start_line": 1,
            "end_line": 10,
            "word_count": 100,
            "level": 0,
            "breadcrumb": ["Preamble"],
        },
        {
            "index": 1,
            "file": "001-a.md",
            "title": "A",
            "start_line": 11,
            "end_line": 20,
            "word_count": 80,
            "level": 2,
            "breadcrumb": ["A"],
        },
    ]
    write_coverage_map(manifest, tmp_path)
    text = (tmp_path / "coverage-map.md").read_text(encoding="utf-8")
    assert "000-preamble.md" in text
    assert "001-a.md" in text
    assert text.count("| unread |") == 2


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
