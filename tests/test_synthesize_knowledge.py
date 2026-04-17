#!/usr/bin/env python3
"""Tests for synthesize_knowledge.py script."""

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


def test_build_synthesis_outputs_candidate_pages_and_link_map():
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
            "batch_key": "giant-guide-chapter-a-b01",
            "batch_hash": json.loads(
                (run_dir / "batch-notes" / "giant-guide-chapter-a-b01.json").read_text(
                    encoding="utf-8"
                )
            )["batch_hash"],
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
            "batch_key": "giant-guide-chapter-b-b01",
            "batch_hash": json.loads(
                (run_dir / "batch-notes" / "giant-guide-chapter-b-b01.json").read_text(
                    encoding="utf-8"
                )
            )["batch_hash"],
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
        (run_dir / "batch-notes" / "giant-guide-chapter-a-b01.json").write_text(
            json.dumps(note1, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        (run_dir / "batch-notes" / "giant-guide-chapter-b-b01.json").write_text(
            json.dumps(note2, ensure_ascii=False, indent=2), encoding="utf-8"
        )

        report = build_synthesis(
            run_dir, out_dir, default_area="learning", owner="Codex", status="draft"
        )

        assert report["completed_notes"] == 2
        assert (out_dir / "source-overview.md").exists()
        assert (out_dir / "chapter-summaries.md").exists()
        assert (out_dir / "topic-candidates.md").exists()
        assert (out_dir / "glossary-seeds.md").exists()
        assert (out_dir / "unresolved-questions.md").exists()
        assert (out_dir / "candidate-link-map.md").exists()
        assert (out_dir / "candidate-link-map.json").exists()
        assert (out_dir / "candidate-pages" / "overview-giant-guide.md").exists()
        assert (
            out_dir / "candidate-pages" / "knowledge-giant-guide-chapter-a.md"
        ).exists()
        assert (out_dir / "candidate-pages" / "knowledge-alpha.md").exists()

        overview = (out_dir / "source-overview.md").read_text(encoding="utf-8")
        overview_page = (
            out_dir / "candidate-pages" / "overview-giant-guide.md"
        ).read_text(encoding="utf-8")
        chapter_page = (
            out_dir / "candidate-pages" / "knowledge-giant-guide-chapter-a.md"
        ).read_text(encoding="utf-8")
        topic_page = (out_dir / "candidate-pages" / "knowledge-alpha.md").read_text(
            encoding="utf-8"
        )
        link_map = json.loads(
            (out_dir / "candidate-link-map.json").read_text(encoding="utf-8")
        )

        assert "candidate-pages/overview-giant-guide.md" in overview
        assert 'type: "overview"' in overview_page
        assert 'area: "learning"' in overview_page
        assert "candidate: true" in overview_page
        assert 'owner: "Codex"' in overview_page
        assert "knowledge-alpha.md" in chapter_page
        assert 'type: "knowledge"' in chapter_page
        assert 'status: "draft"' in chapter_page
        assert "knowledge-giant-guide-chapter-a.md" in topic_page
        assert "overview-giant-guide.md" == link_map["overview_page"]
        assert (
            "knowledge-alpha.md"
            in link_map["pages"]["knowledge-giant-guide-chapter-a.md"]["links"]
        )
        assert report["candidate_metadata"]["default_area"] == "learning"

        # Re-run synthesis with Gamma removed and ensure stale candidate pages are cleaned up.
        note2["status"] = "pending"
        note2["summary"] = ""
        note2["concepts"] = []
        note2["candidate_topics"] = []
        (run_dir / "batch-notes" / "giant-guide-chapter-b-b01.json").write_text(
            json.dumps(note2, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        build_synthesis(run_dir, out_dir, default_area="learning")
        assert not (out_dir / "candidate-pages" / "knowledge-gamma.md").exists()
