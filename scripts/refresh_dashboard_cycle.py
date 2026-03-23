#!/usr/bin/env python3
import argparse
import subprocess
import time
from pathlib import Path


REPO = Path("/Users/badelement/.openclaw/workspace/daily-reports")
ALLOWED_FILES = [
    "status/system-dashboard.md",
    "status/openclaw-session-status.md",
]


def run(cmd, timeout=120, check=False):
    return subprocess.run(
        cmd,
        cwd=REPO,
        capture_output=True,
        text=True,
        timeout=timeout,
        check=check,
    )


def refresh_snapshots():
    run(["python3", str(REPO / "scripts" / "update_dashboard.py")], check=True)
    run(["python3", str(REPO / "scripts" / "update_session_status.py")], check=True)


def changed_allowed_files():
    result = run(["git", "status", "--porcelain", "--"] + ALLOWED_FILES, timeout=30)
    return [line for line in result.stdout.splitlines() if line.strip()]


def stage_and_commit():
    run(["git", "add", "--"] + ALLOWED_FILES, timeout=30, check=True)
    result = run(
        ["git", "commit", "-m", "dashboard: refresh status snapshots [cron:d2e5fda8-439e-44e2-b475-cdfb4a96c0b0]"],
        timeout=30,
    )
    return result.returncode == 0


def push_with_retry():
    for attempt in range(3):
        result = run(["git", "push", "origin", "main"], timeout=60)
        if result.returncode == 0:
            return True
        if attempt < 2:
            time.sleep(2 ** attempt)
    return False


def main():
    parser = argparse.ArgumentParser(description="Refresh dashboard snapshots and optionally publish them.")
    parser.add_argument("--skip-git", action="store_true", help="Refresh files only, do not commit or push.")
    args = parser.parse_args()

    refresh_snapshots()

    if args.skip_git:
        print("dashboard refresh: snapshots updated locally")
        return 0

    changed = changed_allowed_files()
    if not changed:
        print("dashboard refresh: no tracked snapshot changes")
        return 0

    if not stage_and_commit():
        print("dashboard refresh: no commit created")
        return 0

    if push_with_retry():
        print("dashboard refresh: committed and pushed")
        return 0

    print("dashboard refresh: commit created but push failed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
