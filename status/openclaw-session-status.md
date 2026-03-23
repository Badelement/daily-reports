# OpenClaw Session Status

更新时间：2026-03-23 14:47 (Asia/Shanghai)

## 当前主会话状态

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
│ Update          │ pnpm · npm latest 2026.3.13                                                                        │
│ Gateway         │ local · ws://127.0.0.1:18789 (local loopback) · unreachable (missing scope: operator.read)         │
│ Gateway service │ LaunchAgent installed · loaded · running (pid 69349, state active)                                 │
│ Node service    │ LaunchAgent installed · not loaded · unknown                                                       │
│ Agents          │ 1 · no bootstrap files · sessions 61 · default main active 1m ago                                  │
│ Memory          │ enabled (plugin memory-core) · unavailable                                                         │
│ Probes          │ skipped (use --deep)                                                                               │
│ Events          │ none                                                                                               │
│ Heartbeat       │ 30m (main)                                                                                         │
│ Sessions        │ 61 active · default deepseek-chat (128k ctx) · ~/.openclaw/agents/main/sessions/sessions.json      │
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
│ agent:main:cron:d2e5fda8-439e-4…                │ direct │ 1m ago  │ deepseek-chat │ 16k/128k (13%) · 🗄️ 736% cached │
│ agent:main:cron:d2e5fda8-439e-4…                │ direct │ 1m ago  │ deepseek-chat │ 16k/128k (13%) · 🗄️ 736% cached │
│ agent:main:main                                 │ direct │ 1m ago  │ deepseek-chat │ 63k/128k (49%) · 🗄️ 99% cached  │
│ agent:main:cron:d2e5fda8-439e-4…                │ direct │ 31m ago │ deepseek-chat │ 16k/128k (13%) · 🗄️ 736% cached │
│ agent:main:cron:d2e5fda8-439e-4…                │ direct │ 1h ago  │ deepseek-chat │ 16k/128k (13%) · 🗄️ 829% cached │
│ agent:main:cron:d2e5fda8-439e-4…                │ direct │ 2h ago  │ deepseek-chat │ 15k/128k (12%) · 🗄️ 795% cached │
│ agent:main:cron:d2e5fda8-439e-4…                │ direct │ 2h ago  │ deepseek-chat │ 18k/128k (14%) · 🗄️ 802% cached │
│ agent:main:cron:d2e5fda8-439e-4…                │ direct │ 3h ago  │ deepseek-chat │ 16k/128k (12%) · 🗄️ 648% cached │
│ agent:main:cron:d2e5fda8-439e-4…                │ direct │ 3h ago  │ deepseek-chat │ 18k/128k (14%) · 🗄️ 803% cached │
│ agent:main:cron:d2e5fda8-439e-4…                │ direct │ 4h ago  │ deepseek-chat │ 15k/128k (12%) · 🗄️ 793% cached │
└─────────────────────────────────────────────────┴────────┴─────────┴───────────────┴─────────────────────────────────┘

FAQ: https://docs.openclaw.ai/faq
Troubleshooting: https://docs.openclaw.ai/troubleshooting

Next steps:
  Need to share?      openclaw status --all
  Need to debug live? openclaw logs --follow
  Fix reachability first: openclaw gateway probe
```

## 状态摘要

- **系统状态**: 正常
- **Gateway 服务**: 运行中 (pid 69349)
- **Telegram 通道**: 正常
- **活跃会话**: 61 个
- **主会话**: 1 分钟前活跃
- **安全审计**: 0 个关键问题，0 个警告，1 个信息项
- **心跳频率**: 30 分钟

## 注意事项

1. Gateway 仅监听本机回环地址 (127.0.0.1:18789)
2. Node 服务未加载
3. Memory 插件已启用但当前不可用
4. 会话缓存率较高，部分会话达到 800%+ 缓存

## 相关链接

- [返回系统仪表板](system-dashboard.md)
- [返回仓库首页](../README.md)