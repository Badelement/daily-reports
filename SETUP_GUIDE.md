# daily-reports 维护说明

这份文档描述 **daily-reports 当前的真实用途**，不再是仓库初始化待办清单。

## 仓库定位

`daily-reports` 是 OpenClaw 的：
- 报告归档仓库
- 状态快照仓库
- 自动同步输出仓库

## 当前内容

### 报告目录
- `morning-briefs/`：每日早报
- `evening-reviews/`：晚间复盘
- `weekly-security/`：每周安全笔记
- `open-source-watch/`：开源观察

### 状态目录
- `status/system-dashboard.md`：主监控页
- `status/openclaw-session-status.md`：会话状态快照

### 脚本目录
- `scripts/push_report.py`：推送单类报告
- `scripts/sync_all.py`：批量同步历史内容
- `scripts/update_dashboard.py`：刷新 dashboard 与状态摘要

---

## 当前运行方式

### 自动流程
1. OpenClaw 定时任务生成报告或状态快照
2. 文件写入本地工作目录
3. 推送脚本提交到 `daily-reports`
4. 自动推送到 GitHub 仓库

### 当前仓库属性
- GitHub 仓库：`https://github.com/Badelement/daily-reports`
- 当前可见性：**Public**

如果后续要改为私有仓库，应同步调整 README、维护说明和推送方式说明。

---

## 常用维护命令

### 查看仓库状态
```bash
cd ~/.openclaw/workspace/daily-reports
git status
git log --oneline -5
```

### 手动推送某类报告
```bash
cd ~/.openclaw/workspace/daily-reports
python3 scripts/push_report.py --type morning
python3 scripts/push_report.py --type evening
python3 scripts/push_report.py --type security
python3 scripts/push_report.py --type watch
```

### 手动刷新 dashboard
```bash
cd ~/.openclaw/workspace/daily-reports
python3 scripts/update_dashboard.py
```

### 批量同步
```bash
cd ~/.openclaw/workspace/daily-reports
python3 scripts/sync_all.py --days 7
```

---

## 常见问题

### 1. 首页看起来内容不全
先看：
- `README.md`
- `status/system-dashboard.md`

首页只负责导航，详细内容在子目录里。

### 2. dashboard 内容过期
先运行：
```bash
python3 scripts/update_dashboard.py
```
然后检查是否有新提交或未推送变更。

### 3. 自动任务正常，但仓库没更新
检查：
```bash
openclaw cron list
git -C ~/.openclaw/workspace/daily-reports status
git -C ~/.openclaw/workspace/daily-reports log --oneline -5
```

### 4. 推送失败
通常先检查：
- GitHub 认证
- 远程仓库 URL
- 本地工作区是否有冲突

---

## 维护原则

- 不把这个仓库再写成“只有早报”的单用途仓库
- 首页文档要和真实目录结构一致
- status 页负责系统状态，reports 页负责内容归档
- 优先小改动，不随便迁移历史文件

---

**最后更新**: 2026-03-21
**状态**: 🟢 按当前自动化流程维护中
