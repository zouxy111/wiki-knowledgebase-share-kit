# Wiki Knowledge Base Share Kit

[![Release](https://img.shields.io/github/v/release/zouxy111/wiki-knowledgebase-share-kit)](https://github.com/zouxy111/wiki-knowledgebase-share-kit/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](./LICENSE)
[![Repo](https://img.shields.io/badge/GitHub-zouxy111%2Fwiki--knowledgebase--share--kit-black?logo=github)](https://github.com/zouxy111/wiki-knowledgebase-share-kit)
[![Validate](https://github.com/zouxy111/wiki-knowledgebase-share-kit/actions/workflows/validate.yml/badge.svg)](https://github.com/zouxy111/wiki-knowledgebase-share-kit/actions/workflows/validate.yml)

> 一套可分享的 markdown/wiki 知识库维护方法包。  
> 目标：把“知识库优先、页面角色清晰、噪音不过度回流”的维护方式，抽成可安装 skill + 可阅读文档。

**语言 / Language**：[`中文 README`](./README.md) · [`English README`](./README.en.md)

## 快速入口
- [`START-HERE.md`](./START-HERE.md)：第一次拿到仓库时的最短上手路径
- [`COVER-CN.md`](./COVER-CN.md)：中文封面说明
- [`templates/vault-profile-template.md`](./templates/vault-profile-template.md)：配置自己的 vault profile
- [`examples/example-vault-profile-generic.md`](./examples/example-vault-profile-generic.md)：不带个人路径的通用 profile 示例
- [`docs/customization-guide.md`](./docs/customization-guide.md)：如何改造成自己的知识库体系
- [`docs/example-prompts.md`](./docs/example-prompts.md)：可直接复制的提示词
- [`templates/working-profile-page-template.md`](./templates/working-profile-page-template.md)：working profile 页面模板
- [`examples/case-study-pathology-ingest-iteration.md`](./examples/case-study-pathology-ingest-iteration.md)：测试驱动的长文档导入案例
- [`Releases`](https://github.com/zouxy111/wiki-knowledgebase-share-kit/releases)：下载发布版本
- [`GitHub Pages`](https://zouxy111.github.io/wiki-knowledgebase-share-kit/)：浏览开源落地页

---

## 开发者

- 邹星宇
- 杨琦

---

![Share kit preview](./docs/assets/social-preview.png)

## 30 秒看懂这套 kit

| 你现在的 vault 可能是 | 用完这套 kit 后希望变成 |
|---|---|
| 根页堆了很多执行过程和临时记录 | 根页只保留导航、稳定边界、专题入口 |
| `ops` 页越写越像按天流水账 | `ops` 页沉淀成“现象 / 根因 / 处理法 / 边界” |
| `log.md` 变成任务回放 | `log.md` 只保留 milestone 级变化 |
| 有内容页，但没有稳定入口 | 页面必须被 root page / reader entry 收录 |
| 审计时不知道先看结构还是正文 | 先看 metadata、导航、死链、边界漂移、噪音回流 |

一句话说：

> 这不是“帮你多记日志”的包，而是“把知识库重新写得像知识库”的包。

---

## 这套分享包解决什么问题

很多 markdown/wiki vault 会遇到同一类问题：
- 新内容越写越像项目日志，而不像知识库
- 根页、专题页、运维页职责混乱
- `index.md`、导航入口和里程碑日志不同步
- 审计时不知道该检查结构、边界还是噪音回流

这套 kit 把这些问题抽成四类能力：

1. **Ingest**：把长 markdown / 书稿 / 教程按章节拆分，并生成目录、术语候选和 related links 建议后导入知识库
   - 第一版导入只作为**可测试基线**，后续应根据测试结果继续优化拆分粒度、页面角色和链接架构
   - 整个 ingest 回路可以当作一个轻量 harness / 回归底座来用
2. **Maintenance**：把任务结果或结论沉淀进知识库
3. **Working Profile**：把持续沟通中反复出现的偏好、决策习惯和协作边界沉淀成 working profile
4. **Audit**：检查知识库结构、导航、元数据和噪音回流

同时保留固定页面角色模型：
- `project`
- `knowledge`
- `ops`
- `task`
- `overview`

但把这些内容改成用户自定义：
- vault 路径
- `pages/` 目录位置
- root pages
- area 列表
- 命名约定
- frontmatter 约定

---

## 适合谁 / 不适合谁

### 适合
- 已经在维护 Obsidian / markdown / wiki vault 的个人或团队
- 想把"任务过程"和"长期知识"拆开的使用者
- 接受固定页面角色模型：`project / knowledge / ops / task / overview`
- 希望把"写入维护"和"结构审计"拆成两条明确工作流的人
- 想把这份包直接分享给其他维护者的人（见下方"交付边界"）

### 不太适合
- 完全不想配置 profile 的人
- 希望 vault 继续以流水日志为主的人
- 不接受固定页面角色模型的人
- 只想记录原始过程，不在意知识沉淀和导航治理的人

## 交付边界

### 这份包已包含
- 可安装 skill（5 个）
- 安装与配置说明
- vault profile 模板
- 示例 profile
- 使用口令示例

### 这份包不包含
- 自动生成 profile 的脚本
- 针对某个平台的专用 installer
- 针对某个业务领域的 area/root page 预设

### 分享时的最短指引
```text
这是一个可复用的 wiki/markdown 知识库维护包。
先看 START-HERE.md，再复制 5 个 skills，填好 vault-profile-template.md，然后先用 knowledge-base-kit-guide 上手。
```

## 使用案例

- [`examples/case-study-current-vault.md`](./examples/case-study-current-vault.md)：从当前 vault 抽象出可分享的固定规则
- [`examples/case-study-pathology-ingest-iteration.md`](./examples/case-study-pathology-ingest-iteration.md)：展示如何把长篇专业 Markdown 先导入成可测试基线，再以轻量 harness 的方式通过测试、回归和版本对比持续优化知识库结构

---

## 支持平台状态

| 平台 | 状态 | 说明 |
|---|---|---|
| Codex / ChatGPT Codex 风格 skills 目录 | 推荐 | 仓库已包含 5 个 skill 的 `SKILL.md`、`references/`、`agents/openai.yaml` |
| Claude 风格 skills 目录 | 可用 | 直接复制五个 skill 目录即可 |
| 其他支持 `SKILL.md` 目录结构的平台 | 可能可用 | 需自行适配调用方式与 skill 发现机制 |

如果你不确定平台兼容性，先看：
- `START-HERE.md`
- `docs/usage-sop.md`

---

## 包内结构

```text
wiki-knowledgebase-share-kit/
  COVER-CN.md
  中文封面说明页.md
  START-HERE.md
  README.md
  docs/
  templates/
  examples/
    example-vault-profile-generic.md
  skills/
    knowledge-base-kit-guide/
    knowledge-base-ingest/
    knowledge-base-maintenance/
    knowledge-base-working-profile/
    knowledge-base-audit/
```

### `skills/`
可直接复制到本地 AI 平台的 `skills/` 目录里使用。

### `docs/`
平台无关的说明文档。即使不安装 skill，也可以按这里的方法手工维护知识库。

### `templates/`
`vault profile` 模板。使用前先填写它，再把 skill 指向你的 profile。

### `examples/`
既包含真实案例，也包含**不带个人路径的通用示例**，方便公开仓库读者直接参考。

---

## 推荐安装方式

把以下五个目录复制到你的 skills 目录：

- `skills/knowledge-base-kit-guide`
- `skills/knowledge-base-ingest`
- `skills/knowledge-base-maintenance`
- `skills/knowledge-base-working-profile`
- `skills/knowledge-base-audit`

常见位置示例：
- `~/.codex/skills`
- `~/.claude/skills`

安装后，先准备自己的 `vault profile`，再调用 skill。

---

## 推荐使用顺序

### 第一次适配
1. 先读 `docs/customization-guide.md`
2. 复制 `templates/vault-profile-template.md`
3. 填写自己的 vault root、areas、root pages、frontmatter 规则
4. 参考 `examples/example-vault-profile-generic.md`
5. 根据需要微调 checklist

### 第一次上手时
- 先用 `knowledge-base-kit-guide` 理解安装顺序、profile 配置和技能分工

### 日常使用
- 要导入长文档 / 书籍 / 教程时：用 `knowledge-base-ingest`（支持拆分、TOC、术语候选、related links 建议，以及轻量 harness 风格的结构迭代）
- 要沉淀任务结果时：用 `knowledge-base-maintenance`
- 要沉淀长期协作画像时：用 `knowledge-base-working-profile`
- 要做结构审计时：用 `knowledge-base-audit`
- 大改之后：先 ingest / maintenance，再 audit

---

## 这套方法的固定部分

以下内容默认固定，不建议轻易改掉：
- 知识库优先，不收一次性过程噪音
- 页面角色模型：`project / knowledge / ops / task / overview`
- 根页只做导航和稳定总览
- `ops` 页默认写成“现象 / 根因 / 处理法 / 边界”
- `log.md` 只写里程碑，不写任务回放
- 每次实质维护至少同步：目标页、根页、`index.md`、`log.md`

---

## 可自定义部分

以下内容应由使用者在自己的 `vault profile` 中定义：
- vault 路径
- 页面目录
- 读者入口
- 日志文件
- 维护入口
- area 列表
- root pages
- 命名规则
- frontmatter 规则
- 允许存在于 vault 根目录的 canonical markdown 文件

---

## 先读哪几个文件

最短路径：
- `COVER-CN.md`
- `中文封面说明页.md`
- `START-HERE.md`
- `docs/customization-guide.md`
- `templates/vault-profile-template.md`
- `templates/working-profile-page-template.md`
- `docs/usage-sop.md`

如果想看一个完整落地示例，再读：
- `examples/example-vault-profile-generic.md`
- `examples/example-vault-profile.md`
- `examples/case-study-current-vault.md`
- `examples/case-study-pathology-ingest-iteration.md`

---

## 开源仓库补充文件

为了方便直接发布到 GitHub，本仓库额外提供：
- `LICENSE`
- `CONTRIBUTING.md`
- `CHANGELOG.md`
- `README.en.md`
- `.gitignore`
- `.github/workflows/validate.yml`

如果你要直接开源，保留这些文件即可。

## License

本项目采用 MIT License，详见 `LICENSE`。
