# Reuse From Zero / 从零复用指南

> 给**完全不懂这个仓库、也不了解你当前项目背景的人**看的第一份说明。  
> 目标不是让她先理解你的历史上下文，而是让她在自己的知识库或共享项目目录里**第一次成功跑通**。

---

## 先一句话说明：这个仓库到底是什么

它不是“现成知识内容模板仓库”，也不是只适配作者本地环境的 Obsidian 配置。

它更像是一套：

> **知识库维护方法 + 多人协同方法 + 可渐进加载的 PM 主线 + 10 个可安装 skills + 配置模板**

所以，别人复用的不是你的 wiki 内容本身，而是你的：
- 知识库维护能力模型
- 多人协同能力模型
- 项目推进与交付审计能力模型

---

## 谁适合复用

适合：
- 已经有 markdown / wiki / Obsidian / Notes 仓库的人
- 希望 AI 帮她维护知识库，但又不想让知识库退化成任务流水账的人
- 想把 2 人及以上项目的问卷、对齐、派单、决策沉淀到共享目录里的人
- 想给项目 owner 增加 milestone / blocker / ready-check 板面的人
- 能接受固定页面角色模型和固定项目目录契约的人

不太适合：
- 只是想找一个现成主题模板的人
- 没有知识库，也没有共享项目目录，只想临时聊几句的人
- 不想使用固定页面角色模型的人
- 不想接受 draft / approved / blocked 这类状态门槛的人

---

## 她第一次会卡住的 7 个地方

如果对方完全不懂你的项目，通常会卡在这里：

1. 她不知道“skill”是什么，也不知道装到哪里  
2. 她不知道 `vault profile` 是什么、该保存成什么文件  
3. 她不知道共享项目目录应该长什么样  
4. 她不知道成员画像应该独立成文件，还是塞在项目目录里  
5. 她不知道要把 profile / 项目目录以什么方式交给 agent  
6. 她不知道 PM 主线是不是所有人一开始都必须配置  
7. 她不知道第一次成功的标准是什么

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

---

## Skill 模式：真正推荐的复用路径

### Step 2：安装 10 个 skill

复制以下目录到她自己的 skills 目录：

- `skills/knowledge-base-kit-guide`
- `skills/knowledge-base-orchestrator`
- `skills/knowledge-base-ingest`
- `skills/knowledge-base-maintenance`
- `skills/knowledge-base-audit`
- `skills/knowledge-base-project-management`
- `skills/knowledge-base-team-coordination`
- `skills/knowledge-base-delivery-audit`
- `skills/knowledge-base-working-profile`
- `skills/work-journal`

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

#### 如果她要启用 PM 主线
只有在她明确需要：
- 项目 owner 视角推进
- 周计划 / milestone / blocker
- handoff / ready / greenlight

时，再复制：
- `templates/project-management/`

> 这一步很重要：`project-management` 是**可选 area**，不是所有用户第一次都必须配置。

### Step 4：推荐协作接入方式

推荐把多人协同理解成三层：
- `team-project/`：共享事实源
- 每个人自己的个人 wiki / 私有资料区：个人工作面
- 每个人自己的 agent（如 OpenClaw / Hermes / 其他 agent）：个人协作助手

推荐同步拓扑有两种：
1. 把 `team-project/` 独立放在 NAS / 网盘同步目录里
2. 把 `team-project/` 嵌入共享 wiki / 共享知识库子目录中

无论用哪种模式，最终进入 coordinator 流程的都必须是**已同步回 shared project directory 的 markdown 文件**。

### Step 5：第一次调用时必须带上绝对路径

不要只说：
> “read my vault profile”

也不要只说：
> “look at my project folder”

应该明确说：

```text
Use $knowledge-base-kit-guide to help me set up this share kit.
My vault profile is at /ABSOLUTE/PATH/TO/vault-profile.md .
My shared project directory is at /ABSOLUTE/PATH/TO/team-project/ .
Read whichever inputs apply, tell me whether my setup is complete, and tell me which skill I should use next.
```

### Step 6：第一次成功的标准

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

#### 成功标准 C：第一次 team coordination kickoff 成功
agent 能够：
- 读取共享项目目录
- 根据 roster 和成员资料生成差异化问卷
- 把 alignment / assignment 当成 draft 而不是直接当成事实
- 明确指出是否需要更多回答或人工确认

#### 成功标准 D：第一次 PM owner 推进成功
agent 能够：
- 读取项目 brief、最近 journal、当前 blocker
- 输出项目摘要、里程碑、风险和个人执行板
- 明确哪些事项应该继续留在 PM 主线，哪些应该转入 team coordination / maintenance / delivery audit

#### 成功标准 E：第一次 orchestrator 初始化成功
agent 能够：
- 检查用户是否已经有可用 vault
- 只在必要时建议安装 Obsidian
- 创建骨架并生成初始 profile
- 明确告诉用户下一步 specialist skill

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
   - `README.md`
   - `docs/team-coordination-workflow.md`
   - `docs/collaboration-integration-patterns.md`

### 如果她要启用 PM 主线
1. `templates/project-management/`
2. `docs/project-management-workflow.md`
3. 相关 prompt 示例

结论很简单：

> 没有 skill 生态，也可以复用这套方法；只是“自动发现 skill”的那层要手动做。
