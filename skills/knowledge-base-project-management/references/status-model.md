# Status Model

## Artifact status
- `draft`：草案，可讨论，不作为正式事实源
- `approved`：已确认，可作为后续管理或同步依据
- `blocked`：依赖未解或资料不足，不能继续推进
- `superseded`：被新版本替代，但保留追溯

## Project-level state
- `active`：正在推进
- `blocked`：因依赖 / 风险 / 缺资料而中断
- `done`：主要交付已完成
- `parked`：主动暂停，暂不推进

## Greenlight note
`greenlight` 不是普通 artifact status。
它属于交付审计语义，应由 `knowledge-base-delivery-audit` 判断，而不是由 PM board 直接自我宣布。
