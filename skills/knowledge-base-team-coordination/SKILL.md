---
name: knowledge-base-team-coordination
description: This skill should be used when the user asks to coordinate a shared project for 2+ people, generate role-aware questionnaires, align different members before assignment, run a multi-person intake workflow, distill team decisions, do 问卷派单, 多人协同, 工作对接, QC 多人协同, or sync stable collaboration knowledge back into a vault. It reads a shared project directory, uses reusable member profiles when available, drafts questionnaires and assignments, tracks approval status, and optionally syncs approved knowledge into the existing knowledge-base model.
---

# Knowledge Base Team Coordination

这个 skill 负责 **2 人及以上** 的共享项目目录协同。

它不替代：
- `knowledge-base-maintenance`
- `knowledge-base-audit`

它的职责是：
- 读取共享项目目录中的项目 brief、成员 roster、资料和已有回答
- 基于成员画像与项目目标生成**成员级问卷草案**
- 汇总回答并生成**对齐摘要**
- 生成**任务分配草案**
- 在收到确认后写入正式任务文件
- 在执行过程中收集阶段性更新，必要时发起补问或重分配
- 在关键节点与结项时输出**决策蒸馏**
- 若提供 vault profile，则同步稳定知识到知识库

## When to use
- 用户要协调 2 人及以上做同一个项目
- 用户要基于不同成员能力做差异化问卷
- 用户要先对齐目标和颗粒度，再派任务
- 用户要把决策蒸馏、协作边界和人物画像沉淀下来
- 用户要跑 QC 多人协同，但又不想把产品做成 QC 专用工具

## Required input
默认先读取共享项目目录。

用户至少应通过以下任一方式提供：
- 共享项目目录的**绝对路径**
- 一个完整附带的项目目录
- 直接粘贴关键文件内容（最低也要有 `project-brief.md` 和 `team-roster.md`）

如果有以下输入，也应一并读取：
- `team-roster.md` 中列出的 canonical member profiles
- 可选 vault profile（仅用于知识库同步）

如果用户没有提供 canonical member profiles：
- 不应失败
- 先通过第一轮问卷建立项目内画像，再继续推进

如果用户没有提供 vault profile：
- 仍应完成项目目录内的问卷、对齐、派单和蒸馏
- 只是不执行知识库同步

## Core operating model
- 默认运行方式是**单协调 AI**，不是每个成员都直接调自己的 AI。
- 本仓库主推在 **OpenClaw** 和 **Hermes** 上承接这个 workflow，但不依赖它们的私有 API。
- 默认成员参与方式是**填写共享项目目录中的 markdown 文件**，不要求实时对话。
- 每位成员可以在自己的个人 wiki / 私有资料区里，用自己的 agent（如 OpenClaw / Hermes / 其他 agent）协助整理问卷回答和进展；但只有同步回 shared project directory 的 markdown 文件才进入正式协调闭环。
- 默认问卷采用**角色模板 + 项目定制**，不是完全自由生成。
- 默认知识库同步是**有 profile 才同步**；没有 profile 时只保留项目目录结果。
- 默认 QC 只是**示例与默认模板来源**，不把产品限制为 QC 专用工具。

## State machine
固定按以下阶段推进：
1. Kickoff
2. Questionnaire
3. Alignment
4. Assignment
5. Follow-up
6. Distill / Closeout

不要把多人协同退化成“一次性生成一张问卷”的 prompt。

## Draft / approval rules
以下文件至少要支持 `status`：
- `members/<id>/questionnaire.md`
- `members/<id>/assignment.md`
- `coordination/alignment-summary.md`
- `coordination/task-board.md`
- `coordination/decision-register.md`

最少支持：
- `draft`
- `approved`
- `superseded`
- `blocked`

固定规则：
- **AI 先生成草案，人确认后落盘。**
- **只有 `approved` 的任务与决策，才允许作为后续事实源。**
- follow-up 阶段如果发生变化，旧版本标记为 `superseded`。
- 如果成员回答颗粒度不一致且信息未补齐，assignment 保持 `draft` 或 `blocked`。

## Dual-layer member profile model
### 1. 跨项目成员画像
长期、稳定、可复用，例如：
- strengths
- weaknesses / support needed
- preferred task granularity
- preferred output formats
- typical decision areas
- recurring constraints
- collaboration style

### 2. 项目内成员上下文
临时、本项目专属，例如：
- 本次负责模块
- 当前手头资料
- 可投入时间
- 本次目标理解
- 当前阻塞

## Workflow expectations
### Kickoff
- 读取 `project-brief.md`、`team-roster.md`、shared materials、成员资料
- 输出项目理解摘要与问卷草案

### Questionnaire
- 为每位成员生成 `questionnaire.md`
- 问题必须覆盖：目标理解、证据/资料掌握、输出颗粒度、依赖关系、约束、待确认决策

### Alignment
- 读取 `response.md`
- 输出 `coordination/alignment-summary.md`
- 明确共识、冲突点、缺口、待确认项、颗粒度不一致

### Assignment
- 生成成员级 `assignment.md` 和共享 `coordination/task-board.md`
- 默认标记为 draft
- 人确认后再标记为 approved

### Follow-up
- 读取 `progress-update.md`
- 输出补问、任务重排、依赖提醒、风险升级
- 如项目范围变化，旧 assignment 必须标记为 `superseded`

### Distill / Closeout
- 生成成员级 `decision-distill.md`
- 汇总到 `coordination/decision-register.md`
- 若提供 vault profile，则同步稳定能力/决策到知识库

## Optional vault sync
若存在 vault profile，默认同步两类内容：
- **人物画像增量**：长期有效的能力 / 偏好 / 约束变化
- **稳定决策蒸馏**：未来项目仍可复用的判断规则、协同模式、任务边界、问卷策略

同步时必须遵守现有 kit 的 page-role model，不能新增第二套治理模型。

## Recommended response shape
执行后至少说明：
- 当前阶段
- 读取了哪些文件
- 生成或更新了哪些草案 / 正式文件
- 哪些内容仍待确认
- 是否发现颗粒度不一致 / 资料缺口 / 范围变更
- 是否执行了 vault sync；如未执行，是因为缺 profile 还是用户不需要

## Additional resources
- `references/workspace-contract.md`
- `references/state-machine.md`
- `references/member-profile-model.md`
- `references/questionnaire-and-status-rules.md`
- `references/vault-sync-contract.md`
- `../../docs/team-coordination-workflow.md`
- `../../docs/collaboration-integration-patterns.md`
- `../../templates/member-capability-profile-template.md`
- `../../templates/team-project-workspace/README.md`
