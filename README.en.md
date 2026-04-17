# Wiki Knowledge Base Share Kit

[![Release](https://img.shields.io/github/v/release/zouxy111/wiki-knowledgebase-share-kit)](https://github.com/zouxy111/wiki-knowledgebase-share-kit/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](./LICENSE)
[![Repo](https://img.shields.io/badge/GitHub-zouxy111%2Fwiki--knowledgebase--share--kit-black?logo=github)](https://github.com/zouxy111/wiki-knowledgebase-share-kit)
[![Validate](https://github.com/zouxy111/wiki-knowledgebase-share-kit/actions/workflows/validate.yml/badge.svg)](https://github.com/zouxy111/wiki-knowledgebase-share-kit/actions/workflows/validate.yml)

An **8-skill knowledge-base package** for markdown / wiki / Obsidian-style vaults.  
The goal is not to record more process logs, but to keep a vault navigable, durable, and collaboration-friendly.

> **New here?** Start with [`START-HERE.md`](./START-HERE.md)

**Language / 语言**: [`English README`](./README.en.md) · [`中文 README`](./README.md)

## Quick links
- [`START-HERE.md`](./START-HERE.md): 5-minute onboarding
- [`GLOSSARY.md`](./GLOSSARY.md): core concepts
- [`templates/vault-profile-template.md`](./templates/vault-profile-template.md): primary vault profile template
- [`templates/working-profile-page-template.md`](./templates/working-profile-page-template.md): working-profile page template
- [`templates/journal-profile-template.md`](./templates/journal-profile-template.md): journal profile template
- [`docs/example-prompts.md`](./docs/example-prompts.md): copy-ready prompts
- [`docs/customization-guide.md`](./docs/customization-guide.md): adapt the package to your own vault
- [`examples/example-vault-profile-generic.md`](./examples/example-vault-profile-generic.md): generic profile example without personal paths
- [`examples/case-study-pathology-ingest-iteration.md`](./examples/case-study-pathology-ingest-iteration.md): test-driven ingest case study
- [`GitHub Pages`](https://zouxy111.github.io/wiki-knowledgebase-share-kit/): landing page
- [`Releases`](https://github.com/zouxy111/wiki-knowledgebase-share-kit/releases): published versions

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
| Content grows without stable entrypoints | Pages are discoverable from root pages or the reader entrypoint |
| Teammates do not know which workflow to use first | Onboarding and specialist skills provide clear routing |

In one sentence:

> This kit is not for recording more logs. It is for making a vault behave like a real knowledge base again.

---

## This is an 8-skill package

The current public package contains 8 skills:

1. `knowledge-base-kit-guide`
2. `knowledge-base-ingest`
3. `knowledge-base-maintenance`
4. `knowledge-base-audit`
5. `knowledge-base-orchestrator`
6. `knowledge-base-team-coordination`
7. `knowledge-base-working-profile`
8. `work-journal`

Those 8 skills cover **7 capability tracks**:

1. **Onboarding / Orchestration**
   - `knowledge-base-kit-guide`: installation, profile setup, skill routing
   - `knowledge-base-orchestrator`: low-friction initializer; detect existing setup, optionally install Obsidian, create a vault skeleton, generate a profile, and recommend the next skill
2. **Ingest**
   - `knowledge-base-ingest`: split long-form markdown sources and treat the first import as a testable baseline
3. **Maintenance**
   - `knowledge-base-maintenance`: write durable conclusions back into the vault
4. **Audit**
   - `knowledge-base-audit`: inspect structure, navigation, metadata, and noise regression
5. **Working profile**
   - `knowledge-base-working-profile`: distill stable collaboration preferences and boundaries
6. **Team coordination**
   - `knowledge-base-team-coordination`: handle questionnaires, alignment, assignment, and decision distillation for shared projects
7. **Work journal**
   - `work-journal`: daily work logs, meeting notes, temporary ideas, weekly distillation

---

## Best fit / not fit

### Best fit
- People already maintaining an Obsidian, markdown, or wiki vault
- Teams that want to separate durable knowledge from execution history
- Users who accept the fixed page-role model: `project / knowledge / ops / task / overview`
- Setups that also want stable collaboration memory, shared-project coordination, or work journaling

### Not a good fit
- People who do not want to configure a profile at all
- Log-first vaults that do not care about retrieval or governance
- Users who reject the fixed page-role model entirely
- Anyone expecting Orchestrator to be a fully autonomous all-purpose agent

---

## Platform status

| Platform | Status | Notes |
|---|---|---|
| Codex / ChatGPT Codex-style skill directories | Recommended | Repository includes 8 complete skill bundles with `SKILL.md`, `references/`, and `agents/openai.yaml` |
| Claude-style skill directories | Works | Copy the 8 skill folders directly |
| Other platforms supporting `SKILL.md` bundles | Maybe | Invocation and discovery may need adaptation |

---

## Repository layout
```text
wiki-knowledgebase-share-kit/
  START-HERE.md
  COVER-CN.md
  GLOSSARY.md
  README.md
  README.en.md
  docs/
  templates/
    vault-profile-template.md
    working-profile-page-template.md
    journal-profile-template.md
    member-capability-profile-template.md
    ingest-iteration-log-template.md
  examples/
    example-vault-profile-generic.md
    scenario-*.md
  skills/
    knowledge-base-kit-guide/
    knowledge-base-ingest/
    knowledge-base-maintenance/
    knowledge-base-audit/
    knowledge-base-orchestrator/
    knowledge-base-team-coordination/
    knowledge-base-working-profile/
    work-journal/
```

### About `examples/`
- `example-vault-profile*.md` and case studies are closer to real reuse
- `scenario-*.md` files are **scenario-only demonstrations**; some page links inside them are intentionally hypothetical and do not correspond to real repo files

---

## Recommended installation

Copy these 8 directories into your AI platform's `skills/` folder:

- `skills/knowledge-base-kit-guide`
- `skills/knowledge-base-ingest`
- `skills/knowledge-base-maintenance`
- `skills/knowledge-base-audit`
- `skills/knowledge-base-orchestrator`
- `skills/knowledge-base-team-coordination`
- `skills/knowledge-base-working-profile`
- `skills/work-journal`

Common locations:
- `~/.codex/skills`
- `~/.claude/skills`

Then prepare at least your `vault profile` before day-to-day use.

---

## Recommended usage order

### If you want the easiest start
- Start with `knowledge-base-orchestrator`
- It first checks whether you already have an existing Obsidian / vault / profile setup
- Optional Obsidian installation is exactly that: **optional**, not the core value of the repository
- After initialization, it routes you to the right next specialist skill

### If you want to understand the package first
- Start with `knowledge-base-kit-guide`
- It explains the profile, installation shape, and which skill to call next

### Day-to-day routing
- Long-form import: `knowledge-base-ingest`
- Durable task result: `knowledge-base-maintenance`
- Structural review: `knowledge-base-audit`
- Collaboration profile distillation: `knowledge-base-working-profile`
- Shared project coordination: `knowledge-base-team-coordination`
- Daily work notes / weekly summary: `work-journal`

---

## Fixed rules of the method
- knowledge-base-first, not process-log-first
- fixed page-role model: `project / knowledge / ops / task / overview`
- root pages are for navigation and stable overview
- `ops` pages default to symptom / root cause / fix / boundary
- milestone logs should not become task playback logs
- durable maintenance should update both content and navigation surfaces

---

## Read these first

Shortest path:
- `START-HERE.md`
- `GLOSSARY.md`
- `templates/vault-profile-template.md`
- `docs/example-prompts.md`
- `docs/usage-sop.md`

If you want to go deeper:
- `docs/customization-guide.md`
- `templates/working-profile-page-template.md`
- `templates/journal-profile-template.md`
- `templates/member-capability-profile-template.md`
- `examples/case-study-pathology-ingest-iteration.md`

## License
Released under the MIT License. See `/LICENSE`.
