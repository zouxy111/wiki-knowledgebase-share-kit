# Source Coverage Rules

当导入一个长文档时，**不能只凭“我大概读完了”就宣布完成**。

## 核心要求

1. 先对原始 markdown 做 deterministic split
2. 读取 `manifest.json` 和 `coverage-map.md`
3. **逐个 chunk 完成 disposition**，不能跳过未读 chunk
4. 每个 chunk 在导入结束前都必须有明确状态
5. 在 coverage verification 通过前，不得把导入标记为“已完成”

---

## 推荐状态

### Final statuses（可作为完成态）
- `covered`：该 chunk 的内容已被目标页面吸收
- `merged`：该 chunk 已与其他 chunk 合并吸收到更高层页面
- `index-only`：该 chunk 不单独落页，但已在 overview / appendix / index 中被保留
- `intentionally-omitted`：明确决定不导入，且必须写明理由

### Incomplete statuses（不允许宣称完成）
- `unread`
- `blocked`
- 空白状态

---

## Completion gate

如果任一 chunk 仍是：
- `unread`
- `blocked`
- 空白

或者没有写明 target pages / omission 理由，
则这轮导入只能汇报为：
- partial
- draft
- not yet complete

**不能汇报为 fully imported / completed / 已完整回写。**

---

## 为什么要这样做

很多“导入不完整”的问题，不是因为模型完全没能力，
而是因为：
- 源文档太长
- 中途只读了前半部分
- 后半部分被压缩、省略或遗忘
- 最终却没有一个 chunk-level 覆盖检查

覆盖表的作用就是把“是否真的完整读过并做过处理”变成显式工件，而不是口头承诺。

---

## 推荐验证命令

在完成 coverage-map.md 后，运行：

```bash
python3 skills/knowledge-base-ingest/scripts/verify_ingest_coverage.py \
  --manifest <dir>/manifest.json \
  --coverage <dir>/coverage-map.md
```

如果脚本返回非零，就说明：
- 仍有 chunk 未读
- 或仍有 chunk 没被明确处理
- 或 omitted / merged 没有写清楚去向
