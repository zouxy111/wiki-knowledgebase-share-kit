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
I want to understand the profile first, then know which of the 8 skills I should use next.
```

```text
用 $knowledge-base-kit-guide 帮我理解这套知识库维护包。
我想先搞清楚 profile、安装方式和 8 个 skill 的分工，再决定下一步用哪个。
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

```text
用 $knowledge-base-ingest 处理这份超大 Markdown 源材料并导入我的知识库。
先读 vault profile。
不要把这次当成一次性导入；请切到 close-reading mode：
先拆 chunk，再生成 batch packets，维护 rolling reading state，每个 batch 输出一份 JSON 精读笔记，最后再汇总 chapter summaries、topic candidates、glossary seeds 和 overview 页。
整个 run 必须支持断点续跑，下一轮不要从头重读整份材料。
如果后续 source 有修改，也要尽量只重跑 changed batches，并输出 candidate pages 和 candidate link map，方便最后落页。
candidate pages 还要带 draft frontmatter，这样它们更接近真正可落进 vault 的页面，而不是普通笔记草稿。
```

## 3C. 对超大文本启用“防漏 + 防吹牛”模式

```text
Use $knowledge-base-ingest to import this oversized Markdown source into my knowledge base.
Read my vault profile first.
Switch into close-reading mode and do not self-certify completion.
Use batch-notes as extractive evidence notes rather than loose summaries:
for each batch, record headings_seen, must_keep_facts, boundaries_and_exceptions, and omission_risk where relevant.
After synthesis, create a claim map for the important conclusions in candidate pages and only use supported or clearly weakly-supported claims.
Do not say the import is complete until chunk coverage, extractive notes, evidence mapping, and the final delivery gate all pass.
```

```text
用 $knowledge-base-ingest 处理这份超大 Markdown 源材料并导入我的知识库。
先读 vault profile。
请切到 close-reading mode，并禁止自我认证“已经完成”。
把 batch-notes 当作抽取式证据层，而不是松散总结：
每个 batch 在需要时都要显式记录 headings_seen、must_keep_facts、boundaries_and_exceptions 和 omission_risk。
在 synthesis 之后，再为 candidate pages 里的关键结论建立 claim map，只允许用 supported 或明确标注 weakly-supported 的结论。
在 chunk coverage、extractive notes、evidence mapping 和 final delivery gate 全部通过前，不要宣称完整导入。
```

## 4. 我已经有 profile，想沉淀一轮任务结果

```text
Use $knowledge-base-maintenance to integrate this task into my markdown knowledge base.
Read my vault profile first. Keep only durable conclusions or reusable troubleshooting knowledge, choose the right page role, and sync the target page, relevant root page, reader entrypoint, and milestone log.
```

```text
用 $knowledge-base-maintenance 把这次结果沉淀进我的知识库。
先读 vault profile，再过滤过程噪音，按页面角色归类，并同步目标页、root page、reader entry 和 milestone log。
```

## 5. 我怀疑 wiki 结构已经乱了

```text
Use $knowledge-base-audit to inspect my knowledge base.
Read the vault profile first, then report dead links, orphan pages, missing entrypoints, metadata issues, page-boundary drift, noise regression, and stray markdown files at the vault root.
```

```text
用 $knowledge-base-audit 审计我的知识库。
先读 vault profile，再检查死链、孤立页、metadata、页面边界漂移、噪音回流，以及根目录 stray markdown 文件。
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

```text
用 $knowledge-base-working-profile 从我们的持续沟通里更新我的 working profile。
先读 vault profile，再只保留对未来协作有用的稳定信号，区分 confirmed / repeated / inferred，过滤敏感个人信息，并按 visibility 规则同步到目标画像页。
```

## 8. 协调一个多人共享项目

```text
Use $knowledge-base-team-coordination to coordinate this shared project.
Read the shared project directory first, generate role-aware questionnaires, summarize alignment gaps, keep assignments in draft until approved, and distill reusable decisions at closeout.
```

```text
用 $knowledge-base-team-coordination 协调这个共享项目。
先读取共享项目目录，生成成员级问卷，总结对齐缺口，在确认前保持 assignment 为 draft，并在结项时输出可复用的决策蒸馏。
```

## 9. 记录今天的工作 / 会议纪要

```text
Use $work-journal to create today's work log.
Include timestamps, project associations, meeting notes, temporary ideas, and any distillation hooks worth revisiting later.
```

```text
用 $work-journal 帮我写今天的工作记录。
包含时间戳、项目关联、会议纪要、临时想法，以及后续值得沉淀的条目。
```

## 10. 从本周 journal 生成周报

```text
Use $work-journal to distill a weekly summary from my journal entries this week.
Highlight key achievements, decisions made, blockers, and knowledge worth sending back into the knowledge base.
```

```text
用 $work-journal 帮我生成本周的周报。
突出关键成果、做出的决策、阻塞项，以及值得回流到知识库的知识。
```
