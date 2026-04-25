# START HERE — 5 分钟快速上手

> 这是当前仓库的**唯一新手入口**。  
> 目标：让你在最短时间内理解 10 个 skill、完成安装、准备 profile，并知道第一步该调用哪个 skill。

---

## 先知道这 4 件事

1. 这不是单个 skill，而是一个 **10-skill package**
2. 你不一定要安装 Obsidian；如果你已经有 markdown/wiki vault，也可以直接用
3. 默认先走知识库维护主线；**只有当你明确需要项目管理 / 里程碑 / blocker / handoff / ready 审计时**，再进入 PM 主线
4. 完全新手建议先用 `knowledge-base-orchestrator`；想先理解结构的人先用 `knowledge-base-kit-guide`

---

## 本项目包含的 10 个 skills

<!-- skill-catalog:zh:start -->
| # | Skill | 能力线 | 主要职责 |
|---|---|---|---|
| 1 | `knowledge-base-kit-guide` | Onboarding / Orchestration | 使用说明、profile 配置、技能分流 |
| 2 | `knowledge-base-orchestrator` | Onboarding / Orchestration | 零门槛初始化入口 |
| 3 | `knowledge-base-ingest` | Ingest | 长文档导入与结构化重组 |
| 4 | `knowledge-base-maintenance` | Maintenance | 任务结果与会议结论沉淀 |
| 5 | `knowledge-base-audit` | Audit | 结构审计与知识库健康检查 |
| 6 | `knowledge-base-project-management` | Project management | 项目 intake / milestone / blocker / owner 执行板 |
| 7 | `knowledge-base-team-coordination` | Team coordination | 共享项目协调与角色化问卷 |
| 8 | `knowledge-base-delivery-audit` | Delivery audit | 交付完整性 / ready / blocked / greenlight 审计 |
| 9 | `knowledge-base-working-profile` | Working profile | 协作画像提炼与维护 |
| 10 | `work-journal` | Work journal | 工作记录、会议纪要与周期沉淀 |
<!-- skill-catalog:zh:end -->

---

## 第一步：安装 10 个 skill

### 推荐方式：统一 CLI（单平台自动检测，多平台显式选择）

```bash
# 先看 CLI 检测到哪些平台
./wiki-kit detect

# 直接从仓库运行统一 CLI（单平台环境可直接安装）
./wiki-kit install

# 预览安装内容（不实际执行）
./wiki-kit install --dry-run

# 多 runtime 共存时，显式指定平台
./wiki-kit install --platform codex --force

# 验证安装结果
./wiki-kit verify
```

如果 `./wiki-kit detect` 提示发现了多个可用 skills 目录，说明这台机器上装了不止一个 runtime。此时请直接加 `--platform <codex|claude|kimi|agents>`，避免装到错误的位置。

也可以不用可执行权限，直接走 Python 模块入口：

```bash
python3 -m wiki_knowledgebase_share_kit install
python3 -m wiki_knowledgebase_share_kit verify
```

如果你想把命令装到系统里，再直接执行 `wiki-kit`：

```bash
pipx install git+https://github.com/zouxy111/wiki-knowledgebase-share-kit.git
wiki-kit install
wiki-kit verify
```

> **符号链接提示**：如果你的 `~/.claude/skills` 是指向 `~/.agents/skills` 的符号链接，CLI 会自动识别真实目录；如果你需要保持 repo 与运行时联动，可额外使用 `--mode symlink`。

### 兼容入口：保留旧脚本

```bash
# 这些入口现在都走同一套 CLI 后端
bash install.sh
python3 scripts/install_skills.py --platform codex --force
```

### 手动安装（备选）

```bash
cp -r skills/knowledge-base-kit-guide ~/.claude/skills/
cp -r skills/knowledge-base-orchestrator ~/.claude/skills/
cp -r skills/knowledge-base-ingest ~/.claude/skills/
cp -r skills/knowledge-base-maintenance ~/.claude/skills/
cp -r skills/knowledge-base-audit ~/.claude/skills/
cp -r skills/knowledge-base-project-management ~/.claude/skills/
cp -r skills/knowledge-base-team-coordination ~/.claude/skills/
cp -r skills/knowledge-base-delivery-audit ~/.claude/skills/
cp -r skills/knowledge-base-working-profile ~/.claude/skills/
cp -r skills/work-journal ~/.claude/skills/
```

### 验证安装

```bash
./wiki-kit verify
```

安装后一定要：
- 重开当前会话或重启 runtime
- 再检查 available skills
- 如果仍报 `Skill not found`，看 `docs/skill-installation-troubleshooting.md`

---

## 第二步：准备你的 profile

至少复制并填写：

- `templates/vault-profile-template.md`

可选模板：
- `templates/working-profile-page-template.md`
- `templates/journal-profile-template.md`
- `templates/member-capability-profile-template.md`
- `templates/team-project-workspace/`（**只有你需要 2 人及以上共享项目协调时才复制**）
- `templates/project-management/`（**只有你需要 PM 主线时才复制**）

最少应补这些字段：
- Vault name
- Vault root path
- Primary markdown page directory
- Reader entrypoint file
- Milestone log file
- Area list
- Root page map

如果你要启用 PM 主线：
- 可以额外新增 `project-management` area
- 但这不是所有用户一开始都必须配置的内容

不确定怎么填，就先看：
- `GLOSSARY.md`
- `examples/example-vault-profile-generic.md`

---

## 第三步：选你的第一条路径

### 路径 A：完全新手 / 想最省事
直接用 `knowledge-base-orchestrator`：

```text
Use $knowledge-base-orchestrator to help me set up this knowledge-base package.
Check whether I already have a usable vault first. Only offer Obsidian installation if I actually need it. Create a vault skeleton if needed, generate a vault profile, and then tell me which skill to use next.
```

### 路径 B：我想先理解清楚再动手
直接用 `knowledge-base-kit-guide`：

```text
Use $knowledge-base-kit-guide to help me install and configure this share kit.
I want to understand the profile first, then know which of the 10 skills I should use next.
```

### 路径 C：我已经知道自己要做什么
直接进对应 specialist skill：
- 导入长文档 → `knowledge-base-ingest`
- 沉淀任务结果 → `knowledge-base-maintenance`
- 做结构审计 → `knowledge-base-audit`
- 更新协作画像 → `knowledge-base-working-profile`
- 写工作记录 / 周报 → `work-journal`

---

## 第四步：只有在需要时，才进入 PM 主线

当你明确出现这些意图，再进入 PM 主线：
- 项目 intake
- 周计划 / next actions
- milestone / blocker / dependency
- 2 人及以上协作对齐
- handoff / ready / greenlight

推荐分流：

### A. 单人 / owner 视角推进
```text
Use $knowledge-base-project-management to help me run this project.
Read my vault profile and the relevant project brief / recent journal / current blockers first.
Generate a concise project summary, milestones, risks, dependencies, and a personal execution board.
Only suggest the project-management area if PM workflows are actually needed.
```

### B. 多人共享项目
```text
Use $knowledge-base-team-coordination to coordinate this shared project.
Read the shared project directory first, generate role-aware questionnaires, summarize alignment gaps, keep assignments in draft until approved, and distill reusable decisions at closeout.
```

如果你还没有共享项目目录骨架：
- 先复制 `templates/team-project-workspace/`
- 再把 `project-brief.md`、`team-roster.md` 和成员目录补齐

### C. 交付闭环 / ready 审计
```text
Use $knowledge-base-delivery-audit to review whether this project is actually ready.
Read the project brief, current assignments, decision records, and evidence first.
Report missing proof, write-back gaps, and whether the current state should stay blocked, move to ready, or wait for greenlight approval.
```

---

## 第五步：进入日常使用

### 导入长文档 / 书籍
```text
Use $knowledge-base-ingest to import this long Markdown source into my knowledge base.
Read my vault profile first.
For large sources, do not read the whole file in one pass. First generate bounded chunks plus manifest.json and coverage-map.md, then process every chunk, and do not call the import complete until coverage verification passes.
Treat the first import as a testable baseline rather than the final structure.
```

### 沉淀任务结果
```text
Use $knowledge-base-maintenance to integrate this task result into my knowledge base.
Read my vault profile first, keep only durable conclusions, and sync the relevant navigation surfaces.
```

### 做结构审计
```text
Use $knowledge-base-audit to inspect my knowledge base.
Read my vault profile first, then report dead links, orphan pages, missing entrypoints, metadata issues, boundary drift, and noise regression.
```

### 沉淀协作画像
```text
Use $knowledge-base-working-profile to update my working profile from our recent interactions.
Keep only collaboration-relevant stable signals and separate confirmed / repeated / inferred items.
```

### 写工作记录 / 周报
```text
Use $work-journal to create today's work log.
Include timestamps, project associations, meeting notes, and weekly distillation hooks when relevant.
```

---

## 常见问题

### 1. 我一定要用 Obsidian 吗？
不一定。  
只要你有一个 markdown/wiki vault，并且你的 AI 平台支持 `SKILL.md` 目录结构，就可以直接使用。

### 2. 我是不是一开始就必须配置 `project-management` area？
不是。  
这是**可选 area**。只有你真的需要项目推进 / 里程碑 / blocker / delivery gate 主线时再启用。

### 3. Orchestrator 会不会自动替我做完所有事情？
不会。  
它的定位是 onboarding coordinator：检测现状、初始化骨架、生成 profile、推荐下一步。不是万能自动代理。

### 4. 如果我只想手动照着文档做？
直接读：
1. `GLOSSARY.md`
2. `templates/vault-profile-template.md`
3. `docs/usage-sop.md`
4. `docs/example-prompts.md`

---

## 最短学习路径

### 15 分钟版本
1. 读完这份 `START-HERE.md`
2. 看 `GLOSSARY.md`
3. 复制 `templates/vault-profile-template.md`
4. 用 `knowledge-base-orchestrator` 或 `knowledge-base-kit-guide` 完成初始化
5. 跑一次 `knowledge-base-audit` 或做一次 `knowledge-base-maintenance`

### 进阶版本
1. `docs/customization-guide.md`
2. `docs/usage-sop.md`
3. `docs/example-prompts.md`
4. `docs/project-management-workflow.md`
5. `docs/collaboration-integration-patterns.md`
6. `docs/agent-runtime-writeback-patterns.md`
7. `examples/case-study-pathology-ingest-iteration.md`
