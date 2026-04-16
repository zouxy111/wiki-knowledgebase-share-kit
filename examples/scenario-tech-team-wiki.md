# 场景示例：技术团队 Wiki

> 这是一个完整的真实场景示例，展示一个 10 人技术团队如何用这套工具维护团队 Wiki。

---

## 场景背景

**团队**：某创业公司后端团队，10 人

**痛点**：
- 技术文档、运维手册、项目文档全混在一起
- 新人入职找不到文档
- 线上故障时找不到排障手册
- 文档更新后没人知道
- 很多文档写了但从来没人看（因为找不到入口）

**目标**：
- 技术文档、运维手册、项目文档分开
- 新人能快速找到入职文档
- 故障时能快速找到排障手册
- 文档有清晰的导航和更新日志

---

## 第一步：设计知识库结构

### Areas（分类）
```yaml
- backend       # 后端技术
- infrastructure # 基础设施
- operations    # 运维手册
- projects      # 项目文档
- onboarding    # 新人入职
- governance    # 团队治理
```

### Root Pages（导航页）
```yaml
- backend       → pages/project-backend-overview.md
- infrastructure → pages/project-infra-overview.md
- operations    → pages/project-ops-overview.md
- projects      → pages/project-projects-overview.md
- onboarding    → pages/project-onboarding-overview.md
- governance    → pages/workspace-governance-overview.md
```

---

## 第二步：填写 Vault Profile

```yaml
---
## 1. Vault identity

- Vault name: 后端团队 Wiki
- Vault root path: /team/backend-wiki
- Primary markdown page directory: /team/backend-wiki/pages
- Reader entrypoint file: /team/backend-wiki/index.md
- Milestone log file: /team/backend-wiki/log.md
- Maintainer entrypoint file: /team/backend-wiki/pages/workspace-governance-overview.md

## 3. Area list

| area | 用途说明 |
|---|---|
| backend | 后端技术文档 |
| infrastructure | 基础设施文档 |
| operations | 运维排障手册 |
| projects | 项目文档 |
| onboarding | 新人入职指南 |
| governance | 团队治理规则 |

## 4. Root page map

| area | root page file | 作用 |
|---|---|---|
| backend | pages/project-backend-overview.md | 后端技术导航 |
| infrastructure | pages/project-infra-overview.md | 基础设施导航 |
| operations | pages/project-ops-overview.md | 运维手册导航 |
| projects | pages/project-projects-overview.md | 项目文档导航 |
| onboarding | pages/project-onboarding-overview.md | 新人入职导航 |
| governance | pages/workspace-governance-overview.md | 团队治理导航 |

## 5. Canonical root-level markdown files

- README.md
- index.md
- log.md
- CONTRIBUTING.md

## 6. Frontmatter contract

最少字段：
- title
- type
- area
- tags
- updated
- owner  # 团队文档需要明确负责人

## 7. Naming conventions

- Root pages 以 `project-` 或 `workspace-` 开头
- Ops pages 用 `-ops` / `-runbook` / `-troubleshooting` 结尾
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
backend-wiki/
├── index.md                    # 团队 Wiki 首页
├── log.md                      # 重要变更日志
├── README.md                   # Wiki 说明
├── CONTRIBUTING.md             # 贡献指南
└── pages/
    ├── project-backend-overview.md         # 后端技术导航
    ├── project-infra-overview.md           # 基础设施导航
    ├── project-ops-overview.md             # 运维手册导航
    ├── project-projects-overview.md        # 项目文档导航
    ├── project-onboarding-overview.md      # 新人入职导航
    ├── workspace-governance-overview.md    # 团队治理导航
    │
    ├── golang-best-practices.md            # Go 最佳实践
    ├── api-design-guide.md                 # API 设计指南
    ├── database-schema-design.md           # 数据库设计
    ├── microservices-architecture.md       # 微服务架构
    │
    ├── kubernetes-setup.md                 # K8s 配置
    ├── ci-cd-pipeline.md                   # CI/CD 流程
    ├── monitoring-alerting.md              # 监控告警
    │
    ├── redis-troubleshooting-ops.md        # Redis 排障
    ├── mysql-troubleshooting-ops.md        # MySQL 排障
    ├── deployment-runbook.md               # 部署手册
    ├── incident-response-ops.md            # 故障响应
    │
    ├── user-service-project.md             # 用户服务文档
    ├── payment-service-project.md          # 支付服务文档
    ├── notification-service-project.md     # 通知服务文档
    │
    ├── onboarding-day1.md                  # 入职第 1 天
    ├── onboarding-week1.md                 # 入职第 1 周
    ├── dev-environment-setup.md            # 开发环境搭建
    │
    └── code-review-guidelines.md           # Code Review 规范
```

---

## 第四步：真实页面示例

### 示例 1：导航页（project）

**文件**：`pages/project-ops-overview.md`

```markdown
---
title: "运维手册总览"
type: "project"
area: "operations"
tags: ["导航", "运维"]
updated: "2026-04-17"
owner: "张三（SRE）"
---

# 运维手册总览

## 🚨 紧急故障响应

**线上故障时先看这里！**

- [故障响应流程](./incident-response-ops.md) ⭐
- [值班手册](./oncall-runbook.md)
- [紧急联系人](./emergency-contacts.md)

## 🔧 常见问题排查

### 数据库
- [MySQL 慢查询排查](./mysql-troubleshooting-ops.md)
- [Redis 连接超时排查](./redis-troubleshooting-ops.md)
- [PostgreSQL 死锁排查](./postgres-troubleshooting-ops.md)

### 服务
- [API 超时排查](./api-timeout-ops.md)
- [内存泄漏排查](./memory-leak-ops.md)
- [CPU 飙高排查](./cpu-spike-ops.md)

### 基础设施
- [K8s Pod 重启排查](./k8s-pod-restart-ops.md)
- [负载均衡器故障](./lb-troubleshooting-ops.md)
- [网络连通性排查](./network-troubleshooting-ops.md)

## 📋 操作手册

### 部署
- [生产环境部署流程](./deployment-runbook.md)
- [回滚操作手册](./rollback-runbook.md)
- [灰度发布流程](./canary-deployment-runbook.md)

### 维护
- [数据库备份与恢复](./db-backup-restore-ops.md)
- [日志清理](./log-cleanup-ops.md)
- [证书更新](./cert-renewal-ops.md)

## 📊 监控与告警

- [监控大盘](https://grafana.company.com/dashboards)
- [告警规则配置](./alerting-rules.md)
- [PagerDuty 使用指南](./pagerduty-guide.md)

## 🔗 相关链接

- [基础设施文档](./project-infra-overview.md)
- [项目文档](./project-projects-overview.md)
- [团队值班表](./oncall-schedule.md)
```

---

### 示例 2：知识页（knowledge）

**文件**：`pages/api-design-guide.md`

```markdown
---
title: "API 设计指南"
type: "knowledge"
area: "backend"
tags: ["api", "restful", "设计规范"]
updated: "2026-04-17"
owner: "李四（架构师）"
---

# API 设计指南

## RESTful 设计原则

### 1. 使用名词而非动词

✅ **推荐**：
```
GET    /users          # 获取用户列表
GET    /users/123      # 获取单个用户
POST   /users          # 创建用户
PUT    /users/123      # 更新用户
DELETE /users/123      # 删除用户
```

❌ **不推荐**：
```
GET  /getUsers
POST /createUser
POST /updateUser
POST /deleteUser
```

### 2. 使用复数形式

✅ **推荐**：`/users`, `/orders`, `/products`

❌ **不推荐**：`/user`, `/order`, `/product`

### 3. 使用层级关系

```
GET /users/123/orders          # 获取用户的订单列表
GET /users/123/orders/456      # 获取用户的某个订单
POST /users/123/orders         # 为用户创建订单
```

## HTTP 状态码规范

| 状态码 | 含义 | 使用场景 |
|--------|------|----------|
| 200 | OK | 成功返回数据 |
| 201 | Created | 成功创建资源 |
| 204 | No Content | 成功但无返回内容（如删除） |
| 400 | Bad Request | 请求参数错误 |
| 401 | Unauthorized | 未认证 |
| 403 | Forbidden | 无权限 |
| 404 | Not Found | 资源不存在 |
| 409 | Conflict | 资源冲突（如重复创建） |
| 500 | Internal Server Error | 服务器错误 |

## 请求/响应格式

### 统一响应格式

```json
{
  "code": 0,
  "message": "success",
  "data": {
    "id": 123,
    "name": "张三",
    "email": "zhangsan@example.com"
  },
  "timestamp": "2026-04-17T10:30:00Z"
}
```

### 错误响应格式

```json
{
  "code": 40001,
  "message": "用户名已存在",
  "errors": [
    {
      "field": "username",
      "message": "username 'zhangsan' already exists"
    }
  ],
  "timestamp": "2026-04-17T10:30:00Z"
}
```

## 分页规范

### 请求参数

```
GET /users?page=1&page_size=20&sort=created_at&order=desc
```

### 响应格式

```json
{
  "code": 0,
  "message": "success",
  "data": {
    "items": [...],
    "pagination": {
      "page": 1,
      "page_size": 20,
      "total": 100,
      "total_pages": 5
    }
  }
}
```

## 版本控制

### 方式 1：URL 路径（推荐）

```
GET /v1/users
GET /v2/users
```

### 方式 2：请求头

```
GET /users
Header: API-Version: v1
```

## 认证与授权

### JWT Token

```
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

### API Key

```
X-API-Key: your-api-key-here
```

## 限流规范

### 响应头

```
X-RateLimit-Limit: 1000        # 每小时限制
X-RateLimit-Remaining: 999     # 剩余次数
X-RateLimit-Reset: 1618308000  # 重置时间（Unix 时间戳）
```

### 超限响应

```json
{
  "code": 42900,
  "message": "Rate limit exceeded",
  "retry_after": 3600
}
```

## 实战案例

### 用户服务 API

```
# 用户管理
GET    /v1/users              # 获取用户列表
GET    /v1/users/:id          # 获取用户详情
POST   /v1/users              # 创建用户
PUT    /v1/users/:id          # 更新用户
DELETE /v1/users/:id          # 删除用户

# 用户认证
POST   /v1/auth/login         # 登录
POST   /v1/auth/logout        # 登出
POST   /v1/auth/refresh       # 刷新 Token

# 用户订单
GET    /v1/users/:id/orders   # 获取用户订单列表
POST   /v1/users/:id/orders   # 创建订单
```

## 相关链接

- [Go API 实现示例](./golang-api-example.md)
- [API 测试规范](./api-testing-guide.md)
- [用户服务文档](./user-service-project.md)
```

---

### 示例 3：操作手册（ops）

**文件**：`pages/redis-troubleshooting-ops.md`

```markdown
---
title: "Redis 故障排查手册"
type: "ops"
area: "operations"
tags: ["redis", "troubleshooting", "database"]
updated: "2026-04-17"
owner: "王五（SRE）"
---

# Redis 故障排查手册

## 问题 1：Redis 连接超时

### 现象
应用日志出现：
```
Error: Redis connection timeout after 5000ms
ETIMEDOUT: Connection timed out
```

### 根因
1. Redis 服务未启动
2. 防火墙阻止了 6379 端口
3. Redis 配置的 `bind` 地址不正确
4. 网络延迟过高
5. Redis 连接数已满

### 处理法

#### 步骤 1：检查 Redis 服务状态

```bash
# 检查 Redis 进程
ps aux | grep redis

# 检查 Redis 服务状态
systemctl status redis

# 如果未启动，启动服务
systemctl start redis
```

#### 步骤 2：检查端口连通性

```bash
# 测试端口是否可达
telnet redis-host 6379

# 或使用 nc
nc -zv redis-host 6379

# 检查防火墙规则
sudo iptables -L -n | grep 6379
```

#### 步骤 3：检查 Redis 配置

```bash
# 查看 bind 配置
grep "^bind" /etc/redis/redis.conf

# 正确配置应该是：
# bind 0.0.0.0  # 允许所有 IP 连接
# 或
# bind 127.0.0.1 10.0.1.100  # 只允许特定 IP
```

#### 步骤 4：检查连接数

```bash
# 连接到 Redis
redis-cli

# 查看当前连接数
INFO clients

# 查看最大连接数配置
CONFIG GET maxclients

# 如果连接数已满，增加最大连接数
CONFIG SET maxclients 10000
```

#### 步骤 5：检查网络延迟

```bash
# 测试网络延迟
ping redis-host

# 测试 Redis 响应时间
redis-cli --latency -h redis-host

# 如果延迟过高，检查网络路由
traceroute redis-host
```

### 边界
- 适用于 Redis 5.0+
- 适用于 Linux 环境
- 需要 root 权限执行部分命令

---

## 问题 2：Redis 内存占用过高

### 现象
```
Redis 内存使用率 > 90%
OOM (Out of Memory) 错误
```

### 根因
1. 没有设置过期时间
2. 大 key 占用过多内存
3. 内存淘汰策略不合理
4. 内存碎片过多

### 处理法

#### 步骤 1：检查内存使用情况

```bash
redis-cli INFO memory

# 关键指标：
# used_memory: 实际使用内存
# used_memory_rss: 操作系统分配内存
# mem_fragmentation_ratio: 内存碎片率
```

#### 步骤 2：查找大 key

```bash
# 扫描大 key
redis-cli --bigkeys

# 或使用 RDB 工具分析
redis-rdb-tools /var/lib/redis/dump.rdb --command memory --bytes 1048576
```

#### 步骤 3：设置过期时间

```bash
# 查找没有过期时间的 key
redis-cli --scan --pattern '*' | while read key; do
  ttl=$(redis-cli TTL "$key")
  if [ "$ttl" = "-1" ]; then
    echo "$key has no expiration"
  fi
done

# 批量设置过期时间
redis-cli --scan --pattern 'cache:*' | xargs -L 1 redis-cli EXPIRE 3600
```

#### 步骤 4：配置内存淘汰策略

```bash
# 查看当前策略
redis-cli CONFIG GET maxmemory-policy

# 推荐策略：
# allkeys-lru: 淘汰最少使用的 key
# volatile-lru: 只淘汰设置了过期时间的 key
# allkeys-lfu: 淘汰最少访问的 key（Redis 4.0+）

# 设置策略
redis-cli CONFIG SET maxmemory-policy allkeys-lru

# 设置最大内存
redis-cli CONFIG SET maxmemory 4gb
```

#### 步骤 5：清理内存碎片

```bash
# Redis 4.0+ 支持自动碎片整理
redis-cli CONFIG SET activedefrag yes

# 手动触发（会阻塞）
redis-cli MEMORY PURGE
```

### 边界
- 适用于 Redis 4.0+
- 内存碎片整理会影响性能
- 大 key 删除可能导致阻塞

---

## 问题 3：Redis 主从同步延迟

### 现象
```
从库数据落后主库 > 10 秒
应用读取从库数据不一致
```

### 根因
1. 网络带宽不足
2. 主库写入压力过大
3. 从库性能不足
4. repl-backlog-size 太小

### 处理法

#### 步骤 1：检查同步状态

```bash
# 在主库执行
redis-cli INFO replication

# 关键指标：
# master_repl_offset: 主库偏移量
# slave0:offset: 从库偏移量
# 差值 = 同步延迟
```

#### 步骤 2：检查网络带宽

```bash
# 测试主从之间的网络带宽
iperf3 -s  # 在从库执行
iperf3 -c slave-host  # 在主库执行
```

#### 步骤 3：调整 repl-backlog-size

```bash
# 查看当前配置
redis-cli CONFIG GET repl-backlog-size

# 增加 backlog 大小（建议 256MB+）
redis-cli CONFIG SET repl-backlog-size 268435456
```

#### 步骤 4：优化主库写入

```bash
# 启用 AOF 重写压缩
redis-cli CONFIG SET auto-aof-rewrite-percentage 100
redis-cli CONFIG SET auto-aof-rewrite-min-size 64mb

# 调整 RDB 保存策略
redis-cli CONFIG SET save "900 1 300 10 60 10000"
```

### 边界
- 适用于 Redis 主从架构
- 需要监控网络带宽
- 可能需要升级硬件

---

## 快速诊断清单

```bash
# 1. 检查服务状态
systemctl status redis

# 2. 检查内存使用
redis-cli INFO memory | grep used_memory_human

# 3. 检查连接数
redis-cli INFO clients | grep connected_clients

# 4. 检查慢查询
redis-cli SLOWLOG GET 10

# 5. 检查主从同步
redis-cli INFO replication

# 6. 检查持久化
redis-cli INFO persistence
```

## 相关链接

- [Redis 监控配置](./redis-monitoring.md)
- [Redis 性能优化](./redis-performance-tuning.md)
- [基础设施总览](./project-infra-overview.md)
```

---

### 示例 4：项目文档（project）

**文件**：`pages/user-service-project.md`

```markdown
---
title: "用户服务文档"
type: "project"
area: "projects"
tags: ["microservice", "user", "golang"]
updated: "2026-04-17"
owner: "赵六（后端负责人）"
---

# 用户服务文档

## 服务概述

**服务名称**：user-service

**职责**：
- 用户注册、登录、登出
- 用户信息管理
- 用户权限验证
- 用户会话管理

**技术栈**：
- 语言：Go 1.21
- 框架：Gin
- 数据库：MySQL 8.0
- 缓存：Redis 7.0
- 消息队列：Kafka

## 架构设计

```
┌─────────────┐
│   API Gateway   │
└────────┬────────┘
         │
    ┌────▼────┐
    │ User Service │
    └────┬────┘
         │
    ┌────▼────┬────────┬────────┐
    │  MySQL  │ Redis  │ Kafka  │
    └─────────┴────────┴────────┘
```

## API 文档

### 用户注册

```
POST /v1/users/register
```

**请求体**：
```json
{
  "username": "zhangsan",
  "email": "zhangsan@example.com",
  "password": "password123"
}
```

**响应**：
```json
{
  "code": 0,
  "message": "success",
  "data": {
    "user_id": 123,
    "username": "zhangsan",
    "email": "zhangsan@example.com",
    "created_at": "2026-04-17T10:30:00Z"
  }
}
```

### 用户登录

```
POST /v1/users/login
```

**请求体**：
```json
{
  "username": "zhangsan",
  "password": "password123"
}
```

**响应**：
```json
{
  "code": 0,
  "message": "success",
  "data": {
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "expires_in": 3600
  }
}
```

## 数据库设计

### users 表

```sql
CREATE TABLE users (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  username VARCHAR(50) UNIQUE NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  status TINYINT DEFAULT 1 COMMENT '1:正常 2:禁用',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  INDEX idx_username (username),
  INDEX idx_email (email)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```

## 部署信息

### 生产环境

- **地址**：https://api.company.com/user-service
- **实例数**：3
- **负载均衡**：Nginx
- **监控**：https://grafana.company.com/d/user-service

### 测试环境

- **地址**：https://test-api.company.com/user-service
- **实例数**：1

## 依赖服务

- **MySQL**：user-db.prod.company.com:3306
- **Redis**：user-redis.prod.company.com:6379
- **Kafka**：kafka.prod.company.com:9092

## 监控告警

### 关键指标

- **QPS**：正常 < 1000，告警 > 5000
- **响应时间**：P99 < 200ms，告警 > 500ms
- **错误率**：正常 < 0.1%，告警 > 1%
- **CPU**：正常 < 70%，告警 > 90%
- **内存**：正常 < 80%，告警 > 95%

### 告警规则

- 错误率 > 1% 持续 5 分钟 → PagerDuty 通知值班人员
- 响应时间 P99 > 500ms 持续 5 分钟 → Slack 通知
- 服务不可用 → 立即 PagerDuty 通知

## 常见问题

### 问题 1：登录接口响应慢

**排查步骤**：
1. 检查 MySQL 慢查询日志
2. 检查 Redis 连接是否正常
3. 检查 JWT 生成是否耗时

**参考文档**：[API 超时排查](./api-timeout-ops.md)

### 问题 2：用户注册失败

**排查步骤**：
1. 检查用户名/邮箱是否重复
2. 检查数据库连接是否正常
3. 检查 Kafka 消息是否发送成功

## 相关链接

- [API 设计指南](./api-design-guide.md)
- [Go 最佳实践](./golang-best-practices.md)
- [部署手册](./deployment-runbook.md)
- [MySQL 排障手册](./mysql-troubleshooting-ops.md)
```

---

## 第五步：使用效果

### 新人入职
1. 打开 `index.md`
2. 点击"新人入职"
3. 按照 `onboarding-day1.md` 一步步操作
4. 1 天内完成环境搭建和基础了解

### 线上故障
1. 打开 `project-ops-overview.md`
2. 找到对应的排障手册
3. 按照"现象 / 根因 / 处理法 / 边界"快速定位问题
4. 平均故障恢复时间从 30 分钟降到 10 分钟

### 日常开发
1. 需要查 API 规范 → `api-design-guide.md`
2. 需要查某个服务 → `user-service-project.md`
3. 需要查排障手册 → `redis-troubleshooting-ops.md`
4. 所有文档都能在 3 次点击内找到

---

## 维护规则

### 文档更新
- 每次上线新功能，必须更新对应的项目文档
- 每次修复线上问题，必须更新排障手册
- 每月审计一次，清理过期文档

### 责任人
- 每个文档必须有 `owner` 字段
- owner 负责文档的准确性和及时更新
- 文档过期超过 3 个月，自动提醒 owner

### 审计
- 每月运行一次 `knowledge-base-audit`
- 检查死链、孤立页、缺失 frontmatter
- 检查是否有临时内容混入知识库

---

## 总结

通过这套工具，团队 Wiki 从"找不到文档"变成了"3 次点击找到任何文档"，新人入职时间从 3 天缩短到 1 天，线上故障恢复时间从 30 分钟缩短到 10 分钟。
