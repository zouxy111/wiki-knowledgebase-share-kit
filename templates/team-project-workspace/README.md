# Team Project Workspace Template

> 用途：给 `knowledge-base-team-coordination` 提供一个**可直接复制**的共享项目目录骨架。
> 建议：复制整个目录后，把 `members/member-template/` 复制成实际成员目录，例如 `members/alice/`、`members/bob/`。

## 固定原则
- 共享项目目录是唯一事实源
- 多人协同默认由**单协调 AI** 驱动
- `questionnaire.md`、`assignment.md`、`coordination/alignment-summary.md`、`coordination/task-board.md`、`coordination/decision-register.md` 都必须支持 `status`
- 默认状态至少支持：`draft / approved / superseded / blocked`
- 只有 `approved` 的任务与决策，才允许成为后续事实源或知识库同步来源

## 复制后先填哪些文件
1. `project-brief.md`
2. `team-roster.md`
3. `members/<id>/member-context.md`
4. `shared-materials/`
5. 如有长期成员画像，把绝对路径填到 `team-roster.md` 的 `canonical profile path`

## 推荐协作工作模式
- 共享项目目录仍是唯一事实源
- 每位成员可以在自己的个人 wiki / 私有资料区里整理资料和草稿
- 每位成员可以使用自己的 agent（如 OpenClaw / Hermes / 其他 agent）协助填写 `questionnaire.md`、整理 `response.md`、更新 `progress-update.md`
- 但 coordinator 默认只把**已同步回 shared project directory 的 markdown 文件**视为正式输入
- `team-project/` 可以独立放在 NAS / 网盘同步目录中，也可以嵌入共享 wiki / 共享知识库子目录中

## 与 PM 主线的关系
- 如果你还需要项目 owner 视角的里程碑 / blocker / portfolio / delivery gate，请额外复制 `templates/project-management/`
- `team-project/` 仍只负责多人协同事实层，不代替 `project-management` area

## 目录结构

```text
team-project/
  project-brief.md
  team-roster.md
  shared-materials/
  members/
    member-template/
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
