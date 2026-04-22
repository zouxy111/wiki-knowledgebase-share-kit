# Quickstart

## 最短上手路径

1. 先读 share kit 根目录下的 `README.md`
2. 再读 `docs/customization-guide.md`
3. 复制 `templates/vault-profile-template.md`
4. 填好你自己的 vault 路径、areas、root pages、frontmatter 规则
5. 安装所有 10 个 skills：
   - `skills/knowledge-base-kit-guide`（使用指南）
   - `skills/knowledge-base-orchestrator`（总控/一键式）
   - `skills/knowledge-base-ingest`（长文档导入）
   - `skills/knowledge-base-maintenance`（知识库维护）
   - `skills/knowledge-base-audit`（结构审计）
   - `skills/knowledge-base-project-management`（项目 owner / 里程碑 / blocker）
   - `skills/knowledge-base-team-coordination`（团队协调）
   - `skills/knowledge-base-delivery-audit`（交付完整性 / ready / greenlight）
   - `skills/knowledge-base-working-profile`（协作画像）
   - `skills/work-journal`（工作记录）
   - 推荐直接运行：`python3 scripts/install_skills.py --platform codex --force`
   - 或：`python3 scripts/install_skills.py --platform claude --force`
   - 安装后记得重开会话，否则 runtime 可能继续显示旧的 available skills
6. 第一次落地时：
   - 如果完全新手：先用 `knowledge-base-orchestrator` 一键完成环境配置
   - 如果想手动：先用 maintenance 沉淀一个小结果，再用 audit 看结构是否健康

## 如果用户只想先看懂
推荐顺序：
- `README.md`
- `docs/usage-sop.md`
- `examples/example-vault-profile.md`

## 如果用户已经安装但不会用
先确认：
- 有没有填写 `vault profile`
- 是否明确 root pages
- 是否明确 canonical root-level markdown files
- 是否知道各个 skills 的职责边界

## 各 skill 使用场景

| 场景 | 推荐 skill |
|------|-----------|
| 第一次安装，不知道从哪开始 | `knowledge-base-kit-guide` |
| 一键配置环境，不想折腾 | `knowledge-base-orchestrator` |
| 导入长文档/书籍 | `knowledge-base-ingest` |
| 沉淀任务结果到知识库 | `knowledge-base-maintenance` |
| 检查知识库健康度 | `knowledge-base-audit` |
| 项目 intake / 周计划 / milestone / blocker | `knowledge-base-project-management` |
| 多人协作项目 | `knowledge-base-team-coordination` |
| 交付闭环 / ready / greenlight 审计 | `knowledge-base-delivery-audit` |
| 记录协作习惯/决策偏好 | `knowledge-base-working-profile` |
| 写日报/会议纪要 | `work-journal` |
