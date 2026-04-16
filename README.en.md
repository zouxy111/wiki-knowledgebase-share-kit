# Wiki Knowledge Base Share Kit

A reusable open-source kit for **long-form ingest, knowledge-base maintenance, audit, and multi-person project coordination** on top of markdown/wiki workflows.

**Language / 语言**: [`English README`](./README.en.md) · [`中文 README`](./README.md)

## Quick links
- [`START-HERE.md`](./START-HERE.md): shortest onboarding path
- [`docs/reuse-from-zero.md`](./docs/reuse-from-zero.md): zero-context reuse path for someone who does not know this project yet
- [`docs/team-coordination-workflow.md`](./docs/team-coordination-workflow.md): the multi-person questionnaire / assignment / distillation workflow
- [`docs/collaboration-integration-patterns.md`](./docs/collaboration-integration-patterns.md): recommended OpenClaw / Hermes / NAS / shared-wiki collaboration patterns
- [`docs/ingest-evaluation-rubric.md`](./docs/ingest-evaluation-rubric.md): candidate-vs-baseline promotion rubric for ingest iterations
- [`templates/vault-profile-template.md`](./templates/vault-profile-template.md): configure your own vault profile
- [`templates/member-capability-profile-template.md`](./templates/member-capability-profile-template.md): reusable cross-project member capability profile
- [`templates/team-project-workspace/`](./templates/team-project-workspace/): shared project directory template
- [`templates/ingest-iteration-log-template.md`](./templates/ingest-iteration-log-template.md): iteration log for ingest baseline / candidate / regression / decision
- [`docs/customization-guide.md`](./docs/customization-guide.md): adapt the kit to your own vault and collaboration setup
- [`docs/example-prompts.md`](./docs/example-prompts.md): copy-ready prompts
- [`examples/case-study-pathology-ingest-iteration.md`](./examples/case-study-pathology-ingest-iteration.md): test-driven ingest case study
- [`Releases`](https://github.com/zouxy111/wiki-knowledgebase-share-kit/releases): download published versions
- [`GitHub Pages`](https://zouxy111.github.io/wiki-knowledgebase-share-kit/): browse the landing page

---

![Share kit preview](./docs/assets/social-preview.png)

## 30-second overview

| Typical drifting vault / project state | Target state after adopting this kit |
|---|---|
| Root pages accumulate temporary execution history | Root pages return to navigation, stable boundaries, and topic entrypoints |
| `ops` pages become chronological logs | `ops` pages become reusable symptom / root-cause / fix / boundary references |
| `log.md` turns into task replay | `log.md` stays milestone-only |
| Long-form imports get rewritten ad hoc | ingest starts with a stable baseline, compares candidates, and promotes only post-regression winners |
| Multi-person work lives only in chat | shared project directories hold questionnaires, alignment, assignments, follow-up, and decision distillation |
| Everyone works in private notes with no convergence point | personal wiki + personal agent are allowed, but the shared project directory stays the formal source of truth |

In one sentence:

> This kit is not for recording more logs. It is for making a vault behave like a real knowledge base again while making multi-person coordination reusable.

---

## What this project does

This repository now bundles **five installable skills**:

1. **Guide** — installation, setup, routing, and first-run help
2. **Ingest** — split long markdown sources or books into reusable pages, generate TOC / glossary candidates / related-link suggestions, compare candidate structures against a stable baseline, and promote only the versions that survive regression checks
3. **Maintenance** — write durable conclusions into a vault
4. **Audit** — inspect structure, metadata, navigation coverage, boundary drift, and noise regression
5. **Team coordination** — run a shared-project workflow for 2+ people: intake, role-aware questionnaires, alignment, assignment, follow-up, and decision distillation, with optional knowledge-base sync

The kit keeps a fixed page-role model:
- `project`
- `knowledge`
- `ops`
- `task`
- `overview`

But leaves these pieces configurable:
- vault root and page layout
- areas and root pages
- frontmatter rules
- member profile paths
- shared project directory path
- whether stable decisions should sync back into a vault

---

## Recommended collaboration integration

### Recommended runtimes
For multi-person coordination, this repository explicitly recommends:
- **OpenClaw**
- **Hermes**

“Seamless integration” here means the workflow can be reused through the same shared-project-directory contract plus the same skills / prompts / coordinator flow. It does **not** depend on a private platform API.

### Recommended working model
Think of collaboration as three layers:
- **shared project directory**: the team source of truth
- **personal wiki / private working area**: each member’s own drafting surface
- **personal agent** (for example OpenClaw / Hermes): each member’s helper for questionnaire answers, responses, and progress updates

Only markdown files synced back into the shared project directory enter the formal coordination loop.

### Recommended sync topologies
- **Mode 1**: keep `team-project/` as its own NAS / cloud-drive synced folder
- **Mode 2**: embed `team-project/` inside a shared wiki / shared knowledge-base subtree

See [`docs/collaboration-integration-patterns.md`](./docs/collaboration-integration-patterns.md).

---

## Best fit / not fit

### Best fit
- People already maintaining an Obsidian, markdown, or wiki vault
- Teams that want to separate durable knowledge from execution history
- Anyone who wants long-form ingest to behave like an iterative evaluation loop instead of a one-shot import
- Anyone coordinating 2+ people through a shared markdown workspace
- Users who accept the fixed page-role model

### Not a good fit
- People who do not want to configure a profile or shared workspace at all
- Vaults meant to stay log-first
- Users who reject the fixed page-role model
- Setups that only care about raw process capture, not durable retrieval or navigation
- Teams that want all coordination to stay in chat without a shared markdown contract

---

## Case studies
- [`examples/case-study-current-vault.md`](./examples/case-study-current-vault.md): what should be abstracted from a real vault before sharing it
- [`examples/case-study-pathology-ingest-iteration.md`](./examples/case-study-pathology-ingest-iteration.md): how a long-form professional markdown source is imported, tested, compared, refactored, and stabilized with a baseline/candidate loop
- [`examples/team-project-generic/`](./examples/team-project-generic/): generic 2-person shared-project example
- [`examples/team-project-qc/`](./examples/team-project-qc/): QC-flavored multi-person coordination example

---

## Platform status

| Platform | Status | Notes |
|---|---|---|
| Codex / ChatGPT Codex-style skill directories | Recommended | Repository includes `SKILL.md`, `references/`, and `agents/openai.yaml` |
| Claude-style skill directories | Works | Copy the five skill folders directly |
| OpenClaw / Hermes | Recommended runtime for team coordination | Best fit for the shared-project-directory workflow |
| Other platforms supporting `SKILL.md` bundles | Maybe | Invocation and discovery may need adaptation |

---

## Repository layout
```text
wiki-knowledgebase-share-kit/
  START-HERE.md
  README.md
  README.en.md
  docs/
    team-coordination-workflow.md
    collaboration-integration-patterns.md
    ingest-evaluation-rubric.md
  templates/
    vault-profile-template.md
    member-capability-profile-template.md
    team-project-workspace/
    ingest-iteration-log-template.md
  examples/
    example-vault-profile-generic.md
    team-project-generic/
    team-project-qc/
  skills/
    knowledge-base-kit-guide/
    knowledge-base-ingest/
    knowledge-base-maintenance/
    knowledge-base-audit/
    knowledge-base-team-coordination/
```

## Shortest path

### If you are here for knowledge-base work
1. Read [`START-HERE.md`](./START-HERE.md)
2. Copy [`templates/vault-profile-template.md`](./templates/vault-profile-template.md)
3. Copy the five `skills/` folders into your platform
4. Start with `knowledge-base-kit-guide`
5. Use [`docs/ingest-evaluation-rubric.md`](./docs/ingest-evaluation-rubric.md) and [`templates/ingest-iteration-log-template.md`](./templates/ingest-iteration-log-template.md) when iterating long-form ingest structures

### If you are here for team coordination
1. Read [`START-HERE.md`](./START-HERE.md)
2. Read [`docs/collaboration-integration-patterns.md`](./docs/collaboration-integration-patterns.md)
3. Copy [`templates/team-project-workspace/`](./templates/team-project-workspace/)
4. Copy [`templates/member-capability-profile-template.md`](./templates/member-capability-profile-template.md) if you want reusable member profiles
5. Start with `knowledge-base-kit-guide` or `knowledge-base-team-coordination`

---

## Developers
- 邹星宇
- 杨琦
