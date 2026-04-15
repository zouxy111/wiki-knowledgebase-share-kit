# 中文封面说明页

> 这是一套可以直接复用的 **wiki / markdown 知识库维护包**。  
> 如果你收到这个包，但还不知道里面是什么、该先看哪里、该怎么开始，就先看这一页。

---

## 这套包是干什么的

它的目标是把一个容易越写越乱的 markdown / wiki 知识库，收敛成：
- **知识库优先**，而不是任务流水优先
- **页面职责清晰**，而不是所有东西都堆在一起
- **可持续维护**，而不是每次靠临时发挥

它特别适合这些场景：
- 你有自己的 Obsidian / markdown wiki
- 你想把任务结果沉淀成长期可检索的知识
- 你想定期检查知识库有没有死链、孤立页、导航漂移、噪音回流
- 你不想让 wiki 退化成项目日志集合

---

## 这个包里有什么

### 3 个 skills
1. `knowledge-base-kit-guide`
   - 安装说明 / 配置说明 / 技能分流
2. `knowledge-base-maintenance`
   - 把任务结果沉淀进知识库
3. `knowledge-base-audit`
   - 审计知识库结构、导航、元数据和噪音回流

### 1 个配置模板
- `templates/vault-profile-template.md`

### 1 套说明文档
- `README.md`
- `START-HERE.md`
- `docs/customization-guide.md`
- `docs/usage-sop.md`
- `docs/example-prompts.md`

### 1 套示例
- `examples/example-vault-profile.md`
- `examples/case-study-current-vault.md`

---

## 你收到后应该怎么开始

### 如果你想最快上手
按这个顺序：
1. 看 `START-HERE.md`
2. 复制 `templates/vault-profile-template.md`
3. 填你的 vault 路径、areas、root pages、frontmatter 规则
4. 把 3 个 skills 复制到你的 skills 目录
5. 第一次先用 `knowledge-base-kit-guide`

### 如果你想先了解方法论
按这个顺序：
1. 看 `README.md`
2. 看 `docs/customization-guide.md`
3. 看 `docs/usage-sop.md`
4. 再看示例文件

---

## 这套方法最重要的固定原则

这套包不是“万能 wiki 包”，它有明确的方法论边界：

- 页面角色固定为：`project / knowledge / ops / task / overview`
- 根页只做导航和稳定总览
- `ops` 页默认写成：**现象 / 根因 / 处理法 / 边界**
- `log.md` 只写里程碑，不写任务回放
- 默认不把一次性过程噪音直接写进知识库

也就是说：
> 它不是帮你多记日志，而是帮你把知识库写得更像知识库。

---

## 这套包最适合谁

适合：
- 自己长期维护 markdown/wiki 知识库的人
- 想把知识沉淀和任务过程分开的个人或团队
- 已经在用支持 `SKILL.md` 结构的平台的人
- 想把“维护”和“审计”拆成两条明确工作流的人

不太适合：
- 完全不想配置 profile 的人
- 不接受固定页面角色模型的人
- 只想记录原始过程、不关心知识沉淀的人

---

## 你可以直接怎么用

### 第一次上手可以直接对 agent 说

```text
用 $knowledge-base-kit-guide 帮我开始用这套知识库维护包。
我还没有配 vault profile，请先告诉我最少要补哪些信息，再告诉我下一步应该调用哪个 skill。
```

### 想写入知识库时可以说

```text
用 $knowledge-base-maintenance 把这次结果沉淀进我的知识库。
先读 vault profile，再过滤过程噪音，按页面角色归类，并同步目标页、root page、reader entry 和 milestone log。
```

### 想做结构体检时可以说

```text
用 $knowledge-base-audit 审计我的知识库。
先读 vault profile，再检查死链、孤立页、metadata、页面边界漂移、噪音回流，以及根目录 stray markdown 文件。
```

---

## 如果你是转发给别人

你可以直接附这句话：

```text
这是一个可复用的 wiki/markdown 知识库维护包。
先看《中文封面说明页.md》或 START-HERE.md，再复制 3 个 skills，填 vault-profile-template.md，然后先用 knowledge-base-kit-guide 上手。
```

---

## 一句话总结

> 这是一个把“知识库维护”和“知识库审计”拆开，并要求先配 profile、再稳定使用的通用分享包。
