#!/usr/bin/env python3
"""Validate skill bundle structure, frontmatter, catalog sync, and doc snippets."""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path

from skill_catalog import render_capability_areas, render_skill_table, skill_entries

REPO_ROOT = Path(__file__).resolve().parent.parent
ALLOWED_FRONTMATTER_KEYS = {
    "name",
    "description",
    "license",
    "allowed-tools",
    "metadata",
}


@dataclass(frozen=True)
class DocSyncSpec:
    path: str
    marker: str
    language: str | None = None
    renderer: str = "table"


DOC_SYNC_SPECS = [
    DocSyncSpec("README.md", "skill-catalog:zh", language="zh"),
    DocSyncSpec("README.md", "capability-areas", renderer="areas"),
    DocSyncSpec("README.en.md", "skill-catalog:en", language="en"),
    DocSyncSpec("README.en.md", "capability-areas", renderer="areas"),
    DocSyncSpec("START-HERE.md", "skill-catalog:zh", language="zh"),
    DocSyncSpec("docs/README.md", "skill-catalog:zh", language="zh"),
]


def _read_frontmatter(skill_md: Path) -> dict[str, str]:
    text = skill_md.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n?", text, re.DOTALL)
    if not match:
        raise ValueError("missing YAML frontmatter")

    frontmatter: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line.startswith((" ", "\t")):
            continue
        if ":" not in line:
            raise ValueError(f"invalid frontmatter line: {line}")
        key, value = line.split(":", 1)
        frontmatter[key.strip()] = value.strip()
    return frontmatter


def _render_expected(root: Path, spec: DocSyncSpec) -> str:
    catalog_path = root / "skills" / "catalog.toml"
    if spec.renderer == "areas":
        return render_capability_areas(catalog_path)
    return render_skill_table(language=spec.language or "zh", catalog_path=catalog_path)


def _replace_doc_block(text: str, marker: str, rendered: str) -> str:
    start = f"<!-- {marker}:start -->"
    end = f"<!-- {marker}:end -->"
    pattern = re.compile(rf"{re.escape(start)}\n.*?\n{re.escape(end)}", re.DOTALL)
    replacement = f"{start}\n{rendered}\n{end}"
    if not pattern.search(text):
        raise ValueError(f"marker block not found: {marker}")
    return pattern.sub(replacement, text, count=1)


def validate_repository(root: Path, write_doc_sync: bool = False) -> list[str]:
    errors: list[str] = []
    entries = skill_entries(root / "skills" / "catalog.toml")

    if not entries:
        return ["skills/catalog.toml does not define any skills"]

    names = [entry.name for entry in entries]
    if len(names) != len(set(names)):
        errors.append("skills/catalog.toml contains duplicate skill names")

    orders = [entry.order for entry in entries]
    if len(orders) != len(set(orders)):
        errors.append("skills/catalog.toml contains duplicate skill order values")

    catalog_paths = {entry.path for entry in entries}
    actual_dirs = {
        f"skills/{path.name}"
        for path in (root / "skills").iterdir()
        if path.is_dir() and path.name != "__pycache__"
    }
    if catalog_paths != actual_dirs:
        missing = sorted(catalog_paths - actual_dirs)
        extra = sorted(actual_dirs - catalog_paths)
        if missing:
            errors.append("catalog paths missing from skills/: " + ", ".join(missing))
        if extra:
            errors.append(
                "skills/ directories missing from catalog: " + ", ".join(extra)
            )

    for entry in entries:
        skill_dir = root / entry.path
        skill_md = skill_dir / "SKILL.md"
        references_dir = skill_dir / "references"
        agent_config = skill_dir / "agents" / "openai.yaml"

        if not skill_md.exists():
            errors.append(f"{entry.path}: missing SKILL.md")
            continue

        try:
            frontmatter = _read_frontmatter(skill_md)
        except ValueError as exc:
            errors.append(f"{entry.path}/SKILL.md: {exc}")
            continue

        unexpected_keys = sorted(set(frontmatter) - ALLOWED_FRONTMATTER_KEYS)
        if unexpected_keys:
            errors.append(
                f"{entry.path}/SKILL.md: unexpected frontmatter key(s): {', '.join(unexpected_keys)}"
            )

        if frontmatter.get("name") != entry.name:
            errors.append(
                f"{entry.path}/SKILL.md: frontmatter name '{frontmatter.get('name', '')}' "
                f"does not match catalog name '{entry.name}'"
            )
        if not frontmatter.get("description"):
            errors.append(f"{entry.path}/SKILL.md: description is missing or empty")
        if skill_dir.name != entry.name:
            errors.append(
                f"{entry.path}: directory name does not match skill name '{entry.name}'"
            )

        if not references_dir.exists():
            errors.append(f"{entry.path}: missing references/")
        elif not any(references_dir.iterdir()):
            errors.append(f"{entry.path}: references/ is empty")

        if not agent_config.exists():
            errors.append(f"{entry.path}: missing agents/openai.yaml")

    for spec in DOC_SYNC_SPECS:
        path = root / spec.path
        rendered = _render_expected(root, spec)
        current = path.read_text(encoding="utf-8")
        try:
            updated = _replace_doc_block(current, spec.marker, rendered)
        except ValueError as exc:
            errors.append(f"{spec.path}: {exc}")
            continue
        if write_doc_sync:
            if updated != current:
                path.write_text(updated, encoding="utf-8")
        elif updated != current:
            errors.append(
                f"{spec.path}: marker '{spec.marker}' is out of sync with skills/catalog.toml "
                "(run python3 scripts/validate_skill_bundle.py --write-doc-sync)"
            )

    return errors


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Validate the share-kit skill bundle and optionally rewrite synced doc snippets."
    )
    parser.add_argument(
        "--root",
        default=str(REPO_ROOT),
        help="Repository root to validate. Defaults to this repository.",
    )
    parser.add_argument(
        "--write-doc-sync",
        action="store_true",
        help="Rewrite the marker-based doc snippets so they match skills/catalog.toml.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    errors = validate_repository(Path(args.root), write_doc_sync=args.write_doc_sync)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("Skill bundle validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
