# Wiki Knowledge Base Share Kit

A reusable skill-and-docs kit for keeping markdown/wiki vaults structured, durable, and knowledge-base-first.

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
