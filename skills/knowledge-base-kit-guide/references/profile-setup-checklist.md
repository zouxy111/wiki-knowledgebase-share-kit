# Profile Setup Checklist

在开始真正使用 `knowledge-base-maintenance` 或 `knowledge-base-audit` 之前，先确认这些配置已经明确：

## 必填
- vault root path
- pages directory
- reader entrypoint
- milestone log
- maintainer entrypoint
- area list
- root page map
- canonical root-level markdown files
- frontmatter contract

## 强烈建议明确
- 命名约定
- 是否启用 knowledge-base-first mode
- 是否启用 milestone-only log
- 是否启用 `ops` 四段式写法
- working profile page（如果你要沉淀长期协作画像）
- working profile visibility 与 never-store categories

## 常见卡点

### 1. 不知道 root page 怎么定
先按业务主线划分，每个 area 至少给一个导航入口。

### 2. 不知道哪些 markdown 文件能放在 vault 根目录
先列 canonical 清单，其他一律视为应迁出的候选项。

### 3. 不知道 maintenance 和 audit 谁先用
- 要写内容：maintenance
- 要体检结构：audit
- 大改之后：先 maintenance，再 audit
