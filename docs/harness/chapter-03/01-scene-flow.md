# CH-03 Scene Flow

## Flow tổng

`S01 Cổng Phong Châu bị nuốt`
`-> S02 Lính gác không mặt`
`-> S03 Nghĩa địa dưới rễ`
`-> S04 Lời thề của người chết`
`-> S05 Lõi đỏ thức dậy`
`-> B03 Mộc Tinh`
`-> S06 Tiếng binh khí im`

Màn ẩn (tùy chọn, ADR-004): `CH-03-HIDDEN Gò mộ dưới rễ` -> `HB-03 Tướng Quân Vô Đầu`. Có thể vào sau khi đọc đủ manh mối ở `S03`/`S04`, trước hoặc sau `B03` nhưng trước khi rời Phong Châu.

## CH-03-S01: Cổng Phong Châu bị nuốt

### Purpose

Đặt Long Nhân vào một kinh đô cũ đã bị rừng nuốt; giới thiệu câu hỏi "ai đang đứng gác nơi không còn ai sống?" và gieo dấu vết Mộc Tinh.

### Entry

- Mang Rìu Thần Thạch Sơn, `LG-01`, `LG-02`.
- Yêu khí xuất hiện như sợi đỏ lẫn trong rễ và sương thấp.
- Hook vào từ CH-02: một NPC/tiếng hát/đường yêu khí dẫn về phía rừng (tùy hậu quả CH-02).

### Beats

1. Cổng đá Phong Châu bị rễ siết nứt; biển chữ cũ bị rêu che nửa, chỉ đọc được "...châu".
2. Trên mặt đá có vết cào của nhiều thế hệ lính gác đứng tựa - dấu người, nhưng đã rất lâu không có người sống.
3. Một hàng giáp rỗng mọc rêu đứng dọc lối vào; chúng không tấn công, chỉ "đứng gác".
4. Tiếng binh khí vọng từ sâu trong rừng, đều nhịp như một buổi tập trận không bao giờ kết thúc.
5. Tutorial nhỏ: dùng `Thế Trảm` phát quang cụm rễ chặn đường; rễ rỉ nhựa đỏ như máu loãng.

### Exit

Người chơi hiểu: đây là một doanh trại của người chết, không phải một khu rừng hoang. Chưa biết vì sao họ ở lại.

### Choice

Không có choice chính. Cho phép khám phá: đọc biển cổng (mở lore fragment về kinh đô cũ) hoặc đi thẳng. Đọc chỉ mở lore, không đổi state.

## CH-03-S02: Lính gác không mặt

### Purpose

Cho người chơi thấy yêu khí đã "quân hóa" người chết; giới thiệu hai phe vong linh qua một tình huống cụ thể, không qua lời giảng.

### Situation

Một toán lính gác không mặt chặn lối. Chúng không hung hăng vô cớ; chúng "tuần tra" theo lệnh cũ. Giữa chúng, một vong linh còn giữ được chút ý chí - **Hiến** - lên tiếng; một vong linh khác - **Trưởng** - khăng khăng giữ hàng ngũ.

### Primary choice: `C-CH03-001`

**Giải thoát toán gác (chặt rễ điều khiển)**

- Người chơi dùng `Thế Trảm`/`Thế Đột` phá các nút rễ cắm vào gáy từng xác, giải phóng chúng.
- `mercy_marks +1` (nếu giải thoát thay vì tiêu diệt), mở manh mối `TRUTH_OLD_ARMY_WAS_BOUND` clue A: "rễ cắm vào gáy, không phải vào tim".
- Hiến và một phần vong linh tỉnh ra, biết ơn nhưng buồn; Trưởng phản đối: "Ngươi cắt dây của họ, hay cắt lý do họ ở lại?"
- Mở đường tắt tới nghĩa địa.

**Giữ họ chiến đấu (lợi dụng hàng ngũ để mở cổng nhanh)**

- Người chơi kích động toán gác đánh lẫn nhau/đánh Mộc Tinh con để cổng rễ mở ra, không giải thoát ai.
- `dragon_hunger +1` chỉ khi người chơi sau đó chọn cưỡng đoạt nguyên thần; bản thân choice không tự kết tội.
- Mở cổng nhanh hơn, nhưng Hiến giữ khoảng cách; một số vong linh sau này từ chối giúp ở `S04`.
- Không khóa đường đi; cost là thông tin và trust.

### Exit

Hai nhánh đều tới được nghĩa địa dưới rễ. Khác biệt nằm ở mức vong linh còn tin Long Nhân, thoại, và số lượng manh mối lời thề đọc được.

## CH-03-S03: Nghĩa địa dưới rễ

### Purpose

Biến lore thành hành động điều tra. Người chơi ghép ba "lời thề" để hiểu `LG-03` là một đội quân bị trói (một phần tự nguyện), chưa phải "mảnh phong ấn bị phá".

### Three oaths (ba bia lời thề)

1. **Bia "Giữ đất":** thề bảo vệ kinh đô tới người cuối cùng - lời thề chính nghĩa.
2. **Bia "Không tên":** những chiến binh bị lịch sử xóa tên, bám lời thề vì đó là thứ duy nhất chứng minh họ từng tồn tại.
3. **Bia "Tự ở lại":** dấu hiệu một số vong linh KHÔNG bị rễ trói mà tự nguyện đứng vào hàng - clue then chốt cho `TRUTH_OLD_ARMY_WAS_BOUND` và cho màn ẩn `HB-03`.

### Investigation rules

- Đọc đủ ba bia: mở điều kiện bond, set `TRUTH_OLD_ARMY_WAS_BOUND` như clue chưa hoàn chỉnh; mở manh mối dẫn tới `CH-03-HIDDEN`.
- Đọc một hoặc hai bia: vẫn có thể thắng boss, nhưng không đủ thông tin cho `released`.
- Dùng rìu chẻ bia để mở đường nhanh: `dragon_hunger +1`, khóa `C-CH03-003` nhánh release, mất manh mối màn ẩn.

### Optional discovery: `Q-CH03-002`

Ba mảnh quân kỳ cũ rải trong nghĩa địa; đủ ba mảnh khôi phục một hồi trống lệnh, giúp đọc telegraph "rễ siết" sớm hơn trong arena. Không đổi ending condition.

### Exit

Người chơi nhận ra: đội quân này không chỉ bị trói - một phần đã chọn ở lại. Một gò mộ lớn nằm lệch khỏi hàng, rễ không chạm tới, là manh mối màn ẩn.

## CH-03-S04: Lời thề của người chết

### Purpose

Cho người chơi nghe phiên bản của Mộc Tinh và của vong linh trước trận đấu; làm rõ Mộc Tinh không chiến đấu chỉ vì đói, và lời thề không chỉ là xiềng.

### Staging

Mộc Tinh chưa lộ toàn thân. Rễ của nó quấn quanh một lõi đỏ đập chậm như tim, phía sau hàng xác đứng im. Nó nói qua tiếng lá và tiếng binh khí vọng, mỗi câu đến chậm như rừng đang nhớ lại.

### Key reveal

- Lạc Việt từng có một đội quân thề giữ kinh đô; khi kinh đô thất thủ, họ chết nhưng lời thề chưa được "thu hồi".
- Mộc Tinh bén rễ từ máu và lời thề ấy; nó giữ người chết lại vì nó tin (hoặc được khiến tin) rằng buông ra là phản bội.
- Mảnh ngọc không làm nó sống; nó làm nỗi sợ bị quên có hình dạng.

### Choice: `C-CH03-002`

**Gọi đúng tên nỗi đau:** "Họ ở lại vì sợ bị quên, không phải vì ngươi giữ."

- Mở đường điều tra trong boss fight; Mộc Tinh tức giận nhưng không phủ nhận.
- Set `CH03_BOSS_NAMED_WOUND`.

**Gọi nó là quái vật:** "Ngươi ăn máu người chết để lớn."

- Boss vào phase 1 ngay; set `CH03_BOSS_CONDEMNED`.
- Không khóa `released`, nhưng cần hoàn thành điều kiện khó hơn trong arena.

**Im lặng, giữ thế Ngự:**

- Mở một khoảng parry tutorial với rễ quất; set `CH03_BOSS_HEARD`.
- Nếu phản đòn thành công ba lần trong encounter, mở thêm line ký ức về Tướng Quân (gợi màn ẩn).

## CH-03-S05: Lõi đỏ thức dậy

### Purpose

Chuyển từ điều tra sang sinh tồn. Đây là pre-boss set piece, không phải boss phase kéo dài.

### Beats

1. Rễ quanh nghĩa địa đồng loạt co lại, kéo các bia đá sụp xuống như bị rừng nuốt lần nữa.
2. Hàng xác đứng im bỗng quay mặt (nơi từng là mặt) về phía Long Nhân; tiếng binh khí dồn nhịp.
3. Lõi đỏ của Mộc Tinh trồi lên giữa rừng, đập mạnh; sương đỏ lan thấp quanh gốc.
4. Người chơi lần đầu cần dùng `Thế Trảm` để dọn một cụm xác-rễ chặn đường rút (hook diện rộng).
5. Một rễ cái đập xuống, mở arena quanh lõi đỏ.

### Exit

Long Nhân đứng trên nền nghĩa địa nửa sụp. Mộc Tinh trồi lên. Không còn đường quay lại vùng khám phá cho tới khi encounter kết thúc (trừ lối tắt màn ẩn nếu đã mở).

## CH-03-B03: Mộc Tinh

Encounter được mô tả chi tiết ở `05-boss-encounter.md`.

### Player objective

Không chỉ "chặt đổ cây". Người chơi phải nhận ra các nút rễ trói vong linh quanh arena và quyết định: phá rễ để giải thoát (chậm, risk) hay để nguyên và đánh thẳng vào lõi (nhanh, nhưng bỏ rơi người chết).

### Exit

Mộc Tinh bị hạ, được giải thoát hoặc bị cưỡng đoạt. `LG-03` chuyển trạng thái. Rừng im tiếng binh khí hoặc tiếp tục vọng, tùy fate.

## CH-03-S06: Tiếng binh khí im

### Purpose

Cho người chơi nhìn thấy hậu quả ngay, khép chapter và kéo sang CH-04.

### Released variant

Hiến và phần vong linh được giải thoát cúi đầu rồi tan vào sương; một vài người TỰ NGUYỆN ở lại canh ký ức (không bị trói). Trưởng, nếu được thuyết phục, đặt thanh kiếm rêu xuống. Tiếng binh khí im hẳn. Hiến nói: "Cảm ơn. Nhưng đừng gọi đó là chiến thắng - chúng ta vừa quên thêm một lần nữa những người không được gọi tên."

### Force variant

Mộc Tinh đổ nhưng rễ vẫn cắm vào xác; đội quân đứng im, không còn bị điều khiển nhưng chưa được gọi tên. Trưởng vẫn gác. Tiếng binh khí thưa dần rồi tắt, lạnh. Tiếng Vọng Lạc Long: "Sức mạnh đã dọn rừng. Ký ức thì chưa."

### Absorbed variant

Rễ đen chạy ngược lên tay Long Nhân rồi biến mất dưới da. Lõi đỏ tắt. Từ xa, một tiếng trống lệnh vang lên rồi im bặt - mồi dẫn vào CH-04 (núi Thạch Môn), không phải Đại Bàng Tinh xuất hiện trực tiếp.

### Sacrificed variant

Nếu `CH03_END_SACRIFICED`: vong linh tự hy sinh (hoặc Tướng Quân Vô Đầu, nếu màn ẩn đã mở) phá vòng lặp; các vong linh khác lần lượt buông vũ khí, không ai bị chặt. Cảnh lặng, nặng ân nghĩa. Đây là biến thể của `released` với cờ riêng.

### Chapter close

Camera rời khỏi tán rừng, lộ một dãy núi đá có những bóng lông vũ khổng lồ lượn trên sương - hướng CH-04. Cắt trước khi cho thấy Đại Bàng Tinh.

## CH-03-HIDDEN: Gò mộ dưới rễ (Oan Khuất Ẩn, ADR-004)

### Unlock

Mở khi đọc bia "Tự ở lại" ở `S03` (và khuyến khích đã nghe line ký ức về Tướng Quân ở `S04`). Một gò mộ lớn nằm lệch hàng, rễ KHÔNG chạm tới - dấu hiệu một người tự đứng ra ngoài lời thề chung nhưng vẫn ở lại.

### Purpose

Đào sâu `TRUTH_OLD_ARMY_WAS_BOUND`: hóa ra kẻ chỉ huy không bị Mộc Tinh trói - ông TỰ trói mình, vì sợ rằng nếu ông buông lời thề, lịch sử sẽ quên luôn cả đội quân. Ông là "nút rễ trung tâm" tự nguyện.

### Encounter: `HB-03` Tướng Quân Vô Đầu

Một thân giáp cổ không đầu, đứng giữa gò mộ, tay giữ một lời thề khắc trên lưỡi kiếm cùn. Rễ từ ông tỏa ra nối với cả nghĩa địa - nhưng là rễ ông tự mọc, không phải rễ Mộc Tinh cắm vào. Chi tiết đầy đủ ở `05-boss-encounter.md` (mục Hidden) và `03-quests-and-choices.md` (`Q-CH03-00H`).

### Choice: `C-CH03-00H`

- **Trả lại "cái đầu" (danh tính):** ghép đủ tên của đội quân (từ ba bia + quân kỳ) và đọc lên; Tướng Quân buông kiếm, lời thề được "thu hồi" đúng nghĩa. `boss_fates[HB-03] = released`, `hidden_released +1`, `mercy_marks +1`, mở `hidden_truth` (một phần vong binh tự nguyện ở lại).
- **Chém nút rễ trung tâm:** hạ Tướng Quân bằng lực để cả nghĩa địa sụp rễ nhanh. `boss_fates[HB-03] = defeated_by_force` hoặc `absorbed`, `dragon_hunger +1`, KHÔNG tăng `hidden_released`.
- **Để ông tự quyết (nếu đã nghe đủ):** ở nhánh sâu, Tướng Quân có thể TỰ hy sinh (`sacrificed`) để phá vòng lặp, mở `CH03_END_SACRIFICED`.

### Exit

Màn ẩn không đổi ending của chương, nhưng cộng `hidden_released` (điều kiện `E-04`) và mở một lớp thoại/ký ức sâu hơn ở `S06`.
