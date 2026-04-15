---
name: knowledge-base-maintenance
description: This skill should be used when the user asks to "maintain a markdown knowledge base", "sync durable conclusions into a vault", "organize a wiki by page roles", "维护到 wiki", "同步到知识库", "把任务结果沉淀进知识库", or "更新知识库导航和里程碑日志". It maintains a markdown/wiki vault by reading a vault profile first, applying a fixed page-role model, and filtering process noise before writing.
---

# Knowledge Base Maintenance

把任务结果、聊天结论、排障经验或治理规则沉淀进任意 markdown/wiki 知识库。

默认目标不是“把过程都记下来”，而是把目标 vault 维护成**知识库优先**的系统：
- 优先保留：稳定知识、长期边界、复用方法、可复用排障结论
- 默认拒绝：一次性过程、长流水、低价值路径噪音、原始运行时镜像

## When to use
- 用户要把“这次任务/聊天/排查结果”沉淀进知识库
- 用户要更新现有页面、导航或里程碑日志，而不是只在聊天里口头总结
- 用户要清理、压缩、重写已有页面，让它更像知识库而不是项目笔记
- 用户已经有一个 markdown/wiki vault，希望按固定页面角色模型持续维护

## Required input
在执行维护前，先读取 **vault profile**。

默认需要以下输入：
- vault root
- 页面目录
- reader entrypoint
- milestone log
- maintainer entrypoint
- area 列表
- root page map
- canonical root-level markdown files
- frontmatter 规则

先读：
- `references/vault-profile-contract.md`
- `references/maintenance-checklist.md`
- `../../templates/vault-profile-template.md`

如果用户没有提供 profile，就先要求最小配置，再继续执行，不要凭空猜测路径或 root pages。

## Fixed page-role model
这套技能固定保留以下角色模型：
- `project`：主线导航、稳定总览、长期边界、专题入口
- `knowledge`：结构、概念、方法、判断框架
- `ops`：流程、排障、版本边界、回归方法
- `task`：分工、协同、回填顺序、仍在推进的任务结构
- `overview`：索引、治理、维护入口、全库说明

如果目标 vault 不使用这套角色模型，这个 skill 不应直接套用。

## Core rules
- **先读 profile，再动文件。** 不要假定路径、areas 或 root pages。
- **先做噪音过滤。** 不要把一次性过程直接写进知识库。
- **先判页面角色，再判 area。** 不要跳过分类直接写内容。
- **优先更新已有页，不默认新建页。**
- **每次实质更新至少同步四处：** 目标页、对应 root page、reader entrypoint、milestone log。
- **不写 secrets。**
- **不制造占位死链。**
- **若 profile 缺失关键字段，先补配置，再执行。**

## Knowledge-base-first writing rules

### `project`
- 写导航、稳定总览、长期边界、专题入口
- 不写长段运行流水

### `knowledge`
- 写结构、概念、方法、规则、判断框架
- 不写单次修复过程和临时待办

### `ops`
- 默认写成：现象 / 根因 / 处理法 / 边界
- 保留固定流程、可复用排障、版本边界、回归方法
- 不写完整流水账

### `task`
- 写分工、协同、回填顺序和当前任务结构
- 稳定知识应迁出到 `knowledge` 或 `ops`

### `overview`
- 写全库入口、治理规则、维护说明
- 不承载项目运行历史

### `log`
- 只写里程碑级变化
- 不写任务回放

## Workflow

### 1. Gather source truth
- 先读取当前任务、聊天或外部结果
- 再读取 vault profile
- 如有必要，再比对现有页面和导航入口

### 2. Run the noise filter first
写入前先判断：
- 这段内容未来是否值得检索？
- 它是稳定结论还是过程噪音？
- 它应该进入知识库，还是只应留在原始记录里？

以下内容默认不直接进入知识库：
- 长过程
- 单次运行状态
- 低价值路径清单
- 原始镜像
- 只对当次会话有意义的解释过程

### 3. Decide update vs create
- 若已有对应页面，优先更新
- 仅当主题长期可复用且现有页面边界不合适时再新建
- 新建页前确认它会挂到某个 root page，并能进入 reader entrypoint

### 4. Classify by role + area
- 先判 `project / knowledge / ops / task / overview`
- 再按 profile 中的 area map 归类

### 5. Update the target page
- 刷新 frontmatter 和 `updated`
- 重写成知识库口径，而不是复制原始聊天
- 若必须保留路径，只保留长期稳定入口

### 6. Sync navigation and milestones
- 更新对应 root page
- 更新 reader entrypoint
- 更新 milestone log
- 如改变治理规则，再更新 maintainer entrypoint 或相关 overview 页面

### 7. Validate before finishing
- frontmatter 是否完整
- 页面是否有入口
- 是否引入死链
- 内容是否混边界
- 是否把过程噪音写回了根页或知识页

## Output expectations
汇报时至少说明：
- 更新了哪些页面
- 为什么归到该页面角色
- 是否同步了 root page / reader entry / milestone log
- 哪些内容被视为噪音而被压缩或删除

## Additional resources
- `references/vault-profile-contract.md`：需要用户提供哪些 profile 信息
- `references/maintenance-checklist.md`：固定维护回路、同步要求、噪音过滤规则
- `../../templates/vault-profile-template.md`：可填写的 profile 模板
