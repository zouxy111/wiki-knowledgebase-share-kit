#!/usr/bin/env python3
"""Tests for synthesize_knowledge.py script."""

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
from synthesize_knowledge import build_synthesis  # noqa: E402


def make_source(path: Path) -> None:
    path.write_text(
        """# Giant Guide

## Chapter A

### Topic A1

Alpha flow. Alpha flow. Alpha flow.

### Topic A2

Beta flow. Beta flow. Beta flow.

## Chapter B

### Topic B1

Gamma flow. Gamma flow. Gamma flow.
""",
        encoding="utf-8",
    )


def test_build_synthesis_outputs_expected_files():
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp = Path(tmpdir)
        source = tmp / "source.md"
        run_dir = tmp / "run"
        out_dir = run_dir / "synthesis"
        make_source(source)

        prepare_run(
            source=source,
            out_dir=run_dir,
            level=2,
            max_chunk_words=60,
            max_batch_words=40,
            max_chunks_per_batch=2,
            prefix="guide-",
        )

        note1 = {
            "batch_id": "batch-001",
            "status": "completed",
            "summary": "Chapter A introduces Alpha and Beta.",
            "key_claims": ["Alpha and Beta are paired concepts."],
            "concepts": ["Alpha", "Beta"],
            "procedures": ["Review Topic A1 before Topic A2"],
            "entities": ["Giant Guide"],
            "open_questions": ["How is Gamma related?"],
            "cross_refs": ["guide-topic-b1.md"],
            "candidate_topics": ["Alpha", "Beta"],
        }
        note2 = {
            "batch_id": "batch-002",
            "status": "completed",
            "summary": "Chapter B introduces Gamma as a follow-up topic.",
            "key_claims": ["Gamma extends the earlier flow."],
            "concepts": ["Gamma", "Alpha"],
            "procedures": ["Compare Gamma with Alpha"],
            "entities": ["Giant Guide"],
            "open_questions": [],
            "cross_refs": ["guide-topic-a1.md"],
            "candidate_topics": ["Gamma", "Alpha"],
        }
        (run_dir / "batch-notes" / "batch-001.json").write_text(
            json.dumps(note1, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        (run_dir / "batch-notes" / "batch-002.json").write_text(
            json.dumps(note2, ensure_ascii=False, indent=2), encoding="utf-8"
        )

        report = build_synthesis(run_dir, out_dir)

        assert report["completed_notes"] == 2
        assert (out_dir / "source-overview.md").exists()
        assert (out_dir / "chapter-summaries.md").exists()
        assert (out_dir / "topic-candidates.md").exists()
        assert (out_dir / "glossary-seeds.md").exists()
        assert (out_dir / "unresolved-questions.md").exists()
        assert (out_dir / "synthesis-report.json").exists()

        overview = (out_dir / "source-overview.md").read_text(encoding="utf-8")
        topics = (out_dir / "topic-candidates.md").read_text(encoding="utf-8")
        assert "Giant Guide" in overview
        assert "Alpha" in topics
