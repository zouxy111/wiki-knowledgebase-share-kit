#!/usr/bin/env python3
"""Tests for close_read_markdown.py script."""

import sys
import json
import tempfile
from pathlib import Path

# Add scripts directory to path
scripts_dir = (
    Path(__file__).parent.parent / "skills" / "knowledge-base-ingest" / "scripts"
)
sys.path.insert(0, str(scripts_dir))

from close_read_markdown import prepare_run  # noqa: E402


def make_source(path: Path) -> None:
    path.write_text(
        """# Sample Handbook

## Chapter 1

Intro text. Intro text. Intro text.

### Section 1.1

Alpha beta gamma. Alpha beta gamma. Alpha beta gamma.

### Section 1.2

Delta epsilon zeta. Delta epsilon zeta. Delta epsilon zeta.

## Chapter 2

Bridge text.

### Section 2.1

Theta iota kappa. Theta iota kappa. Theta iota kappa.
""",
        encoding="utf-8",
    )


def test_prepare_run_creates_packets_and_state():
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
        assert (out / "batch-packets" / "batch-001.md").exists()
        assert (out / "batch-notes" / "batch-001.json").exists()

        note_payload = json.loads(
            (out / "batch-notes" / "batch-001.json").read_text(encoding="utf-8")
        )
        assert note_payload["status"] == "pending"
        assert note_payload["batch_id"] == "batch-001"


def test_prepare_run_refreshes_rolling_state_from_completed_notes():
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

        note = {
            "batch_id": "batch-001",
            "status": "completed",
            "summary": "The first batch defines Alpha as the core concept.",
            "key_claims": ["Alpha governs the first chapter."],
            "concepts": ["Alpha", "Core concept"],
            "procedures": ["Read section 1.1 before section 1.2"],
            "entities": ["Sample Handbook"],
            "open_questions": ["How does Chapter 2 refine Alpha?"],
            "cross_refs": ["book-section-2-1.md"],
            "candidate_topics": ["Alpha"],
        }
        (out / "batch-notes" / "batch-001.json").write_text(
            json.dumps(note, ensure_ascii=False, indent=2), encoding="utf-8"
        )

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
        assert (
            state["snapshot"]["latest_summary"]
            == "The first batch defines Alpha as the core concept."
        )
        assert state["snapshot"]["top_concepts"][0]["term"] == "Alpha"

        second_packet = (out / "batch-packets" / "batch-002.md").read_text(
            encoding="utf-8"
        )
        assert "The first batch defines Alpha as the core concept." in second_packet
        assert "Alpha (x1)" in second_packet
