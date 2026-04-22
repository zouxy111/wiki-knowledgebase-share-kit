# Collaboration Integration Patterns

> 这份文档专门解释这套 share kit 的**协作接入模式**：  
> 如何把 `knowledge-base-team-coordination` 跑在 OpenClaw、Hermes 或其他 agent runtime 上，以及为什么共享项目目录仍是唯一事实源。

---

## 1. 这份文档解决什么问题

很多人已经能看懂这套仓库有 10 个 skills，但第一次真正落地多人协同时，仍会卡在这些问题：
- OpenClaw / Hermes 到底是“兼容”还是“主推平台”？
- 共享项目目录应该放在 NAS / 网盘里，还是直接嵌进共享 wiki？
- 每个人能不能在自己的 wiki / 私有资料区里先整理内容？
- 每个人自己的 agent 能不能先帮忙回答问卷？
- 如果大家都在并行工作，最终到底什么才算 coordinator 的事实源？

这份文档把这些协作接入模式一次说清楚。

---

## 2. OpenClaw / Hermes 为什么是主推平台

本仓库把 **OpenClaw** 和 **Hermes** 视为主推运行平台。

这里说的“主推”，不是因为 repo 里为它们写了平台专有逻辑，而是因为它们都很适合承接这套 workflow：
- 适合驱动共享项目目录上的多文件协作流程
- 适合把 skills / prompts / 项目规则组织成稳定工作流
- 适合让不同成员在自己的工作面里使用 agent 协助整理问卷、回应和进展

### “无缝接入”在这里是什么意思
默认解释为：
1. 使用同一套 `team-project/` 目录契约
2. 承接同一套 `knowledge-base-team-coordination` 协调逻辑
3. 可以复用同样的 prompts / skills / markdown 协作协议
4. 不依赖 OpenClaw 或 Hermes 的平台私有 API

也就是说：

> 兼容性来自 **共享项目目录契约 + 协作文档协议 + skills/prompt 工作方式**，而不是某个平台专有功能。

---

## 3. 推荐协作模式：共享目录 + 各自 agent + 可选知识库同步

本仓库推荐把多人协同理解成三层：

### A. 共享项目目录
这是 coordinator 的唯一事实源。

### B. 每个人自己的工作面
每位成员可以保留自己的：
- wiki
- 私有资料区
- 草稿区
- 笔记区
- 本地 agent 工作区

这些空间可以用来：
- 整理原始资料
- 写草稿
- 做判断过程
- 让自己的 OpenClaw / Hermes / 其他 agent 帮忙形成更好的回答

### C. 可选知识库同步
只有当：
- 有 vault profile
- 用户希望同步
- 内容已是 `approved`

时，稳定决策或成员画像增量才回写知识库。

---

## 4. NAS / 网盘同步的双模式并列拓扑

本仓库明确支持两种推荐拓扑，不强制单一默认模式。

### 模式 1：共享项目目录独立放在 NAS / 网盘同步目录

适合：
- 团队已经有共享 NAS / 网盘
- 大家不共用同一棵 wiki
- 想把协作事实层和个人知识层分开

### 模式 2：共享项目目录嵌入共享 wiki / 共享知识库子目录

适合：
- 团队本来就维护同一个共享 wiki
- 希望协作和知识沉淀在同一棵库里完成

### 两种模式共同的底线
无论你选哪种拓扑：
- `team-project/` 始终是协调事实源
- 个人 wiki / 个人资料区只是辅助工作区
- 只有已同步进共享项目目录的 markdown 内容，才进入正式协调流程

---

## 5. 个人 wiki + 自己的 agent 的推荐工作方式

这是本仓库明确推荐、但**不写成模板硬约束**的工作模式。

### 推荐做法
每位成员都可以：
1. 在自己的 wiki / 私有资料区整理材料
2. 用自己的 OpenClaw / Hermes / 其他 agent 辅助阅读问卷
3. 先在个人空间里形成草稿、对照表、判断过程
4. 再把最终要进入协作流程的版本，写回：
   - `members/<id>/response.md`
   - `members/<id>/progress-update.md`
   - 或其它 shared project 约定文件

### 为什么推荐这样做
因为它同时满足两件事：
- **允许并行工作**：每个人都能用自己熟悉的工具、自己的 agent、自己的知识库节奏
- **不破坏共享事实源**：只有同步回 shared project directory 的内容才会被 coordinator 采信

---

## 6. Coordinator 与成员 agent 的职责分工

### Coordinator AI 负责
- 读取共享项目目录
- 生成成员级问卷
- 做 alignment / assignment / follow-up / distill
- 判断哪些内容仍是 draft，哪些可以进入 approved

### 每位成员自己的 agent 负责
- 协助理解问卷
- 协助整理个人资料和草稿
- 协助把个人想法组织成更清晰的回应
- 协助把阶段性进展整理成可同步格式

### 固定原则
- 成员 agent 不是 coordinator 的替代者
- 成员 agent 不应直接改写团队事实边界
- 最终进入协作闭环的仍是共享目录里的文件

---

## 7. 它和 PM 主线是什么关系

多人协同接入模式与 PM 主线兼容，但不是同一个层次：
- `knowledge-base-project-management` 负责 owner 视角的里程碑 / blocker / priority
- `knowledge-base-team-coordination` 负责共享项目目录上的多人成员事实层
- `knowledge-base-delivery-audit` 负责 closeout / ready / greenlight 审计

所以：

> 个人 wiki 和个人 agent 是辅助工作面；shared project directory 是协调事实源；`project-management` area 则是 owner 和 gate 的管理层工作面。

---

## 8. 推荐入口文件顺序

如果你想让第一次接触的人快速看懂“怎么接入”，推荐按这个顺序读：
1. `START-HERE.md`
2. `README.md`
3. `docs/collaboration-integration-patterns.md`
4. `docs/team-coordination-workflow.md`
5. `docs/project-management-workflow.md`
6. `docs/reuse-from-zero.md`
7. `docs/example-prompts.md`
