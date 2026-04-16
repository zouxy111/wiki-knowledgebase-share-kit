# Generic Example Vault Profile

> 这是一个**不包含个人路径、业务专名或私有 area 命名**的通用示例。  
> 适合公开仓库读者直接复制、再替换成自己的环境。

---

## 1. Vault identity

- Vault name: Example Team Wiki
- Vault root path: `/path/to/your-vault`
- Primary markdown page directory: `/path/to/your-vault/pages`
- Reader entrypoint file: `/path/to/your-vault/index.md`
- Milestone log file: `/path/to/your-vault/log.md`
- Maintainer entrypoint file: `/path/to/your-vault/pages/workspace-governance-overview.md`

---

## 2. Fixed page-role model

- `project`
- `knowledge`
- `ops`
- `task`
- `overview`

---

## 3. Area list

| area | 用途说明 |
|---|---|
| product | 产品主线 |
| engineering | 工程实现与技术方案 |
| operations | 运维与排障 |
| research | 调研与知识沉淀 |
| governance | 知识库治理与维护 |

---

## 4. Root page map

| area | root page file | 作用 |
|---|---|---|
| product | `project-product-overview.md` | 产品主线导航入口 |
| engineering | `project-engineering-overview.md` | 工程主线导航入口 |
| operations | `project-operations-overview.md` | 运维主线导航入口 |
| research | `project-research-overview.md` | 调研主线导航入口 |
| governance | `workspace-governance-overview.md` | 维护者入口 |

---

## 5. Canonical root-level markdown files

允许直接放在 vault 根目录：
- `README.md`
- `index.md`
- `log.md`
- `schema.md`
- `prompts.md`

其他 markdown 文件默认应进入：
- `pages/`
- 或你在 profile 中额外声明的合法目录

---

## 6. Frontmatter contract

内容页最少字段：
- `title`
- `type`
- `area`
- `tags`
- `updated`

允许的 `type`：
- `project / knowledge / ops / task / overview`

示例：

```yaml
---
title: "Troubleshooting Message Queue Delays"
type: "ops"
area: "operations"
tags: ["message-queue", "latency"]
updated: "2026-04-16"
---
```

---

## 7. Naming conventions

- 根页以 `project-` 或 `workspace-` 开头
- `ops` 页常用 `-ops` / `-history` / `-runbook`
- `task` 页常用 `-task-list` 或责任人名
- 治理入口常用 `workspace-*` 或明确 overview 名称

---

## 8. Writing rules switches

- Knowledge-base-first mode: yes
- Milestone-only log: yes
- `ops` page four-part pattern: yes
- Root pages should avoid long process narration: yes

---

## 9. Maintenance expectations

每次实质更新至少同步：
- 目标页
- 对应 root page
- reader entrypoint
- milestone log

---

## 10. Audit priorities

默认优先级：
1. 结构问题
2. 导航问题
3. 治理漂移
4. 噪音回流

---

## 11. Working profile settings

- Working profile page: `/path/to/your-vault/pages/workspace-working-profile.md`
- Working profile visibility: `maintainer-only`
- Confirmation threshold for inferred items: `medium`
- Never-store categories:
  - secrets / tokens / credentials
  - precise home address or highly sensitive contact data
  - third-party private data
  - medical or legal sensitive details unless explicitly needed
