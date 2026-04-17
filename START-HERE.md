# START HERE — 5 分钟快速上手

> 这是当前仓库的**唯一新手入口**。  
> 目标：让你在最短时间内理解 8 个 skill、完成安装、准备 profile，并知道第一步该调用哪个 skill。

---

## 先知道这 3 件事

1. 这不是单个 skill，而是一个 **8-skill package**
2. 你不一定要安装 Obsidian；如果你已经有 markdown/wiki vault，也可以直接用
3. 完全新手建议先用 `knowledge-base-orchestrator`；想先理解结构的人先用 `knowledge-base-kit-guide`

---

## 本项目包含的 8 个 skills

1. `knowledge-base-kit-guide` — 使用说明、profile 配置、技能分流
2. `knowledge-base-ingest` — 长文档 / 书籍 / 教程导入
3. `knowledge-base-maintenance` — 任务结果写回知识库
4. `knowledge-base-audit` — 结构审计与健康检查
5. `knowledge-base-orchestrator` — 零门槛初始化入口
6. `knowledge-base-team-coordination` — 多人共享项目协调
7. `knowledge-base-working-profile` — 协作画像沉淀
8. `work-journal` — 工作记录 / 会议纪要 / 周报沉淀

---

## 第一步：安装 8 个 skill

如果你已经在使用 Codex / Claude Code 或其他支持 `SKILL.md` 的平台，直接把这 8 个目录复制到平台的 `skills/` 目录：

```bash
# Codex 示例
cp -r skills/knowledge-base-kit-guide ~/.codex/skills/
cp -r skills/knowledge-base-ingest ~/.codex/skills/
cp -r skills/knowledge-base-maintenance ~/.codex/skills/
cp -r skills/knowledge-base-audit ~/.codex/skills/
cp -r skills/knowledge-base-orchestrator ~/.codex/skills/
cp -r skills/knowledge-base-team-coordination ~/.codex/skills/
cp -r skills/knowledge-base-working-profile ~/.codex/skills/
cp -r skills/work-journal ~/.codex/skills/

# Claude Code 示例
cp -r skills/knowledge-base-kit-guide ~/.claude/skills/
cp -r skills/knowledge-base-ingest ~/.claude/skills/
cp -r skills/knowledge-base-maintenance ~/.claude/skills/
cp -r skills/knowledge-base-audit ~/.claude/skills/
cp -r skills/knowledge-base-orchestrator ~/.claude/skills/
cp -r skills/knowledge-base-team-coordination ~/.claude/skills/
cp -r skills/knowledge-base-working-profile ~/.claude/skills/
cp -r skills/work-journal ~/.claude/skills/
```

验证安装时，确认平台已经能看到这 8 个 skill。

> 如果你还没有任何 skill-compatible AI 平台，请先安装你自己的平台，再回到这里；本仓库不绑定单一平台。

---

## 第二步：准备你的 profile

至少复制并填写：

- `templates/vault-profile-template.md`

可选模板：
- `templates/working-profile-page-template.md`
- `templates/journal-profile-template.md`
- `templates/member-capability-profile-template.md`

最少应补这些字段：
- Vault name
- Vault root path
- Primary markdown page directory
- Reader entrypoint file
- Milestone log file
- Area list
- Root page map

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

或中文：

```text
用 $knowledge-base-orchestrator 帮我初始化这套知识库维护包。
先检查我是不是已经有可用的 vault；只有在我真的需要时才建议安装 Obsidian。
如有必要就创建骨架、生成 vault profile，然后告诉我下一步该用哪个 skill。
```

### 路径 B：我想先理解清楚再动手
直接用 `knowledge-base-kit-guide`：

```text
Use $knowledge-base-kit-guide to help me install and configure this share kit.
I want to understand the profile first, then know which of the 8 skills I should use next.
```

或中文：

```text
用 $knowledge-base-kit-guide 帮我安装并配置这套知识库维护包。
我想先理解 profile，再决定下一步该用哪一个 skill。
```

---

## 第四步：进入日常使用

### 导入长文档 / 书籍
```text
Use $knowledge-base-ingest to import this long Markdown source into my knowledge base.
Read my vault profile first and treat the first import as a testable baseline rather than the final structure.
```

如果是超大文本 / 整本书 / 需要分块精读，再明确要求它切到 `close-reading mode`，先生成 batch packets 和 rolling state，再逐轮汇总；如果后续 source 有修改，优先只重跑 changed batches，并让 candidate pages 带上 draft frontmatter。

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

### 协调多人共享项目
```text
Use $knowledge-base-team-coordination to coordinate this shared project.
Read the shared project directory, generate role-aware questionnaires, and keep assignments in draft until confirmed.
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

### 2. Orchestrator 是不是会自动替我做完所有事情？
不是。  
它的定位是**onboarding coordinator**：检测现状、初始化骨架、生成 profile、推荐下一步。不是“万能自动代理”。

### 3. 我应该先用哪一个？
- 完全新手：`knowledge-base-orchestrator`
- 想先理解结构：`knowledge-base-kit-guide`
- 你已经知道自己要做什么：直接进对应 specialist skill

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
4. `examples/case-study-pathology-ingest-iteration.md`
5. `examples/scenario-*.md`（注意：这些是场景化示意）
