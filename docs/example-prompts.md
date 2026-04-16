# Example Prompts

## 0. 以轻量 harness 方式导入一本 markdown 书到知识库

```text
Use $knowledge-base-ingest to import this long Markdown document into my knowledge base.
Read my vault profile first.
Create a minimal workable overview/chapter/topic structure with source lineage, toc, glossary candidates, and related-link suggestions.
Treat the first import as a testable baseline rather than the final structure.
Use a lightweight harness mindset: keep versioned structure outputs, compare split strategies across iterations, refine page roles, improve link architecture, and run regression-style checks on navigation, lineage, and entry pages after each iteration.
Sync the stabilized structure back to the required entry pages.
```

## 1. 第一次安装后，不知道怎么开始

```text
Use $knowledge-base-kit-guide to walk me through this share kit.
My vault profile will be at /ABSOLUTE/PATH/TO/vault-profile.md .
My shared project directory will be at /ABSOLUTE/PATH/TO/team-project/ .
If either input is incomplete, tell me the minimum setup I still need, then tell me which skill I should use next.
```

## 2. 我已经有 profile，想沉淀一轮任务结果

```text
Use $knowledge-base-maintenance to integrate this task into my markdown knowledge base.
My vault profile is at /ABSOLUTE/PATH/TO/vault-profile.md .
Read that file first. Keep only durable conclusions or reusable troubleshooting knowledge, choose the right page role, and sync the target page, relevant root page, reader entrypoint, and milestone log.
```

## 3. 我怀疑 wiki 结构已经乱了

```text
Use $knowledge-base-audit to inspect my knowledge base.
My vault profile is at /ABSOLUTE/PATH/TO/vault-profile.md .
Read that file first, then report dead links, orphan pages, missing entrypoints, metadata issues, page-boundary drift, noise regression, and stray markdown files at the vault root.
```

## 4. 多人协同 Kickoff：先生成问卷草案

```text
Use $knowledge-base-team-coordination to start this shared project.
The shared project directory is at /ABSOLUTE/PATH/TO/team-project/ .
If team-roster.md includes canonical member profile paths, read them too.
If I want stable outputs synced into a knowledge base, my vault profile is at /ABSOLUTE/PATH/TO/vault-profile.md .
First produce a project understanding summary and member-level questionnaire drafts. Do not treat drafts as approved facts.
```

## 5. 多人协同 Alignment：读取回答并生成对齐摘要

```text
Use $knowledge-base-team-coordination on /ABSOLUTE/PATH/TO/team-project/ .
Read every members/<id>/response.md file that already exists.
Then update coordination/alignment-summary.md and tell me:
- what is aligned,
- what conflicts remain,
- whether anyone answered at a much coarser or finer granularity,
- and whether assignments should stay draft, approved, or blocked.
```

## 6. 多人协同 Assignment：生成成员任务与共享 task-board

```text
Use $knowledge-base-team-coordination on /ABSOLUTE/PATH/TO/team-project/ .
Read the latest approved or draft alignment summary, then generate members/<id>/assignment.md and coordination/task-board.md as drafts.
Make sure the member assignments and the shared task board stay consistent.
Do not mark them approved until I confirm.
```

## 7. 多人协同 Follow-up：根据进展做补问或重排

```text
Use $knowledge-base-team-coordination on /ABSOLUTE/PATH/TO/team-project/ .
Read every members/<id>/progress-update.md plus the latest project-brief.md.
If scope changed, supersede the old assignments and regenerate the alignment and task draft.
If responses or updates are too uneven in granularity, generate follow-up questions before approving new assignments.
```

## 8. 多人协同结项：生成决策蒸馏并可选同步知识库

```text
Use $knowledge-base-team-coordination on /ABSOLUTE/PATH/TO/team-project/ .
Generate members/<id>/decision-distill.md and coordination/decision-register.md.
Only sync stable, approved decisions and durable member-profile updates into my knowledge base if a vault profile is available.
If no vault profile is provided, write only to the project directory and treat that as expected behavior rather than failure.
```

## 9. 中文首次上手

```text
用 $knowledge-base-kit-guide 帮我开始用这套分享包。
我现在不确定应该走知识库维护流程，还是多人协同流程。
我的 vault profile 会放在 /绝对路径/vault-profile.md 。
我的共享项目目录会放在 /绝对路径/team-project/ 。
如果输入还没配完整，请先告诉我最少要补哪些信息，再告诉我下一步应该调用哪个 skill。
```

## 10. 中文多人协同启动

```text
用 $knowledge-base-team-coordination 帮我启动这个多人协同项目。
共享项目目录在 /绝对路径/team-project/ 。
如果 roster 里引用了 canonical member profiles，请一并读取。
如果我要把稳定结果同步回知识库，我的 vault profile 在 /绝对路径/vault-profile.md 。
先输出项目理解摘要和成员级 questionnaire.md 草案，不要直接把任务标记成 approved。
```

## 11. 中文多人协同跟进

```text
用 $knowledge-base-team-coordination 继续这个项目。
共享项目目录在 /绝对路径/team-project/ 。
请读取已有的 response.md、assignment.md、progress-update.md 和 coordination/status.md 。
如果项目范围变了，就把旧 assignment 标记为 superseded，再重新生成 alignment 和新的任务草案。
如果有人回答过粗或过细，请先补问，不要直接批准任务。
```

## 12. 成员用 OpenClaw / Hermes 协助填写问卷

```text
Use OpenClaw or Hermes to help one member answer the questionnaire for this shared project.
The member will work in their own wiki or private notes first, but the final answer must be written back into members/<id>/response.md inside the shared project directory.
Do not treat personal notes as team facts until the markdown has been synced back into the shared project directory.
```

## 13. 中文：成员先在个人 wiki 里整理，再同步回 shared project directory

```text
请用 OpenClaw 或 Hermes 协助这位成员回答问卷。
她会先在自己的 wiki / 私有资料区里整理草稿，但最终进入团队协作闭环的版本，必须写回共享项目目录里的 members/<id>/response.md 。
不要把个人 wiki 中尚未同步的内容当成 coordinator 的正式事实源。
```
