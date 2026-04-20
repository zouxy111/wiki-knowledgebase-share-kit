# Example Prompts

## 1. 零门槛初始化（推荐给完全新手）

```text
Use $knowledge-base-orchestrator to help me set up this knowledge-base package.
Check whether I already have a usable vault first. Only offer Obsidian installation if I actually need it. Create a vault skeleton if needed, generate a vault profile, and then tell me which skill to use next.
```

```text
用 $knowledge-base-orchestrator 帮我初始化这套知识库维护包。
先检查我是不是已经有可用的 vault；只有在我真的需要时才建议安装 Obsidian。
如有必要就创建骨架、生成 vault profile，然后告诉我下一步该用哪个 skill。
```

## 2. 我想先理解再动手

```text
Use $knowledge-base-kit-guide to walk me through this share kit.
I want to understand the profile first, then know which of the 10 skills I should use next.
Keep the default path narrow unless I explicitly ask for project-management workflows.
```

```text
用 $knowledge-base-kit-guide 帮我理解这套知识库维护包。
我想先搞清楚 profile、安装方式和 10 个 skill 的分工，再决定下一步用哪个。
如果我没明确提项目管理，就先不要强推 PM 主线。
```

## 3. 以轻量 harness 方式导入一本 markdown 书到知识库

```text
Use $knowledge-base-ingest to import this long Markdown document into my knowledge base.
Read my vault profile first.
For large sources, do not rely on a single direct read. First run bounded splitting to produce chunk files, manifest.json, and coverage-map.md; then process every chunk and keep the import in draft/partial state until coverage verification passes.
Create a minimal workable overview/chapter/topic structure with source lineage, toc, glossary candidates, and related-link suggestions.
Treat the first import as a testable baseline rather than the final structure.
Use a lightweight harness mindset: keep versioned structure outputs, compare split strategies across iterations, refine page roles, improve link architecture, and run regression-style checks on navigation, lineage, and entry pages after each iteration.
Sync the stabilized structure back to the required entry pages.
```

## 3B. 对超大文本启用分块精读

```text
Use $knowledge-base-ingest to import this oversized Markdown source into my knowledge base.
Read my vault profile first.
Do not treat this as a one-pass import. Switch into close-reading mode:
split the source into chunks, create batch packets, maintain a rolling reading state, extract one JSON note per batch, and only then synthesize chapter summaries, topic candidates, glossary seeds, and overview pages.
Keep the run resumable so the next iteration can continue from completed batches instead of rereading the whole source.
If the source changes later, rerun only the changed batches and generate candidate pages plus a candidate link map for final landing.
Write draft frontmatter into candidate pages so they are closer to real vault pages instead of plain notes.
```

## 4. 我已经有 profile，想沉淀一轮任务结果

```text
Use $knowledge-base-maintenance to integrate this task into my markdown knowledge base.
Read my vault profile first. Keep only durable conclusions or reusable troubleshooting knowledge, choose the right page role, and sync the target page, relevant root page, reader entrypoint, and milestone log.
```

## 5. 我怀疑 wiki 结构已经乱了

```text
Use $knowledge-base-audit to inspect my knowledge base.
Read the vault profile first, then report dead links, orphan pages, missing entrypoints, metadata issues, page-boundary drift, noise regression, and stray markdown files at the vault root.
```

## 6. 先审计，再修

```text
Use $knowledge-base-audit first to inspect my vault and list findings by priority.
Then use $knowledge-base-maintenance to fix the high-priority issues while preserving the page-role model.
```

## 7. 从持续沟通中更新 working profile

```text
Use $knowledge-base-working-profile to update my working profile from our recent interactions.
Read my vault profile first, keep only collaboration-relevant stable signals, separate confirmed / repeated / inferred items, filter sensitive personal data, and sync the target profile page according to its visibility rules.
```

## 8. 单人 / owner 视角推进项目

```text
Use $knowledge-base-project-management to help me run this project.
Read my vault profile and the relevant brief / recent journal / current blockers first.
Generate a concise project summary, milestones, risks, dependencies, and a personal execution board.
Only suggest the optional project-management area if PM workflows are actually needed.
```

```text
用 $knowledge-base-project-management 帮我推进这个项目。
先读 vault profile，以及相关 brief / 最近 journal / 当前 blocker。
输出项目摘要、里程碑、风险、依赖和个人执行板。
只有在 PM 工作流确实需要时，再建议我启用可选的 project-management area。
```

## 9. 协调一个多人共享项目

```text
Use $knowledge-base-team-coordination to coordinate this shared project.
Read the shared project directory first, generate role-aware questionnaires, summarize alignment gaps, keep assignments in draft until approved, and distill reusable decisions at closeout.
```

```text
用 $knowledge-base-team-coordination 协调这个共享项目。
先读取共享项目目录，生成成员级问卷，总结对齐缺口，在确认前保持 assignment 为 draft，并在结项时输出可复用的决策蒸馏。
```

## 9B. 用个人 agent 协助成员填写问卷

```text
Use OpenClaw / Hermes / my own agent to help me answer the questionnaire in members/<id>/questionnaire.md.
Work in my personal wiki or private notes first if needed, but only write the final answer back into members/<id>/response.md in the shared project directory.
Do not treat my private draft notes as the coordinator's source of truth.
```

## 10. 检查这个项目是否真的 ready

```text
Use $knowledge-base-delivery-audit to review whether this project is actually ready.
Read the project brief, current task or assignment artifacts, decision records, and evidence first.
Report missing proof, missing write-backs, missing decisions, and whether the current state should stay blocked, move to ready, or wait for greenlight approval.
```

```text
用 $knowledge-base-delivery-audit 审这个项目是不是真的 ready。
先读项目 brief、当前任务 / assignment 工件、决策记录和证据。
指出缺失的证据、缺失的回写、缺失的决策，并判断当前状态应该继续 blocked、进入 ready，还是等待 greenlight 审批。
```

## 11. 记录今天的工作 / 会议纪要

```text
Use $work-journal to create today's work log.
Include timestamps, project associations, meeting notes, temporary ideas, and any distillation hooks worth revisiting later.
```

## 12. 从本周 journal 生成周报

```text
Use $work-journal to distill a weekly summary from my journal entries this week.
Highlight key achievements, decisions made, blockers, and knowledge worth sending back into the knowledge base.
```
