#!/usr/bin/env python3
"""Regression tests for legacy installer and verifier entrypoints."""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
INSTALL_SCRIPT = REPO_ROOT / "install.sh"
VERIFY_SCRIPT = REPO_ROOT / "verify-installation.sh"
INSTALL_PY = REPO_ROOT / "scripts" / "install_skills.py"


def run_command(
    *args: str, env: dict[str, str] | None = None
) -> subprocess.CompletedProcess[str]:
    merged_env = os.environ.copy()
    if env:
        merged_env.update(env)
    return subprocess.run(
        list(args),
        cwd=REPO_ROOT,
        env=merged_env,
        text=True,
        capture_output=True,
        check=True,
    )


def test_install_script_supports_legacy_positional_target_dir(tmp_path: Path) -> None:
    nested_target = tmp_path / "a" / "b" / "skills"

    result = run_command("bash", str(INSTALL_SCRIPT), "--dry-run", str(nested_target))

    assert f"Target directory: {nested_target}" in result.stdout
    assert "Dry run: true" in result.stdout
    assert not nested_target.exists()


def test_verify_script_supports_legacy_positional_target_dir(tmp_path: Path) -> None:
    target_dir = tmp_path / "runtime-skills"
    run_command(
        sys.executable,
        "-m",
        "wiki_knowledgebase_share_kit",
        "install",
        "--target-dir",
        str(target_dir),
        "--skills",
        "work-journal",
    )

    result = run_command(
        "bash",
        str(VERIFY_SCRIPT),
        str(target_dir),
        "--skills",
        "work-journal",
    )

    assert f"Target directory: {target_dir}" in result.stdout
    assert "Verification passed." in result.stdout


def test_install_skills_wrapper_uses_same_cli_backend(tmp_path: Path) -> None:
    target_dir = tmp_path / "runtime-skills"

    result = run_command(
        sys.executable,
        str(INSTALL_PY),
        "--dry-run",
        str(target_dir),
        "--skills",
        "knowledge-base-kit-guide",
    )

    assert f"Target directory: {target_dir}" in result.stdout
    assert "knowledge-base-kit-guide: dry-run-installed" in result.stdout
