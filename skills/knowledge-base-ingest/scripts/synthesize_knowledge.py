#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from split_markdown import slugify  # noqa: E402

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


def normalize_evidence_items(value) -> list[dict]:
    if value is None:
        return []
    if isinstance(value, (str, dict)):
        value = [value]
    if not isinstance(value, list):
        return []
    normalized = []
    for index, item in enumerate(value, start=1):
        if isinstance(item, str):
            text = " ".join(item.split()).strip()
            if text:
                normalized.append(
                    {
                        "item_id": f"item-{index:03d}",
                        "text": text,
                        "importance": "normal",
                        "supported_by": [],
                    }
                )
            continue
        if not isinstance(item, dict):
            continue
        text = " ".join(str(item.get("text", "")).split()).strip()
        if not text:
            continue
        supported_by = item.get("supported_by", [])
        if isinstance(supported_by, dict):
            supported_by = [supported_by]
        evidence_rows = []
        if isinstance(supported_by, list):
            for evidence in supported_by:
                if not isinstance(evidence, dict):
                    continue
                chunk_file = " ".join(
                    str(evidence.get("chunk_file", "")).split()
                ).strip()
                quote = " ".join(str(evidence.get("quote", "")).split()).strip()
                if chunk_file or quote:
                    evidence_rows.append(
                        {
                            "chunk_file": chunk_file,
                            "quote": quote,
                        }
                    )
        item_id = (
            " ".join(str(item.get("fact_id", "")).split()).strip()
            or " ".join(str(item.get("boundary_id", "")).split()).strip()
            or " ".join(str(item.get("item_id", "")).split()).strip()
            or f"item-{index:03d}"
        )
        importance = " ".join(str(item.get("importance", "normal")).split()).strip()
        normalized.append(
            {
                "item_id": item_id,
                "text": text,
                "importance": importance or "normal",
                "supported_by": evidence_rows,
            }
        )
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
        headings_seen = normalize_list(payload.get("headings_seen", []))
        must_keep_facts = normalize_evidence_items(payload.get("must_keep_facts", []))
        boundaries = normalize_evidence_items(
            payload.get("boundaries_and_exceptions", [])
        )
        omission_risk = normalize_list(payload.get("omission_risk", []))
        meaningful = (
            summary
            or any(lists[field] for field in NOTE_LIST_FIELDS)
            or headings_seen
            or must_keep_facts
            or boundaries
            or omission_risk
        )
        if not meaningful or status != "completed":
            continue
        notes[row["batch_key"]] = {
            "summary": summary,
            "status": status,
            "batch_id": payload.get("batch_id", row.get("batch_id", row["batch_key"])),
            "batch_key": row["batch_key"],
            "headings_seen": headings_seen,
            "must_keep_facts": must_keep_facts,
            "boundaries_and_exceptions": boundaries,
            "omission_risk": omission_risk,
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


def evidence_support_rows(
    claim_text: str, note: dict, chunk_files: list[str]
) -> tuple[str, list[dict]]:
    normalized_claim = " ".join(claim_text.split()).strip().lower()
    direct_support = []
    for field in ("must_keep_facts", "boundaries_and_exceptions"):
        for item in note.get(field, []):
            text = " ".join(str(item.get("text", "")).split()).strip()
            if not text or text.lower() != normalized_claim:
                continue
            supported_by = item.get("supported_by", [])
            for evidence in supported_by:
                direct_support.append(
                    {
                        "batch_key": note["batch_key"],
                        "item_id": item.get("item_id"),
                        "chunk_file": evidence.get("chunk_file", ""),
                        "quote": evidence.get("quote", ""),
                    }
                )
    if direct_support:
        return "supported", direct_support
    if claim_text in note.get("key_claims", []):
        fallback_chunk = chunk_files[0] if chunk_files else ""
        return (
            "weakly-supported",
            [
                {
                    "batch_key": note["batch_key"],
                    "item_id": None,
                    "chunk_file": fallback_chunk,
                    "quote": "",
                }
            ],
        )
    return "unsupported", []


def relative_link_issues(candidate_pages_dir: Path) -> tuple[int, int]:
    link_pattern = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
    dead_links = 0
    missing_frontmatter = 0
    for page in candidate_pages_dir.glob("*.md"):
        text = page.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            missing_frontmatter += 1
        for target in link_pattern.findall(text):
            if target.startswith(("http://", "https://", "mailto:", "#", "data:")):
                continue
            target = target.split("#", 1)[0]
            if not target:
                continue
            resolved = (page.parent / target).resolve()
            if not resolved.exists():
                dead_links += 1
    return dead_links, missing_frontmatter


def final_gate_status(
    *,
    expected_batches: int,
    completed_notes: int,
    weak_batches: list[str],
    unsupported_claims: int,
    inferred_claims: int,
    dead_links: int,
    missing_frontmatter: int,
) -> str:
    if completed_notes < expected_batches or weak_batches:
        return "partial"
    if unsupported_claims or inferred_claims:
        return "coverage-complete"
    if dead_links or missing_frontmatter:
        return "evidence-complete"
    return "ready-to-promote"


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
    batch_lookup = {row["batch_key"]: row for row in batches}
    notes = load_completed_notes(run_dir, batches)

    concept_counter: Counter[str] = Counter()
    entity_counter: Counter[str] = Counter()
    topic_counter: Counter[str] = Counter()
    question_counter: Counter[str] = Counter()
    claim_counter: Counter[str] = Counter()
    procedure_counter: Counter[str] = Counter()
    must_keep_counter: Counter[str] = Counter()
    boundary_counter: Counter[str] = Counter()
    weak_batches: list[str] = []
    chapter_rows: dict[str, dict] = defaultdict(
        lambda: {
            "batches": [],
            "summaries": [],
            "claims": [],
            "procedures": [],
            "topics": [],
            "cross_refs": [],
            "fact_items": [],
            "boundary_items": [],
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
        chapter_rows[chapter]["fact_items"].extend(note["must_keep_facts"])
        chapter_rows[chapter]["boundary_items"].extend(
            note["boundaries_and_exceptions"]
        )
        concept_counter.update(note["concepts"])
        entity_counter.update(note["entities"])
        topic_counter.update(note["candidate_topics"])
        question_counter.update(note["open_questions"])
        claim_counter.update(note["key_claims"])
        procedure_counter.update(note["procedures"])
        must_keep_counter.update(item["text"] for item in note["must_keep_facts"])
        boundary_counter.update(
            item["text"] for item in note["boundaries_and_exceptions"]
        )
        if not note["headings_seen"] or (
            not note["must_keep_facts"]
            and not note["boundaries_and_exceptions"]
            and not note["procedures"]
            and not note["omission_risk"]
        ):
            weak_batches.append(row["batch_key"])
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
        lines.extend(["", "## Must-keep facts", ""])
        if payload["fact_items"]:
            for item in dedupe([fact["text"] for fact in payload["fact_items"]])[:10]:
                lines.append(f"- {item}")
        else:
            lines.append("- none yet")
        lines.extend(["", "## Boundaries and exceptions", ""])
        if payload["boundary_items"]:
            for item in dedupe(
                [boundary["text"] for boundary in payload["boundary_items"]]
            )[:10]:
                lines.append(f"- {item}")
        else:
            lines.append("- none yet")
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

    claim_map_pages = []
    evidence_status_counter: Counter[str] = Counter()
    for chapter in chapter_list:
        page_claims = []
        for claim in dedupe(chapter_rows[chapter]["claims"]):
            supporting_rows = []
            claim_status = "unsupported"
            for batch_key, note in notes.items():
                if claim not in note["key_claims"]:
                    continue
                row = batch_lookup.get(batch_key, {})
                batch_status, rows = evidence_support_rows(
                    claim, note, row.get("chunk_files", [])
                )
                if batch_status == "supported":
                    claim_status = "supported"
                elif batch_status == "weakly-supported" and claim_status != "supported":
                    claim_status = "weakly-supported"
                supporting_rows.extend(rows)
            if not supporting_rows and claim_status == "unsupported":
                claim_status = "inferred"
            evidence_status_counter.update([claim_status])
            page_claims.append(
                {
                    "claim_id": f"{slugify(chapter)}-{slugify(claim)[:24]}",
                    "text": claim,
                    "claim_kind": "chapter-claim",
                    "status": claim_status,
                    "supported_by": supporting_rows,
                }
            )
        claim_map_pages.append(
            {
                "page_file": f"candidate-pages/{chapter_candidates[chapter].name}",
                "page_type": "knowledge",
                "claims": page_claims,
            }
        )

    for topic, path in topic_candidates.items():
        topic_claims = []
        for batch_key, note in notes.items():
            if topic not in note["candidate_topics"] and topic not in note["concepts"]:
                continue
            row = batch_lookup.get(batch_key, {})
            for item in note["must_keep_facts"][:4]:
                claim_status = (
                    "supported" if item.get("supported_by") else "weakly-supported"
                )
                evidence_status_counter.update([claim_status])
                topic_claims.append(
                    {
                        "claim_id": f"{slugify(topic)}-{item['item_id']}",
                        "text": item["text"],
                        "claim_kind": "topic-fact",
                        "status": claim_status,
                        "supported_by": [
                            {
                                "batch_key": batch_key,
                                "item_id": item.get("item_id"),
                                "chunk_file": evidence.get("chunk_file", ""),
                                "quote": evidence.get("quote", ""),
                            }
                            for evidence in item.get("supported_by", [])
                        ]
                        or [
                            {
                                "batch_key": batch_key,
                                "item_id": item.get("item_id"),
                                "chunk_file": (
                                    row.get("chunk_files", [""])[0]
                                    if row.get("chunk_files")
                                    else ""
                                ),
                                "quote": "",
                            }
                        ],
                    }
                )
        claim_map_pages.append(
            {
                "page_file": f"candidate-pages/{path.name}",
                "page_type": "knowledge",
                "claims": topic_claims,
            }
        )

    claim_map = {
        "generated_at": generated_at,
        "run_name": run_dir.name,
        "source_title": source_title,
        "pages": claim_map_pages,
    }
    write_text(
        out_dir / "claim-map.json",
        json.dumps(claim_map, ensure_ascii=False, indent=2) + "\n",
    )

    dead_links, missing_frontmatter = relative_link_issues(candidate_pages_dir)
    unsupported_claims = evidence_status_counter["unsupported"]
    inferred_claims = evidence_status_counter["inferred"]
    weakly_supported_claims = evidence_status_counter["weakly-supported"]
    supported_claims = evidence_status_counter["supported"]
    final_status = final_gate_status(
        expected_batches=len(batches),
        completed_notes=len(notes),
        weak_batches=weak_batches,
        unsupported_claims=unsupported_claims,
        inferred_claims=inferred_claims,
        dead_links=dead_links,
        missing_frontmatter=missing_frontmatter,
    )
    delivery_gate = {
        "generated_at": generated_at,
        "run_name": run_dir.name,
        "coverage_check": {
            "status": "pass" if len(notes) == len(batches) else "pending",
            "manifest_entries": sum(len(row["chunk_files"]) for row in batches),
            "coverage_rows": len(batches),
            "unread_chunks": sum(
                len(row["chunk_files"])
                for row in batches
                if row["batch_key"] not in notes
            ),
            "blocked_chunks": 0,
        },
        "extractive_check": {
            "status": (
                "pass" if not weak_batches and len(notes) == len(batches) else "pending"
            ),
            "expected_batches": len(batches),
            "completed_notes": len(notes),
            "missing_notes": [
                row["batch_key"] for row in batches if row["batch_key"] not in notes
            ],
            "weak_batches": weak_batches,
        },
        "evidence_check": {
            "status": (
                "pass" if not unsupported_claims and not inferred_claims else "pending"
            ),
            "total_claims": sum(len(page["claims"]) for page in claim_map_pages),
            "supported_claims": supported_claims,
            "weakly_supported_claims": weakly_supported_claims,
            "inferred_claims": inferred_claims,
            "unsupported_claims": unsupported_claims,
        },
        "integrity_check": {
            "status": (
                "pass" if dead_links == 0 and missing_frontmatter == 0 else "pending"
            ),
            "candidate_pages_exist": bool(list(candidate_pages_dir.glob("*.md"))),
            "dead_links": dead_links,
            "missing_frontmatter": missing_frontmatter,
            "unregistered_pages": 0,
        },
        "final_status": final_status,
    }
    write_text(
        out_dir / "delivery-gate.json",
        json.dumps(delivery_gate, ensure_ascii=False, indent=2) + "\n",
    )

    gap_lines = ["# Gap Report", ""]
    if weak_batches:
        gap_lines.append("## Weak extractive batches")
        for batch_key in weak_batches:
            gap_lines.append(f"- {batch_key}")
        gap_lines.append("")
    if unsupported_claims or inferred_claims:
        gap_lines.append("## Claims not safe to overclaim yet")
        for page in claim_map_pages:
            for claim in page["claims"]:
                if claim["status"] in {"unsupported", "inferred"}:
                    gap_lines.append(
                        f"- {page['page_file']}: {claim['text']} ({claim['status']})"
                    )
        gap_lines.append("")
    if not weak_batches and not unsupported_claims and not inferred_claims:
        gap_lines.append("- No major evidence gaps detected.")
    write_text(out_dir / "gap-report.md", "\n".join(gap_lines) + "\n")

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
        "evidence_gate": {
            "final_status": final_status,
            "weak_batches": weak_batches,
            "supported_claims": supported_claims,
            "weakly_supported_claims": weakly_supported_claims,
            "inferred_claims": inferred_claims,
            "unsupported_claims": unsupported_claims,
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
