#!/usr/bin/env python3
"""
批量同步所有历史报告到GitHub仓库
"""

import os
import re
import sys
from pathlib import Path
from datetime import datetime, timedelta
import shutil
import subprocess
import logging

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class ReportSyncer:
    """报告同步器"""
    
    def __init__(self, repo_path=None):
        self.repo_path = Path(repo_path) if repo_path else Path.home() / '.openclaw' / 'workspace' / 'daily-reports'
        
        # 报告类型配置
        self.report_configs = {
            'morning': {
                'source_pattern': '*-morning-brief.md',
                'source_dir': Path.home() / '.openclaw' / 'workspace' / 'briefings',
                'target_dir': self.repo_path / 'morning-briefs',
                'date_format': '%Y-%m-%d',
                'prefix': 'morning'
            },
            'evening': {
                'source_pattern': '*-self-iteration.md',
                'source_dir': Path.home() / '.openclaw' / 'workspace' / 'review',
                'target_dir': self.repo_path / 'evening-reviews',
                'date_format': '%Y-%m-%d',
                'prefix': 'evening'
            },
            'security': {
                'source_pattern': '*-weekly-agent-security-notes.md',
                'source_dir': Path.home() / '.openclaw' / 'workspace' / 'review',
                'target_dir': self.repo_path / 'weekly-security',
                'date_format': '%Y-%m-%d',
                'prefix': 'security'
            }
        }
        
        # 确保目标目录存在
        for config in self.report_configs.values():
            config['target_dir'].mkdir(parents=True, exist_ok=True)
    
    def extract_date_from_filename(self, filename, report_type):
        """从文件名提取日期"""
        try:
            stem = filename.stem
            match = re.match(r'^(\d{4}-\d{2}-\d{2})-', stem)
            if match:
                return datetime.strptime(match.group(1), '%Y-%m-%d').date()
        except Exception as e:
            logger.warning(f"无法从 {filename} 提取日期: {e}")
        
        return None
    
    def sync_report_type(self, report_type, days_back=30):
        """同步特定类型的报告"""
        config = self.report_configs[report_type]
        source_dir = config['source_dir']
        target_dir = config['target_dir']
        pattern = config['source_pattern']
        
        logger.info(f"开始同步 {report_type} 报告...")
        
        # 查找源文件
        source_files = list(source_dir.glob(pattern))
        if not source_files:
            logger.warning(f"未找到 {report_type} 报告: {source_dir}/{pattern}")
            return 0
        
        logger.info(f"找到 {len(source_files)} 个 {report_type} 报告")
        
        synced_count = 0
        skipped_count = 0
        error_count = 0
        
        # 计算日期范围
        end_date = datetime.now().date()
        start_date = end_date - timedelta(days=days_back)
        
        for source_file in source_files:
            try:
                # 提取日期
                file_date = self.extract_date_from_filename(source_file, report_type)
                if not file_date:
                    logger.warning(f"跳过无法解析日期的文件: {source_file}")
                    skipped_count += 1
                    continue
                
                # 检查是否在日期范围内
                if file_date < start_date:
                    logger.debug(f"跳过旧文件: {source_file} ({file_date})")
                    skipped_count += 1
                    continue
                
                # 生成目标文件名
                date_str = file_date.strftime('%Y-%m-%d')
                target_filename = f"{date_str}-{config['prefix']}.md"
                target_path = target_dir / target_filename
                
                # 检查是否已存在
                if target_path.exists():
                    # 比较文件大小和修改时间
                    source_mtime = source_file.stat().st_mtime
                    target_mtime = target_path.stat().st_mtime
                    source_size = source_file.stat().st_size
                    target_size = target_path.stat().st_size
                    
                    if source_mtime <= target_mtime and source_size == target_size:
                        logger.debug(f"文件已是最新: {target_filename}")
                        skipped_count += 1
                        continue
                
                # 复制文件
                shutil.copy2(source_file, target_path)
                logger.info(f"同步: {source_file.name} -> {target_filename}")
                synced_count += 1
                
                # 添加元数据
                self.add_metadata(target_path, report_type, file_date)
                
            except Exception as e:
                logger.error(f"同步文件失败 {source_file}: {e}")
                error_count += 1
        
        logger.info(f"{report_type} 同步完成: {synced_count} 新增, {skipped_count} 跳过, {error_count} 错误")
        return synced_count
    
    def add_metadata(self, filepath, report_type, date):
        """添加元数据到文件"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 报告类型中文名
            type_names = {
                'morning': '早报',
                'evening': '复盘',
                'security': '安全笔记'
            }
            
            metadata = f"""---
title: {date.strftime('%Y-%m-%d')} {type_names.get(report_type, report_type)}
type: {report_type}
date: {date.strftime('%Y-%m-%d')}
tags: [openclaw, automation]
synced_at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
synced_by: batch_sync
---

"""
            
            # 如果文件已有元数据，替换它
            if content.startswith('---'):
                # 找到元数据结束位置
                end_metadata = content.find('---', 3)
                if end_metadata != -1:
                    content = metadata + content[end_metadata + 3:].lstrip()
                else:
                    content = metadata + content
            else:
                content = metadata + content
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
                
        except Exception as e:
            logger.warning(f"添加元数据失败 {filepath}: {e}")
    
    def update_latest_links(self):
        """更新最新文件软链接"""
        logger.info("更新最新文件软链接...")
        
        for report_type, config in self.report_configs.items():
            target_dir = config['target_dir']
            
            # 查找最新的文件
            pattern = f"*-{config['prefix']}.md"
            files = [f for f in target_dir.glob(pattern) if not f.name.startswith('latest-')]
            
            if not files:
                logger.warning(f"未找到 {report_type} 文件")
                continue
            
            # 按日期排序
            files.sort(key=lambda x: x.stat().st_mtime, reverse=True)
            latest_file = files[0]
            
            # 创建或更新软链接
            latest_link = target_dir / f"latest-{config['prefix']}.md"
            if latest_link.exists() or latest_link.is_symlink():
                latest_link.unlink()
            
            try:
                latest_link.symlink_to(latest_file.name)
                logger.info(f"更新链接: {latest_link} -> {latest_file.name}")
            except Exception as e:
                logger.error(f"创建软链接失败: {e}")
    
    def git_commit_and_push(self, commit_message=None):
        """提交并推送到GitHub"""
        logger.info("执行Git操作...")
        
        original_cwd = os.getcwd()
        os.chdir(self.repo_path)
        
        try:
            # 检查状态
            status = subprocess.run(
                ['git', 'status', '--porcelain'],
                capture_output=True,
                text=True,
                timeout=10
            )
            
            if not status.stdout.strip():
                logger.info("没有需要提交的更改")
                os.chdir(original_cwd)
                return True
            
            # 添加文件
            subprocess.run(['git', 'add', '.'], check=True, timeout=10)
            
            # 提交
            if not commit_message:
                commit_message = f"Batch sync reports - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
            
            subprocess.run(
                ['git', 'commit', '-m', commit_message],
                check=True,
                timeout=10
            )
            
            # 推送
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
                logger.error(f"推送失败: {push_result.stderr}")
                os.chdir(original_cwd)
                return False
                
        except Exception as e:
            logger.error(f"Git操作失败: {e}")
            os.chdir(original_cwd)
            return False
    
    def sync_all(self, days_back=30):
        """同步所有报告"""
        logger.info(f"开始批量同步报告（最近 {days_back} 天）")
        
        total_synced = 0
        results = {}
        
        for report_type in self.report_configs.keys():
            synced = self.sync_report_type(report_type, days_back)
            results[report_type] = synced
            total_synced += synced
        
        # 更新软链接
        self.update_latest_links()
        
        # 如果有同步的文件，提交到GitHub
        if total_synced > 0:
            success = self.git_commit_and_push()
            if success:
                logger.info("GitHub同步成功")
            else:
                logger.error("GitHub同步失败")
        
        # 输出结果
        print("\n" + "="*50)
        print("批量同步结果:")
        print("="*50)
        for report_type, count in results.items():
            print(f"{report_type:10} {count:3} 个文件")
        print(f"\n总计: {total_synced} 个文件同步完成")
        
        return total_synced

def main():
    """主函数"""
    import argparse
    
    parser = argparse.ArgumentParser(description='批量同步历史报告到GitHub')
    parser.add_argument('--days', type=int, default=30,
                       help='同步多少天内的报告（默认：30）')
    parser.add_argument('--repo-path', help='仓库路径')
    parser.add_argument('--type', choices=['morning', 'evening', 'security', 'all'],
                       default='all', help='报告类型')
    
    args = parser.parse_args()
    
    syncer = ReportSyncer(args.repo_path)
    
    if args.type == 'all':
        total = syncer.sync_all(args.days)
        if total > 0:
            print(f"\n✅ 成功同步 {total} 个报告文件")
            sys.exit(0)
        else:
            print("\n⚠️  没有需要同步的报告文件")
            sys.exit(0)
    else:
        # 同步单个类型
        synced = syncer.sync_report_type(args.type, args.days)
        if synced > 0:
            syncer.update_latest_links()
            syncer.git_commit_and_push()
            print(f"\n✅ 成功同步 {synced} 个 {args.type} 报告")
            sys.exit(0)
        else:
            print(f"\n⚠️  没有需要同步的 {args.type} 报告")
            sys.exit(0)

if __name__ == "__main__":
    main()