#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from pathlib import Path

WORD_RE = re.compile(r"[A-Za-z][A-Za-z0-9_-]{2,}|[\u4e00-\u9fff]{2,}")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*\S)\s*$", re.MULTILINE)
FRONTMATTER_TITLE_RE = re.compile(r'^title:\s*["\']?(.+?)["\']?\s*$', re.MULTILINE)
STOPWORDS = {
    "the",
    "and",
    "for",
    "with",
    "from",
    "this",
    "that",
    "into",
    "your",
    "page",
    "pages",
    "chapter",
    "section",
    "overview",
    "知识库",
    "页面",
    "章节",
    "内容",
    "相关",
    "一个",
    "可以",
    "进行",
    "以及",
    "使用",
    "导入",
}


def load_pages(directory: Path):
    pages = []
    for path in sorted(directory.rglob("*.md")):
        if path.name.lower() in {"toc.md", "readme.md", "glossary-candidates.md"}:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        title_match = FRONTMATTER_TITLE_RE.search(text)
        if title_match:
            title = title_match.group(1).strip()
        else:
            heading_match = HEADING_RE.search(text)
            title = heading_match.group(2).strip() if heading_match else path.stem
        tokens = []
        for token in WORD_RE.findall(text):
            lowered = token.lower()
            if lowered in STOPWORDS:
                continue
            tokens.append(lowered)
        pages.append({"path": path, "title": title, "tokens": set(tokens)})
    return pages


def score(a, b):
    if not a["tokens"] or not b["tokens"]:
        return 0.0, []
    shared = sorted(a["tokens"] & b["tokens"])
    if not shared:
        return 0.0, []
    jaccard = len(shared) / len(a["tokens"] | b["tokens"])
    title_overlap = len(
        set(WORD_RE.findall(a["title"].lower()))
        & set(WORD_RE.findall(b["title"].lower()))
    )
    score_value = jaccard + (0.08 * title_overlap)
    return score_value, shared[:8]


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Suggest related links between markdown pages in a directory."
    )
    parser.add_argument("directory", help="Directory containing markdown pages")
    parser.add_argument(
        "--top", type=int, default=3, help="Top related suggestions per page"
    )
    parser.add_argument(
        "--min-score", type=float, default=0.08, help="Minimum score threshold"
    )
    args = parser.parse_args()

    directory = Path(args.directory)
    pages = load_pages(directory)
    suggestions = defaultdict(list)

    for i, a in enumerate(pages):
        for j, b in enumerate(pages):
            if i >= j:
                continue
            value, shared = score(a, b)
            if value < args.min_score:
                continue
            rel_a = str(b["path"].relative_to(directory))
            rel_b = str(a["path"].relative_to(directory))
            suggestions[str(a["path"].relative_to(directory))].append(
                {
                    "target": rel_a,
                    "title": b["title"],
                    "score": round(value, 3),
                    "shared_terms": shared,
                }
            )
            suggestions[str(b["path"].relative_to(directory))].append(
                {
                    "target": rel_b,
                    "title": a["title"],
                    "score": round(value, 3),
                    "shared_terms": shared,
                }
            )

    normalized = {}
    for key, values in suggestions.items():
        normalized[key] = sorted(values, key=lambda x: (-x["score"], x["target"]))[
            : args.top
        ]

    (directory / "related-links.json").write_text(
        json.dumps(normalized, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    lines = ["# Related Link Suggestions", ""]
    for source in sorted(normalized):
        lines.append(f"## {source}")
        for item in normalized[source]:
            shared = ", ".join(item["shared_terms"])
            lines.append(
                f"- `{item['target']}` — {item['title']} (score: {item['score']}; shared: {shared})"
            )
        lines.append("")
    (directory / "related-links.md").write_text("\n".join(lines), encoding="utf-8")
    print(
        json.dumps(
            {
                "pages": len(pages),
                "with_suggestions": len(normalized),
                "output_dir": str(directory),
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
