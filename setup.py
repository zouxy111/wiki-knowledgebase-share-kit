from __future__ import annotations

from pathlib import Path

from setuptools import find_packages, setup

ROOT = Path(__file__).resolve().parent
PACKAGE_NAME = "wiki-knowledgebase-share-kit"


def build_data_files() -> list[tuple[str, list[str]]]:
    grouped: dict[str, list[str]] = {}
    for path in sorted((ROOT / "skills").rglob("*")):
        if not path.is_file():
            continue
        target_dir = Path("share") / PACKAGE_NAME / path.parent.relative_to(ROOT)
        grouped.setdefault(target_dir.as_posix(), []).append(path.relative_to(ROOT).as_posix())
    return sorted(grouped.items())


setup(
    name=PACKAGE_NAME,
    version="0.1.0",
    description="CLI and install helpers for the Wiki Knowledge Base Share Kit.",
    long_description=(ROOT / "README.en.md").read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",
    author="zouxy111",
    license="MIT",
    python_requires=">=3.10",
    packages=find_packages(include=["wiki_knowledgebase_share_kit*"]),
    include_package_data=True,
    data_files=build_data_files(),
    entry_points={
        "console_scripts": [
            "wiki-kit=wiki_knowledgebase_share_kit.cli:main",
        ]
    },
)
