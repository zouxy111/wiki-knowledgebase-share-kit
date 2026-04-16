# Workspace Contract

`knowledge-base-team-coordination` 把共享项目目录视为唯一事实源。

## Standard structure

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

## Public interface files
- `project-brief.md`：项目目标、成功标准、范围、约束、产出要求
- `team-roster.md`：成员清单、角色、路径、画像引用
- `members/<id>/questionnaire.md`：AI 生成的问卷
- `members/<id>/response.md`：成员回答
- `members/<id>/assignment.md`：分配结果
- `members/<id>/progress-update.md`：阶段进展
- `members/<id>/decision-distill.md`：成员决策蒸馏
- `coordination/alignment-summary.md`：多方共识与冲突对齐
- `coordination/task-board.md`：共享任务面
- `coordination/decision-register.md`：共享决策登记

## `team-roster.md` minimum fields
- member id
- display name
- canonical profile path（可选）
- project folder path
- declared role
- expected contribution
- current status

## Source-of-truth rule
- 不要把事实分散在聊天描述和目录外临时文件里。
- 任何后续协调都应回读此目录中的最新版本。
- 只有 `approved` 的 artifact 才能作为后续事实源或同步源。
