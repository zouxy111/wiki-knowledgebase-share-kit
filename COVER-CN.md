# 中文封面说明页

> 这是一套可以直接复用的 **wiki / markdown 知识库导入 + 维护 + 审计 + 多人协同协调包**。  
> 如果你收到这个包，但还不知道里面是什么、该先看哪里、该怎么开始，就先看这一页。

---

## 这套包是干什么的

它现在同时解决三类问题：

### A. 长文档导入
把书稿、教程、规范这类长篇 Markdown，收敛成：
- **overview / chapter / topic** 的可导航结构
- **先落 baseline，再比较 candidate，再决定是否 promote** 的迭代回路
- **术语候选、related links、source lineage** 都可持续维护

### B. 知识库维护
把一个容易越写越乱的 markdown / wiki 知识库，收敛成：
- **知识库优先**，而不是任务流水优先
- **页面职责清晰**，而不是所有东西都堆在一起
- **可持续维护**，而不是每次靠临时发挥

### C. 多人协同协调
把一个 2 人及以上项目，收敛成：
- **共享项目目录为唯一事实源**
- **按成员能力生成差异化问卷**
- **先对齐，再派单，再跟进，再蒸馏**
- **稳定决策和成员画像可以复用，必要时可同步回知识库**

---

## 这个包里有什么

### 5 个 skills
1. `knowledge-base-kit-guide`
   - 安装说明 / 配置说明 / 技能分流
2. `knowledge-base-ingest`
   - 把长 markdown / 书稿 / 教程拆分、链接并导入知识库，并通过 rubric 决定 candidate 是否晋升
3. `knowledge-base-maintenance`
   - 把任务结果沉淀进知识库
4. `knowledge-base-audit`
   - 审计知识库结构、导航、元数据和噪音回流
5. `knowledge-base-team-coordination`
   - 多人项目 intake、问卷派发、目标对齐、任务分配、跟进重排、决策蒸馏，以及可选知识库同步

### 模板
- `templates/vault-profile-template.md`
- `templates/ingest-iteration-log-template.md`
- `templates/team-project-workspace/`
- `templates/member-capability-profile-template.md`

### 说明文档
- `README.md`
- `START-HERE.md`
- `GLOSSARY.md`
- `docs/ingest-evaluation-rubric.md`
- `docs/collaboration-integration-patterns.md`
- `docs/team-coordination-workflow.md`
- `docs/customization-guide.md`
- `docs/usage-sop.md`
- `docs/example-prompts.md`

### 示例
- `examples/example-vault-profile-generic.md`
- `examples/case-study-current-vault.md`
- `examples/case-study-pathology-ingest-iteration.md`
- `examples/team-project-generic/`
- `examples/team-project-qc/`

---

## 主推接入平台与推荐协作模式

### 主推平台
本仓库主推：
- **OpenClaw**
- **Hermes**

这里说的“主推”，不是因为 repo 依赖它们的私有 API，而是因为它们很适合承接：
- shared project directory 工作流
- skills / prompts 驱动的协作流程
- 每位成员用自己的 agent 协助整理问卷、回应和进展

### 推荐协作模式
推荐这样理解多人协同：
- **共享项目目录**：团队事实源
- **每个人自己的 wiki / 私有资料区**：个人工作面
- **每个人自己的 OpenClaw / Hermes / 其他 agent**：个人协作助手
- **可选知识库同步**：只同步稳定、已批准的内容

### 两种推荐同步拓扑
- **模式 1：team-project 独立放在 NAS / 网盘同步目录**
- **模式 2：team-project 直接嵌进共享 wiki / 共享知识库子目录**

无论选哪种拓扑，底线都一样：
- shared project directory 才是 coordinator 的唯一事实源
- 个人 wiki / 个人 agent 只是辅助工作面

---

## 你收到后应该怎么开始

### 如果你想最快上手
按这个顺序：
1. 看 `START-HERE.md`
2. 看 `README.md`
3. 如果是知识库场景，复制 `templates/vault-profile-template.md`
4. 如果是 ingest 场景，再看 `docs/ingest-evaluation-rubric.md`
5. 如果是多人协同场景，复制 `templates/team-project-workspace/`
6. 把 5 个 skills 复制到你的 skills 目录
7. 第一次先用 `knowledge-base-kit-guide`

### 如果你想先了解协作模式
按这个顺序：
1. 看 `README.md`
2. 看 `docs/collaboration-integration-patterns.md`
3. 看 `docs/team-coordination-workflow.md`
4. 看 `docs/usage-sop.md`
5. 再看示例文件

---

## 这套方法最重要的固定原则

- 页面角色固定为：`project / knowledge / ops / task / overview`
- 根页只做导航和稳定总览
- `ops` 页默认写成：**现象 / 根因 / 处理法 / 边界**
- `log.md` 只写里程碑，不写任务回放
- ingest 默认遵循：**先 baseline，再 candidate，再 regression，再 promote**
- 多人协同默认由**单协调 AI**驱动
- `team-project/` 是多人协同的唯一事实源
- 问卷、alignment、assignment、decision 都先 draft，后 approved
- 个人 wiki / 个人 agent 是推荐工作模式，但不是团队事实源

---

## 一句转发文案

```text
这是一个可复用的 wiki/markdown 知识库导入 + 维护 + 审计 + 多人协同分享包。
先看 START-HERE.md，再复制 5 个 skills。
如果你是知识库场景，先填 vault-profile-template.md；
如果你是多人协同场景，先复制 team-project-workspace 模板。
这套协作模式主推在 OpenClaw / Hermes 上运行，也适合把共享项目目录放到 NAS、网盘或共享 wiki 下同步。
```
