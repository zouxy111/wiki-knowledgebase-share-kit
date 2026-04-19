# Docs Index

这个目录承载平台无关的说明文档。和 [`START-HERE.md`](../START-HERE.md) 的区别是：
- `START-HERE.md` 面向第一次上手的人
- `docs/README.md` 面向已经进入仓库、想快速找到对应说明的人

## 技能总览

规范清单位于 [`skills/catalog.toml`](../skills/catalog.toml)，下表由 catalog 驱动：

<!-- skill-catalog:zh:start -->
| # | Skill | 能力线 | 主要职责 |
|---|---|---|---|
| 1 | `knowledge-base-kit-guide` | Onboarding / Orchestration | 使用说明、profile 配置、技能分流 |
| 2 | `knowledge-base-orchestrator` | Onboarding / Orchestration | 零门槛初始化入口 |
| 3 | `knowledge-base-ingest` | Ingest | 长文档导入与结构化重组 |
| 4 | `knowledge-base-maintenance` | Maintenance | 任务结果与会议结论沉淀 |
| 5 | `knowledge-base-audit` | Audit | 结构审计与知识库健康检查 |
| 6 | `knowledge-base-working-profile` | Working profile | 协作画像提炼与维护 |
| 7 | `knowledge-base-team-coordination` | Team coordination | 共享项目协调与角色化问卷 |
| 8 | `work-journal` | Work journal | 工作记录、会议纪要与周期沉淀 |
<!-- skill-catalog:zh:end -->

## 新用户入口

- [`../START-HERE.md`](../START-HERE.md) — 5 分钟快速上手
- [`../GLOSSARY.md`](../GLOSSARY.md) — 术语与固定模型
- [`../README.md`](../README.md) — 产品定位、适用场景、安装入口
- [`../README.en.md`](../README.en.md) — 英文总览

## 日常使用

- [`usage-sop.md`](./usage-sop.md) — 8 个 skill 的职责分工与路线选择
- [`example-prompts.md`](./example-prompts.md) — 常见调用示例
- [`customization-guide.md`](./customization-guide.md) — 如何适配自己的 vault 结构
- [`skill-installation-troubleshooting.md`](./skill-installation-troubleshooting.md) — skill 安装后仍无法识别时怎么排查

## 深入主题

- [`ingest-completeness-guardrails.md`](./ingest-completeness-guardrails.md) — chunk 覆盖与完成态要求
- [`ingest-evaluation-rubric.md`](./ingest-evaluation-rubric.md) — 导入质量评估
- [`team-coordination-workflow.md`](./team-coordination-workflow.md) — 共享项目协调 workflow
- [`collaboration-integration-patterns.md`](./collaboration-integration-patterns.md) — 多平台协作接入模式
- [`reuse-from-zero.md`](./reuse-from-zero.md) — 从零复用到自己的环境
- [`core-vs-local-overlay.md`](./core-vs-local-overlay.md) — 核心 skill 与本地 overlay 的边界

## 维护者入口

- [`../CONTRIBUTING.md`](../CONTRIBUTING.md) — 提交前注意事项
- [`../skills/catalog.toml`](../skills/catalog.toml) — skill 的规范清单
- [`../scripts/validate_skill_bundle.py`](../scripts/validate_skill_bundle.py) — catalog / frontmatter / doc sync 校验
- [`../Makefile`](../Makefile) — 常用维护命令

## 示例与模板

- [`../examples/`](../examples/) — 场景化案例与共享项目示例
- [`../examples/local-overlay/README.md`](../examples/local-overlay/README.md) — 本地 overlay 示例
- [`../templates/`](../templates/) — profile、journal、team workspace 模板
