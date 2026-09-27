# BOL 客服邮件处理工作流（BOL Email Processing Workflow）

一套面向 **bol.com 荷兰站卖家** 的客服邮件起草工作流。把过去一年积累的写作规则、业务口径、场景模板和真实案例沉淀成可直接复用的配置文件，让任意一台电脑（或任意一个 AI 客户端）克隆后都能**按同一套标准**产出荷兰语客服邮件。

- 输入：顾客来信（荷兰语 / 英语）＋ 卖家中文处理意见
- 输出：**仅荷兰语邮件正文**（不含称呼与签名，因为 bol.com 平台会自动生成）
- 目标：语气统一、事实准确、合规不踩坑、换机不丢经验

---

## 一、目录结构

```
BOL-Email-Processing-Workflow/
├── README.md                    # 本文件：流程说明
├── config/                      # 规则配置（工作流的"大脑"）
│   ├── bootstrap_prompt.txt     # 系统提示词：贴给任意 AI 客户端即可复现全部写作规则
│   ├── interaction_rules.md     # 硬性写作规则 + 常用荷兰语句式速查表
│   ├── preferences.yaml         # 输出语言 / 格式 / 语气 / 退款与争议策略
│   ├── persona.json             # 卖家身份与语言对（zh-CN → nl-NL）
│   └── domain_context.md        # 业务背景：品类、物流商、bol 规则、退货退款口径
├── templates/nl/                # 荷兰语场景模板（10 个高频场景，含占位符与变体）
├── knowledge/MEMORY.md          # 长期经验库（脱敏版）：真实案例沉淀的处理口径
├── samples/                     # 8 个真实邮件归档样本（含中文说明与荷兰语正文）
├── scripts/
│   ├── new_draft.py             # 生成带时间戳的草稿文件
│   └── check_draft.py           # 校验正文是否符合全部硬性规则
└── drafts/                      # 日常产出的邮件草稿（本地生成，可按需提交）
```

---

## 二、快速开始（换一台电脑只需 3 步）

```bash
git clone https://github.com/xiaoyang717/BOL-Email-Processing-Workflow.git
cd BOL-Email-Processing-Workflow
python scripts/check_draft.py samples/01-lost-package-refund.md   # 验证环境可用
```

要求：Python 3.8+，**无需任何第三方依赖**（脚本只用标准库）。Windows / macOS / Linux 均可运行。

---

## 三、完整流程（每次处理一封顾客邮件）

### 第 1 步：装载系统提示词

把 `config/bootstrap_prompt.txt` 的全文作为系统提示词贴给 AI（ChatGPT、Claude、WorkBuddy 等任意客户端均可）。该文件包含 14 条规则：语言、格式、语气、结构、扩写、换行、禁止承诺、退款前置询问、追踪链接、重量证据、不猜测部件、不指责顾客、物流措辞。

> 若客户端支持"项目知识库"，建议同时把 `config/interaction_rules.md`、`config/domain_context.md`、`knowledge/MEMORY.md` 一起放入上下文，命中率更高。

### 第 2 步：投喂素材

按以下格式提供输入：

```
Q: <顾客来信原文，荷兰语或英语；如有物流状态，一并贴出>
A: <卖家中文处理意见，例如"物流商可能丢件，订单已退款">
```

### 第 3 步：拿到荷兰语正文

AI 只输出邮件正文。生成后请人工确认：

- 顾客姓名、订单号、追踪号、日期等事实是否准确
- 处理方案是否与卖家意见一致
- 是否需要补 DSB 链接或取证要求

### 第 4 步：自动校验

```bash
python scripts/check_draft.py drafts/bol-klantenservice-email_20260101_120000.md
```

校验项：中文字符、称呼、签名、主动跟进承诺、标准结尾句、分行、追踪链接。全部通过输出 `全部规则校验通过。`，有问题则以退出码 1 列出。

### 第 5 步：归档草稿

```bash
python scripts/new_draft.py --title "包裹丢失已退款" \
  --scenario "PostNL 追踪显示未领取，疑似丢件" \
  --decision "直接退款，无需退回商品" \
  --body-file body.txt
```

生成 `drafts/bol-klantenservice-email_YYYYMMDD_HHMMSS.md`，文件内含：场景、处理决策、荷兰语正文、中文翻译、措辞要点。

### 第 6 步：回流经验

遇到新场景或新口径时，补写进 `knowledge/MEMORY.md`（脱敏后再提交），并视情况补充 `templates/nl/`。经验库是工作流能持续变准的关键。

---

## 四、硬性规则（不可违反）

| 规则 | 说明 |
| --- | --- |
| 荷兰语输出 | 正文零中文字符，"物流轨迹"写 `trackinggegevens` |
| 无称呼 | 不写 Beste / Geachte / Dear / Hallo |
| 无签名 | 不写 Met vriendelijke groet / Mvg / 姓名 / 公司名 |
| 段后换行 | 每个完整句子或独立段落后换行 |
| 禁止承诺跟进 | 不写 `Zodra er een update is, laten wij u dit weten` 及同类表述 |
| 标准结尾 | `Mocht u nog vragen hebben, neem dan gerust contact met ons op.` |
| 退款前置 | 除确认破损 / 丢件 / 首次使用即坏 / 善意补偿外，先问顾客退款还是补发 |
| 部件不确定 | 无法判断具体部位时用 `het product`，不要写 `de folie` 等 |
| 重量证据 | 退货数量争议引用 `het door de vervoerder geregistreerde gewicht` |
| 追踪链接 | `https://www.dhlecommerce.nl/nl/consument/track-en-trace`（不拼单号） |
| DHL 客服 | `https://my.dhlecommerce.nl/home/more/chat` |
| 不指责顾客 | 事实导向，保持礼貌与中性 |

标准退款告知句：

```
Wij hebben inmiddels de terugbetaling voor u verwerkt. Het bedrag wordt binnen enkele werkdagen zichtbaar op uw rekening.
```

---

## 五、场景模板索引

| 文件 | 场景 |
| --- | --- |
| `templates/nl/01-refund-confirmation.md` | 退款确认、无需退回 |
| `templates/nl/02-refund-not-received.md` | 退款未到账 |
| `templates/nl/03-lost-package.md` | 包裹丢失（退款 / 补发 / 二选一） |
| `templates/nl/04-shipment-delay.md` | 物流延迟、预计送达 |
| `templates/nl/05-pickup-point-reminder.md` | 取件点提醒、未取退回 |
| `templates/nl/06-split-shipment.md` | 拆单发货、多追踪号 |
| `templates/nl/07-return-dispute.md` | 退货数量争议、未收到退货 |
| `templates/nl/08-quality-issue.md` | 破损、色差、尺寸、墙板脱落 |
| `templates/nl/09-address-cancel-refuse.md` | 地址修改、取消、拒收、非本店商品 |
| `templates/nl/10-invoice-and-misc.md` | 发票、差评跟进、主动通知 |

---

## 六、隐私与脱敏说明

`knowledge/MEMORY.md` 由本地工作区的经验库**脱敏后**生成：

- 真实顾客姓名 → `[KLANT]`
- 订单号 → `ORDER-NR`
- DHL / PostNL 追踪号 → `JVGL-XXXX` / `3SBLCR-XXXX`
- bol 案件号 → `CASE-ID`
- 邮箱地址 → `[E-MAIL]`

业务口径、处理逻辑与决策依据**完整保留**，不影响工作流效果。若当前仓库为公开仓库，请始终保持这一脱敏约定；如需要使用未脱敏版本，建议将仓库设为私有后再覆盖本文件。

---

## 七、使用小贴士

- bol.com 后台会把顾客邮件自动翻译成英文供卖家查看，**英文正文不等于顾客用英文沟通**，回复仍一律使用荷兰语。
- 使用 bol.com 官方退货标签的包裹会先到 bol 仓库，而不是商家退货地址，核验退货凭证时不要误判为异常。
- 追踪信息在不同渠道不一致时，以实际发货方（如 VVB / PostNL）的记录为准。
- 荷兰顾客邮箱注意区分 `hotmail.nl` 与 `hotmail.com`。
- 物流仍在运输途中时不要对顾客说"可能丢件"；给出送达日期一律使用"预计"语气。
