#!/usr/bin/env python3
"""Tests for the unified wiki-kit install and verify backend."""

from __future__ import annotations

from pathlib import Path

import pytest

from wiki_knowledgebase_share_kit import core


def write_skill(skills_root: Path, name: str) -> None:
    skill_dir = skills_root / name
    (skill_dir / "references").mkdir(parents=True)
    (skill_dir / "agents").mkdir()
    (skill_dir / "SKILL.md").write_text(
        f"---\nname: {name}\ndescription: Test skill\n---\n",
        encoding="utf-8",
    )
    (skill_dir / "agents" / "openai.yaml").write_text("name: test\n", encoding="utf-8")
    (skill_dir / "references" / "ref.md").write_text("reference\n", encoding="utf-8")


@pytest.fixture()
def fake_bundle(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> Path:
    skills_root = tmp_path / "skills"
    skills_root.mkdir()
    for name in [
        "knowledge-base-kit-guide",
        "knowledge-base-ingest",
        "knowledge-base-audit",
    ]:
        write_skill(skills_root, name)
    monkeypatch.setattr(core, "share_root_candidates", lambda: [skills_root])
    return skills_root


def test_available_skills_reads_bundled_directory(fake_bundle: Path) -> None:
    assert core.available_skills() == [
        "knowledge-base-audit",
        "knowledge-base-ingest",
        "knowledge-base-kit-guide",
    ]


def test_install_skills_copy_mode(fake_bundle: Path, tmp_path: Path) -> None:
    target_dir = tmp_path / "runtime-skills"

    result = core.install_skills(
        target_dir=str(target_dir),
        skills=["knowledge-base-kit-guide", "knowledge-base-ingest"],
        mode="copy",
    )

    assert result["platform"] == "custom"
    assert [item["action"] for item in result["skills"]] == ["installed", "installed"]
    assert (target_dir / "knowledge-base-kit-guide" / "SKILL.md").exists()
    assert (target_dir / "knowledge-base-ingest" / "agents" / "openai.yaml").exists()


def test_install_skills_dry_run_leaves_target_missing(fake_bundle: Path, tmp_path: Path) -> None:
    target_dir = tmp_path / "runtime-skills"

    result = core.install_skills(
        target_dir=str(target_dir),
        skills=["knowledge-base-audit"],
        mode="copy",
        dry_run=True,
    )

    assert result["skills"] == [
        {
            "skill": "knowledge-base-audit",
            "action": "dry-run-installed",
            "target": str(target_dir / "knowledge-base-audit"),
            "backup": None,
        }
    ]
    assert not target_dir.exists()


def test_verify_installation_reports_subset(fake_bundle: Path, tmp_path: Path) -> None:
    target_dir = tmp_path / "runtime-skills"
    core.install_skills(
        target_dir=str(target_dir),
        skills=["knowledge-base-ingest"],
        mode="copy",
    )

    result = core.verify_installation(
        target_dir=str(target_dir),
        skills=["knowledge-base-ingest"],
    )

    assert result["ok"] is True
    assert result["passed_count"] == 1
    assert result["failed_count"] == 0


def test_resolve_target_prefers_env_hint_when_multiple_platforms_exist(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    codex_dir = tmp_path / ".codex" / "skills"
    claude_dir = tmp_path / ".claude" / "skills"
    codex_dir.mkdir(parents=True)
    claude_dir.mkdir(parents=True)
    monkeypatch.setattr(
        core,
        "PLATFORM_DIRS",
        {
            "claude": claude_dir,
            "codex": codex_dir,
        },
    )
    monkeypatch.setenv("CODEX_HOME", str(tmp_path / ".codex"))

    assert core.resolve_target("auto", None) == ("codex", codex_dir)


def test_resolve_target_rejects_ambiguous_platforms_without_hint(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    codex_dir = tmp_path / ".codex" / "skills"
    claude_dir = tmp_path / ".claude" / "skills"
    codex_dir.mkdir(parents=True)
    claude_dir.mkdir(parents=True)
    monkeypatch.setattr(
        core,
        "PLATFORM_DIRS",
        {
            "claude": claude_dir,
            "codex": codex_dir,
        },
    )
    monkeypatch.delenv("CODEX_HOME", raising=False)
    monkeypatch.delenv("CLAUDE_CONFIG_DIR", raising=False)
    monkeypatch.delenv("CLAUDE_HOME", raising=False)
    monkeypatch.delenv("CLAUDE_PROJECT_DIR", raising=False)

    with pytest.raises(core.WikiKitError, match="Multiple supported skills directories were detected"):
        core.resolve_target("auto", None)
