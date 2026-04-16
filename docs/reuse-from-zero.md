# Reuse From Zero / 从零复用指南

> 给**完全不懂这个仓库、也不了解你当前项目背景的人**看的第一份说明。
> 目标不是让她先理解你的历史上下文，而是让她在自己的知识库或共享项目目录里**第一次成功跑通**。

---

## 先一句话说明：这个仓库到底是什么

这不是一个“现成知识库内容模板仓库”，也不是一个只适用于你当前项目的 Obsidian 配置。

它更像是一套 **“知识库维护方法 + 多人协同方法 + 可安装 skills + 配置模板”**：

- 你保留固定的方法论：
  - knowledge-base-first
  - 固定页面角色：`project / knowledge / ops / task / overview`
  - 根页只做导航和稳定总览
  - `ops` 页默认写成：现象 / 根因 / 处理法 / 边界
  - `log.md` 只记里程碑
  - 多人协同默认由单协调 AI 驱动
  - 共享项目目录是唯一事实源
- 别人替换她自己的：
  - vault 路径
  - area 列表
  - root pages
  - frontmatter 规则
  - 项目目录路径
  - 成员画像路径
  - 是否同步知识库

所以，**别人复用的不是你的 wiki 内容本身，而是你的“知识库维护能力模型 + 多人协同能力模型”。**

---

## 谁适合复用

适合：
- 已经有 markdown / wiki / Obsidian / Notes 仓库的人
- 希望 AI 帮她维护知识库，但又不想让知识库退化成任务流水账的人
- 想把 2 人及以上项目的问卷、对齐、派单、决策沉淀到共享目录里的人
- 能接受固定页面角色模型和固定项目目录契约的人

不太适合：
- 只是想找一个现成主题模板的人
- 没有知识库，也没有共享项目目录，只想临时聊几句的人
- 不想使用固定页面角色模型的人
- 不想接受 draft / approved 状态门槛的人

---

## 她第一次会卡住的 6 个地方

如果对方完全不懂你的项目，通常会卡在这里：

1. **她不知道“skill”是什么，也不知道装到哪里。**
2. **她不知道 `vault profile` 是什么、该保存成什么文件。**
3. **她不知道共享项目目录应该长什么样。**
4. **她不知道成员画像应该独立成文件，还是塞在项目目录里。**
5. **她不知道要把 profile / 项目目录以什么方式交给 agent。**
6. **她不知道第一次成功的标准是什么。**

本仓库真正要解决的，就是这 6 个问题。

---

## 最短复用路径：先让她第一次成功

### Step 1：确认她有什么环境

先分成两类：

#### A. 她的 AI 平台支持 `SKILL.md`
例如：
- Codex
- OpenClaw
- Hermes
- Claude Code / Claude Desktop（若支持本地 skills）
- 其他支持 skill 目录结构的平台

其中，本仓库当前主推：
- **OpenClaw**
- **Hermes**

→ 走 **Skill 模式**

#### B. 她的平台不支持 `SKILL.md`
但能：
- 读取本地 markdown 文件
- 执行你给的 prompt

→ 走 **Manual 模式**

> 这一步非常重要。
> 对完全陌生的人，不应该默认她已经懂 skill 生态。

---

## Skill 模式：真正推荐的复用路径

### Step 2：先安装 4 个 skill

复制以下目录到她自己的 skills 目录：

- `skills/knowledge-base-kit-guide`
- `skills/knowledge-base-maintenance`
- `skills/knowledge-base-audit`
- `skills/knowledge-base-team-coordination`

常见位置示例：
- `~/.codex/skills`
- `~/.claude/skills`

如果她不确定平台支不支持 skills，先不要跳到后面的 prompt；先确认这一点。

### Step 3：根据任务准备输入模板

#### 如果她要维护知识库
复制：
- `templates/vault-profile-template.md`

建议直接保存成一个**明确、稳定、可引用的绝对路径文件**，例如：
- `<vault-root>/vault-profile.md`
- 或 `<workspace-root>/my-vault-profile.md`

#### 如果她要跑多人协同
复制：
- `templates/team-project-workspace/`

至少填：
- `project-brief.md`
- `team-roster.md`
- `members/<member-id>/member-context.md`

如果她有长期成员画像，再复制：
- `templates/member-capability-profile-template.md`

并把画像文件保存成稳定路径，在 `team-roster.md` 里引用。

### 推荐协作接入方式
推荐把多人协同理解成三层：
- `team-project/`：共享事实源
- 每个人自己的个人 wiki / 私有资料区：个人工作面
- 每个人自己的 agent（如 OpenClaw / Hermes / 其他 agent）：个人协作助手

推荐同步拓扑有两种：
1. 把 `team-project/` 独立放在 NAS / 网盘同步目录里
2. 把 `team-project/` 嵌入共享 wiki / 共享知识库子目录中

无论用哪种模式，最终进入 coordinator 流程的都必须是**已同步回 shared project directory 的 markdown 文件**。

### Step 4：第一次调用时必须带上绝对路径

不要只说：
> “read my vault profile”

也不要只说：
> “look at my project folder”

因为对陌生用户来说，agent 并不知道这些文件或目录在哪里。

应该明确说：

```text
Use $knowledge-base-kit-guide to help me set up this share kit.
My vault profile is at /ABSOLUTE/PATH/TO/vault-profile.md .
My shared project directory is at /ABSOLUTE/PATH/TO/team-project/ .
Read whichever inputs apply, tell me whether my setup is complete, and tell me which skill I should use next.
```

### Step 5：第一次成功的标准

第一次成功，不是“她完全理解了整个仓库”。

而是以下任意一个能跑通：

#### 成功标准 A：第一次 maintenance 成功
agent 能够：
- 读取 profile
- 正确判断页面角色
- 更新目标页
- 同步 root page
- 同步 `index.md`
- 同步 `log.md`

#### 成功标准 B：第一次 audit 成功
agent 能够：
- 读取 profile
- 扫描 frontmatter / links / entrypoints
- 输出 P1 / P2 / P3 findings
- 指出是否存在 root-level stray markdown files

#### 成功标准 C：第一次 team coordination Kickoff 成功
agent 能够：
- 读取共享项目目录
- 根据 roster 和成员资料生成差异化问卷
- 把 alignment / assignment 当成 draft 而不是直接当成事实
- 明确指出是否需要更多回答或人工确认

只要第一次成功达到其中一个，她就已经“复用”了你的项目核心能力。

---

## Manual 模式：对没有 skills 生态的人怎么复用

即使她的平台不支持 `SKILL.md`，也仍然可以复用这套方法。

她需要把下面几类东西一起交给 agent：

### 如果她要维护知识库
1. `templates/vault-profile-template.md` 或她已经填好的 profile
2. 相关说明文档，例如：
   - `README.md`
   - `docs/customization-guide.md`
   - `docs/usage-sop.md`
3. 她自己的 vault 文件

### 如果她要跑多人协同
1. `templates/team-project-workspace/` 或她已经填好的项目目录
2. `templates/member-capability-profile-template.md` 或她已有的成员画像
3. 相关说明文档，例如：
   - `docs/team-coordination-workflow.md`
   - `docs/example-prompts.md`
4. 她自己的共享项目目录

然后直接用类似这样的 prompt：

```text
I want you to coordinate a shared project using the method in this repository.
First read these files and folders:
- /ABSOLUTE/PATH/TO/team-project/
- /ABSOLUTE/PATH/TO/docs/team-coordination-workflow.md
- /ABSOLUTE/PATH/TO/docs/example-prompts.md
- /ABSOLUTE/PATH/TO/templates/member-capability-profile-template.md

Then treat the shared project directory as the only source of truth,
use draft/approved gating, generate role-aware questionnaires,
and assume that each member may prepare drafts in their own wiki with OpenClaw, Hermes, or another local agent before syncing the final markdown back into the shared project directory.
Tell me whether you are at kickoff, alignment, assignment, follow-up, or closeout.
```

也就是说：

> **skill 只是更方便的包装。真正可复用的核心，是 profile / 项目目录模板 + 方法文档 + prompt 约束。**

---

## 你应该给陌生用户看的文件顺序

如果对方完全不懂你的项目，建议强制按这个顺序读：

1. `README.md`
2. `START-HERE.md`
3. `docs/reuse-from-zero.md`
4. `docs/collaboration-integration-patterns.md`
5. `docs/team-coordination-workflow.md`
6. `docs/customization-guide.md`
7. `templates/vault-profile-template.md`
7. `templates/member-capability-profile-template.md`
8. `templates/team-project-workspace/README.md`
9. `docs/example-prompts.md`

这个顺序的意义是：
- 先知道项目是什么
- 再知道第一步做什么
- 再知道如何从零复用
- 再进入知识库配置和多人协同配置

---

## 对开源仓库来说，最关键的外部视角问题

从陌生人的角度，这个仓库最重要的问题不是“方法论对不对”，而是：

### 1. 她能不能在 10 分钟内知道自己该做什么
如果不能，README 再完整也没用。

### 2. 她能不能在第一次调用里就把 profile 或项目目录正确交给 agent
如果不能，skills 会显得“像不能用”。

### 3. 她能不能不用理解你的历史项目，也能在自己的 vault 或项目里落地
如果不能，这个仓库就还在“你的项目衍生物”阶段，而不是“可复用开源能力”。

### 4. 她能不能看到通用示例和 QC 示例的区别
如果不能，她会误以为这个项目只能服务你的 QC 场景。

---

## 推荐你对外强调的仓库定位

对外不要优先说：
- 这是我的 Obsdain 经验抽象
- 这是我自己的 wiki 治理方式
- 这是我的 QC 项目衍生物

而应该优先说：

> A reusable kit for keeping markdown knowledge bases structured and knowledge-base-first, while also coordinating multi-person shared-project workflows through role-aware questionnaires, alignment, assignment, and decision distillation.

这样陌生用户更容易理解：
- 这是什么
- 适用于谁
- 她拿到后第一步做什么
- 为什么它可以无缝接入 OpenClaw / Hermes，并通过共享目录让多人并行工作
