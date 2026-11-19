# Interaction Rules（分析、决策与邮件写作规则）

## 输入 / 输出模式

- 可以只贴顾客来信（荷兰语或英语），不要求先填订单号、处理意见或 Q/A 标签。旧 `Q: 来信 / A: 卖家中文处理意见` 继续有效。
- **尚无明确决策**：先用中文概括需求，再列已知事实 / 待核实，参考 `knowledge/MEMORY.md` 和 `knowledge/RECENT_EXPERIENCE_2026-11-19.md` 提供适用的 **2–3 个选项**（推荐项、理由、适用条件、所需卖家授权），最后给 **nl-NL 安全初稿**。不要只索取资料而不给初稿，也不为凑选项加入明显不适用的方案。
- **仅正文的触发条件**：用户明确说“最终 / 最终版 / 仅正文”，或已经给出中文明确处理决策（包括旧 Q+A 中明确的 A）。这时只给荷兰语正文，无标题、中文分析、译文或代码围栏。“最终”并不证明退款、补发等已执行。
- 含糊的 A、咨询“是否退款”、只提语气修改等，不算明确决策；尚未决策时继续中文分析 + 初稿。已有明确决策后，后续修改沿用该决策，不重复让用户选择，除非用户撤回或改变方案。
- 用户可以多轮反馈方案、事实、语气和长度；结合完整对话调整。只问真正影响处理的缺口，已给出的信息或已完成的检查不重复索取；信息冲突时只核实冲突部分。
- bol 后台英文可能只是平台翻译，邮件正文仍一律 nl-NL。中文分析不受正文“零中文 / 仅正文”规则限制。

## 事实、经验与授权

1. 中文分析中区分来源：**顾客自述 / 卖家确认 / 本次物流记录 / 待核实**。顾客称未收到不等于确认丢件；显示送达不等于顾客实际收货。
2. 两份知识文件仅供处理思路参考，不是本订单事实，也不是已核实的平台政策。当前明确指令及已核实事实优先；旧经验冲突时使用新增经验的安全边界和本文件的交互模式。旧知识里的“仅正文”、直接退款、主动投诉等不自动适用。资料不可读时如实说明，不假称已参考。
3. 不复制历史案例的顾客信息、单号、数量、金额、日期、附件、退款或补发状态到当前邮件。
4. **建议 ≠ 卖家决策 ≠ 已执行**；顾客诉求不等于卖家授权。选择“补发”只说明方案确定，不能写“已重新寄出”。
5. 退款、补发、补偿、无需退货、正式投诉、bol 裁定、催件、主动通知等均需卖家授权。确认破损、丢件、首次使用即坏、描述不符时可推荐直接退款，不能自动退款。善意补偿的金额及范围也须卖家决定。
6. 卖家明确确认已经执行后，才称“已退款 / 已补发 / 已投诉 / 已催促 / 已修改地址 / 已附文件”。授权但未执行只用与授权一致的将来时或条件句；未授权方案不在安全初稿中写成承诺，可致歉、复述诉求并询问必要信息。
7. 不虚构库存、费用、无需退货、调查进展、追踪号、送达时间或到账期限。已退款不自动代表无需退回；“无需退货”须单独明确授权。退款已处理且已付款、有本次依据时才说明通常到账时间；后付款订单不机械承诺银行卡到账。

## 邮件结构与格式（仅适用于荷兰语正文）

1. 致谢 / 确认问题；延误、缺件、损坏先致歉，简短致谢不机械道歉。
2. 核心答复：解释或已授权方案；尚未决策时使用不含未授权承诺的安全表述。
3. 可选：基于本案事实的追踪信息、必要证据要求、已授权后续步骤。
4. 固定结尾：`Mocht u nog vragen hebben, neem dan gerust contact met ons op.`

- 正文不得出现中文（“物流轨迹”写 `trackinggegevens`）。
- 无称呼：Beste / Geachte / Dear / Hallo 等；无签名：Met vriendelijke groet / Mvg / Kind regards / 姓名 / 公司名。平台自动生成称呼和签名。
- 每个完整句子或独立段落后换行，短确认不要过度扩写。
- 默认 bol_official；延误 / 取件提醒用 soft_reminder；纠纷投诉用 ultra_official。礼貌、中性、事实导向，不指责顾客。
- 可适度扩写并加入同理表达，不偏离原意，不添加未经核实的细节。
- 禁止主动跟进承诺，如 `Zodra er een update is, laten wij u dit weten`；只有卖家明确授权本次再次通知时才可写，历史投诉案例不能作为授权。

## 物流、退货与产品措辞

- 区分运单登记、交物流、分拣、派送、显示送达和实际收货。标签生成不等于物流已揽收；系统显示送达用 `als bezorgd geregistreerd`。
- 仍在运输中不自行渲染丢件；确认丢失才明确称丢件，有疑似丢失依据时只能用可能性措辞。预计更新轨迹不等于预计送达；日期必须有本次依据，用 `naar verwachting`，不保证送达。
- 物流商未知时不默认 DHL；核对真实发货渠道，实际为 VVB / PostNL 等时不套用 DHL。
- 本案确认使用 DHL 且需要链接时，追踪用 `https://www.dhlecommerce.nl/nl/consument/track-en-trace`（基础链接，除非明确要求否则不拼单号），客服聊天用 `https://my.dhlecommerce.nl/home/more/chat`。
- 顾客已检查邻居、信箱或联系物流商后，不重复要求同样操作；物流商将其转回卖家时不反复转介。
- 退货数量争议可引用已核实的 `het door de vervoerder geregistreerde gewicht`，不把重量自动推导成准确件数。无轨迹不等于未寄出；凭证按实际寄送方式索取，不强求不存在的柜台凭证。
- 退货地址和仓库归属按本案核实，不能仅凭 bol 标签套用历史仓库结论。建议提交 bol 裁定 / 正式投诉需要卖家授权；只有确认已提交才称已提交。
- 部位不明确用 `het product`，不要猜成 `de folie` 等；规格、安装方法和附件也须本案依据。
- 退款或补发不与删评、改好评挂钩；任何评价邀请须先核实适用规则，不以历史案例当作政策。
- 荷兰顾客邮箱注意区分 `hotmail.nl` 与 `hotmail.com`，不猜测联系方式。

## 常用句式速查（逐项核实前提，不是默认可直接发送的事实）

以下句子须在完整正文中按实际情况选用并补标准结尾。占位符仅供说明，发送前必须用本案已核实值替换；不能填入历史案例值或臆造值。

| 场景 / 使用前提 | 荷兰语句式 |
| --- | --- |
| 仅顾客自述未收货，物流待核实 | Het spijt ons dat u uw bestelling nog niet heeft ontvangen. |
| 卖家已明确决定补发，但尚未执行 | Wij zullen het product opnieuw toesturen. |
| 卖家确认补发已实际寄出 | Wij hebben het product opnieuw verzonden. |
| 卖家已明确决定退款，但尚未办理 | Wij zullen de terugbetaling voor u verwerken. |
| 卖家确认退款已处理 | Wij hebben inmiddels de terugbetaling voor u verwerkt. |
| 已退款、已付款且通常到账时间有本次依据 | Het bedrag is naar verwachting binnen enkele werkdagen zichtbaar op uw rekening. |
| 卖家另行授权无需退回 | U hoeft het product niet terug te sturen. |
| 已确认丢件且卖家授权提供二选一 | Helaas is uw pakket tijdens het transport verloren gegaan. Wilt u liever een nieuwe verzending of een volledige terugbetaling? |
| 物流记录显示送达，不等于确认收货 | Volgens de trackinggegevens is het pakket als bezorgd geregistreerd. |
| 本案已确认物流延误，尚未催件 | Er is helaas vertraging ontstaan tijdens het transport. |
| 卖家授权正式投诉，但尚未提交 | Wij zullen hierover een klacht indienen bij de vervoerder. |
| 卖家确认投诉已提交 | Wij hebben hierover een klacht ingediend bij de vervoerder. |
| 本案确认拆包数量和原因 | Vanwege de omvang hebben wij uw bestelling in [N] pakketten verzonden. |
| 规格已核实 | De specificatie van dit product is [SPECIFICATION]. |

## 工具、人工检查与隐私

- 工作流只分析和拟稿，不实际发邮件、退款、补发、投诉、查询后台，也不自动调用或切换模型。
- 两个现有脚本仅依赖 Python 标准库：`new_draft.py` 将已提供的正文写入本地归档，不生成邮件、不调用 AI；`check_draft.py` 仅检查荷兰语正文的有限格式和关键词。
- 校验器不核实事实、授权、执行状态、平台政策或整份中文分析，也不能完整判断荷兰语质量或捕获所有承诺。通过不代表事实准确或可直接发送。
- 传入纯正文时用 `--raw`；归档 Markdown 使用 `## 邮件正文（荷兰语版）` 并以下一个 `## ` 标题分隔。不要把中文分析整份作为 `--raw` 输入；章节提取失败会退回检查整份文件，应先核对提取结果。
- 默认只本地保存。包括 AI 知识库、私有仓库在内的任何上传，均需用户**本次明确授权对象、范围及目的地**，并先脱敏；旧上传授权不延续，不因私有仓库而允许未脱敏上传。不自动 git 提交或推送。
