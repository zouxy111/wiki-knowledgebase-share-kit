#!/usr/bin/env python3
"""Tests for scripts/validate_skill_bundle.py."""

import sys
from pathlib import Path

scripts_dir = Path(__file__).parent.parent / "scripts"
sys.path.insert(0, str(scripts_dir))

from validate_skill_bundle import validate_repository  # noqa: E402


def _write_skill(skill_dir: Path, name: str) -> None:
    (skill_dir / "references").mkdir(parents=True)
    (skill_dir / "agents").mkdir(parents=True)
    (skill_dir / "references" / "note.md").write_text("reference", encoding="utf-8")
    (skill_dir / "agents" / "openai.yaml").write_text("name: test\n", encoding="utf-8")
    (skill_dir / "SKILL.md").write_text(
        f"---\nname: {name}\ndescription: test description\n---\n\n# {name}\n",
        encoding="utf-8",
    )


def _write_repo(tmp_path: Path) -> Path:
    repo = tmp_path / "repo"
    (repo / "skills").mkdir(parents=True)
    (repo / "docs").mkdir(parents=True)

    (repo / "skills" / "catalog.toml").write_text(
        "\n".join(
            [
                "version = 1",
                "",
                "[package]",
                'name = "test-kit"',
                "",
                "[[skills]]",
                "order = 1",
                'name = "alpha-skill"',
                'path = "skills/alpha-skill"',
                'area = "Track A"',
                'role = "Alpha role"',
                'role_en = "Alpha role"',
                "",
                "[[skills]]",
                "order = 2",
                'name = "beta-skill"',
                'path = "skills/beta-skill"',
                'area = "Track B"',
                'role = "Beta role"',
                'role_en = "Beta role"',
                "",
            ]
        ),
        encoding="utf-8",
    )

    _write_skill(repo / "skills" / "alpha-skill", "alpha-skill")
    _write_skill(repo / "skills" / "beta-skill", "beta-skill")

    synced_table = "\n".join(
        [
            "<!-- skill-catalog:zh:start -->",
            "| # | Skill | 能力线 | 主要职责 |",
            "|---|---|---|---|",
            "| 1 | `alpha-skill` | Track A | Alpha role |",
            "| 2 | `beta-skill` | Track B | Beta role |",
            "<!-- skill-catalog:zh:end -->",
        ]
    )
    synced_areas = "\n".join(
        [
            "<!-- capability-areas:start -->",
            "- **Track A**",
            "- **Track B**",
            "<!-- capability-areas:end -->",
        ]
    )
    synced_table_en = "\n".join(
        [
            "<!-- skill-catalog:en:start -->",
            "| # | Skill | Capability area | Primary responsibility |",
            "|---|---|---|---|",
            "| 1 | `alpha-skill` | Track A | Alpha role |",
            "| 2 | `beta-skill` | Track B | Beta role |",
            "<!-- skill-catalog:en:end -->",
        ]
    )

    (repo / "README.md").write_text(
        f"# README\n\n{synced_table}\n\n{synced_areas}\n",
        encoding="utf-8",
    )
    (repo / "README.en.md").write_text(
        f"# README EN\n\n{synced_table_en}\n\n{synced_areas}\n",
        encoding="utf-8",
    )
    (repo / "START-HERE.md").write_text(
        f"# START\n\n{synced_table}\n", encoding="utf-8"
    )
    (repo / "docs" / "README.md").write_text(
        f"# DOCS\n\n{synced_table}\n", encoding="utf-8"
    )
    return repo


def test_validate_repository_passes_for_synced_bundle(tmp_path):
    repo = _write_repo(tmp_path)
    assert validate_repository(repo) == []


def test_validate_repository_flags_out_of_sync_docs(tmp_path):
    repo = _write_repo(tmp_path)
    (repo / "README.md").write_text(
        "# README\n\n<!-- skill-catalog:zh:start -->\nwrong\n<!-- skill-catalog:zh:end -->\n\n"
        "<!-- capability-areas:start -->\nwrong\n<!-- capability-areas:end -->\n",
        encoding="utf-8",
    )
    errors = validate_repository(repo)
    assert any(
        "README.md: marker 'skill-catalog:zh' is out of sync" in error
        for error in errors
    )


def test_validate_repository_can_rewrite_synced_docs(tmp_path):
    repo = _write_repo(tmp_path)
    (repo / "README.en.md").write_text(
        "# README EN\n\n<!-- skill-catalog:en:start -->\nold\n<!-- skill-catalog:en:end -->\n\n"
        "<!-- capability-areas:start -->\nold\n<!-- capability-areas:end -->\n",
        encoding="utf-8",
    )
    errors = validate_repository(repo, write_doc_sync=True)
    assert errors == []
    updated = (repo / "README.en.md").read_text(encoding="utf-8")
    assert "| 2 | `beta-skill` | Track B | Beta role |" in updated
