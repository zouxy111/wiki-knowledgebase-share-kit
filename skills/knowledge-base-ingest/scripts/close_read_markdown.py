#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from collections import Counter
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Iterable

from split_markdown import (
    choose_level,
    find_headings,
    split_range,
    write_chunks,
    write_toc,
)

NOTE_LIST_FIELDS = [
    "key_claims",
    "concepts",
    "procedures",
    "entities",
    "open_questions",
    "cross_refs",
    "candidate_topics",
]


@dataclass
class Batch:
    batch_id: str
    chapter_key: str
    chunk_files: list[str]
    chunk_titles: list[str]
    total_words: int


@dataclass
class CompletedNote:
    batch_id: str
    summary: str
    key_claims: list[str]
    concepts: list[str]
    procedures: list[str]
    entities: list[str]
    open_questions: list[str]
    cross_refs: list[str]
    candidate_topics: list[str]
    status: str
    note_path: str


def now_iso() -> str:
    return datetime.now().replace(microsecond=0).isoformat()


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


def normalize_list(value) -> list[str]:
    if value is None:
        return []
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


def make_source_title(lines: list[str], source: Path) -> str:
    headings = find_headings(lines)
    if headings:
        return headings[0].title
    return source.stem


def prepare_chunks(
    source: Path,
    chunks_dir: Path,
    level: int,
    max_chunk_words: int,
    prefix: str,
    force_resplit: bool,
) -> tuple[list[dict], int, str]:
    manifest_path = chunks_dir / "manifest.json"
    meta_path = chunks_dir / "source-metadata.json"
    if manifest_path.exists() and meta_path.exists() and not force_resplit:
        manifest = read_json(manifest_path)
        meta = read_json(meta_path)
        return manifest, int(meta["effective_level"]), str(meta["source_title"])

    chunks_dir.mkdir(parents=True, exist_ok=True)
    lines = source.read_text(encoding="utf-8").splitlines(keepends=True)
    headings = find_headings(lines)
    if not headings:
        raise SystemExit("No markdown headings found; add headings or split manually.")

    effective_level = choose_level(headings, level)
    chunks = split_range(
        lines, headings, effective_level, 0, len(lines), max_chunk_words
    )

    preamble_start = headings[0].line_index
    preamble_path = chunks_dir / "000-preamble.md"
    if preamble_start > 0:
        preamble = lines[:preamble_start]
        if "".join(preamble).strip():
            preamble_path.write_text("".join(preamble), encoding="utf-8")
    elif preamble_path.exists():
        preamble_path.unlink()

    manifest = write_chunks(chunks, chunks_dir, prefix)
    write_json(manifest_path, manifest)
    write_toc(manifest, chunks_dir)
    source_title = make_source_title(lines, source)
    write_json(
        meta_path,
        {
            "source": str(source),
            "source_title": source_title,
            "effective_level": effective_level,
            "generated_at": now_iso(),
            "chunk_count": len(manifest),
        },
    )
    return manifest, effective_level, source_title


def chapter_key(item: dict) -> str:
    breadcrumb = item.get("breadcrumb") or [item.get("title", "Untitled")]
    if len(breadcrumb) >= 2:
        return " / ".join(breadcrumb[:2])
    return breadcrumb[0]


def plan_batches(
    manifest: list[dict],
    max_batch_words: int,
    max_chunks_per_batch: int,
) -> list[Batch]:
    batches: list[Batch] = []
    current_items: list[dict] = []
    current_words = 0
    current_chapter: str | None = None

    def flush() -> None:
        nonlocal current_items, current_words, current_chapter
        if not current_items:
            return
        batch_id = f"batch-{len(batches) + 1:03d}"
        batches.append(
            Batch(
                batch_id=batch_id,
                chapter_key=current_chapter or "Ungrouped",
                chunk_files=[item["file"] for item in current_items],
                chunk_titles=[item["title"] for item in current_items],
                total_words=sum(
                    int(item.get("word_count", 0)) for item in current_items
                ),
            )
        )
        current_items = []
        current_words = 0
        current_chapter = None

    for item in manifest:
        item_words = int(item.get("word_count", 0))
        item_chapter = chapter_key(item)
        exceeds_word_budget = (
            current_items and current_words + item_words > max_batch_words
        )
        exceeds_chunk_budget = (
            current_items and len(current_items) >= max_chunks_per_batch
        )
        chapter_switched = current_items and item_chapter != current_chapter
        if exceeds_word_budget or exceeds_chunk_budget or chapter_switched:
            flush()
        current_items.append(item)
        current_words += item_words
        current_chapter = item_chapter
    flush()
    return batches


def note_template(batch: Batch) -> dict:
    return {
        "batch_id": batch.batch_id,
        "status": "pending",
        "summary": "",
        "key_claims": [],
        "concepts": [],
        "procedures": [],
        "entities": [],
        "open_questions": [],
        "cross_refs": [],
        "candidate_topics": [],
    }


def load_completed_note(path: Path) -> CompletedNote | None:
    if not path.exists():
        return None
    payload = read_json(path)
    summary = " ".join(str(payload.get("summary", "")).split()).strip()
    status = str(payload.get("status", "pending")).strip().lower() or "pending"
    lists = {
        field: normalize_list(payload.get(field, [])) for field in NOTE_LIST_FIELDS
    }
    meaningful = summary or any(lists[field] for field in NOTE_LIST_FIELDS)
    if not meaningful and status != "completed":
        return None
    return CompletedNote(
        batch_id=str(payload.get("batch_id", path.stem)),
        summary=summary,
        key_claims=lists["key_claims"],
        concepts=lists["concepts"],
        procedures=lists["procedures"],
        entities=lists["entities"],
        open_questions=lists["open_questions"],
        cross_refs=lists["cross_refs"],
        candidate_topics=lists["candidate_topics"],
        status=status,
        note_path=str(path),
    )


def build_rolling_snapshot(completed_notes: Iterable[CompletedNote]) -> dict:
    if not isinstance(completed_notes, list):
        completed_notes = list(completed_notes)
    summaries: list[str] = []
    concept_counter: Counter[str] = Counter()
    entity_counter: Counter[str] = Counter()
    topic_counter: Counter[str] = Counter()
    open_questions: list[str] = []
    claim_counter: Counter[str] = Counter()

    for note in completed_notes:
        if note.summary:
            summaries.append(note.summary)
        concept_counter.update(note.concepts)
        entity_counter.update(note.entities)
        topic_counter.update(note.candidate_topics)
        claim_counter.update(note.key_claims)
        for question in note.open_questions:
            if question not in open_questions:
                open_questions.append(question)

    return {
        "completed_batches": len(completed_notes),
        "recent_summaries": summaries[-3:],
        "top_concepts": [
            {"term": term, "count": count}
            for term, count in concept_counter.most_common(12)
        ],
        "top_entities": [
            {"term": term, "count": count}
            for term, count in entity_counter.most_common(12)
        ],
        "candidate_topics": [
            {"term": term, "count": count}
            for term, count in topic_counter.most_common(12)
        ],
        "repeated_claims": [
            {"claim": claim, "count": count}
            for claim, count in claim_counter.most_common(8)
        ],
        "open_questions": open_questions[:12],
        "latest_summary": summaries[-1] if summaries else "",
    }


def render_snapshot_section(snapshot: dict) -> str:
    def render_counter(title: str, items: list[dict], key: str = "term") -> list[str]:
        if not items:
            return [f"- {title}: none yet"]
        lines = [f"- {title}:"]
        for item in items[:6]:
            lines.append(f"  - {item[key]} (x{item['count']})")
        return lines

    lines = ["## Rolling context from completed batches", ""]
    lines.append(f"- Completed batches so far: {snapshot['completed_batches']}")
    if snapshot["recent_summaries"]:
        lines.append("- Recent summaries:")
        for summary in snapshot["recent_summaries"]:
            lines.append(f"  - {summary}")
    else:
        lines.append("- Recent summaries: none yet")
    lines.extend(render_counter("Top concepts", snapshot["top_concepts"]))
    lines.extend(render_counter("Top entities", snapshot["top_entities"]))
    lines.extend(render_counter("Candidate topics", snapshot["candidate_topics"]))
    if snapshot["open_questions"]:
        lines.append("- Open questions:")
        for question in snapshot["open_questions"][:6]:
            lines.append(f"  - {question}")
    else:
        lines.append("- Open questions: none yet")
    return "\n".join(lines)


def render_packet(
    batch: Batch,
    source_title: str,
    batch_index: int,
    total_batches: int,
    chunk_dir: Path,
    note_path: Path,
    snapshot: dict,
) -> str:
    lines = [
        f"# Close Reading Packet — {batch.batch_id}",
        "",
        "## Batch identity",
        "",
        f"- Source: {source_title}",
        f"- Batch: {batch_index}/{total_batches}",
        f"- Chapter key: {batch.chapter_key}",
        f"- Chunk files: {', '.join(batch.chunk_files)}",
        f"- Total words in this batch: {batch.total_words}",
        "",
        render_snapshot_section(snapshot),
        "",
        "## What to extract",
        "",
        "Write one JSON note for this batch. Keep the output faithful to the source and optimized for later synthesis.",
        "",
        f"- Save JSON to: `{note_path}`",
        "- Keep `summary` to 2-5 sentences.",
        "- Use short bullet-like strings for arrays.",
        "- Add only stable, reusable claims and concepts; skip filler prose.",
        "- Use `cross_refs` for chunk files or batch ids that should be revisited together.",
        "- Leave `status` as `completed` once the note is usable.",
        "",
        "## Required JSON shape",
        "",
        "```json",
        json.dumps(note_template(batch), ensure_ascii=False, indent=2),
        "```",
        "",
        "## Source chunks",
        "",
    ]
    for chunk_file, chunk_title in zip(batch.chunk_files, batch.chunk_titles):
        chunk_text = (chunk_dir / chunk_file).read_text(encoding="utf-8")
        lines.extend(
            [
                f"### {chunk_title} ({chunk_file})",
                "",
                "```markdown",
                chunk_text.rstrip(),
                "```",
                "",
            ]
        )
    return "\n".join(lines).rstrip() + "\n"


def prepare_run(
    source: Path,
    out_dir: Path,
    level: int,
    max_chunk_words: int,
    max_batch_words: int,
    max_chunks_per_batch: int,
    prefix: str,
    force_resplit: bool = False,
) -> dict:
    out_dir.mkdir(parents=True, exist_ok=True)
    chunks_dir = out_dir / "chunks"
    batch_packets_dir = out_dir / "batch-packets"
    batch_notes_dir = out_dir / "batch-notes"
    batch_packets_dir.mkdir(exist_ok=True)
    batch_notes_dir.mkdir(exist_ok=True)

    manifest, effective_level, source_title = prepare_chunks(
        source, chunks_dir, level, max_chunk_words, prefix, force_resplit
    )
    batches = plan_batches(manifest, max_batch_words, max_chunks_per_batch)
    write_json(
        out_dir / "batch-plan.json",
        {
            "source": str(source),
            "source_title": source_title,
            "generated_at": now_iso(),
            "effective_split_level": effective_level,
            "max_chunk_words": max_chunk_words,
            "max_batch_words": max_batch_words,
            "max_chunks_per_batch": max_chunks_per_batch,
            "batches": [batch.__dict__ for batch in batches],
        },
    )

    notes_by_batch: dict[str, CompletedNote] = {}
    for batch in batches:
        note_path = batch_notes_dir / f"{batch.batch_id}.json"
        if not note_path.exists():
            write_json(note_path, note_template(batch))
        note = load_completed_note(note_path)
        if note is not None:
            notes_by_batch[batch.batch_id] = note

    completed_before_current: list[CompletedNote] = []
    batch_rows = []
    for idx, batch in enumerate(batches, start=1):
        note_path = batch_notes_dir / f"{batch.batch_id}.json"
        snapshot = build_rolling_snapshot(completed_before_current)
        packet_text = render_packet(
            batch,
            source_title,
            idx,
            len(batches),
            chunks_dir,
            note_path,
            snapshot,
        )
        packet_path = batch_packets_dir / f"{batch.batch_id}.md"
        packet_path.write_text(packet_text, encoding="utf-8")

        status = "completed" if batch.batch_id in notes_by_batch else "pending"
        batch_rows.append(
            {
                "batch_id": batch.batch_id,
                "status": status,
                "chapter_key": batch.chapter_key,
                "chunk_files": batch.chunk_files,
                "chunk_titles": batch.chunk_titles,
                "total_words": batch.total_words,
                "note_file": str(note_path.relative_to(out_dir)),
                "packet_file": str(packet_path.relative_to(out_dir)),
            }
        )
        if batch.batch_id in notes_by_batch:
            completed_before_current.append(notes_by_batch[batch.batch_id])

    completed_notes = [
        notes_by_batch[row["batch_id"]]
        for row in batch_rows
        if row["batch_id"] in notes_by_batch
    ]
    snapshot = build_rolling_snapshot(completed_notes)
    completed_chunks = sum(
        len(row["chunk_files"]) for row in batch_rows if row["status"] == "completed"
    )
    reading_state = {
        "source": str(source),
        "source_title": source_title,
        "generated_at": now_iso(),
        "effective_split_level": effective_level,
        "batch_count": len(batch_rows),
        "completed_batches": len(completed_notes),
        "pending_batches": len(batch_rows) - len(completed_notes),
        "completed_chunks": completed_chunks,
        "snapshot": snapshot,
        "batches": batch_rows,
    }
    write_json(out_dir / "reading-state.json", reading_state)

    index_lines = [
        "# Close Reading Run",
        "",
        f"- Source: `{source}`",
        f"- Source title: {source_title}",
        f"- Effective split level: H{effective_level}",
        f"- Batches: {len(batch_rows)}",
        f"- Completed batches: {len(completed_notes)}",
        "",
        "## Batch queue",
        "",
    ]
    for row in batch_rows:
        index_lines.append(
            f"- **{row['batch_id']}** [{row['status']}] — {row['chapter_key']} "
            f"({len(row['chunk_files'])} chunks, {row['total_words']} words)"
        )
    (out_dir / "README.md").write_text("\n".join(index_lines) + "\n", encoding="utf-8")
    return reading_state


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Prepare a chunked close-reading harness for oversized markdown sources."
    )
    parser.add_argument("source", help="Path to the source markdown file")
    parser.add_argument(
        "--out", required=True, help="Output directory for the close-reading run"
    )
    parser.add_argument(
        "--level",
        type=int,
        default=2,
        help="Preferred heading level for chunking (default: 2)",
    )
    parser.add_argument(
        "--max-chunk-words",
        type=int,
        default=1800,
        help="Maximum words per chunk before recursive re-splitting (default: 1800)",
    )
    parser.add_argument(
        "--max-batch-words",
        type=int,
        default=4800,
        help="Maximum total words per close-reading batch (default: 4800)",
    )
    parser.add_argument(
        "--max-chunks-per-batch",
        type=int,
        default=4,
        help="Maximum chunks included in one batch packet (default: 4)",
    )
    parser.add_argument(
        "--prefix", default="", help="Optional filename prefix for chunk files"
    )
    parser.add_argument(
        "--force-resplit",
        action="store_true",
        help="Rebuild chunks even if an existing manifest already exists",
    )
    args = parser.parse_args()

    state = prepare_run(
        source=Path(args.source),
        out_dir=Path(args.out),
        level=args.level,
        max_chunk_words=args.max_chunk_words,
        max_batch_words=args.max_batch_words,
        max_chunks_per_batch=args.max_chunks_per_batch,
        prefix=args.prefix,
        force_resplit=args.force_resplit,
    )
    print(json.dumps(state, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
