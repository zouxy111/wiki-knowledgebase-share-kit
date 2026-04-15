# Example Prompts

## 1. 第一次安装后，不知道怎么开始

```text
Use $knowledge-base-kit-guide to walk me through this share kit.
I have not configured my vault profile yet. Tell me the minimum setup I need, then tell me which skill I should use next.
```

## 2. 我已经有 profile，想沉淀一轮任务结果

```text
Use $knowledge-base-maintenance to integrate this task into my markdown knowledge base.
Read my vault profile first. Keep only durable conclusions or reusable troubleshooting knowledge, choose the right page role, and sync the target page, relevant root page, reader entrypoint, and milestone log.
```

## 3. 我怀疑 wiki 结构已经乱了

```text
Use $knowledge-base-audit to inspect my knowledge base.
Read the vault profile first, then report dead links, orphan pages, missing entrypoints, metadata issues, page-boundary drift, noise regression, and stray markdown files at the vault root.
```

## 4. 先审计，再修

```text
Use $knowledge-base-audit first to inspect my vault and list findings by priority.
Then use $knowledge-base-maintenance to fix the high-priority issues while preserving the page-role model.
```

## 5. 中文首次上手

```text
用 $knowledge-base-kit-guide 帮我开始用这套知识库维护包。
我还没有配 vault profile，请先告诉我最少要补哪些信息，再告诉我下一步应该调用哪个 skill。
```

## 6. 中文写入知识库

```text
用 $knowledge-base-maintenance 把这次结果沉淀进我的知识库。
先读 vault profile，再过滤过程噪音，按页面角色归类，并同步目标页、root page、reader entry 和 milestone log。
```

## 7. 中文结构体检

```text
用 $knowledge-base-audit 审计我的知识库。
先读 vault profile，再检查死链、孤立页、metadata、页面边界漂移、噪音回流，以及根目录 stray markdown 文件。
```
