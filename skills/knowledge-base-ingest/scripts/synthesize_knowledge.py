#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

from split_markdown import slugify

NOTE_LIST_FIELDS = [
    "key_claims",
    "concepts",
    "procedures",
    "entities",
    "open_questions",
    "cross_refs",
    "candidate_topics",
]


def now_iso() -> str:
    return datetime.now().replace(microsecond=0).isoformat()


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def normalize_list(value) -> list[str]:
    if isinstance(value, str):
        value = [value]
    if not isinstance(value, list):
        return []
    normalized = []
    for item in value:
        if not isinstance(item, str):
            continue
        text = " ".join(item.split()).strip()
        if text:
            normalized.append(text)
    return normalized


def load_completed_notes(run_dir: Path, batch_rows: list[dict]) -> dict[str, dict]:
    notes = {}
    for row in batch_rows:
        note_file = row.get("note_file", f"batch-notes/{row['batch_id']}.json")
        note_path = run_dir / note_file
        if not note_path.exists():
            continue
        payload = read_json(note_path)
        summary = " ".join(str(payload.get("summary", "")).split()).strip()
        lists = {
            field: normalize_list(payload.get(field, [])) for field in NOTE_LIST_FIELDS
        }
        meaningful = summary or any(lists[field] for field in NOTE_LIST_FIELDS)
        if not meaningful:
            continue
        notes[row["batch_id"]] = {
            "summary": summary,
            **lists,
        }
    return notes


def build_synthesis(run_dir: Path, out_dir: Path) -> dict:
    plan = read_json(run_dir / "batch-plan.json")
    batches = plan["batches"]
    notes = load_completed_notes(run_dir, batches)

    concept_counter: Counter[str] = Counter()
    entity_counter: Counter[str] = Counter()
    topic_counter: Counter[str] = Counter()
    question_counter: Counter[str] = Counter()
    claim_counter: Counter[str] = Counter()
    procedure_counter: Counter[str] = Counter()
    chapter_rows: dict[str, dict] = defaultdict(
        lambda: {
            "batches": [],
            "summaries": [],
            "claims": [],
            "procedures": [],
            "topics": [],
        }
    )

    for row in batches:
        chapter = row["chapter_key"]
        chapter_rows[chapter]["batches"].append(row["batch_id"])
        note = notes.get(row["batch_id"])
        if not note:
            continue
        if note["summary"]:
            chapter_rows[chapter]["summaries"].append(note["summary"])
        chapter_rows[chapter]["claims"].extend(note["key_claims"])
        chapter_rows[chapter]["procedures"].extend(note["procedures"])
        chapter_rows[chapter]["topics"].extend(note["candidate_topics"])
        concept_counter.update(note["concepts"])
        entity_counter.update(note["entities"])
        topic_counter.update(note["candidate_topics"])
        question_counter.update(note["open_questions"])
        claim_counter.update(note["key_claims"])
        procedure_counter.update(note["procedures"])

    source_title = plan["source_title"]

    overview_lines = [
        f"# Source Overview — {source_title}",
        "",
        f"- Generated at: {now_iso()}",
        f"- Source path: `{plan['source']}`",
        f"- Effective split level: H{plan['effective_split_level']}",
        f"- Total batches: {len(batches)}",
        f"- Completed notes: {len(notes)}",
        "",
        "## What this synthesis gives you",
        "",
        "- a source overview baseline",
        "- chapter-level summaries from completed close-reading batches",
        "- topic/glossary seeds worth promoting into stable pages",
        "- unresolved questions to revisit before final import",
        "",
        "## Strongest repeated concepts",
        "",
    ]
    for term, count in concept_counter.most_common(12):
        overview_lines.append(f"- **{term}** (x{count})")
    if not concept_counter:
        overview_lines.append("- none yet")

    overview_lines.extend(["", "## Candidate page map", ""])
    overview_lines.append(
        f"- `overview-{slugify(source_title)}.md` — source overview / ingest rules / lineage"
    )
    for chapter in chapter_rows:
        overview_lines.append(
            f"- `knowledge-{slugify(chapter)}.md` — chapter summary / links / extracted knowledge"
        )
    for term, _ in topic_counter.most_common(10):
        overview_lines.append(
            f"- `knowledge-{slugify(term)}.md` — candidate topic page"
        )
    write_text(out_dir / "source-overview.md", "\n".join(overview_lines) + "\n")

    chapter_lines = ["# Chapter Summaries", ""]
    for chapter, payload in chapter_rows.items():
        chapter_lines.extend([f"## {chapter}", ""])
        chapter_lines.append(f"- Batches: {', '.join(payload['batches'])}")
        if payload["summaries"]:
            chapter_lines.append("- Summaries:")
            for summary in payload["summaries"]:
                chapter_lines.append(f"  - {summary}")
        else:
            chapter_lines.append("- Summaries: pending")
        if payload["claims"]:
            chapter_lines.append("- Repeated claims:")
            for claim in payload["claims"][:8]:
                chapter_lines.append(f"  - {claim}")
        if payload["procedures"]:
            chapter_lines.append("- Procedures:")
            for item in payload["procedures"][:8]:
                chapter_lines.append(f"  - {item}")
        chapter_lines.append("")
    write_text(out_dir / "chapter-summaries.md", "\n".join(chapter_lines) + "\n")

    topic_lines = ["# Topic Candidates", ""]
    for term, count in topic_counter.most_common(20):
        topic_lines.append(f"- **{term}** (x{count})")
    if not topic_counter:
        topic_lines.append("- none yet")
    write_text(out_dir / "topic-candidates.md", "\n".join(topic_lines) + "\n")

    glossary_lines = ["# Glossary Seeds", ""]
    for term, count in concept_counter.most_common(25):
        glossary_lines.append(f"- **{term}** (x{count})")
    if not concept_counter:
        glossary_lines.append("- none yet")
    write_text(out_dir / "glossary-seeds.md", "\n".join(glossary_lines) + "\n")

    question_lines = ["# Unresolved Questions", ""]
    for question, count in question_counter.most_common(20):
        question_lines.append(f"- {question} (x{count})")
    if not question_counter:
        question_lines.append("- none yet")
    write_text(out_dir / "unresolved-questions.md", "\n".join(question_lines) + "\n")

    report = {
        "generated_at": now_iso(),
        "source_title": source_title,
        "batch_count": len(batches),
        "completed_notes": len(notes),
        "chapters": len(chapter_rows),
        "top_concepts": [
            {"term": term, "count": count}
            for term, count in concept_counter.most_common(20)
        ],
        "top_entities": [
            {"term": term, "count": count}
            for term, count in entity_counter.most_common(20)
        ],
        "candidate_topics": [
            {"term": term, "count": count}
            for term, count in topic_counter.most_common(20)
        ],
        "open_questions": [
            {"question": question, "count": count}
            for question, count in question_counter.most_common(20)
        ],
        "repeated_claims": [
            {"claim": claim, "count": count}
            for claim, count in claim_counter.most_common(20)
        ],
        "procedures": [
            {"procedure": item, "count": count}
            for item, count in procedure_counter.most_common(20)
        ],
    }
    write_text(
        out_dir / "synthesis-report.json",
        json.dumps(report, ensure_ascii=False, indent=2) + "\n",
    )
    return report


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Synthesize completed close-reading batch notes into knowledge-base candidates."
    )
    parser.add_argument("run_dir", help="Directory produced by close_read_markdown.py")
    parser.add_argument(
        "--out",
        help="Output directory for synthesis artifacts (default: <run_dir>/synthesis)",
    )
    args = parser.parse_args()

    run_dir = Path(args.run_dir)
    out_dir = Path(args.out) if args.out else run_dir / "synthesis"
    report = build_synthesis(run_dir, out_dir)
    print(json.dumps(report, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
