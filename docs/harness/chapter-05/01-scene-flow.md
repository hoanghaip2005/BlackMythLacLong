# CH-05 Scene Flow

## Flow tổng

`S01 Làng nổi`
`-> S02 Hai tiếng gọi dưới lũ`
`-> S03 Bè chiến giữa song giao`
`-> S04 Mảnh ngọc lộ diện`
`-> B05A Song Giao`
`-> B05B Hắc Giao Long`
`-> S05 Nước rút để lộ bậc tế đàn`
`(optional) -> HIDDEN Miếu chìm ở ngã ba nước`

Màn ẩn `CH-05-HIDDEN` có thể mở ở bất kỳ điểm nào sau `S02` và nên được giải quyết trước `B05B` để người chơi bước vào hợp thể với hiểu biết về Giao Mẫu; nếu bỏ lỡ, nó vẫn mở được sau chương nhưng mất cửa sổ "nhớ lại mẹ" ngay trong trận.

## CH-05-S01: Làng nổi

### Purpose

Đặt Long Nhân vào một cộng đồng sống *giữa* hai thế lực, cho thấy xung đột không phải chuyện của quái vật mà là chuyện của người đang kẹt ở giữa.

### Entry

- Long Nhân đã có Rìu Thần Thạch Sơn và các ability từ CH-01..04.
- Đã có bốn mảnh Long Ngọc (`LG-01..LG-04`); chưa có `LG-05`.
- Yêu khí xuất hiện như phù sa đen cuộn trong dòng lũ, không phải sinh vật đơn lẻ.

### Beats

1. Bè mảng và nhà nổi chao theo con nước; dây neo căng như sắp đứt.
2. Người làng không nhìn Long Nhân bằng sợ hãi thuần; họ nhìn như nhìn "một bên thứ ba" có thể làm lệch cán cân.
3. Một cột nước dựng đứng ở nhánh sông bên trái, một cột khác ở nhánh bên phải — hai tiếng gọi khác nhau.
4. `Ông Chài` nói rằng ngày xưa ngã ba này có *một* người mẹ chia nước cho hai con; giờ không ai nhớ bà nữa.

### Exit

Người chơi hiểu: có hai thế lực giao đang tranh một thứ, và làng nổi là kẻ chịu trận. Mở `Q-CH05-001`.

### Choice

Không có choice chính. Cho phép khám phá: nghe lời kể của dân làng bên nhánh trái trước hay nhánh phải trước — chỉ mở lore và đổi thứ tự tiếp cận ở `S02`, không đổi state đạo đức.

## CH-05-S02: Hai tiếng gọi dưới lũ

### Purpose

Cho người chơi nghe *cả hai* giao tự xưng là người giữ ngọc chính đáng, gieo nghi ngờ "ai đúng?" rồi lật thành "cả hai đều bị lừa".

### Beats

1. Giao Anh (nhánh thượng) gọi: ngọc là của nó vì nó giữ nguồn.
2. Giao Em (nhánh hạ) gọi: ngọc là của nó vì nó giữ cửa ra biển.
3. Cả hai đều kể *cùng một ký ức* nhưng với chi tiết lệch nhau — dấu hiệu ký ức đã bị chỉnh sửa.
4. Một vệt phù sa đen không thuộc về giao nào bò ngược dòng, lắng nghe cả hai — dấu vết chủ động đầu tiên của "nguồn nuôi xung đột".

### Choice: `C-CH05-001` (Nghe bên nào trước)

- **Nghe Giao Anh trước:** mở góc nhìn "giữ nguồn"; `tribal_trust` với nhánh thượng nếu người chơi bênh họ.
- **Nghe Giao Em trước:** mở góc nhìn "giữ cửa"; `tribal_trust` với nhánh hạ nếu người chơi bênh họ.
- **Nghe cả hai, không bênh bên nào:** mở clue đối chiếu ký ức lệch (`CH05_MEMORY_MISMATCH`), cần cho `released`; không tăng `tribal_trust` bên nào nhưng tăng hiểu biết.

### Exit

Người chơi nhận ra hai ký ức mâu thuẫn nhưng cả hai đều *tin thật*. Mở điều kiện điều tra bond và `Q-CH05-002`.

## CH-05-S03: Bè chiến giữa song giao

### Purpose

Biến "chọn phe hay tìm gốc" thành hành động giữa trận: chiến đấu trên bè trôi, *giữa* hai boss, nơi người chơi có thể lợi dụng va chạm hoặc đi tìm nguồn nước.

### Beats

1. Hai giao quần nhau; sóng và bè mảng trở thành địa hình động.
2. Người chơi phải di chuyển giữa hai luồng tấn công, dùng `Thủy Ảnh` để né hoàn hảo trong nước.
3. Có hai hướng giải quyết rõ ràng, tạo `C-CH05-002`.
4. Nếu đã mở màn ẩn, người chơi thấy dòng phù sa đen luôn chảy về một điểm cố định dưới ngã ba — gợi ý "nguồn".

### Choice: `C-CH05-002` (Narrative gate)

- **Kích hai giao đánh nhau:** để chúng tự làm yếu nhau, tạo lợi thế combat. Nhanh, ít rủi ro, nhưng củng cố vòng tranh giành; `dragon_hunger +1` nếu người chơi cố tình đẩy chúng vào chỗ chết; không mở clue về nguồn.
- **Phá nguồn nước nuôi xung đột:** lội theo dòng phù sa đen tới điểm neo ký ức (liên quan `Q-CH05-003`/màn ẩn). Chậm hơn, khó hơn, mở `TRUTH_CONFLICT_WAS_FED` như clue và cho phép `released` dễ hơn.

### Exit

Cả hai nhánh đều dẫn tới `S04`; khác nhau ở thông tin, `tribal_trust`, và liệu người chơi đã chạm tới "nạn nhân thứ ba" hay chưa.

## CH-05-S04: Mảnh ngọc lộ diện

### Purpose

Cho `LG-05` hiện ra không phải như phần thưởng mà như *bằng chứng* bị giành giật; xác nhận mảnh thứ năm và chuẩn bị hợp thể.

### Beats

1. Nước xoáy ở tâm ngã ba; `LG-05` nổi lên giữa hai luồng, không thuộc nhánh nào.
2. Cả hai giao lao vào cùng lúc — khoảnh khắc chúng chạm ngọc, yêu khí ép chúng xoắn vào nhau.
3. Tiếng Vọng Lạc Long: "Ngọc không nhớ ai giữ nó. Nó nhớ ai đã chia nó ra."
4. Người chơi bị hút vào arena khi hai thân giao bắt đầu hợp thể.

### Exit

Mở `B05A`. Người chơi hiểu trận này không phải "giết con nào" mà là "ngăn một vụ cưỡng ép".

## CH-05-B05A: Song Giao (giai đoạn boss A)

Encounter chi tiết ở `05-boss-encounter.md`.

### Player objective

Sống sót giữa hai boss, đọc rằng chúng *đang tự vệ chứ không săn mồi*, và kích hoạt các neo ký ức (hoặc lợi dụng va chạm) để làm lộ điểm yếu của lời nói dối.

### Exit

Sau khi đủ điều kiện, yêu khí cưỡng ép hai giao hợp thể. Chuyển `B05B`. Không có "thắng" ở giai đoạn A; chỉ có "sống sót và hiểu".

## CH-05-B05B: Hắc Giao Long (giai đoạn boss B)

### Player objective

Đối đầu hợp thể đang đau đớn. Người chơi quyết định số phận: giải thoát (nếu đã hiểu bond + Giao Mẫu), đánh bại bằng sức mạnh, hoặc cưỡng đoạt.

### Exit

`boss_fates[B-05]` được ghi. `LG-05` chuyển trạng thái. Mở `S05`.

## CH-05-S05: Nước rút để lộ bậc tế đàn

### Purpose

Khép chương, cho thấy hậu quả ngay của cách giải quyết, và mở đường lên Nghĩa Lĩnh (CH-06).

### Released variant

Hai giao tách ra, bơi song song một nhịp như anh em; nước rút trong. Bậc đá tế đàn hiện ra trong bùn, còn ướt. `Ông Chài` đặt tay lên bè: "Ngã ba này từng có một người mẹ. Cảm ơn người đã nhớ giùm."

### Force variant

Hợp thể tan thành hai dòng đục; hai giao biến mất không nhìn nhau. Bậc tế đàn lộ ra nhưng phủ phù sa đen. Làng nổi không gọi Long Nhân là người hòa giải; họ gọi là "kẻ đã làm lặng nước".

### Absorbed variant

Long Nhân hút nguyên thần hợp thể; vệt đen chạy ngược lên cánh tay. Nước rút nhanh bất thường, để lại bậc tế đàn khô nứt. Từ xa, cả hai tiếng gọi im bặt — không phải vì được giải thoát, mà vì bị nuốt.

### Chapter close

Máy quay nâng lên theo bậc tế đàn dẫn vào mây, về phía Đỉnh Nghĩa Lĩnh. Cắt trước khi cho thấy đỉnh núi. Hook CH-06: "Đủ năm mảnh. Giờ ai là người quyết định chúng dùng để làm gì?"

## CH-05-HIDDEN: Miếu chìm ở ngã ba nước (optional, ADR-004)

### Purpose

Mở "nạn nhân thứ ba" — Giao Mẫu — và biến `TRUTH_CONFLICT_WAS_FED` từ clue thành sự thật sống: xung đột này có một người mẹ bị cả hai bên quên.

### Entry

Mở khi người chơi đi theo dòng phù sa đen tới điểm neo cố định dưới ngã ba (gợi ý từ `S03` nếu chọn "phá nguồn", hoặc từ lời `Ông Chài` ở `S01`). Không bắt buộc; missable nếu người chơi chỉ muốn thắng nhanh.

### Beats

1. Một miếu nhỏ chìm ở đáy, mái còn vướng lưới đánh cá cũ — không phải của dân làng hiện tại.
2. Trên bệ thờ: ba bát nước, hai còn, một đã cạn — dấu vết "một người mẹ chia nước cho hai con".
3. Giao Mẫu hiện ra không phải để chiến đấu ngay; bà tưởng Long Nhân là một trong hai con trở về.

### Choice: `C-CH05-00H`

- **Nói thật bà đã bị quên:** mở bond, dẫn tới giải thoát; `HB-05` có thể `released`.
- **Lợi dụng bà để khống chế hai giao:** biến bà thành công cụ; dẫn tới `absorbed`/`defeated_by_force` cho `HB-05`, `dragon_hunger +1`.

### Exit

Nếu `released`: bà trao "ký ức người mẹ" để mang lên trận hợp thể — hai giao *nhớ lại mẹ*, mở cửa `released` thật sự cho `B-05` và cộng `hidden_released`. Nếu không: màn ẩn khép, `hidden_released` không tăng; người chơi vẫn đánh `B-05` nhưng thiếu chìa khóa hòa giải.
