---
title: 2026-03-19 开源观察
type: watch
date: 2026-03-19
tags: [openclaw, automation, open-source]
synced_at: 2026-03-20 12:31:19
synced_by: cron_runs_sync
---

基于我的搜索和分析，我发现今天确实有一个值得关注的新动态：

**发现了什么**：OpenClaw 2026.3.13 版本已发布，修复了三个关键bug：1) 中英文混合文本自动空格导致路径错误，2) 长会话中嵌入式运行失败问题，3) `openclaw gateway start` 无响应问题。

**为什么对朽木有用**：你正在Mac mini上运行本地OpenClaw，这些bug修复直接影响系统稳定性。特别是路径错误问题可能导致技能加载失败，gateway启动问题会影响服务可用性。

**如果要试，最小起步方式**：运行 `openclaw --version` 检查当前版本，如果是旧版，执行 `npm update -g openclaw` 升级，然后 `openclaw gateway restart` 重启服务。

**额外发现**：ClawHub新增了"polymarket-elon-tweets"技能(v1.1.2)，但这对你的自动化环境价值有限，建议关注更实用的GitHub Workflow技能(评分3.493)，用于优化CI/CD管道。
