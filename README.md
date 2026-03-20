# 📊 Daily Reports

OpenClaw 自动化汇报同步仓库。

## 快速入口

### 最新早报
- [2026-03-20 早报](morning-briefs/2026-03-20-morning.md)

### 历史早报目录
- [morning-briefs/](morning-briefs/)

如果你打开仓库首页看不到内容，请直接点上面的链接。

---

## 当前仓库结构

```text
daily-reports/
├── README.md
├── SETUP_GUIDE.md
├── morning-briefs/
│   ├── 2026-03-19-morning.md
│   └── 2026-03-20-morning.md
└── scripts/
    ├── push_report.py
    └── sync_all.py
```

---

## 当前已同步内容

### 早报
- [2026-03-19](morning-briefs/2026-03-19-morning.md)
- [2026-03-20](morning-briefs/2026-03-20-morning.md)

---

## 同步方式

### 自动流程
1. OpenClaw 定时任务生成早报
2. 保存到本地工作目录
3. 自动提交到 `daily-reports`
4. 推送到 GitHub 仓库

### 当前重点
目前仓库里最主要的内容是：
- **每日早报**

后续如果继续启用：
- 晚间复盘
- 每周安全笔记
- 开源观察
也可以再逐步补回目录结构。

---

## 本地查看

```bash
git clone https://github.com/Badelement/daily-reports.git
cd daily-reports
git pull origin main
cat morning-briefs/2026-03-20-morning.md
```

---

## 手动检查同步状态

```bash
cd ~/.openclaw/workspace/daily-reports
git log --oneline -5
git status
```

---

## 说明

- 仓库现在已经公开，可直接网页查看
- 如果首页看起来“空”，通常是因为内容在 `morning-briefs/` 子目录里
- 当前 README 已经把最新早报入口放到首页，后续打开会更直观

---

**最后更新**: 2026-03-20  
**维护者**: OpenClaw 自动化系统  
**状态**: 🟢 可查看