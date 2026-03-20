#!/usr/bin/env python3
import json
import subprocess
from datetime import datetime
from pathlib import Path

REPO = Path('/Users/badelement/.openclaw/workspace/daily-reports')
STATUS_DIR = REPO / 'status'
STATUS_DIR.mkdir(parents=True, exist_ok=True)


def run(cmd):
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        return r.returncode, (r.stdout or '').strip(), (r.stderr or '').strip()
    except Exception as e:
        return 1, '', str(e)


def get_session_status():
    code, out, err = run(['openclaw', 'status'])
    return out if out else (err or 'unavailable')


def get_gateway_status():
    code, out, err = run(['openclaw', 'gateway', 'status'])
    text = out if out else err
    lines = text.splitlines()[:12]
    return '\n'.join(lines) if lines else 'unavailable'


def get_cron_list():
    code, out, err = run(['openclaw', 'cron', 'list'])
    text = out if out else err
    lines = text.splitlines()[:20]
    return '\n'.join(lines) if lines else 'unavailable'


def get_git_status():
    code, out, err = run(['git', '-C', str(REPO), 'log', '--oneline', '-5'])
    return out if out else (err or 'unavailable')


def get_report_counts():
    sections = {
        'morning-briefs': len(list((REPO / 'morning-briefs').glob('*.md'))),
        'evening-reviews': len(list((REPO / 'evening-reviews').glob('*.md'))),
        'weekly-security': len(list((REPO / 'weekly-security').glob('*.md'))),
        'open-source-watch': len(list((REPO / 'open-source-watch').glob('*.md'))),
    }
    return sections


def latest_file_line(folder, label):
    p = REPO / folder
    files = sorted([f for f in p.glob('*.md') if not f.name.startswith('latest-')])
    if not files:
        return f'- {label}: 暂无'
    latest = files[-1].name
    return f'- {label}: [{latest}]({folder}/{latest})'


def write_dashboard():
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    counts = get_report_counts()
    content = f'''# 🖥️ OpenClaw System Dashboard

主监控页。这个页面优先于报告页，用于集中查看 OpenClaw 当前运行状态。

**更新时间**: {now} (Asia/Shanghai)

---

## 1. 当前系统概览

### 最新内容入口
{latest_file_line('morning-briefs', '最新早报')}
{latest_file_line('evening-reviews', '最新复盘')}
{latest_file_line('weekly-security', '最新安全笔记')}
{latest_file_line('open-source-watch', '最新开源观察')}

### 报告库存
- 早报数量: {counts['morning-briefs']}
- 复盘数量: {counts['evening-reviews']}
- 安全笔记数量: {counts['weekly-security']}
- 开源观察数量: {counts['open-source-watch']}

---

## 2. OpenClaw 会话状态

```text
{get_session_status()}
```

---

## 3. Gateway 状态

```text
{get_gateway_status()}
```

---

## 4. Cron 状态

```text
{get_cron_list()}
```

---

## 5. 仓库最近提交

```text
{get_git_status()}
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
'''
    (STATUS_DIR / 'system-dashboard.md').write_text(content, encoding='utf-8')


if __name__ == '__main__':
    write_dashboard()
