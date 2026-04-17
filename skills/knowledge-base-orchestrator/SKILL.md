---
name: knowledge-base-orchestrator
description: Optional onboarding coordinator for this 8-skill knowledge-base package. Use when the user wants the easiest setup path, needs environment detection, wants help checking whether Obsidian or an existing vault is already available, wants a vault skeleton plus profile generated, or asks for 零门槛初始化, 一键式上手, setup orchestrator, or 先帮我把环境和 profile 跑通. It coordinates setup and recommends the next specialist skill; it is not a universal autonomous agent.
---

# Knowledge Base Orchestrator

这是这套仓库里的**onboarding coordinator**。  
它的目标是：**先把环境、vault 骨架和 profile 跑通，再把用户路由到正确的 specialist skill。**

它不是：
- “万能总控”
- 自动替用户完成全部知识库治理
- 复杂多轮代理编排系统

## What success looks like
执行完成时，至少要做到以下几件事中的大部分：
1. 检查用户是否已经有可用的 Obsidian / markdown vault / vault profile
2. 在用户需要时，提供**可选**的 Obsidian 安装路径
3. 需要新建时，创建标准 vault 骨架
4. 生成一个可继续编辑的 `vault-profile.md`
5. 明确告诉用户下一步该用哪个 specialist skill

## Required resources
执行前先读取：
- `references/environment-setup.md`
- `scripts/detect-obsidian.sh`
- `scripts/install-obsidian.sh`
- `scripts/create-vault-structure.sh`
- `scripts/generate-vault-profile.sh`
- `../../START-HERE.md`
- `../../templates/vault-profile-template.md`

## Core rules
- **先检查有没有现成环境，再建议安装。**
- **Obsidian 安装只是可选能力，不是仓库主价值。**
- **没有必要时，不要把用户往“重装环境”这条路上推。**
- **创建骨架和生成 profile 后，要立即给出下一步 specialist skill。**
- **如果平台不支持自动调起别的 skill，就明确给出下一条 prompt，而不是假装已经自动路由。**
- **不要把自己描述成“万能自动代理”。**

## Recommended workflow

### 1. Environment check
先判断：
- 用户是否已经有 Obsidian
- 用户是否已经有一个现成的 markdown/wiki vault
- 用户是否已经有 `vault-profile.md` 或等价配置

如果用户已有可用环境：
- 跳过安装
- 直接进入 profile 检查或 specialist skill 路由

### 2. Optional Obsidian path
只有在用户明确需要、且没有可用编辑环境时，才走安装路径。

安装时：
- 先说明这是**可选步骤**
- 先征得用户同意
- 安装失败时，降级成“用户继续使用现有编辑器/现有 vault”的路径

### 3. Create vault skeleton
如果用户没有现成 vault，使用 `scripts/create-vault-structure.sh` 创建最小骨架。

默认产物包括：
- `index.md`
- `log.md`
- `README.md`
- `pages/`
- `.obsidian/`
- 若干默认 overview 页面

### 4. Generate vault profile
使用 `scripts/generate-vault-profile.sh` 生成初始 `vault-profile.md`。

需要收集的最少信息：
- vault path
- vault name
- areas（允许先用默认值）

生成后要提醒用户：
- 这是初始 profile，不是最终版本
- 如需 working profile / journal / team coordination 的高级配置，可继续编辑模板

### 5. Route to the next skill
初始化完成后，根据用户目标给出下一步：
- 想理解结构：`knowledge-base-kit-guide`
- 导入长文档：`knowledge-base-ingest`
- 写回知识：`knowledge-base-maintenance`
- 审计结构：`knowledge-base-audit`
- 沉淀协作画像：`knowledge-base-working-profile`
- 跑多人项目：`knowledge-base-team-coordination`
- 写工作记录：`work-journal`

## Output expectations
汇报时至少说明：
- 检查了哪些环境项
- 跳过了哪些不必要步骤
- 是否创建了 vault 骨架
- 是否生成了 vault profile
- 下一步推荐哪个 specialist skill，为什么

## Notes on automation boundaries
如果脚本能力只完成：
- 环境检查
- 骨架创建
- profile 生成

那就应该如实说明“这里完成的是初始化，不是后续 specialist work”。

## Additional resources
- `references/environment-setup.md`
- `scripts/detect-obsidian.sh`
- `scripts/install-obsidian.sh`
- `scripts/create-vault-structure.sh`
- `scripts/generate-vault-profile.sh`
