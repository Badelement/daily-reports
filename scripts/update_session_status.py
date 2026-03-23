#!/usr/bin/env python3
import re
import subprocess
from pathlib import Path

REPO = Path('/Users/badelement/.openclaw/workspace/daily-reports')
STATUS_DIR = REPO / 'status'

def run(cmd):
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        return r.returncode, (r.stdout or '').strip(), (r.stderr or '').strip()
    except Exception as e:
        return 1, '', str(e)

def get_session_status():
    code, out, err = run(['openclaw', 'status'])
    return out if out else (err or 'unavailable')

def parse_session_info(status_text):
    info = {
        'model': 'deepseek/deepseek-chat',
        'auth': 'telegram',
        'current_session': 'agent:main:cron:d2e5fda8-439e-44e2-b475-cdfb4a96c0b0',
        'mode': 'direct',
        'reasoning': 'off',
        'permission': 'normal',
        'context_usage': 'unknown',
        'active_sessions': 'unknown'
    }
    
    lines = status_text.splitlines()

    model_match = re.search(r'Sessions\s*│\s*\d+ active · default ([^(·\n]+)', status_text)
    if model_match:
        info['model'] = model_match.group(1).strip()
    
    session_match = re.search(r'Sessions\s*│\s*(\d+) active', status_text)
    if session_match:
        info['active_sessions'] = session_match.group(1)

    context_match = re.search(r'agent:main:[^\n]*?(\d+k/\d+k \(\d+%\))', status_text)
    if context_match:
        info['context_usage'] = context_match.group(1)

    if info['context_usage'] == 'unknown':
        overview_match = re.search(r'Sessions\s*│\s*\d+ active · [^·]+ · ([^\n]+)', status_text)
        if overview_match:
            info['context_usage'] = overview_match.group(1).strip()
    
    return info

def update_session_status_file():
    status_text = get_session_status()
    info = parse_session_info(status_text)
    
    content = f'''# OpenClaw Session Status

## 当前主会话状态

- **模型**：`{info['model']}`
- **认证方式**：`{info['auth']}`
- **当前会话**：`{info['current_session']}`
- **运行模式**：`{info['mode']}`
- **Reasoning/Think**：`{info['reasoning']}`
- **权限级别**：`{info['permission']}`

## 使用情况

- **活跃会话数**：`{info['active_sessions']}`
- **当前上下文占用**：`{info['context_usage']}`

## 原始状态摘要

```text
{chr(10).join(status_text.splitlines()[:18])}
```

---

## 说明

- 此文件为 OpenClaw 会话状态快照
- 每 30 分钟随仪表板一起更新
- 用于追踪会话状态和资源使用情况
- 原始状态快照可用于故障排查
'''
    
    (STATUS_DIR / 'openclaw-session-status.md').write_text(content, encoding='utf-8')
    print("会话状态文件已更新")

if __name__ == '__main__':
    update_session_status_file()
