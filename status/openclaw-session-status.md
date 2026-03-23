# OpenClaw Session Status

更新时间：2026-03-23 20:48 (Asia/Shanghai)

## 当前主会话状态

- **模型**：`deepseek/deepseek-chat`
- **认证方式**：`telegram`
- **当前会话**：`agent:main:cron:d2e5fda8-439e-44e2-b475-cdfb4a96c0b0`
- **运行模式**：`direct`
- **上下文使用**：`13k/128k (10%) · 🗄️ 764% cached`
- **会话年龄**：`1m ago`

## 系统概览

```
OpenClaw status

Overview
┌─────────────────┬────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ Item            │ Value                                                                                              │
├─────────────────┼────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ Dashboard       │ disabled                                                                                           │
│ OS              │ macos 26.3.1 (arm64) · node 22.22.1                                                                │
│ Tailscale       │ off                                                                                                │
│ Channel         │ stable (default)                                                                                   │
│ Update          │ available · pnpm · npm update 2026.3.22                                                            │
│ Gateway         │ local · ws://127.0.0.1:18789 (local loopback) · unreachable (missing scope: operator.read)         │
│ Gateway service │ LaunchAgent installed · loaded · running (pid 69349, state active)                                 │
│ Node service    │ LaunchAgent installed · not loaded · unknown                                                       │
│ Agents          │ 1 · no bootstrap files · sessions 60 · default main active 1m ago                                  │
│ Memory          │ enabled (plugin memory-core) · unavailable                                                         │
│ Probes          │ skipped (use --deep)                                                                               │
│ Events          │ none                                                                                               │
│ Heartbeat       │ 30m (main)                                                                                         │
│ Sessions        │ 60 active · default deepseek-chat (128k ctx) · ~/.openclaw/agents/main/sessions/sessions.json      │
└─────────────────┴────────────────────────────────────────────────────────────────────────────────────────────────────┘

Security audit
Summary: 0 critical · 0 warn · 1 info
No critical or warn findings detected.
Full report: openclaw security audit
Deep probe: openclaw security audit --deep

Channels
┌──────────┬─────────┬────────┬────────────────────────────────────────────────────────────────────────────────────────┐
│ Channel  │ Enabled │ State  │ Detail                                                                                 │
├──────────┼─────────┼────────┼────────────────────────────────────────────────────────────────────────────────────────┤
│ Telegram │ ON      │ OK     │ token config (8672…S1_g · len 46) · accounts 1/1                                       │
└──────────┴─────────┴────────┴────────────────────────────────────────────────────────────────────────────────────────┘

Sessions
┌─────────────────────────────────────────────────┬────────┬─────────┬───────────────┬─────────────────────────────────┐
│ Key                                             │ Kind   │ Age     │ Model         │ Tokens                          │
├─────────────────────────────────────────────────┼────────┼─────────┼───────────────┼─────────────────────────────────┤
│ agent:main:cron:d2e5fda8-439e-4…                │ direct │ 1m ago  │ deepseek-chat │ 13k/128k (10%) · 🗄️ 764% cached │
│ agent:main:cron:d2e5fda8-439e-4…                │ direct │ 1m ago  │ deepseek-chat │ 13k/128k (10%) · 🗄️ 764% cached │
│ agent:main:main                                 │ direct │ 2m ago  │ deepseek-chat │ 85k/128k (67%) · 🗄️ 16% cached  │
│ agent:main:telegram:direct:7310…                │ direct │ 29m ago │ deepseek-chat │ 19k/128k (14%) · 🗄️ 41% cached  │
│ agent:main:cron:d2e5fda8-439e-4…                │ direct │ 31m ago │ deepseek-chat │ 13k/128k (10%) · 🗄️ 764% cached │
│ agent:main:cron:d2e5fda8-439e-4…                │ direct │ 1h ago  │ deepseek-chat │ 15k/128k (12%) · 🗄️ 787% cached │
│ agent:main:cron:d2e5fda8-439e-4…                │ direct │ 2h ago  │ deepseek-chat │ 13k/128k (10%) · 🗄️ 765% cached │
│ agent:main:cron:ef3bb9db-238b-4…                │ direct │ 2h ago  │ deepseek-chat │ 12k/128k (9%) · 🗄️ 946% cached  │
│ agent:main:cron:ef3bb9db-238b-4…                │ direct │ 2h ago  │ deepseek-chat │ 12k/128k (9%) · 🗄️ 946% cached  │
│ agent:main:cron:d2e5fda8-439e-4…                │ direct │ 2h ago  │ deepseek-chat │ 16k/128k (12%) · 🗄️ 568% cached │
└─────────────────────────────────────────────────┴────────┴─────────┴───────────────┴─────────────────────────────────┘
```

## 状态分析

### 正常状态
1. ✅ Gateway 服务正常运行 (pid 69349, state active)
2. ✅ Telegram 通道正常连接
3. ✅ 安全审计无严重问题 (0 critical · 0 warn)
4. ✅ 主会话活跃 (1m ago)

### 需要注意
1. ⚠️ Gateway 仅监听本地回环地址 (ws://127.0.0.1:18789)
2. ⚠️ 有可用更新 (npm update 2026.3.22)
3. ⚠️ Node 服务未加载 (not loaded · unknown)
4. ⚠️ Memory 插件状态为 unavailable

### 会话统计
- 活跃会话总数：60
- 最近10个会话中，大部分为 cron 任务
- 主会话上下文使用率：67% (85k/128k)
- 当前 cron 任务上下文使用率：10% (13k/128k)

## 建议操作

1. **考虑更新**：运行 `openclaw update` 获取最新版本
2. **检查内存插件**：确认 memory-core 插件配置是否正确
3. **监控会话增长**：60个活跃会话可能偏高，考虑清理旧会话
4. **检查 Node 服务**：确认 Node 服务为何未加载

---

*此状态文件由 daily-reports dashboard 刷新任务自动更新*
*刷新频率：每30分钟*