# Wiki Knowledge Base Share Kit

[![Release](https://img.shields.io/github/v/release/zouxy111/wiki-knowledgebase-share-kit)](https://github.com/zouxy111/wiki-knowledgebase-share-kit/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](./LICENSE)
[![Repo](https://img.shields.io/badge/GitHub-zouxy111%2Fwiki--knowledgebase--share--kit-black?logo=github)](https://github.com/zouxy111/wiki-knowledgebase-share-kit)
[![Validate](https://github.com/zouxy111/wiki-knowledgebase-share-kit/actions/workflows/validate.yml/badge.svg)](https://github.com/zouxy111/wiki-knowledgebase-share-kit/actions/workflows/validate.yml)

A reusable skill-and-docs kit for keeping markdown/wiki vaults structured, durable, and knowledge-base-first.

**Language / 语言**: [`English README`](./README.en.md) · [`中文 README`](./README.md)

## Quick links
- [`START-HERE.md`](./START-HERE.md): shortest onboarding path
- [`COVER-CN.md`](./COVER-CN.md): Chinese cover page for forwarding the project
- [`templates/vault-profile-template.md`](./templates/vault-profile-template.md): configure your own vault profile
- [`examples/example-vault-profile-generic.md`](./examples/example-vault-profile-generic.md): generic profile example without personal paths
- [`docs/customization-guide.md`](./docs/customization-guide.md): adapt the kit to your own vault
- [`docs/example-prompts.md`](./docs/example-prompts.md): copy-ready prompts
- [`examples/case-study-pathology-ingest-iteration.md`](./examples/case-study-pathology-ingest-iteration.md): test-driven ingest case study
- [`Releases`](https://github.com/zouxy111/wiki-knowledgebase-share-kit/releases): download published versions
- [`GitHub Pages`](https://zouxy111.github.io/wiki-knowledgebase-share-kit/): browse the landing page

---

## Developers

- 邹星宇
- 杨琦

---

![Share kit preview](./docs/assets/social-preview.png)

## 30-second overview

| Typical drifting vault | Target state after adopting this kit |
|---|---|
| Root pages accumulate temporary execution history | Root pages return to navigation, stable boundaries, and topic entrypoints |
| `ops` pages become chronological logs | `ops` pages become reusable symptom / root cause / fix / boundary references |
| `log.md` turns into task replay | `log.md` stays milestone-only |
| Content exists without stable entrypoints | Pages are discoverable from root pages or the reader entrypoint |
| Review work starts from prose instead of structure | Audit starts from metadata, navigation, dead links, boundary drift, and noise regression |

In one sentence:

> This kit is not for recording more logs. It is for making a vault behave like a real knowledge base again.

## What this project does
Many markdown or Obsidian-style vaults eventually drift into a mix of task logs, navigation notes, and unstable process history. This kit separates that problem into two repeatable workflows:

1. **Ingest** — split long markdown sources or books, generate TOC / glossary candidates / related-link suggestions, and import them as reusable knowledge-base pages
   - The first import is treated as a **testable baseline**, then refined through testing, regression checks, and version comparison
2. **Maintenance** — integrate durable conclusions into a vault
3. **Audit** — inspect vault structure, metadata, navigation coverage, and noise regression

The kit keeps a fixed page-role model:
- `project`
- `knowledge`
- `ops`
- `task`
- `overview`

But leaves these pieces configurable through a vault profile:
- vault root
- pages directory
- reader entrypoint
- milestone log
- area list
- root pages
- naming conventions
- frontmatter rules

## Best fit / not fit

### Best fit
- People already maintaining an Obsidian, markdown, or wiki vault
- Teams that want to separate durable knowledge from execution history
- Users who accept the fixed page-role model
- Anyone who wants maintenance and audit as two explicit loops

### Not a good fit
- People who do not want to configure a profile at all
- Vaults meant to stay log-first
- Users who reject the fixed page-role model
- Setups that only care about raw process capture, not durable retrieval or navigation

## Case studies

- [`examples/case-study-current-vault.md`](./examples/case-study-current-vault.md): what should be abstracted from a real vault before sharing it
- [`examples/case-study-pathology-ingest-iteration.md`](./examples/case-study-pathology-ingest-iteration.md): how a long-form professional markdown source is imported, tested, refactored, and stabilized as a knowledge-base structure

## Platform status

| Platform | Status | Notes |
|---|---|---|
| Codex / ChatGPT Codex-style skill directories | Recommended | Repository includes `SKILL.md`, `references/`, and `agents/openai.yaml` |
| Claude-style skill directories | Works | Copy the four skill folders directly |
| Other platforms supporting `SKILL.md` bundles | Maybe | Invocation and discovery may need adaptation |

## Repository layout
```text
wiki-knowledgebase-share-kit/
  START-HERE.md
  COVER-CN.md
  README.md
  README.en.md
  docs/
  templates/
  examples/
    example-vault-profile-generic.md
  skills/
    knowledge-base-kit-guide/
    knowledge-base-ingest/
    knowledge-base-maintenance/
    knowledge-base-audit/
```

## Quick start
1. Read `/START-HERE.md`
2. Copy `templates/vault-profile-template.md` and fill it for your own vault
3. Review `examples/example-vault-profile-generic.md`
4. Install the four skill directories into your AI platform's `skills/` folder
5. Start with `knowledge-base-kit-guide`
6. Review `examples/case-study-pathology-ingest-iteration.md` for a test-driven ingest example

## Principles
- knowledge-base-first, not process-log-first
- root pages are for navigation and stable overview
- `ops` pages default to symptom / root cause / fix / boundary
- milestone logs should not become task playback logs
- maintenance should sync both content and navigation surfaces

## Open-source files
- `LICENSE` — MIT
- `CONTRIBUTING.md` — contribution guidance
- `CHANGELOG.md` — release history
- `.github/workflows/validate.yml` — basic repo validation

## Language
The main docs are currently Chinese-first, with English prompts and this English summary for broader reuse.

## License
Released under the MIT License. See `/LICENSE`.
