# Coordination State Machine

## 1. Kickoff
读取：
- `project-brief.md`
- `team-roster.md`
- `shared-materials/`
- `members/<id>/member-context.md`
- 可选 canonical member profiles

输出：
- 项目理解摘要
- `questionnaire.md` drafts

## 2. Questionnaire
固定覆盖：
- 目标理解
- 资料 / 证据掌握
- 输出颗粒度
- 依赖关系
- 约束
- 待确认决策

## 3. Alignment
读取 `response.md` 后产出：
- `coordination/alignment-summary.md`

必须明确：
- 共识
- 冲突
- 缺口
- 待确认项
- 颗粒度不一致

## 4. Assignment
生成：
- `members/<id>/assignment.md`
- `coordination/task-board.md`

默认：
- `draft`
- 人确认后才变 `approved`

## 5. Follow-up
读取：
- `progress-update.md`
- 更新后的 `project-brief.md`

输出：
- 补问
- 任务重排
- 依赖提醒
- 风险升级

如果范围变化：
- 旧 assignment 标记 `superseded`
- 重新生成 alignment 与新任务草案
- 在 decision register 记录变更原因

## 6. Distill / Closeout
生成：
- `members/<id>/decision-distill.md`
- `coordination/decision-register.md`

只有 `approved` 的稳定结论才允许外部复用或知识库同步。
