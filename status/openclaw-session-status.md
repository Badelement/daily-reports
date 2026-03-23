# OpenClaw Session Status

更新时间：2026-03-23 16:18 (Asia/Shanghai)

## 当前主会话状态

- **模型**：`Key`
- **认证方式**：`telegram`
- **当前会话**：`agent:main:cron:d2e5fda8-439e-4…`
- **运行模式**：`direct`
- **Reasoning/Think**：`off`
- **权限级别**：`normal`

## 使用情况

- **当前上下文占用**：`16k/128k (约 13%)`
- **缓存命中率**：`832%`
- **缓存量**：`16k cached`

## 原始状态快照

```text
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
┌────────────────────────────────────────────────┬────────┬─────────┬───────────────┬──────────────────────────────────┐
│ Key                                            │ Kind   │ Age     │ Model         │ Tokens                           │
├────────────────────────────────────────────────┼────────┼─────────┼───────────────┼──────────────────────────────────┤
│ agent:main:cron:d2e5fda8-439e-4…               │ direct │ 1m ago  │ deepseek-chat │ 16k/128k (13%) · 🗄️ 920% cached  │
│ agent:main:cron:d2e5fda8-439e-4…               │ direct │ 1m ago  │ deepseek-chat │ 16k/128k (13%) · 🗄️ 920% cached  │
│ agent:main:main                                │ direct │ 2m ago  │ deepseek-chat │ 67k/128k (53%) · 🗄️ 99% cached   │
│ agent:main:cron:d2e5fda8-439e-4…               │ direct │ 31m ago │ deepseek-chat │ 16k/128k (13%) · 🗄️ 920% cached  │
│ agent:main:cron:d2e5fda8-439e-4…               │ direct │ 1h ago  │ deepseek-chat │ 15k/128k (12%) · 🗄️ 801% cached  │
│ agent:main:cron:d2e5fda8-439e-4…               │ direct │ 2h ago  │ deepseek-chat │ 19k/128k (15%) · 🗄️ 1104% cached │
│ agent:main:cron:d2e5fda8-439e-4…               │ direct │ 2h ago  │ deepseek-chat │ 16k/128k (13%) · 🗄️ 736% cached  │
│ agent:main:cron:d2e5fda8-439e-4…               │ direct │ 3h ago  │ deepseek-chat │ 16k/128k (13%) · 🗄️ 829% cached  │
│ agent:main:cron:d2e5fda8-439e-4…               │ direct │ 3h ago  │ deepseek-chat │ 15k/128k (12%) · 🗄️ 795% cached  │
│ agent:main:cron:d2e5fda8-439e-4…               │ direct │ 4h ago  │ deepseek-chat │ 18k/128k (14%) · 🗄️ 802% cached  │
└────────────────────────────────────────────────┴────────┴─────────┴───────────────┴──────────────────────────────────┘

FAQ: https://docs.openclaw.ai/faq
Troubleshooting: https://docs.openclaw.ai/troubleshooting

Next steps:
  Need to share?      openclaw status --all
  Need to debug live? openclaw logs --follow
  Fix reachability first: openclaw gateway probe
```

---

## 说明

- 此文件为 OpenClaw 会话状态快照
- 每 30 分钟随仪表板一起更新
- 用于追踪会话状态和资源使用情况
- 原始状态快照可用于故障排查
