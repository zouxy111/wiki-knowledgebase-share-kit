#!/usr/bin/env python3
"""Helpers for the canonical skill catalog."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CATALOG_PATH = REPO_ROOT / "skills" / "catalog.toml"


@dataclass(frozen=True)
class SkillEntry:
    order: int
    name: str
    path: str
    area: str
    role: str
    role_en: str


def load_catalog(
    catalog_path: Path = CATALOG_PATH,
) -> tuple[dict[str, str], list[SkillEntry]]:
    raw = parse_catalog(catalog_path.read_text(encoding="utf-8"))
    package = raw.get("package", {})
    skills = [SkillEntry(**entry) for entry in raw.get("skills", [])]
    skills.sort(key=lambda entry: (entry.order, entry.name))
    return package, skills


def parse_catalog(text: str) -> dict[str, object]:
    package: dict[str, object] = {}
    root_fields: dict[str, object] = {}
    skills: list[dict[str, object]] = []
    current_skill: dict[str, object] | None = None
    section: str | None = None

    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if line == "[package]":
            section = "package"
            continue
        if line == "[[skills]]":
            current_skill = {}
            skills.append(current_skill)
            section = "skills"
            continue
        if "=" not in line:
            raise ValueError(f"Invalid catalog line: {raw_line}")

        key, value = [part.strip() for part in line.split("=", 1)]
        parsed_value: object
        if value.startswith('"') and value.endswith('"'):
            parsed_value = value[1:-1]
        else:
            parsed_value = int(value)

        if section == "package":
            package[key] = parsed_value
        elif section == "skills" and current_skill is not None:
            current_skill[key] = parsed_value
        elif section is None:
            root_fields[key] = parsed_value
        else:
            raise ValueError(
                f"Key/value pair outside of a recognized section: {raw_line}"
            )

    return {"package": package, "skills": skills, **root_fields}


def skill_entries(catalog_path: Path = CATALOG_PATH) -> list[SkillEntry]:
    return load_catalog(catalog_path)[1]


def skill_names(catalog_path: Path = CATALOG_PATH) -> list[str]:
    return [entry.name for entry in skill_entries(catalog_path)]


def capability_areas(catalog_path: Path = CATALOG_PATH) -> list[str]:
    areas: list[str] = []
    for entry in skill_entries(catalog_path):
        if entry.area not in areas:
            areas.append(entry.area)
    return areas


def render_skill_table(language: str = "zh", catalog_path: Path = CATALOG_PATH) -> str:
    headers = {
        "zh": ("#", "Skill", "能力线", "主要职责"),
        "en": ("#", "Skill", "Capability area", "Primary responsibility"),
    }
    if language not in headers:
        raise ValueError(f"Unsupported language: {language}")

    role_field = "role" if language == "zh" else "role_en"
    first, second, third, fourth = headers[language]
    lines = [
        f"| {first} | {second} | {third} | {fourth} |",
        "|---|---|---|---|",
    ]
    for entry in skill_entries(catalog_path):
        role = getattr(entry, role_field)
        lines.append(f"| {entry.order} | `{entry.name}` | {entry.area} | {role} |")
    return "\n".join(lines)


def render_capability_areas(catalog_path: Path = CATALOG_PATH) -> str:
    return "\n".join(f"- **{area}**" for area in capability_areas(catalog_path))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Read or render the canonical skill catalog."
    )
    parser.add_argument(
        "command",
        choices=("list-names", "render-table", "render-areas"),
        help="Output skill names, a markdown table, or the capability-area bullet list.",
    )
    parser.add_argument(
        "--lang",
        choices=("zh", "en"),
        default="zh",
        help="Language for rendered markdown tables.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.command == "list-names":
        print("\n".join(skill_names()))
    elif args.command == "render-table":
        print(render_skill_table(language=args.lang))
    else:
        print(render_capability_areas())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
