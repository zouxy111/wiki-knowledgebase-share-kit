# Wiki Knowledge Base Share Kit

[![Release](https://img.shields.io/github/v/release/zouxy111/wiki-knowledgebase-share-kit)](https://github.com/zouxy111/wiki-knowledgebase-share-kit/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](./LICENSE)
[![Repo](https://img.shields.io/badge/GitHub-zouxy111%2Fwiki--knowledgebase--share--kit-black?logo=github)](https://github.com/zouxy111/wiki-knowledgebase-share-kit)

> 一套可分享的 markdown/wiki 知识库维护方法包。  
> 目标：把“知识库优先、页面角色清晰、噪音不过度回流”的维护方式，抽成可安装 skill + 可阅读文档。

**语言 / Language**：[`中文 README`](./README.md) · [`English README`](./README.en.md)

## 快速入口
- [`START-HERE.md`](./START-HERE.md)：第一次拿到仓库时的最短上手路径
- [`COVER-CN.md`](./COVER-CN.md)：中文封面说明
- [`templates/vault-profile-template.md`](./templates/vault-profile-template.md)：配置自己的 vault profile
- [`docs/customization-guide.md`](./docs/customization-guide.md)：如何改造成自己的知识库体系
- [`docs/example-prompts.md`](./docs/example-prompts.md)：可直接复制的提示词
- [`Releases`](https://github.com/zouxy111/wiki-knowledgebase-share-kit/releases)：下载发布版本

---


## 这套分享包解决什么问题

很多 markdown/wiki vault 会遇到同一类问题：
- 新内容越写越像项目日志，而不像知识库
- 根页、专题页、运维页职责混乱
- `index.md`、导航入口和里程碑日志不同步
- 审计时不知道该检查结构、边界还是噪音回流

这套 kit 把这些问题抽成两类能力：

1. **Maintenance**：把任务结果或结论沉淀进知识库
2. **Audit**：检查知识库结构、导航、元数据和噪音回流

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
  skills/
    knowledge-base-kit-guide/
    knowledge-base-maintenance/
    knowledge-base-audit/
```

### `skills/`
可直接复制到本地 AI 平台的 `skills/` 目录里使用。

### `docs/`
平台无关的说明文档。即使不安装 skill，也可以按这里的方法手工维护知识库。

### `templates/`
`vault profile` 模板。使用前先填写它，再把 skill 指向你的 profile。

### `examples/`
当前真实 vault 的案例化示例，用来展示“这套模板如何落到一个具体知识库上”。

---

## 推荐安装方式

把以下三个目录复制到你的 skills 目录：

- `skills/knowledge-base-kit-guide`
- `skills/knowledge-base-maintenance`
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
4. 根据需要微调 checklist

### 第一次上手时
- 先用 `knowledge-base-kit-guide` 理解安装顺序、profile 配置和技能分工

### 日常使用
- 要沉淀任务结果时：用 `knowledge-base-maintenance`
- 要做结构审计时：用 `knowledge-base-audit`
- 大改之后：先 maintenance，再 audit

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
- `docs/usage-sop.md`

如果想看一个完整落地示例，再读：
- `examples/example-vault-profile.md`
- `examples/case-study-current-vault.md`


---

## 开源仓库补充文件

为了方便直接发布到 GitHub，本仓库额外提供：
- `LICENSE`
- `CONTRIBUTING.md`
- `CHANGELOG.md`
- `README.en.md`
- `.gitignore`

如果你要直接开源，保留这些文件即可。

## License

本项目采用 MIT License，详见 `LICENSE`。
