# Wiki Knowledge Base Share Kit

[![Release](https://img.shields.io/github/v/release/zouxy111/wiki-knowledgebase-share-kit)](https://github.com/zouxy111/wiki-knowledgebase-share-kit/releases)
[![Validate](https://github.com/zouxy111/wiki-knowledgebase-share-kit/actions/workflows/validate.yml/badge.svg)](https://github.com/zouxy111/wiki-knowledgebase-share-kit/actions/workflows/validate.yml)
[![Stars](https://img.shields.io/github/stars/zouxy111/wiki-knowledgebase-share-kit)](https://github.com/zouxy111/wiki-knowledgebase-share-kit/stargazers)
[![Forks](https://img.shields.io/github/forks/zouxy111/wiki-knowledgebase-share-kit)](https://github.com/zouxy111/wiki-knowledgebase-share-kit/forks)
[![Contributors](https://img.shields.io/github/contributors/zouxy111/wiki-knowledgebase-share-kit)](https://github.com/zouxy111/wiki-knowledgebase-share-kit/graphs/contributors)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](./LICENSE)

> 一套面向 markdown / wiki / Obsidian-style vault 的 **8-skill 知识库维护包**。
> 目标不是堆更多日志，而是把知识库收敛成：**入口清楚、页面角色稳定、长期可维护、对协作友好、可审计**。

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
- 根页越写越像流水账
- 长文档、会议纪要、任务结论混在一起
- 新人或协作者不知道先看哪里，也不知道该用哪个 workflow

这套 kit 要解决的是：

| 典型问题 | 目标状态 |
|---|---|
| 根页越来越像流水账 | 根页只保留导航、稳定边界、专题入口 |
| 长文档导入后很难复用 | 拆成 overview / chapter / topic 结构，并保留来源链 |
| 任务结果只存在聊天里 | 把可复用结论沉淀到合适页面 |
| 知识库乱了却没人知道哪里坏了 | 用 audit 定期检查死链、孤页、边界漂移、噪音回流 |
| 协作信息零散、不好交接 | 用 working profile、team coordination、journal 形成稳定协作面 |

一句话说：

> 让你的 markdown 仓库更像知识库，而不是“写过但以后找不到”的资料堆。

---

## 这是一个 8-skill package

当前正式包包含 8 个 skill：

1. `knowledge-base-kit-guide`
2. `knowledge-base-orchestrator`
3. `knowledge-base-ingest`
4. `knowledge-base-maintenance`
5. `knowledge-base-audit`
6. `knowledge-base-working-profile`
7. `knowledge-base-team-coordination`
8. `work-journal`

它们共同覆盖 7 条能力线：
- **Onboarding / Orchestration**
- **Ingest**
- **Maintenance**
- **Audit**
- **Working profile**
- **Team coordination**
- **Work journal**

其中：
- `knowledge-base-kit-guide` 负责解释安装、profile 配置、技能分流
- `knowledge-base-orchestrator` 负责低门槛初始化：检查现有环境、创建骨架、生成 profile、推荐下一步 specialist skill

> `knowledge-base-orchestrator` 是 **onboarding coordinator**，不是“万能自动代理”。

---

## 适合谁

### 适合
- 已经在维护 markdown / wiki / Obsidian vault 的个人或团队
- 想把“任务过程”和“长期知识”拆开的使用者
- 接受固定 page-role model：`project / knowledge / ops / task / overview`
- 想为长文档导入、知识沉淀、协作画像、团队协调、工作记录建立稳定 workflow 的人

### 不太适合
- 完全不想配置 `vault profile` 的人
- 只想保留日志式记录、不关心导航治理的人
- 期待系统默认后台全自动运行的人
- 不接受固定页面角色模型的人

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
- journal 里的内容需要经过筛选后，才应进入 `knowledge` / `ops` / `project` 等稳定页面

---

## 为什么这套方法有效

它依赖几个固定原则：

1. **Knowledge-base-first**：只保留长期有用的内容，过滤一次性噪音
2. **固定角色模型**：每个页面都有清晰职责，避免混写
3. **四同步机制**：每次实质更新至少同步目标页、root page、`index.md`、`log.md`
4. **Milestone-only log**：`log.md` 只记录里程碑，不写任务回放
5. **定期审计**：周期性检查结构、导航、元数据和噪音回流

---

## 推荐场景：高知识密度 + 多人协作 + 可审计

这套 kit 特别适合一类场景：

> **知识密度高、更新频繁、协作复杂、又需要可追溯和可审计的工作环境。**

这包括但不限于：
- 医疗 / 病理 / 科研
- 企业知识库 / 项目交付 / 运维文档
- 跨团队协作 / 新人 onboarding / 会议结论沉淀

这些场景看上去不同，但底层问题很像：

| 共同问题 | 在医疗/科研里的表现 | 在企业/团队里的表现 |
|---|---|---|
| 长文档多，复用难 | 指南、教材、文献、病例总结难检索 | PRD、方案、操作手册、会议材料难回查 |
| 经验零散 | 临床/科研经验散在笔记里 | 项目经验散在聊天、会议纪要、临时文档里 |
| 人员协作复杂 | 导师、同事、研究伙伴的信息难追踪 | 跨部门、跨角色协作要反复同步背景 |
| 需要边界和可审计性 | 内容不能随意混写，更新要谨慎 | 团队治理需要清楚的导航、责任和审计结果 |

所以更准确地说，这不是“医生版”和“企业版”两个不同产品；而是同一套方法在 **高知识密度协作场景** 下的两种常见落地。

---

## 这套 kit 在这个场景里怎么用

### 1. 导入长文档 / 书籍 / 指南 / 方案
使用 `knowledge-base-ingest`：
- 先读 `vault profile`
- 先把长 source 脚本化拆成 bounded chunks，再重组为 overview / chapter / topic
- 建立 toc、glossary candidates、related-link suggestions
- 用 `manifest.json` + `coverage-map.md` 显式跟踪每个 chunk 是否已处理
- 只有 `verify_ingest_coverage.py` 通过后，才把结果视为完整导入
- 把第一版导入当成 **可测试基线**，通过迭代和回归继续优化结构

适合：
- 医学书籍 / 指南 / 文献整理
- 企业 SOP / PRD / 交付文档 / 培训资料整理

### 2. 沉淀任务结果和会议结论
使用 `knowledge-base-maintenance`：
- 从任务、会议、对话、交付物中提炼稳定结论
- 过滤一次性过程噪音
- 更新目标页面，并同步导航入口和里程碑日志

### 3. 做周期性结构治理
使用 `knowledge-base-audit`：
- 检查 dead links、orphan pages、missing entrypoints
- 检查 page-boundary drift、metadata 问题、root-level stray files
- 输出可追溯的 P1 / P2 / P3 findings

### 4. 维护协作画像和共享项目上下文
使用：
- `knowledge-base-working-profile`
- `knowledge-base-team-coordination`
- `work-journal`

这里的目标不是“自动建私人档案”，而是：
- 只提炼**对未来协作有用**的稳定信号
- 区分 `confirmed / repeated / inferred`
- 过滤敏感个人信息与不应长期保存的内容
- 在共享项目中保持 draft / approved 边界

---

## 关于 working profile：边界要说清楚

`knowledge-base-working-profile` 沉淀的是 **working profile**，不是私人档案系统。

它关注的是：
- 稳定偏好
- 决策习惯
- 协作边界
- 反模式
- 与未来协作直接相关的稳定信号

默认不应长期保存：
- 高敏感个人信息
- 与未来协作无关的私人细节
- 第三方隐私
- 未经确认的强推断
- 一次性情绪表达

如果涉及共享、团队、医疗等敏感场景，应该额外强调：
- consent
- visibility
- 只共享必要信息
- 先确认，再升级为稳定画像

---

## 推荐使用顺序

### 完全新手
1. 先看 `START-HERE.md`
2. 准备 `templates/vault-profile-template.md`
3. 用 `knowledge-base-orchestrator` 完成初始化
4. 再进入 specialist skill

### 想先理解方法再动手
1. 先用 `knowledge-base-kit-guide`
2. 理解 profile、角色模型、技能分流
3. 再选择 ingest / maintenance / audit / working-profile / team-coordination / journal

### 已经知道自己要做什么
直接进入对应 specialist skill：
- 导入长文档：`knowledge-base-ingest`
- 沉淀任务结果：`knowledge-base-maintenance`
- 做结构体检：`knowledge-base-audit`
- 更新协作画像：`knowledge-base-working-profile`
- 协调共享项目：`knowledge-base-team-coordination`
- 记录日常工作：`work-journal`

---

## 安装方式

先说原则：

> 这套包本质上是 **8 个 `SKILL.md` 风格 skill bundle**。
> 只要你的 AI 平台支持类似 skills 目录结构，就可以安装；不同平台的目录位置可能不同。
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

常见示例：

```bash
cp -r skills/knowledge-base-kit-guide ~/.codex/skills/
cp -r skills/knowledge-base-orchestrator ~/.codex/skills/
cp -r skills/knowledge-base-ingest ~/.codex/skills/
cp -r skills/knowledge-base-maintenance ~/.codex/skills/
cp -r skills/knowledge-base-audit ~/.codex/skills/
cp -r skills/knowledge-base-working-profile ~/.codex/skills/
cp -r skills/knowledge-base-team-coordination ~/.codex/skills/
cp -r skills/work-journal ~/.codex/skills/
```

也可按平台改到：
- `~/.codex/skills`
- `~/.claude/skills`
- 或其他支持 `SKILL.md` bundle 的平台目录

> 如果你使用 OpenClaw、Hermes Agent、Claude Code 或其他兼容平台，请先确认该平台的 skills 目录约定，再安装。

---

## OpenClaw / Hermes / MinerU 适配说明

这套方法和以下工具组合时通常会更顺手：
- **OpenClaw**：适合作为日常 AI 助手运行平台
- **Hermes Agent**：适合作为可持续协作与成长型 agent 平台
- **MinerU**：适合把 PDF / 复杂文档转成 LLM 可处理的 markdown

但要注意：
- 这些平台/工具是**推荐组合**，不是本仓库唯一依赖
- 本仓库的核心价值仍然是 **知识库结构治理与 workflow 设计**，不是平台绑定

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

# 4. 把 8 个 skills 安装到你的运行时目录
python3 scripts/install_skills.py --platform codex --force
```

如果你已经准备好平台和 skills 目录，再安装 8 个 skill bundle。

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

**Q：企业和医疗是不是两套完全不同的方案？**
A：不是。它们都属于“高知识密度 + 多人协作 + 可审计”的场景，只是资料类型和协作方式不同。

**Q：working profile 会不会变成隐私档案？**
A：不应该。正确做法是只保留协作相关的稳定信号，并明确 consent、visibility 和敏感信息过滤边界。

---

## 建议先读哪些文件

- `START-HERE.md`
- `GLOSSARY.md`
- `templates/vault-profile-template.md`
- `docs/example-prompts.md`
- `docs/usage-sop.md`
- `examples/case-study-pathology-ingest-iteration.md`

---

## 需要帮助？

- [GitHub Issues](https://github.com/zouxy111/wiki-knowledgebase-share-kit/issues)
- 开发者：邹星宇、杨琦

---

## License

MIT License

---

> 如果你想让知识库更像知识库，而不是更像资料堆，先从 `START-HERE.md` 开始。
