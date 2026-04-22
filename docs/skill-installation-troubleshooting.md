# Skill Installation Troubleshooting

> 这份文档专门处理这类问题：  
> `Skill "knowledge-base-ingest" not found`
>
> 最常见原因不是仓库里没有这个 skill，  
> 而是**当前运行的 agent 没有从它真正扫描的 skills 目录里加载到它**。

---

## 1. 先分清两件事

### A. 仓库里有没有这个 skill
例如：
- `skills/knowledge-base-ingest/`
- `skills/knowledge-base-project-management/`
- `skills/knowledge-base-delivery-audit/`
- `skills/work-journal/`

这说明 **repo 自身是否包含该 skill bundle**。

### B. 运行时有没有加载这个 skill
例如运行平台真正扫描的目录可能是：
- `~/.codex/skills/`
- `~/.claude/skills/`
- 或某个平台自己的 custom skills directory

报错 `Skill not found` 时，真正关键的是 **B**，不是 **A**。

---

## 2. 最快修法：用安装脚本把整套 skills 同步到运行时目录

推荐优先使用仓库自带脚本，而不是手工一条条 `cp -r`。

### 安装到 Codex

```bash
python3 scripts/install_skills.py --platform codex --force
```

### 安装到 Claude Code

```bash
python3 scripts/install_skills.py --platform claude --force
```

### 如果你的平台使用自定义目录

```bash
python3 scripts/install_skills.py --target-dir /path/to/your/skills --force
```

### 如果你的系统或平台不方便使用 symlink

```bash
python3 scripts/install_skills.py --platform codex --mode copy --force
```

---

## 3. 安装后一定要做的事

很多平台只在**启动会话时**扫描技能目录。

所以安装后要：
1. **重开当前会话**，或直接**重启 AI runtime**
2. 再次查看平台里的 available skills
3. 再调用目标 skill

如果你不重开会话，常见现象是：
- 磁盘上已经有 skill 目录
- 但当前会话的 `Available skills` 仍然是旧列表
- 然后继续报 `Skill not found`

---

## 4. 常见根因清单

### 情况 1：repo 里有 skill，但运行时目录里没有
典型症状：
- `skills/knowledge-base-ingest/` 存在
- 但 `~/.codex/skills/knowledge-base-ingest/` 不存在

修法：
- 用 `scripts/install_skills.py` 安装到正确目录

### 情况 2：装到了 Claude，但你实际在 Codex 里运行
典型症状：
- `~/.claude/skills/knowledge-base-ingest/` 存在
- `~/.codex/skills/knowledge-base-ingest/` 不存在

修法：
- 安装到你当前实际运行的平台目录

### 情况 3：只装了部分 skill，不是完整 10-skill package
典型症状：
- `knowledge-base-ingest` 有
- `knowledge-base-project-management` / `knowledge-base-team-coordination` / `knowledge-base-delivery-audit` 等缺失

修法：
- 整包同步，而不是只补单个 skill

### 情况 4：skill 已装，但当前会话没刷新
典型症状：
- 目录已存在
- 但 `Available skills` 列表里没有它

修法：
- 重开会话或重启运行环境

### 情况 5：skill 名称拼错
当前 repo 中应使用：
- `knowledge-base-kit-guide`
- `knowledge-base-orchestrator`
- `knowledge-base-ingest`
- `knowledge-base-maintenance`
- `knowledge-base-audit`
- `knowledge-base-project-management`
- `knowledge-base-team-coordination`
- `knowledge-base-delivery-audit`
- `knowledge-base-working-profile`
- `work-journal`

---

## 5. 推荐验证方式

### 检查 repo 里有哪些 skills

```bash
ls skills
```

### 检查运行时目录里有哪些 skills

```bash
ls ~/.codex/skills
ls ~/.claude/skills
```

### 检查某个具体 skill 是否已安装到目标 runtime

```bash
ls ~/.codex/skills/knowledge-base-project-management
ls ~/.codex/skills/knowledge-base-delivery-audit
```

---

## 6. 推荐安装策略

对于本地长期使用，推荐：

```bash
python3 scripts/install_skills.py --platform codex --force
python3 scripts/install_skills.py --platform claude --force
```

这样可以：
- 保持 Codex / Claude 两边技能目录一致
- 避免“这个平台有、那个平台没有”的版本偏差
- 降低 `Skill not found` / partial package / stale install 这类问题

---

## 7. 如果还是失败

请同时检查：
- 你当前到底是在 **Codex / Claude Code / OpenClaw / Hermes / 其他 runtime** 的哪一个里运行
- 这个 runtime 实际扫描的 `skills` 目录是哪一个
- 当前会话是不是在安装前就已经启动了
- `Available skills` 列表里是否真的出现了目标 skill 名

如果你要提 issue，建议附上：
- 你使用的平台
- 你安装到的 skills 目录
- `Available skills` 列表截图或文本
- 你调用的具体 skill 名
- 你是否在安装后重启了会话
