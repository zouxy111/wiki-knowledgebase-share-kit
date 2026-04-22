#!/usr/bin/env python3
"""
创建每日工作记录文件
用法: python create_daily_journal.py --date YYYY-MM-DD [--project 项目名]
"""

from __future__ import annotations

import argparse
import json
from datetime import datetime, date
from pathlib import Path


def yaml_quote(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def create_journal_file(
    journal_dir: Path, target_date: date, project: str | None = None
) -> Path:
    year_month = target_date.strftime("%Y-%m")
    month_dir = journal_dir / year_month
    month_dir.mkdir(parents=True, exist_ok=True)

    filename = f"{target_date.strftime('%Y-%m-%d')}.md"
    filepath = month_dir / filename

    if filepath.exists():
        return filepath

    date_str = target_date.strftime("%Y-%m-%d")
    projects_line = f"projects: [{yaml_quote(project)}]" if project else "projects: []"

    content = f"""---
title: "{date_str} 工作记录"
type: "journal"
date: "{date_str}"
{projects_line}
people: []
tags: []
---

# {date_str} 工作记录

## 时间线

<!-- 在此添加会议、想法、进展等记录 -->

---

## 今日项目关联

| 项目 | 今日进展 | 相关知识页 |
|------|---------|-----------|
<!-- 自动填充 -->

---

## 今日人名参与

| 人名 | 参与事件 | 备注 |
|------|---------|------|
<!-- 自动填充 -->
"""

    filepath.write_text(content, encoding="utf-8")
    return filepath


def main() -> int:
    parser = argparse.ArgumentParser(description="创建每日工作记录文件")
    parser.add_argument("--date", help="目标日期 YYYY-MM-DD，默认今天")
    parser.add_argument("--journal-dir", default="journals", help="journal 目录路径")
    parser.add_argument("--project", help="关联项目名称")
    parser.add_argument("--vault-root", help="Vault 根目录路径（可选）")
    args = parser.parse_args()

    if args.date:
        target_date = datetime.strptime(args.date, "%Y-%m-%d").date()
    else:
        target_date = date.today()

    if args.vault_root:
        journal_dir = Path(args.vault_root) / args.journal_dir
    else:
        journal_dir = Path(args.journal_dir)

    filepath = create_journal_file(journal_dir, target_date, args.project)
    print(f"创建记录文件: {filepath}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
