# CH-04 Scene Flow

## Flow tổng

`S01 Đường đá vỡ`
`-> S02 Hồn bị bắt trong lông vũ`
`-> S03 Bản đồ bộ tộc mất tên`
`-> S04 Phán quyết trên vực`
`-> B04 Đại Bàng Tinh`
`-> S05 Lệ đá rơi xuống mây`
`[tùy chọn] CH-04-HIDDEN Khe đá dựng -> HB-04 Tù Trưởng Lệ Đá`

## CH-04-S01: Đường đá vỡ

### Purpose

Chuyển ngôn ngữ di chuyển từ nước (CH-01) sang **chiều thẳng đứng và gió**; gieo không khí "nơi bị bỏ quên" và câu hỏi "ai đã bị đày lên đây?".

### Entry

- Đã có Rìu Thần Thạch Sơn (từ CH-01), `LG-01..LG-03` tùy tiến trình.
- Yêu khí biểu hiện như **đứt gãy trọng lực**: bụi đá rơi ngược, sương treo lơ lửng, bậc thang lệch.

### Beats

1. Chân núi: một cổng đá gãy (Thạch Môn), nửa chữ khắc đã bị đục mất.
2. Gió đổi hướng theo nhịp không đều; có lúc đẩy người chơi lên, có lúc hút ra vực.
3. Dấu móng chim khổng lồ cào trên đá — không khớp với bất kỳ loài nào người chơi từng thấy.
4. Trên cao, một bóng che thoáng qua mặt trời rồi biến mất trong sương.
5. Tutorial `Thế Đột` trên bệ đá hẹp: đâm trụ để không bị gió thổi rơi.

### Exit

Người chơi lên được tầng đá thứ nhất, thấy một "rừng" vật thể cắm trên mép vực — hóa ra là **lông chim lớn**, mỗi chiếc to như mái chèo.

### Choice

Không có choice chính. Khám phá tùy chọn: đọc nửa chữ khắc còn lại trên cổng đá (mở lore fragment về một dân tộc từng sống ở đây), không đổi state.

## CH-04-S02: Hồn bị bắt trong lông vũ

### Purpose

Cho người chơi thấy **cái giá** của phẫn nộ: những linh hồn bị xóa tên bị kẹt trong lông Đại Bàng, vừa là nạn nhân vừa là nhiên liệu của cơn giận. Giới thiệu lựa chọn mercy/instrument đầu tiên.

### Beats

1. Mỗi chiếc lông vũ phát sáng mờ; bên trong có bóng người co lại, miệng mở mà không ra tiếng.
2. Một hồn tỉnh táo hơn các hồn khác, nhận ra ấn rồng trên tay Long Nhân và **sợ** — tưởng Long Nhân là kẻ cai trị mới đến xóa nốt họ.
3. Gió mạnh lên; vài chiếc lông rung như sắp gãy, hồn bên trong sẽ rơi xuống vực nếu lông gãy.
4. Người chơi học cách dùng `Lôi Kích` nhẹ để đánh thức một hồn đủ lâu cho nó nói một cái tên.

### Primary choice: `C-CH04-001`

**Giải thoát hồn khỏi lông (chậm, rủi ro)**

- Người chơi đỡ từng chiếc lông, cắt "gân" yêu khí giữ hồn, để hồn tan thành sương sáng.
- `mercy_marks +1` (một lần, cho cả cụm), `tribal_trust +1`.
- Mở clue `TRUTH_EXILE_WAS_ERASED` (A): "họ không chết vì thú dữ; họ chết vì bị gạch tên".
- Làm yếu một phần "nhiên liệu" của Đại Bàng — boss fight sau này có ít projectile hồn hơn.

**Giữ hồn làm mồi khiên (nhanh, thực dụng)**

- Người chơi bẻ lông, dồn hồn về phía ổ để dụ Đại Bàng lộ diện sớm.
- `dragon_hunger +1` **chỉ khi** người chơi sau đó chọn cưỡng đoạt; bản thân choice không tự kết tội.
- Mở arena sớm, nhưng Đại Bàng vào trận **giận dữ hơn** (phase gắt hơn, nhiều đòn bổ nhào).
- Hồn bị dùng làm mồi sẽ không còn ở S05 để "về"; hậu cảnh lạnh hơn.

### Exit

Hai nhánh đều dẫn lên tầng đá cao hơn, nơi có ánh lửa trại và tiếng người — dấu hiệu của **bộ tộc bị ruồng bỏ** còn sót.

## CH-04-S03: Bản đồ bộ tộc mất tên

### Purpose

Biến lore thành **lời chứng**. Người chơi gặp những linh hồn/descendant của bộ tộc bị xóa và hiểu "cuộc chiến thống nhất" từng là "cuộc chiến xóa tên". Đây là nơi mở **cổng narrative** của chương.

### Situation

Một khe đá khuất gió, có rừng **bia không tên** (bia đã bị đục mất chữ). Vài bóng người ngồi quanh lửa lạnh. Người giữ ký ức là **Bà Lệ** (`NPC-CH04-BA-LE`) — hậu duệ/người canh trí nhớ của bộ tộc, mắt luôn ươn ướt, nước mắt rơi xuống hóa đá vụn ("lệ đá"). Phe đối lập là **Hồn Tướng Lưu Đày** (`NPC-CH04-HON-TUONG-LUU-DAY`) — một chiến hồn muốn dùng Đại Bàng để trả thù triều đại cũ.

### Key reveal

- Bộ tộc này từng bị triều đại "thống nhất" **gạch tên** khỏi sử: đất bị đổi tên, bia bị đục chữ, người bị đày lên Thạch Môn làm "lính canh quỷ" rồi bị bỏ quên.
- Đại Bàng Tinh không "bắt" họ; nó **hứng** phẫn nộ của họ và giữ hộ, vì không ai khác chịu nghe.
- `LG-04` từng là "neo ký ức" của bộ tộc — thứ giữ tên họ trong mạng lưới Long Khí. Mất nó, tên họ rơi hẳn vào quên lãng.

### Narrative gate choice: `C-CH04-002`

**Nghe trọn lời chứng (bond path)**

- Người chơi ngồi lại, đỡ bia, ghi nhớ bản đồ bộ tộc bằng trí nhớ (S03 beat), đồng ý **trả tên** trước khi lấy ngọc.
- Mở `Q-CH04-003` (bond), mở đường `released`, `tribal_trust +1`.
- Bà Lệ tiết lộ manh mối về màn ẩn `CH-04-HIDDEN` (Khe đá dựng) và tên Tù Trưởng.

**Săn Đại Bàng trước, lấy `LG-04` bằng lực (force path)**

- Người chơi từ chối chờ, leo thẳng lên ổ để đoạt ngọc — "cứ mạnh là lấy lại được tên".
- Không mở bond; `released` bị khóa trừ khi người chơi quay lại nghe sau (cho phép, nhưng khó hơn).
- Hồn Tướng Lưu Đày ủng hộ hướng này; Bà Lệ im lặng, lệ đá rơi nhiều hơn.

### Dialogue gate

Nếu đã giải thoát hồn ở S02, lời chứng của Bà Lệ **có tiếng đáp** của các hồn đã về; nếu giữ hồn làm mồi, khe đá vắng tiếng, lời chứng đơn độc và gay gắt hơn.

## CH-04-S04: Phán quyết trên vực

### Purpose

Pre-boss set piece + lựa chọn thái độ cuối trước trận. Đại Bàng Tinh lộ diện trên một mỏm đá nhô ra vực; gió và trọng lực gãy tạo thành "tòa án" tự nhiên.

### Staging

Đại Bàng Tinh chưa xòe hết cánh. Nó đậu trên mỏm vực, mắt là hai hốc sương, thân phủ lông có bóng người lấp ló. Khi nó "nói", nhiều giọng chồng lên nhau — giọng đàn ông, đàn bà, trẻ con, già trẻ — tất cả cùng một câu.

### Key reveal

- Nó hỏi Long Nhân: "Ngươi lên đây để **nghe**, hay để **cai trị**?" — nó nhận ra ấn rồng và mặc định Long Nhân là một kẻ cai trị mới.
- Nó **không** đòi mạng; nó đòi một **phán quyết**: ai có quyền quyết định ai được nhớ, ai bị quên.
- Nếu người chơi đã biết tội của triều đại (S03 bond), Đại Bàng ngừng tấn công một nhịp khi Long Nhân đến gần.

### Choice: `C-CH04-003`

**Gọi tên tội lỗi của triều đại:** "Họ bị gạch tên. Đó không phải thống nhất, đó là xóa người."

- Mở đường điều tra trong boss fight; `CH04_BOSS_NAMED_CRIME`.
- Đại Bàng giận nhưng **không phủ nhận**; phase 1 có thêm cửa sổ bond.

**Kết án Đại Bàng là quái vật:** "Ngươi giữ hồn người làm của riêng. Thả họ ra."

- `CH04_BOSS_CONDEMNED`; boss vào phase 1 ngay, ưu tiên đòn bổ nhào.
- Không khóa `released`, nhưng cần điều kiện arena khó hơn.

**Im lặng, giữ Thế Ngự, đỡ gió:**

- `CH04_BOSS_HEARD`; mở tutorial phản đòn bằng gió; nếu đỡ thành công ba đợt gió, mở một line ký ức về Tù Trưởng (gợi màn ẩn).

### Exit

Đại Bàng xòe cánh, che kín mặt trời; trọng lực quanh mỏm vực **gãy**. Long Nhân bị kéo vào arena trên không. Không còn đường lui đến khe bia cho tới khi encounter kết thúc.

## CH-04-B04: Đại Bàng Tinh

Encounter được mô tả chi tiết ở `05-boss-encounter.md`.

### Player objective

Không chỉ "giết con chim". Người chơi phải đọc được **phẫn nộ tập thể** bên trong nó, và quyết định: dập tắt bằng lực, hay trả lại tên để cơn giận có chỗ đặt xuống.

### Exit

Đại Bàng bị hạ/giải thoát/cưỡng đoạt. `LG-04` chuyển trạng thái. Các hồn trong lông vũ được về / bị kẹt / bị nuốt, tùy fate.

## CH-04-S05: Lệ đá rơi xuống mây

### Purpose

Hậu quả ngay + **xác nhận reveal huyết thống** + kéo sang CH-05. Đây là khoảnh khắc quiet payoff của chương.

### Fate resolution choice: `C-CH04-004`

**Trả tên, nhận ngọc có chủ ý** (chỉ khả dụng nếu bond hoàn tất):

- Người chơi khắc/gọi lại tên bộ tộc lên bia; nguyên thần Đại Bàng tự tách ra, **đồng thuận** trao `LG-04`.
- `boss_fates[B-04] = released`, `memory_recovered +1`, `mercy_marks +1`, `relics_purified +1`, `TRUTH_EXILE_WAS_ERASED` xác nhận.
- Lệ đá ngừng rơi; sương trên đỉnh hóa trong; các hồn tan thành ánh sáng bay xuống núi.

**Không chạm nguyên thần** (boss đã hạ nhưng không trả tên):

- `boss_fates[B-04] = defeated_by_force`; nguyên thần hòa vào `LG-04` nhưng không thanh tẩy; `memory_recovered` không tăng; một phần ký ức bộ tộc **mất tiếng** ở CH-06.

**Cưỡng đoạt phẫn nộ**:

- `boss_fates[B-04] = absorbed`, `dragon_hunger +1`; Long Khí bùng mạnh lần đầu nhưng nhiễu hình ảnh phẫn nộ; lệ đá rơi thành dòng đỏ.

### Reveal huyết thống (mọi nhánh, mức độ khác nhau)

- **Tiếng Vọng Lạc Long** hiện trên lưỡi rìu/mặt bia, nói về lý do tổ tiên rời đi: khi con người bắt đầu lấy **huyết thống** làm cớ để cai trị và xóa kẻ khác, Lạc Long Quân đã bỏ ngai, không ở lại làm "lý do" cho bất kỳ ai.
- Câu chốt (mọi nhánh): "Dòng máu nói lên ngươi **từ đâu tới**. Nó không nói ngươi **được phép làm gì** với người khác."
- Nhánh `released`: Long Nhân hiểu mình có thể là "người trả tên" thay vì "người cai trị". Nhánh `absorbed`: Tiếng Vọng im lặng lâu hơn, như thất vọng.

### Chapter close + hook CH-05

Camera kéo ra khỏi đỉnh Thạch Môn. Từ trên cao, người chơi thấy **ba dòng nước** gặp nhau ở một ngã ba xa tít dưới đồng bằng, và trên mặt nước lũ có **hai quầng sáng** đang hút về nhau như sắp cắn nhau. Tiếng Vọng: "Dưới đó, hai kẻ cùng tin mình đang tự vệ." Cut trước khi lộ rõ. (Hook CH-05: Ngã Ba Hạc / Song Giao.)

## CH-04-HIDDEN: Khe đá dựng (màn ẩn, tùy chọn)

### Purpose

Phần thưởng tri thức cho người tò mò; đào sâu `TRUTH_EXILE_WAS_ERASED` thành **sự thật khó chịu**: cái tên bị xóa **có chủ đích**, không phải do thời gian.

### Entry (cách mở)

- Chỉ hiện khi người chơi **nghe một hồn đọc sai tên bộ tộc** (S02, cần `Lôi Kích`) rồi **đối chiếu** với bia bị đục ở S03, và đỡ ba đợt gió ở S04 (`CH04_BOSS_HEARD`) — chuỗi clue mở một khe đá hẹp phía sau rừng bia.
- Không cần hoàn thành bond chính; màn ẩn độc lập với `released`/`force`.

### Beats

1. Một khe đá dựng đứng, hai vách cắm đầy **bia không tên** — hàng trăm tấm, tấm nào cũng bị đục đúng một dòng.
2. Cuối khe, một **tù trưởng hóa đá** quỳ, hai tay bưng mặt, nước mắt đông thành cột đá đỡ lấy cằm (`HB-04`).
3. Trên tay tù trưởng là một tấm bia **còn nguyên chữ** — tên thật của bộ tộc — nhưng chữ chỉ hiện khi có người **đọc to** nó.
4. Gặp gỡ phi chiến đấu: người chơi phải **gọi/khắc lại đúng tên** (ghép từ các clue S02/S03/S04) để giải thoát.

### Hidden boss: `HB-04` Tù Trưởng Lệ Đá

Chi tiết ở `05-boss-encounter.md` (mục Hidden).

### Exit / `C-CH04-00H`

- **Trả lại tên** (khắc tên bộ tộc lên bia trống): `boss_fates[HB-04] = released`, `hidden_released +1`, `mercy_marks +1`, `CH04_HIDDEN_RELEASED`, `TRUTH_EXILE_WAS_ERASED_HIDDEN`. Tù Trưởng tan thành sương; lệ đá trên cả đỉnh núi **ngừng rơi** một nhịp.
- **Cưỡng đoạt lệ đá** (hấp thụ "nước mắt ký ức" làm sức mạnh): `boss_fates[HB-04] = absorbed`, `dragon_hunger +1`, không tăng `hidden_released`. Tên bộ tộc vĩnh viễn không ai đọc lại.
- **Bỏ đi / khắc sai tên**: `boss_fates[HB-04] = defeated_by_force`; bia vẫn trống; màn ẩn đóng, không cộng `hidden_released`.
