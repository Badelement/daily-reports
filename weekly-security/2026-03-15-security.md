---
title: 2026-03-15 安全笔记
type: security
date: 2026-03-15
tags: [openclaw, automation]
synced_at: 2026-03-20 12:21:29
synced_by: batch_sync
---

# 2026-03-15 AI Agent 安全学习笔记

## 1）这周最重要的安全认识
OpenClaw gateway 默认运行在本地回环地址（127.0.0.1）但未配置认证，导致浏览器控制接口和HTTP API完全无认证。任何本地进程或SSRF攻击都可调用敏感端点。安全审计显示2个关键问题：gateway.loopback_no_auth 和 browser.control_no_auth。这暴露了"本地即安全"的认知误区——即使绑定到loopback，仍需基础认证层防止本地恶意进程滥用。

## 2）这周最值得警惕的风险点
技能供应链风险：当前环境安装了5个自定义技能（agentic-compass、find-skills、self-improving-agent、knowledge-sync、openclaw-history-viewer、video-transcript-pdf），均来自本地workspace而非clawhub.com官方源。这些技能拥有与主agent相同的文件系统访问权限，但缺乏代码审计和版本控制。特别是knowledge-sync技能涉及文件监控和Git操作，若被恶意修改可能造成数据泄露或破坏。

## 3）这周最值得补的一项能力
自动化安全基线检查能力。当前依赖手动运行`openclaw security audit`，但应建立定期自动化检查：1) 网关认证状态监控，2) 技能文件完整性校验，3) 端口暴露情况检测，4) 权限配置审计。缺少这项能力意味着安全配置漂移无法及时发现，如gateway.auth配置丢失或技能被意外修改。

## 4）下周最值得做的一步
立即修复gateway认证缺口：运行`openclaw security audit --fix`启用自动生成的token认证，或手动配置`gateway.auth.token`。这是当前最紧迫的暴露面，修复后能立即消除无认证API访问风险。同时建立每周安全审计cron任务，确保配置持续合规。

*报告字数：约350字*