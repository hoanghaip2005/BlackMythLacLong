# CH-01 Scene Flow

## Flow tổng

`S01 Trứng đá mở mắt`
`-> S02 Rạn san hô héo`
`-> S03 Người giữ đèn`
`-> S04 Đền chìm và ba ký hiệu`
`-> S05 Lời hứa bị bỏ lại`
`-> S06 Xoáy vực`
`-> B01 Ngư Tinh`
`-> S07 Nguyên thần và Rìu Thần Thạch Sơn`
`-> S08 Bờ nước chết`

## CH-01-S01: Trứng đá mở mắt

### Purpose

Đặt Long Nhân vào trạng thái không có bản sắc, giới thiệu di chuyển trong nước và tạo câu hỏi “ai đã đặt ta ở đây?”.

### Entry

- Không có weapon state.
- Không có Long Ngọc.
- Yêu khí chỉ xuất hiện như những sợi đen lẫn trong dòng nước.

### Beats

1. Âm thanh đầu tiên là tiếng đá nứt, không phải tiếng tim.
2. Một quầng sáng xanh từ vết nứt dẫn đường; khi người chơi quay lại, quầng sáng đã tắt.
3. Long Nhân chạm vào vỏ trứng; một tiếng vọng không rõ lời gọi “con của biển”.
4. Đoản kiếm rỉ sét mắc trong xương san hô bên cạnh bàn thờ vỡ.
5. Tutorial chiến đấu đầu tiên dùng sinh vật nhỏ, không dùng humanoid.

### Exit

Người chơi có đoản kiếm, biết đánh thường và né cơ bản. Chưa biết tên của bản thân, Lạc Long Quân hay Long Ngọc.

### Choice

Không có choice chính. Cho phép khám phá lựa chọn: lấy kiếm ngay hoặc quan sát vết khắc trên bàn thờ trước. Quan sát chỉ mở lore fragment, không đổi state.

## CH-01-S02: Rạn san hô héo

### Purpose

Cho người chơi thấy yêu khí đã làm biến dạng hệ sinh thái và gieo dấu vết đầu tiên của Ngư Tinh.

### Beats

1. San hô chuyển màu xám, nhưng một nhánh vẫn phát ra ánh sáng giống ánh mắt.
2. Cá nhỏ bơi theo đội hình rồi đồng loạt quay đầu khi Long Nhân đi qua.
3. Một xác thuyền bị cào ba đường dài; trên gỗ có ký hiệu hình sóng bị gạch ngang.
4. Một dòng nước mạnh kéo người chơi về hai hướng: đèn cứu nạn bên trái, tiếng va đập bên phải.

### Optional discovery: `Q-CH01-002`

Người chơi có thể tìm ba mảnh chuông đền trong rạn san hô. Đủ ba mảnh mở âm thanh cảnh báo trong arena, không thay đổi ending condition nhưng giúp đọc telegraph sớm hơn.

### Exit

Người chơi nhìn thấy một đèn đền đang chớp tắt. Một bóng người bị mắc trong lưới ở phía dưới.

## CH-01-S03: Người giữ đèn

### Purpose

Tạo lựa chọn đầu tiên giữa mục tiêu trước mắt và một sinh mạng cụ thể. Giới thiệu Linh, người đại diện cho Thủy tộc.

### Situation

Linh bị lưới rễ nước quấn quanh chân ở một hốc đá. Cô không yêu cầu được cứu bằng lời; cô dùng chuông đền gõ ba nhịp để báo vị trí. Một đàn thủy quái nhỏ tiến đến.

### Primary choice: `C-CH01-001`

**Cứu Linh**

- Người chơi phá ba nút lưới, chiến đấu trong không gian hẹp.
- `tribal_trust +1`.
- Mở `TRUTH_SEAL_WAS_NEVER_BROKEN` clue A: “lời hứa có ba hồi chuông”.
- Mở shortcut tới đền chìm.

**Đuổi theo dòng kéo**

- Người chơi bơi theo dấu vảy lửa và bỏ Linh lại.
- `dragon_hunger +1` chỉ khi người chơi sau đó chọn cưỡng đoạt nguyên thần; bản thân choice không tự kết tội người chơi.
- Linh sống sót nhờ tự cắt lưới, nhưng mất đèn dẫn đường.
- Arena thiếu một cảnh báo sớm; không khóa đường đi.

### Exit

Hai nhánh đều đến đền chìm. Khác biệt nằm ở mức tin tưởng, thoại và khả năng nhận diện pattern.

## CH-01-S04: Đền chìm và ba ký hiệu

### Purpose

Biến lore thành hành động điều tra. Người chơi ghép ba ký hiệu để hiểu `LG-01` là một lời hứa bị bỏ quên, chưa phải “mảnh phong ấn bị phá”.

### Three glyphs

1. **Sóng ôm đá:** Thủy tộc bảo vệ người đi biển.
2. **Móng vuốt đứt:** Ngư Tinh từng bị chém và bị bỏ lại.
3. **Vòng trống:** vị trí phong ấn không có dấu khóa; đây là clue phủ định, chưa phải xác nhận cuối game.

### Investigation rules

- Đọc đủ ba ký hiệu: `memory_recovered` chưa tăng; mở điều kiện bond và set `TRUTH_SEAL_WAS_NEVER_BROKEN` như một clue chưa hoàn chỉnh.
- Đọc một hoặc hai ký hiệu: người chơi vẫn có thể thắng boss, nhưng không đủ thông tin cho `released`.
- Dùng đoản kiếm phá bia: mở nhanh arena, gắn `dragon_hunger +1` và khóa `C-CH01-003`.

### Dialogue gate

Nếu Linh được cứu, cô đọc được nhịp chuông cổ. Nếu bị bỏ lại, tiếng đọc đến từ một xác đèn trôi; nội dung giống nhau nhưng cảm xúc khác.

## CH-01-S05: Lời hứa bị bỏ lại

### Purpose

Cho người chơi nghe phiên bản của Ngư Tinh trước trận đấu và làm rõ nó không chiến đấu chỉ vì đói.

### Staging

Ngư Tinh chưa lộ toàn thân. Đuôi lửa quấn quanh tháp đền, phần thân nằm ngoài vùng nhìn thấy. Nó nói qua nước, mỗi câu đến chậm hơn một nhịp như thể biển đang nhớ lại.

### Key reveal

- Lạc Long Quân từng hứa Thủy tộc sẽ không bị bỏ mặc.
- Ngư Tinh đã biến lời hứa thành lý do để giữ tất cả dưới đáy biển.
- Mảnh ngọc không làm nó sống lại; nó làm nỗi oán hận có hình dạng.

### Choice: `C-CH01-002`

**Gọi đúng tên nỗi đau:** “Ngươi bị bỏ lại.”

- Mở đường điều tra trong boss fight.
- Ngư Tinh tức giận nhưng không phủ nhận.

**Gọi nó là quái vật:** “Ngươi đã nhấn chìm họ.”

- Boss vào phase 1 ngay.
- Không khóa `released`, nhưng cần hoàn thành điều kiện khó hơn trong arena.

**Im lặng, giữ thế Ngự:**

- Mở một khoảng parry tutorial.
- Nếu phản đòn thành công ba lần trong encounter, mở thêm line ký ức.

## CH-01-S06: Xoáy vực

### Purpose

Chuyển từ điều tra sang sinh tồn. Đây là pre-boss set piece, không phải boss phase kéo dài.

### Beats

1. Nước quanh đền rút khỏi mặt đá như bị hút ngược xuống lòng vực.
2. Ba cột đèn lần lượt tắt; nếu Linh được cứu, cô thắp lại một cột.
3. Xoáy nước mở, kéo cả mảnh bia và xác thuyền vào tâm.
4. Người chơi lần đầu cần dùng `Thủy Ảnh` để tránh một đợt hút bắt buộc.
5. Đuôi lửa của Ngư Tinh đập xuống, mở arena.

### Exit

Long Nhân đứng trên nền đền nửa chìm. Ngư Tinh trồi lên. Không còn đường quay lại vùng khám phá cho tới khi encounter kết thúc.

## CH-01-B01: Ngư Tinh

Encounter được mô tả chi tiết ở `05-boss-encounter.md`.

### Player objective

Không chỉ “giết boss”. Người chơi phải nhận ra ba neo lời hứa quanh arena và quyết định có phá vòng lặp hay không.

### Exit

Ngư Tinh bị đánh bại, được giải thoát hoặc bị cưỡng đoạt. `LG-01` chuyển trạng thái. Rìu Thần Thạch Sơn thức tỉnh trong mọi nhánh, nhưng ánh sáng và âm thanh khác nhau.

## CH-01-S07: Nguyên thần và Rìu Thần Thạch Sơn

### Purpose

Biến phần thưởng combat thành quyết định về quyền lực.

### Sequence

1. Nguyên thần tách khỏi thân Ngư Tinh như một con cá sáng không có vảy.
2. Rìu Thần Thạch Sơn trồi khỏi nền đá; nó không bay vào tay người chơi, người chơi phải bước tới.
3. Tiếng Vọng Lạc Long hỏi: “Con muốn nhớ điều gì, hay chỉ muốn mạnh hơn?”
4. Người chơi chọn cách tiếp nhận nguyên thần.

### Choice: `C-CH01-003`

- **Tiếp nhận có chủ ý:** chỉ khả dụng nếu đủ điều kiện bond; `boss_fates[B-01] = released`, `memory_recovered +1`, `mercy_marks +1`, `relics_purified +1`, thêm truth flag.
- **Cưỡng đoạt:** luôn khả dụng sau khi boss bị hạ; `boss_fates[B-01] = absorbed`, `dragon_hunger +1`.
- **Không chạm vào nguyên thần:** `boss_fates[B-01] = defeated_by_force`; nguyên thần hòa vào `LG-01` nhưng không thanh tẩy; mở hậu cảnh lạnh hơn.

## CH-01-S08: Bờ nước chết

### Purpose

Cho người chơi nhìn thấy hậu quả ngay, khép chapter và kéo sang CH-02.

### Released variant

Linh cùng vài người Thủy tộc đưa Long Nhân tới bờ. Họ không quỳ lạy. Linh đặt một vỏ ốc vào tay Long Nhân và nói: “Đừng mang lời hứa của chúng ta như vương miện.”

### Force variant

Đền chìm vẫn mở nhưng Thủy tộc đứng xa. Một cậu bé nhặt mảnh vảy cháy rồi ném xuống nước. Tiếng Vọng Lạc Long chỉ nói: “Sức mạnh đã trở lại. Ký ức thì chưa.”

### Absorbed variant

Nước rút nhanh. Những vệt đen chạy ngược lên cánh tay Long Nhân rồi biến mất dưới da. Từ xa, một giọng hát nữ vọng qua sương đất liền; đây là mồi dẫn vào CH-02, không phải Hồ Tinh xuất hiện trực tiếp.

### Chapter close

Camera rời khỏi mặt biển, lộ một đường yêu khí mảnh như mực nối về đất liền. Cắt trước khi cho thấy nguồn của nó.
