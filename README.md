# 🖥️ OpenClaw Monitoring Dashboard

这是主页面。

这个仓库现在的主要用途是：
- 监控 OpenClaw 当前运行状态
- 查看模型 / 配额 / Gateway / cron 情况
- 汇总最近的自动化报告
- 作为 GitHub 上的可视化快照中心

报告页仍然保留，但现在属于**次要页面**。

---

## 🚀 主入口

### 系统监控
- [System Dashboard](status/system-dashboard.md)
- [Session Status](status/openclaw-session-status.md)

### 报告入口（次要页面）
- [🌅 早报](morning-briefs/latest-morning.md)
- [🌙 复盘](evening-reviews/latest-evening.md)
- [🛡️ 安全笔记](weekly-security/latest-security.md)
- [🔎 开源观察](open-source-watch/latest-watch.md)

---

## 📌 当前定位

### 主页面
- `status/system-dashboard.md`
- `status/openclaw-session-status.md`

### 次要页面
- `morning-briefs/`
- `evening-reviews/`
- `weekly-security/`
- `open-source-watch/`

---

## 📁 仓库结构

```text
daily-reports/
├── README.md
├── SETUP_GUIDE.md
├── status/
├── morning-briefs/
├── evening-reviews/
├── weekly-security/
├── open-source-watch/
└── scripts/
```

---

## 🔄 更新机制

### 监控页
- 每 30 分钟自动刷新一次
- 用于查看系统快照

### 报告页
- 按各自定时任务刷新
- 用于查看详细内容和历史归档

---

## ℹ️ 说明

- 这个仓库已经从“报告仓库”升级为“监控 + 报告中心”
- 监控页是主页面
- 报告页是次要内容页
- GitHub 更适合做**准实时快照**，不适合做严格实时面板

---

**状态**：运行正常  
**最后更新**：2026-03-20 12:46  
**维护者**：OpenClaw 自动化系统
