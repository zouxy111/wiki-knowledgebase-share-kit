#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Iterable

HEADING_RE = re.compile(r'^(#{1,6})\s+(.*\S)\s*$', re.MULTILINE)
CODE_RE = re.compile(r'`([^`]{2,80})`')
BOLD_RE = re.compile(r'\*\*([^*\n]{2,80})\*\*|__([^_\n]{2,80})__')
TITLE_RE = re.compile(r'\b(?:[A-Z][a-z]+(?:\s+[A-Z][a-z]+){0,4}|[A-Z]{2,}(?:\s+[A-Z]{2,})*)\b')
CJK_QUOTE_RE = re.compile(r'[《「“]([^》」”\n]{2,80})[》」”]')
STOP_TERMS = {
    'Chapter', 'Section', 'Part', 'Introduction', 'Conclusion', 'Overview',
    'The', 'And', 'For', 'With', 'From', 'This', 'That'
}


def iter_md_files(source: Path) -> Iterable[Path]:
    if source.is_dir():
        for path in sorted(source.rglob('*.md')):
            if path.name.lower() in {'toc.md', 'readme.md'}:
                continue
            yield path
    else:
        yield source


def normalize(term: str) -> str:
    term = re.sub(r'\s+', ' ', term.strip())
    return term.strip(' -:：,，。.;；')


def collect_terms(path: Path, counter: Counter, sources: dict[str, set[str]]) -> None:
    text = path.read_text(encoding='utf-8', errors='ignore')

    for _, title in HEADING_RE.findall(text):
        term = normalize(title)
        if len(term) >= 2:
            counter[term] += 3
            sources[term].add(path.name)

    for match in CODE_RE.findall(text):
        term = normalize(match)
        if len(term) >= 2:
            counter[term] += 2
            sources[term].add(path.name)

    for match in BOLD_RE.findall(text):
        term = normalize(match[0] or match[1])
        if len(term) >= 2:
            counter[term] += 2
            sources[term].add(path.name)

    for match in TITLE_RE.findall(text):
        term = normalize(match)
        if len(term) >= 2 and term not in STOP_TERMS:
            counter[term] += 1
            sources[term].add(path.name)

    for match in CJK_QUOTE_RE.findall(text):
        term = normalize(match)
        if len(term) >= 2:
            counter[term] += 1
            sources[term].add(path.name)


def main() -> int:
    parser = argparse.ArgumentParser(description='Extract glossary candidates from a markdown file or directory.')
    parser.add_argument('source', help='Markdown file or directory')
    parser.add_argument('--out', required=True, help='Output directory')
    parser.add_argument('--top', type=int, default=80, help='Maximum number of terms to output')
    parser.add_argument('--min-score', type=int, default=2, help='Minimum aggregate score')
    args = parser.parse_args()

    source = Path(args.source)
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)

    counter: Counter[str] = Counter()
    sources: dict[str, set[str]] = defaultdict(set)
    for path in iter_md_files(source):
        collect_terms(path, counter, sources)

    items = []
    for term, score in counter.most_common():
        if score < args.min_score:
            continue
        items.append({
            'term': term,
            'score': score,
            'source_files': sorted(sources[term]),
        })
        if len(items) >= args.top:
            break

    (out / 'glossary-candidates.json').write_text(json.dumps(items, ensure_ascii=False, indent=2), encoding='utf-8')
    lines = ['# Glossary Candidates', '']
    for item in items:
        files = ', '.join(item['source_files'])
        lines.append(f"- **{item['term']}** (score: {item['score']}; files: {files})")
    (out / 'glossary-candidates.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(json.dumps({'candidates': len(items), 'output_dir': str(out)}, ensure_ascii=False))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
