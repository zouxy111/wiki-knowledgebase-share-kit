# 中文封面说明页

> 这是一个可直接转发的 **8-skill wiki / markdown 知识库维护包**。  
> 如果对方第一次拿到仓库，不知道先看哪里，就先看这一页。

---

## 这套包是干什么的

它的目标是把一个容易越写越乱的 markdown / wiki 知识库，收敛成：
- **知识库优先**，而不是任务流水优先
- **页面职责清晰**，而不是所有东西都堆在一起
- **长期可维护**，而不是每次靠临时发挥
- **对协作友好**，而不是每次都重新解释上下文

它既能做：
- 长文档导入
- 任务结果沉淀
- 结构审计
- 协作画像沉淀
- 多人项目协调
- 工作记录 / 周报

也提供两个 onboarding 入口：
- `knowledge-base-kit-guide`：解释和分流
- `knowledge-base-orchestrator`：零门槛初始化入口

---

## 这个包里有什么

### 8 个 skills
1. `knowledge-base-kit-guide` — 使用说明 / 配置分流
2. `knowledge-base-ingest` — 长文档导入
3. `knowledge-base-maintenance` — 任务结果沉淀
4. `knowledge-base-audit` — 结构审计
5. `knowledge-base-orchestrator` — 零门槛初始化入口
6. `knowledge-base-team-coordination` — 多人项目协调
7. `knowledge-base-working-profile` — 协作画像沉淀
8. `work-journal` — 工作记录 / 周报沉淀

### 常用模板
- `templates/vault-profile-template.md`
- `templates/working-profile-page-template.md`
- `templates/journal-profile-template.md`
- `templates/member-capability-profile-template.md`

### 核心说明文档
- `README.md`
- `START-HERE.md`
- `GLOSSARY.md`
- `docs/usage-sop.md`
- `docs/example-prompts.md`

---

## 对方收到后应该怎么开始

### 最快上手
1. 看 `START-HERE.md`
2. 复制 `templates/vault-profile-template.md`
3. 把 8 个 skill 复制到自己的 `skills/` 目录
4. 完全新手先用 `knowledge-base-orchestrator`
5. 想先理解结构的人先用 `knowledge-base-kit-guide`

### 如果对方只想知道“我该用哪个 skill”
- 初始化 / 检查环境：`knowledge-base-orchestrator`
- 解释安装 / profile / 分流：`knowledge-base-kit-guide`
- 导入一本书：`knowledge-base-ingest`
- 写回知识：`knowledge-base-maintenance`
- 做结构体检：`knowledge-base-audit`
- 沉淀协作画像：`knowledge-base-working-profile`
- 多人项目协调：`knowledge-base-team-coordination`
- 记录工作 / 周报：`work-journal`

---

## 这套方法最重要的固定原则

- 页面角色固定为：`project / knowledge / ops / task / overview`
- 根页只做导航和稳定总览
- `ops` 页默认写成：**现象 / 根因 / 处理法 / 边界**
- `log.md` 只写里程碑，不写任务回放
- 默认不把一次性过程噪音直接写进知识库

也就是说：
> 它不是帮你多记日志，而是帮你把知识库写得更像知识库。

---

## 转发给别人时可以直接附这句话

```text
这是一个可复用的 8-skill wiki/markdown 知识库维护包。
先看 START-HERE.md，再复制 8 个 skills，填 vault-profile-template.md。
完全新手先用 knowledge-base-orchestrator；想先理解结构就先用 knowledge-base-kit-guide。
```
