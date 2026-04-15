# Wiki Knowledge Base Share Kit

[![Release](https://img.shields.io/github/v/release/zouxy111/wiki-knowledgebase-share-kit)](https://github.com/zouxy111/wiki-knowledgebase-share-kit/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](./LICENSE)
[![Repo](https://img.shields.io/badge/GitHub-zouxy111%2Fwiki--knowledgebase--share--kit-black?logo=github)](https://github.com/zouxy111/wiki-knowledgebase-share-kit)

A reusable skill-and-docs kit for keeping markdown/wiki vaults structured, durable, and knowledge-base-first.

**Language / 语言**: [`English README`](./README.en.md) · [`中文 README`](./README.md)

## Quick links
- [`START-HERE.md`](./START-HERE.md): shortest onboarding path
- [`COVER-CN.md`](./COVER-CN.md): Chinese cover page for forwarding the project
- [`templates/vault-profile-template.md`](./templates/vault-profile-template.md): configure your own vault profile
- [`docs/customization-guide.md`](./docs/customization-guide.md): adapt the kit to your own vault
- [`docs/example-prompts.md`](./docs/example-prompts.md): copy-ready prompts
- [`Releases`](https://github.com/zouxy111/wiki-knowledgebase-share-kit/releases): download published versions

---
## What this project does
Many markdown or Obsidian-style vaults eventually drift into a mix of task logs, navigation notes, and unstable process history. This kit separates that problem into two repeatable workflows:

1. **Maintenance** — integrate durable conclusions into a vault
2. **Audit** — inspect vault structure, metadata, navigation coverage, and noise regression

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
  skills/
    knowledge-base-kit-guide/
    knowledge-base-maintenance/
    knowledge-base-audit/
```

## Quick start
1. Read `/START-HERE.md`
2. Copy `templates/vault-profile-template.md` and fill it for your own vault
3. Install the three skill directories into your AI platform's `skills/` folder
4. Start with `knowledge-base-kit-guide`

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

## Language
The main docs are currently Chinese-first, with English prompts and this English summary for broader reuse.

## License
Released under the MIT License. See `/LICENSE`.
