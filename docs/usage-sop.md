# Usage SOP

## 三个 skill 的职责分工

### `knowledge-base-kit-guide`
用于：
- 教用户怎么安装这套分享包
- 教用户怎么填写 `vault profile`
- 判断当前该先用 maintenance 还是 audit
- 给第一次接触这套 kit 的人做分流说明

### `knowledge-base-maintenance`
用于：
- 把任务结果沉淀进知识库
- 把聊天结论写进合适页面
- 收敛根页、知识页、运维页的写法边界
- 把噪音挡在知识库外面

### `knowledge-base-audit`
用于：
- 做结构健康检查
- 检查 dead links、orphan pages、frontmatter、导航覆盖
- 检查 page-boundary drift
- 检查 noise regression
- 检查 vault 根目录 stray markdown files

---

## 标准工作流

### 场景 A：任务完成后沉淀知识
1. 先用 `knowledge-base-maintenance`
2. 如果改动较大，再用 `knowledge-base-audit` 做复检

也就是：**先写，再审**。

### 场景 B：怀疑知识库已经乱了
1. 先用 `knowledge-base-audit`
2. 根据问题清单，再用 `knowledge-base-maintenance` 去修

也就是：**先查，再写**。

### 场景 C：周期巡检
定期只跑 `knowledge-base-audit`，看有没有：
- 入口丢失
- 页面边界漂移
- 根页堆流水
- `ops` 页退化成日志
- `log.md` 变任务回放

---

## Maintenance 的默认回路

1. 先读 vault profile
2. 先做噪音过滤
3. 判页面角色和 area
4. 优先更新已有页
5. 同步根页 / 读者入口 / 里程碑日志
6. 汇报哪些内容被保留、哪些被压缩

---

## Audit 的默认回路

1. 先读 vault profile
2. 查 frontmatter 和 metadata
3. 查 dead links / orphan pages / missing entrypoints
4. 查 root page coverage
5. 查 page-boundary drift
6. 查 noise regression
7. 查 root-level stray markdown files
8. 按 P1 / P2 / P3 输出

---

## 什么时候不该用 maintenance

如果内容只是：
- 临时聊天
- 单次运行日志
- 长过程记录
- 原始素材镜像
- 还没沉淀成结论的草稿

默认不该直接进知识库。

---

## 什么时候不该用 audit

如果你已经明确知道：
- 这次要改哪一页
- 这次要把什么结论写进去

那就直接用 maintenance，不必先做审计。

---

## 输出要求

### maintenance
至少说明：
- 改了哪些页
- 为什么归到该页面角色
- 是否同步了入口和日志
- 哪些内容被判为噪音

### audit
至少说明：
- audit summary
- P1 / P2 / P3 findings
- 影响页面
- 建议修复顺序
- 是否存在 root-level stray files
