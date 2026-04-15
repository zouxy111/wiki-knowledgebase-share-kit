# Vault Profile Template

> 用途：给 `knowledge-base-maintenance` 和 `knowledge-base-audit` 提供唯一配置入口。  
> 用法：复制本模板，填写你自己的 vault 信息，再让 skill 先读取这个 profile。

---

## 1. Vault identity

- Vault name:
- Vault root path:
- Primary markdown page directory:
- Reader entrypoint file:
- Milestone log file:
- Maintainer entrypoint file:

---

## 2. Fixed page-role model

这套模板默认固定使用：
- `project`
- `knowledge`
- `ops`
- `task`
- `overview`

如果不用这套角色模型，不建议直接使用本 kit。

---

## 3. Area list

列出你的 area：

| area | 用途说明 |
|---|---|
| example-area | 说明 |

---

## 4. Root page map

每个 area 至少给一个 root page：

| area | root page file | 作用 |
|---|---|---|
| example-area | `project-example.md` | 该 area 的导航入口 |

---

## 5. Canonical root-level markdown files

只有以下 markdown 文件允许直接放在 vault 根目录：
- `index.md`
- `log.md`
- 

其他 markdown 文件默认应进入：
- `pages/`
- 或你另行定义的合法目录

这一项会被 audit 用于判断 root-level stray markdown files。

---

## 6. Frontmatter contract

最少字段：
- `title`
- `type`
- `area`
- `tags`
- `updated`

可选字段：
- 
- 

示例：

```yaml
---
title: "Example Page"
type: "knowledge"
area: "example-area"
tags: ["example"]
updated: "2026-04-15"
---
```

---

## 7. Naming conventions

说明：
- root pages 是否统一以 `project-` 开头：
- `ops` 页是否统一用 `-ops` / `-history` / `-recent-activity`：
- `task` 页是否统一用 `-task-list` 或负责人名：
- `overview` 页如何命名：

---

## 8. Writing rules switches

请明确这几个开关：

- Knowledge-base-first mode: yes / no
- Milestone-only log: yes / no
- `ops` page four-part pattern (`现象 / 根因 / 处理法 / 边界`): yes / no
- Root pages should avoid long process narration: yes / no

---

## 9. Maintenance expectations

每次实质更新至少同步：
- 目标页
- 对应 root page
- reader entrypoint
- milestone log

如有额外要求，也写在这里。

---

## 10. Audit priorities

默认优先级可写为：
1. 结构问题
2. 导航问题
3. 治理漂移
4. 噪音回流

如需调整，可写在这里。
