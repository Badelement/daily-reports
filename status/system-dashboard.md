# 🖥️ OpenClaw System Dashboard

主监控页。这个页面优先于报告页，用于集中查看 OpenClaw 当前运行状态。

**更新时间**: 2026-03-20 12:47:06 (Asia/Shanghai)

---

## 1. 当前系统概览

### 最新内容入口
- 最新早报: [2026-03-20-morning.md](morning-briefs/2026-03-20-morning.md)
- 最新复盘: [2026-03-19-evening.md](evening-reviews/2026-03-19-evening.md)
- 最新安全笔记: [2026-03-15-security.md](weekly-security/2026-03-15-security.md)
- 最新开源观察: [2026-03-19-watch.md](open-source-watch/2026-03-19-watch.md)

### 报告库存
- 早报数量: 8
- 复盘数量: 8
- 安全笔记数量: 2
- 开源观察数量: 6

---

## 2. OpenClaw 会话状态

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
│ Gateway service │ LaunchAgent installed · loaded · running (pid 5165, state active)                                  │
│ Node service    │ LaunchAgent installed · not loaded · unknown                                                       │
│ Agents          │ 1 · no bootstrap files · sessions 11 · default main active 1m ago                                  │
│ Memory          │ enabled (plugin memory-core) · unavailable                                                         │
│ Probes          │ skipped (use --deep)                                                                               │
│ Events          │ none                                                                                               │
│ Heartbeat       │ 30m (main)                                                                                         │
│ Sessions        │ 11 active · default deepseek-chat (128k ctx) · ~/.openclaw/agents/main/sessions/sessions.json      │
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
│ agent:main:telegram:direct:7310…               │ direct │ 1m ago  │ gpt-5.4       │ 182k/272k (67%) · 🗄️ 99% cached  │
│ agent:main:main                                │ direct │ 29m ago │ deepseek-chat │ 46k/128k (36%) · 🗄️ 100% cached  │
│ agent:main:cron:9fea7709-95fe-4…               │ direct │ 4h ago  │ deepseek-chat │ 20k/128k (16%) · 🗄️ 1163% cached │
│ agent:main:cron:9fea7709-95fe-4…               │ direct │ 4h ago  │ deepseek-chat │ 20k/128k (16%) · 🗄️ 1163% cached │
│ agent:main:cron:bbbba49f-c5d4-4…               │ direct │ 15h ago │ deepseek-chat │ 15k/128k (11%) · 🗄️ 743% cached  │
│ agent:main:cron:bbbba49f-c5d4-4…               │ direct │ 15h ago │ deepseek-chat │ 15k/128k (11%) · 🗄️ 743% cached  │
│ agent:main:cron:ef3bb9db-238b-4…               │ direct │ 18h ago │ deepseek-chat │ 17k/128k (13%) · 🗄️ 1365% cached │
│ agent:main:cron:ef3bb9db-238b-4…               │ direct │ 18h ago │ deepseek-chat │ 17k/128k (13%) · 🗄️ 1365% cached │
│ agent:main:cron:9fea7709-95fe-4…               │ direct │ 20h ago │ deepseek-chat │ 13k/128k (10%) · 🗄️ 1307% cached │
│ agent:main:cron:6b5c0215-c791-4…               │ direct │ 5d ago  │ deepseek-chat │ 17k/128k (14%) · 🗄️ 1173% cached │
└────────────────────────────────────────────────┴────────┴─────────┴───────────────┴──────────────────────────────────┘

FAQ: https://docs.openclaw.ai/faq
Troubleshooting: https://docs.openclaw.ai/troubleshooting

Next steps:
  Need to share?      openclaw status --all
  Need to debug live? openclaw logs --follow
  Fix reachability first: openclaw gateway probe
```

---

## 3. Gateway 状态

```text
Service: LaunchAgent (loaded)
File logs: /tmp/openclaw/openclaw-2026-03-20.log
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

## 4. Cron 状态

```text
ID                                   Name                     Schedule                         Next       Last       Status    Target    Agent ID   Model               
ef3bb9db-238b-4e6b-9dda-dbc79e87a541 open-source-watch-for... cron 15 19 * * * @ Asia/Shang... in 6h      18h ago    ok        isolated  main       deepseek/deepseek...
bbbba49f-c5d4-4690-b1be-3616a294cc26 daily-self-iteration     cron 35 21 * * * @ Asia/Shang... in 9h      15h ago    ok        isolated  -          deepseek/deepseek...
9fea7709-95fe-462f-b38c-752efed139b0 morning-intel-brief      cron 20 8 * * * @ Asia/Shangh... in 20h     4h ago     ok        isolated  -          deepseek/deepseek...
6b5c0215-c791-4e55-bcd6-64abd24afbb9 weekly-agent-security... cron 30 20 * * 0 @ Asia/Shang... in 2d      5d ago     ok        isolated  main       deepseek/deepseek...
```

---

## 5. 仓库最近提交

```text
9f79d1d feat: add OpenClaw session status page to dashboard
94b1d16 fix: replace latest symlinks with real markdown files
a87a133 docs: turn daily-reports homepage into a dashboard
a6102e5 fix: sync open-source-watch into daily reports
63ab3f4 Batch sync reports - 2026-03-20 12:31:19
```

---

## 6. 次要页面入口

### 报告页
- [早报目录](../morning-briefs/)
- [复盘目录](../evening-reviews/)
- [安全笔记目录](../weekly-security/)
- [开源观察目录](../open-source-watch/)

### 状态页
- [会话状态](openclaw-session-status.md)

---

## 说明

- 此页为主页面快照
- 每 30 分钟自动刷新一次
- 报告目录为次要页面，用于看详细内容和历史存档
