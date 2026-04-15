# Example Vault Profile

> 这是一个真实知识库的示例 profile，用来展示模板如何落到具体环境。  
> 这个示例保留了本地路径、当前 area 与 root pages，因此只应作为示例参考，不应直接拿来当模板本体。

---

## 1. Vault identity

- Vault name: Obsdain wiki
- Vault root path: `/Users/zouxingyu/Desktop/obsdain/wiki`
- Primary markdown page directory: `/Users/zouxingyu/Desktop/obsdain/wiki/pages`
- Reader entrypoint file: `/Users/zouxingyu/Desktop/obsdain/wiki/index.md`
- Milestone log file: `/Users/zouxingyu/Desktop/obsdain/wiki/log.md`
- Maintainer entrypoint file: `/Users/zouxingyu/Desktop/obsdain/wiki/pages/workspace-harness-maintenance.md`

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
| pathology | 病理主线 |
| robotics | 机器人与 ACT |
| openclaw | 文献采集与交付 |
| qc | QC 协同 |
| governance | 维护与治理 |

---

## 4. Root page map

| area | root page file | 作用 |
|---|---|---|
| pathology | `project-xuantong-medpilot.md` | 病理主线根页 |
| robotics | `project-so101-act.md` | 机器人主线根页 |
| openclaw | `project-openclaw-literature.md` | 文献交付主线根页 |
| qc | `project-xuantong-qc.md` | QC 协同根页 |
| governance | `workspace-harness-maintenance.md` | 维护者入口 |

---

## 5. Canonical root-level markdown files

允许直接放在 vault 根目录：
- `README.md`
- `index.md`
- `log.md`
- `schema.md`
- `prompts.md`

当前实际观察到一个应被审计报告标出的历史残片：
- `/Users/zouxingyu/Desktop/obsdain/wiki/pathology-harness-ops.md`

该文件为空、且不在 canonical 根文档清单中，因此适合作为 **root-level stray markdown artifact** 的真实示例。

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

---

## 7. Naming conventions

- 根页以 `project-` 或 `workspace-` 开头
- `ops` 页常用 `-ops` / `-history` / `-recent-activity`
- `task` 页常用 `-task-list` 或负责人名
- 治理入口常用 `workspace-*` 或明确 overview 名称

---

## 8. Writing rules switches

- Knowledge-base-first mode: yes
- Milestone-only log: yes
- `ops` page four-part pattern: yes
- Root pages should avoid long process narration: yes
