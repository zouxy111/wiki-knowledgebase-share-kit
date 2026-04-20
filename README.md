# Wiki Knowledge Base Share Kit

[![Release](https://img.shields.io/github/v/release/zouxy111/wiki-knowledgebase-share-kit)](https://github.com/zouxy111/wiki-knowledgebase-share-kit/releases)
[![Validate](https://github.com/zouxy111/wiki-knowledgebase-share-kit/actions/workflows/validate.yml/badge.svg)](https://github.com/zouxy111/wiki-knowledgebase-share-kit/actions/workflows/validate.yml)
[![Stars](https://img.shields.io/github/stars/zouxy111/wiki-knowledgebase-share-kit)](https://github.com/zouxy111/wiki-knowledgebase-share-kit/stargazers)
[![Forks](https://img.shields.io/github/forks/zouxy111/wiki-knowledgebase-share-kit)](https://github.com/zouxy111/wiki-knowledgebase-share-kit/forks)
[![Contributors](https://img.shields.io/github/contributors/zouxy111/wiki-knowledgebase-share-kit)](https://github.com/zouxy111/wiki-knowledgebase-share-kit/graphs/contributors)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](./LICENSE)

> 一套面向 markdown / wiki / Obsidian-style vault 的 **10-skill 知识库维护 + 协作包**。  
> 默认先解决知识库结构治理；当你需要项目 owner 推进、多人协同和交付闭环时，再渐进式加载 PM 主线。

<p align="center">
  <a href="https://zouxy111.github.io/wiki-knowledgebase-share-kit/"><img src="https://img.shields.io/badge/Open-HTML_Homepage-4ab9ff?style=for-the-badge" alt="Open HTML Homepage" /></a>
  <a href="./START-HERE.md"><img src="https://img.shields.io/badge/Read-START--HERE-0f172a?style=for-the-badge" alt="Read START-HERE" /></a>
  <a href="https://github.com/zouxy111/wiki-knowledgebase-share-kit/releases"><img src="https://img.shields.io/badge/Browse-Releases-0ea5a4?style=for-the-badge" alt="Browse Releases" /></a>
</p>

[![HTML homepage preview](./docs/assets/social-preview.png)](https://zouxy111.github.io/wiki-knowledgebase-share-kit/)

> 想看更像产品首页的 HTML 界面，请直接打开上面的 **HTML Homepage**；仓库 README 继续承担安装、分流和方法说明。

---

## 30 秒看懂

很多知识库的问题，不是“没写”，而是：
- 写了很多，但没有稳定入口
- 根页越来越像流程流水账
- 长文档、会议纪要、任务结论混写
- 协作上下文散落在聊天、个人笔记和临时文档里
- 项目明明在推进，但没有统一的 milestone / blocker / delivery gate 视图

这套 kit 要把它收敛成：

| 典型问题 | 目标状态 |
|---|---|
| 根页越来越像流水账 | 根页只保留导航、边界、专题入口 |
| 长文档导入后很难复用 | 拆成 overview / chapter / topic 结构，并保留来源链 |
| 任务结果只存在聊天里 | 把稳定结论沉淀到合适页面 |
| 知识库乱了却没人知道哪里坏了 | 用 audit 周期性检查死链、孤页、边界漂移、噪音回流 |
| 多人协作总在重复解释背景 | 用 working profile、team coordination、journal 建立稳定协作面 |
| 项目 owner 不知道怎么推进 | 用 project-management / delivery-audit 建立里程碑、blocker、验收闭环 |

一句话说：

> 让你的 markdown 仓库更像知识库，也让共享项目更像可追踪、可验收的工作流，而不是“聊过就散”的临时协作。

---

## 这是一个 10-skill package

当前正式包包含 10 个 skill：

1. `knowledge-base-kit-guide`
2. `knowledge-base-orchestrator`
3. `knowledge-base-ingest`
4. `knowledge-base-maintenance`
5. `knowledge-base-audit`
6. `knowledge-base-project-management`
7. `knowledge-base-team-coordination`
8. `knowledge-base-delivery-audit`
9. `knowledge-base-working-profile`
10. `work-journal`

它们共同覆盖 9 条能力线：
- **Onboarding / Orchestration**
- **Ingest**
- **Maintenance**
- **Audit**
- **Project management**
- **Team coordination**
- **Delivery audit**
- **Working profile**
- **Work journal**

其中：
- `knowledge-base-kit-guide` 负责解释安装、profile 配置、技能分流
- `knowledge-base-orchestrator` 负责低门槛初始化：检查现有环境、创建骨架、生成 profile、推荐下一步 specialist skill
- `knowledge-base-project-management` 负责项目 owner 视角的 intake / 里程碑 / blocker / next action
- `knowledge-base-team-coordination` 负责 2 人及以上的共享项目目录协调
- `knowledge-base-delivery-audit` 负责交付完整性、ready / blocked / greenlight 审计

> `knowledge-base-orchestrator` 是 **onboarding coordinator**，不是“万能自动代理”。

---

## 默认主线 vs 可选 PM 主线

### 默认主线：先窄后稳
如果你只是：
- 导入长文档
- 维护知识库
- 做结构审计
- 记录协作画像或工作日志

那默认先走：
- `knowledge-base-kit-guide`
- `knowledge-base-orchestrator`
- `knowledge-base-ingest`
- `knowledge-base-maintenance`
- `knowledge-base-audit`

### 可选 PM 主线：按需加载
只有当你明确出现这些意图时，再进入 PM 主线：
- 项目管理
- 周计划
- 里程碑
- blocker / dependency
- handoff
- ready / greenlight
- 项目复盘

PM 主线由这 3 个 skill 构成：
- `knowledge-base-project-management`
- `knowledge-base-team-coordination`
- `knowledge-base-delivery-audit`

这条主线对应一个新的**可选 area**：
- `project-management`

它只承接**管理层材料**，不替代业务 area，也不替代 `governance`。

详见：
- [`docs/project-management-workflow.md`](./docs/project-management-workflow.md)
- [`templates/project-management/README.md`](./templates/project-management/README.md)

---

## 适合谁

### 适合
- 已经在维护 markdown / wiki / Obsidian vault 的个人或团队
- 想把“任务过程”和“长期知识”拆开的使用者
- 接受固定 page-role model：`project / knowledge / ops / task / overview`
- 想为长文档导入、知识沉淀、协作画像、多人协作、项目推进和交付审计建立稳定 workflow 的人

### 不太适合
- 完全不想配置 `vault profile` 的人
- 只想保留日志式记录、不关心导航治理的人
- 期待系统默认后台全自动运行的人
- 不接受固定页面角色模型和显式状态边界的人

---

## 核心模型：5 个固定页面角色

这套方法使用 **5 个固定 page roles**：

| 角色 | 用途 | 不该承载什么 |
|---|---|---|
| `project` | 项目导航、总览、边界 | 长流水、临时聊天记录 |
| `knowledge` | 方法、概念、可复用知识 | “今天做了什么”式过程记录 |
| `ops` | 排障手册、操作流程、边界说明 | 单次修复回放 |
| `task` | 待办、分工、进行中任务 | 长期知识沉淀 |
| `overview` | 知识库首页、治理规则、索引 | 项目历史细节 |

补充说明：
- `work-journal` 是**独立 workflow**，不是第 6 个固定 page role
- `project-management` 是**可选 area**，不是新 page role
- journal、PM 板面和 shared project artifacts 里的信息，都要经过筛选后再进入稳定知识页

---

## 为什么这套方法有效

它依赖几个固定原则：

1. **Knowledge-base-first**：只保留长期有用的内容，过滤一次性噪音
2. **固定角色模型**：每个页面都有清晰职责，避免混写
3. **四同步机制**：每次实质更新至少同步目标页、root page、`index.md`、`log.md`
4. **Milestone-only log**：`log.md` 只记录里程碑，不写任务回放
5. **定期审计**：周期性检查结构、导航、元数据和噪音回流
6. **草案 / 审批边界**：多人协同和 PM 主线中的关键工件要区分 `draft / approved / blocked / superseded`

---

## 推荐场景：高知识密度 + 多人协作 + 可审计

这套 kit 特别适合一类场景：

> **知识密度高、更新频繁、协作复杂、又需要可追溯和可审计的工作环境。**

这包括但不限于：
- 医疗 / 病理 / 科研
- 企业知识库 / 项目交付 / 运维文档
- 跨团队协作 / 新人 onboarding / 会议结论沉淀
- 需要项目 owner 推进、多人对齐和交付 gate 的协作型团队

---

## PM 主线怎么放，才不污染结构

新增 area：
- `project-management`

边界固定为：
- 业务事实 → 原业务 area
- 知识库治理 → `governance`
- 项目推进方法 / 看板 / 风险 / 决策 / delivery gate → `project-management`

默认推荐 3 个板块：
1. **Portfolio / 项目总览**
2. **Team coordination / 团队协同**
3. **Personal execution / 个人执行**

推荐模板：
- `project-project-management-overview.md`
- `pm-portfolio-board.md`
- `pm-operating-model.md`
- `pm-personal-execution-board.md`
- `pm-weekly-review-ops.md`
- `pm-delivery-gates.md`
- `pm-risk-register.md`
- `pm-decision-register.md`

---

## OpenClaw / Hermes / NAS / 个人 wiki 的协作接入模式

本仓库当前主推：
- **OpenClaw**
- **Hermes**

这里说的“无缝接入”，默认是指：
- 使用同一套 shared project directory 契约
- 承接同一套 skills / prompts / coordinator workflow
- 不依赖平台私有 API

推荐协作模式：
- `team-project/` 作为共享事实源
- 每位成员在自己的个人 wiki / 私有资料区里整理草稿和判断过程
- 每位成员可以用自己的 OpenClaw / Hermes / 其他 agent 协助填写问卷、整理回应、更新进展
- 最终只有**同步回 shared project directory 的 markdown 文件**进入正式协调闭环

推荐同步拓扑：
1. `team-project/` 独立放在 NAS / 网盘同步目录
2. `team-project/` 嵌入共享 wiki / 共享知识库子目录

详见：
- [`docs/collaboration-integration-patterns.md`](./docs/collaboration-integration-patterns.md)
- [`docs/team-coordination-workflow.md`](./docs/team-coordination-workflow.md)

---

## 安装方式

先说原则：

> 这套包本质上是 **10 个 `SKILL.md` 风格 skill bundle**。  
> 只要你的 AI 平台支持类似 skills 目录结构，就可以安装。  
> **重点：运行时只会读取它自己的 skills 目录，不会自动读取这个 Git 仓库里的 `skills/`。**

推荐优先使用仓库自带安装脚本，而不是手工逐条复制：

```bash
# 安装到 Codex
python3 scripts/install_skills.py --platform codex --force

# 安装到 Claude Code
python3 scripts/install_skills.py --platform claude --force
```

安装后一定要：
1. **重开当前会话**或重启 runtime
2. 确认 available skills 里真的出现目标 skill 名
3. 如果还报 `Skill not found`，先看 [`docs/skill-installation-troubleshooting.md`](./docs/skill-installation-troubleshooting.md)

### 推荐：一键安装脚本

```bash
# 自动检测平台并安装（支持 Kimi CLI / Claude Code / Codex / 通用 agents）
bash install.sh

# 预览安装内容
bash install.sh --dry-run

# 验证安装结果
bash verify-installation.sh
```

### 手动安装（备选）

```bash
cp -r skills/knowledge-base-kit-guide ~/.codex/skills/
cp -r skills/knowledge-base-orchestrator ~/.codex/skills/
cp -r skills/knowledge-base-ingest ~/.codex/skills/
cp -r skills/knowledge-base-maintenance ~/.codex/skills/
cp -r skills/knowledge-base-audit ~/.codex/skills/
cp -r skills/knowledge-base-project-management ~/.codex/skills/
cp -r skills/knowledge-base-team-coordination ~/.codex/skills/
cp -r skills/knowledge-base-delivery-audit ~/.codex/skills/
cp -r skills/knowledge-base-working-profile ~/.codex/skills/
cp -r skills/work-journal ~/.codex/skills/
```

---

## 快速上手

```bash
# 1. 克隆仓库
git clone https://github.com/zouxy111/wiki-knowledgebase-share-kit.git
cd wiki-knowledgebase-share-kit

# 2. 先看新手入口
cat START-HERE.md

# 3. 复制模板并准备 profile
cp templates/vault-profile-template.md ./my-vault-profile.md

# 4. 把 10 个 skills 安装到你的运行时目录
python3 scripts/install_skills.py --platform codex --force
```

如果你已经准备好平台和 skills 目录，再安装整包即可。  
如果你暂时不需要 PM 主线，不必一开始就配置 `project-management` area。

---

## 常见问题

**Q：我不用 Obsidian，能用吗？**  
A：能。只要你有 markdown/wiki vault，并且平台支持相应 skill 目录结构，就可以用。

**Q：我不想全自动，只想按规则手动整理，能用吗？**  
A：能。你可以直接使用文档、模板和 checklist；AI 只是提高执行效率。

**Q：我已经有很多旧笔记了，还能用吗？**  
A：能。建议先跑一次 audit，再逐步修结构、补导航、收敛页面边界。

**Q：为什么 repo 里明明有 `knowledge-base-ingest`，运行时却说 `Skill not found`？**  
A：通常不是 repo 缺 skill，而是**当前运行平台的 skills 目录没有安装/刷新**。先用 `python3 scripts/install_skills.py --platform <codex|claude> --force` 安装，再重开会话；详见 [`docs/skill-installation-troubleshooting.md`](./docs/skill-installation-troubleshooting.md)。

**Q：怎么防止长文档只读前半部分就被误判为“已完整导入”？**  
A：不要直接把超长 source 整篇塞给模型。先运行 `split_markdown.py` 生成 `manifest.json` 和 `coverage-map.md`，逐 chunk 处理，再用 `verify_ingest_coverage.py` 做完成态校验；详见 [`docs/ingest-completeness-guardrails.md`](./docs/ingest-completeness-guardrails.md)。

**Q：项目管理是不是会把业务知识和 governance 搅在一起？**  
A：不会。PM 主线固定要求：业务事实回原 area，治理规则留在 `governance`，管理层板面才进入 `project-management`。

**Q：我是不是一开始就必须配置 PM area？**  
A：不是。PM 主线按需加载。只有当你真的需要项目 owner 视角推进、多人协同和交付 gate 时再启用。

**Q：OpenClaw / Hermes 是不是平台专供逻辑？**  
A：不是。当前是主推平台，但兼容性来自 shared project directory 契约、skills/prompt 工作方式和 markdown 协议，不依赖平台私有 API。

---

## 建议先读哪些文件

- [`START-HERE.md`](./START-HERE.md)
- [`GLOSSARY.md`](./GLOSSARY.md)
- [`templates/vault-profile-template.md`](./templates/vault-profile-template.md)
- [`docs/example-prompts.md`](./docs/example-prompts.md)
- [`docs/usage-sop.md`](./docs/usage-sop.md)
- [`docs/project-management-workflow.md`](./docs/project-management-workflow.md)
- [`examples/case-study-pathology-ingest-iteration.md`](./examples/case-study-pathology-ingest-iteration.md)

---

## 需要帮助？

- [GitHub Issues](https://github.com/zouxy111/wiki-knowledgebase-share-kit/issues)
- 开发者：邹星宇、杨琦、张陈祎

---

## License

MIT License

---

> 如果你想让知识库更像知识库，也想让项目协作更像可复用、可审计的工作流，先从 `START-HERE.md` 开始。
