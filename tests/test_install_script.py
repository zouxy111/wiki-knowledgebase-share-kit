#!/usr/bin/env python3
"""Regression tests for install.sh."""

from __future__ import annotations

import os
import subprocess
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
INSTALL_SCRIPT = REPO_ROOT / "install.sh"


def run_install_script(*args: str, env: dict[str, str] | None = None) -> subprocess.CompletedProcess[str]:
    merged_env = os.environ.copy()
    if env:
        merged_env.update(env)
    return subprocess.run(
        ["bash", str(INSTALL_SCRIPT), *args],
        cwd=REPO_ROOT,
        env=merged_env,
        text=True,
        capture_output=True,
        check=True,
    )


def test_install_script_preserves_requested_nested_target_path(tmp_path: Path) -> None:
    nested_target = tmp_path / "a" / "b" / "skills"

    result = run_install_script("--dry-run", str(nested_target))

    assert f"Using specified directory: {nested_target}" in result.stdout
    assert "Would create directory: /skills" not in result.stdout
    assert f"Would create directory: {nested_target}" in result.stdout


def test_install_script_skips_same_source_symlink_without_overwrite(tmp_path: Path) -> None:
    target_dir = tmp_path / "runtime-skills"
    target_dir.mkdir()

    source_skill = (REPO_ROOT / "skills" / "knowledge-base-kit-guide").resolve()
    (target_dir / "knowledge-base-kit-guide").symlink_to(source_skill, target_is_directory=True)

    result = run_install_script("--dry-run", str(target_dir))

    assert "knowledge-base-kit-guide is already a symlink to source — skipping" in result.stdout
    assert f"Would overwrite: {target_dir / 'knowledge-base-kit-guide'}" not in result.stdout
    assert f"Would copy: {source_skill} → {target_dir / 'knowledge-base-kit-guide'}" not in result.stdout
    assert "1 skills are already linked to source and would be skipped." in result.stdout
