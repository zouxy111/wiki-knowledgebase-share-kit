# Vault Sync Contract

## When sync is allowed
仅在以下条件同时成立时允许知识库同步：
1. 用户提供了 vault profile
2. 用户希望同步
3. 被同步的内容已是 `approved`

## Default sync targets
### 1. Member-profile increments
例如：
- 长期有效的能力变化
- 稳定偏好
- 重复出现的约束
- 更清晰的协作边界

### 2. Stable decision distills
例如：
- 未来项目仍可复用的判断规则
- 问卷策略
- 协作模式
- 任务边界

## What must not be synced
- raw drafts
- 未确认的 alignment 冲突
- 一次性运行状态
- 原始长问答
- secrets / private data

## Governance rule
同步时仍必须遵守现有 knowledge-base model：
- `project / knowledge / ops / task / overview`
- 不新增第二套治理模型
- 如需页面更新，应按维护口径写入 durable knowledge，而不是复制项目流水
