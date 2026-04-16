# Customization Guide

## 目标

把这套分享包从“通用方法包”适配到你自己的 markdown/wiki 知识库。

这套方法默认保留固定页面角色模型：
- `project`
- `knowledge`
- `ops`
- `task`
- `overview`

你真正要改的是：
- 路径
- area
- root pages
- 文件布局
- frontmatter 约束

---

## 第 1 步：先填写 vault profile

复制：
- `templates/vault-profile-template.md`

填写至少这些字段：
- vault root
- pages directory
- reader entrypoint
- milestone log
- maintainer entrypoint
- allowed page roles
- area list
- root page table
- canonical root-level markdown files
- frontmatter schema
- naming conventions

如果这些没填，maintenance 和 audit 都无法稳定落地。

---

## 第 2 步：定义你的 root pages

root page 是你的知识库主线入口。

推荐每个 area 至少有一个 root page，并明确：
- area 名
- 对应 root page 文件名
- 该 root page 的职责

例如：
- 产品文档主线
- 技术运维主线
- 研究资料主线
- 协作任务主线

不要求你沿用任何特定命名，但必须在 profile 里写清楚映射关系。

---

## 第 3 步：确认 frontmatter 规则

这套模板默认要求每个内容页有稳定 frontmatter。

推荐至少包含：
- `title`
- `type`
- `area`
- `tags`
- `updated`

如果你的 vault 还需要：
- `status`
- `owner`
- `created`
- `aliases`

也可以放进自己的 profile。

---

## 第 4 步：确认根目录允许出现哪些 markdown 文件

这是为了让 audit 能正确识别 **root-level stray markdown artifacts**。

你需要在 profile 里写清楚：
- 哪些 markdown 文件允许直接放在 vault 根目录
- 其他 markdown 文件是否都应该进 `pages/` 或其它指定目录

常见允许项可能是：
- `index.md`
- `log.md`
- `schema.md`
- `prompts.md`
- `README.md`

如果 profile 没有这条，审计无法稳定判断“根目录历史残片”。

---

## 第 4.5 步：如果你要沉淀 working profile

如果你准备使用 `knowledge-base-working-profile`，建议在 profile 中额外写清：
- working profile page
- 该页面是否 `maintainer-only` 还是 `reader-visible`
- inferred 项采用多严格的确认阈值
- 哪些内容类型永远不写入长期画像

这一步的作用不是“多收集个人信息”，而是防止长期画像写错地方、写错可见范围、或写进不该保存的内容。

## 第 5 步：尽量不要改的核心原则

如果你希望这套方法真的有效，尽量不要改掉：

### A. 知识库优先
- 默认不把一次性运行过程写进主叙事
- 只沉淀长期可检索的知识、规则、边界、排障经验

### B. 页面角色清晰
- `project`：导航 + 稳定总览
- `knowledge`：结构、概念、方法、判断框架
- `ops`：流程、排障、版本边界、回归方法
- `task`：分工、协同、回填顺序
- `overview`：治理、索引、全库入口

### C. 里程碑日志
- `log.md` 只写结构变化和治理变化
- 不写任务回放

---

## 第 6 步：安装 skill 后怎么调用

### Maintenance
可以这样说：

```text
Use $knowledge-base-maintenance to integrate this task or chat into my markdown knowledge base.
Read the vault profile first, keep only durable conclusions or reusable troubleshooting knowledge, choose the right page role, and sync the target page, relevant root page, reader entry, and milestone log.
```

### Audit
可以这样说：

```text
Use $knowledge-base-audit to inspect my wiki vault.
Read the vault profile first, then check metadata completeness, dead links, orphan pages, root page coverage, page-boundary drift, noise regression, and stray markdown files at the vault root.
```

---

## 定制完成后的最小验收

你的 profile 配好后，至少应该能回答这些问题：
- root pages 是哪些？
- areas 是哪些？
- 哪些文件允许放在 vault 根目录？
- 哪些页面要进 `pages/`？
- `ops` 页是否默认采用“现象 / 根因 / 处理法 / 边界”？
- `log.md` 是否是 milestone-only？
