#!/usr/bin/env python3
"""Compatibility wrapper for the new wiki-kit CLI install command."""

from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from wiki_knowledgebase_share_kit.cli import main  # noqa: E402

if __name__ == "__main__":
    raise SystemExit(main(["install", *sys.argv[1:]]))
