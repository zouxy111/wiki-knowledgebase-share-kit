---
name: knowledge-base-project-management
description: This skill should be used when the user wants project intake, owner-side project management, weekly planning, milestone planning, blockers, dependencies, portfolio view, handoff planning, greenlight preparation, project review, 周计划, 里程碑, blocker, 项目管理, 项目拆解, next actions, or a management-layer board that does not mix business facts into governance. It reads the vault profile and relevant project inputs, drafts management-layer artifacts, routes multi-person work into team coordination, and routes durable conclusions into maintenance.
---

# Knowledge Base Project Management

这个 skill 负责 **项目 owner / 单人推进 / 管理层视角** 的项目管理主线。

它不替代：
- `knowledge-base-maintenance`
- `knowledge-base-audit`
- `knowledge-base-team-coordination`
- `knowledge-base-delivery-audit`

它的职责是：
- 读取项目 brief、最近 journal、当前 blocker、已有任务板
- 生成**项目摘要 / 项目分解 / 里程碑 / 风险与依赖**
- 维护 **portfolio / team / personal execution** 三层管理视图里的管理层材料
- 明确哪些事项应该升级成多人协同事项，转交 `knowledge-base-team-coordination`
- 明确哪些稳定结论应回写业务 area，转交 `knowledge-base-maintenance`
- 明确哪些交付应该进入 ready / blocked / greenlight 审计，转交 `knowledge-base-delivery-audit`

## When to use
- 用户要做项目 intake、项目拆解、优先级判断或里程碑规划
- 用户要维护“本周推进什么 / 下一个动作是什么 / 当前 blocker 是什么”
- 用户要建立项目组合视图或项目 owner 看板
- 用户要把 journal 里的执行线索提升成稳定任务板
- 用户要判断哪些事项需要转入多人协同、哪些事项还停留在单人推进

## When not to use
- 你只是要把稳定业务知识写回原 area → 用 `knowledge-base-maintenance`
- 你只是要协调 2 人及以上共享项目目录 → 用 `knowledge-base-team-coordination`
- 你只是要检查知识库结构健康 → 用 `knowledge-base-audit`
- 你要审“任务是不是已经真完成、证据是不是齐了、能不能 greenlight” → 用 `knowledge-base-delivery-audit`

## Required input
默认先读取：
- vault profile（如果涉及知识库内页更新）
- 项目 brief / 项目目标描述
- 当前项目 owner 手头的 blocker、依赖、待办
- 最近相关 journal / task / project 页面

如果用户还没配置 `project-management` area：
- 不应直接失败
- 先说明这是 **可选管理层 area**
- 仍可先输出 PM 草案
- 在用户明确要采用 PM 主线时，再建议复制 `templates/project-management/`

## Core operating model
- `project-management` 是**管理层 area**，不是业务事实总库。
- 业务事实仍回原 area，例如 `pathology / openclaw / qc / medical-guidelines`。
- `governance` 继续放全库规则、维护规范、审计口径。
- `project-management` 只放组合视图、执行节奏、风险、门禁、决策与项目管理模板。

## Three-board model
`project-management` 内默认固定三块：

### 1. Portfolio / 项目总览板块
看：
- 当前有哪些项目
- owner / 阶段 / 成功标准 / 优先级
- 哪些是 `active / blocked / done / parked`

### 2. Team coordination / 团队协同板块
不另造第二套能力，直接链接：
- `knowledge-base-team-coordination`

### 3. Personal execution / 个人执行板块
看：
- 本周推进什么
- blocker / dependency
- next actions
- 哪些信息仍留在 journal，哪些要升级成 task / project / knowledge

## State semantics
### Artifact status
- `draft`
- `approved`
- `blocked`
- `superseded`

### Project-level execution state
- `active`
- `blocked`
- `done`
- `parked`

## Workflow expectations
### 1. Intake
- 先把项目目标、成功标准、范围、当前阶段压成一个简明摘要
- 明确 owner、当前节奏、关键风险和关键依赖

### 2. Decomposition
- 把项目拆成：
  - milestones
  - workstreams
  - next actions
  - risks / dependencies
- 明确哪些 workstream 已经超出“单人 owner 推进”范围

### 3. Routing
- 需要多人目标对齐、能力分工、问卷派单 → 转 `knowledge-base-team-coordination`
- 稳定结论已经形成，可进入知识库 → 转 `knowledge-base-maintenance`
- 要做交付验收、缺口审计、greenlight 判断 → 转 `knowledge-base-delivery-audit`

### 4. Execution board update
- 更新 `pm-portfolio-board`
- 更新 `pm-personal-execution-board`
- 必要时更新风险 / 决策 register

## Recommended response shape
执行后至少说明：
- 读了哪些输入
- 当前项目摘要是什么
- 识别出的 milestones / risks / blockers / next actions
- 哪些内容属于 PM area，哪些仍应留在业务 area
- 哪些事项要转给 team coordination / maintenance / delivery audit
- 如果用户还没启用 PM area，下一步该复制哪些模板

## Additional resources
- `references/operating-model.md`
- `references/board-family.md`
- `references/routing-boundaries.md`
- `references/status-model.md`
- `../../docs/project-management-workflow.md`
- `../../templates/project-management/README.md`
