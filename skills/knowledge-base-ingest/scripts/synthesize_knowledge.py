#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

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


def yaml_quote(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


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
        note_file = row.get("note_file", f"batch-notes/{row['batch_key']}.json")
        note_path = run_dir / note_file
        if not note_path.exists():
            continue
        payload = read_json(note_path)
        summary = " ".join(str(payload.get("summary", "")).split()).strip()
        status = str(payload.get("status", "pending")).strip().lower() or "pending"
        lists = {
            field: normalize_list(payload.get(field, [])) for field in NOTE_LIST_FIELDS
        }
        meaningful = summary or any(lists[field] for field in NOTE_LIST_FIELDS)
        if not meaningful or status != "completed":
            continue
        notes[row["batch_key"]] = {
            "summary": summary,
            "status": status,
            "batch_id": payload.get("batch_id", row.get("batch_id", row["batch_key"])),
            **lists,
        }
    return notes


def dedupe(items: list[str]) -> list[str]:
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def frontmatter_block(meta: dict) -> str:
    lines = ["---"]
    for key, value in meta.items():
        if value is None:
            continue
        if isinstance(value, bool):
            rendered = "true" if value else "false"
        elif isinstance(value, list):
            rendered = "[" + ", ".join(yaml_quote(str(item)) for item in value) + "]"
        else:
            rendered = yaml_quote(str(value))
        lines.append(f"{key}: {rendered}")
    lines.append("---")
    return "\n".join(lines)


def build_page_frontmatter(
    *,
    title: str,
    page_type: str,
    area: str,
    tags: list[str],
    status: str,
    source_title: str,
    source_path: str,
    source_hash: str,
    generated_at: str,
    run_name: str,
    candidate_kind: str,
    owner: str | None = None,
) -> str:
    return frontmatter_block(
        {
            "title": title,
            "type": page_type,
            "area": area,
            "tags": tags,
            "status": status,
            "owner": owner,
            "candidate": True,
            "candidate_kind": candidate_kind,
            "candidate_run": run_name,
            "source_title": source_title,
            "source_path": source_path,
            "source_hash": source_hash,
            "generated_at": generated_at,
            "updated": generated_at[:10],
        }
    )


def build_synthesis(
    run_dir: Path,
    out_dir: Path,
    *,
    default_area: str = "__SET_ME__",
    owner: str | None = None,
    status: str = "draft",
) -> dict:
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
            "cross_refs": [],
        }
    )
    topic_to_chapters: dict[str, set[str]] = defaultdict(set)

    for row in batches:
        chapter = row["chapter_key"]
        chapter_rows[chapter]["batches"].append(row["batch_id"])
        note = notes.get(row["batch_key"])
        if not note:
            continue
        if note["summary"]:
            chapter_rows[chapter]["summaries"].append(note["summary"])
        chapter_rows[chapter]["claims"].extend(note["key_claims"])
        chapter_rows[chapter]["procedures"].extend(note["procedures"])
        chapter_rows[chapter]["topics"].extend(note["candidate_topics"])
        chapter_rows[chapter]["cross_refs"].extend(note["cross_refs"])
        concept_counter.update(note["concepts"])
        entity_counter.update(note["entities"])
        topic_counter.update(note["candidate_topics"])
        question_counter.update(note["open_questions"])
        claim_counter.update(note["key_claims"])
        procedure_counter.update(note["procedures"])
        for topic in note["candidate_topics"]:
            topic_to_chapters[topic].add(chapter)

    source_title = plan["source_title"]
    source_slug = slugify(source_title)
    generated_at = now_iso()
    candidate_pages_dir = out_dir / "candidate-pages"
    candidate_pages_dir.mkdir(parents=True, exist_ok=True)
    for stale_page in candidate_pages_dir.glob("*.md"):
        stale_page.unlink()

    overview_candidate = candidate_pages_dir / f"overview-{source_slug}.md"
    chapter_candidates = {
        chapter: candidate_pages_dir / f"knowledge-{slugify(chapter)}.md"
        for chapter in chapter_rows
    }
    topic_candidates = {
        topic: candidate_pages_dir / f"knowledge-{slugify(topic)}.md"
        for topic, _ in topic_counter.most_common(20)
    }

    link_map: dict[str, dict] = {}
    area_needs_confirmation = default_area == "__SET_ME__"
    base_tags = dedupe(["candidate", "ingest", source_slug])[:3]

    chapter_list = list(chapter_rows.keys())
    overview_frontmatter = build_page_frontmatter(
        title=source_title,
        page_type="overview",
        area=default_area,
        tags=base_tags + ["overview"],
        status=status,
        source_title=source_title,
        source_path=plan["source"],
        source_hash=plan.get("source_hash", ""),
        generated_at=generated_at,
        run_name=run_dir.name,
        candidate_kind="overview",
        owner=owner,
    )
    overview_candidate_lines = [
        overview_frontmatter,
        "",
        f"# {source_title} — candidate overview page",
        "",
        f"- Generated at: {generated_at}",
        f"- Source path: `{plan['source']}`",
        f"- Effective split level: H{plan['effective_split_level']}",
        f"- Candidate status: `{status}`",
        f"- Candidate area: `{default_area}`",
    ]
    if area_needs_confirmation:
        overview_candidate_lines.extend(
            [
                "",
                "> `area` is still `__SET_ME__`. Confirm the vault area before promoting this page into a real knowledge base.",
            ]
        )
    overview_candidate_lines.extend(
        [
            "",
            "## Chapter links",
            "",
        ]
    )
    for chapter in chapter_list:
        chapter_path = chapter_candidates[chapter]
        overview_candidate_lines.append(f"- [{chapter}]({chapter_path.name})")
    overview_candidate_lines.extend(["", "## Topic links", ""])
    for topic, path in topic_candidates.items():
        overview_candidate_lines.append(f"- [{topic}]({path.name})")
    write_text(overview_candidate, "\n".join(overview_candidate_lines) + "\n")
    link_map[overview_candidate.name] = {
        "type": "overview",
        "links": [chapter_candidates[chapter].name for chapter in chapter_list]
        + [path.name for path in topic_candidates.values()],
    }

    for index, chapter in enumerate(chapter_list):
        chapter_path = chapter_candidates[chapter]
        payload = chapter_rows[chapter]
        topic_names = [
            topic for topic in dedupe(payload["topics"]) if topic in topic_candidates
        ]
        prev_path = (
            chapter_candidates[chapter_list[index - 1]].name if index > 0 else None
        )
        next_path = (
            chapter_candidates[chapter_list[index + 1]].name
            if index + 1 < len(chapter_list)
            else None
        )
        chapter_frontmatter = build_page_frontmatter(
            title=chapter,
            page_type="knowledge",
            area=default_area,
            tags=dedupe(
                base_tags + ["chapter"] + [slugify(topic) for topic in topic_names[:4]]
            ),
            status=status,
            source_title=source_title,
            source_path=plan["source"],
            source_hash=plan.get("source_hash", ""),
            generated_at=generated_at,
            run_name=run_dir.name,
            candidate_kind="chapter",
            owner=owner,
        )
        lines = [
            chapter_frontmatter,
            "",
            f"# {chapter}",
            "",
            f"- Source overview: [{overview_candidate.name}]({overview_candidate.name})",
            f"- Candidate status: `{status}`",
            f"- Candidate area: `{default_area}`",
        ]
        if prev_path:
            lines.append(f"- Previous chapter: [{prev_path}]({prev_path})")
        if next_path:
            lines.append(f"- Next chapter: [{next_path}]({next_path})")
        lines.extend(["", "## Batch summaries", ""])
        if payload["summaries"]:
            for summary in payload["summaries"]:
                lines.append(f"- {summary}")
        else:
            lines.append("- pending")
        lines.extend(["", "## Related topic candidates", ""])
        if topic_names:
            for topic in topic_names:
                lines.append(f"- [{topic}]({topic_candidates[topic].name})")
        else:
            lines.append("- none yet")
        lines.extend(["", "## Cross refs worth revisiting", ""])
        if payload["cross_refs"]:
            for ref in dedupe(payload["cross_refs"])[:10]:
                lines.append(f"- `{ref}`")
        else:
            lines.append("- none yet")
        write_text(chapter_path, "\n".join(lines) + "\n")
        links = [overview_candidate.name]
        if prev_path:
            links.append(prev_path)
        if next_path:
            links.append(next_path)
        links.extend(topic_candidates[topic].name for topic in topic_names)
        link_map[chapter_path.name] = {"type": "chapter", "links": links}

    topic_chapter_lists = {
        topic: sorted(chapters)
        for topic, chapters in topic_to_chapters.items()
        if topic in topic_candidates
    }
    for topic, path in topic_candidates.items():
        chapters = topic_chapter_lists.get(topic, [])
        sibling_topics = []
        for chapter in chapters:
            sibling_topics.extend(
                other
                for other in dedupe(chapter_rows[chapter]["topics"])
                if other != topic and other in topic_candidates
            )
        sibling_topics = dedupe(sibling_topics)[:6]
        topic_frontmatter = build_page_frontmatter(
            title=topic,
            page_type="knowledge",
            area=default_area,
            tags=dedupe(base_tags + ["topic", slugify(topic)]),
            status=status,
            source_title=source_title,
            source_path=plan["source"],
            source_hash=plan.get("source_hash", ""),
            generated_at=generated_at,
            run_name=run_dir.name,
            candidate_kind="topic",
            owner=owner,
        )
        lines = [
            topic_frontmatter,
            "",
            f"# {topic}",
            "",
            f"- Source overview: [{overview_candidate.name}]({overview_candidate.name})",
            f"- Candidate status: `{status}`",
            f"- Candidate area: `{default_area}`",
            "",
            "## Mentioned in chapters",
            "",
        ]
        if chapters:
            for chapter in chapters:
                lines.append(f"- [{chapter}]({chapter_candidates[chapter].name})")
        else:
            lines.append("- none yet")
        lines.extend(["", "## Neighbor topics", ""])
        if sibling_topics:
            for sibling in sibling_topics:
                lines.append(f"- [{sibling}]({topic_candidates[sibling].name})")
        else:
            lines.append("- none yet")
        write_text(path, "\n".join(lines) + "\n")
        link_map[path.name] = {
            "type": "topic",
            "links": [overview_candidate.name]
            + [chapter_candidates[chapter].name for chapter in chapters]
            + [topic_candidates[sibling].name for sibling in sibling_topics],
        }

    overview_lines = [
        f"# Source Overview — {source_title}",
        "",
        f"- Generated at: {generated_at}",
        f"- Source path: `{plan['source']}`",
        f"- Effective split level: H{plan['effective_split_level']}",
        f"- Total batches: {len(batches)}",
        f"- Completed notes: {len(notes)}",
        f"- Candidate overview page: [{overview_candidate.name}](candidate-pages/{overview_candidate.name})",
        f"- Default candidate area: `{default_area}`",
        "",
        "## What this synthesis gives you",
        "",
        "- a source overview baseline",
        "- chapter-level summaries from completed close-reading batches",
        "- topic/glossary seeds worth promoting into stable pages",
        "- unresolved questions to revisit before final import",
        "- candidate draft pages with explicit relative links",
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
        f"- [candidate-pages/{overview_candidate.name}](candidate-pages/{overview_candidate.name})"
    )
    for chapter in chapter_list:
        path = chapter_candidates[chapter]
        overview_lines.append(
            f"- [{path.name}](candidate-pages/{path.name}) — chapter summary draft"
        )
    for topic, path in topic_candidates.items():
        overview_lines.append(
            f"- [{path.name}](candidate-pages/{path.name}) — topic draft for {topic}"
        )
    write_text(out_dir / "source-overview.md", "\n".join(overview_lines) + "\n")

    chapter_lines = ["# Chapter Summaries", ""]
    for chapter, payload in chapter_rows.items():
        chapter_lines.extend(
            [f"## [{chapter}](candidate-pages/{chapter_candidates[chapter].name})", ""]
        )
        chapter_lines.append(f"- Batches: {', '.join(payload['batches'])}")
        if payload["summaries"]:
            chapter_lines.append("- Summaries:")
            for summary in payload["summaries"]:
                chapter_lines.append(f"  - {summary}")
        else:
            chapter_lines.append("- Summaries: pending")
        if payload["claims"]:
            chapter_lines.append("- Repeated claims:")
            for claim in dedupe(payload["claims"])[:8]:
                chapter_lines.append(f"  - {claim}")
        if payload["procedures"]:
            chapter_lines.append("- Procedures:")
            for item in dedupe(payload["procedures"])[:8]:
                chapter_lines.append(f"  - {item}")
        if payload["topics"]:
            chapter_lines.append("- Topic links:")
            for topic in dedupe(payload["topics"]):
                if topic in topic_candidates:
                    chapter_lines.append(
                        f"  - [{topic}](candidate-pages/{topic_candidates[topic].name})"
                    )
        chapter_lines.append("")
    write_text(out_dir / "chapter-summaries.md", "\n".join(chapter_lines) + "\n")

    topic_lines = ["# Topic Candidates", ""]
    for term, count in topic_counter.most_common(20):
        path = topic_candidates.get(term)
        if path:
            topic_lines.append(f"- [{term}](candidate-pages/{path.name}) (x{count})")
        else:
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

    link_map_json = {
        "overview_page": overview_candidate.name,
        "pages": link_map,
    }
    write_text(
        out_dir / "candidate-link-map.json",
        json.dumps(link_map_json, ensure_ascii=False, indent=2) + "\n",
    )
    link_map_lines = [
        "# Candidate Link Map",
        "",
        f"- Overview page: [candidate-pages/{overview_candidate.name}](candidate-pages/{overview_candidate.name})",
        "",
    ]
    for page, payload in sorted(link_map.items()):
        link_map_lines.append(f"## {page}")
        link_map_lines.append(f"- Type: {payload['type']}")
        if payload["links"]:
            link_map_lines.append("- Outgoing links:")
            for link in payload["links"]:
                link_map_lines.append(
                    f"  - [candidate-pages/{link}](candidate-pages/{link})"
                )
        else:
            link_map_lines.append("- Outgoing links: none")
        link_map_lines.append("")
    write_text(out_dir / "candidate-link-map.md", "\n".join(link_map_lines) + "\n")

    report = {
        "generated_at": generated_at,
        "source_title": source_title,
        "batch_count": len(batches),
        "completed_notes": len(notes),
        "chapters": len(chapter_rows),
        "candidate_metadata": {
            "default_area": default_area,
            "status": status,
            "owner": owner,
        },
        "candidate_pages": {
            "overview": overview_candidate.name,
            "chapters": [path.name for path in chapter_candidates.values()],
            "topics": [path.name for path in topic_candidates.values()],
        },
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
    parser.add_argument(
        "--default-area",
        default="__SET_ME__",
        help="Area value to write into candidate page frontmatter (default: __SET_ME__)",
    )
    parser.add_argument(
        "--owner",
        help="Optional owner value to write into candidate page frontmatter",
    )
    parser.add_argument(
        "--status",
        default="draft",
        help="Status value to write into candidate page frontmatter (default: draft)",
    )
    args = parser.parse_args()

    run_dir = Path(args.run_dir)
    out_dir = Path(args.out) if args.out else run_dir / "synthesis"
    report = build_synthesis(
        run_dir,
        out_dir,
        default_area=args.default_area,
        owner=args.owner,
        status=args.status,
    )
    print(json.dumps(report, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
