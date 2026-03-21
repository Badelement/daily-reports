# 🖥️ OpenClaw System Dashboard

主监控页。用于集中查看 OpenClaw 当前运行状态，并作为这个仓库的状态入口页。

**更新时间**: 2026-03-22 05:47:56 (Asia/Shanghai)

---

## 1. 当前系统概览

### 最新内容入口
- 最新早报: [2026-03-21-morning.md](../morning-briefs/2026-03-21-morning.md)
- 最新复盘: [2026-03-19-evening.md](../evening-reviews/2026-03-19-evening.md)
- 最新安全笔记: [2026-03-15-security.md](../weekly-security/2026-03-15-security.md)
- 最新开源观察: [2026-03-19-watch.md](../open-source-watch/2026-03-19-watch.md)

### 报告库存
- 早报数量: 9
- 复盘数量: 8
- 安全笔记数量: 2
- 开源观察数量: 6

---

## 2. 异常状态摘要

- 当前未发现明显异常

---

## 3. OpenClaw 会话状态

### 中文摘要
- Gateway 服务：运行中
- Telegram 通道：正常
- 活跃会话数：42
- 心跳频率：30m (main)

### 原始状态
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
│ Agents          │ 1 · no bootstrap files · sessions 42 · default main active just now                                │
│ Memory          │ enabled (plugin memory-core) · unavailable                                                         │
│ Probes          │ skipped (use --deep)                                                                               │
│ Events          │ none                                                                                               │
│ Heartbeat       │ 30m (main)                                                                                         │
│ Sessions        │ 42 active · default deepseek-chat (128k ctx) · ~/.openclaw/agents/main/sessions/sessions.json      │
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
┌───────────────────────────────────────────────┬────────┬──────────┬───────────────┬──────────────────────────────────┐
│ Key                                           │ Kind   │ Age      │ Model         │ Tokens                           │
├───────────────────────────────────────────────┼────────┼──────────┼───────────────┼──────────────────────────────────┤
│ agent:main:cron:d2e5fda8-439e-4…              │ direct │ just now │ deepseek-chat │ 15k/128k (11%) · 🗄️ 816% cached  │
│ agent:main:cron:d2e5fda8-439e-4…              │ direct │ just now │ deepseek-chat │ 15k/128k (11%) · 🗄️ 816% cached  │
│ agent:main:main                               │ direct │ 9m ago   │ deepseek-chat │ 68k/128k (53%) · 🗄️ 100% cached  │
│ agent:main:cron:d2e5fda8-439e-4…              │ direct │ 30m ago  │ deepseek-chat │ 15k/128k (11%) · 🗄️ 816% cached  │
│ agent:main:cron:d2e5fda8-439e-4…              │ direct │ 1h ago   │ deepseek-chat │ 16k/128k (13%) · 🗄️ 880% cached  │
│ agent:main:cron:d2e5fda8-439e-4…              │ direct │ 2h ago   │ deepseek-chat │ 17k/128k (13%) · 🗄️ 955% cached  │
│ agent:main:cron:d2e5fda8-439e-4…              │ direct │ 2h ago   │ deepseek-chat │ 16k/128k (13%) · 🗄️ 1008% cached │
│ agent:main:cron:d2e5fda8-439e-4…              │ direct │ 3h ago   │ deepseek-chat │ 15k/128k (11%) · 🗄️ 818% cached  │
│ agent:main:cron:d2e5fda8-439e-4…              │ direct │ 3h ago   │ deepseek-chat │ 15k/128k (11%) · 🗄️ 817% cached  │
│ agent:main:cron:d2e5fda8-439e-4…              │ direct │ 4h ago   │ deepseek-chat │ 22k/128k (17%) · 🗄️ 931% cached  │
└───────────────────────────────────────────────┴────────┴──────────┴───────────────┴──────────────────────────────────┘

FAQ: https://docs.openclaw.ai/faq
Troubleshooting: https://docs.openclaw.ai/troubleshooting

Next steps:
  Need to share?      openclaw status --all
  Need to debug live? openclaw logs --follow
  Fix reachability first: openclaw gateway probe
```

---

## 4. Gateway 状态

### 中文摘要
- Gateway 服务已加载
- 当前仅监听本机回环地址
- 监听端口：18789
- OpenClaw 内建 dashboard：关闭

### 原始状态
```text
Service: LaunchAgent (loaded)
File logs: /tmp/openclaw/openclaw-2026-03-22.log
Command: /Users/badelement/.local/node-v22.22.1-darwin-arm64/bin/node /Users/badelement/.npm-global/lib/node_modules/openclaw/dist/index.js gateway --port 18789
Service file: ~/Library/LaunchAgents/ai.openclaw.gateway.plist
Service env: OPENCLAW_GATEWAY_PORT=18789

Config (cli): ~/.openclaw/openclaw.json
Config (service): ~/.openclaw/openclaw.json

Gateway: bind=loopback (127.0.0.1), port=18789 (service args)
Probe target: ws://127.0.0.1:18789
Dashboard: disabled
```

---

## 5. Cron 状态

### 中文摘要
- 定时任务数量：5
- 最近状态正常的任务：4/5
- dashboard 刷新任务：已在列表中

### 原始状态
```text
ID                                   Name                     Schedule                         Next       Last       Status    Target    Agent ID   Model               
d2e5fda8-439e-44e2-b475-cdfb4a96c0b0 daily-reports-dashboa... every 30m                        <1m ago    30m ago    running   isolated  main       deepseek/deepseek...
9fea7709-95fe-462f-b38c-752efed139b0 morning-intel-brief      cron 20 8 * * * @ Asia/Shangh... in 3h      21h ago    ok        isolated  -          deepseek/deepseek...
ef3bb9db-238b-4e6b-9dda-dbc79e87a541 open-source-watch-for... cron 15 19 * * * @ Asia/Shang... in 13h     11h ago    ok        isolated  main       deepseek/deepseek...
6b5c0215-c791-4e55-bcd6-64abd24afbb9 weekly-agent-security... cron 30 20 * * 0 @ Asia/Shang... in 15h     6d ago     ok        isolated  main       deepseek/deepseek...
bbbba49f-c5d4-4690-b1be-3616a294cc26 daily-self-iteration     cron 35 21 * * * @ Asia/Shang... in 16h     8h ago     ok        isolated  -          deepseek/deepseek...
```

---

## 6. 仓库状态

### 中文摘要
- 最近一次提交：8e27ef3 chore: update system dashboard status snapshot [cron:d2e5fda8-439e-44e2-b475-cdfb4a96c0b0]
- 工作区状态：干净

### 最近提交
```text
8e27ef3 chore: update system dashboard status snapshot [cron:d2e5fda8-439e-44e2-b475-cdfb4a96c0b0]
b02c6ee chore: update system dashboard snapshot [cron:d2e5fda8-439e-44e2-b475-cdfb4a96c0b0]
e683b53 chore: update system dashboard snapshot [cron:d2e5fda8-439e-44e2-b475-cdfb4a96c0b0]
052912a 🔄 dashboard refresh: 2026-03-22 03:47
d2817bc dashboard: auto-update status snapshot at 2026-03-22 03:18:14
```

### 工作区状态
```text
working tree clean
```

---

## 7. 次要页面入口

### 报告页
- [早报目录](../morning-briefs/)
- [复盘目录](../evening-reviews/)
- [安全笔记目录](../weekly-security/)
- [开源观察目录](../open-source-watch/)

### 状态页
- [会话状态](openclaw-session-status.md)
- [仓库首页](../README.md)

---

## 说明

- 此页为状态总览页
- 每 30 分钟自动刷新一次
- 报告目录用于查看详细内容和历史存档
- “异常状态摘要”用于快速定位需关注问题
