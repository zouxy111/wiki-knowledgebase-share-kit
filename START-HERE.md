# START HERE

> 这是给“第一次拿到这套分享包的人”看的最短使用说明。  
> 如果你只是想把这套东西发给别人，请直接把整个目录发出去；对方先看这份文件即可。

---

## 你拿到的是什么

这是一个可直接复用的 **wiki / markdown 知识库维护包**，里面有 5 个 skill：

1. `knowledge-base-kit-guide`
   - 负责安装说明、profile 配置说明、技能分流
2. `knowledge-base-ingest`
   - 负责把长 markdown / 书稿 / 教程拆分、链接并导入知识库
3. `knowledge-base-maintenance`
   - 负责把任务结果沉淀进知识库
4. `knowledge-base-working-profile`
   - 负责把持续沟通中的稳定偏好、决策习惯和协作边界沉淀成 working profile
5. `knowledge-base-audit`
   - 负责检查知识库结构、导航、元数据和噪音回流

---

## 最短上手步骤

### 第 1 步：把 5 个 skill 复制到你的 skills 目录
复制这 5 个目录：
- `skills/knowledge-base-kit-guide`
- `skills/knowledge-base-ingest`
- `skills/knowledge-base-maintenance`
- `skills/knowledge-base-working-profile`
- `skills/knowledge-base-audit`

常见目标目录：
- `~/.codex/skills`
- `~/.claude/skills`
- 其他支持 `SKILL.md` 目录结构的平台

### 第 2 步：填写你的 vault profile
复制：
- `templates/vault-profile-template.md`

填写你自己的：
- vault 路径
- `pages/` 目录
- `index.md`
- `log.md`
- root pages
- area 列表
- frontmatter 规则
- 哪些 markdown 文件允许留在 vault 根目录

### 第 3 步：第一次上手先用 guide skill
直接对 agent 说：

```text
Use $knowledge-base-kit-guide to help me set up this knowledge-base share kit.
I want to configure my vault profile and understand which skill to use first.
```

### 第 4 步：开始日常使用
- 要导入长文档/书籍：用 `knowledge-base-ingest`
- 要写入知识库：用 `knowledge-base-maintenance`
- 要沉淀 working profile：用 `knowledge-base-working-profile`
- 要检查结构健康：用 `knowledge-base-audit`

---

## 中文直接可用口令

### 安装 / 上手说明
```text
用 $knowledge-base-kit-guide 帮我开始配置这套知识库维护包，先告诉我应该填哪些 profile 信息，以及我现在下一步该做什么。
```

### 回写维护
```text
用 $knowledge-base-maintenance 把这次任务结果沉淀进我的知识库。
先读取 vault profile，再按 project / knowledge / ops / task / overview 角色模型归类，过滤过程噪音，并同步目标页、root page、reader entry 和 milestone log。
```

### 结构审计
```text
用 $knowledge-base-audit 审计我的知识库。
先读取 vault profile，再检查 metadata、死链、孤立页、root page coverage、page-boundary drift、noise regression，以及根目录 stray markdown files。
```

---

## 如果对方完全不懂这套东西

就让对方按这个顺序读：
1. `START-HERE.md`
2. `README.md`
3. `docs/customization-guide.md`
4. `templates/vault-profile-template.md`
5. 再开始用 `knowledge-base-kit-guide`

---

## 这套方法最重要的固定原则

- 知识库优先，不把一次性任务过程直接写进主叙事
- 页面角色固定为：`project / knowledge / ops / task / overview`
- 根页只做导航和稳定总览
- `ops` 页默认写成：现象 / 根因 / 处理法 / 边界
- `log.md` 只写里程碑，不写任务回放

---

## 一句话理解

> 这是一个把“知识库维护”和“知识库审计”拆开，并且要求先配 profile、再稳定使用的通用分享包。


---

## 如果你要直接发布到 GitHub

这个目录已经补齐了基础开源文件：
- `LICENSE`
- `CONTRIBUTING.md`
- `CHANGELOG.md`
- `README.en.md`
- `.gitignore`

也就是说，它不只是“可转发包”，也可以直接作为 GitHub 开源仓库初始化。

### Working profile 沉淀
```text
用 $knowledge-base-working-profile 从我们的持续沟通里更新我的 working profile。
先读取 vault profile，再只保留对未来协作有用的稳定信号，区分 confirmed / repeated / inferred，过滤敏感个人信息，并按 visibility 规则同步到目标画像页。
```
