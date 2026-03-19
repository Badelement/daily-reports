#!/usr/bin/env python3
"""
OpenClaw 报告推送脚本
将生成的报告自动推送到 GitHub 仓库
"""

import os
import sys
import json
import shutil
from pathlib import Path
from datetime import datetime
import subprocess
import time
import logging

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('/tmp/openclaw_report_push.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class ReportPusher:
    """报告推送器"""
    
    def __init__(self, repo_path=None):
        """初始化"""
        self.repo_path = Path(repo_path) if repo_path else Path.home() / '.openclaw' / 'workspace' / 'daily-reports'
        self.report_types = {
            'morning': {
                'source_dir': Path.home() / '.openclaw' / 'workspace' / 'briefings',
                'target_dir': self.repo_path / 'morning-briefs',
                'pattern': '*-morning-brief.md'
            },
            'evening': {
                'source_dir': Path.home() / '.openclaw' / 'workspace' / 'review',
                'target_dir': self.repo_path / 'evening-reviews',
                'pattern': '*-self-iteration.md'
            },
            'security': {
                'source_dir': Path.home() / '.openclaw' / 'workspace' / 'review',
                'target_dir': self.repo_path / 'weekly-security',
                'pattern': '*-weekly-agent-security-notes.md'
            },
            'watch': {
                'source_dir': Path.home() / '.openclaw' / 'workspace',
                'target_dir': self.repo_path / 'open-source-watch',
                'pattern': 'open-source-watch-*.md'
            }
        }
        
        # 确保目录存在
        for config in self.report_types.values():
            config['target_dir'].mkdir(parents=True, exist_ok=True)
    
    def get_latest_report(self, report_type):
        """获取最新报告"""
        if report_type not in self.report_types:
            logger.error(f"未知的报告类型: {report_type}")
            return None
        
        config = self.report_types[report_type]
        source_dir = config['source_dir']
        pattern = config['pattern']
        
        # 查找最新文件
        try:
            files = list(source_dir.glob(pattern))
            if not files:
                logger.warning(f"未找到 {report_type} 报告: {source_dir}/{pattern}")
                return None
            
            # 按修改时间排序，取最新的
            latest_file = max(files, key=lambda x: x.stat().st_mtime)
            logger.info(f"找到最新 {report_type} 报告: {latest_file}")
            return latest_file
        except Exception as e:
            logger.error(f"查找 {report_type} 报告失败: {e}")
            return None
    
    def copy_report_to_repo(self, report_type, source_file):
        """复制报告到仓库"""
        if report_type not in self.report_types:
            return False
        
        config = self.report_types[report_type]
        target_dir = config['target_dir']
        
        # 生成目标文件名
        date_str = datetime.now().strftime("%Y-%m-%d")
        target_filename = f"{date_str}-{report_type}.md"
        target_path = target_dir / target_filename
        
        try:
            # 读取源文件内容
            with open(source_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 添加元数据
            metadata = f"""---
title: {date_str} {'早报' if report_type == 'morning' else '复盘' if report_type == 'evening' else '安全笔记' if report_type == 'security' else '开源观察'}
type: {report_type}
date: {date_str}
tags: [openclaw, automation]
generated_by: OpenClaw定时任务
source_file: {source_file.name}
---

"""
            
            # 写入目标文件
            with open(target_path, 'w', encoding='utf-8') as f:
                f.write(metadata + content)
            
            logger.info(f"复制报告到: {target_path}")
            
            # 更新最新文件软链接
            latest_link = target_dir / f"latest-{report_type}.md"
            if latest_link.exists():
                latest_link.unlink()
            latest_link.symlink_to(target_filename)
            logger.info(f"更新软链接: {latest_link} -> {target_filename}")
            
            return True
            
        except Exception as e:
            logger.error(f"复制报告失败: {e}")
            return False
    
    def git_operations(self, commit_message=None):
        """执行Git操作"""
        try:
            # 切换到仓库目录
            original_cwd = os.getcwd()
            os.chdir(self.repo_path)
            
            # 检查是否有更改
            status_result = subprocess.run(
                ['git', 'status', '--porcelain'],
                capture_output=True,
                text=True,
                timeout=10
            )
            
            if not status_result.stdout.strip():
                logger.info("没有需要提交的更改")
                os.chdir(original_cwd)
                return True
            
            logger.info("检测到更改，准备提交")
            
            # 添加所有文件
            subprocess.run(
                ['git', 'add', '.'],
                check=True,
                timeout=10
            )
            
            # 提交
            if not commit_message:
                commit_message = f"Update reports - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
            
            subprocess.run(
                ['git', 'commit', '-m', commit_message],
                check=True,
                timeout=10
            )
            
            # 推送（最多重试3次）
            max_retries = 3
            for attempt in range(max_retries):
                try:
                    push_result = subprocess.run(
                        ['git', 'push', 'origin', 'main'],
                        capture_output=True,
                        text=True,
                        timeout=30
                    )
                    
                    if push_result.returncode == 0:
                        logger.info("推送成功")
                        os.chdir(original_cwd)
                        return True
                    else:
                        logger.warning(f"推送失败 (尝试 {attempt + 1}/{max_retries}): {push_result.stderr}")
                        if attempt < max_retries - 1:
                            time.sleep(2 ** attempt)  # 指数退避
                
                except subprocess.TimeoutExpired:
                    logger.warning(f"推送超时 (尝试 {attempt + 1}/{max_retries})")
                    if attempt < max_retries - 1:
                        time.sleep(2 ** attempt)
            
            logger.error("推送失败，达到最大重试次数")
            os.chdir(original_cwd)
            return False
            
        except Exception as e:
            logger.error(f"Git操作失败: {e}")
            os.chdir(original_cwd)
            return False
    
    def push_report(self, report_type, commit_message=None):
        """推送单个报告"""
        logger.info(f"开始推送 {report_type} 报告")
        
        # 1. 获取最新报告
        source_file = self.get_latest_report(report_type)
        if not source_file:
            logger.warning(f"未找到 {report_type} 报告，跳过")
            return False
        
        # 2. 复制到仓库
        if not self.copy_report_to_repo(report_type, source_file):
            logger.error(f"复制 {report_type} 报告失败")
            return False
        
        # 3. 执行Git操作
        if not self.git_operations(commit_message):
            logger.error(f"Git操作失败")
            return False
        
        logger.info(f"成功推送 {report_type} 报告")
        return True
    
    def push_all_reports(self):
        """推送所有报告"""
        logger.info("开始推送所有报告")
        
        results = {}
        for report_type in self.report_types.keys():
            success = self.push_report(report_type)
            results[report_type] = success
        
        # 汇总结果
        success_count = sum(1 for success in results.values() if success)
        total_count = len(results)
        
        logger.info(f"报告推送完成: {success_count}/{total_count} 成功")
        
        # 如果有成功推送的，最后再执行一次Git操作确保所有更改都提交
        if success_count > 0:
            self.git_operations(f"Batch update - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        return results

def main():
    """主函数"""
    import argparse
    
    parser = argparse.ArgumentParser(description='推送OpenClaw报告到GitHub')
    parser.add_argument('--type', choices=['morning', 'evening', 'security', 'watch', 'all'],
                       default='all', help='报告类型')
    parser.add_argument('--repo-path', help='仓库路径')
    parser.add_argument('--commit-message', help='提交信息')
    
    args = parser.parse_args()
    
    pusher = ReportPusher(args.repo_path)
    
    if args.type == 'all':
        results = pusher.push_all_reports()
        
        # 输出结果
        print("\n" + "="*50)
        print("报告推送结果:")
        print("="*50)
        for report_type, success in results.items():
            status = "✅ 成功" if success else "❌ 失败"
            print(f"{report_type:10} {status}")
        
        success_count = sum(1 for success in results.values() if success)
        total_count = len(results)
        print(f"\n总计: {success_count}/{total_count} 成功")
        
        if success_count == total_count:
            sys.exit(0)
        else:
            sys.exit(1)
    else:
        success = pusher.push_report(args.type, args.commit_message)
        if success:
            print(f"✅ {args.type} 报告推送成功")
            sys.exit(0)
        else:
            print(f"❌ {args.type} 报告推送失败")
            sys.exit(1)

if __name__ == "__main__":
    main()