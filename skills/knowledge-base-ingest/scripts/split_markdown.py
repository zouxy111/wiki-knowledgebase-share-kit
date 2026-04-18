#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import List

HEADING_RE = re.compile(r"^(#{1,6})\s+(.*\S)\s*$")
NON_SLUG_RE = re.compile(r"[^a-z0-9]+")


@dataclass
class Heading:
    line_index: int
    level: int
    title: str
    breadcrumb: List[str]


@dataclass
class Chunk:
    title: str
    level: int
    slug: str
    lines: List[str]
    start_line: int
    end_line: int
    word_count: int
    breadcrumb: List[str]


def slugify(text: str) -> str:
    text = text.lower().strip()
    text = NON_SLUG_RE.sub("-", text)
    text = text.strip("-")
    return text or "section"


def find_headings(lines: List[str]) -> List[Heading]:
    headings: List[Heading] = []
    stack: List[tuple[int, str]] = []
    for idx, line in enumerate(lines):
        m = HEADING_RE.match(line)
        if not m:
            continue
        level = len(m.group(1))
        title = m.group(2).strip()
        while stack and stack[-1][0] >= level:
            stack.pop()
        breadcrumb = [item[1] for item in stack] + [title]
        stack.append((level, title))
        headings.append(Heading(idx, level, title, breadcrumb))
    return headings


def choose_level(headings: List[Heading], requested: int) -> int:
    levels = {h.level for h in headings}
    if requested in levels:
        return requested
    for level in range(requested + 1, 7):
        if level in levels:
            return level
    for level in range(requested - 1, 0, -1):
        if level in levels:
            return level
    return 1


def count_words(lines: List[str]) -> int:
    text = "".join(lines)
    # Count Latin-alphabet / number tokens as words.
    en_words = len(re.findall(r"[A-Za-z0-9_]+", text))
    # Count CJK characters individually so mixed Chinese/English sources do not
    # massively undercount chunk size.
    cjk_chars = len(re.findall(r"[\u4e00-\u9fff\u3000-\u303f\uff00-\uffef]", text))
    return en_words + cjk_chars


def make_chunk(
    title: str,
    level: int,
    lines: List[str],
    start_line: int,
    end_line: int,
    breadcrumb: List[str],
) -> Chunk:
    return Chunk(
        title=title,
        level=level,
        slug=slugify(title),
        lines=lines,
        start_line=start_line,
        end_line=end_line,
        word_count=count_words(lines),
        breadcrumb=breadcrumb,
    )


def window_split_chunks(
    lines: List[str],
    start: int,
    end: int,
    *,
    base_title: str,
    level: int,
    breadcrumb: List[str],
    max_lines: int,
) -> List[Chunk]:
    total_lines = end - start
    if total_lines <= 0:
        return []
    if not max_lines or total_lines <= max_lines:
        return [
            make_chunk(
                title=base_title,
                level=level,
                lines=lines[start:end],
                start_line=start + 1,
                end_line=end,
                breadcrumb=breadcrumb,
            )
        ]

    chunks: List[Chunk] = []
    part_number = 1
    for window_start in range(start, end, max_lines):
        window_end = min(window_start + max_lines, end)
        window_title = f"{base_title} (Part {part_number})"
        window_breadcrumb = breadcrumb + [f"Part {part_number}"]
        chunks.append(
            make_chunk(
                title=window_title,
                level=level,
                lines=lines[window_start:window_end],
                start_line=window_start + 1,
                end_line=window_end,
                breadcrumb=window_breadcrumb,
            )
        )
        part_number += 1
    return chunks


def split_range(
    lines: List[str],
    headings: List[Heading],
    level: int,
    start: int,
    end: int,
    max_words: int,
    max_lines: int,
) -> List[Chunk]:
    scoped = [h for h in headings if start <= h.line_index < end and h.level == level]
    if not scoped:
        return window_split_chunks(
            lines,
            start,
            end,
            base_title=f"part-{start + 1}",
            level=level,
            breadcrumb=[f"part-{start + 1}"],
            max_lines=max_lines,
        )

    chunks: List[Chunk] = []
    for i, heading in enumerate(scoped):
        section_start = heading.line_index
        if i + 1 < len(scoped):
            section_end = scoped[i + 1].line_index
        else:
            next_shallower = [
                h.line_index
                for h in headings
                if h.line_index > heading.line_index
                and h.level < level
                and h.line_index < end
            ]
            section_end = min(next_shallower) if next_shallower else end
        chunk_lines = lines[section_start:section_end]
        word_count = count_words(chunk_lines)
        line_count = section_end - section_start

        deeper = [
            h
            for h in headings
            if section_start < h.line_index < section_end and h.level == level + 1
        ]
        if (
            (
                (max_words and word_count > max_words)
                or (max_lines and line_count > max_lines)
            )
            and deeper
            and level < 6
        ):
            chunks.extend(
                split_range(
                    lines,
                    headings,
                    level + 1,
                    section_start,
                    section_end,
                    max_words,
                    max_lines,
                )
            )
            continue

        if (max_words and word_count > max_words) or (
            max_lines and line_count > max_lines
        ):
            chunks.extend(
                window_split_chunks(
                    lines,
                    section_start,
                    section_end,
                    base_title=heading.title,
                    level=heading.level,
                    breadcrumb=heading.breadcrumb,
                    max_lines=max_lines,
                )
            )
            continue

        chunks.append(
            make_chunk(
                title=heading.title,
                level=heading.level,
                lines=chunk_lines,
                start_line=section_start + 1,
                end_line=section_end,
                breadcrumb=heading.breadcrumb,
            )
        )
    return chunks


def unique_filename(output_dir: Path, idx: int, prefix: str, slug: str) -> str:
    candidate = f"{idx:03d}-{prefix}{slug}.md"
    counter = 2
    while (output_dir / candidate).exists():
        candidate = f"{idx:03d}-{prefix}{slug}-{counter}.md"
        counter += 1
    return candidate


def make_manifest_entry(
    *,
    index: int,
    filename: str,
    title: str,
    level: int,
    breadcrumb: list[str],
    start_line: int,
    end_line: int,
    word_count: int,
) -> dict:
    return {
        "index": index,
        "file": filename,
        "title": title,
        "level": level,
        "breadcrumb": breadcrumb,
        "start_line": start_line,
        "end_line": end_line,
        "word_count": word_count,
    }


def write_preamble(lines: List[str], output_dir: Path) -> dict | None:
    if not "".join(lines).strip():
        return None
    filename = "000-preamble.md"
    (output_dir / filename).write_text("".join(lines), encoding="utf-8")
    return make_manifest_entry(
        index=0,
        filename=filename,
        title="Preamble",
        level=0,
        breadcrumb=["Preamble"],
        start_line=1,
        end_line=len(lines),
        word_count=count_words(lines),
    )


def write_chunks(chunks: List[Chunk], output_dir: Path, prefix: str) -> list[dict]:
    manifest = []
    for idx, chunk in enumerate(chunks, start=1):
        filename = unique_filename(output_dir, idx, prefix, chunk.slug)
        path = output_dir / filename
        path.write_text("".join(chunk.lines), encoding="utf-8")
        manifest.append(
            make_manifest_entry(
                index=idx,
                filename=filename,
                title=chunk.title,
                level=chunk.level,
                breadcrumb=chunk.breadcrumb,
                start_line=chunk.start_line,
                end_line=chunk.end_line,
                word_count=chunk.word_count,
            )
        )
    return manifest


def write_toc(manifest: list[dict], output_dir: Path) -> None:
    lines = ["# Extracted Table of Contents", ""]
    for item in manifest:
        indent = "  " * max(0, len(item["breadcrumb"]) - 1)
        lines.append(f"{indent}- [{item['title']}]({item['file']})")
    (output_dir / "toc.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_coverage_map(manifest: list[dict], output_dir: Path) -> None:
    lines = [
        "# Source Coverage Map",
        "",
        "> Completion rule: every manifest row must be assigned a final status before the import can be called complete.",
        "> Final statuses: `covered`, `merged`, `index-only`, `intentionally-omitted`.",
        "> Incomplete statuses: `unread`, `blocked`.",
        "",
        "| index | file | title | lines | words | status | target pages | notes |",
        "|---|---|---|---|---:|---|---|---|",
    ]
    for item in manifest:
        line_span = f"{item['start_line']}-{item['end_line']}"
        lines.append(
            f"| {item['index']:03d} | {item['file']} | {item['title']} | {line_span} | {item['word_count']} | unread |  |  |"
        )
    (output_dir / "coverage-map.md").write_text(
        "\n".join(lines) + "\n", encoding="utf-8"
    )


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Split a long markdown file into bounded chunks so large sources can be read and validated incrementally."
    )
    parser.add_argument("source", help="Path to the source markdown file")
    parser.add_argument("--out", required=True, help="Output directory for chunk files")
    parser.add_argument(
        "--level",
        type=int,
        default=2,
        help="Preferred heading level to split on (default: 2)",
    )
    parser.add_argument(
        "--max-words",
        type=int,
        default=1800,
        help="Recursively split oversized chunks at the next heading level (default: 1800)",
    )
    parser.add_argument(
        "--max-lines",
        type=int,
        default=400,
        help="Hard line cap per chunk. If no suitable deeper headings exist, the script falls back to fixed line windows (default: 400)",
    )
    parser.add_argument(
        "--prefix", default="", help="Optional filename prefix, e.g. book-"
    )
    args = parser.parse_args()

    source = Path(args.source)
    output_dir = Path(args.out)
    output_dir.mkdir(parents=True, exist_ok=True)

    lines = source.read_text(encoding="utf-8").splitlines(keepends=True)
    headings = find_headings(lines)

    manifest: list[dict] = []
    if headings:
        level = choose_level(headings, args.level)
        preamble_start = headings[0].line_index
        if preamble_start > 0:
            preamble_entry = write_preamble(lines[:preamble_start], output_dir)
            if preamble_entry:
                manifest.append(preamble_entry)
        chunks = split_range(
            lines,
            headings,
            level,
            preamble_start if preamble_start > 0 else 0,
            len(lines),
            args.max_words,
            args.max_lines,
        )
        used_heading_split = True
    else:
        level = 1
        chunks = window_split_chunks(
            lines,
            0,
            len(lines),
            base_title="Source",
            level=1,
            breadcrumb=["Source"],
            max_lines=args.max_lines,
        )
        used_heading_split = False

    manifest.extend(write_chunks(chunks, output_dir, args.prefix))
    (output_dir / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    write_toc(manifest, output_dir)
    write_coverage_map(manifest, output_dir)
    print(
        json.dumps(
            {
                "source": str(source),
                "effective_level": level,
                "chunks": len(chunks),
                "manifest_entries": len(manifest),
                "used_heading_split": used_heading_split,
                "output_dir": str(output_dir),
                "coverage_map": str(output_dir / "coverage-map.md"),
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
