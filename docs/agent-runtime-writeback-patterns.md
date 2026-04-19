# Agent Runtime Write-back Patterns

> 这份文档专门解释：如果你把这套 share kit 跑在 OpenClaw、Hermes 或其他 agent runtime 上，哪些内容应该写回共享项目目录 / wiki，哪些内容应该先落在 agent 自己的辅助工作区，以及为什么推荐保留一个与 `pages/` 并行的可选目录。

---

## 1. 先给严格结论

**能，OpenClaw 也可以承接这套写回模式。**

但正确做法不是把所有 agent 产物直接塞进 `pages/`，而是把写回目标分成三层：
1. **稳定知识层**：`pages/`
2. **共享协作事实层**：`team-project/` 或其它 shared project directory
3. **agent 辅助工作层**：一个与 `pages/` 并行的可选目录，例如 `agent-workspace/`

这第三层不是新的强制 schema，也不是 coordinator 的事实源；它只是一个**干净的缓冲层**，用来接住 OpenClaw / Hermes 的草稿、蒸馏、中间对照表、批处理产物和 runtime 辅助材料。

---

## 2. 为什么推荐保留一个与 `pages/` 并行的目录

如果没有这个缓冲层，最常见的问题就是：
- 草稿直接混进稳定知识页
- session 过程噪音回流到 wiki
- runtime 特有的中间文件无处安放
- 成员各自用 agent 并行工作时，临时材料和正式事实边界不清

所以更稳妥的做法是：

> **让 `pages/` 继续只负责稳定知识，让一个与 `pages/` 并行的可选目录负责 agent 的工作过程与中间产物。**

这样做的好处：
- 不破坏现有 `pages/` 契约
- 不把 OpenClaw / Hermes 的平台细节硬写进公共模板
- 给草稿 / distill / imports / 对照表一个明确落点
- 更适合多人并行，再按规则提升为正式知识或正式协作事实

---

## 3. 推荐的三层写回模型

### A. `pages/`：稳定知识层
这里放：
- `knowledge` 页面
- `ops` 页面
- `project` 导航页
- `task` 页面
- `overview` 页面
- 经确认后可长期复用的稳定知识

这里**不应该**直接堆：
- session 原始流水
- 大量补问草稿
- 临时对照表
- 未确认的多人协调中间态

### B. `team-project/`：共享协作事实层
这里放：
- `project-brief.md`
- `team-roster.md`
- `members/<id>/questionnaire.md`
- `members/<id>/response.md`
- `members/<id>/assignment.md`
- `coordination/alignment-summary.md`
- `coordination/task-board.md`
- `coordination/decision-register.md`

它的职责是：
- 承接 coordinator workflow
- 保持 draft / approved / superseded / blocked 边界
- 作为多人协作时的唯一事实源

### C. `agent-workspace/`：runtime 辅助工作层（可选但推荐）
这里可以放：
- drafts
- distills
- imports
- intermediate comparison notes
- local helper checklists
- runtime-specific scratch files
- 需要稍后再提升的候选材料

这一层的定位是：
- **帮助 OpenClaw / Hermes 并行工作**
- **隔离过程噪音**
- **为后续 promotion 做准备**

它不是本仓库的公共硬契约；没有它也能跑，只是更容易把过程噪音混回稳定知识层。

---

## 4. 推荐目录示意（可选模式，不是强制模板）

```text
my-vault/
  index.md
  log.md
  pages/
    ... stable knowledge pages ...
  agent-workspace/
    drafts/
    distills/
    imports/
    shared-projects/
    openclaw/
      prompts/
      scratch/
    hermes/
      session-notes/
      promoted-skills/
```

说明：
- `pages/` 继续只放稳定知识页
- `agent-workspace/` 是**可选增强层**，不是强制 schema
- `shared-projects/` 可以只是本地镜像、辅助材料或待同步版本
- 真正进入 coordinator 闭环的，仍应以正式 shared project directory 为准

如果你的团队已经把 `team-project/` 放在 NAS / 网盘同步目录里，那么 `agent-workspace/shared-projects/` 也可以不保留，或只保留本地辅助副本。

---

## 5. OpenClaw 怎么接这个写回模式

OpenClaw 这类 runtime 很适合承接：
- 日常多入口资料收集
- 共享项目目录驱动的 coordinator workflow
- 基于 skills / prompts / workspace 的持续工作流

因此，推荐把它理解成：
- **一个可以驱动 shared project directory 的运行平台**
- **一个可以承接 `agent-workspace/` 的个人工作面**
- **一个可以沉淀可复用 procedural pattern 的 skill 运行面**

更实际地说，OpenClaw 侧通常可以写回三类东西：
1. 写回 shared project directory 中需要正式进入协作闭环的 markdown 文件
2. 写回 `agent-workspace/` 中的草稿、distill、中间产物
3. 把反复出现的稳定操作方法沉淀为更可复用的 prompts / skills / runbook 说明

### 边界
不要把下面这些内容直接当成稳定知识：
- 原始 chat transcript
- 尚未确认的补问草稿
- 平台专有调试痕迹
- 一次性临时判断过程

这些内容更适合先留在 `agent-workspace/`，再决定是否提升进 `pages/` 或 shared project directory。

---

## 6. Hermes 怎么接这个写回模式

Hermes 更适合承接另一类“长期沉淀”：
- 协作相关的稳定记忆
- 可反复复用的 procedural memory
- 经过筛选的 distill
- 长期会继续用到的 skill 化方法

所以 Hermes 更像：
- **长期记忆与技能提升层**
- **重复工作模式的压缩层**
- **更适合做持续自进化的 agent 面**

但即便如此，Hermes 也不应该绕开 shared project directory 的事实边界。
多人协作里，正式事实仍应回到：
- `team-project/`
- `pages/`
- 已批准的 knowledge-base sync 目标

而不是散落在 runtime 自己的内部状态里。

---

## 7. 一个简单可执行的 promotion 规则

推荐按下面的顺序判断：

### 先放进 `agent-workspace/`
适用于：
- 草稿
- 待确认补问
- session distill 初稿
- 中间对照表
- imports / packets / temporary synthesis

### 再放进 shared project directory
适用于：
- 已进入协作闭环的问题、回答、对齐摘要、任务草案、决策草案
- 需要让 coordinator 和所有成员共同读取的项目事实

### 最后提升进 `pages/` 或知识库同步面
适用于：
- 已确认、稳定、跨项目可复用的知识
- 稳定 runbook / ops 结论
- 经过批准的长期决策规则
- working profile 的稳定增量

一句话：

> **先把过程留在 `agent-workspace/`，把协作事实留在 shared project directory，把真正稳定的内容再提升进 `pages/`。**

---

## 8. 这不会改变核心公开契约

这份文档描述的是：
- 一个**推荐接入模式**
- 一个**更稳的运行习惯**
- 一个**与 `pages/` 并行的可选辅助目录**

它**不会**改变本仓库的核心公开契约：
- `pages/` 的角色模型不变
- `team-project/` 的模板契约不变
- `questionnaire / response / assignment / progress-update / decision-distill` 契约不变
- OpenClaw / Hermes 仍然是推荐平台，而不是强依赖平台

---

## 9. 对外最推荐怎么讲

如果你要向陌生用户解释，最稳妥的一句话是：

> 这套 share kit 可以跑在 OpenClaw、Hermes 或其他兼容 runtime 上；推荐把 `pages/` 保持为稳定知识层，再保留一个与 `pages/` 并行的可选 `agent-workspace/` 目录承接草稿、蒸馏和中间产物。这样既能让每个人用自己的 agent 并行工作，也不会破坏 shared project directory 和 wiki 的事实边界。
