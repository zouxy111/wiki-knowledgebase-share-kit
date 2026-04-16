---
name: knowledge-base-kit-guide
description: This skill should be used when the user asks to "how do I use this wiki skill kit", "set up a markdown knowledge base workflow", "install the knowledge base skills", "which skill should I use first", "怎么用这套 skills", "怎么开始配置这套知识库维护包", "先用 maintenance 还是 audit", "怎么做多人协同项目目录", or "怎么填写 vault profile / member profile". It explains how to install, configure, and start using the knowledge-base share kit before day-to-day maintenance, audit, or team-coordination work begins.
---

# Knowledge Base Kit Guide

这个 skill 不直接维护知识库，也不直接做审计或多人派单。

它的职责是：
- 教用户如何安装这套 share kit
- 教用户如何填写 `vault profile`
- 教用户如何准备共享项目目录与成员画像
- 教用户如何理解 OpenClaw / Hermes + shared project directory 的推荐接入模式
- 教用户什么时候该用 `knowledge-base-maintenance`
- 教用户什么时候该用 `knowledge-base-audit`
- 教用户什么时候该用 `knowledge-base-team-coordination`
- 帮用户判断当前卡在哪个配置步骤

## When to use
- 用户第一次拿到这套 share kit，不知道从哪开始
- 用户问“怎么安装这些 skills”
- 用户问“怎么填写 vault profile / member profile”
- 用户问“先用 maintenance 还是 audit，还是多人协同 skill”
- 用户问“为什么这套模板还不能直接跑”
- 用户还没搞清楚自己缺的是知识库配置，还是共享项目目录配置

## What this skill should do

### 1. Explain the package structure
先说明这套分享包有四层：
- `skills/`：可安装 skill
- `templates/`：需要先填写的 profile / workspace 模板
- `docs/`：平台无关使用说明
- `examples/`：真实案例参考

### 2. Explain the first-run path
默认推荐用户按以下顺序开始：
1. 读 `START-HERE.md`
2. 安装 4 个 skill（或至少先安装本 guide skill）
3. 如果是知识库场景：复制并填写 `templates/vault-profile-template.md`
4. 如果是多人协同场景：复制 `templates/team-project-workspace/`
5. 如需复用成员画像：填写 `templates/member-capability-profile-template.md`
6. 把 profile 或项目目录保存到稳定的绝对路径
7. 调用本 skill，并明确告诉 agent 这些路径
8. 最后进入 maintenance / audit / team-coordination 工作流

### 3. Explain the fixed model vs customizable parts
明确告诉用户：
- 固定不变的是页面角色模型：`project / knowledge / ops / task / overview`
- 固定不变的是多人协同状态机：Kickoff → Questionnaire → Alignment → Assignment → Follow-up → Distill / Closeout
- 固定不变的是 shared project directory 作为协调事实源
- 可自定义的是 vault 路径、area、root pages、命名规则、frontmatter 规则、成员画像路径、项目目录路径，以及是否通过 NAS / 网盘或共享 wiki 来同步该目录

### 4. Explain skill responsibilities
- `knowledge-base-maintenance`：把任务结果沉淀进知识库
- `knowledge-base-audit`：检查结构、导航、元数据和噪音回流
- `knowledge-base-team-coordination`：负责多人项目协同、问卷派发、目标对齐、任务分配、跟进和决策蒸馏
- 本 skill：负责安装、上手、配置和分流说明

### 5. Detect missing setup prerequisites
如果用户还没准备这些内容，就优先提示补齐：

#### 知识库场景必备
- vault root
- pages directory
- root pages
- canonical root-level markdown files
- frontmatter contract

#### 多人协同场景必备
- shared project directory path
- `project-brief.md`
- `team-roster.md`
- 至少一个成员目录
- 是否已有 canonical member profiles
- 是否有 vault profile
- 是否需要 knowledge-base sync
- 是否打算用 OpenClaw / Hermes 作为主推运行平台
- 是否让成员在自己的 wiki / 私有工作区中用自己的 agent 协助填写问卷

### 6. Explain how the user should provide the inputs
默认接受三种方式：
- 给出 profile / 项目目录的**绝对路径**
- 直接附上一个 markdown 文件或整个目录
- 直接把 profile 内容粘贴到对话里

如果都没有，就不要假定 agent 能自己找到这些文件。
优先建议用户把 profile 保存成稳定路径，例如：
- `<vault-root>/vault-profile.md`
- `<workspace-root>/my-vault-profile.md`
- `<workspace-root>/team-project/`

## Recommended response shape
回答时优先给出：
- 当前所处阶段（未安装 / 未配置 / 已配置待使用 / 已在跑多人协同）
- 下一步只做什么
- 对应应该打开哪个文件
- 当前该调用哪个 skill

## Additional resources
- `references/quickstart.md`
- `references/profile-setup-checklist.md`
- `../../README.md`
- `../../docs/customization-guide.md`
- `../../docs/team-coordination-workflow.md`
- `../../docs/collaboration-integration-patterns.md`
- `../../docs/usage-sop.md`
- `../../templates/vault-profile-template.md`
- `../../templates/member-capability-profile-template.md`
- `../../templates/team-project-workspace/README.md`
