#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import sys
from collections import Counter
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Iterable

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from split_markdown import (
    choose_level,
    find_headings,
    slugify,
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
    batch_key: str
    batch_hash: str
    chapter_key: str
    chunk_files: list[str]
    chunk_titles: list[str]
    total_words: int


@dataclass
class CompletedNote:
    batch_id: str
    batch_key: str
    batch_hash: str
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


class ChunkPreparationError(ValueError):
    pass


def now_iso() -> str:
    return datetime.now().replace(microsecond=0).isoformat()


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


def sha1_text(text: str) -> str:
    return hashlib.sha1(text.encode("utf-8")).hexdigest()


def file_sha1(path: Path) -> str:
    return sha1_text(path.read_text(encoding="utf-8"))


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


def enrich_manifest_hashes(manifest: list[dict], chunks_dir: Path) -> list[dict]:
    enriched = []
    for item in manifest:
        new_item = dict(item)
        chunk_path = chunks_dir / new_item["file"]
        if chunk_path.exists():
            new_item["content_hash"] = file_sha1(chunk_path)
        enriched.append(new_item)
    return enriched


def reset_generated_chunk_artifacts(chunks_dir: Path) -> None:
    if not chunks_dir.exists():
        return
    for path in chunks_dir.iterdir():
        if path.is_file():
            path.unlink()
        elif path.is_dir():
            shutil.rmtree(path)


def prepare_chunks(
    source: Path,
    chunks_dir: Path,
    level: int,
    max_chunk_words: int,
    max_chunk_lines: int,
    prefix: str,
    force_resplit: bool,
) -> tuple[list[dict], int, str, str]:
    manifest_path = chunks_dir / "manifest.json"
    meta_path = chunks_dir / "source-metadata.json"
    source_text = source.read_text(encoding="utf-8")
    source_hash = sha1_text(source_text)

    if manifest_path.exists() and meta_path.exists() and not force_resplit:
        meta = read_json(meta_path)
        if meta.get("source_hash") == source_hash:
            manifest = enrich_manifest_hashes(read_json(manifest_path), chunks_dir)
            write_json(manifest_path, manifest)
            return (
                manifest,
                int(meta["effective_level"]),
                str(meta["source_title"]),
                source_hash,
            )

    chunks_dir.mkdir(parents=True, exist_ok=True)
    reset_generated_chunk_artifacts(chunks_dir)
    lines = source_text.splitlines(keepends=True)
    headings = find_headings(lines)
    if not headings:
        raise ChunkPreparationError(
            "No markdown headings found; add headings or split manually."
        )

    effective_level = choose_level(headings, level)
    chunks = split_range(
        lines,
        headings,
        effective_level,
        0,
        len(lines),
        max_chunk_words,
        max_chunk_lines,
    )

    preamble_start = headings[0].line_index
    preamble_path = chunks_dir / "000-preamble.md"
    if preamble_start > 0:
        preamble = lines[:preamble_start]
        if "".join(preamble).strip():
            preamble_path.write_text("".join(preamble), encoding="utf-8")

    manifest = write_chunks(chunks, chunks_dir, prefix)
    manifest = enrich_manifest_hashes(manifest, chunks_dir)
    write_json(manifest_path, manifest)
    write_toc(manifest, chunks_dir)
    source_title = make_source_title(lines, source)
    write_json(
        meta_path,
        {
            "source": str(source),
            "source_title": source_title,
            "source_hash": source_hash,
            "effective_level": effective_level,
            "generated_at": now_iso(),
            "chunk_count": len(manifest),
        },
    )
    return manifest, effective_level, source_title, source_hash


def chapter_key(item: dict) -> str:
    breadcrumb = item.get("breadcrumb") or [item.get("title", "Untitled")]
    if len(breadcrumb) >= 2:
        return " / ".join(breadcrumb[:2])
    return breadcrumb[0]


def make_batch_hash(items: list[dict]) -> str:
    payload = [
        {
            "file": item["file"],
            "title": item.get("title"),
            "hash": item.get("content_hash", ""),
            "words": int(item.get("word_count", 0)),
        }
        for item in items
    ]
    return sha1_text(json.dumps(payload, ensure_ascii=False, sort_keys=True))


def plan_batches(
    manifest: list[dict],
    max_batch_words: int,
    max_chunks_per_batch: int,
) -> list[Batch]:
    batches: list[Batch] = []
    current_items: list[dict] = []
    current_words = 0
    current_chapter: str | None = None
    chapter_counts: Counter[str] = Counter()

    def flush() -> None:
        nonlocal current_items, current_words, current_chapter
        if not current_items:
            return
        chapter_slug = slugify(current_chapter or "ungrouped")
        chapter_counts[chapter_slug] += 1
        batch_index = chapter_counts[chapter_slug]
        batch_key = f"{chapter_slug}-b{batch_index:02d}"
        batch_hash = make_batch_hash(current_items)
        batches.append(
            Batch(
                batch_id=f"batch-{len(batches) + 1:03d}",
                batch_key=batch_key,
                batch_hash=batch_hash,
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
        "batch_key": batch.batch_key,
        "batch_hash": batch.batch_hash,
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


def has_meaningful_note(payload: dict) -> bool:
    summary = " ".join(str(payload.get("summary", "")).split()).strip()
    if summary:
        return True
    for field in NOTE_LIST_FIELDS:
        if normalize_list(payload.get(field, [])):
            return True
    return False


def parse_completed_note(path: Path, payload: dict) -> CompletedNote | None:
    status = str(payload.get("status", "pending")).strip().lower() or "pending"
    if status != "completed" and not has_meaningful_note(payload):
        return None
    summary = " ".join(str(payload.get("summary", "")).split()).strip()
    lists = {
        field: normalize_list(payload.get(field, [])) for field in NOTE_LIST_FIELDS
    }
    if not summary and not any(lists[field] for field in NOTE_LIST_FIELDS):
        return None
    return CompletedNote(
        batch_id=str(payload.get("batch_id", path.stem)),
        batch_key=str(payload.get("batch_key", path.stem)),
        batch_hash=str(payload.get("batch_hash", "")),
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


def archive_note(path: Path, stale_dir: Path, suffix: str) -> Path:
    stale_dir.mkdir(parents=True, exist_ok=True)
    archived = stale_dir / f"{path.stem}--{suffix}{path.suffix}"
    counter = 2
    while archived.exists():
        archived = stale_dir / f"{path.stem}--{suffix}-{counter}{path.suffix}"
        counter += 1
    shutil.move(str(path), str(archived))
    return archived


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
    note_link = f"../{note_path.parent.name}/{note_path.name}"
    chunk_links = [
        f"[{chunk_file}](../{chunk_dir.name}/{chunk_file})"
        for chunk_file in batch.chunk_files
    ]
    lines = [
        f"# Close Reading Packet — {batch.batch_id}",
        "",
        "## Batch identity",
        "",
        f"- Source: {source_title}",
        f"- Batch: {batch_index}/{total_batches}",
        f"- Batch key: `{batch.batch_key}`",
        f"- Batch hash: `{batch.batch_hash}`",
        f"- Chapter key: {batch.chapter_key}",
        f"- Chunk files: {', '.join(chunk_links)}",
        f"- Total words in this batch: {batch.total_words}",
        "",
        render_snapshot_section(snapshot),
        "",
        "## What to extract",
        "",
        "Write one JSON note for this batch. Keep the output faithful to the source and optimized for later synthesis.",
        "",
        f"- Save JSON to: [{note_path.name}]({note_link})",
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
                f"### {chunk_title} ([{chunk_file}](../{chunk_dir.name}/{chunk_file}))",
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
    max_chunk_lines: int = 400,
    force_resplit: bool = False,
) -> dict:
    out_dir.mkdir(parents=True, exist_ok=True)
    chunks_dir = out_dir / "chunks"
    batch_packets_dir = out_dir / "batch-packets"
    batch_notes_dir = out_dir / "batch-notes"
    stale_notes_dir = out_dir / "stale-notes"
    batch_packets_dir.mkdir(exist_ok=True)
    batch_notes_dir.mkdir(exist_ok=True)
    stale_notes_dir.mkdir(exist_ok=True)

    manifest, effective_level, source_title, source_hash = prepare_chunks(
        source,
        chunks_dir,
        level,
        max_chunk_words,
        max_chunk_lines,
        prefix,
        force_resplit,
    )
    batches = plan_batches(manifest, max_batch_words, max_chunks_per_batch)

    active_batch_keys = {batch.batch_key for batch in batches}
    removed_batches = []
    for existing_note in sorted(batch_notes_dir.glob("*.json")):
        if existing_note.stem not in active_batch_keys:
            archive_note(
                existing_note, stale_notes_dir, f"removed-{now_iso().replace(':', '-')}"
            )
            removed_batches.append(existing_note.stem)
    for existing_packet in sorted(batch_packets_dir.glob("*.md")):
        if existing_packet.stem not in active_batch_keys:
            existing_packet.unlink()

    notes_by_batch: dict[str, CompletedNote] = {}
    changed_batches = 0
    new_batches = 0
    batch_rows = []

    for batch in batches:
        note_path = batch_notes_dir / f"{batch.batch_key}.json"
        change_status = "unchanged"
        if note_path.exists():
            payload = read_json(note_path)
            if str(payload.get("batch_hash", "")) != batch.batch_hash:
                if has_meaningful_note(payload):
                    archive_note(note_path, stale_notes_dir, batch.batch_hash[:10])
                write_json(note_path, note_template(batch))
                change_status = "changed"
                changed_batches += 1
            else:
                note = parse_completed_note(note_path, payload)
                if note is not None and note.status == "completed":
                    notes_by_batch[batch.batch_key] = note
        else:
            write_json(note_path, note_template(batch))
            change_status = "new"
            new_batches += 1

        packet_path = batch_packets_dir / f"{batch.batch_key}.md"
        batch_rows.append(
            {
                "batch_id": batch.batch_id,
                "batch_key": batch.batch_key,
                "batch_hash": batch.batch_hash,
                "change_status": change_status,
                "chapter_key": batch.chapter_key,
                "chunk_files": batch.chunk_files,
                "chunk_titles": batch.chunk_titles,
                "total_words": batch.total_words,
                "note_file": str(note_path.relative_to(out_dir)),
                "packet_file": str(packet_path.relative_to(out_dir)),
            }
        )

    completed_before_current: list[CompletedNote] = []
    for idx, row in enumerate(batch_rows, start=1):
        batch = next(item for item in batches if item.batch_key == row["batch_key"])
        note_path = out_dir / row["note_file"]
        snapshot = build_rolling_snapshot(completed_before_current)
        packet_text = render_packet(
            batch, source_title, idx, len(batch_rows), chunks_dir, note_path, snapshot
        )
        (out_dir / row["packet_file"]).write_text(packet_text, encoding="utf-8")
        if row["batch_key"] in notes_by_batch:
            row["status"] = "completed"
            completed_before_current.append(notes_by_batch[row["batch_key"]])
        else:
            row["status"] = "pending"

    completed_notes = [
        notes_by_batch[row["batch_key"]]
        for row in batch_rows
        if row["batch_key"] in notes_by_batch
    ]
    snapshot = build_rolling_snapshot(completed_notes)
    completed_chunks = sum(
        len(row["chunk_files"]) for row in batch_rows if row["status"] == "completed"
    )

    batch_plan = {
        "source": str(source),
        "source_title": source_title,
        "source_hash": source_hash,
        "generated_at": now_iso(),
        "effective_split_level": effective_level,
        "max_chunk_words": max_chunk_words,
        "max_chunk_lines": max_chunk_lines,
        "max_batch_words": max_batch_words,
        "max_chunks_per_batch": max_chunks_per_batch,
        "batches": batch_rows,
    }
    write_json(out_dir / "batch-plan.json", batch_plan)

    reading_state = {
        "source": str(source),
        "source_title": source_title,
        "source_hash": source_hash,
        "generated_at": now_iso(),
        "effective_split_level": effective_level,
        "batch_count": len(batch_rows),
        "completed_batches": len(completed_notes),
        "pending_batches": len(batch_rows) - len(completed_notes),
        "completed_chunks": completed_chunks,
        "changed_batches": changed_batches,
        "new_batches": new_batches,
        "removed_batches": removed_batches,
        "snapshot": snapshot,
        "batches": batch_rows,
    }
    write_json(out_dir / "reading-state.json", reading_state)

    index_lines = [
        "# Close Reading Run",
        "",
        f"- Source: `{source}`",
        f"- Source title: {source_title}",
        f"- Source hash: `{source_hash}`",
        f"- Effective split level: H{effective_level}",
        f"- Batches: {len(batch_rows)}",
        f"- Completed batches: {len(completed_notes)}",
        f"- Changed batches: {changed_batches}",
        f"- New batches: {new_batches}",
        f"- Removed batches archived: {len(removed_batches)}",
        "",
        "## Batch queue",
        "",
        "| Batch | Status | Change | Packet | Note |",
        "|---|---|---|---|---|",
    ]
    for row in batch_rows:
        packet_link = f"[{Path(row['packet_file']).name}]({row['packet_file']})"
        note_link = f"[{Path(row['note_file']).name}]({row['note_file']})"
        index_lines.append(
            f"| `{row['batch_key']}` | {row['status']} | {row['change_status']} | {packet_link} | {note_link} |"
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
        "--max-chunk-lines",
        type=int,
        default=400,
        help="Hard line cap per chunk before fixed-window fallback (default: 400)",
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

    try:
        state = prepare_run(
            source=Path(args.source),
            out_dir=Path(args.out),
            level=args.level,
            max_chunk_words=args.max_chunk_words,
            max_chunk_lines=args.max_chunk_lines,
            max_batch_words=args.max_batch_words,
            max_chunks_per_batch=args.max_chunks_per_batch,
            prefix=args.prefix,
            force_resplit=args.force_resplit,
        )
    except ChunkPreparationError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    print(json.dumps(state, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
