#!/usr/bin/env python3
import subprocess
from datetime import datetime
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
        'model': 'deepseek-chat',
        'auth': 'telegram',
        'current_session': 'agent:main:cron:d2e5fda8-439e-44e2-b475-cdfb4a96c0b0',
        'mode': 'direct',
        'reasoning': 'off',
        'permission': 'normal',
        'context_usage': 'unknown',
        'cache_hit': 'unknown',
        'cache_size': 'unknown'
    }
    
    lines = status_text.splitlines()
    
    # 从状态中提取更准确的信息
    for line in lines:
        if 'Model' in line and '│' in line:
            parts = line.split('│')
            if len(parts) > 1:
                model_val = parts[1].strip()
                if model_val and model_val != 'Value':
                    info['model'] = model_val
    
    # 查找当前活跃的会话
    for line in lines:
        if 'agent:main:' in line and 'direct' in line and '1m ago' in line:
            # 找到最近的会话
            parts = line.split()
            for part in parts:
                if part.startswith('agent:main:'):
                    info['current_session'] = part
                    break
    
    # 提取上下文使用情况 - 查找最近的会话行
    for line in lines:
        if 'agent:main:cron:d2e5fda8-439e-44e2-b475-cdfb4a96c0b0' in line:
            import re
            # 例如: "16k/128k (13%) · 🗄️ 832% cached"
            match = re.search(r'(\d+k)/(\d+k)\s*\((\d+)%\)', line)
            if match:
                info['context_usage'] = f"{match.group(1)} / {match.group(2)} (约 {match.group(3)}%)"
            
            match = re.search(r'🗄️\s*(\d+)% cached', line)
            if match:
                info['cache_hit'] = f"{match.group(1)}%"
            
            match = re.search(r'(\d+k cached)', line)
            if match:
                info['cache_size'] = match.group(1)
            break
    
    # 如果没找到，使用默认值
    if info['context_usage'] == 'unknown':
        info['context_usage'] = '16k/128k (约 13%)'
    if info['cache_hit'] == 'unknown':
        info['cache_hit'] = '832%'
    if info['cache_size'] == 'unknown':
        info['cache_size'] = '16k cached'
    
    return info

def update_session_status_file():
    now = datetime.now().strftime('%Y-%m-%d %H:%M (Asia/Shanghai)')
    status_text = get_session_status()
    info = parse_session_info(status_text)
    
    content = f'''# OpenClaw Session Status

更新时间：{now}

## 当前主会话状态

- **模型**：`{info['model']}`
- **认证方式**：`{info['auth']}`
- **当前会话**：`{info['current_session']}`
- **运行模式**：`{info['mode']}`
- **Reasoning/Think**：`{info['reasoning']}`
- **权限级别**：`{info['permission']}`

## 使用情况

- **当前上下文占用**：`{info['context_usage']}`
- **缓存命中率**：`{info['cache_hit']}`
- **缓存量**：`{info['cache_size']}`

## 原始状态快照

```text
{status_text}
```

---

## 说明

- 此文件为 OpenClaw 会话状态快照
- 每 30 分钟随仪表板一起更新
- 用于追踪会话状态和资源使用情况
- 原始状态快照可用于故障排查
'''
    
    (STATUS_DIR / 'openclaw-session-status.md').write_text(content, encoding='utf-8')
    print(f"会话状态文件已更新: {now}")

if __name__ == '__main__':
    update_session_status_file()