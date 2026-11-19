# BOL 客服邮件处理工作流（BOL Email Processing Workflow）

面向 **bol.com 荷兰站卖家** 的客服分析与邮件起草工作流，将写作规则、处理思路和脱敏案例保存在本地，供用户在选定 AI 客户端中使用。

- 输入：**仅贴顾客来信也可**（荷兰语 / 英语）；可附物流记录、中文处理意见，兼容旧 Q+A。
- 默认输出：**中文需求分析 → 已知事实 / 待核实 → 适用的 2–3 个处理选项（推荐、理由、条件及授权）→ nl-NL 安全初稿**。
- 用户可多轮反馈修改；只有明确要求“最终 / 最终版 / 仅正文”，或已经给出中文明确处理决策时，才输出**仅荷兰语正文**，无称呼与签名。
- 目标：辅助卖家决策和拟稿，不虚构事实、退款、补发或物流承诺。**建议 ≠ 执行**，只有卖家确认已执行，才称已退款、已补发等。
- 不实际发邮件、退款、补发、投诉或查询后台，不自动调用 / 切换模型。配置不是自动化执行程序。

---

## 一、目录结构

```text
BOL-Email-Processing-Workflow/
├── README.md                    # 流程说明及多轮案例
├── config/
│   ├── bootstrap_prompt.txt     # 交互、事实边界及邮件写作提示词
│   ├── interaction_rules.md     # 详细规则与带使用前提的句式
│   ├── preferences.yaml         # 分阶段输出、授权与隐私配置
│   ├── persona.json             # 卖家身份与语言对
│   └── domain_context.md        # 业务背景参考，具体事实与政策须核实
├── templates/nl/                # 场景模板，使用前核实本案前提
├── knowledge/
│   ├── MEMORY.md                # 长期脱敏经验，仅作参考
│   └── RECENT_EXPERIENCE_2026-11-19.md # 新增经验及安全边界
├── samples/                     # 历史归档样本，不是当前订单事实
├── scripts/
│   ├── new_draft.py             # 归档用户提供的正文，不生成邮件
│   └── check_draft.py           # 有限的正文格式 / 关键词检查
└── drafts/                      # 默认仅本地保存的草稿
```

## 二、快速开始

已有工作区可直接使用；新电脑可克隆项目后运行已有样本的格式检查：

```bash
git clone https://github.com/xiaoyang717/BOL-Email-Processing-Workflow.git
cd BOL-Email-Processing-Workflow
python scripts/check_draft.py samples/01-lost-package-refund.md
```

要求：Python 3.8+，脚本**仅用标准库，无第三方依赖**。Windows / macOS / Linux 均可运行。示例检查只验证脚本可运行，不证明历史样本中的事实适用于当前订单。

## 三、完整流程

### 第 1 步：装载提示词与参考

在用户选定的 AI 客户端中，将 `config/bootstrap_prompt.txt` 用作系统提示词，并在授权范围内提供 `config/interaction_rules.md`、`config/preferences.yaml`、`knowledge/MEMORY.md` 和 `knowledge/RECENT_EXPERIENCE_2026-11-19.md`。业务背景及模板可按需参考。

若将本地资料上传到 AI 项目知识库，必须先取得**本次明确上传授权**并脱敏；也可在不上传的本地环境使用。资料不可读时应说明缺失，不声称已参考。

两份知识文件只提供思路，不是本订单事实或平台政策。当前明确指令、已核实事实优先；旧经验冲突时，以新增经验的安全边界和当前配置的交互模式为准。旧资料中的默认仅正文、直接退款、主动投诉等不能覆盖本流程。

### 第 2 步：直接贴来信，或沿用旧 Q+A

只贴原文即可，不强制填写订单号或先想好方案。已有信息尽量一并贴出，后续不应重复索取。

旧格式仍兼容：

```text
Q: <顾客来信原文；可附本次已核实物流记录>
A: <卖家中文处理意见，例如“已完成退款，无需退回”>
```

A 是明确决策时直接给荷兰语正文；A 缺省或只是“如何处理 / 要不要退款”等咨询时，先分析选项并给安全初稿。中文明确决策不等于已执行，例如“决定退款”不能写成“已退款”。

### 第 3 步：分析、选项与安全初稿

尚未决策时，依次输出：

1. **中文需求**：概括顾客诉求及需要回应的问题。
2. **已知事实 / 待核实**：标明顾客自述、卖家确认或本次物流记录；单独辨别售后执行状态。
3. **2–3 个适用选项**：标出推荐、理由、条件和所需卖家授权，不机械凑不适用方案。
4. **nl-NL 安全初稿**：只使用本案事实及已授权表达。未授权时可致歉、复述诉求及询问关键缺口，不承诺退款、补发、无需退货、投诉、催件或再次通知。

不要因信息不全就只列问题而不给初稿；不要将历史单号、金额、日期或处理结果带入当前邮件。顾客自述未收到不等于确认丢件，显示送达也不等于实际收货。

### 第 4 步：多轮优化与仅正文模式

用户可选择方案、补充事实、改变语气或要求精简。沿用对话里已确认的信息和决策，只问影响处理的关键缺口；有矛盾时只核实冲突，不让用户或顾客重复已回答的问题或已完成的检查。

- 明确要求“最终 / 仅正文”，或已有中文明确决策：只给荷兰语正文，不加标题、中文分析、译文或代码围栏。
- 只有语气反馈、含糊意见且仍未决策：继续中文分析 + 初稿。
- **最终不等于已执行**。卖家授权但尚未执行时，只写与授权一致的将来时 / 条件句；明确确认已执行后才改完成时。
- 实际发送、退款、补发和投诉仍由卖家自行完成，本工作流不执行。

### 第 5 步：人工核对与格式检查

人工确认来源、订单 / 追踪号、数量、日期、方案授权、执行状态、付款方式和附件是否真实，再检查荷兰语正文：

```bash
# 纯荷兰语正文；body.txt 为用户准备的正文文件
python scripts/check_draft.py body.txt --raw
# 已归档的 Markdown，脚本尝试提取正文章节
python scripts/check_draft.py drafts/bol-klantenservice-email_20260101_120000.md
```

`check_draft.py` 仅做**有限格式 / 关键词检查**：中文字符、称呼、签名、部分主动跟进措辞、标准结尾，并对部分分行与链接问题提示。它**不检查事实、授权、退款 / 补发是否执行、平台政策、整份中文分析，也不完整评估荷兰语或全部承诺**。

归档正文应置于 `## 邮件正文（荷兰语版）` 下，并以下一个 `## ` 标题分隔；未找到正文标题时脚本会退回检查整份文本，务必核对其打印的提取结果。不要把中文分析整份传给 `--raw`。

`全部规则校验通过。` 只表示未发现脚本能识别的格式问题，不代表事实正确或可以直接发送；退出码 1 表示发现问题，部分提示并不导致失败。即使卖家授权了通知，关键词检查仍可能报错，须人工审阅，不能将它当作完整规则引擎。

### 第 6 步：按需本地归档

```bash
python scripts/new_draft.py --title "补发方案待执行" \
  --scenario "顾客自述未收到，实际物流状态待核实" \
  --decision "卖家已选择补发，尚未执行" \
  --body-file body.txt
```

`new_draft.py` 只是把已提供的正文及场景 / 决策写入 `drafts/bol-klantenservice-email_YYYYMMDD_HHMMSS.md`，不生成邮件、不调用模型、不检查事实。中文翻译为待补充占位，内置措辞要点也不是检查结论。两个脚本均不读取配置来执行售后动作。

新经验可在用户要求时另行整理、脱敏并本地保存；归档、上传和 Git 操作是不同动作，不自动连带执行。

## 四、多轮案例：只贴来信 → 选补发未执行 → 确认已补发 → 最终

以下为虚构的脱敏教学对话，不代表任何真实订单状态。每个荷兰语示例均无称呼、签名。

### 第 1 轮：仅贴顾客来信

用户：

> Ik heb mijn bestelling nog niet ontvangen. Ik heb al bij de buren en in de brievenbus gekeken, maar niets gevonden. Kunt u mij helpen?

助手（中文分析 + 选项 + 安全初稿）：

- **需求**：顾客希望解决未收到订单的问题。
- **已知**：顾客自述未收货，已查邻居和信箱，不应再要求同样检查。
- **待核实**：本次实际物流状态、是否已有售后处理、补发库存。未确认丢件，未获退款或补发授权。
- **参考**：长期经验提供退款 / 补发思路；新增经验要求避免重复检查，区分记录与收货，按卖家授权处理。
- **选项 1（推荐）**：先由卖家核对当前物流及投递凭证。适合物流状态不明；需卖家同意并自行核查，未核查不能写“已调查”。
- **选项 2**：卖家确认库存及补发条件后安排补发。适合顾客仍需要商品；需要卖家明确选择，选择不等于已寄出。
- **选项 3**：卖家评估后退款。适合无法履约或顾客不愿继续等待；退款及无需退货分别确认，未办理不能写已退款。

**荷兰语安全初稿**：

```text
Het spijt ons dat u uw bestelling nog niet heeft ontvangen.
U geeft aan dat u al bij de buren en in de brievenbus heeft gekeken, maar het pakket niet heeft gevonden.
Wij begrijpen dat dit vervelend voor u is.
Mocht u nog vragen hebben, neem dan gerust contact met ons op.
```

此稿不虚构物流状态，不声称已经调查，也未把待选方案承诺给顾客；卖家决策后再补充实质方案。

### 第 2 轮：选补发，但尚未执行

用户：“选补发，库存有，我决定给顾客补发，但还没实际寄出。”

助手（已有中文明确决策，仅正文；将来时不冒充已寄出）：

```text
Het spijt ons dat u uw bestelling nog niet heeft ontvangen.
Wij zullen het product opnieuw toesturen.
Mocht u nog vragen hebben, neem dan gerust contact met ons op.
```

### 第 3 轮：卖家确认已补发

用户：“现在已经补发并实际交给物流商了，还没有提供追踪号。”

助手（沿用决策，仅正文；可以使用已寄出，不编造单号、日期或通知承诺）：

```text
Het spijt ons dat u uw bestelling nog niet heeft ontvangen.
Wij hebben het product opnieuw verzonden.
Mocht u nog vragen hebben, neem dan gerust contact met ons op.
```

### 第 4 轮：最终

用户：“最终，仅正文，保持简短。”

助手实际只输出以下正文（此处代码框仅供 README 展示，实际回复不带代码框或标题）：

```text
Het spijt ons dat u uw bestelling nog niet heeft ontvangen.
Wij hebben het product opnieuw verzonden.
Mocht u nog vragen hebben, neem dan gerust contact met ons op.
```

如果用户在第 1 轮后直接要求“最终”，也只能给不含未授权承诺的安全正文，不能因此视为已补发或已退款。

## 五、硬性规则

| 规则 | 说明 |
| --- | --- |
| 分阶段输出 | 未决策先中文分析 + 2–3 选项 + 安全初稿；明确最终 / 仅正文或中文明确决策后仅正文 |
| 荷兰语正文 | nl-NL，零中文，无称呼、签名；中文分析不受零中文限制 |
| 换行及语气 | 每个完整句子或独立段落后换行，礼貌、中性、不指责顾客 |
| 标准结尾 | `Mocht u nog vragen hebben, neem dan gerust contact met ons op.` |
| 执行状态 | 只有卖家确认已执行，才写已退款、已补发、已投诉、已催促等 |
| 退款与补发 | 先建议 / 由卖家选择；破损、丢件等也不自动退款，仍需授权 |
| 无需退货 | 须卖家单独明确授权，不由退款状态自动推导 |
| 主动通知 / 投诉 | 需要本次卖家明确授权；待提交投诉不能称已提交，不擅自承诺跟进 |
| 物流 | 标签不等于揽收，扫描送达不等于实际收到，预计更新不等于送达；日期有本案依据才用预计语气 |
| 链接 | 先确认实际承运商；DHL 使用现有官方基础链接，不自行拼接单号 |
| 部件与证据 | 不确定部件用 `het product`；重量不能单独证明准确件数，无轨迹不等于未寄出 |
| 历史经验 | 仅参考，不套用旧事实、政策或执行结果，不重复索取已提供信息 |

仅当卖家确认本次退款已处理时可使用：

```text
Wij hebben inmiddels de terugbetaling voor u verwerkt.
```

是否补充到账预期取决于本次依据及付款状态；后付款订单不机械承诺银行卡到账。

## 六、场景模板索引

旧模板保留，但使用前须按当前授权、事实和执行状态调整，不直接复制其中“已执行”或承诺句。

| 文件 | 场景 |
| --- | --- |
| `templates/nl/01-refund-confirmation.md` | 已确认退款、经授权无需退回 |
| `templates/nl/02-refund-not-received.md` | 退款未到账 |
| `templates/nl/03-lost-package.md` | 包裹丢失（退款 / 补发 / 二选一） |
| `templates/nl/04-shipment-delay.md` | 物流延迟、预计送达 |
| `templates/nl/05-pickup-point-reminder.md` | 取件点提醒、未取退回 |
| `templates/nl/06-split-shipment.md` | 拆单发货、多追踪号 |
| `templates/nl/07-return-dispute.md` | 退货数量争议、未收到退货 |
| `templates/nl/08-quality-issue.md` | 破损、色差、尺寸、墙板脱落 |
| `templates/nl/09-address-cancel-refuse.md` | 地址修改、取消、拒收、非本店商品 |
| `templates/nl/10-invoice-and-misc.md` | 发票、差评跟进、主动通知 |

## 七、隐私、存储与授权

**默认仅本地保存**，不自动上传、不自动 git 提交或推送。上传到 AI 客户端知识库、GitHub 或其他远程服务前，必须取得用户**本次对上传对象、范围、目的地的明确授权**，并先脱敏；历史授权仅限原次范围，不可沿用。

即使仓库是私有的，也不应上传未脱敏来信或用未脱敏材料覆盖远程文件。对知识文件中旧的“复制未脱敏版本覆盖”建议，不按上传许可执行。

脱敏示例：真实姓名 → `[KLANT]`，订单号 → `ORDER-NR`，追踪号 → `JVGL-XXXX` / `3SBLCR-XXXX`，案件号 → `CASE-ID`，邮箱 → `[E-MAIL]`。地址、电话及附件同样应移除或替换可识别信息，保留处理逻辑即可。

## 八、使用小贴士

- bol 后台可能自动显示英文翻译，回复仍用荷兰语。
- 退货标签上的实际地址需要核实，不因历史 bol 仓库案例作通用判断。
- 渠道冲突时先核对实际发货方及承运商，不默认 DHL。
- 注意 `hotmail.nl` 与 `hotmail.com` 的区别，不猜测联系方式。
- 顾客要求退款应正面回应，但最终方案由卖家确认，不能把新物流扫描当作顾客同意等待。
- 正文格式检查通过不代替人工审核，也不意味着邮件已发送或售后已执行。
