# 📊 Daily Reports

OpenClaw 自动化汇报同步仓库。

## 快速入口

### 最新早报
- [latest 早报](morning-briefs/latest-morning.md)

### 最新晚间复盘
- [evening-reviews/](evening-reviews/)

### 最新每周安全笔记
- [latest 安全笔记](weekly-security/latest-security.md)

### 最新开源观察
- [open-source-watch/](open-source-watch/)

如果首页看起来内容不全，请直接进入对应子目录查看。

---

## 当前仓库结构

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

## 当前已同步内容

### 早报
- [2026-03-19](morning-briefs/2026-03-19-morning.md)
- [2026-03-20](morning-briefs/2026-03-20-morning.md)

### 每周安全笔记
- [2026-03-15](weekly-security/2026-03-15-security.md)

### 晚间复盘
- 正在补同步

### 开源观察
- 正在补同步

---

## 同步方式

### 自动流程
1. OpenClaw 定时任务生成对应报告
2. 保存到本地工作目录
3. 自动提交到 `daily-reports`
4. 推送到 GitHub 仓库

### 目标汇总类型
- 早报
- 晚间复盘
- 每周安全笔记
- 开源观察

---

## 本地查看

```bash
git clone https://github.com/Badelement/daily-reports.git
cd daily-reports
git pull origin main
```

查看具体内容：

```bash
cat morning-briefs/latest-morning.md
cat weekly-security/latest-security.md
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

- 仓库已经公开，可直接网页查看
- 这是一个**多定时任务汇总仓库**，不只是早报仓库
- 目前早报链路已通，安全笔记已补入，复盘与开源观察正在修复补齐

---

**最后更新**: 2026-03-20 12:21  
**维护者**: OpenClaw 自动化系统  
**状态**: 🟢 修复中