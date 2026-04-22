from __future__ import annotations

import os
import re
import shutil
import sys
import sysconfig
from dataclasses import asdict, dataclass
from datetime import datetime
from pathlib import Path

PACKAGE_SHARE_NAME = "wiki-knowledgebase-share-kit"
PLATFORM_DIRS = {
    "kimi": Path.home() / ".kimi" / "skills",
    "claude": Path.home() / ".claude" / "skills",
    "codex": Path.home() / ".codex" / "skills",
    "agents": Path.home() / ".agents" / "skills",
}
AUTO_PLATFORM_HINTS = {
    "codex": ("CODEX_HOME", "CODEX_CONFIG_DIR"),
    "claude": ("CLAUDE_CONFIG_DIR", "CLAUDE_HOME", "CLAUDE_PROJECT_DIR"),
    "agents": ("AGENTS_HOME",),
    "kimi": ("KIMI_HOME",),
}
NAME_RE = re.compile(r"^name:\s*(.+?)\s*$", re.MULTILINE)
DESCRIPTION_RE = re.compile(r"^description:\s*", re.MULTILINE)


class WikiKitError(RuntimeError):
    pass


@dataclass
class PlatformCandidate:
    name: str
    path: str
    exists: bool


@dataclass
class InstallResult:
    skill: str
    action: str
    target: str
    backup: str | None = None


@dataclass
class VerifyResult:
    skill: str
    ok: bool
    issues: list[str]


def repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


def share_root_candidates() -> list[Path]:
    data_path = Path(sysconfig.get_path("data"))
    prefix_path = Path(sys.prefix)
    return [
        repo_root() / "skills",
        prefix_path / "share" / PACKAGE_SHARE_NAME / "skills",
        data_path / "share" / PACKAGE_SHARE_NAME / "skills",
    ]


def bundled_skills_root() -> Path:
    for candidate in share_root_candidates():
        if candidate.exists():
            return candidate
    raise WikiKitError(
        "Could not locate bundled skills. Expected either a repo checkout with "
        "`skills/` or an installed package data directory."
    )


def available_skills() -> list[str]:
    skills_root = bundled_skills_root()
    return sorted(path.name for path in skills_root.iterdir() if path.is_dir())


def resolve_skill_names(requested: list[str] | None) -> list[str]:
    names = requested or available_skills()
    available = set(available_skills())
    unknown = [name for name in names if name not in available]
    if unknown:
        raise WikiKitError(
            "Unknown skill(s): "
            + ", ".join(unknown)
            + ". Available: "
            + ", ".join(sorted(available))
        )
    return names


def detect_platforms() -> list[PlatformCandidate]:
    return [
        PlatformCandidate(name=name, path=str(path), exists=path.exists())
        for name, path in PLATFORM_DIRS.items()
    ]


def hinted_platforms() -> list[str]:
    return [
        name
        for name, env_names in AUTO_PLATFORM_HINTS.items()
        if any(os.environ.get(env_name) for env_name in env_names)
    ]


def auto_detect_target() -> tuple[str, Path] | None:
    candidates = [item for item in detect_platforms() if item.exists]
    if not candidates:
        return None

    hinted_names = set(hinted_platforms())
    hinted_candidates = [item for item in candidates if item.name in hinted_names]

    if len(hinted_candidates) == 1:
        selected = hinted_candidates[0]
        return selected.name, Path(selected.path)

    if len(candidates) == 1:
        selected = candidates[0]
        return selected.name, Path(selected.path)

    candidate_summary = ", ".join(f"{item.name} ({item.path})" for item in candidates)
    raise WikiKitError(
        "Multiple supported skills directories were detected: "
        + candidate_summary
        + ". Use --platform <kimi|claude|codex|agents> or --target-dir to choose the install target explicitly."
    )


def detection_report() -> dict:
    candidates = [asdict(item) for item in detect_platforms()]
    try:
        detected_name, detected_path = resolve_target("auto", None)
        detected = {"name": detected_name, "path": str(detected_path)}
        error = None
    except WikiKitError as exc:
        detected = None
        error = str(exc)
    return {
        "detected": detected,
        "candidates": candidates,
        "env_hints": hinted_platforms(),
        "error": error,
    }


def resolve_target(platform: str | None, target_dir: str | None) -> tuple[str, Path]:
    if platform and platform != "auto" and target_dir:
        raise WikiKitError("Use either --platform or --target-dir, not both.")
    if target_dir:
        return "custom", Path(target_dir).expanduser()
    if platform and platform != "auto":
        return platform, PLATFORM_DIRS[platform]
    detected = auto_detect_target()
    if detected:
        return detected
    raise WikiKitError(
        "No supported skills directory was auto-detected. Use --target-dir or "
        "--platform <kimi|claude|codex|agents>."
    )


def resolve_real_path(path: Path) -> Path:
    try:
        return path.resolve(strict=False)
    except OSError:
        return path


def is_same_target(source: Path, target: Path) -> bool:
    return resolve_real_path(source) == resolve_real_path(target)


def remove_existing(path: Path) -> None:
    if path.is_symlink() or path.is_file():
        path.unlink()
    elif path.exists():
        shutil.rmtree(path)


def timestamp() -> str:
    return datetime.now().strftime("%Y%m%d_%H%M%S")


def install_skills(
    *,
    platform: str | None = None,
    target_dir: str | None = None,
    mode: str = "copy",
    force: bool = False,
    backup: bool = False,
    dry_run: bool = False,
    skills: list[str] | None = None,
) -> dict:
    resolved_platform, resolved_target = resolve_target(platform, target_dir)
    names = resolve_skill_names(skills)
    source_root = bundled_skills_root()
    results: list[InstallResult] = []

    if not dry_run:
        resolved_target.mkdir(parents=True, exist_ok=True)

    for name in names:
        source = source_root / name
        target = resolved_target / name
        backup_path: str | None = None
        action = "installed"

        if target.is_symlink() and is_same_target(source, target):
            action = "skipped"
        elif target.exists() or target.is_symlink():
            if backup:
                backup_target = resolved_target / f"{name}.backup.{timestamp()}"
                backup_path = str(backup_target)
                action = "backed-up-and-installed"
                if not dry_run:
                    shutil.move(str(target), str(backup_target))
            elif force:
                action = "replaced"
                if not dry_run:
                    remove_existing(target)
            else:
                action = "skipped"

        if action != "skipped":
            if mode == "symlink":
                if dry_run:
                    action = f"dry-run-{action}"
                else:
                    os.symlink(source, target, target_is_directory=True)
            else:
                if dry_run:
                    action = f"dry-run-{action}"
                else:
                    if target.exists() or target.is_symlink():
                        remove_existing(target)
                    shutil.copytree(source, target)
        results.append(
            InstallResult(
                skill=name,
                action=action,
                target=str(target),
                backup=backup_path,
            )
        )

    return {
        "platform": resolved_platform,
        "target_dir": str(resolved_target),
        "mode": mode,
        "dry_run": dry_run,
        "skills": [asdict(item) for item in results],
    }


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def verify_skill_dir(skill_dir: Path, skill_name: str) -> VerifyResult:
    issues: list[str] = []
    skill_md = skill_dir / "SKILL.md"
    agents_yaml = skill_dir / "agents" / "openai.yaml"
    references_dir = skill_dir / "references"

    if not skill_dir.is_dir():
        issues.append("directory missing")
        return VerifyResult(skill=skill_name, ok=False, issues=issues)

    if not skill_md.is_file():
        issues.append("SKILL.md missing")
    else:
        skill_text = read_text(skill_md)
        name_match = NAME_RE.search(skill_text)
        if not name_match:
            issues.append("SKILL.md missing name frontmatter")
        elif name_match.group(1).strip().strip('"\'') != skill_name:
            issues.append("SKILL.md name frontmatter does not match directory name")
        if not DESCRIPTION_RE.search(skill_text):
            issues.append("SKILL.md missing description frontmatter")

    if not agents_yaml.is_file():
        issues.append("agents/openai.yaml missing")
    if not references_dir.is_dir():
        issues.append("references/ missing")
    elif not any(references_dir.iterdir()):
        issues.append("references/ is empty")

    return VerifyResult(skill=skill_name, ok=not issues, issues=issues)


def verify_installation(
    *,
    platform: str | None = None,
    target_dir: str | None = None,
    skills: list[str] | None = None,
) -> dict:
    resolved_platform, resolved_target = resolve_target(platform, target_dir)
    names = resolve_skill_names(skills)
    results = [verify_skill_dir(resolved_target / name, name) for name in names]
    passed = [item.skill for item in results if item.ok]
    failed = [asdict(item) for item in results if not item.ok]
    return {
        "platform": resolved_platform,
        "target_dir": str(resolved_target),
        "expected_skills": names,
        "passed_count": len(passed),
        "failed_count": len(failed),
        "ok": not failed,
        "results": [asdict(item) for item in results],
    }
