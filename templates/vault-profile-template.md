# Vault Profile Template

> **用途**：告诉工具你的知识库结构，让它知道怎么帮你整理笔记。  
> **用法**：复制本模板，填写你自己的信息，保存为 `my-vault-profile.md`。

---

## 1. Vault identity（知识库基本信息）

### 必填字段

- **Vault name**（知识库名称）: `我的学习笔记`
  - 💡 随便起个名字，方便识别即可

- **Vault root path**（知识库根目录）: `/Users/yourname/Documents/my-notes`
  - 💡 你的笔记文件夹的**完整路径**
  - 💡 Obsidian 用户：就是你的 vault 文件夹路径
  - 💡 Mac 示例：`/Users/zhangsan/Documents/obsidian-vault`
  - 💡 Windows 示例：`C:\Users\zhangsan\Documents\my-notes`

- **Primary markdown page directory**（笔记存放目录）: `/Users/yourname/Documents/my-notes/pages`
  - 💡 你的 `.md` 文件主要放在哪个文件夹
  - 💡 如果直接放在根目录，就填和上面一样的路径

- **Reader entrypoint file**（导航首页）: `/Users/yourname/Documents/my-notes/index.md`
  - 💡 你的知识库"首页"文件
  - 💡 如果还没有，创建一个 `index.md` 作为导航页

- **Milestone log file**（里程碑日志）: `/Users/yourname/Documents/my-notes/log.md`
  - 💡 记录重要变化的日志文件
  - 💡 如果还没有，创建一个 `log.md`

- **Maintainer entrypoint file**（维护者入口）: `/Users/yourname/Documents/my-notes/pages/governance.md`
  - 💡 记录维护规则的文件
  - 💡 可选，如果不需要可以留空

---

## 2. Fixed page-role model（固定页面角色）

这套模板使用 5 种固定页面角色，**不要修改**：
- `project` — 项目文档、导航页
- `knowledge` — 知识沉淀、学习笔记
- `ops` — 操作手册、排障文档
- `task` — 任务清单、待办事项
- `overview` — 总览页、索引页

💡 **不理解这 5 种角色？** 先看 [`GLOSSARY.md`](../GLOSSARY.md)

---

## 3. Area list（知识库分类）

列出你的知识库有哪些主要分类：

| area（分类名） | 用途说明 |
|---|---|
| `learning` | 个人学习笔记 |
| `work` | 工作相关文档 |
| `projects` | 项目管理 |
| `life` | 生活记录 |

💡 **示例场景**：
- 学生：`math`（数学）、`english`（英语）、`programming`（编程）
- 工程师：`frontend`（前端）、`backend`（后端）、`devops`（运维）
- 产品经理：`product`（产品）、`design`（设计）、`research`（调研）

💡 **建议**：先从 2-3 个分类开始，不要一开始就分太细

---

## 4. Root page map（导航页映射）

每个分类（area）至少需要一个导航页（root page）：

| area（分类） | root page file（导航页文件） | 作用 |
|---|---|---|
| `learning` | `pages/project-learning-overview.md` | 学习笔记的导航入口 |
| `work` | `pages/project-work-overview.md` | 工作文档的导航入口 |
| `projects` | `pages/project-projects-overview.md` | 项目管理的导航入口 |

💡 **什么是 root page？**
- 就是每个分类的"目录页"
- 用户通过这个页面找到该分类下的所有内容

💡 **命名建议**：
- 统一用 `project-` 开头
- 格式：`project-{area名}-overview.md`

---

## 5. Canonical root-level markdown files（允许放在根目录的文件）

只有以下 markdown 文件允许直接放在 vault 根目录：
- `README.md` — 项目说明
- `index.md` — 导航首页
- `log.md` — 里程碑日志
- `schema.md` — 结构说明（可选）
- `prompts.md` — 常用命令（可选）

💡 **为什么要限制？**
- 防止根目录堆满临时文件
- 让知识库结构更清晰

💡 **其他 markdown 文件应该放在哪？**
- 放到 `pages/` 目录
- 或者你在上面定义的 "Primary markdown page directory"

---

## 6. Frontmatter contract（文件头部元数据规则）

每个笔记文件开头必须包含这些信息：

### 最少字段（必填）
```yaml
---
title: "笔记标题"
type: "knowledge"  # 必须是 project/knowledge/ops/task/overview 之一
area: "learning"   # 必须是你在上面定义的 area 之一
tags: ["python", "tutorial"]  # 标签，方便搜索
updated: "2026-04-17"  # 最后更新日期
---
```

### 可选字段
```yaml
status: "draft"  # 草稿/完成状态
owner: "张三"    # 负责人
created: "2026-04-01"  # 创建日期
aliases: ["Python 教程", "Python 入门"]  # 别名
```

💡 **完整示例**：
```markdown
---
title: "Python 基础语法"
type: "knowledge"
area: "learning"
tags: ["python", "programming", "basics"]
updated: "2026-04-17"
---

# Python 基础语法

## 变量定义
...
```

💡 **不知道 frontmatter 是什么？** 看 [`GLOSSARY.md`](../GLOSSARY.md)

---

## 7. Naming conventions（文件命名规则）

建议遵循以下命名规则：

- **Root pages（导航页）**：统一以 `project-` 开头
  - 示例：`project-learning-overview.md`
  
- **Ops pages（操作手册）**：用 `-ops` / `-runbook` / `-troubleshooting` 结尾
  - 示例：`redis-ops.md`、`deployment-runbook.md`
  
- **Task pages（任务清单）**：用 `-tasks` / `-todo` 结尾
  - 示例：`q2-tasks.md`、`weekly-todo.md`
  
- **Overview pages（总览页）**：用 `-overview` / `-index` 结尾
  - 示例：`workspace-overview.md`

💡 **为什么要统一命名？**
- 一眼就能看出文件类型
- 方便搜索和管理

---

## 8. Writing rules switches（写作规则开关）

请明确这几个开关（建议全部选 `yes`）：

- **Knowledge-base-first mode**（知识库优先模式）: `yes`
  - 💡 只保留长期有用的内容，过滤掉临时过程
  
- **Milestone-only log**（里程碑日志模式）: `yes`
  - 💡 log.md 只记录重要变化，不记录流水账
  
- **`ops` page four-part pattern**（ops 页四段式结构）: `yes`
  - 💡 ops 页统一写成：现象 / 根因 / 处理法 / 边界
  
- **Root pages should avoid long process narration**（根页避免长流水）: `yes`
  - 💡 导航页只做导航，不堆积执行细节

---

## 9. Maintenance expectations（维护要求）

每次实质更新至少同步这 4 个地方：
1. ✅ 目标页面本身
2. ✅ 对应的 root page（导航页）
3. ✅ reader entrypoint（index.md）
4. ✅ milestone log（log.md）

💡 **为什么要同步？**
- 确保内容能被找到（有导航入口）
- 记录重要变化（更新日志）

---

## 10. Audit priorities（审计优先级）

默认优先级（建议不修改）：
1. **结构问题**（死链、孤立页、缺失 frontmatter）
2. **导航问题**（缺少入口、root page 覆盖不全）
3. **治理漂移**（页面角色混乱、边界不清）
4. **噪音回流**（临时内容混入知识库）

---

## ✅ 配置完成检查清单

填完后，检查这些问题：

- [ ] 所有路径都是**完整的绝对路径**（不是相对路径）
- [ ] 路径里的文件夹都**真实存在**
- [ ] 至少定义了 **2-3 个 areas**
- [ ] 每个 area 都有对应的 **root page**
- [ ] frontmatter 规则里的 `type` 只能是 **5 种角色之一**
- [ ] frontmatter 规则里的 `area` 只能是**你定义的 areas 之一**

---

## 🆘 需要帮助？

- 📖 看不懂某个概念？查看 [`GLOSSARY.md`](../GLOSSARY.md)
- 📝 不知道怎么填？参考 [`examples/example-vault-profile-generic.md`](../examples/example-vault-profile-generic.md)
- 💬 还有问题？在 [GitHub Issues](https://github.com/zouxy111/wiki-knowledgebase-share-kit/issues) 提问
