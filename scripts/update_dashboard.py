#!/usr/bin/env python3
import json
import re
import subprocess
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


def get_git_porcelain():
    code, out, err = run(['git', '-C', str(REPO), 'status', '--short'])
    return out if out else ''


def get_report_counts():
    return {
        'morning-briefs': len(list((REPO / 'morning-briefs').glob('*.md'))),
        'evening-reviews': len(list((REPO / 'evening-reviews').glob('*.md'))),
        'weekly-security': len(list((REPO / 'weekly-security').glob('*.md'))),
        'open-source-watch': len(list((REPO / 'open-source-watch').glob('*.md'))),
    }


def latest_file_line(folder, label):
    p = REPO / folder
    files = sorted([f for f in p.glob('*.md') if not f.name.startswith('latest-')])
    if not files:
        return f'- {label}: 暂无'
    latest = files[-1].name
    return f'- {label}: [{latest}](../{folder}/{latest})'


def parse_cron_anomalies(cron_text):
    anomalies = []
    for line in cron_text.splitlines()[1:]:
        low = line.lower()
        if any(flag in low for flag in [' fail', ' error', ' overdue', ' disabled ']):
            anomalies.append(line)
    return anomalies[:8]


def derive_anomalies(session_text, gateway_text, cron_text, git_status):
    anomalies = []

    gw_low = gateway_text.lower()
    if 'loaded' not in gw_low and 'bind=' not in gw_low:
        anomalies.append('Gateway 状态异常：未看到正常服务标记')

    session_low = session_text.lower()
    if 'queue:' in session_low and 'depth 0' not in session_low:
        anomalies.append('会话队列非空：存在待处理消息')
    if 'context:' in session_low:
        m = re.search(r'context:\s*[^\n]*\((\d+)%\)', session_low)
        if m and int(m.group(1)) >= 80:
            anomalies.append(f'上下文占用偏高：{m.group(1)}%')

    cron_anomalies = parse_cron_anomalies(cron_text)
    if cron_anomalies:
        anomalies.append('发现异常 cron 状态：')
        anomalies.extend([f'- {x}' for x in cron_anomalies])

    if git_status.strip():
        anomalies.append('daily-reports 仓库存在未提交更改')

    return anomalies


def build_session_summary(session_text):
    lines = session_text.splitlines()
    summary = []

    if 'Gateway service' in session_text and 'running' in session_text:
        summary.append('- Gateway 服务：运行中')
    elif 'Gateway service' in session_text:
        summary.append('- Gateway 服务：状态异常或未运行')

    if 'Telegram │ ON' in session_text or 'Telegram | ON' in session_text:
        summary.append('- Telegram 通道：正常')

    m = re.search(r'Sessions\s*│\s*(\d+) active', session_text)
    if m:
        summary.append(f'- 活跃会话数：{m.group(1)}')

    m = re.search(r'Heartbeat\s*│\s*([^\n│]+)', session_text)
    if m:
        summary.append(f'- 心跳频率：{m.group(1).strip()}')

    m = re.search(r'Context:\s*[^\n]*\((\d+)%\)', session_text, re.IGNORECASE)
    if m:
        summary.append(f'- 当前上下文占用：{m.group(1)}%')

    return '\n'.join(summary) if summary else '- 暂时无法提取中文摘要，请查看下方原始状态'


def build_gateway_summary(gateway_text):
    summary = []
    if 'LaunchAgent (loaded)' in gateway_text:
        summary.append('- Gateway 服务已加载')
    if 'bind=loopback' in gateway_text:
        summary.append('- 当前仅监听本机回环地址')
    m = re.search(r'port=(\d+)', gateway_text)
    if m:
        summary.append(f'- 监听端口：{m.group(1)}')
    if 'Dashboard: disabled' in gateway_text:
        summary.append('- OpenClaw 内建 dashboard：关闭')
    return '\n'.join(summary) if summary else '- 暂时无法提取中文摘要，请查看下方原始状态'


def build_cron_summary(cron_text):
    lines = [line for line in cron_text.splitlines() if line.strip()]
    summary = []
    job_lines = [line for line in lines if re.match(r'^[a-f0-9-]{8,}', line)]
    if job_lines:
        summary.append(f'- 定时任务数量：{len(job_lines)}')
    ok_count = sum(1 for line in job_lines if ' ok ' in f' {line} ')
    if job_lines:
        summary.append(f'- 最近状态正常的任务：{ok_count}/{len(job_lines)}')
    if any('daily-reports-dashboa' in line for line in job_lines):
        summary.append('- dashboard 刷新任务：已在列表中')
    return '\n'.join(summary) if summary else '- 暂时无法提取中文摘要，请查看下方原始状态'


def build_repo_summary(git_status):
    summary = []
    if git_status.strip():
        changed = len([line for line in git_status.splitlines() if line.strip()])
        summary.append(f'- 工作区有未提交更改：{changed} 项')
    else:
        summary.append('- 工作区状态：干净')
    return '\n'.join(summary) if summary else '- 暂时无法提取中文摘要，请查看下方原始状态'


def write_dashboard():
    counts = get_report_counts()
    session_status = get_session_status()
    gateway_status = get_gateway_status()
    cron_list = get_cron_list()
    git_status = get_git_porcelain()
    anomalies = derive_anomalies(session_status, gateway_status, cron_list, git_status)
    session_summary = build_session_summary(session_status)
    gateway_summary = build_gateway_summary(gateway_status)
    cron_summary = build_cron_summary(cron_list)
    repo_summary = build_repo_summary(git_status)

    anomaly_block = '\n'.join([f'- {a}' if not a.startswith('- ') else a for a in anomalies]) if anomalies else '- 当前未发现明显异常'
    git_status_block = git_status if git_status.strip() else 'working tree clean'

    content = f'''# 🖥️ OpenClaw System Dashboard

主监控页。用于集中查看 OpenClaw 当前运行状态，并作为这个仓库的状态入口页。

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

## 2. 异常状态摘要

{anomaly_block}

---

## 3. OpenClaw 会话状态

### 中文摘要
{session_summary}

### 原始状态
```text
{session_status}
```

---

## 4. Gateway 状态

### 中文摘要
{gateway_summary}

### 原始状态
```text
{gateway_status}
```

---

## 5. Cron 状态

### 中文摘要
{cron_summary}

### 原始状态
```text
{cron_list}
```

---

## 6. 仓库状态

### 中文摘要
{repo_summary}

### 工作区状态
```text
{git_status_block}
```

---

## 7. 次要页面入口

### 报告页
- [早报目录](../morning-briefs/)
- [复盘目录](../evening-reviews/)
- [安全笔记目录](../weekly-security/)
- [开源观察目录](../open-source-watch/)

### 状态页
- [会话状态](openclaw-session-status.md)
- [仓库首页](../README.md)

---

## 说明

- 此页为状态总览页
- 每 30 分钟自动刷新一次
- 报告目录用于查看详细内容和历史存档
- “异常状态摘要”用于快速定位需关注问题
'''
    (STATUS_DIR / 'system-dashboard.md').write_text(content, encoding='utf-8')


if __name__ == '__main__':
    write_dashboard()
