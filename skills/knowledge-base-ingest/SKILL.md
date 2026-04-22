---
name: knowledge-base-ingest
description: This skill should be used when the user asks to import a long markdown document, handbook, book, tutorial, notes dump, or chapter collection into a markdown/wiki knowledge base. Use it when Codex needs to split long-form source material into reusable pages, create parent/child and sibling links, preserve source lineage, extract a table of contents or glossary candidates, and sync the result into the user's knowledge base instead of leaving the source as one giant page. Trigger on requests like "import this markdown book", "拆分这本书到知识库", "把这份长文档拆开并建立链接", "按章节导入 wiki", "提取目录和术语表", or "把整本 markdown 维护进知识库".
---

# Knowledge Base Ingest

把**长 markdown 文档 / 整本书 / 大型教程 / 章节合集**导入 markdown/wiki 知识库。

它和 `knowledge-base-maintenance` 的区别是：
- `knowledge-base-maintenance`：处理一次任务结果、聊天结论、排障经验的回写
- `knowledge-base-ingest`：处理**长源材料**，先拆分，再重组，再链接，再写入知识库

默认目标不是把整本书原样塞进 vault，而是把它整理成：
- 可导航的 `overview / chapter / topic` 页面群
- 可复用的知识页、方法页与术语页
- 有 `parent / child / prev / next / related` links 的结构化知识库
- 可作为后续 glossary / hub / root page 更新依据的中间产物

## Required input

执行前先读取：
- `references/vault-profile-contract.md`
- `references/ingestion-checklist.md`
- `references/source-coverage-rules.md`
- `references/ingest-iteration-loop.md`
- `references/ingest-evaluation-rubric.md`
- `references/chunking-strategy.md`
- `references/close-reading-mode.md`
- `references/rolling-state-contract.md`
- `references/chunk-note-schema.md`
- `references/claim-map-contract.md`
- `references/delivery-gate-contract.md`
- `references/glossary-strategy.md`
- `references/linking-strategy.md`
- `../../templates/vault-profile-template.md`
- `../../templates/ingest-iteration-log-template.md`

默认需要这些输入：
- source markdown 文件路径，或用户直接提供的大段 markdown
- vault profile
- source title / source type（book, handbook, notes, tutorial, spec）
- 是否允许较多保留原文（默认否，默认以总结重组为主）
- 如果已有历史版本：当前 stable baseline 或上一轮 iteration log

如果缺少 profile，不要猜测 root pages 或页面目录。

## Core rules

- **先分块，再写入。** 不要把长文档整页导入知识库。
- **长文档禁止直接整篇读完再回写。** 超长源材料必须先变成受控 chunk 集合。
- **先做 ingestion map，再动目标文件。** 先确定 part / chapter / section / topic 的落点。
- **超长源材料必须先产出 `manifest.json` + `coverage-map.md`。**
- **每个 chunk 在结束前都必须有明确 disposition。** 没有 chunk-level 覆盖表，不得宣称“已完整导入”。
- **coverage verification 没通过，就只能汇报 partial / draft / incomplete。**
- **默认采用 overview / chapter / topic 三层结构。** 除非源材料本身有更适合的层级。
- **先认定 stable baseline。** 如果不是第一次导入，本轮要明确“当前稳定版本”是什么。
- **超大源材料要切到 close-reading mode。** 不要指望一次 prompt 读完整本书。
- **超大源材料优先增量重跑。** 改动了哪个 chapter，就尽量只重跑受影响的 batches。
- **`batch-notes/` 默认视为 extractive evidence layer。** 不要只写松散 summary。
- **没有 claim map，就不能把关键结论当成“已证实知识”。**
- **执行 agent 不得自我认证“已完整导入”。** 完成态必须交给 delivery gate。
- **优先知识库口径，而不是原文镜像口径。**
- **保留 source lineage。** 每个导入页面都应能看出来自哪本书、哪一章、哪一节。
- **链接优先级高于排版复刻。**
- **默认少引原文，多做结构化总结。** 除非用户明确要求归档型导入，或明确拥有相应内容权利。
- **不要制造死链或孤立页。**
- **每轮优先只改一类结构问题。** 避免一次同时大改拆分、角色和导航，导致无法归因。
- **候选结构需要通过回归检查后才能晋升。**
- **每次实质导入至少同步：** 目标页群、对应 root page、reader entrypoint、milestone log。

## Recommended workflow

### 1. Read source and profile
- 读取长文档或源书稿
- 读取 vault profile
- 判断 source 类型：book / handbook / spec / tutorial / notes dump
- 识别目录结构：part / chapter / section / appendix / glossary
- 如果 source 很长（例如几千行以上），不要直接尝试整篇塞进单轮上下文

### 2. Build the ingestion map first
先生成一个 page map，而不是直接开始写：
- source overview page
- part pages（如需要）
- chapter pages
- topic pages / concept pages / runbook pages（按内容类型抽出）
- glossary page（如适用）
- 哪些内容不入库，只保留简短索引或摘要

如果已有历史版本：
- 先明确当前 stable baseline
- 说明本轮 candidate 主要准备优化什么
- 优先只改一类结构问题

### 3. Split and extract structure artifacts
如果文档过长，先运行：
- `python3 scripts/split_markdown.py <source.md> --out <dir>`

这个脚本会输出：
- chunk 文件
- `manifest.json`
- `toc.md`
- `coverage-map.md`

默认优先遵循：
- H1/H2 对应大的章节单元
- 过长章节再按更深一层标题拆分
- 单页尽量保持在**一个可读、可维护的长度**，避免再次变成长页
- 如果没有合适标题层级，脚本会退化成**固定行数窗口切分**
- 因此即使 source 达到 10 万行，也应先被变成可遍历的 chunk ledger，而不是一次性让模型“自己读完”

### 4. Read every chunk through the coverage map
读取 `manifest.json` 和 `coverage-map.md`：
- 逐个 chunk 阅读和处理
- 给每个 chunk 填写最终状态：`covered / merged / index-only / intentionally-omitted`
- 如果某个 chunk 还没处理完，只能保留 `unread` 或 `blocked`
- 在所有 chunk 都有 final status 之前，不能宣称导入完成

完成时运行：
- `python3 scripts/verify_ingest_coverage.py --manifest <dir>/manifest.json --coverage <dir>/coverage-map.md`

只有 verification 通过，才允许把结果汇报为完整导入。

### 5. Run close-reading mode for oversized sources
如果 source 已经大到不适合“一轮拆完立刻落页”，切到 close-reading mode：
- `python3 scripts/close_read_markdown.py <source.md> --out <run-dir>`

这个脚本会输出：
- `chunks/`
- `batch-plan.json`
- `reading-state.json`
- `batch-packets/`
- `batch-notes/`

close-reading mode 的目标是：
- 让 AI 按 batch 分块精读
- 让每一轮精读保留可恢复、可比较的中间状态
- 让后续 synthesis 能跨 batch 累积理解，而不是每块重新开始
- 尽量保留 unchanged completed batches，只重置 changed batches

当 source 满足任一条件时，优先进入 close-reading mode：
- 超过 25,000 words
- 或拆分后 chunk 数明显很多（例如 > 15）
- 或用户明确要求“超大文本 / 分块精读 / 整本书精读”

执行时：
- 先运行 `scripts/close_read_markdown.py`
- 按 batch packet 逐轮精读
- 每轮把抽取结果写入 `batch-notes/<batch-key>.json`
- 把 `batch-notes` 当作 extractive evidence layer；对于高风险 batch，补充 `headings_seen / must_keep_facts / boundaries_and_exceptions / omission_risk`
- 反复重跑脚本以刷新 rolling state
- 如果 source 改了，优先利用 chunk hash / batch hash 只重跑 changed batches
- 需要汇总时运行：
  - `python3 scripts/synthesize_knowledge.py <run-dir>`

### 5B. Build evidence gates after synthesis
在 close-reading mode 之后，不要立刻宣称完成。

还需要准备：
- `claim-map.json`：记录 candidate pages 中的重要 claim 如何回指到 batch note / source chunk / evidence quote
- `delivery-gate.json`：统一汇总 coverage / extractive / evidence / integrity 的状态

建议的完成态枚举：
- `partial`
- `coverage-complete`
- `evidence-complete`
- `ready-to-promote`

只有 `ready-to-promote` 才允许说：
- 已完整导入
- fully imported
- ready to merge / ready to promote

### 6. Classify by page role
导入时仍遵循固定 page-role model：
- `overview`：这本书 / 这份源材料的总览、目录、 ingestion rules
- `knowledge`：概念、框架、模型、结论、定义、方法论
- `ops`：步骤、操作法、排障法、执行边界、可复用 runbook
- `project`：当 source 明显服务于某个长期专题主线时，作为稳定入口页
- `task`：通常不作为书籍导入的主要落点，除非源文档本身就是协作任务结构

### 7. Extract glossary and related-link suggestions
需要辅助结构化时，可运行：
- `python3 scripts/extract_terms.py <source-or-dir> --out <dir>`
- `python3 scripts/suggest_related_links.py <dir> --top 3`

这些脚本用于：
- 生成 glossary candidates
- 为 chapter / topic 页面提供 related links 建议
- 发现重复概念与潜在 hub 页面

### 8. Rewrite into knowledge-base form
写入时：
- 压缩重复叙述
- 合并平行概念
- 把长段论述改写成更利于检索的结构
- 保留必要 source attribution（书名、章节、版本、作者）
- 如需保留原文，只保留短引用和关键原句，避免大段照搬

### 9. Create the link model
至少建立这些链接：
- parent / child
- prev / next
- sibling / related
- source overview backlink
- root page / reader entrypoint entry

如果在 close-reading mode：
- 让 synthesis 产出 candidate pages
- 让 candidate pages 自带 overview / prev-next / related topic links
- 让 candidate pages 直接带 draft frontmatter / source metadata / candidate metadata
- 额外产出 candidate link map，避免后续落页时重新猜链接

如果某一页只是孤零零的摘录页，不应视为完成导入。

### 10. Compare candidate structure to the stable baseline
如果当前不是第一次导入，而是在迭代已有结构：
- 用 `references/ingest-evaluation-rubric.md` 的口径比较 baseline 和 candidate
- 重点看拆分适配度、页面角色、导航覆盖、related links 是否真的更好
- 只在 candidate 明显更利于检索、维护和回查时，才考虑晋升

### 11. Run regression checks and record the round
至少检查：
- overview / root page / reader entrypoint 是否仍可达
- source lineage 是否仍完整
- 有没有新增 dead links / orphan pages
- milestone log 是否同步

如果这一轮是正式结构迭代：
- 用 `../../templates/ingest-iteration-log-template.md` 记录 baseline / candidate / regression / decision
- 决策为 promote / rework / drop 之一

### 12. Sync navigation surfaces
至少同步：
- source overview page
- 对应 root page
- reader entrypoint
- milestone log

必要时再更新：
- glossary
- governance / maintainer overview
- related topic hubs

### 13. Validate before finishing
检查：
- source 是否已经先拆成 bounded chunks
- `manifest.json` 是否覆盖了 source 全部范围（包括 preamble / appendix）
- `coverage-map.md` 是否每一行都有 final status
- `verify_ingest_coverage.py` 是否通过
- 有没有单页过长
- 有没有只拆分但没建立链接
- 有没有 source lineage 丢失
- 有没有把一本书直接导成原文镜像
- 有没有 orphan pages / missing entrypoints
- 页面角色是否合理
- glossary / related links 建议是否需要落页

## Output expectations

汇报时至少说明：
- source 总行数 / chunk 数量 / 是否使用了固定窗口切分
- source 被拆成了哪些页面组
- 当前 stable baseline 是什么（如果存在）
- 本轮 candidate 主要改了什么
- page-role 是如何判定的
- 建了哪些关键链接
- 哪些原文被压缩 / 总结 / 改写
- 是否抽取了 toc / glossary candidates / related links 建议
- 是否启用了 close-reading mode
- close-reading run 是否有 batch plan / reading state / completed notes / synthesis 产物
- `batch-notes` 是否只是 summary，还是已经作为 extractive evidence layer 使用
- 是否生成了 `claim-map.json`
- 是否生成了 `delivery-gate.json`
- 当前 gate 是 `partial / coverage-complete / evidence-complete / ready-to-promote` 中的哪一种
- rerun 时是否只重置了 changed batches，而不是整本书重读
- synthesis 是否产出了 candidate pages 和 candidate link map
- candidate pages 是否已经带 frontmatter，且 `area` / `owner` / `status` 是否明确
- 是否做了 baseline vs candidate 的结构比较
- 是否通过 coverage verification
- 是否通过回归检查
- 本轮最终决定是 promote / rework / drop
- 是否同步了 root page / reader entrypoint / milestone log
- 是否仍有待二次整理的大章节

## Resources

### scripts/
- `scripts/split_markdown.py`：按标题层级或固定窗口做 deterministic split，输出 chunk 文件、manifest、toc 和 coverage map
- `scripts/verify_ingest_coverage.py`：检查每个 source chunk 是否已经被明确处理，未通过则不得宣称完整导入
- `scripts/close_read_markdown.py`：为超大源材料生成 batch 级精读包、rolling state 和可续跑的 batch notes
- `scripts/extract_terms.py`：提取 glossary candidates，输出 JSON 和 Markdown 列表
- `scripts/suggest_related_links.py`：基于标题和关键词重合度生成 related links 建议
- `scripts/synthesize_knowledge.py`：把 completed batch notes 汇总成 source overview / chapter summaries / topic candidates / candidate pages / candidate link map，并给 candidate pages 写入 draft frontmatter

### references/
- `references/vault-profile-contract.md`：导入前需要哪些 profile 信息
- `references/ingestion-checklist.md`：固定导入回路和验收清单
- `references/source-coverage-rules.md`：如何用 chunk-level coverage map 防止半读半写
- `references/ingest-iteration-loop.md`：如何把 ingest 当作稳定基线和候选结构的迭代回路
- `references/ingest-evaluation-rubric.md`：如何判断候选结构是否值得晋升
- `references/chunking-strategy.md`：如何决定 chapter / section / topic 的拆分粒度
- `references/close-reading-mode.md`：什么时候切入超大文本的分块精读模式
- `references/rolling-state-contract.md`：`reading-state.json` 和 `batch-notes/*.json` 应该如何保持稳定
- `references/chunk-note-schema.md`：batch note 应提取哪些字段，如何避免变成流水账
- `references/claim-map-contract.md`：如何把最终交付里的关键 claim 回指到 source 证据
- `references/delivery-gate-contract.md`：什么状态下才允许说“已完整导入”
- `references/glossary-strategy.md`：术语页与 glossary candidates 的处理方式
- `references/linking-strategy.md`：如何从 related links 建议落到真实 wiki 链接模型
- `../../templates/ingest-iteration-log-template.md`：记录每轮 baseline / candidate / regression / decision
