# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

## [1.1.0] - 2026-04-17
### Added
- Added `knowledge-base-orchestrator` as an onboarding coordinator for low-friction setup, environment checks, vault skeleton creation, and initial profile generation.
- Added `knowledge-base-working-profile` for durable collaboration-profile distillation.
- Added `knowledge-base-team-coordination` for shared-project questionnaire, alignment, assignment, and decision-distill workflows.
- Added `work-journal` for daily work logs, meeting notes, and weekly distillation.
- Added template support around working profile, journaling, and reusable member-capability profiles.
- Added `SECURITY.md`, `CODE_OF_CONDUCT.md`, issue templates, and a pull request template for open-source collaboration hygiene.
- Added a bilingual GitHub Pages homepage with a scenario switcher and a copy-to-clone shortcut.

### Changed
- Reframed the repository as a public **8-skill package** with a consistent onboarding / orchestration, ingest, maintenance, audit, working-profile, team-coordination, and work-journal story.
- Updated `README.md`, `README.en.md`, `START-HERE.md`, `COVER-CN.md`, `docs/usage-sop.md`, `docs/example-prompts.md`, and `docs/index.html` so skill counts, installation steps, routing logic, and public positioning all match the current package.
- Tightened `GLOSSARY.md` and scenario docs so public docs no longer present misleading repo-internal dead links as if they were real files.
- Narrowed Orchestrator positioning from a “万能总控” narrative to an onboarding coordinator aligned with the actual scripts.
- Enhanced the HTML homepage with bilingual switching, translucent hero panels, scenario navigation, and a cyber brain-drive data-exchange visual.
- Added concise repository badges to `README.md` and `README.en.md`.

### Fixed
- Fixed Orchestrator-generated vault files so `updated` frontmatter now writes real dates instead of literal `$(date ...)` strings.
- Updated generated vault-profile next steps so they reflect the full 8-skill package instead of only maintenance / audit.

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
