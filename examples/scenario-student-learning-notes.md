# 场景示例：学生学习笔记

> 这是一个完整的真实场景示例，展示一个大学生如何用这套工具整理学习笔记。

---

## 场景背景

**用户**：张三，大三计算机专业学生

**痛点**：
- 课程笔记、作业、项目、面试准备全混在一起
- 想复习某个知识点，翻半天找不到
- 有些笔记写了但从来没再看过（因为找不到）
- 临时想法和正式笔记混在一起

**目标**：
- 把笔记按学科分类
- 课程笔记和知识沉淀分开
- 作业和项目有清晰的任务清单
- 能快速找到任何一个知识点

---

## 第一步：设计知识库结构

### Areas（分类）
```yaml
- cs-courses    # 计算机课程
- math          # 数学课程  
- projects      # 个人项目
- interview     # 面试准备
- life          # 生活记录
```

### Root Pages（导航页）
```yaml
- cs-courses    → pages/project-cs-overview.md
- math          → pages/project-math-overview.md
- projects      → pages/project-projects-overview.md
- interview     → pages/project-interview-overview.md
- life          → pages/project-life-overview.md
```

---

## 第二步：填写 Vault Profile

```yaml
---
## 1. Vault identity

- Vault name: 张三的学习笔记
- Vault root path: /Users/zhangsan/Documents/study-notes
- Primary markdown page directory: /Users/zhangsan/Documents/study-notes/pages
- Reader entrypoint file: /Users/zhangsan/Documents/study-notes/index.md
- Milestone log file: /Users/zhangsan/Documents/study-notes/log.md
- Maintainer entrypoint file: /Users/zhangsan/Documents/study-notes/pages/governance.md

## 3. Area list

| area | 用途说明 |
|---|---|
| cs-courses | 计算机课程笔记 |
| math | 数学课程笔记 |
| projects | 个人项目 |
| interview | 面试准备 |
| life | 生活记录 |

## 4. Root page map

| area | root page file | 作用 |
|---|---|---|
| cs-courses | pages/project-cs-overview.md | 计算机课程导航 |
| math | pages/project-math-overview.md | 数学课程导航 |
| projects | pages/project-projects-overview.md | 项目导航 |
| interview | pages/project-interview-overview.md | 面试准备导航 |
| life | pages/project-life-overview.md | 生活记录导航 |

## 5. Canonical root-level markdown files

- README.md
- index.md
- log.md

## 6. Frontmatter contract

最少字段：
- title
- type
- area
- tags
- updated

## 7. Naming conventions

- Root pages 以 `project-` 开头
- Ops pages 用 `-ops` 结尾
- Task pages 用 `-tasks` 结尾

## 8. Writing rules switches

- Knowledge-base-first mode: yes
- Milestone-only log: yes
- ops page four-part pattern: yes
- Root pages should avoid long process narration: yes
---
```

---

## 第三步：创建文件结构

```bash
study-notes/
├── index.md                    # 总导航
├── log.md                      # 里程碑日志
├── README.md                   # 说明文档
└── pages/
    ├── project-cs-overview.md          # 计算机课程导航
    ├── project-math-overview.md        # 数学课程导航
    ├── project-projects-overview.md    # 项目导航
    ├── project-interview-overview.md   # 面试准备导航
    ├── project-life-overview.md        # 生活导航
    │
    ├── data-structures.md              # 数据结构知识
    ├── algorithms.md                   # 算法知识
    ├── operating-systems.md            # 操作系统知识
    ├── database-concepts.md            # 数据库概念
    │
    ├── linear-algebra.md               # 线性代数知识
    ├── calculus.md                     # 微积分知识
    │
    ├── web-app-project.md              # Web 项目
    ├── ml-project.md                   # 机器学习项目
    │
    ├── leetcode-tasks.md               # LeetCode 刷题清单
    ├── interview-prep-tasks.md         # 面试准备任务
    │
    └── governance.md                   # 维护规则
```

---

## 第四步：真实页面示例

### 示例 1：导航页（project）

**文件**：`pages/project-cs-overview.md`

```markdown
---
title: "计算机课程总览"
type: "project"
area: "cs-courses"
tags: ["导航", "计算机"]
updated: "2026-04-17"
---

# 计算机课程总览

## 当前学期课程（2026 春季）
- [数据结构与算法](./data-structures.md)
- [操作系统](./operating-systems.md)
- [数据库系统](./database-concepts.md)

## 已完成课程
- [计算机网络](./computer-networks.md)（2025 秋季）
- [编译原理](./compilers.md)（2025 秋季）

## 学习资源
- [推荐书单](./cs-books.md)
- [在线课程](./cs-online-courses.md)

## 相关链接
- [面试准备](./project-interview-overview.md)
- [个人项目](./project-projects-overview.md)
```

---

### 示例 2：知识页（knowledge）

**文件**：`pages/data-structures.md`

```markdown
---
title: "数据结构核心概念"
type: "knowledge"
area: "cs-courses"
tags: ["数据结构", "算法", "计算机"]
updated: "2026-04-17"
---

# 数据结构核心概念

## 线性结构

### 数组（Array）
- **特点**：连续内存、随机访问 O(1)
- **适用场景**：已知大小、频繁随机访问
- **不适用**：频繁插入删除

### 链表（Linked List）
- **特点**：非连续内存、插入删除 O(1)
- **适用场景**：频繁插入删除、大小不固定
- **不适用**：需要随机访问

## 树形结构

### 二叉搜索树（BST）
- **特点**：左子树 < 根 < 右子树
- **时间复杂度**：
  - 平均：O(log n)
  - 最坏：O(n)（退化成链表）
- **应用**：数据库索引、文件系统

### 平衡树（AVL / 红黑树）
- **特点**：自动平衡，保证 O(log n)
- **应用**：
  - AVL：读多写少
  - 红黑树：读写平衡（Java TreeMap、C++ map）

## 哈希表（Hash Table）

### 核心原理
```
index = hash(key) % table_size
```

### 冲突解决
1. **链地址法**：每个槽位是链表
2. **开放寻址**：线性探测、二次探测

### 时间复杂度
- 平均：O(1)
- 最坏：O(n)（所有元素冲突）

## 图（Graph）

### 表示方法
1. **邻接矩阵**：适合稠密图
2. **邻接表**：适合稀疏图

### 常见算法
- **遍历**：BFS、DFS
- **最短路径**：Dijkstra、Bellman-Ford
- **最小生成树**：Prim、Kruskal

## 快速对照表

| 数据结构 | 查找 | 插入 | 删除 | 空间 |
|---------|------|------|------|------|
| 数组 | O(1) | O(n) | O(n) | O(n) |
| 链表 | O(n) | O(1) | O(1) | O(n) |
| BST | O(log n) | O(log n) | O(log n) | O(n) |
| 哈希表 | O(1) | O(1) | O(1) | O(n) |

## 相关链接
- [算法分析](./algorithms.md)
- [LeetCode 刷题清单](./leetcode-tasks.md)
- [面试常考题](./interview-data-structures.md)
```

---

### 示例 3：任务页（task）

**文件**：`pages/leetcode-tasks.md`

```markdown
---
title: "LeetCode 刷题清单"
type: "task"
area: "interview"
tags: ["leetcode", "算法", "面试"]
updated: "2026-04-17"
---

# LeetCode 刷题清单

## 本周目标（2026-04-14 ~ 2026-04-20）

### 数组专题
- [x] #1 两数之和（Easy）
- [x] #15 三数之和（Medium）
- [ ] #42 接雨水（Hard）
- [ ] #53 最大子数组和（Medium）

### 链表专题
- [x] #206 反转链表（Easy）
- [ ] #141 环形链表（Easy）
- [ ] #142 环形链表 II（Medium）

## 下周计划（2026-04-21 ~ 2026-04-27）

### 二叉树专题
- [ ] #94 二叉树中序遍历
- [ ] #102 二叉树层序遍历
- [ ] #104 二叉树最大深度

## 已完成（归档）

### 第 1 周（2026-04-07 ~ 2026-04-13）
- [x] #1 两数之和
- [x] #20 有效的括号
- [x] #21 合并两个有序链表

## 刷题统计
- 总题数：150 / 300
- 本周完成：5 题
- Easy：80 题
- Medium：60 题
- Hard：10 题

## 相关链接
- [数据结构笔记](./data-structures.md)
- [算法笔记](./algorithms.md)
- [面试准备总览](./project-interview-overview.md)
```

---

### 示例 4：操作手册（ops）

**文件**：`pages/git-ops.md`

```markdown
---
title: "Git 常见问题排查"
type: "ops"
area: "projects"
tags: ["git", "troubleshooting"]
updated: "2026-04-17"
---

# Git 常见问题排查

## 问题 1：误提交了敏感信息

### 现象
不小心把 API key 提交到了 Git 仓库

### 根因
- 没有配置 .gitignore
- 直接 `git add .` 没有检查

### 处理法

#### 方法 1：还没 push（推荐）
```bash
# 撤销最后一次提交，保留修改
git reset --soft HEAD~1

# 删除敏感文件
rm config/secrets.yml

# 添加到 .gitignore
echo "config/secrets.yml" >> .gitignore

# 重新提交
git add .
git commit -m "Remove sensitive data"
```

#### 方法 2：已经 push
```bash
# 使用 BFG Repo-Cleaner
brew install bfg
bfg --delete-files secrets.yml
git reflog expire --expire=now --all
git gc --prune=now --aggressive
git push --force
```

### 边界
- 方法 1 只适用于还没 push 的情况
- 方法 2 会改写历史，团队协作需谨慎
- 如果已经泄露，立即更换密钥

---

## 问题 2：合并冲突

### 现象
```
CONFLICT (content): Merge conflict in file.txt
```

### 根因
- 两个分支修改了同一行代码
- Git 无法自动合并

### 处理法

#### 步骤 1：查看冲突文件
```bash
git status
```

#### 步骤 2：手动解决冲突
打开文件，找到：
```
<<<<<<< HEAD
你的修改
=======
别人的修改
>>>>>>> branch-name
```

保留需要的内容，删除标记。

#### 步骤 3：标记为已解决
```bash
git add file.txt
git commit
```

### 边界
- 适用于所有合并冲突场景
- 复杂冲突建议用 IDE 的可视化工具

---

## 问题 3：想撤销某次提交

### 现象
发现某次提交有 bug，想撤销

### 根因
- 代码有问题
- 需要回退到之前的版本

### 处理法

#### 方法 1：revert（推荐，保留历史）
```bash
git revert <commit-hash>
```

#### 方法 2：reset（危险，改写历史）
```bash
# 软重置（保留修改）
git reset --soft HEAD~1

# 硬重置（丢弃修改）
git reset --hard HEAD~1
```

### 边界
- 已经 push 的提交，用 revert
- 还没 push 的提交，可以用 reset
- 团队协作禁止用 reset --hard

---

## 相关链接
- [Git 学习笔记](./git-basics.md)
- [项目开发规范](./project-dev-guidelines.md)
```

---

## 第五步：使用效果

### 整理前 vs 整理后

| 维度 | 整理前 | 整理后 |
|------|--------|--------|
| 文件数量 | 200+ 个散乱文件 | 50 个结构化页面 |
| 查找时间 | 5-10 分钟 | 10 秒 |
| 重复内容 | 很多 | 几乎没有 |
| 导航 | 没有 | 清晰的 5 个入口 |
| 死链 | 20+ 个 | 0 个 |

### 实际使用场景

#### 场景 1：复习数据结构
1. 打开 `index.md`
2. 点击"计算机课程"
3. 点击"数据结构与算法"
4. 10 秒找到所有笔记

#### 场景 2：准备面试
1. 打开 `index.md`
2. 点击"面试准备"
3. 看到 LeetCode 刷题清单
4. 看到面试常考知识点

#### 场景 3：开始新项目
1. 打开 `index.md`
2. 点击"个人项目"
3. 创建新项目页面
4. 自动链接到相关技术笔记

---

## 第六步：定期维护

### 每周维护（5 分钟）
```bash
# 运行审计
Use $knowledge-base-audit to check my knowledge base.
Read vault profile at: ~/study-notes/my-vault-profile.md
```

检查：
- 有没有死链
- 有没有孤立页面
- 有没有缺失 frontmatter

### 每月维护（30 分钟）
1. 清理临时笔记
2. 合并重复内容
3. 更新导航页
4. 更新 log.md

---

## 总结

这个学生通过这套工具：
- ✅ 把 200+ 个散乱文件整理成 50 个结构化页面
- ✅ 查找时间从 5-10 分钟降到 10 秒
- ✅ 建立了清晰的 5 个分类导航
- ✅ 消除了所有死链和孤立页面
- ✅ 知识沉淀和临时笔记完全分开

**关键成功因素**：
1. 一开始就设计好 areas 和 root pages
2. 严格遵守 5 种页面角色
3. 每周定期审计
4. 临时笔记不直接进知识库
