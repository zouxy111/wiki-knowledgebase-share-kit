from __future__ import annotations

import pytest

from tests.helpers import load_module


def test_ingest_scripts_import_without_cwd_hacks():
    close_read = load_module(
        "test_close_read_markdown_module",
        "skills/knowledge-base-ingest/scripts/close_read_markdown.py",
    )
    synthesize = load_module(
        "test_synthesize_knowledge_module",
        "skills/knowledge-base-ingest/scripts/synthesize_knowledge.py",
    )

    assert hasattr(close_read, "prepare_chunks")
    assert hasattr(synthesize, "build_synthesis")


def test_prepare_chunks_raises_catchable_error_without_headings(tmp_path):
    close_read = load_module(
        "test_close_read_markdown_prepare_chunks",
        "skills/knowledge-base-ingest/scripts/close_read_markdown.py",
    )
    source = tmp_path / "headingless.md"
    source.write_text("plain text only\nstill no headings\n", encoding="utf-8")

    with pytest.raises(close_read.ChunkPreparationError):
        close_read.prepare_chunks(
            source=source,
            chunks_dir=tmp_path / "chunks",
            level=2,
            max_chunk_words=100,
            max_chunk_lines=40,
            prefix="",
            force_resplit=False,
        )
