# Team Coordination Workflow

> 这份文档专门解释 `knowledge-base-team-coordination`：
> 它如何在共享项目目录上跑 **2 人及以上** 的问卷派单、目标对齐、跟进重排和决策蒸馏。

---

## 1. 这是什么

这是当前 **8-skill knowledge-base package** 里的一个 specialist skill：
- 名称固定为：`knowledge-base-team-coordination`
- 面向：2 人及以上的共享项目目录工作流
- 默认运行模型：**单协调 AI + 共享项目目录唯一事实源**

它不是 QC 专用产品。
QC 只是默认示例之一。

---

## 2. 什么时候该用它

适用：
- 你要协调 2 人及以上做同一个项目
- 每个人的能力、颗粒度、资料掌握程度不同
- 你希望 AI 先做 intake，再按角色差异发问卷
- 你希望对齐结果、任务分配、决策蒸馏都落到共享目录里

不适用：
- 你只是要把某次任务写回知识库 → 用 `knowledge-base-maintenance`
- 你只是要检查知识库结构健康 → 用 `knowledge-base-audit`
- 你还没准备共享项目目录，或还没想清楚整体分流 → 先用 `knowledge-base-kit-guide` 或 `knowledge-base-orchestrator`

---

## 3. 主推平台与推荐接入方式

本仓库把 **OpenClaw** 和 **Hermes** 视为主推运行平台。

这里说的“无缝接入”，默认是指：
- 使用同一套 shared project directory 契约
- 承接同一套 `knowledge-base-team-coordination` 工作流
- 复用相同的 skills / prompts / markdown 协作协议
- 不依赖平台私有 API

推荐工作模式是：
- coordinator AI 负责读取共享项目目录并驱动主流程
- 每位成员可以在自己的个人 wiki / 私有资料区里整理材料和草稿
- 每位成员可以用自己的 agent（如 OpenClaw / Hermes）协助回答问卷或整理回应
- 但只有**同步回 shared project directory 的 markdown 文件**才进入正式协调闭环

推荐同步拓扑有两种：
1. `team-project/` 独立放在 NAS / 网盘同步目录
2. `team-project/` 嵌入共享 wiki / 共享知识库的子目录

无论选哪种拓扑，shared project directory 都始终是协调事实源。

详见：`docs/collaboration-integration-patterns.md`

---

## 4. 共享项目目录契约

请直接复制：
- `templates/team-project-workspace/`

固定推荐结构：

```text
team-project/
  project-brief.md
  team-roster.md
  shared-materials/
  members/
    <member-id>/
      member-context.md
      materials/
      questionnaire.md
      response.md
      assignment.md
      progress-update.md
      decision-distill.md
  coordination/
    alignment-summary.md
    task-board.md
    decision-register.md
    status.md
```

其中这些文件是公开接口：
- `project-brief.md`
- `team-roster.md`
- `members/<id>/questionnaire.md`
- `members/<id>/response.md`
- `members/<id>/assignment.md`
- `members/<id>/progress-update.md`
- `members/<id>/decision-distill.md`
- `coordination/alignment-summary.md`
- `coordination/task-board.md`
- `coordination/decision-register.md`

---

## 5. 双层成员画像模型

### A. 跨项目成员画像
长期、稳定、可复用。

模板：
- `templates/member-capability-profile-template.md`

典型字段：
- identity / display name
- strengths
- weaknesses / support needed
- preferred task granularity
- preferred output formats
- typical decision areas
- recurring constraints
- collaboration style
- reusable notes from past projects

### B. 项目内成员上下文
记录在：
- `members/<id>/member-context.md`

典型内容：
- 本次负责模块
- 当前手头资料
- 本次可投入时间
- 当前目标理解
- 当前阻塞

如果 `team-roster.md` 里没有 `canonical profile path`：
- 不应失败
- 应先通过第一轮问卷建立项目内画像，再继续派单

---

## 6. `team-roster.md` 最小字段

每位成员最少要有：
- `member id`
- `display name`
- `canonical profile path`（可选）
- `project folder path`
- `declared role`
- `expected contribution`
- `current status`

建议固定成表格，便于 AI 和人都能快速核对。

---

## 7. 固定状态机

### 1) Kickoff
读取：
- `project-brief.md`
- `team-roster.md`
- `shared-materials/`
- 成员目录中的 `member-context.md`
- 可选：canonical member profiles

输出：
- 项目理解摘要
- 问卷草案

### 2) Questionnaire
AI 需要为每位成员生成 `questionnaire.md`。
问题来源不是随意 prompt，而是：
- **角色模板**
- 加上 **项目定制**

固定覆盖：
- 目标理解
- 资料 / 证据掌握
- 输出颗粒度
- 依赖关系
- 约束
- 待确认决策

### 3) Alignment
读取成员的 `response.md`，生成：
- `coordination/alignment-summary.md`

至少要写清楚：
- 共识
- 冲突点
- 缺口
- 待确认项
- 颗粒度不一致

### 4) Assignment
生成：
- `members/<id>/assignment.md`
- `coordination/task-board.md`

默认先是 `draft`。
只有人确认后，才改成 `approved`。

### 5) Follow-up
读取：
- `progress-update.md`
- 以及更新后的 `project-brief.md`

输出：
- 补问
- 任务重排
- 依赖提醒
- 风险升级

### 6) Distill / Closeout
生成：
- `members/<id>/decision-distill.md`
- `coordination/decision-register.md`

如提供 vault profile，则可同步稳定知识到知识库。
