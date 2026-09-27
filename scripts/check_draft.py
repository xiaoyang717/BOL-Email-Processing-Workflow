#!/usr/bin/env python3
"""校验荷兰语客服邮件正文是否符合 BOL 写作规则。

用法：
    python scripts/check_draft.py drafts/bol-klantenservice-email_20260101_120000.md

也可直接校验纯荷兰语文本：
    python scripts/check_draft.py body.txt --raw

检查项：
    1. 正文中不得出现中文字符
    2. 不得出现称呼（Beste / Geachte / Dear / Hallo ...）
    3. 不得出现签名（Met vriendelijke groet / Mvg / Kind regards ...）
    4. 不得承诺主动跟进（Zodra er een update is ... 等）
    5. 结尾应为标准句 Mocht u nog vragen hebben, neem dan gerust contact met ons op.
    6. 每个完整句子 / 独立段落单独成行（不把多句话挤在同一行）
    7. 追踪链接必须是官方 DHL 基础链接

退出码：0 = 全部通过；1 = 发现问题。
"""

import argparse
import os
import re
import sys

CLOSING = "Mocht u nog vragen hebben, neem dan gerust contact met ons op."
TRACK_URL = "https://www.dhlecommerce.nl/nl/consument/track-en-trace"

GREETING_RE = re.compile(
    r"^\s*(Beste|Geachte|Beste\s+\w|Dear|Hallo|Hi|Hey|Goedendag|Good morning|Good afternoon)\b",
    re.IGNORECASE | re.MULTILINE,
)
SIGNATURE_RE = re.compile(
    r"(Met vriendelijke groet|Vriendelijke groet|Mvg\.?|Kind regards|Best regards|"
    r"Sincerely|Groeten|Sincerely yours|Hoogachtend|Team Windvogel\s*$|Windvogel\s*$)",
    re.IGNORECASE | re.MULTILINE,
)
PROMISE_RE = re.compile(
    r"(Zodra er (?:een|nieuwe) update is|zodra we (?:meer|nader) (?:weten|horen)|"
    r"wij (?:zullen|houden) u (?:op de hoogte|ervan op de hoogte|informeren)|"
    r"we (?:will|shall) keep you (?:posted|updated)|laten wij u dit (?:direct|zo snel mogelijk) weten|"
    r"nemen wij (?:opnieuw|weer) contact met u op)",
    re.IGNORECASE,
)
CJK_RE = re.compile(r"[\u4e00-\u9fff\u3400-\u4dbf]")
URL_RE = re.compile(r"https?://\S+")

DUTCH_BODY_HEADINGS = ("邮件正文", "Dutch", "Nederlands", "荷兰语")


def extract_dutch_body(text: str) -> str:
    """从草稿 Markdown 中截取荷兰语正文部分；失败则返回整份文本。"""
    lines = text.splitlines()
    start = None
    for i, line in enumerate(lines):
        if line.lstrip().startswith("#") and any(h in line for h in DUTCH_BODY_HEADINGS):
            start = i + 1
            break
    if start is None:
        return text
    body_lines = []
    for line in lines[start:]:
        if line.lstrip().startswith("## "):
            break
        body_lines.append(line)
    return "\n".join(body_lines)


def check(body: str):
    problems = []
    warnings = []

    cjk_lines = {}
    for m in CJK_RE.finditer(body):
        line_no = body[: m.start()].count("\n") + 1
        cjk_lines.setdefault(line_no, m.group())
    for line_no in sorted(cjk_lines):
        problems.append(
            "第 %d 行出现中文字符（例如 '%s'），荷兰语正文不得包含中文" % (line_no, cjk_lines[line_no])
        )

    for m in GREETING_RE.finditer(body):
        problems.append("出现称呼 '%s'，平台会自动生成抬头" % m.group().strip())

    for m in SIGNATURE_RE.finditer(body):
        problems.append("出现签名 '%s'，平台会自动生成签名" % m.group().strip())

    for m in PROMISE_RE.finditer(body):
        problems.append("出现主动跟进承诺 '%s'，除非卖家明确要求否则禁止" % m.group().strip())

    paragraphs = [p.strip() for p in body.split("\n\n") if p.strip()]
    if not paragraphs:
        problems.append("正文为空")
        return problems, warnings

    last = paragraphs[-1]
    if CLOSING.lower() not in last.lower():
        problems.append("结尾缺少标准句：%s" % CLOSING)

    for para in paragraphs:
        if "\n" in para:
            continue
        sentences = [s for s in re.split(r"(?<=[.!?])\s+", para) if s.strip()]
        if len(sentences) > 2:
            warnings.append("同一段内有 3 句以上，建议拆分段落：'%s'" % para[:60])

    for url in URL_RE.findall(body):
        if "dhlecommerce.nl" in url and not url.startswith(TRACK_URL):
            warnings.append("DHL 追踪链接建议使用官方基础链接：%s" % TRACK_URL)
        if "postnl" in url.lower():
            warnings.append("正文中出现 PostNL 链接，请确认是否已核实该渠道为实际承运商")

    if not re.search(r"[.!?]\s*$", body.strip()):
        warnings.append("正文结尾似乎缺少句号")

    return problems, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description="校验 BOL 荷兰语客服邮件正文")
    parser.add_argument("path", help="草稿 Markdown 文件或荷兰语文本文件")
    parser.add_argument("--raw", action="store_true", help="输入为纯荷兰语文本，不做章节提取")
    args = parser.parse_args()

    if not os.path.exists(args.path):
        print("文件不存在：%s" % args.path)
        return 1

    with open(args.path, "r", encoding="utf-8") as fh:
        text = fh.read()

    body = text if args.raw else extract_dutch_body(text)
    body = body.strip()
    if not body:
        print("未找到荷兰语正文（请检查文件中是否有「## 邮件正文」章节）")
        return 1

    problems, warnings = check(body)

    print("—— 荷兰语正文 ——")
    print(body)
    print("—— 检查结果 ——")
    if warnings:
        print("[提示]")
        for w in warnings:
            print("  - %s" % w)
    if problems:
        print("[必须修正]")
        for p in problems:
            print("  - %s" % p)
        return 1
    print("全部规则校验通过。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
