#!/usr/bin/env python3
"""Tests for scripts/install_skills.py."""
import sys
from pathlib import Path

scripts_dir = Path(__file__).parent.parent / "scripts"
sys.path.insert(0, str(scripts_dir))

import pytest
from install_skills import InstallError, install_selected_skills, resolve_skill_names


@pytest.fixture()
def fake_repo(tmp_path):
    repo_root = tmp_path / "repo"
    skills_root = repo_root / "skills"
    skills_root.mkdir(parents=True)
    (skills_root / "catalog.toml").write_text(
        "\n".join(
            [
                "version = 1",
                "",
                "[package]",
                'name = "fake-kit"',
                "",
                "[[skills]]",
                "order = 1",
                'name = "knowledge-base-kit-guide"',
                'path = "skills/knowledge-base-kit-guide"',
                'area = "Onboarding / Orchestration"',
                'role = "Guide"',
                'role_en = "Guide"',
                "",
                "[[skills]]",
                "order = 2",
                'name = "knowledge-base-ingest"',
                'path = "skills/knowledge-base-ingest"',
                'area = "Ingest"',
                'role = "Ingest"',
                'role_en = "Ingest"',
                "",
                "[[skills]]",
                "order = 3",
                'name = "knowledge-base-audit"',
                'path = "skills/knowledge-base-audit"',
                'area = "Audit"',
                'role = "Audit"',
                'role_en = "Audit"',
                "",
            ]
        ),
        encoding="utf-8",
    )
    for name in [
        "knowledge-base-kit-guide",
        "knowledge-base-ingest",
        "knowledge-base-audit",
    ]:
        skill_dir = skills_root / name
        (skill_dir / "references").mkdir(parents=True)
        (skill_dir / "agents").mkdir(parents=True)
        (skill_dir / "SKILL.md").write_text(f"# {name}\n", encoding="utf-8")
        (skill_dir / "agents" / "openai.yaml").write_text("name: test\n", encoding="utf-8")
    return repo_root


def test_resolve_skill_names_defaults_to_requested_subset(fake_repo):
    names = resolve_skill_names(fake_repo, ["knowledge-base-ingest", "knowledge-base-audit"])
    assert names == ["knowledge-base-ingest", "knowledge-base-audit"]


def test_resolve_skill_names_rejects_unknown(fake_repo):
    with pytest.raises(InstallError):
        resolve_skill_names(fake_repo, ["missing-skill"])


def test_install_selected_skills_copy_mode(fake_repo, tmp_path):
    target_dir = tmp_path / "runtime-skills"
    results = install_selected_skills(
        repo_root=fake_repo,
        target_dir=target_dir,
        skill_names=["knowledge-base-kit-guide", "knowledge-base-ingest"],
        mode="copy",
        force=False,
    )

    assert results == {
        "knowledge-base-kit-guide": "copied",
        "knowledge-base-ingest": "copied",
    }
    assert (target_dir / "knowledge-base-kit-guide" / "SKILL.md").exists()
    assert (target_dir / "knowledge-base-ingest" / "agents" / "openai.yaml").exists()


def test_install_selected_skills_symlink_mode(fake_repo, tmp_path):
    target_dir = tmp_path / "runtime-skills"
    results = install_selected_skills(
        repo_root=fake_repo,
        target_dir=target_dir,
        skill_names=["knowledge-base-ingest"],
        mode="symlink",
        force=False,
    )

    installed = target_dir / "knowledge-base-ingest"
    assert results == {"knowledge-base-ingest": "symlinked"}
    assert installed.is_symlink()
    assert installed.resolve() == (fake_repo / "skills" / "knowledge-base-ingest").resolve()


def test_install_selected_skills_skips_existing_without_force(fake_repo, tmp_path):
    target_dir = tmp_path / "runtime-skills"
    target_dir.mkdir(parents=True)
    existing = target_dir / "knowledge-base-ingest"
    existing.mkdir()
    (existing / "old.txt").write_text("stale", encoding="utf-8")

    results = install_selected_skills(
        repo_root=fake_repo,
        target_dir=target_dir,
        skill_names=["knowledge-base-ingest"],
        mode="copy",
        force=False,
    )

    assert results == {"knowledge-base-ingest": "skipped"}
    assert (existing / "old.txt").read_text(encoding="utf-8") == "stale"


def test_install_selected_skills_force_replaces_existing(fake_repo, tmp_path):
    target_dir = tmp_path / "runtime-skills"
    target_dir.mkdir(parents=True)
    existing = target_dir / "knowledge-base-ingest"
    existing.mkdir()
    (existing / "old.txt").write_text("stale", encoding="utf-8")

    results = install_selected_skills(
        repo_root=fake_repo,
        target_dir=target_dir,
        skill_names=["knowledge-base-ingest"],
        mode="copy",
        force=True,
    )

    assert results == {"knowledge-base-ingest": "copied"}
    assert not (existing / "old.txt").exists()
    assert (existing / "SKILL.md").exists()
