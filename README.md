# 📊 daily-reports

OpenClaw 自动化**报告与状态快照**仓库。

这个仓库现在承载两类内容：
- **reports**：早报、晚间复盘、每周安全笔记、开源观察
- **status**：系统 dashboard、会话状态、运行快照

---

## 快速入口

### 主入口
- [系统 Dashboard](status/system-dashboard.md)

### 最新报告
- [最新早报](morning-briefs/latest-morning.md)
- [最新复盘](evening-reviews/latest-evening.md)
- [最新安全笔记](weekly-security/latest-security.md)
- [最新开源观察](open-source-watch/latest-watch.md)

---

## 仓库结构

```text
daily-reports/
├── README.md
├── SETUP_GUIDE.md
├── morning-briefs/       # 每日早报
├── evening-reviews/      # 晚间复盘
├── weekly-security/      # 每周安全笔记
├── open-source-watch/    # 开源观察
├── status/               # dashboard 与系统状态快照
└── scripts/              # 推送、同步、dashboard 生成脚本
```

---

## 自动更新内容

### 报告类
- 早报
- 晚间复盘
- 每周安全笔记
- 开源观察

### 状态类
- Dashboard 总览页
- OpenClaw 会话状态快照
- 仓库状态摘要

---

## 使用说明

### 网页查看
直接从仓库首页进入，推荐顺序：
1. 先看 [系统 Dashboard](status/system-dashboard.md)
2. 再看各类最新报告

### 本地查看
```bash
git clone https://github.com/Badelement/daily-reports.git
cd daily-reports
git pull origin main
```

### 手动检查同步状态
```bash
cd ~/.openclaw/workspace/daily-reports
git log --oneline -5
git status
```

---

## 维护说明

- 这个仓库已经不只是“早报仓库”
- 首页负责导航，详细内容放在各子目录
- dashboard 负责回答“现在系统怎么样”
- 报告目录负责回答“最近发生了什么”

---

**最后更新**: 2026-03-21
**维护者**: OpenClaw 自动化系统
**状态**: 🟢 运行中
