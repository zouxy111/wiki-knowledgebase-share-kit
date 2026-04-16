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
I have not configured my vault profile yet. Tell me the minimum setup I need, then tell me which skill I should use next.
```

## 2. 我已经有 profile，想沉淀一轮任务结果

```text
Use $knowledge-base-maintenance to integrate this task into my markdown knowledge base.
Read my vault profile first. Keep only durable conclusions or reusable troubleshooting knowledge, choose the right page role, and sync the target page, relevant root page, reader entrypoint, and milestone log.
```

## 3. 我怀疑 wiki 结构已经乱了

```text
Use $knowledge-base-audit to inspect my knowledge base.
Read the vault profile first, then report dead links, orphan pages, missing entrypoints, metadata issues, page-boundary drift, noise regression, and stray markdown files at the vault root.
```

## 4. 先审计，再修

```text
Use $knowledge-base-audit first to inspect my vault and list findings by priority.
Then use $knowledge-base-maintenance to fix the high-priority issues while preserving the page-role model.
```

## 5. 中文首次上手

```text
用 $knowledge-base-kit-guide 帮我开始用这套知识库维护包。
我还没有配 vault profile，请先告诉我最少要补哪些信息，再告诉我下一步应该调用哪个 skill。
```

## 6. 中文写入知识库

```text
用 $knowledge-base-maintenance 把这次结果沉淀进我的知识库。
先读 vault profile，再过滤过程噪音，按页面角色归类，并同步目标页、root page、reader entry 和 milestone log。
```

## 7. 中文结构体检

```text
用 $knowledge-base-audit 审计我的知识库。
先读 vault profile，再检查死链、孤立页、metadata、页面边界漂移、噪音回流，以及根目录 stray markdown 文件。
```

## 8. 一键配置环境（新手推荐）

```text
Use $knowledge-base-orchestrator to help me set up my knowledge base from scratch.
Auto-detect my environment, install Obsidian if needed, create the vault structure, and generate a vault profile.
```

或中文：

```text
用 $knowledge-base-orchestrator 帮我从零配置知识库。
自动检测环境，安装 Obsidian，创建文件夹结构，生成 vault profile。
```

## 9. 团队协调

```text
Use $knowledge-base-team-coordination to set up a shared project for our team.
Generate questionnaires for each member, align everyone before assignment, and track approval status.
```

或中文：

```text
用 $knowledge-base-team-coordination 帮我们团队协调一个共享项目。
生成每人对应的问卷，在对齐后再派单，跟踪审批状态。
```

## 10. 协作画像

```text
Use $knowledge-base-working-profile to distill my collaboration preferences from our recent interactions.
Extract stable signals like decision heuristics, boundaries, and anti-patterns, but keep confirmed and inferred items separate.
```

或中文：

```text
用 $knowledge-base-working-profile 从最近的交互中整理我的协作画像。
提取稳定的决策习惯、边界和反模式，但要把确认项和推断项分开。
```

## 11. 工作记录/日报

```text
Use $work-journal to create today's work log.
Include timestamps, project associations, meeting notes, and temporary ideas.
```

或中文：

```text
用 $work-journal 帮我写今天的工作记录。
包含时间戳、项目关联、会议纪要和临时想法。
```

## 12. 周报生成

```text
Use $work-journal to distill a weekly summary from my journal entries this week.
Highlight key achievements, decisions made, and knowledge worth keeping in the knowledge base.
```

或中文：

```text
用 $work-journal 帮我生成本周的周报。
突出关键成果、做出的决策，以及值得沉淀到知识库的知识。
```
