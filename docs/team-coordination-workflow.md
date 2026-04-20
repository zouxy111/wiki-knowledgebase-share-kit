# Team Coordination Workflow

> 这份文档专门解释 `knowledge-base-team-coordination`：  
> 它如何在共享项目目录上跑 **2 人及以上** 的问卷派单、目标对齐、跟进重排和决策蒸馏。

---

## 1. 这是什么

这是当前 **10-skill core share kit** 里的一个 specialist skill：
- 名称固定为：`knowledge-base-team-coordination`
- 面向：2 人及以上的共享项目目录工作流
- 默认运行模型：**单协调 AI + 共享项目目录唯一事实源**

它不是 QC 专用产品。  
QC 只是默认示例之一。

---

## 2. 它在 PM 主线里的位置

它现在是 PM 主线里的**多人 specialist**：
- `knowledge-base-project-management` 负责 owner 视角的 intake / milestone / blocker / priority
- `knowledge-base-team-coordination` 负责 shared project directory 上的多人成员问卷、alignment、assignment、follow-up、distill
- `knowledge-base-delivery-audit` 负责交付闭环、ready / blocked / greenlight 审计

也就是说：

> team coordination 负责多人事实层，不负责代替 portfolio board，也不负责代替 closeout gate。

---

## 3. 什么时候该用它

适用：
- 你要协调 2 人及以上做同一个项目
- 每个人的能力、颗粒度、资料掌握程度不同
- 你希望 AI 先做 intake，再按角色差异发问卷
- 你希望对齐结果、任务分配、决策蒸馏都落到共享目录里

不适用：
- 你只是要把某次任务写回知识库 → 用 `knowledge-base-maintenance`
- 你只是要检查知识库结构健康 → 用 `knowledge-base-audit`
- 你只是要做项目 owner 视角的推进板 → 用 `knowledge-base-project-management`
- 你要审“是否真的 ready / 能不能 greenlight” → 用 `knowledge-base-delivery-audit`

---

## 4. 主推平台与推荐接入方式

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

## 5. 共享项目目录契约

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

这些文件是公开接口：
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

## 6. 双层成员画像模型

### A. 跨项目成员画像
长期、稳定、可复用。  
模板：
- `templates/member-capability-profile-template.md`

### B. 项目内成员上下文
记录在：
- `members/<id>/member-context.md`

如果 `team-roster.md` 里没有 `canonical profile path`：
- 不应失败
- 应先通过第一轮问卷建立项目内画像，再继续派单

---

## 7. 固定状态机

### 1) Kickoff
读取：
- `project-brief.md`
- `team-roster.md`
- `shared-materials/`
- `members/<id>/member-context.md`
- 可选 canonical member profiles

输出：
- 项目理解摘要
- 问卷草案

### 2) Questionnaire
AI 为每位成员生成 `questionnaire.md`。  
问题来源必须是：
- **角色模板**
- 加上 **项目定制**

### 3) Alignment
读取成员 `response.md`，生成：
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
- 更新后的 `project-brief.md`

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

---

## 8. 与 PM / delivery audit 的边界

### 继续留在 team coordination 的内容
- 问卷
- alignment
- assignment
- follow-up
- team decision distill

### 应该转 project-management 的内容
- owner 视角的周计划
- 里程碑推进
- blocker / dependency 总览
- portfolio board

### 应该转 delivery-audit 的内容
- 是否真的完成
- 证据是否齐全
- 回写是否齐全
- 能不能 ready / greenlight

---

## 9. 一句最稳的对外说法

> `knowledge-base-team-coordination` 是这套 share kit 里的多人 specialist：它把共享项目目录当成唯一事实源，让 OpenClaw / Hermes 或其他 agent runtime 上的成员可以并行回答问卷和更新进展，同时让 coordinator 统一做 alignment、assignment 和 decision distill。
