# Profile Setup Checklist

在开始真正使用 `knowledge-base-maintenance`、`knowledge-base-audit` 或 `knowledge-base-team-coordination` 之前，先确认这些配置已经明确：

## A. 知识库场景必填
- vault root path
- pages directory
- reader entrypoint
- milestone log
- maintainer entrypoint
- area list
- root page map
- canonical root-level markdown files
- frontmatter contract

## B. 多人协同场景必填
- shared project directory path
- `project-brief.md`
- `team-roster.md`
- 至少一个 `members/<id>/` 目录
- 共享资料目录 `shared-materials/`
- 是否已有 canonical member profiles
- 是否需要 knowledge-base sync

## 强烈建议明确
- 命名约定
- 是否启用 knowledge-base-first mode
- 是否启用 milestone-only log
- 是否启用 `ops` 四段式写法
- 问卷 / 对齐 / 派单 / 决策是否都需要明确 `status`

## 常见卡点

### 1. 不知道 root page 怎么定
先按业务主线划分，每个 area 至少给一个导航入口。

### 2. 不知道哪些 markdown 文件能放在 vault 根目录
先列 canonical 清单，其他一律视为应迁出的候选项。

### 3. 不知道 maintenance、audit、team-coordination 谁先用
- 要写知识库：maintenance
- 要体检结构：audit
- 要跑多人协同：team-coordination
- 不确定自己缺什么：先用 guide

### 4. 没有 canonical member profile path
先不要失败，先让系统通过第一轮问卷建立项目内画像。
