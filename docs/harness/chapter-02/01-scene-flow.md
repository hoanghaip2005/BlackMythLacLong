# CH-02 Scene Flow

## Flow tổng

`S01 Làng không bóng`
`-> S02 Bài hát dưới sương`
`-> S03 Ba khuôn mặt của Hồ Tinh`
`-> S04 Đạo sĩ bị thao túng`
`-> S05 Tên thật trong gương nước`
`-> B02 Cửu Vĩ hiện hình`
`-> S06 Người sống gọi lại tên mình`
`-> [tùy chọn] HIDDEN Hang gương dưới đầm`

Màn ẩn `CH-02-HIDDEN` có thể mở ở bất kỳ điểm nào sau `CH-02-S03` (khi người chơi đã học cách đối chiếu thật/giả) và nên được phát hiện trước `B02` để người chơi mang `hidden_truth` vào trận; nếu phát hiện sau `B02`, nó vẫn tính cho `hidden_released` toàn cục nhưng bỏ lỡ một lớp thoại của Cửu Vĩ.

## CH-02-S01: Làng không bóng

### Purpose

Đặt Long Nhân vào một nơi hình hài không đáng tin: người làng không đổ bóng, hoặc bóng đi lệch hướng. Tạo câu hỏi "khuôn mặt này có phải người thật?".

### Entry

- Weapon state: Rìu Thần Thạch Sơn (đã thức tỉnh sau CH-01). `Phân Thân` chưa mở.
- Long Ngọc: `LG-01` nếu người chơi đã nhận ở CH-01; chưa có `LG-02`.
- Yêu khí xuất hiện như sương đọng thành mặt người rồi tan.

### Beats

1. Long Nhân theo tiếng hát nữ vọng từ sương (hook `CH-01-S08`); tiếng hát luôn đi trước một bước, không bao giờ tới gần.
2. Làng chài ven hồ: người vẫn sinh hoạt, nhưng nắng lên mà sân không có bóng người; bóng của họ tụ lại ở mép nước.
3. Một đứa trẻ gọi Long Nhân bằng một cái tên không phải của người chơi - rồi quên ngay tên đó.
4. Ma trơi lập lòe trên đầm; chúng dẫn đường nhưng cũng dẫn lệch.
5. Tutorial đọc "thật/giả": một NPC có hai cái bóng; chỉ một khớp với cử động.

### Exit

Người chơi hiểu luật đầu tiên của đầm: **một nguồn tin là chưa đủ**. Chưa biết Hồ Tinh là gì, chưa biết vì sao làng mất bóng.

### Choice

Không có choice chính. Cho phép khám phá: theo ma trơi (mở lore fragment về người mất tích) hoặc theo tiếng hát (mở đường tới `S02`). Cả hai đều tới `S02`; khác biệt là thông tin, không phải khóa content.

## CH-02-S02: Bài hát dưới sương

### Purpose

Biến tiếng hát thành một lựa chọn tin/không tin. Giới thiệu Người Hát - một cái bóng mất tên, không phải Hồ Tinh.

### Situation

Giữa đầm, một người phụ nữ đứng hát trên chiếc thuyền không đáy. Cô không có bóng. Giọng cô là giọng thật, nhưng khuôn mặt cô đổi mỗi lần sương tan. Cô hát tên những người đã mất - nhưng không hát được tên mình.

### Primary choice: `C-CH02-001`

**Ngồi lại nghe hết bài hát (điều tra)**

- Người chơi mất thời gian; ma trơi vây kín nhưng không hại.
- `tribal_trust +1` (Người Hát nhận ra Long Nhân không săn cô).
- Mở clue: "con cáo không ăn tên; nó giấu tên hộ người khác."
- Mở điều kiện cho `Q-CH02-003` (bond).

**Chộp lấy khuôn mặt đang hiện ra (truy đuổi hình mạnh nhất)**

- Người chơi tóm "khuôn mặt" - nó vỡ thành sương; đó là mặt nạ, không phải người.
- `dragon_hunger +1` chỉ khi sau đó người chơi chọn cưỡng đoạt nguyên thần; bản thân choice không tự kết tội.
- Người Hát im bặt; mất một lớp thoại bond; `tribal_trust` không tăng.
- Mở arena sớm hơn nhưng thiếu clue đối chiếu.

### Exit

Hai nhánh đều dẫn tới `S03`. Khác biệt: người chơi đã học "nghe" hay đã học "chộp", và Người Hát còn hát hay đã câm.

## CH-02-S03: Ba khuôn mặt của Hồ Tinh

### Purpose

Dạy cơ chế cốt lõi của chương: Hồ Tinh xuất hiện dưới ba khuôn mặt cùng lúc; chỉ một là thật, và cách nhận ra là **đối chiếu ba nguồn**, không phải đánh cái mạnh nhất. Mở `Phân Thân`.

### Three faces

1. **Khuôn mặt đứa trẻ bị mất:** khóc, gọi người chơi lại gần đầm.
2. **Khuôn mặt người làng tin cậy:** hứa chỉ chỗ con cáo nếu người chơi giúp.
3. **Khuôn mặt giống hệt Long Nhân:** đứng yên, không nói, cầm một thanh đoản kiếm rỉ sét (vật của CH-01).

### Investigation rules

- Đối chiếu đủ ba clue (bóng, phản chiếu gương nước, và một chi tiết chỉ người thật có): mở `CH02_FACES_CROSSCHECKED`, `memory_recovered` chưa tăng nhưng mở điều kiện bond và đặt `TRUTH_FOX_WAS_A_REFUGE` như clue chưa hoàn chỉnh.
- Tin một khuôn mặt duy nhất: người chơi vẫn có thể thắng boss, nhưng không đủ thông tin cho `released`.
- Đánh cả ba để "chọn nhanh": mở arena sớm, `dragon_hunger +1`, khóa một phần `C-CH02-003: released`.

### Phân Thân unlock

Khi người chơi nhận ra khuôn mặt giống mình chỉ là đất sét mượn hình, Tiếng Vọng Lạc Long hỏi: "Nếu mặt nạ là đất, con có dám nặn mặt mình không?" - mở `Phân Thân` (`SPELL_PHAN_THANH_AWAKENED`). Đây là ability tạo ảo ảnh từ đất sét, gắn với câu hỏi bản ngã.

### Exit

Người chơi thấy con cáo thật không nằm trong ba khuôn mặt; nó ở *dưới* mặt nước, nơi mọi phản chiếu đều thật.

## CH-02-S04: Đạo sĩ bị thao túng

### Purpose

Đưa ra một con người thật đang bị Hỗn Mang lợi dụng: một đạo sĩ trừ tà tin rằng Hồ Tinh ăn thịt người. Cho người chơi thấy "kẻ săn" cũng là nạn nhân, và lời đồn là vũ khí.

### Situation

Một đạo sĩ già bày trận bên đầm, dán bùa lên những cái bóng để "trừ hồ ly". Ông có thật, có bóng, nhưng mắt ông phản chiếu một khuôn mặt không phải của ông khi ông nói về con cáo. Dân đầm chia hai phe: theo đạo sĩ, hoặc im lặng vì sợ.

### Choice: `C-CH02-002`

**Tin đạo sĩ, giúp bày trận săn cáo**

- Người chơi dựng bẫy; Hồ Tinh bị dồn, vào trận sớm.
- `tribal_trust -1` với nhóm dân đầm từng được cáo che chở (họ thấy Long Nhân là kẻ săn mới).
- Mở `CH02_DAOSI_SIDED`.

**Đối chiếu và vạch trần khuôn mặt mượn trong mắt đạo sĩ**

- Người chơi chỉ ra ông đang bị đội lốt; trận bùa sụp; đạo sĩ suy sụp nhưng tỉnh lại.
- `tribal_trust +1`, `mercy_marks +1`, mở `CH02_DAOSI_EXPOSED`.
- Mở clue: kẻ ăn tên không phải cáo.

**Từ chối cả hai, đi tìm tên thật trước**

- Người chơi bỏ trận, đi về phía gương nước.
- Mở `CH02_DAOSI_REFUSED`; đạo sĩ tự bày trận và thất bại, hậu cảnh đầm xấu đi nhưng không khóa đường.

### Exit

Dù chọn gì, người chơi đều tới được `S05`; khác biệt là đạo sĩ còn tỉnh hay đã bị nuốt, và dân đầm tin hay sợ Long Nhân.

## CH-02-S05: Tên thật trong gương nước

### Purpose

Cho người chơi nghe phiên bản của Hồ Tinh trước trận và hiểu bond của `LG-02`: đầm từng là nơi trú ẩn, và Hồ Tinh giữ tên cho người chạy loạn.

### Staging

Hồ Tinh chưa lộ toàn thân. Mặt đầm phẳng như gương; phản chiếu của nó là một con cáo lớn, nhưng trên bờ chỉ có sương và những mặt nạ nổi. Nó nói qua mặt nước, mỗi câu đến từ một hướng khác nhau.

### Key reveal

- Chiến tranh từng đuổi người chạy loạn tới đầm; Hồ Tinh giấu họ, và vì họ sợ bị tìm ra, nó giữ tên thật của họ để "không ai gọi nhầm".
- Nỗi sợ tích tụ thành bóng; Hỗn Mang ăn những cái tên bị bỏ quên và đeo chúng làm mặt nạ.
- Đầm Xác Cáo không phải xác của cáo do nó giết - đó là tên của những người đã quên mình là ai.

### Choice: `C-CH02-003` (một phần, hoàn tất ở B02)

**Gọi đúng bản chất:** "Ngươi không ăn tên. Ngươi giữ chúng."

- Mở đường điều tra trong boss fight; Hồ Tinh ngừng một nhịp.
- Đặt `CH02_BOSS_NAMED_WOUND`.

**Gọi nó là quái vật:** "Ngươi đã nuốt cả làng."

- Boss vào phase 1 ngay; `CH02_BOSS_CONDEMNED`.
- Không khóa `released`, nhưng cần điều kiện khó hơn trong arena.

**Im lặng, giữ thế Ngự:**

- Mở khoảng parry tutorial; phản đòn thành công ba lần mở thêm line ký ức; `CH02_BOSS_HEARD`.

## CH-02-B02: Cửu Vĩ hiện hình

Encounter chi tiết ở `05-boss-encounter.md`.

### Player objective

Không chỉ "giết con cáo". Người chơi phải nhận ra trong chín cái đuôi, đuôi nào giữ tên thật, và quyết định có trả tên về hay đoạt lấy năng lực mượn mặt.

### Exit

Hồ Tinh được giải thoát, bị hạ hoặc bị cưỡng đoạt. `LG-02` chuyển trạng thái. `Phân Thân` đã mở trước đó; ở đây nó thành counterplay để phân biệt bóng thật của boss.

## CH-02-S06: Người sống gọi lại tên mình

### Purpose

Cho người chơi thấy hậu quả ngay của cách nhận nguyên thần, khép chương và kéo sang CH-03.

### Released variant

Những cái bóng dọc đầm đặc lại thành người; từng người gọi tên mình, lúng túng như học lại tiếng mẹ đẻ. Người Hát hát nốt phần tên của chính cô. Nếu `tribal_trust >= 3`, cô đề nghị đi cùng Long Nhân một đoạn (NPC đồng hành ngắn hạn, không phải companion combat cố định). Nếu thấp hơn, cô chỉ còn là tiếng hát khi người chơi quay lại.

### Force variant

Bóng vẫn loãng; vài người lấy lại tên, vài người không. Đạo sĩ (nếu còn sống) gom mặt nạ lại và nói: "Ngươi giết thứ giữ tên. Giờ ai giữ?" Tiếng Vọng Lạc Long: "Một khuôn mặt chưa tìm được người gọi tên."

### Absorbed variant

Long Nhân nuốt năng lực mượn mặt; da dưới cổ tay gợn lên như có mặt người đẩy ra. Dân đầm lùi lại, gọi Long Nhân là "cái bóng biết đi". Từ phía rừng xa, có tiếng binh khí va nhau và mùi rễ ướt - mồi dẫn vào CH-03, không phải Mộc Tinh xuất hiện trực tiếp.

### Chapter close

Camera rời mặt đầm, theo một dòng yêu khí mảnh như mực chảy về phía rừng Phong Châu, nơi một cổng thành bị rễ nuốt. Cắt trước khi cho thấy nguồn của nó.

## CH-02-HIDDEN: Hang gương dưới đầm (màn ẩn - ADR-004)

### Unlock

Mở khi `CH02_FACES_CROSSCHECKED = true` VÀ người chơi tìm ra một mặt nạ không khớp với bất kỳ khuôn mặt nào trong làng - mặt nạ của "người đầu tiên". Theo nó xuống một hang nước cạn dưới đầm, nơi vách là gương.

### Purpose

Gặp `HB-02` Bóng Vô Danh - người tị nạn đầu tiên Hồ Tinh che chở, bị Hỗn Mang ăn mất tên, nay thành cái bóng không mặt đi mượn tên người khác để cảm thấy mình có thật.

### Beats

1. Hang gương phản chiếu không phải hình người chơi, mà là ký ức đầm ngày còn là nơi trú ẩn.
2. Bóng Vô Danh đeo khuôn mặt của những người chơi đã gặp (Linh, Người Hát, đạo sĩ) - kể cả khuôn mặt Long Nhân.
3. Tên thật của nó bị khắc ngược trên một mặt nạ chìm; chỉ đọc được khi người chơi dùng gương nước đối chiếu (không phải bằng sức mạnh).
4. Encounter `HB-02`: bóng sao chép đòn thế và *mượn mặt người chơi*; nó không thể sao chép một lựa chọn người chơi chưa thực hiện.

### Resolution

- **Giải thoát (`released`):** gọi đúng tên thật của Bóng Vô Danh → nó đặc lại thành một người đã chết từ lâu, rồi tan yên. `hidden_released +1`, `mercy_marks +1`, mở `hidden_truth` (Hồ Tinh giữ tên; Hỗn Mang mới là kẻ ăn tên). Đặt `CH02_HIDDEN_RELEASED`.
- **Cưỡng đoạt (`absorbed`):** nuốt bóng → `dragon_hunger +1`, `Phân Thân` mạnh hơn nhưng nhiễu; KHÔNG tăng `hidden_released`. Đặt `CH02_HIDDEN_ABSORBED`.
- **Hạ bằng lực (`defeated_by_force`):** bóng tan nhưng tên vẫn mất; không tăng `hidden_released`. Đặt `CH02_HIDDEN_KILLED`.

### Exit

Người chơi trở lại đầm với một mảnh sự thật sâu hơn về Hỗn Mang; không có Long Ngọc thứ hai.
