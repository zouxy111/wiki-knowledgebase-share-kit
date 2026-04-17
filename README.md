# Wiki Knowledge Base Share Kit

[![Release](https://img.shields.io/github/v/release/zouxy111/wiki-knowledgebase-share-kit)](https://github.com/zouxy111/wiki-knowledgebase-share-kit/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](./LICENSE)
[![Repo](https://img.shields.io/badge/GitHub-zouxy111%2Fwiki--knowledgebase--share--kit-black?logo=github)](https://github.com/zouxy111/wiki-knowledgebase-share-kit)
[![Validate](https://github.com/zouxy111/wiki-knowledgebase-share-kit/actions/workflows/validate.yml/badge.svg)](https://github.com/zouxy111/wiki-knowledgebase-share-kit/actions/workflows/validate.yml)

一套面向 markdown / wiki / Obsidian vault 的**8-skill 知识库维护包**。  
目标不是继续堆日志，而是把知识库收敛成：**入口清楚、页面角色稳定、长期可维护、对多人协作友好**。

> **完全新手先看：** [`START-HERE.md`](./START-HERE.md)

**语言 / Language**：[`中文 README`](./README.md) · [`English README`](./README.en.md)

## 快速入口
- [`START-HERE.md`](./START-HERE.md)：5 分钟快速上手
- [`GLOSSARY.md`](./GLOSSARY.md)：核心概念解释
- [`templates/vault-profile-template.md`](./templates/vault-profile-template.md)：主配置模板
- [`templates/working-profile-page-template.md`](./templates/working-profile-page-template.md)：working profile 页面模板
- [`templates/journal-profile-template.md`](./templates/journal-profile-template.md)：journal 配置模板
- [`docs/example-prompts.md`](./docs/example-prompts.md)：可直接复制的提示词
- [`docs/customization-guide.md`](./docs/customization-guide.md)：如何适配自己的 vault
- [`examples/example-vault-profile-generic.md`](./examples/example-vault-profile-generic.md)：不带个人路径的通用 profile 示例
- [`examples/case-study-pathology-ingest-iteration.md`](./examples/case-study-pathology-ingest-iteration.md)：测试驱动的长文档导入案例
- [`GitHub Pages`](https://zouxy111.github.io/wiki-knowledgebase-share-kit/)：在线落地页
- [`Releases`](https://github.com/zouxy111/wiki-knowledgebase-share-kit/releases)：下载已发布版本

---

## 开发者
- 邹星宇
- 杨琦

---

![Share kit preview](./docs/assets/social-preview.png)

## 30 秒看懂这套 kit

| 你现在的 vault 可能是 | 用完这套 kit 后希望变成 |
|---|---|
| 根页堆了很多执行过程和临时记录 | 根页只保留导航、稳定边界、专题入口 |
| `ops` 页越写越像按天流水账 | `ops` 页沉淀成“现象 / 根因 / 处理法 / 边界” |
| `log.md` 变成任务回放 | `log.md` 只保留 milestone 级变化 |
| 内容页越来越多，但没有稳定入口 | 页面必须被 root page / reader entry 收录 |
| 新人或协作者不知道先用哪个 skill | 先走 onboarding，再进入明确分流 |

一句话说：

> 这不是“帮你多记日志”的包，而是“把知识库重新写得像知识库”的包。

---

## 这是一个 8-skill package

当前正式包包含 8 个 skill：

1. `knowledge-base-kit-guide`
2. `knowledge-base-ingest`
3. `knowledge-base-maintenance`
4. `knowledge-base-audit`
5. `knowledge-base-orchestrator`
6. `knowledge-base-team-coordination`
7. `knowledge-base-working-profile`
8. `work-journal`

这 8 个 skill 共同覆盖 **7 条能力线**：

1. **Onboarding / Orchestration**
   - `knowledge-base-kit-guide`：解释安装、profile 配置、技能分流
   - `knowledge-base-orchestrator`：零门槛初始化入口；检测现有环境、可选安装 Obsidian、创建骨架、生成 profile，并给出下一步 skill 路由
2. **Ingest**
   - `knowledge-base-ingest`：拆分长 markdown / 书稿 / 教程，并把第一次导入作为可测试基线
3. **Maintenance**
   - `knowledge-base-maintenance`：把任务结果或结论沉淀进知识库
4. **Audit**
   - `knowledge-base-audit`：检查结构、导航、元数据和噪音回流
5. **Working profile**
   - `knowledge-base-working-profile`：从持续沟通中提炼稳定协作画像
6. **Team coordination**
   - `knowledge-base-team-coordination`：面向多人项目的问卷、对齐、派单和决策蒸馏
7. **Work journal**
   - `work-journal`：记录每日工作、会议纪要、临时想法，并支持周报/沉淀

---

## 适合谁 / 不适合谁

### 适合
- 已经在维护 Obsidian / markdown / wiki vault 的个人或团队
- 想把“任务过程”和“长期知识”拆开的使用者
- 接受固定页面角色模型：`project / knowledge / ops / task / overview`
- 想给长期协作画像、多人项目协调、工作记录建立稳定入口的人

### 不太适合
- 完全不想配置 profile 的人
- 只想保留日志式记录、不关心导航治理的人
- 不接受固定页面角色模型的人
- 希望把 Orchestrator 当成“万能自动代理”的人

---

## 支持平台状态

| 平台 | 状态 | 说明 |
|---|---|---|
| Codex / ChatGPT Codex 风格 skills 目录 | 推荐 | 仓库包含 8 个完整 skill bundle，每个都有 `SKILL.md`、`references/`、`agents/openai.yaml` |
| Claude 风格 skills 目录 | 可用 | 直接复制 8 个 skill 目录即可 |
| 其他支持 `SKILL.md` 目录结构的平台 | 可能可用 | 需自行适配 skill 发现与调用方式 |

如果你不确定平台兼容性，先看：
- `START-HERE.md`
- `docs/usage-sop.md`

---

## 包内结构

```text
wiki-knowledgebase-share-kit/
  COVER-CN.md
  START-HERE.md
  GLOSSARY.md
  README.md
  README.en.md
  docs/
  templates/
    vault-profile-template.md
    working-profile-page-template.md
    journal-profile-template.md
    member-capability-profile-template.md
    ingest-iteration-log-template.md
  examples/
    example-vault-profile-generic.md
    scenario-*.md
  skills/
    knowledge-base-kit-guide/
    knowledge-base-ingest/
    knowledge-base-maintenance/
    knowledge-base-audit/
    knowledge-base-orchestrator/
    knowledge-base-team-coordination/
    knowledge-base-working-profile/
    work-journal/
```

### `examples/` 的说明
- `example-vault-profile*.md` 和 case study 更接近真实落地
- `scenario-*.md` 是**场景化示意**，其中出现的页面链接和目录结构可能是假设性示例，不等于仓库真实文件

---

## 推荐安装方式

把以下 8 个目录复制到你的 skills 目录：

- `skills/knowledge-base-kit-guide`
- `skills/knowledge-base-ingest`
- `skills/knowledge-base-maintenance`
- `skills/knowledge-base-audit`
- `skills/knowledge-base-orchestrator`
- `skills/knowledge-base-team-coordination`
- `skills/knowledge-base-working-profile`
- `skills/work-journal`

常见位置示例：
- `~/.codex/skills`
- `~/.claude/skills`

安装后，至少准备好自己的 `vault profile`，再进入日常使用。

---

## 推荐使用顺序

### 完全新手
- 先用 `knowledge-base-orchestrator`
- 它会优先检测你是否已经有现成的 Obsidian / vault / profile
- 如需安装 Obsidian，默认是**可选步骤**，不是必须步骤
- 初始化完成后，再进入具体 skill

### 想手动理解和配置
- 先用 `knowledge-base-kit-guide`
- 它负责解释 profile、安装方式、以及后续该调用哪个 skill

### 日常分流
- 要导入长文档 / 书籍 / 教程：`knowledge-base-ingest`
- 要沉淀任务结果：`knowledge-base-maintenance`
- 要做结构体检：`knowledge-base-audit`
- 要沉淀长期协作画像：`knowledge-base-working-profile`
- 要协调多人共享项目：`knowledge-base-team-coordination`
- 要记每日工作 / 会议 / 周报：`work-journal`

---

## 这套方法的固定部分

以下内容默认固定，不建议轻易改掉：
- 知识库优先，不收一次性过程噪音
- 页面角色模型：`project / knowledge / ops / task / overview`
- 根页只做导航和稳定总览
- `ops` 页默认写成“现象 / 根因 / 处理法 / 边界”
- `log.md` 只写里程碑，不写任务回放
- 实质维护要同步内容页与导航入口

---

## 先读哪几个文件

最短路径：
- `START-HERE.md` — 新手入口
- `GLOSSARY.md` — 概念解释
- `templates/vault-profile-template.md` — 主配置模板
- `docs/example-prompts.md` — 第一批可直接复制的提示词
- `docs/usage-sop.md` — 8 个 skill 的职责与分流

如果你想继续深入：
- `docs/customization-guide.md`
- `templates/working-profile-page-template.md`
- `templates/journal-profile-template.md`
- `templates/member-capability-profile-template.md`
- `examples/case-study-pathology-ingest-iteration.md`
