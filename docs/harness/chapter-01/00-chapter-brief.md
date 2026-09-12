# CH-01: Trầm Thủy Ngư Tinh

## Trạng thái

- ID: `CH-01`
- Version: `0.2`
- Status: `draft`
- Vùng: Vực Biển Đông, đền chìm và bờ đá thủy triều.
- Thời lượng narrative mục tiêu: 90-120 phút cho first playthrough, chưa tính khám phá tùy chọn.
- Mảnh Long Ngọc: `LG-01`
- Boss: `B-01`, Ngư Tinh
- Truth flag: `TRUTH_SEAL_WAS_NEVER_BROKEN`

## Chapter promise

Người chơi bắt đầu như một sinh vật không tên, không ký ức, chỉ biết đánh và sống sót. Cuối chương, người chơi hiểu ba điều:

1. Long Nhân có huyết mạch rồng nhưng không phải Lạc Long Quân.
2. Ngư Tinh không phải nguồn gốc duy nhất của tai họa; nó đang giữ một món nợ bị bỏ quên.
3. Thu hồi sức mạnh luôn là một lựa chọn đạo đức, không chỉ là phần thưởng.

## Dramatic question

**Khi sức mạnh đầu tiên nằm trong tay một kẻ thù bị bỏ rơi, Long Nhân sẽ chiếm đoạt nó hay chấp nhận gánh món nợ đi kèm?**

## Emotional arc

| Chặng | Trạng thái Long Nhân | Cảm xúc người chơi | Hình ảnh chủ đạo |
|---|---|---|---|
| Mở đầu | Không tên, phản xạ | Lạnh, bất an | Vỏ trứng đá dưới áp lực nước |
| Khám phá | Bắt đầu được người khác nhìn nhận | Tò mò, nghi ngờ | San hô chết và đèn đền tắt |
| Điều tra | Chạm vào một lời hứa cũ | Thương cảm, hoài nghi | Bia đá bị nước xóa chữ |
| Đối đầu | Bị Ngư Tinh gọi là “dòng máu bỏ đi” | Giận dữ, phân vân | Đuôi lửa chia đôi mặt biển |
| Hậu quả | Tự chọn cách nhận sức mạnh | Trách nhiệm, dự cảm | Long Ngọc sáng hoặc nước hóa đen |

## Chapter non-goals

- Chưa giải thích Hỗn Mang đầy đủ; chỉ gieo dấu hiệu.
- Chưa mở toàn bộ ba stance như hệ thống hoàn chỉnh; CH-01 chỉ giới thiệu sự khác biệt qua tình huống và tutorial.
- Chưa cho người chơi gặp Hồ Tinh, Mộc Tinh, Đại Bàng Tinh hoặc Song Giao.
- Chưa xác nhận phong ấn bị phá; mọi lời nói về “phong ấn” ở đây là lời truyền hoặc diễn giải sai.

## Canon lock riêng cho CH-01

1. Long Nhân thức tỉnh từ trứng đá dưới đáy biển, tay không, cạnh một thanh đoản kiếm rỉ sét.
2. Đoản kiếm là vật sinh tồn tạm thời, không phải vũ khí định mệnh.
3. Rìu Thần Thạch Sơn chỉ thức tỉnh sau khi kết thúc encounter Ngư Tinh.
4. Ngư Tinh từng bị Lạc Long Quân chém đứt đuôi; phần đuôi lửa mọc lại nhờ `LG-01`.
5. Ngư Tinh biết về lời hứa bảo hộ, nhưng không biết toàn bộ sự thật của Hỗn Mang.
6. Không có lựa chọn nào khiến người chơi bỏ qua `LG-01`; lựa chọn chỉ đổi cách thu hồi và trạng thái của mảnh ngọc.
7. Chapter kết thúc khi Long Nhân rời khỏi vùng nước chết, không phải khi lên đất liền.

## Chapter end states

### `CH01_END_RELEASED`

Ngư Tinh được giải thoát khỏi vòng lặp lời hứa. Long Nhân nhận `LG-01` qua sự đồng thuận của nguyên thần. Thủy tộc mở lối lên bờ và gửi một lời cảnh báo về những khuôn mặt giả trong sương.

### `CH01_END_FORCE`

Ngư Tinh bị đánh bại nhưng bond chưa được giải quyết. Long Nhân lấy `LG-01` từ xác/giáp vảy. Thủy tộc không tấn công, nhưng không gọi Long Nhân là người kế thừa; họ gọi là kẻ mang sức mạnh mới.

### `CH01_END_ABSORBED`

Long Nhân cưỡng đoạt nguyên thần sau trận đấu. `dragon_hunger` tăng. Nước quanh đền chuyển đen trong vài nhịp, gieo mầm cho Ending E-02 nhưng không khóa ending.

## Oan Khuất Ẩn (boss ẩn — ADR-004)

CH-01 có một màn ẩn tùy chọn `CH-01-HIDDEN` (Bãi xác thuyền dưới vực) và boss ẩn `HB-01` Ma Da — Vong Đáy Vực.

- Không chặn tiến độ chính; bỏ qua vẫn đạt `CH01_END_*` và `CH01_COMPLETE`.
- Giải thoát `HB-01` (đánh hồi chuông "không-về" + gọi tên một vong) ⇒ `hidden_released +1`, `mercy_marks +1`, và mở `hidden_truth` đào sâu `TRUTH_SEAL_WAS_NEVER_BROKEN`: *lời hứa bảo hộ từng thất bại trước cả khi đền chìm*.
- `hidden_released = 5` (đủ 5 chương) là một điều kiện của kết thúc thật `E-04` (xem `02` §7).
- Chi tiết: `01-scene-flow.md` (CH-01-HIDDEN), `03-quests-and-choices.md` (Q-CH01-00H), `05-boss-encounter.md` (HB-01), `08-visual-design.md` (character card HB-01).

## Handoff summary

CH-01 cần ba lớp bàn giao:

- **Narrative:** scene flow, dialogue, choice effects, boss fate.
- **Gameplay hook:** bơi, xoáy nước, bệ thủy triều, Thủy Ảnh, phase telegraph, tương tác bia lời hứa.
- **Art/audio hook:** san hô chết, đền chìm, đuôi lửa, âm thanh áp lực nước, tiếng gọi bị bóp méo.

Thông số damage, map coordinates, animation frame, model topology và VFX implementation để `TBD` ở phase sau.
