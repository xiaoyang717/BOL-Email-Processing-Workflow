#!/usr/bin/env python3
"""创建一封新的荷兰语客服邮件草稿文件。

用法：
    python scripts/new_draft.py --title "包裹丢失已退款" \
        --scenario "PostNL 追踪显示未领取，物流商可能丢件，订单已退款" \
        --decision "直接退款，无需退回商品"

    python scripts/new_draft.py --title "..." --scenario "..." --decision "..." --body body.txt

生成文件路径：drafts/bol-klantenservice-email_YYYYMMDD_HHMMSS.md
生成后可用 scripts/check_draft.py 校验正文是否符合规则。
"""

import argparse
import datetime
import os
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DRAFT_DIR = os.path.join(REPO_ROOT, "drafts")
TEMPLATE = """# {title}

**记录时间**: {timestamp} GMT+8
**场景**: {scenario}
**处理决策**: {decision}

## 邮件正文（荷兰语版）

{body}

## 中文翻译

（待补充）

## 措辞要点

- ✅ 不带称呼（Beste / Geachte / Dear）
- ✅ 不带结尾签名（Met vriendelijke groet 等）
- ✅ 每个完整句子或段落后换行
- ✅ 不主动承诺后续联系
- ✅ 荷兰语正文中不含中文字符
"""


def now_str() -> str:
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M")


def file_stamp() -> str:
    return datetime.datetime.now().strftime("%Y%m%d_%H%M%S")


def main() -> int:
    parser = argparse.ArgumentParser(description="创建 BOL 荷兰语客服邮件草稿")
    parser.add_argument("--title", required=True, help="草稿标题，例如：包裹丢失已退款")
    parser.add_argument("--scenario", default="", help="顾客来信与背景说明")
    parser.add_argument("--decision", default="", help="卖家的处理决策")
    parser.add_argument("--body", default="", help="荷兰语邮件正文；也可通过 --body-file 传入文件")
    parser.add_argument("--body-file", default="", help="包含荷兰语正文的文本文件路径")
    args = parser.parse_args()

    body = args.body
    if args.body_file:
        with open(args.body_file, "r", encoding="utf-8") as fh:
            body = fh.read().strip()
    if not body:
        body = "（在此粘贴荷兰语邮件正文）"

    os.makedirs(DRAFT_DIR, exist_ok=True)
    path = os.path.join(DRAFT_DIR, "bol-klantenservice-email_%s.md" % file_stamp())
    content = TEMPLATE.format(
        title=args.title,
        timestamp=now_str(),
        scenario=args.scenario,
        decision=args.decision,
        body=body,
    )
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(content)

    print(path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
