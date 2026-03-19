# GitHub汇报同步系统 - 设置指南

## 🎯 目标
将OpenClaw的定时汇报自动同步到GitHub私有仓库，实现：
1. 永久存档
2. 多设备访问
3. 版本历史
4. 搜索整理

## 📋 前提条件

### 已完成的
✅ 本地仓库结构已创建 (`~/.openclaw/workspace/daily-reports/`)  
✅ 推送脚本已开发 (`scripts/push_report.py`)  
✅ 批量同步脚本已开发 (`scripts/sync_all.py`)  
✅ 早报任务修改方案已准备  

### 需要你完成的
1. 创建GitHub私有仓库
2. 配置远程仓库
3. 测试推送功能
4. 修改定时任务

## 🚀 实施步骤

### 步骤1：创建GitHub私有仓库

1. 访问 https://github.com/new
2. 填写信息：
   - **Repository name**: `daily-reports`
   - **Description**: `OpenClaw每日汇报同步中心`
   - **Visibility**: ⚫ **Private** (必须私有！)
   - 不要勾选 "Initialize this repository with a README"
3. 点击 "Create repository"
4. 复制仓库URL：`https://github.com/Badelement/daily-reports.git`

### 步骤2：配置本地仓库

```bash
# 1. 进入仓库目录
cd ~/.openclaw/workspace/daily-reports

# 2. 添加远程仓库（替换YOUR_URL为实际URL）
git remote add origin https://github.com/Badelement/daily-reports.git

# 3. 推送初始代码
git push -u origin main

# 4. 验证配置
git remote -v
# 应该显示：
# origin  https://github.com/Badelement/daily-reports.git (fetch)
# origin  https://github.com/Badelement/daily-reports.git (push)
```

### 步骤3：测试推送功能

```bash
# 1. 测试推送脚本
cd ~/.openclaw/workspace/daily-reports
python scripts/push_report.py --type morning

# 2. 如果失败，检查：
# - GitHub访问权限（可能需要Personal Access Token）
# - 网络连接
# - 脚本权限：chmod +x scripts/*.py

# 3. 批量同步历史报告（可选）
python scripts/sync_all.py --days 7
```

### 步骤4：修改早报定时任务

```bash
# 运行修改脚本
bash ~/.openclaw/workspace/update_morning_task.sh

# 或者手动执行：
openclaw cron update 9fea7709-95fe-462f-b38c-752efed139b0 --patch '{
  "payload": {
    "message": "请生成早报...（完整内容见脚本）"
  }
}'
```

### 步骤5：验证修改

```bash
# 1. 查看修改后的任务
openclaw cron list

# 2. 手动触发测试
openclaw cron run 9fea7709-95fe-462f-b38c-752efed139b0

# 3. 检查结果：
# - 本地文件：~/.openclaw/workspace/briefings/
# - GitHub仓库：https://github.com/Badelement/daily-reports
# - Telegram：应该收到摘要
```

### 步骤6：修改其他任务（可选）

早报任务测试成功后，可以修改其他任务：
1. 晚间复盘任务ID: `bbbba49f-c5d4-4690-b1be-3616a294cc26`
2. 开源观察任务ID: `ef3bb9db-238b-4e6b-9dda-dbc79e87a541`
3. 每周安全任务ID: `6b5c0215-c791-4e55-bcd6-64abd24afbb9`

## 🔧 故障排除

### 常见问题1：Git推送权限错误
```bash
# 解决方案：使用Personal Access Token
# 1. 生成Token：GitHub → Settings → Developer settings → Personal access tokens
# 2. 选择权限：repo (全部)
# 3. 修改远程URL：
git remote set-url origin https://YOUR_TOKEN@github.com/Badelement/daily-reports.git
```

### 常见问题2：Python脚本执行错误
```bash
# 1. 检查Python版本
python3 --version

# 2. 安装依赖（如果需要）
pip3 install -r requirements.txt

# 3. 检查脚本权限
chmod +x scripts/*.py

# 4. 查看日志
tail -f /tmp/openclaw_report_push.log
```

### 常见问题3：定时任务不执行
```bash
# 1. 检查任务状态
openclaw cron list

# 2. 检查Gateway状态
openclaw gateway status

# 3. 查看日志
tail -f /tmp/openclaw/openclaw-*.log

# 4. 手动触发测试
openclaw cron run <task_id>
```

## 📊 验证成功

### 成功标志
1. ✅ GitHub仓库有文件：`morning-briefs/2026-03-19-morning.md`
2. ✅ 本地软链接更新：`morning-briefs/latest-morning.md`
3. ✅ Telegram收到摘要
4. ✅ Git提交历史正常

### 检查清单
- [ ] GitHub仓库创建成功（私有）
- [ ] 远程仓库配置成功
- [ ] 推送脚本测试通过
- [ ] 早报任务修改成功
- [ ] 自动推送测试通过
- [ ] 所有报告类型都同步

## 🎨 使用方式

### 查看报告
1. **GitHub网页**：直接浏览文件
2. **本地查看**：
   ```bash
   cd ~/.openclaw/workspace/daily-reports
   git pull
   cat morning-briefs/latest-morning.md
   ```
3. **搜索功能**：
   ```bash
   # 搜索包含特定标签的报告
   grep -r "#openclaw" morning-briefs/
   
   # 按日期查找
   find . -name "2026-03-*.md" -type f
   ```

### 管理仓库
```bash
# 更新仓库
cd ~/.openclaw/workspace/daily-reports
git pull origin main

# 查看历史
git log --oneline -10

# 强制同步
python scripts/sync_all.py --days 30
```

## 🔄 后续优化

### 阶段2：修改所有任务
早报任务成功后，批量修改其他任务：
```bash
# 创建批量修改脚本
python ~/.openclaw/workspace/create_batch_update.py
```

### 阶段3：添加统计功能
- 月度汇总报告
- 标签使用统计
- 热门话题分析

### 阶段4：集成GitHub Actions
- 自动生成索引页面
- 定期清理旧文件
- 备份到其他存储

## 📞 支持

### 遇到问题？
1. 检查日志：`/tmp/openclaw_report_push.log`
2. 查看任务状态：`openclaw cron list`
3. 手动测试：`python scripts/push_report.py --type morning`

### 需要帮助？
提供以下信息：
1. 错误信息
2. 相关日志
3. 当前状态截图

---

**最后更新**: 2026-03-19  
**状态**: 🟡 等待GitHub仓库创建

## 🚨 重要提醒

1. **必须使用私有仓库**，避免敏感信息泄露
2. 首次推送可能需要GitHub身份验证
3. 建议先测试，再批量修改任务
4. 保持本地备份 (`~/.openclaw/workspace/`) 作为冗余

**完成步骤1（创建GitHub仓库）后告诉我URL，我帮你完成后续配置！**