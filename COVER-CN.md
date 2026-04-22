# 中文封面说明页

> 这是一个可直接转发的 **10-skill wiki / markdown 知识库维护 + 协作包**。  
> 如果对方第一次拿到仓库，不知道先看哪里，就先看这一页。

---

## 这套包是干什么的

它的目标是把一个容易越写越乱的 markdown / wiki 知识库，收敛成：
- **知识库优先**，而不是任务流水优先
- **页面职责清晰**，而不是所有东西都堆在一起
- **长期可维护**，而不是每次靠临时发挥
- **对协作友好**，而不是每次都重新解释上下文
- **对项目推进有管理层抓手**，而不是只有零散任务和聊天记录

它既能做：
- 长文档导入
- 任务结果沉淀
- 结构审计
- 协作画像沉淀
- 多人项目协调
- 工作记录 / 周报
- 项目 owner 推进
- 交付完整性 / ready / greenlight 审计

也提供两个 onboarding 入口：
- `knowledge-base-kit-guide`：解释和分流
- `knowledge-base-orchestrator`：零门槛初始化入口

---

## 这个包里有什么

### 10 个 skills
1. `knowledge-base-kit-guide` — 使用说明 / 配置分流
2. `knowledge-base-orchestrator` — 零门槛初始化入口
3. `knowledge-base-ingest` — 长文档导入
4. `knowledge-base-maintenance` — 任务结果沉淀
5. `knowledge-base-audit` — 结构审计
6. `knowledge-base-project-management` — 项目 intake / milestone / blocker / owner 执行板
7. `knowledge-base-team-coordination` — 多人项目协调
8. `knowledge-base-delivery-audit` — 交付完整性 / ready / greenlight 审计
9. `knowledge-base-working-profile` — 协作画像沉淀
10. `work-journal` — 工作记录 / 周报沉淀

### 常用模板
- `templates/vault-profile-template.md`
- `templates/working-profile-page-template.md`
- `templates/journal-profile-template.md`
- `templates/member-capability-profile-template.md`
- `templates/project-management/`

### 核心说明文档
- `README.md`
- `START-HERE.md`
- `GLOSSARY.md`
- `docs/usage-sop.md`
- `docs/example-prompts.md`
- `docs/project-management-workflow.md`

---

## 对方收到后应该怎么开始

### 最快上手
1. 看 `START-HERE.md`
2. 复制 `templates/vault-profile-template.md`
3. 把 10 个 skill 复制到自己的 `skills/` 目录
4. 完全新手先用 `knowledge-base-orchestrator`
5. 想先理解结构的人先用 `knowledge-base-kit-guide`

### 如果对方只想知道“我该用哪个 skill”
- 初始化 / 检查环境：`knowledge-base-orchestrator`
- 解释安装 / profile / 分流：`knowledge-base-kit-guide`
- 导入一本书：`knowledge-base-ingest`
- 写回知识：`knowledge-base-maintenance`
- 做结构体检：`knowledge-base-audit`
- 项目 owner 推进：`knowledge-base-project-management`
- 多人项目协调：`knowledge-base-team-coordination`
- 交付闭环审计：`knowledge-base-delivery-audit`
- 沉淀协作画像：`knowledge-base-working-profile`
- 记录工作 / 周报：`work-journal`

---

## PM 主线怎么理解

这个仓库现在有一条**可渐进加载**的 PM 主线：
- `knowledge-base-project-management`
- `knowledge-base-team-coordination`
- `knowledge-base-delivery-audit`

但默认 onboarding 仍然先讲知识库维护主线。  
只有当对方明确提到：
- 项目管理
- 周计划
- 里程碑
- blocker
- handoff
- ready / greenlight

才建议她复制：
- `templates/project-management/`

也就是说：
> 这是核心包扩容，不是强迫所有用户一上来就做 PM 配置。

---

## 协作接入怎么讲最稳

当前主推平台：
- **OpenClaw**
- **Hermes**

推荐协作模式：
- `team-project/` 作为共享事实源
- 可以放在 NAS / 网盘同步目录里
- 也可以嵌入共享 wiki / 共享知识库子目录
- 每位成员都可以在自己的个人 wiki / 私有资料区里整理草稿
- 每位成员都可以用自己的 OpenClaw / Hermes / 其他 agent 协助填写问卷和更新进展
- 但只有**同步回 shared project directory 的 markdown 文件**才进入正式协调闭环

---

## 这套方法最重要的固定原则

- 页面角色固定为：`project / knowledge / ops / task / overview`
- 根页只做导航和稳定总览
- `ops` 页默认写成：**现象 / 根因 / 处理法 / 边界**
- `log.md` 只写里程碑，不写任务回放
- 默认不把一次性过程噪音直接写进知识库
- PM 主线里要显式区分 `draft / approved / blocked / superseded`

也就是说：
> 它不是帮你多记日志，而是帮你把知识库、协作和项目推进都写得更像可复用系统。

---

## 转发给别人时可以直接附这句话

```text
这是一个可复用的 10-skill wiki/markdown 知识库维护 + 协作包。
先看 START-HERE.md，再复制 10 个 skills，填 vault-profile-template.md。
默认先走知识库维护主线；如果你需要项目管理 / 周计划 / 里程碑 / 多人协同 / ready 审计，再启用 project-management 主线。
```
