# Gate Model

## Gate states
- `blocked`：关键缺口存在，不能继续宣告完成
- `ready`：主体闭环已成立，可以进入人工批准 / handoff
- `greenlight pending`：需要明确批准动作，不能自我宣布 greenlight

## Common blocked reasons
- 缺证据
- 缺关键决策记录
- 缺回写
- 缺 handoff 材料
- 成功标准定义不清

## Important boundary
`greenlight` 是管理 / 批准动作，不应由普通执行状态自动推出。
