from __future__ import annotations

import argparse
import json
import shlex
import sys

from wiki_knowledgebase_share_kit import __version__
from wiki_knowledgebase_share_kit.core import (
    PLATFORM_DIRS,
    WikiKitError,
    available_skills,
    detection_report,
    install_skills,
    verify_installation,
)


def emit(payload, *, as_json: bool) -> None:
    if as_json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return
    if isinstance(payload, str):
        print(payload)
        return
    print(json.dumps(payload, ensure_ascii=False, indent=2))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="wiki-kit",
        description="CLI helper for installing and validating the Wiki Knowledge Base Share Kit.",
    )
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    subparsers = parser.add_subparsers(dest="command")

    detect_parser = subparsers.add_parser("detect", help="Show supported platform paths and auto-detect status.")
    detect_parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON.")

    list_parser = subparsers.add_parser("list-skills", help="List bundled skills currently available in this checkout or installed package.")
    list_parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON.")

    install_parser = subparsers.add_parser("install", help="Install bundled skills into a runtime skills directory.")
    install_parser.add_argument("--platform", choices=["auto", *PLATFORM_DIRS], default="auto")
    install_parser.add_argument("--target-dir", help="Explicit target skills directory.")
    install_parser.add_argument("legacy_target_dir", nargs="?", help="Legacy positional alias for --target-dir.")
    install_parser.add_argument("--mode", choices=["copy", "symlink"], default="copy")
    install_parser.add_argument("--force", action="store_true", help="Replace existing installed skills.")
    install_parser.add_argument("-b", "--backup", action="store_true", help="Backup existing installed skills before replacing them.")
    install_parser.add_argument("-d", "--dry-run", action="store_true", help="Preview actions without writing files.")
    install_parser.add_argument("--skills", nargs="+", help="Optional subset of skill names to install.")
    install_parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON.")

    verify_parser = subparsers.add_parser("verify", help="Verify that expected skills are installed correctly.")
    verify_parser.add_argument("--platform", choices=["auto", *PLATFORM_DIRS], default="auto")
    verify_parser.add_argument("--target-dir", help="Explicit target skills directory.")
    verify_parser.add_argument("legacy_target_dir", nargs="?", help="Legacy positional alias for --target-dir.")
    verify_parser.add_argument("--skills", nargs="+", help="Optional subset of skill names to verify.")
    verify_parser.add_argument("-v", "--verbose", action="store_true", help="Show every skill result, not only failures.")
    verify_parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON.")

    return parser


def format_detect(as_json: bool) -> int:
    payload = detection_report()
    if as_json:
        emit(payload, as_json=True)
        return 0
    if payload["env_hints"]:
        print("Environment hints: " + ", ".join(payload["env_hints"]))
    detected = payload["detected"]
    if detected:
        print(f"Auto-detected: {detected['name']} -> {detected['path']}")
    else:
        print("Auto-detected: none")
        if payload["error"]:
            print(f"Reason: {payload['error']}")
    print("Candidates:")
    for item in payload["candidates"]:
        status = "present" if item["exists"] else "missing"
        print(f"- {item['name']}: {item['path']} ({status})")
    return 0


def format_list_skills(as_json: bool) -> int:
    names = available_skills()
    payload = {"count": len(names), "skills": names}
    if as_json:
        emit(payload, as_json=True)
        return 0
    print(f"Bundled skills ({len(names)}):")
    for name in names:
        print(f"- {name}")
    return 0


def pick_target_dir(args) -> str | None:
    if getattr(args, "target_dir", None) and getattr(args, "legacy_target_dir", None):
        raise WikiKitError("Use either --target-dir or the positional target directory, not both.")
    return args.target_dir or getattr(args, "legacy_target_dir", None)


def format_install(args) -> int:
    result = install_skills(
        platform=args.platform,
        target_dir=pick_target_dir(args),
        mode=args.mode,
        force=args.force,
        backup=args.backup,
        dry_run=args.dry_run,
        skills=args.skills,
    )
    if args.json:
        emit(result, as_json=True)
        return 0
    print(f"Target platform: {result['platform']}")
    print(f"Target directory: {result['target_dir']}")
    print(f"Mode: {result['mode']}")
    if result["dry_run"]:
        print("Dry run: true")
    print("Results:")
    for item in result["skills"]:
        suffix = f" (backup: {item['backup']})" if item.get("backup") else ""
        print(f"- {item['skill']}: {item['action']}{suffix}")
    print("Next steps:")
    print("1. Re-open the runtime session so it rescans installed skills.")
    print("2. Run `wiki-kit verify` if you want a structural check.")
    return 0


def format_verify(args) -> int:
    result = verify_installation(
        platform=args.platform,
        target_dir=pick_target_dir(args),
        skills=args.skills,
    )
    if args.json:
        emit(result, as_json=True)
        return 0 if result["ok"] else 1
    print(f"Target platform: {result['platform']}")
    print(f"Target directory: {result['target_dir']}")
    print(f"Passed: {result['passed_count']}")
    print(f"Failed: {result['failed_count']}")
    if args.verbose:
        print("Results:")
        for item in result["results"]:
            status = "ok" if item["ok"] else "failed"
            detail = "OK" if item["ok"] else "; ".join(item["issues"])
            print(f"- {item['skill']} [{status}]: {detail}")
    if result["ok"]:
        print("Verification passed.")
        return 0
    if not args.verbose:
        print("Failures:")
        for item in result["results"]:
            if item["ok"]:
                continue
            print(f"- {item['skill']}: " + "; ".join(item["issues"]))
    return 1


def dispatch(args) -> int:
    if args.command == "detect":
        return format_detect(args.json)
    if args.command == "list-skills":
        return format_list_skills(args.json)
    if args.command == "install":
        return format_install(args)
    if args.command == "verify":
        return format_verify(args)
    return 0


def repl(parser: argparse.ArgumentParser) -> int:
    print("wiki-kit interactive mode")
    print("Type `help` for commands, `exit` to quit.")
    while True:
        try:
            line = input("wiki-kit> ").strip()
        except EOFError:
            print()
            return 0
        except KeyboardInterrupt:
            print()
            continue
        if not line:
            continue
        if line in {"exit", "quit"}:
            return 0
        if line == "help":
            parser.print_help()
            continue
        try:
            args = parser.parse_args(shlex.split(line))
            if not args.command:
                parser.print_help()
                continue
            code = dispatch(args)
            if code:
                print(f"(exit {code})")
        except SystemExit:
            continue
        except WikiKitError as exc:
            print(f"Error: {exc}", file=sys.stderr)


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    argv = list(argv) if argv is not None else sys.argv[1:]

    if not argv:
        if sys.stdin.isatty():
            return repl(parser)
        parser.print_help()
        return 0

    try:
        args = parser.parse_args(argv)
        if not args.command:
            parser.print_help()
            return 0
        return dispatch(args)
    except WikiKitError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
