---
name: knowledge-base-audit
description: This skill should be used when the user asks to "audit a wiki vault", "check dead links or orphan pages", "inspect knowledge base structure", "审计 wiki", "检查知识库结构", "看看有没有死链或孤立页", or "检查导航、frontmatter 和噪音回流". It audits a markdown/wiki knowledge base by reading a vault profile first and then checking structure, navigation, metadata, boundary drift, noise regression, and stray markdown files at the vault root.
---

# Knowledge Base Audit

对任意 markdown/wiki 知识库做结构化审计。

重点不是润色正文，而是检查这个 vault 是否还能稳定作为**知识库**使用，包括：
- metadata completeness
- dead links
- orphan pages
- root page coverage
- page-boundary drift
- noise regression
- root-level stray markdown files

> 如果用户要的是**共享项目目录的问卷派发、alignment、assignment、follow-up 或 decision distill**，不要用本 skill；应改用 `knowledge-base-team-coordination`。

## When to use
- 用户要做 wiki/知识库结构审计
- 用户担心 dead links、orphan pages、frontmatter 缺失、导航漂移
- 用户怀疑页面又开始像项目日志，而不像知识库
- 用户要先出审计报告，再决定是否修复

## Default stance
- **默认只审计，不修改。**
- 只有用户明确要求“顺手修掉”“审计并修复”“把发现的问题直接改掉”时，才进入修改模式。
- 若进入修复模式，优先顺序应是：
  1. 结构问题
  2. 导航问题
  3. 治理漂移
  4. 噪音清理

## Required input
在执行审计前，先读取 **vault profile**。

profile 可以通过以下任一方式提供：
- 一个明确的**绝对文件路径**
- 一个附带的 markdown 文件
- 用户直接粘贴的 profile 内容

如果用户只说“read my vault profile”，但没有给路径或文件，不要假定 agent 能自己定位到它。

先读：
- `references/vault-profile-contract.md`
- `references/audit-checklist.md`
- `../../templates/vault-profile-template.md`

没有 profile 时，不要凭空假定哪些文件算 root pages，哪些 markdown 文件允许留在 vault 根目录。
建议优先让用户把 profile 保存成稳定文件，例如 `<vault-root>/vault-profile.md`。

## Fixed page-role model
这套技能默认检查以下页面角色模型：
- `project`
- `knowledge`
- `ops`
- `task`
- `overview`

审计时重点关注：
- 根页是否仍是导航入口
- `knowledge` 是否变成任务页
- `ops` 是否变成流水账
- `task` 是否开始承载长期方法论
- `overview` 是否还能解释当前治理规则

## Core rules
- **先按 profile 审计，再给问题定性。**
- **导航问题优先级高于正文润色。**
- **孤立页指的是没有有效入口，不是“没有相关页面”。**
- **root-level stray markdown files 需要根据 canonical root-level markdown files 判断。**
- **噪音问题按知识库口径判断。** 重点看页面是否还能稳定回答“这是什么 / 怎么做 / 怎么排障”。

## Audit workflow

### 1. Check metadata completeness
- 检查必要 frontmatter 字段
- 检查页面角色与 area 是否符合 profile

### 2. Check navigation coverage
- 页面是否被 reader entrypoint 或对应 root page 收录
- 是否存在“有页面但没有入口”的情况

### 3. Check link validity
- 识别真实 dead links
- 区分示例文字和应该存在的真实链接

### 4. Check page-boundary drift
- 根页是否堆积执行细节
- `knowledge` 页是否写入了当前待办或过程日志
- `ops` 页是否退化成逐日流水账
- `task` 页是否承载长期结构知识
- `overview` 页是否仍解释当前维护回路

### 5. Check noise regression
- 是否重新积累一次性状态、长任务回放、低价值路径噪音
- `log` 是否仍是 milestone-only

### 6. Check root-level stray markdown files
- 扫描 vault 根目录 markdown 文件
- 对照 profile 中允许的 canonical root-level markdown files
- 报告不该留在根目录的历史残片、空文件或误放文件

### 7. Report or fix
- 只审计时：输出 findings 与修复顺序
- 用户要求修复时：按优先级修，再做复检

## Severity model
- **P1**：dead links、orphan pages、missing frontmatter、missing entrypoints、invalid metadata
- **P2**：root page coverage 缺失、治理文档漂移、log 结构失真、明显的 stray root-level files
- **P3**：边界漂移、叙事冗余、噪音回流、标签或标题不清晰

## Output expectations
输出至少包含：
- audit summary
- P1 / P2 / P3 findings
- 影响页面
- 建议修复顺序
- 是否存在 root-level stray files

## Additional resources
- `references/vault-profile-contract.md`：执行审计前必须知道哪些配置
- `references/audit-checklist.md`：推荐审计顺序、检查点和报告模板
- `../../templates/vault-profile-template.md`：可填写的 profile 模板
