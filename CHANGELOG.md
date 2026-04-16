# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]
### Added
- Added a new `knowledge-base-ingest` skill for splitting long markdown sources or books into reusable knowledge-base pages.
- Added a test-driven ingest case study for long-form professional markdown sources at `examples/case-study-pathology-ingest-iteration.md`.
- Added a deterministic heading-based splitter at `skills/knowledge-base-ingest/scripts/split_markdown.py`.
- Added glossary extraction and related-link suggestion scripts for `knowledge-base-ingest`.
- Generic example vault profile without personal local paths at `examples/example-vault-profile-generic.md`.
- Basic GitHub Actions validation workflow for skill bundle structure and relative links.
- Developer list updated to `邹星宇` and `杨琦` in the main repository surfaces.

### Changed
- Improved Chinese and English README files with a 30-second overview, platform status, clearer audience fit guidance, and test-driven ingest case-study links.
- Updated example prompts, usage SOP, and the GitHub Pages landing page to emphasize baseline import, regression checks, and iterative knowledge-architecture refinement.

## [1.0.1] - 2026-04-16
### Added
- GitHub Pages landing page at `docs/index.html`.
- Social/share preview asset at `docs/assets/social-preview.png`.

### Changed
- Polished Chinese and English README files with release badges, bilingual navigation, and quick links.
- Prepared the repository for a patch release with a downloadable packaged asset.

## [1.0.0] - 2026-04-16
### Added
- Initial open-source release of the wiki knowledge-base share kit.
- Three installable skills: `knowledge-base-kit-guide`, `knowledge-base-maintenance`, and `knowledge-base-audit`.
- Platform-agnostic docs, prompt examples, and a configurable vault profile template.
- Example profile and case study showing how the methodology can be applied to a real vault.
- Chinese cover page plus ASCII alias for safer cross-platform file handling.
- Open-source repository metadata: `LICENSE`, `CONTRIBUTING.md`, and `README.en.md`.
