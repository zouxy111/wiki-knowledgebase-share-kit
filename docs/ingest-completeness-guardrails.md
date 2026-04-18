# Ingest Completeness Guardrails

> 目标：让长文档导入不是“模型看了前半部分，后半部分漏掉”，而是一个**可验证的全量覆盖流程**。

---

## 1. 先讲结论

如果 source 很长，尤其是：
- 几千行以上
- 附录很多
- 有长表格 / 指南 / 规程 / 章节合集
- 甚至达到 **10 万行**

那么 **禁止直接让模型“整篇读完再回写”**。

正确做法是：

1. **先脚本切分**成受控 chunk
2. 生成 `manifest.json`
3. 生成 `coverage-map.md`
4. 按 chunk 逐个处理
5. 用 `verify_ingest_coverage.py` 做完成态校验

只有 verification 通过，才允许说“完整导入”。

---

## 2. 为什么要这样做

长文档导入最常见的失败模式不是“完全不会导”，而是：
- 前半部分读了，后半部分没读完
- 主体章节导了，附录和支持性内容漏了
- 模型以为“核心内容差不多了”，但实际上 coverage 远未完整
- 最后缺少一个逐段核对的工件，所以错误被带入知识库

要解决这个问题，必须把“完整阅读”从隐含要求变成**显式约束**。

---

## 3. GitHub 仓库中的强约束实现

当前仓库建议的完整流程是：

### Step 1：先切分 source

```bash
python3 skills/knowledge-base-ingest/scripts/split_markdown.py \
  source.md \
  --out ./ingest-workdir
```

这个脚本现在会输出：
- chunk files
- `manifest.json`
- `toc.md`
- `coverage-map.md`

### Step 2：逐 chunk 处理，而不是整篇硬读

`coverage-map.md` 里的每一行都对应一个 source chunk。

每一行都必须最终进入以下状态之一：
- `covered`
- `merged`
- `index-only`
- `intentionally-omitted`

如果还是：
- `unread`
- `blocked`
- 空白

那就说明这轮导入**还没完成**。

### Step 3：完成前跑验证脚本

```bash
python3 skills/knowledge-base-ingest/scripts/verify_ingest_coverage.py \
  --manifest ./ingest-workdir/manifest.json \
  --coverage ./ingest-workdir/coverage-map.md
```

如果这个脚本失败，导入结果只能算：
- partial
- draft
- incomplete

不能算 fully imported。

---

## 4. 这个约束为什么能扛 10 万行

关键不在于“模型一次能读多少”，而在于：

> **不要求模型一次读完 10 万行，而要求系统把 10 万行拆成必经的、可枚举的、可校验的 chunk 序列。**

这样做以后：
- 模型只需要逐 chunk 工作
- 每个 chunk 有上限（默认还有 `--max-lines`）
- 即使中途暂停，也知道还剩哪些 chunk 没处理
- 用户可以检查 coverage map，而不是相信一句“我已经完整导入了”

这就是“约束型完整性”，而不是“靠模型自觉完整”。

---

## 5. 推荐工作原则

### 原则 A：source 很大时，禁止直接整篇导入

对于很长的 source，先 split，后 rewrite。

### 原则 B：必须保留 chunk ledger

`manifest.json` + `coverage-map.md` 是完整性工件，不是可选附件。

### 原则 C：没有通过 verification，就不能宣称完成

这一步是 completion gate。

### 原则 D：附录、支持治疗、随访、术语表同样要进 coverage

不要只覆盖“主体章节”，把：
- appendix
- support care
- follow-up
- tables
- report templates
- classification systems

都排除在外。

它们可以被：
- `covered`
- `merged`
- `index-only`
- `intentionally-omitted`

但不能“没有 disposition”。

---

## 6. 什么时候只能汇报 partial

以下任一情况成立时，都只能汇报 partial / incomplete：

- `coverage-map.md` 仍有 `unread`
- 仍有 `blocked`
- 某个 manifest row 没有 coverage row
- 某个 chunk 被说“已覆盖”，但没有 target page
- 某个 chunk 被 `intentionally-omitted`，但没有理由

---

## 7. 推荐用户口径

如果 verification 还没过，应该明确说：

- “已完成第一轮导入基线，但尚未完成全量 coverage verification”
- “核心章节已覆盖，但附录/支持治疗/随访仍未完成 disposition”
- “当前结果是 partial ingest，不应视为完整回写”

而不要说：

- “已完整回写”
- “已全部导入”
- “source 已 fully covered”

---

## 8. 和模型无关的部分

这套 guardrail 的价值正是在于：

- 不要求所有用户都用同一个模型
- 不要求所有 agent 都有同样长的上下文
- 不要求模型一次吞下超长输入

只要求：
- 能跑脚本
- 能按 manifest 分块处理
- 能维护 coverage map
- 能在结束前跑 verification

所以它比“优化一版 prompt”更可复用，也更可靠。
