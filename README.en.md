# Wiki Knowledge Base Share Kit

[![Release](https://img.shields.io/github/v/release/zouxy111/wiki-knowledgebase-share-kit)](https://github.com/zouxy111/wiki-knowledgebase-share-kit/releases)
[![Validate](https://github.com/zouxy111/wiki-knowledgebase-share-kit/actions/workflows/validate.yml/badge.svg)](https://github.com/zouxy111/wiki-knowledgebase-share-kit/actions/workflows/validate.yml)
[![Stars](https://img.shields.io/github/stars/zouxy111/wiki-knowledgebase-share-kit)](https://github.com/zouxy111/wiki-knowledgebase-share-kit/stargazers)
[![Forks](https://img.shields.io/github/forks/zouxy111/wiki-knowledgebase-share-kit)](https://github.com/zouxy111/wiki-knowledgebase-share-kit/forks)
[![Contributors](https://img.shields.io/github/contributors/zouxy111/wiki-knowledgebase-share-kit)](https://github.com/zouxy111/wiki-knowledgebase-share-kit/graphs/contributors)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](./LICENSE)

> A **10-skill knowledge-base maintenance + collaboration package** for markdown / wiki / Obsidian-style vaults.  
> The default path still starts with knowledge-base maintenance; the PM mainline is added progressively only when you need milestones, blockers, team alignment, or delivery gates.

<p align="center">
  <a href="https://zouxy111.github.io/wiki-knowledgebase-share-kit/"><img src="https://img.shields.io/badge/Open-HTML_Homepage-4ab9ff?style=for-the-badge" alt="Open HTML Homepage" /></a>
  <a href="./START-HERE.md"><img src="https://img.shields.io/badge/Read-START--HERE-0f172a?style=for-the-badge" alt="Read START-HERE" /></a>
  <a href="https://github.com/zouxy111/wiki-knowledgebase-share-kit/releases"><img src="https://img.shields.io/badge/Browse-Releases-0ea5a4?style=for-the-badge" alt="Browse Releases" /></a>
</p>

[![HTML homepage preview](./docs/assets/social-preview.png)](https://zouxy111.github.io/wiki-knowledgebase-share-kit/)

> If you want the more product-like HTML landing page, open the **HTML Homepage** above; the repository README remains the authoritative surface for installation, routing, and method documentation.

---

## 30-second overview

Most vault problems are not caused by a lack of writing. They come from drift:
- too much content without stable entrypoints
- root pages turning into process logs
- long-form sources, meeting notes, and task conclusions getting mixed together
- collaboration context living in chat, personal notes, and temporary files
- projects moving forward without a shared milestone / blocker / delivery gate surface

This kit is designed to shift a vault and a collaboration workspace toward the following state:

| Typical problem | Target state |
|---|---|
| Root pages become timeline dumps | Root pages return to navigation, stable boundaries, and topic entrypoints |
| Long documents are hard to reuse after import | Sources are split into overview / chapter / topic structures with lineage preserved |
| Durable conclusions only exist in chat or meetings | Reusable conclusions are written back into the right pages |
| The vault drifts but nobody knows where it is broken | Audit checks dead links, orphan pages, boundary drift, and noise regression |
| Collaboration context is fragmented and hard to hand off | Working profile, team coordination, and journal workflows create a stable collaboration surface |
| A project owner cannot clearly drive the next step | Project-management and delivery-audit add milestones, blockers, and readiness gates |

In one sentence:

> Make your markdown repository behave like a real knowledge base, and make shared projects behave like traceable, auditable workflows instead of scattered temporary coordination.

---

## This is a 10-skill package

The current public package contains 10 skills:

1. `knowledge-base-kit-guide`
2. `knowledge-base-orchestrator`
3. `knowledge-base-ingest`
4. `knowledge-base-maintenance`
5. `knowledge-base-audit`
6. `knowledge-base-project-management`
7. `knowledge-base-team-coordination`
8. `knowledge-base-delivery-audit`
9. `knowledge-base-working-profile`
10. `work-journal`

The canonical registry also lives in [`skills/catalog.toml`](./skills/catalog.toml):

<!-- skill-catalog:en:start -->
| # | Skill | Capability area | Primary responsibility |
|---|---|---|---|
| 1 | `knowledge-base-kit-guide` | Onboarding / Orchestration | installation guidance, profile setup, and skill routing |
| 2 | `knowledge-base-orchestrator` | Onboarding / Orchestration | low-friction onboarding and initial vault setup |
| 3 | `knowledge-base-ingest` | Ingest | long-form source import and structural reorganization |
| 4 | `knowledge-base-maintenance` | Maintenance | durable task-result and meeting write-back |
| 5 | `knowledge-base-audit` | Audit | structural audit and vault health checks |
| 6 | `knowledge-base-project-management` | Project management | project intake, milestones, blockers, and owner execution boards |
| 7 | `knowledge-base-team-coordination` | Team coordination | shared project coordination and role-aware questionnaires |
| 8 | `knowledge-base-delivery-audit` | Delivery audit | delivery completeness, ready/blocked states, and greenlight audits |
| 9 | `knowledge-base-working-profile` | Working profile | collaboration profile extraction and maintenance |
| 10 | `work-journal` | Work journal | work logs, meeting notes, and periodic distillation |
<!-- skill-catalog:en:end -->

Together they cover 9 capability tracks:
<!-- capability-areas:start -->
- **Onboarding / Orchestration**
- **Ingest**
- **Maintenance**
- **Audit**
- **Project management**
- **Team coordination**
- **Delivery audit**
- **Working profile**
- **Work journal**
<!-- capability-areas:end -->

In particular:
- `knowledge-base-kit-guide` explains installation, profile setup, and routing
- `knowledge-base-orchestrator` handles low-friction onboarding
- `knowledge-base-project-management` handles owner-side intake, milestones, blockers, and execution boards
- `knowledge-base-team-coordination` handles 2+ person shared-project workflows
- `knowledge-base-delivery-audit` handles delivery completeness and ready / blocked / greenlight review

> `knowledge-base-orchestrator` is an onboarding coordinator, not a universal autonomous agent.

---

## Default path vs optional PM mainline

### Default path: stay narrow first
If you mainly need to:
- import long-form sources
- maintain a knowledge base
- audit structure
- maintain working profiles or work journals

start with:
- `knowledge-base-kit-guide`
- `knowledge-base-orchestrator`
- `knowledge-base-ingest`
- `knowledge-base-maintenance`
- `knowledge-base-audit`

### Optional PM mainline: load only when needed
Only move into the PM mainline when the intent is clearly about:
- project management
- weekly planning
- milestones
- blockers / dependencies
- handoff
- ready / greenlight
- project retrospectives

The PM mainline is formed by:
- `knowledge-base-project-management`
- `knowledge-base-team-coordination`
- `knowledge-base-delivery-audit`

It corresponds to a new **optional area**:
- `project-management`

This area holds management-layer artifacts only. It does not replace business areas and does not replace `governance`.

See also:
- [`docs/project-management-workflow.md`](./docs/project-management-workflow.md)
- [`templates/project-management/README.md`](./templates/project-management/README.md)

---

## Best fit

### Good fit
- Individuals or teams already maintaining a markdown / wiki / Obsidian-style vault
- People who want to separate execution history from durable knowledge
- Users who accept the fixed page-role model: `project / knowledge / ops / task / overview`
- Teams that want stable workflows for ingest, maintenance, audit, collaboration, project progression, and delivery review

### Not a good fit
- People who do not want to configure a `vault profile`
- Log-first vaults that do not care about navigation or governance
- Users expecting the package to run as a background fully automatic system
- Setups that reject the fixed page-role model and explicit artifact states

---

## Core model: 5 fixed page roles

This method uses **5 fixed page roles**:

| Role | Purpose | What it should not carry |
|---|---|---|
| `project` | project navigation, overview, boundaries | long chronological narration, raw chat history |
| `knowledge` | methods, concepts, reusable knowledge | “what I did today” style process notes |
| `ops` | troubleshooting, operational procedures, boundary rules | one-off fix playback |
| `task` | todo items, assignments, in-progress work | long-term knowledge |
| `overview` | vault homepage, governance rules, indexes | detailed project history |

Additional notes:
- `work-journal` is a separate workflow, not a sixth page role
- `project-management` is an optional area, not a new page role
- journal entries, PM boards, and shared-project artifacts should still be filtered before they are promoted into durable knowledge pages

---

## Why the method works

It relies on a few stable rules:

1. **Knowledge-base-first**: keep durable knowledge, filter one-off noise
2. **Fixed role model**: each page has a clear job
3. **Four-sync mechanism**: substantive updates should sync the target page, root page, `index.md`, and `log.md`
4. **Milestone-only log**: `log.md` should record milestones, not task playback
5. **Periodic audit**: structure, navigation, metadata, and noise regression should be checked regularly
6. **Draft / approval boundaries**: multi-person and PM artifacts should distinguish `draft / approved / blocked / superseded`

---

## Recommended scenario: high-knowledge-density, multi-person, auditable collaboration

This kit is particularly strong in environments that are:

> **knowledge-dense, frequently updated, collaboration-heavy, and in need of traceability and auditability.**

That includes, but is not limited to:
- medical / pathology / research work
- enterprise knowledge bases / project delivery / operational documentation
- cross-team collaboration / onboarding / meeting conclusion distillation
- teams that need owner-side planning, multi-person alignment, and delivery gating

---

## How the PM mainline avoids polluting the structure

New area:
- `project-management`

Its boundary is fixed:
- business facts → original business areas
- vault governance → `governance`
- milestones, boards, risks, decisions, delivery gates → `project-management`

Recommended blocks:
1. **Portfolio / project overview**
2. **Team coordination**
3. **Personal execution**

Recommended templates:
- `project-project-management-overview.md`
- `pm-portfolio-board.md`
- `pm-operating-model.md`
- `pm-personal-execution-board.md`
- `pm-weekly-review-ops.md`
- `pm-delivery-gates.md`
- `pm-risk-register.md`
- `pm-decision-register.md`

---

## OpenClaw / Hermes / NAS / personal wiki integration patterns

Current recommended platforms:
- **OpenClaw**
- **Hermes**

“Seamless integration” here means:
- the same shared project directory contract
- the same skills / prompts / coordinator workflow
- no dependency on platform-private APIs

Recommended collaboration pattern:
- `team-project/` is the shared source of truth
- each member can keep a personal wiki / private workspace for drafts and reasoning
- each member can use OpenClaw / Hermes / another agent to help answer questionnaires and organize updates
- only the markdown files synced back into the shared project directory enter the formal coordination loop

Recommended sync topologies:
1. `team-project/` as a standalone NAS / cloud-synced folder
2. `team-project/` embedded inside a shared wiki / shared knowledge base

See also:
- [`docs/collaboration-integration-patterns.md`](./docs/collaboration-integration-patterns.md)
- [`docs/team-coordination-workflow.md`](./docs/team-coordination-workflow.md)

---

## Installation

Start with the general rule:

> The package is fundamentally a set of **10 `SKILL.md`-style skill bundles**.  
> If your AI platform supports a similar skills-directory structure, you can install it.  
> **Important:** a runtime only reads its own skills directory. It does not automatically read the `skills/` folder inside this Git repository.

Prefer the unified CLI over copying folders one by one:

```bash
# Inspect which runtimes the CLI can see
./wiki-kit detect

# Run from the cloned repository (best when only one runtime is present)
./wiki-kit install

# Pick an explicit runtime when multiple runtimes coexist
./wiki-kit install --platform codex --force

# Verify the target skills directory afterwards
./wiki-kit verify
```

If `./wiki-kit detect` reports multiple available skills directories, the CLI now asks you to choose `--platform <codex|claude|kimi|agents>` or `--target-dir` explicitly so it does not install into the wrong runtime by accident.

You can also invoke the same CLI without executable permissions:

```bash
python3 -m wiki_knowledgebase_share_kit install
python3 -m wiki_knowledgebase_share_kit verify
```

If you want a globally installed command:

```bash
pipx install git+https://github.com/zouxy111/wiki-knowledgebase-share-kit.git
wiki-kit install
wiki-kit verify
```

After installing:
1. reopen the current session or restart the runtime
2. confirm the runtime now lists the expected skill names
3. if it still says `Skill not found`, read [`docs/skill-installation-troubleshooting.md`](./docs/skill-installation-troubleshooting.md)

### Compatibility entrypoints

```bash
# Legacy wrappers now delegate to the same CLI backend
./wiki-kit install
bash install.sh
python3 scripts/install_skills.py --platform claude --force
./wiki-kit verify
```

### Manual install example

```bash
cp -r skills/knowledge-base-kit-guide ~/.codex/skills/
cp -r skills/knowledge-base-orchestrator ~/.codex/skills/
cp -r skills/knowledge-base-ingest ~/.codex/skills/
cp -r skills/knowledge-base-maintenance ~/.codex/skills/
cp -r skills/knowledge-base-audit ~/.codex/skills/
cp -r skills/knowledge-base-project-management ~/.codex/skills/
cp -r skills/knowledge-base-team-coordination ~/.codex/skills/
cp -r skills/knowledge-base-delivery-audit ~/.codex/skills/
cp -r skills/knowledge-base-working-profile ~/.codex/skills/
cp -r skills/work-journal ~/.codex/skills/

# Or use the skill catalog to install dynamically:
# for skill in $(python3 scripts/skill_catalog.py list-names); do
#   cp -r "skills/${skill}" ~/.codex/skills/
# done
```

Other common directory patterns include:
- `~/.kimi/skills` — Kimi CLI
- `~/.claude/skills` — Claude Code
- `~/.codex/skills` — Codex
- `~/.agents/skills` — generic agents

> **Note:** Kimi CLI and Claude Code may share the same `~/.agents/skills` directory via symlinks. If both point there, you only need one install.

> If you are using OpenClaw, Hermes Agent, or another compatible platform, confirm that platform’s skills-directory convention before installation.

---

## OpenClaw / Hermes / MinerU compatibility notes

This method often pairs well with:
- **OpenClaw** as a day-to-day AI assistant platform
- **Hermes Agent** as a long-running collaboration-oriented agent platform
- **MinerU** as a PDF / complex-document to markdown conversion tool

But the important boundary is:
- these are **recommended combinations**, not exclusive dependencies
- the core value of this repository is still **knowledge-base structure governance and workflow design**, not platform lock-in

If you want to plug the method into a longer-running OpenClaw / Hermes workspace, continue with [`docs/agent-runtime-writeback-patterns.md`](./docs/agent-runtime-writeback-patterns.md).
That document explains why we recommend an optional `agent-workspace/` folder parallel to `pages/` for drafts, distills, comparison notes, and runtime helper artifacts; if you really keep a local mirror of shared-project material, it must stay a read-only cache and never replace `team-project/` as the coordination source of truth.

If you need team-specific customization on top of the public bundle, continue with [`docs/core-vs-local-overlay.md`](./docs/core-vs-local-overlay.md).
That doc explains how to keep the public core reusable while moving private conventions into a local overlay.

---

## Quick start

```bash
# 1. Clone the repository
git clone https://github.com/zouxy111/wiki-knowledgebase-share-kit.git
cd wiki-knowledgebase-share-kit

# 2. Read the onboarding entrypoint
cat START-HERE.md

# 3. Copy the template and prepare your profile
cp templates/vault-profile-template.md ./my-vault-profile.md

# 4. Install the bundled skills into your runtime directory
./wiki-kit install --platform codex --force
```

If you do not need the PM mainline yet, you do not have to configure the `project-management` area on day one.

---

## FAQ

**Q: Can I use this without Obsidian?**  
A: Yes. If you have a markdown/wiki vault and a platform that supports a comparable skills directory structure, you can use it.

**Q: Can I use it without full automation?**  
A: Yes. The docs, templates, and checklists are still useful manually; the skills mainly improve execution efficiency.

**Q: My vault is already messy. Can I still adopt this?**  
A: Yes. Start with an audit, then repair structure, navigation, and boundaries incrementally.

**Q: Why does the runtime say `Skill not found` even though `knowledge-base-ingest` exists in the repo?**  
A: Usually the repo is fine; the runtime's actual skills directory was not installed or reloaded. Run `./wiki-kit install --platform <codex|claude|kimi|agents> --force`, then reopen the session. See [`docs/skill-installation-troubleshooting.md`](./docs/skill-installation-troubleshooting.md).

**Q: How do I prevent a huge source from being only half-read and still being reported as “fully imported”?**  
A: Do not feed the whole giant source directly to the model. First generate `manifest.json` and `coverage-map.md` with `split_markdown.py`, process the source chunk by chunk, then gate completion with `verify_ingest_coverage.py`. See [`docs/ingest-completeness-guardrails.md`](./docs/ingest-completeness-guardrails.md).

**Q: Can these distilled outputs also be written back into OpenClaw?**
A: Yes. The recommended pattern is to keep `pages/` for durable knowledge and add an optional `agent-workspace/` folder parallel to it for OpenClaw / Hermes drafts, distills, comparison notes, and runtime helper artifacts. If you keep a local mirror of shared-project material, treat it as a read-only cache only, never as the coordination source of truth. See [`docs/agent-runtime-writeback-patterns.md`](./docs/agent-runtime-writeback-patterns.md).

**Q: Will project management mix business knowledge with governance?**  
A: No. The PM mainline explicitly separates them: business facts stay in business areas, governance stays in `governance`, and management-layer boards live in `project-management`.

**Q: Do I have to configure the PM area from the start?**  
A: No. It is progressive. Enable it only when you actually need owner-side project progression, multi-person alignment, or delivery gating.

**Q: Are OpenClaw / Hermes platform-specific dependencies?**  
A: No. They are recommended platforms, but compatibility comes from the shared project directory contract, markdown protocol, and skills / prompt workflow rather than private APIs.

---

## Read these first

- [`START-HERE.md`](./START-HERE.md)
- [`GLOSSARY.md`](./GLOSSARY.md)
- [`templates/vault-profile-template.md`](./templates/vault-profile-template.md)
- [`docs/example-prompts.md`](./docs/example-prompts.md)
- [`docs/usage-sop.md`](./docs/usage-sop.md)
- [`docs/project-management-workflow.md`](./docs/project-management-workflow.md)
- [`docs/agent-runtime-writeback-patterns.md`](./docs/agent-runtime-writeback-patterns.md)
- [`examples/case-study-pathology-ingest-iteration.md`](./examples/case-study-pathology-ingest-iteration.md)

---

## Need help?

- [GitHub Issues](https://github.com/zouxy111/wiki-knowledgebase-share-kit/issues)
- Developers: 邹星宇, 杨琦, 张陈祎

---

## License

MIT License

---

> If you want your vault to behave more like a knowledge base and your collaboration to behave more like a reusable, auditable workflow, start with `START-HERE.md`.
