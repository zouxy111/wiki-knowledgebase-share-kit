---
name: knowledge-base-ingest
description: This skill should be used when the user asks to import a long markdown document, handbook, book, tutorial, notes dump, or chapter collection into a markdown/wiki knowledge base. Use it when Codex needs to split long-form source material into reusable pages, create parent/child and sibling links, preserve source lineage, and sync the result into the user's knowledge base instead of leaving the source as one giant page. Trigger on requests like "import this markdown book", "拆分这本书到知识库", "把这份长文档拆开并建立链接", "按章节导入 wiki", or "把整本 markdown 维护进知识库".
---

# Knowledge Base Ingest

把**长 markdown 文档 / 整本书 / 大型教程 / 章节合集**导入 markdown/wiki 知识库。

它和 `knowledge-base-maintenance` 的区别是：
- `knowledge-base-maintenance`：处理一次任务结果、聊天结论、排障经验的回写
- `knowledge-base-ingest`：处理**长源材料**，先拆分，再重组，再链接，再写入知识库

默认目标不是把整本书原样塞进 vault，而是把它整理成：
- 可导航的 overview / chapter / topic 页面
- 可复用的知识页与方法页
- 有 parent/child / prev/next / related links 的结构化知识库

## Required input

执行前先读取：
- `references/vault-profile-contract.md`
- `references/ingestion-checklist.md`
- `references/chunking-strategy.md`
- `../../templates/vault-profile-template.md`

默认需要这些输入：
- source markdown 文件路径，或用户直接提供的大段 markdown
- vault profile
- source title / source type（book, handbook, notes, tutorial, spec）
- 是否允许较多保留原文（默认否，默认以总结重组为主）

如果缺少 profile，不要猜测 root pages 或页面目录。

## Core rules

- **先分块，再写入。** 不要把长文档整页导入知识库。
- **先做 ingestion map，再动目标文件。** 先确定 part / chapter / section / topic 的落点。
- **优先知识库口径，而不是原文镜像口径。**
- **保留 source lineage。** 每个导入页面都应能看出来自哪本书、哪一章、哪一节。
- **链接优先级高于排版复刻。**
- **默认少引原文，多做结构化总结。** 除非用户明确要求归档型导入，或明确拥有相应内容权利。
- **不要制造死链或孤立页。**
- **每次实质导入至少同步：** 目标页群、对应 root page、reader entrypoint、milestone log。

## Recommended workflow

### 1. Read source and profile
- 读取长文档或源书稿
- 读取 vault profile
- 判断 source 类型：book / handbook / spec / tutorial / notes dump
- 识别目录结构：part / chapter / section / appendix / glossary

### 2. Build the ingestion map first
先生成一个 page map，而不是直接开始写：
- source overview page
- part pages（如需要）
- chapter pages
- topic pages / concept pages / runbook pages（按内容类型抽出）
- 哪些内容不入库，只保留简短索引或摘要

如果文档过长，先运行：
- `python3 scripts/split_markdown.py <source.md> --out <dir>`

### 3. Decide split granularity
优先遵循：
- H1/H2 对应大的章节单元
- 过长章节再按更深一层标题拆分
- 单页尽量保持在**一个可读、可维护的长度**，避免再次变成长页

默认不要做：
- 每个小标题都拆成碎片页
- 把一本书只做成一个 overview 页
- 把原目录照搬成一堆没有知识价值的壳页

### 4. Classify by page role
导入时仍遵循固定 page-role model：
- `overview`：这本书 / 这份源材料的总览、目录、 ingestion rules
- `knowledge`：概念、框架、模型、结论、定义、方法论
- `ops`：步骤、操作法、排障法、执行边界、可复用 runbook
- `project`：当 source 明显服务于某个长期专题主线时，作为稳定入口页
- `task`：通常不作为书籍导入的主要落点，除非源文档本身就是协作任务结构

### 5. Create the link model
至少建立这些链接：
- parent / child
- prev / next
- sibling / related
- source overview backlink
- root page / reader entrypoint entry

如果某一页只是孤零零的摘录页，不应视为完成导入。

### 6. Rewrite into knowledge-base form
写入时：
- 压缩重复叙述
- 合并平行概念
- 把长段论述改写成更利于检索的结构
- 保留必要 source attribution（书名、章节、版本、作者）
- 如需保留原文，只保留短引用和关键原句，避免大段照搬

### 7. Sync navigation surfaces
至少同步：
- source overview page
- 对应 root page
- reader entrypoint
- milestone log

必要时再更新：
- glossary
- governance / maintainer overview
- related topic hubs

### 8. Validate before finishing
检查：
- 有没有单页过长
- 有没有只拆分但没建立链接
- 有没有 source lineage 丢失
- 有没有把一本书直接导成原文镜像
- 有没有 orphan pages / missing entrypoints
- 页面角色是否合理

## Output expectations

汇报时至少说明：
- source 被拆成了哪些页面组
- page-role 是如何判定的
- 建了哪些关键链接
- 哪些原文被压缩 / 总结 / 改写
- 是否同步了 root page / reader entrypoint / milestone log
- 是否仍有待二次整理的大章节

## Resources

### scripts/
- `scripts/split_markdown.py`：按标题层级做 deterministic split，输出 chunk 文件和 manifest

### references/
- `references/vault-profile-contract.md`：导入前需要哪些 profile 信息
- `references/ingestion-checklist.md`：固定导入回路和验收清单
- `references/chunking-strategy.md`：如何决定 chapter / section / topic 的拆分粒度
