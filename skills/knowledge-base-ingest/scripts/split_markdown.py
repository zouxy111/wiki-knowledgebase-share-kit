#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import List

HEADING_RE = re.compile(r'^(#{1,6})\s+(.*\S)\s*$')
NON_SLUG_RE = re.compile(r'[^a-z0-9]+')


@dataclass
class Heading:
    line_index: int
    level: int
    title: str


@dataclass
class Chunk:
    title: str
    level: int
    slug: str
    lines: List[str]
    start_line: int
    end_line: int
    word_count: int


def slugify(text: str) -> str:
    text = text.lower().strip()
    text = NON_SLUG_RE.sub('-', text)
    text = text.strip('-')
    return text or 'section'


def find_headings(lines: List[str]) -> List[Heading]:
    headings: List[Heading] = []
    for idx, line in enumerate(lines):
        m = HEADING_RE.match(line)
        if m:
            headings.append(Heading(idx, len(m.group(1)), m.group(2).strip()))
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
    return len(re.findall(r'\b\w+\b', ''.join(lines)))


def split_range(lines: List[str], headings: List[Heading], level: int, start: int, end: int, max_words: int) -> List[Chunk]:
    scoped = [h for h in headings if start <= h.line_index < end and h.level == level]
    if not scoped:
        title = f'part-{start + 1}'
        chunk_lines = lines[start:end]
        return [Chunk(title, level, slugify(title), chunk_lines, start + 1, end, count_words(chunk_lines))]

    chunks: List[Chunk] = []
    for i, heading in enumerate(scoped):
        section_start = heading.line_index
        if i + 1 < len(scoped):
            section_end = scoped[i + 1].line_index
        else:
            next_shallower = [h.line_index for h in headings if h.line_index > heading.line_index and h.level < level and h.line_index < end]
            section_end = min(next_shallower) if next_shallower else end
        chunk_lines = lines[section_start:section_end]
        word_count = count_words(chunk_lines)

        deeper = [h for h in headings if section_start < h.line_index < section_end and h.level == level + 1]
        if max_words and word_count > max_words and deeper and level < 6:
            chunks.extend(split_range(lines, headings, level + 1, section_start, section_end, max_words))
            continue

        chunks.append(
            Chunk(
                title=heading.title,
                level=heading.level,
                slug=slugify(heading.title),
                lines=chunk_lines,
                start_line=section_start + 1,
                end_line=section_end,
                word_count=word_count,
            )
        )
    return chunks


def write_chunks(chunks: List[Chunk], output_dir: Path, prefix: str) -> None:
    manifest = []
    for idx, chunk in enumerate(chunks, start=1):
        filename = f'{idx:03d}-{prefix}{chunk.slug}.md'
        path = output_dir / filename
        path.write_text(''.join(chunk.lines), encoding='utf-8')
        manifest.append(
            {
                'index': idx,
                'file': filename,
                'title': chunk.title,
                'level': chunk.level,
                'start_line': chunk.start_line,
                'end_line': chunk.end_line,
                'word_count': chunk.word_count,
            }
        )
    (output_dir / 'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding='utf-8')


def main() -> int:
    parser = argparse.ArgumentParser(description='Split a long markdown file into heading-based chunks.')
    parser.add_argument('source', help='Path to the source markdown file')
    parser.add_argument('--out', required=True, help='Output directory for chunk files')
    parser.add_argument('--level', type=int, default=2, help='Preferred heading level to split on (default: 2)')
    parser.add_argument('--max-words', type=int, default=1800, help='Recursively split oversized chunks at the next heading level (default: 1800)')
    parser.add_argument('--prefix', default='', help='Optional filename prefix, e.g. book-')
    args = parser.parse_args()

    source = Path(args.source)
    output_dir = Path(args.out)
    output_dir.mkdir(parents=True, exist_ok=True)

    lines = source.read_text(encoding='utf-8').splitlines(keepends=True)
    headings = find_headings(lines)
    if not headings:
        raise SystemExit('No markdown headings found; add headings or split manually.')

    level = choose_level(headings, args.level)
    chunks = split_range(lines, headings, level, 0, len(lines), args.max_words)

    preamble_start = headings[0].line_index
    if preamble_start > 0:
        preamble = lines[:preamble_start]
        if ''.join(preamble).strip():
            (output_dir / '000-preamble.md').write_text(''.join(preamble), encoding='utf-8')

    write_chunks(chunks, output_dir, args.prefix)
    print(json.dumps({'source': str(source), 'effective_level': level, 'chunks': len(chunks), 'output_dir': str(output_dir)}, ensure_ascii=False))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
