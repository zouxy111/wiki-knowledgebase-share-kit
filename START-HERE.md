# START HERE

> 这是给“第一次拿到这套分享包的人”看的最短使用说明。  
> 如果你只是想把整个目录发给别人，请让对方先看这份文件。

---

## 你拿到的是什么

这是一个可直接复用的 **wiki / markdown 知识库导入 + 维护 + 审计 + 多人协同协调包**，里面有 **5 个 skill**：

1. `knowledge-base-kit-guide`
   - 安装说明、profile 配置说明、技能分流
2. `knowledge-base-ingest`
   - 把长 markdown / 书稿 / 教程拆分、链接并导入知识库；先落 baseline，再比较 candidate，再决定是否晋升
3. `knowledge-base-maintenance`
   - 把任务结果沉淀进知识库
4. `knowledge-base-audit`
   - 检查知识库结构、导航、元数据和噪音回流
5. `knowledge-base-team-coordination`
   - 负责 2 人及以上项目的 intake、角色化问卷、目标对齐、任务派发、跟进重排、决策蒸馏，以及可选知识库同步

---

## 先判断你要走哪条路

### A. 你要导入长文档 / 书籍 / 教程进知识库
你需要：
- `templates/vault-profile-template.md`
- `templates/ingest-iteration-log-template.md`
- `knowledge-base-kit-guide`
- `knowledge-base-ingest`
- `docs/ingest-evaluation-rubric.md`

### B. 你要维护一个 markdown/wiki 知识库
你需要：
- `templates/vault-profile-template.md`
- `knowledge-base-kit-guide`
- `knowledge-base-maintenance`
- `knowledge-base-audit`

### C. 你要跑一个 2 人及以上的共享项目目录协同
你需要：
- `templates/team-project-workspace/`
- `templates/member-capability-profile-template.md`（如需复用成员画像）
- `knowledge-base-kit-guide` 或 `knowledge-base-team-coordination`
- 推荐运行平台：**OpenClaw / Hermes**

### D. 你要同时做多人协同 + 知识库沉淀
你需要：
- 上面两套都准备
- 但仍只使用**一套知识库治理模型**：沿用现有 `project / knowledge / ops / task / overview`

---

## 第 1 步：把 5 个 skill 复制到你的 skills 目录
复制这 5 个目录：
- `skills/knowledge-base-kit-guide`
- `skills/knowledge-base-ingest`
- `skills/knowledge-base-maintenance`
- `skills/knowledge-base-audit`
- `skills/knowledge-base-team-coordination`

如果你**不确定平台是否支持 skill**，先不要硬装。请先读：
- `README.md`
- `docs/reuse-from-zero.md`

如果平台不支持 skill，也仍然可以手工复用这套方法。

---

## 第 2 步：准备你的输入模板

### 如果你是知识库 / ingest 场景
复制：
- `templates/vault-profile-template.md`

建议保存成一个稳定、明确、能被 agent 读取的文件，例如：
- `<vault-root>/vault-profile.md`
- 或 `<workspace-root>/my-vault-profile.md`

### 如果你是多人协同场景
复制：
- `templates/team-project-workspace/`

然后至少补这几个内容：
- `project-brief.md`
- `team-roster.md`
- `members/<member-id>/member-context.md`
- `shared-materials/`

如果你已经有长期成员画像，再额外复制：
- `templates/member-capability-profile-template.md`

把每位成员的画像保存到稳定路径，并在 `team-roster.md` 里填写 `canonical profile path`。

---

## 第 3 步：记住两条底线

### 知识库底线
- 页面角色固定为：`project / knowledge / ops / task / overview`
- 根页只做导航和稳定总览
- `ops` 页默认写成：**现象 / 根因 / 处理法 / 边界**
- `log.md` 只写 milestone，不写任务回放

### 协作底线
- 多人协同默认由**单协调 AI**驱动
- `team-project/` 是多人协同的唯一事实源
- 问卷、alignment、assignment、decision 都先 `draft`，后 `approved`
- 个人 wiki / 个人 agent 是推荐工作模式，但不是团队事实源

---

## 第 4 步：第一次调用时要怎么说

### 4A. 第一次装完，但不知道该先做什么
```text
Use $knowledge-base-kit-guide.
Read this repository and help me choose the right path: ingest, maintenance, audit, or team coordination.
I will provide either a vault profile path or a shared project directory path.
```

### 4B. 要导入一本 markdown 书 / 长文档
```text
Use $knowledge-base-ingest.
Read my vault profile first.
Treat the first import as a stable baseline, create a candidate structure only for the current iteration goal, and use the ingest rubric before promoting changes.
```

### 4C. 要维护知识库
```text
Use $knowledge-base-maintenance.
Read my vault profile first and write only durable knowledge back into the vault.
```

### 4D. 要做结构审计
```text
Use $knowledge-base-audit.
Read my vault profile first and inspect metadata, navigation, dead links, orphan pages, boundary drift, and noise regression.
```

### 4E. 要跑多人协同
```text
Use $knowledge-base-team-coordination.
Read the shared project directory first.
If canonical member profiles exist, use them before drafting questionnaires.
Members may prepare drafts in their own wiki with OpenClaw, Hermes, or another agent, but only markdown synced back into the shared project directory is formal input.
```

---

## 第 5 步：推荐阅读顺序

### 如果你是知识库 / ingest 场景
1. `README.md`
2. `docs/customization-guide.md`
3. `templates/vault-profile-template.md`
4. `docs/usage-sop.md`
5. `docs/ingest-evaluation-rubric.md`
6. `templates/ingest-iteration-log-template.md`

### 如果你是多人协同场景
1. `README.md`
2. `docs/collaboration-integration-patterns.md`
3. `docs/team-coordination-workflow.md`
4. `templates/team-project-workspace/README.md`
5. `docs/usage-sop.md`

### 如果你想先看例子
- `examples/example-vault-profile-generic.md`
- `examples/case-study-pathology-ingest-iteration.md`
- `examples/team-project-generic/README.md`
- `examples/team-project-qc/README.md`

---

## 第 6 步：第一次使用最常见的坑

### 坑 1：没有给绝对路径
第一次调用时，最好显式给：
- vault profile 的**绝对路径**
- 或 shared project directory 的**绝对路径**

### 坑 2：把 team-project 当成个人草稿区
不是。个人 wiki / 个人 agent 可以并行工作，但正式输入必须同步回共享项目目录。

### 坑 3：把 ingest 当成一次性动作
不是。长文档导入默认是：
- 先落 baseline
- 再做 candidate
- 再跑 regression
- 最后再决定是否 promote

---

## 你只记住一句话也行

- **知识库场景**：先配 profile，再用 guide 分流，再跑 ingest / maintenance / audit
- **多人协同场景**：先建 `team-project/`，再用 coordinator 做问卷、对齐、派单和蒸馏
