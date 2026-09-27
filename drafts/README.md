# drafts/

日常产出的荷兰语客服邮件草稿存放目录。

文件命名规范：`bol-klantenservice-email_YYYYMMDD_HHMMSS.md`

生成方式：

```bash
python scripts/new_draft.py --title "场景标题" --scenario "顾客来信与背景" --decision "处理决策"
```

校验方式：

```bash
python scripts/check_draft.py drafts/<文件名>.md
```

本目录中的草稿可能包含订单号、追踪号等真实业务信息；在公开仓库中提交前请先确认是否已脱敏。
