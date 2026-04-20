# Project Management Workflow

> 这份文档专门解释 share kit 里的 **PM 主线**：
> 如何在不污染业务 area 和 governance 的前提下，把项目 owner 推进、多人协同和交付审计串成闭环。

---

## 1. 这是什么

这是当前核心 share kit 里的**可选主线**：
- 新 area：`project-management`
- 新 skill：`knowledge-base-project-management`
- 现有 specialist：`knowledge-base-team-coordination`
- 新 skill：`knowledge-base-delivery-audit`

它解决的不是“再造一套业务知识库”，而是：
- 项目 owner 怎么推进
- 多人事项什么时候进入 coordination
- 项目声称完成时怎么严审是否闭环

---

## 2. 渐进式加载，而不是强推

默认 onboarding 仍先走原本的知识库维护主线：
- `knowledge-base-kit-guide`
- `knowledge-base-orchestrator`
- `knowledge-base-ingest`
- `knowledge-base-maintenance`
- `knowledge-base-audit`

只有当用户明确出现这些 PM 意图时，才推荐进入 PM 主线：
- 项目管理
- 周计划
- 里程碑
- blocker
- dependency
- handoff
- delivery review
- ready / greenlight
- 项目复盘

所以：

> `project-management` 是核心包里的正式能力，但不是所有用户第一次都必须配置的 area。

---

## 3. `project-management` area 的边界

### 放这里的内容
- 项目组合视图
- owner 视角推进板
- 风险 register
- 决策 register
- delivery gates
- PM operating model

### 不放这里的内容
- 业务知识正文
- 业务运维细节
- 原始长文档导入正文
- 本应回到业务 area 的稳定事实

正确边界：
- 业务事实 → 原 area
- 治理规则 → `governance`
- 项目管理方法 / 看板 / gate / register → `project-management`

---

## 4. 固定 3 个板块

### A. 组合 / 项目总览板块
建议模板：
- `project-project-management-overview.md`
- `pm-portfolio-board.md`
- `pm-operating-model.md`

看这些问题：
- 当前有哪些项目
- 每个项目 owner / 阶段 / 优先级 / 成功标准是什么
- 哪些项目 `active / blocked / done / parked`

### B. 团队协同板块
这里不重复发明第二套能力。

正式入口仍是：
- `knowledge-base-team-coordination`

负责：
- 共享项目目录
- 问卷
- alignment
- assignment
- follow-up
- decision distill

### C. 个人执行板块
建议模板：
- `pm-personal-execution-board.md`
- `pm-weekly-review-ops.md`
- `pm-risk-register.md`
- `pm-decision-register.md`

看这些问题：
- 本周推进什么
- 当前 blocker / dependency 是什么
- 下一步动作是什么
- 哪些结论该继续留在 journal，哪些该升到稳定板面

---

## 5. 3 个 PM 相关 skills 的分工

### `knowledge-base-project-management`
负责：
- intake
- 项目摘要
- 拆解 / 优先级 / 里程碑
- 风险 / 依赖
- owner 执行板
- routing

### `knowledge-base-team-coordination`
负责：
- 2 人及以上共享项目目录
- 问卷 / alignment / assignment / follow-up / distill

不负责：
- 单人 owner 的 portfolio / execution board
- 直接替代 delivery gate 审计

### `knowledge-base-delivery-audit`
负责：
- 交付闭环
- 证据缺口
- ready / blocked / greenlight pending
- handoff / closeout gate

不负责：
- 知识库结构健康检查

---

## 6. 推荐模板族

请复制：
- `templates/project-management/`

包含：
- `project-project-management-overview.md`
- `pm-portfolio-board.md`
- `pm-operating-model.md`
- `pm-personal-execution-board.md`
- `pm-weekly-review-ops.md`
- `pm-delivery-gates.md`
- `pm-risk-register.md`
- `pm-decision-register.md`

---

## 7. 默认状态语义

### Artifact 级
- `draft`
- `approved`
- `blocked`
- `superseded`

### 项目级
- `active`
- `blocked`
- `done`
- `parked`

说明：
- `greenlight` 不是普通 artifact 状态
- `greenlight` 应由 `knowledge-base-delivery-audit` 在 closeout / approval 前后给出结论，而不是 PM board 直接自我声明

---

## 8. 推荐使用顺序

### 场景 A：单人项目 owner
1. `knowledge-base-project-management`
2. 如形成稳定结论 → `knowledge-base-maintenance`
3. 如准备结项 → `knowledge-base-delivery-audit`

### 场景 B：多人项目
1. `knowledge-base-project-management`
2. 识别多人事项后转 `knowledge-base-team-coordination`
3. approved 结果回业务 area 时转 `knowledge-base-maintenance`
4. closeout 前转 `knowledge-base-delivery-audit`

### 场景 C：只是普通知识库维护
仍然可以完全不进入 PM 主线。

---

## 9. 一句最稳的对外说法

> 这套 share kit 仍然首先是知识库维护包；但当你需要项目 owner 视角推进、多人协同对齐和交付闭环审计时，它也提供一条可渐进加载的 PM 主线，而不会把业务知识和治理页面混成一团。
