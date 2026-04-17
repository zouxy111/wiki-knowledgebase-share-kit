#!/usr/bin/env python3
"""Tests for close_read_markdown.py script."""

import json
import sys
import tempfile
from pathlib import Path

# Add scripts directory to path
scripts_dir = (
    Path(__file__).parent.parent / "skills" / "knowledge-base-ingest" / "scripts"
)
sys.path.insert(0, str(scripts_dir))

from close_read_markdown import prepare_run  # noqa: E402


def make_source(path: Path, chapter_two_extra: str = "") -> None:
    path.write_text(
        f"""# Sample Handbook

## Chapter 1

Intro text. Intro text. Intro text.

### Section 1.1

Alpha beta gamma. Alpha beta gamma. Alpha beta gamma.

### Section 1.2

Delta epsilon zeta. Delta epsilon zeta. Delta epsilon zeta.

## Chapter 2

Bridge text. {chapter_two_extra}

### Section 2.1

Theta iota kappa. Theta iota kappa. Theta iota kappa.
""",
        encoding="utf-8",
    )


def test_prepare_run_creates_packets_state_and_links():
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp = Path(tmpdir)
        source = tmp / "source.md"
        out = tmp / "run"
        make_source(source)

        state = prepare_run(
            source=source,
            out_dir=out,
            level=2,
            max_chunk_words=80,
            max_batch_words=60,
            max_chunks_per_batch=2,
            prefix="book-",
        )

        assert state["batch_count"] >= 2
        assert (out / "batch-plan.json").exists()
        assert (out / "reading-state.json").exists()
        assert (out / "README.md").exists()
        packet = out / "batch-packets" / "sample-handbook-chapter-1-b01.md"
        note = out / "batch-notes" / "sample-handbook-chapter-1-b01.json"
        assert packet.exists()
        assert note.exists()

        note_payload = json.loads(note.read_text(encoding="utf-8"))
        assert note_payload["status"] == "pending"
        assert note_payload["batch_key"] == "sample-handbook-chapter-1-b01"
        assert note_payload["batch_hash"]

        packet_text = packet.read_text(encoding="utf-8")
        assert "../batch-notes/sample-handbook-chapter-1-b01.json" in packet_text
        assert "../chunks/001-book-chapter-1.md" in packet_text


def test_prepare_run_preserves_unchanged_batches_and_resets_changed_ones():
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp = Path(tmpdir)
        source = tmp / "source.md"
        out = tmp / "run"
        make_source(source)

        prepare_run(
            source=source,
            out_dir=out,
            level=2,
            max_chunk_words=80,
            max_batch_words=60,
            max_chunks_per_batch=2,
            prefix="book-",
        )

        first_note_path = out / "batch-notes" / "sample-handbook-chapter-1-b01.json"
        second_note_path = out / "batch-notes" / "sample-handbook-chapter-2-b01.json"
        first_note = json.loads(first_note_path.read_text(encoding="utf-8"))
        second_note = json.loads(second_note_path.read_text(encoding="utf-8"))
        first_note.update(
            {
                "status": "completed",
                "summary": "The first batch defines Alpha as the core concept.",
                "concepts": ["Alpha"],
                "candidate_topics": ["Alpha"],
            }
        )
        second_note.update(
            {
                "status": "completed",
                "summary": "The second batch defines Gamma as a later topic.",
                "concepts": ["Gamma"],
                "candidate_topics": ["Gamma"],
            }
        )
        first_note_path.write_text(
            json.dumps(first_note, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        second_note_path.write_text(
            json.dumps(second_note, ensure_ascii=False, indent=2), encoding="utf-8"
        )

        make_source(source, chapter_two_extra="Updated material changed this batch.")
        state = prepare_run(
            source=source,
            out_dir=out,
            level=2,
            max_chunk_words=80,
            max_batch_words=60,
            max_chunks_per_batch=2,
            prefix="book-",
        )

        assert state["completed_batches"] == 1
        assert state["changed_batches"] == 1
        batches = {row["batch_key"]: row for row in state["batches"]}
        assert batches["sample-handbook-chapter-1-b01"]["status"] == "completed"
        assert batches["sample-handbook-chapter-1-b01"]["change_status"] == "unchanged"
        assert batches["sample-handbook-chapter-2-b01"]["status"] == "pending"
        assert batches["sample-handbook-chapter-2-b01"]["change_status"] == "changed"

        archived = list(
            (out / "stale-notes").glob("sample-handbook-chapter-2-b01--*.json")
        )
        assert archived, "changed batch note should be archived for traceability"
        refreshed_note = json.loads(second_note_path.read_text(encoding="utf-8"))
        assert refreshed_note["status"] == "pending"
        assert refreshed_note["summary"] == ""

        second_packet = (
            out / "batch-packets" / "sample-handbook-chapter-2-b01.md"
        ).read_text(encoding="utf-8")
        assert "The first batch defines Alpha as the core concept." in second_packet
        assert "Alpha (x1)" in second_packet
