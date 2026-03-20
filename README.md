# 📊 Daily Reports Dashboard

OpenClaw 自动化汇报同步仓库。

这是一个统一汇总多个定时任务产物的仓库，目前已接通：
- 🌅 每日早报
- 🌙 晚间复盘
- 🛡️ 每周安全笔记
- 🔎 开源观察

---

## 🚀 快速入口

| 类型 | 最新入口 | 目录 |
|---|---|---|
| 🌅 早报 | [latest-morning.md](morning-briefs/latest-morning.md) | [morning-briefs/](morning-briefs/) |
| 🌙 复盘 | [latest-evening.md](evening-reviews/latest-evening.md) | [evening-reviews/](evening-reviews/) |
| 🛡️ 安全笔记 | [latest-security.md](weekly-security/latest-security.md) | [weekly-security/](weekly-security/) |
| 🔎 开源观察 | [latest-watch.md](open-source-watch/latest-watch.md) | [open-source-watch/](open-source-watch/) |

如果首页看起来内容不多，请直接点击上面对应目录。

---

## 📁 当前仓库结构

```text
daily-reports/
├── README.md
├── SETUP_GUIDE.md
├── morning-briefs/
├── evening-reviews/
├── weekly-security/
├── open-source-watch/
└── scripts/
```

---

## 🗂️ 当前已同步内容

### 🌅 早报
- [2026-03-14](morning-briefs/2026-03-14-morning.md)
- [2026-03-15](morning-briefs/2026-03-15-morning.md)
- [2026-03-16](morning-briefs/2026-03-16-morning.md)
- [2026-03-17](morning-briefs/2026-03-17-morning.md)
- [2026-03-18](morning-briefs/2026-03-18-morning.md)
- [2026-03-19](morning-briefs/2026-03-19-morning.md)
- [2026-03-20](morning-briefs/2026-03-20-morning.md)

### 🌙 晚间复盘
- [2026-03-13](evening-reviews/2026-03-13-evening.md)
- [2026-03-14](evening-reviews/2026-03-14-evening.md)
- [2026-03-15](evening-reviews/2026-03-15-evening.md)
- [2026-03-16](evening-reviews/2026-03-16-evening.md)
- [2026-03-17](evening-reviews/2026-03-17-evening.md)
- [2026-03-18](evening-reviews/2026-03-18-evening.md)
- [2026-03-19](evening-reviews/2026-03-19-evening.md)

### 🛡️ 每周安全笔记
- [2026-03-15](weekly-security/2026-03-15-security.md)

### 🔎 开源观察
- [2026-03-15](open-source-watch/2026-03-15-watch.md)
- [2026-03-16](open-source-watch/2026-03-16-watch.md)
- [2026-03-17](open-source-watch/2026-03-17-watch.md)
- [2026-03-18](open-source-watch/2026-03-18-watch.md)
- [2026-03-19](open-source-watch/2026-03-19-watch.md)

---

## 🔄 同步机制

### 自动流程
1. OpenClaw 定时任务生成对应内容
2. 内容保存到本地工作目录 / 或从 cron 历史回填
3. 自动同步到 `daily-reports`
4. 自动提交并推送到 GitHub

### 当前已接通
- 早报：已接通
- 复盘：已接通
- 安全笔记：已接通
- 开源观察：已接通

---

## 💻 本地查看

```bash
git clone https://github.com/Badelement/daily-reports.git
cd daily-reports
git pull origin main
```

查看最新文件：

```bash
cat morning-briefs/latest-morning.md
cat evening-reviews/latest-evening.md
cat weekly-security/latest-security.md
cat open-source-watch/latest-watch.md
```

---

## 🛠️ 手动检查同步状态

```bash
cd ~/.openclaw/workspace/daily-reports
git log --oneline -5
git status
```

---

## ℹ️ 说明

- 仓库已经公开，可直接网页查看
- 这是一个**多定时任务汇总仓库**，不只是早报仓库
- 首页现在作为统一导航页使用
- 各目录中的 `latest-*` 文件可作为稳定入口

---

## ✅ 当前状态

**状态**：运行正常  
**最后检查**：2026-03-20 12:32  
**维护者**：OpenClaw 自动化系统
