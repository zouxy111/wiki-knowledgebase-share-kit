---
name: knowledge-base-kit-guide
description: This skill should be used when the user asks to "how do I use this wiki skill kit", "set up a markdown knowledge base workflow", "install the knowledge base skills", "which skill should I use first", "怎么用这套 skills", "怎么开始配置这套知识库维护包", "先用 maintenance 还是 audit", or "怎么填写 vault profile". It explains how to install, configure, and start using the knowledge-base share kit before day-to-day maintenance or audit work begins.
---

# Knowledge Base Kit Guide

这个 skill 不直接维护知识库，也不直接做审计。

它的职责是：
- 教用户如何安装这套 share kit
- 教用户如何填写 `vault profile`
- 教用户什么时候该用 `knowledge-base-maintenance`
- 教用户什么时候该用 `knowledge-base-audit`
- 帮用户判断当前卡在哪个配置步骤

## When to use
- 用户第一次拿到这套 share kit，不知道从哪开始
- 用户问“怎么安装这些 skills”
- 用户问“怎么填写 vault profile”
- 用户问“先用 maintenance 还是 audit”
- 用户问“为什么这套模板还不能直接跑”

## What this skill should do

### 1. Explain the package structure
先说明这套分享包有三层：
- `skills/`：可安装 skill
- `templates/`：需要先填写的 profile 模板
- `docs/`：平台无关使用说明
- `examples/`：真实案例参考

### 2. Explain the first-run path
默认推荐用户按以下顺序开始：
1. 读 `README.md`
2. 读 `docs/customization-guide.md`
3. 复制并填写 `templates/vault-profile-template.md`
4. 再安装 `knowledge-base-maintenance` 和 `knowledge-base-audit`
5. 最后进入日常 maintenance / audit 工作流

### 3. Explain the fixed model vs customizable parts
明确告诉用户：
- 固定不变的是页面角色模型：`project / knowledge / ops / task / overview`
- 可自定义的是 vault 路径、area、root pages、命名规则、frontmatter 规则

### 4. Explain skill responsibilities
- `knowledge-base-maintenance`：把任务结果沉淀进知识库
- `knowledge-base-audit`：检查结构、导航、元数据和噪音回流
- 本 skill：负责安装、上手、配置和分流说明

### 5. Detect missing setup prerequisites
如果用户还没准备这些内容，就优先提示补齐：
- vault root
- pages directory
- root pages
- area list
- canonical root-level markdown files
- frontmatter contract

## Recommended response shape
回答时优先给出：
- 当前所处阶段（未安装 / 未配置 / 已配置待使用 / 已使用待审计）
- 下一步只做什么
- 对应应该打开哪个文件
- 当前该调用哪个 skill

## Additional resources
- `references/quickstart.md`
- `references/profile-setup-checklist.md`
- `../../README.md`
- `../../docs/customization-guide.md`
- `../../docs/usage-sop.md`
- `../../templates/vault-profile-template.md`
