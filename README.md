# Wiki Knowledge Base Share Kit

> 一套可分享的 markdown/wiki **知识库导入 + 维护 + 审计 + 多人协同协调** 方法包。  
> 目标：把“知识库优先、页面角色清晰、长文档可迭代导入、多人项目可问卷可对齐可派单可蒸馏”的能力，抽成可安装 skill + 可复制模板 + 可阅读文档。

**语言 / Language**：[`中文 README`](./README.md) · [`English README`](./README.en.md)

## 快速入口
- [`START-HERE.md`](./START-HERE.md)：第一次拿到仓库时的最短上手路径
- [`docs/reuse-from-zero.md`](./docs/reuse-from-zero.md)：给完全不了解本项目的人看的从零复用路径
- [`docs/team-coordination-workflow.md`](./docs/team-coordination-workflow.md)：多人协同问卷派单与决策蒸馏工作流
- [`docs/collaboration-integration-patterns.md`](./docs/collaboration-integration-patterns.md)：OpenClaw / Hermes / NAS / 网盘 / 个人 wiki / agent 的协作接入模式
- [`docs/ingest-evaluation-rubric.md`](./docs/ingest-evaluation-rubric.md)：ingest 的 candidate-vs-baseline 晋升口径
- [`templates/vault-profile-template.md`](./templates/vault-profile-template.md)：配置自己的 vault profile
- [`templates/member-capability-profile-template.md`](./templates/member-capability-profile-template.md)：配置可跨项目复用的成员能力画像
- [`templates/team-project-workspace/`](./templates/team-project-workspace/)：共享项目目录模板骨架
- [`templates/ingest-iteration-log-template.md`](./templates/ingest-iteration-log-template.md)：记录 ingest 每轮 baseline / candidate / regression / decision
- [`docs/customization-guide.md`](./docs/customization-guide.md)：如何改造成自己的知识库体系 / 协同体系
- [`docs/example-prompts.md`](./docs/example-prompts.md)：可直接复制的提示词
- [`Releases`](https://github.com/zouxy111/wiki-knowledgebase-share-kit/releases)：下载发布版本
- [`GitHub Pages`](https://zouxy111.github.io/wiki-knowledgebase-share-kit/)：在线文档

---

![Share kit preview](./docs/assets/social-preview.png)

## 30 秒看懂这套 kit

| 你现在的 vault / 项目可能是 | 用完这套 kit 后希望变成 |
|---|---|
| 根页堆了很多执行过程和临时记录 | 根页只保留导航、稳定边界、专题入口 |
| `ops` 页越写越像按天流水账 | `ops` 页沉淀成“现象 / 根因 / 处理法 / 边界” |
| `log.md` 变成任务回放 | `log.md` 只保留 milestone 级变化 |
| 长文档导入一次就定稿，后续难以比较 | ingest 先落 baseline，再用 rubric 比较 candidate，过回归后再晋升 |
| 多人协作都散落在聊天里 | 用共享项目目录做问卷、对齐、派单、跟进和决策蒸馏 |
| 每个人各自在自己的笔记里做事，最后无法统一 | 个人 wiki / 个人 agent 允许并行，但 shared project directory 始终是正式事实源 |

一句话说：

> 这不是“帮你多记日志”的包，而是“把知识库重新写得像知识库，并把多人协同变成可复用闭环”的包。

---

## 这套分享包解决什么问题

很多 markdown/wiki vault 会遇到三类长期问题：

### A. 长文档导入问题
- 书稿、教程、规范导入后还是一个大长页
- 没有清晰的 overview / chapter / topic 结构
- 术语页、related links、entrypoint 不稳定
- 新方案比旧方案到底更好还是更差，缺少统一判断口径

### B. 知识库维护问题
- 新内容越写越像项目日志，而不像知识库
- 根页、专题页、运维页职责混乱
- `index.md`、导航入口和里程碑日志不同步
- 审计时不知道该检查结构、边界还是噪音回流

### C. 多人协同问题
- 2 人及以上协作时，大家理解的目标和颗粒度不一致
- 不同成员擅长的内容不同，但任务分配没有显式依据
- 问卷、对齐、派单、跟进、决策蒸馏都散落在聊天里，后续无法复用
- 项目里形成的稳定判断和成员画像，难以沉淀回知识库

这套 kit 现在把这些问题抽成 **5 个 skill**：

1. **`knowledge-base-kit-guide`**：安装说明、配置说明、技能分流
2. **`knowledge-base-ingest`**：把长 markdown / 书稿 / 教程拆分、链接并导入知识库；先落 baseline，再比较 candidate，再决定是否晋升
3. **`knowledge-base-maintenance`**：把任务结果或结论沉淀进知识库
4. **`knowledge-base-audit`**：检查知识库结构、导航、元数据和噪音回流
5. **`knowledge-base-team-coordination`**：多人项目 intake、问卷派发、对齐、派单、跟进、决策蒸馏、可选知识库同步

同时保留固定页面角色模型：
- `project`
- `knowledge`
- `ops`
- `task`
- `overview`

但把这些内容改成用户自定义：
- vault 路径
- `pages/` 目录位置
- root pages
- area 列表
- 命名约定
- frontmatter 约定
- 成员画像路径
- 共享项目目录路径
- 是否启用知识库同步

---

## 推荐协作接入模式

### 主推运行平台
本仓库主推：
- **OpenClaw**
- **Hermes**

这里说的“主推”，不是因为 repo 依赖它们的私有 API，而是因为它们很适合承接：
- shared project directory 工作流
- skills / prompts 驱动的协作流程
- 每位成员用自己的 agent 协助整理问卷、回应和进展

### 推荐工作方式
推荐把多人协同理解成三层：
- **shared project directory**：团队事实源
- **每个人自己的 wiki / 私有资料区**：个人工作面
- **每个人自己的 agent（如 OpenClaw / Hermes）**：个人协作助手

底线规则：
- 个人 wiki / 个人 agent 不是 coordinator 的默认事实源
- 只有**同步回 shared project directory 的 markdown 文件**才进入正式协调闭环

### 推荐同步拓扑
- **模式 1**：`team-project/` 独立放在 NAS / 网盘同步目录
- **模式 2**：`team-project/` 直接嵌入共享 wiki / 共享知识库子目录

详见：[`docs/collaboration-integration-patterns.md`](./docs/collaboration-integration-patterns.md)

---

## 适合谁 / 不适合谁

### 适合
- 已经在维护 Obsidian / markdown / wiki vault 的个人或团队
- 想把“任务过程”和“长期知识”拆开的使用者
- 想把长篇知识源做成可比较、可回归、可晋升的 ingest 回路的人
- 想协调 2 人及以上共享项目目录，并保留统一事实源的人
- 接受固定页面角色模型：`project / knowledge / ops / task / overview`

### 不太适合
- 完全不想配置 profile 或共享项目目录的人
- 希望 vault 继续以流水日志为主的人
- 不接受固定页面角色模型的人
- 只想记录原始过程，不在意知识沉淀和导航治理的人
- 希望多人协同完全靠聊天推进、不愿意维护共享 markdown 契约的人

---

## 使用案例

- [`examples/case-study-current-vault.md`](./examples/case-study-current-vault.md)：从当前 vault 抽象出可分享的固定规则
- [`examples/case-study-pathology-ingest-iteration.md`](./examples/case-study-pathology-ingest-iteration.md)：展示如何把长篇专业 Markdown 先导入成可测试基线，再用 rubric 和回归检查持续优化
- [`examples/team-project-generic/`](./examples/team-project-generic/)：通用 2 人项目的问卷 / 对齐 / 派单示例
- [`examples/team-project-qc/`](./examples/team-project-qc/)：QC 多人协同示例

---

## 支持平台状态

| 平台 | 状态 | 说明 |
|---|---|---|
| Codex / ChatGPT Codex 风格 skills 目录 | 推荐 | 仓库已包含 `SKILL.md`、`references/`、`agents/openai.yaml` |
| Claude 风格 skills 目录 | 可用 | 直接复制五个 skill 目录即可 |
| OpenClaw / Hermes | 推荐承接多人协同 runtime | 适合复用 shared project directory + skills / prompts 工作流 |
| 其他支持 `SKILL.md` 目录结构的平台 | 可能可用 | 需自行适配调用方式与 skill 发现机制 |

如果你不确定平台兼容性，先看：
- [`START-HERE.md`](./START-HERE.md)
- [`docs/usage-sop.md`](./docs/usage-sop.md)
- [`docs/reuse-from-zero.md`](./docs/reuse-from-zero.md)

---

## 包内结构

```text
wiki-knowledgebase-share-kit/
  COVER-CN.md
  START-HERE.md
  README.md
  README.en.md
  docs/
    team-coordination-workflow.md
    collaboration-integration-patterns.md
    ingest-evaluation-rubric.md
  templates/
    vault-profile-template.md
    member-capability-profile-template.md
    team-project-workspace/
    ingest-iteration-log-template.md
  examples/
    example-vault-profile-generic.md
    team-project-generic/
    team-project-qc/
  skills/
    knowledge-base-kit-guide/
    knowledge-base-ingest/
    knowledge-base-maintenance/
    knowledge-base-audit/
    knowledge-base-team-coordination/
```

### `skills/`
可直接复制到本地 AI 平台的 `skills/` 目录里使用。

### `templates/`
包含三类模板：
- `vault profile`：给知识库 maintenance / audit / 可选 sync 使用
- `team project workspace`：给多人协同项目使用
- `ingest iteration log`：给长文档导入的 baseline / candidate / regression 记录使用

### `docs/`
平台无关的说明文档。即使不安装 skill，也可以按这里的方法手工维护知识库、跑 ingest 迭代或跑多人协同。

### `examples/`
包含真实案例，也包含**不带个人路径的通用示例**，方便公开仓库读者直接参考。

---

## 最短上手顺序

### 如果你是知识库场景
1. 看 [`START-HERE.md`](./START-HERE.md)
2. 复制 [`templates/vault-profile-template.md`](./templates/vault-profile-template.md)
3. 复制五个 `skills/` 目录到你的平台
4. 第一次先用 `knowledge-base-kit-guide`
5. 长文档导入时，再看 [`docs/ingest-evaluation-rubric.md`](./docs/ingest-evaluation-rubric.md)

### 如果你是多人协同场景
1. 看 [`START-HERE.md`](./START-HERE.md)
2. 看 [`docs/collaboration-integration-patterns.md`](./docs/collaboration-integration-patterns.md)
3. 复制 [`templates/team-project-workspace/`](./templates/team-project-workspace/)
4. 如需长期画像，再复制 [`templates/member-capability-profile-template.md`](./templates/member-capability-profile-template.md)
5. 第一次先用 `knowledge-base-kit-guide` 或 `knowledge-base-team-coordination`

---

## 开发者
- 邹星宇
- 杨琦

---

## License

本项目采用 MIT License，详见 [`LICENSE`](./LICENSE)。
