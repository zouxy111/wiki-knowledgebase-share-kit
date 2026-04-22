#!/usr/bin/env python3
"""Install share-kit skills into a runtime skills directory.

Usage examples:
    python3 scripts/install_skills.py --platform codex --force
    python3 scripts/install_skills.py --platform claude --mode copy --force
    python3 scripts/install_skills.py --target-dir /path/to/skills --skills knowledge-base-ingest knowledge-base-audit
"""

from __future__ import annotations

import argparse
import os
import shutil
import sys
from pathlib import Path
from typing import Iterable

DEFAULT_SKILLS = [
    "knowledge-base-kit-guide",
    "knowledge-base-orchestrator",
    "knowledge-base-ingest",
    "knowledge-base-maintenance",
    "knowledge-base-audit",
    "knowledge-base-project-management",
    "knowledge-base-team-coordination",
    "knowledge-base-delivery-audit",
    "knowledge-base-working-profile",
    "work-journal",
]

PLATFORM_DIRS = {
    "codex": Path.home() / ".codex" / "skills",
    "claude": Path.home() / ".claude" / "skills",
}

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILLS_ROOT = REPO_ROOT / "skills"


class InstallError(RuntimeError):
    """Raised when skill installation cannot continue."""


def available_skills(repo_root: Path) -> list[str]:
    skills_root = repo_root / "skills"
    if not skills_root.exists():
        raise InstallError(f"Skills directory not found: {skills_root}")
    return sorted(path.name for path in skills_root.iterdir() if path.is_dir())


def resolve_skill_names(repo_root: Path, requested: Iterable[str] | None) -> list[str]:
    available = set(available_skills(repo_root))
    names = list(requested) if requested else list(DEFAULT_SKILLS)
    unknown = [name for name in names if name not in available]
    if unknown:
        known = ", ".join(sorted(available))
        raise InstallError(
            "Unknown skill(s): "
            + ", ".join(unknown)
            + f"\nAvailable skills: {known}"
        )
    return names


def resolve_target_dir(platform: str | None, target_dir: str | None) -> Path:
    if platform and target_dir:
        raise InstallError("Use either --platform or --target-dir, not both.")
    if platform:
        return PLATFORM_DIRS[platform]
    if target_dir:
        return Path(target_dir).expanduser().resolve()
    raise InstallError("You must provide --platform or --target-dir.")


def remove_existing(path: Path) -> None:
    if path.is_symlink() or path.is_file():
        path.unlink()
    elif path.exists():
        shutil.rmtree(path)


def install_one(source: Path, target: Path, mode: str, force: bool) -> str:
    if target.exists() or target.is_symlink():
        if not force:
            return "skipped"
        remove_existing(target)

    if mode == "symlink":
        try:
            os.symlink(source, target, target_is_directory=True)
        except OSError as exc:
            raise InstallError(
                f"Failed to symlink {source} -> {target}: {exc}. "
                "Retry with --mode copy if your platform blocks symlinks."
            ) from exc
        return "symlinked"

    shutil.copytree(source, target)
    return "copied"


def install_selected_skills(
    repo_root: Path,
    target_dir: Path,
    skill_names: Iterable[str] | None,
    mode: str = "symlink",
    force: bool = False,
) -> dict[str, str]:
    names = resolve_skill_names(repo_root, skill_names)
    target_dir.mkdir(parents=True, exist_ok=True)

    results: dict[str, str] = {}
    for name in names:
        source = (repo_root / "skills" / name).resolve()
        target = target_dir / name
        results[name] = install_one(source, target, mode=mode, force=force)
    return results


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Install share-kit skills into Codex, Claude Code, or another compatible skills directory."
    )
    parser.add_argument(
        "--platform",
        choices=sorted(PLATFORM_DIRS),
        help="Known runtime to install into (codex or claude).",
    )
    parser.add_argument(
        "--target-dir",
        help="Custom skills directory. Use this when your runtime does not use ~/.codex/skills or ~/.claude/skills.",
    )
    parser.add_argument(
        "--mode",
        choices=("symlink", "copy"),
        default="symlink",
        help="Install mode. symlink keeps the runtime pointed at this repo; copy creates a standalone snapshot.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Replace an existing installed skill directory instead of skipping it.",
    )
    parser.add_argument(
        "--skills",
        nargs="+",
        help="Optional subset of skills to install. Defaults to the full 10-skill package.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        target_dir = resolve_target_dir(args.platform, args.target_dir)
        results = install_selected_skills(
            repo_root=REPO_ROOT,
            target_dir=target_dir,
            skill_names=args.skills,
            mode=args.mode,
            force=args.force,
        )
    except InstallError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    print(f"Installed share-kit skills into: {target_dir}")
    print(f"Mode: {args.mode}")
    print()
    for name, status in results.items():
        print(f"- {name}: {status}")

    print()
    print("Next steps:")
    print("1. Re-open or restart your AI runtime so it rescans installed skills.")
    print("2. Verify the runtime now lists the installed skill names.")
    print("3. If it still says 'Skill not found', confirm you installed into the same runtime you are actually using.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
