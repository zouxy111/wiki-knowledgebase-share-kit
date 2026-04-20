---
name: knowledge-base-kit-guide
description: This skill should be used when the user asks how to install or configure this wiki knowledge-base package, which of the 10 skills to use first, how to fill the vault profile, whether to start with orchestrator or a specialist skill, whether they need the optional project-management area, 怎么开始配置这套知识库维护包, 先用哪个 skill, 项目管理主线怎么进, or 怎么填写 vault profile. It explains onboarding, profile setup, progressive routing, and when to stay on the default maintenance path versus entering the PM mainline.
---

# Knowledge Base Kit Guide

这个 skill 不直接做长文档导入，不直接维护知识库，也不直接做审计。

它的职责是：
- 解释这套 10-skill package 的结构
- 解释 `vault profile` 该怎么填
- 帮用户判断是先用 `knowledge-base-orchestrator`，还是直接进入 specialist skill
- 在用户出现项目管理意图时，解释何时进入 `knowledge-base-project-management`
- 给出下一步只该做什么

## When to use
- 用户第一次拿到这套 share kit，不知道从哪开始
- 用户问“怎么安装这些 skills”
- 用户问“怎么填写 vault profile”
- 用户问“我现在该用哪个 skill”
- 用户已经装好了，但不知道下一步该走哪条路径

## What this skill should do

### 1. Explain the package shape
先说明这套分享包至少有三层：
- `skills/`：可安装 skill
- `templates/`：要先填的 profile / page templates
- `docs/` 与 `examples/`：平台无关说明和案例

### 2. Explain the onboarding choice
先帮用户选入口：
- 如果用户完全新手、还没弄清楚环境或有没有现成 vault：优先 `knowledge-base-orchestrator`
- 如果用户想先理解模型、页面角色、profile 和后续分流：优先本 skill
- 如果用户已经明确知道自己的目标：直接进 specialist skill

### 3. Explain the 10-skill routing
- `knowledge-base-orchestrator`：初始化入口；检查现有环境、可选安装 Obsidian、创建骨架、生成 profile、推荐下一步
- `knowledge-base-ingest`：长文档 / 书籍 / 教程导入
- `knowledge-base-maintenance`：任务结果沉淀
- `knowledge-base-audit`：结构健康检查
- `knowledge-base-project-management`：项目 intake、里程碑、blocker、优先级、个人执行板
- `knowledge-base-team-coordination`：多人共享项目协调
- `knowledge-base-delivery-audit`：交付完整性、ready / blocked / greenlight 审计
- `knowledge-base-working-profile`：协作画像沉淀
- `work-journal`：工作记录 / 周报 / 会议纪要
- 本 skill：安装说明、profile 说明、技能分流

### 4. Explain progressive loading
默认分流仍应先保持简洁：
- 不提 PM 意图 → 继续走原本的 onboarding / ingest / maintenance / audit 主线
- 提到 项目管理 / 周计划 / 里程碑 / blocker / handoff / greenlight / 项目复盘 → 再暴露 PM 主线

PM 主线的三个关键 skill：
- `knowledge-base-project-management`
- `knowledge-base-team-coordination`
- `knowledge-base-delivery-audit`

### 5. Detect missing setup prerequisites
如果用户还没准备这些内容，就优先提示补齐：
- vault root
- pages directory
- root pages
- area list
- canonical root-level markdown files
- frontmatter contract
- 当前 runtime 真正扫描的 skills 目录
- 安装后当前会话是否已经刷新 skill 列表

如果用户说：
- repo 里明明有 skill
- 但运行时提示 `Skill not found`

要优先帮助用户区分：
- **仓库里的 `skills/`**
- **运行时真正扫描的 skills 目录**

并明确提醒：
- 安装后通常需要重开会话或重启 runtime
- 可以优先使用 `scripts/install_skills.py`
- 如仍失败，查看 `../../docs/skill-installation-troubleshooting.md`

### 6. Keep the response narrow
回答时优先给出：
- 当前所处阶段（未安装 / 未配置 / 已配置待使用）
- 下一步只做什么
- 对应该打开哪个文件
- 这一步该调用哪个 skill

如果用户还没明确 PM 意图：
- 不要一上来强推 `project-management` area
- 只在需要时再建议复制 `templates/project-management/`

## Additional resources
- `references/quickstart.md`
- `references/profile-setup-checklist.md`
- `../../README.md`
- `../../START-HERE.md`
- `../../docs/usage-sop.md`
- `../../templates/vault-profile-template.md`
