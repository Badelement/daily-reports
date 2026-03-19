# 📊 每日汇报中心

OpenClaw 自动化汇报的 GitHub 同步仓库。

## 📁 目录结构

```
daily-reports/
├── README.md                    # 本文件
├── morning-briefs/              # 每日早报
│   ├── 2026-03-19-morning.md   # 按日期组织的早报
│   └── latest-morning.md       # 最新早报（软链接）
├── evening-reviews/             # 晚间复盘
│   ├── 2026-03-18-evening.md   # 按日期组织的复盘
│   └── latest-evening.md       # 最新复盘（软链接）
├── weekly-security/             # 每周安全笔记
│   ├── 2026-03-16-security.md  # 按日期组织的安全笔记
│   └── latest-security.md      # 最新安全笔记（软链接）
├── open-source-watch/           # 开源观察
│   ├── 2026-03-19-watch.md     # 按日期组织的观察
│   └── latest-watch.md         # 最新观察（软链接）
└── scripts/                     # 自动化脚本
    ├── push_report.py          # 推送脚本
    └── sync_all.py             # 批量同步脚本
```

## 🔄 同步机制

### 自动推送流程
1. OpenClaw 定时任务生成报告
2. 保存到本地工作空间 (`~/.openclaw/workspace/`)
3. 自动推送到本仓库
4. 保持文件结构和版本历史

### 时间安排
| 任务 | 生成时间 | 推送时间 |
|------|----------|----------|
| 早报 | 08:20 每天 | 生成后立即推送 |
| 开源观察 | 19:15 每天 | 生成后立即推送 |
| 晚间复盘 | 21:35 每天 | 生成后立即推送 |
| 每周安全 | 20:30 每周日 | 生成后立即推送 |

## 📊 查看方式

### 网页查看
1. 直接浏览 GitHub 文件
2. 使用 GitHub 的搜索功能
3. 按日期或标签筛选

### 本地查看
```bash
# 克隆仓库
git clone https://github.com/Badelement/daily-reports.git

# 更新
cd daily-reports
git pull origin main

# 查看最新早报
cat morning-briefs/latest-morning.md
```

### 快速链接
- [最新早报](morning-briefs/latest-morning.md)
- [最新复盘](evening-reviews/latest-evening.md)
- [最新安全笔记](weekly-security/latest-security.md)
- [最新开源观察](open-source-watch/latest-watch.md)

## 🏷️ 标签系统

报告使用统一的标签系统：

### 内容类型
- `#早报` - 每日信息筛选
- `#复盘` - 工作总结和改进
- `#安全` - AI agent 安全相关
- `#开源` - 开源项目观察

### 技术领域
- `#openclaw` - OpenClaw 相关
- `#skill` - 技能开发和优化
- `#自动化` - 自动化工作流
- `#github` - GitHub 工作流
- `#mac` - macOS 相关工具

### 项目相关
- `#三组件记忆` - 三组件记忆系统
- `#excel-operator` - Excel 操作技能
- `#skill-creator` - 技能创建工具

## 🔧 技术细节

### 文件命名规范
```
YYYY-MM-DD-{类型}.md
示例：2026-03-19-morning.md
```

### 元数据格式
每份报告开头包含元数据：
```yaml
---
title: 2026-03-19 早报
type: morning-brief
date: 2026-03-19
tags: [openclaw, skill, 自动化]
generated_by: OpenClaw定时任务
---
```

### 软链接维护
每个目录都有 `latest-{类型}.md` 指向最新文件，方便快速访问。

## 📈 统计和索引

### 月度汇总
每月自动生成汇总页面：
```
reports-index/
├── 2026-03-index.md    # 3月所有报告索引
├── 2026-02-index.md    # 2月所有报告索引
└── yearly-summary.md   # 年度总结
```

### 搜索技巧
```bash
# 搜索包含特定标签的报告
grep -r "#openclaw" morning-briefs/

# 搜索特定日期范围
find . -name "2026-03-*.md" -type f

# 统计报告数量
find . -name "*.md" -type f | wc -l
```

## ⚠️ 注意事项

### 隐私保护
- 本仓库为私有仓库，仅你可见
- 敏感信息已自动过滤
- 不包含具体API密钥、密码等

### 同步状态
- 每次推送都会记录状态
- 失败时会自动重试（最多3次）
- 网络问题会延迟推送

### 存储管理
- 报告永久保存，不会自动删除
- 可使用Git历史查看旧版本
- 如需清理，可手动删除旧文件

## 🔄 手动操作

### 强制同步
```bash
cd ~/.openclaw/workspace/daily-reports
python scripts/sync_all.py
```

### 查看同步状态
```bash
cd ~/.openclaw/workspace/daily-reports
git log --oneline -5
```

### 修复问题
```bash
# 重置本地仓库
cd ~/.openclaw/workspace/daily-reports
git reset --hard origin/main
git pull origin main
```

## 📞 支持

如有问题：
1. 检查 `scripts/push_report.py` 日志
2. 查看 GitHub Actions 状态（如果配置）
3. 联系 OpenClaw 维护

---

**最后更新**: 2026-03-19  
**维护者**: OpenClaw 自动化系统  
**状态**: 🟢 运行正常