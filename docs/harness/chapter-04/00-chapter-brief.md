# CH-04: Lệ Đá Đỉnh Sương

## Trạng thái

- ID: `CH-04`
- Version: `0.1`
- Status: `draft`
- Vùng: Núi Thạch Môn — đường đá vỡ, rừng bia không tên, khe vực và đỉnh tế sương.
- Thời lượng narrative mục tiêu: 100-130 phút cho first playthrough, chưa tính khám phá tùy chọn và màn ẩn.
- Mảnh Long Ngọc: `LG-04` (mảnh thứ tư).
- Boss chính: `B-04`, Đại Bàng Tinh.
- Boss ẩn (ADR-004): `HB-04`, Tù Trưởng Lệ Đá.
- Truth flag: `TRUTH_EXILE_WAS_ERASED`.

## Chapter promise

Người chơi đến Thạch Môn để lấy mảnh ngọc thứ tư và gặp một "con quái vật trên đỉnh núi". Cuối chương, người chơi hiểu ba điều:

1. Đại Bàng Tinh không phải một con thú; nó là **vật chứa phẫn nộ** của những người bị xóa khỏi lịch sử triều đại.
2. Công lý bị trì hoãn đủ lâu sẽ lên men thành **trả thù** — và trả thù vẫn nhân danh công lý.
3. Huyết thống rồng của Long Nhân **không phải giấy phép cai trị**; chính vì con người bắt đầu lấy huyết thống làm lý do thống trị mà Lạc Long Quân đã rời đi. Đây là chương **xác nhận** Long Nhân không phải Lạc Long Quân.

## Dramatic question

**Khi một dân tộc bị xóa tên đòi lại công lý bằng chính lưỡi gió đã chém họ, Long Nhân sẽ trả lại tên cho họ hay mượn cơn giận của họ làm sức mạnh?**

## Emotional arc

| Chặng | Trạng thái Long Nhân | Cảm xúc người chơi | Hình ảnh chủ đạo |
|---|---|---|---|
| Mở đầu | Leo lên nơi bị bỏ quên | Lạnh, choáng ngợp, mất phương hướng | Đường đá vỡ, sương phủ, gió đổi hướng |
| Khám phá | Thấy hồn người kẹt trong lông vũ | Bất an, thương cảm | Lông chim lớn như mái chèo, bên trong có bóng người |
| Điều tra | Nghe lời chứng của bộ tộc mất tên | Phẫn nộ thay, hoài nghi lịch sử | Rừng bia không tên, bản đồ khắc bằng trí nhớ |
| Đối đầu | Bị Đại Bàng gọi là "kẻ cai trị mới" | Giận dữ, bị phán xét | Bóng chim che mặt trời, đòn bổ nhào, trọng lực gãy |
| Hậu quả | Tự chọn cách nhận `LG-04` | Trách nhiệm, hiểu ra sự thật về huyết thống | Lệ đá rơi xuống mây |

## Chapter non-goals

- Chưa giải thích trọn vẹn Hỗn Mang; chỉ cho thấy nó **khuếch đại phẫn nộ của người bị xóa tên**.
- Chưa mở nghi lễ cuối; `LG-04` là mảnh thứ tư, người chơi còn thiếu `LG-05`.
- Không cho Lạc Long Quân xuất hiện trực tiếp; chỉ có Tiếng Vọng và dấu tích, và chính Tiếng Vọng **không biện hộ** cho việc lấy huyết thống làm quyền cai trị.
- Không biến Đại Bàng Tinh thành "đại bàng huy chương" của quyền lực; nó là yêu quái bi kịch.
- Không khẳng định phong ấn đã vỡ; mọi lời về "trật tự cũ sụp đổ" ở đây là lời kể của người bị thua, cần được kiểm chứng.

## Canon lock riêng cho CH-04

1. Long Nhân leo Thạch Môn bằng đường đá vỡ; verticality và gió là ngôn ngữ di chuyển chính, không phải bơi như CH-01.
2. Đại Bàng Tinh là **vật chứa** phẫn nộ tập thể của các bộ tộc bị xóa tên; nó nói bằng giọng của nhiều người, không phải một con thú đơn thuần.
3. `LG-04` nằm trong ổ Đại Bàng; không có lựa chọn nào cho phép bỏ qua `LG-04`, chỉ đổi **cách** thu hồi và trạng thái mảnh.
4. Reveal "Lạc Long Quân rời đi khi con người dùng huyết thống làm lý do cai trị" chỉ được **xác nhận** ở CH-04 (đã gieo mồi từ CH-01), qua lời chứng + Tiếng Vọng, không qua cutscene toàn tri.
5. Rìu Thần Thạch Sơn đã có từ CH-01; CH-04 dùng nó như công cụ leo/chém/đỡ, không "thức tỉnh lại".
6. Boss ẩn `HB-04` là tùy chọn; không mở vẫn hoàn thành được chương và vẫn nhận `LG-04`.
7. Chương kết thúc khi lệ đá rơi xuống mây và Long Nhân rời đỉnh, không phải khi Đại Bàng gục.

## Chapter end states

### `CH04_END_RELEASED`

Đại Bàng Tinh được giải thoát: phẫn nộ được **gọi đúng tên** (tội lỗi của triều đại bị nêu ra, tên bộ tộc được trả lại). Nguyên thần đồng thuận trao `LG-04`. Các hồn bị xóa tan thành sương sáng thay vì rơi xuống vực.

### `CH04_END_FORCE`

Đại Bàng Tinh bị đánh bại nhưng bond chưa giải quyết. Long Nhân lấy `LG-04` từ ổ/xương lông. Phẫn nộ không tan; nó lắng xuống như tro, và một phần hồn vẫn kẹt trong lông vũ.

### `CH04_END_ABSORBED`

Long Nhân cưỡng đoạt nguyên thần phẫn nộ. `dragon_hunger` tăng mạnh. Gió trên đỉnh đổi chiều vĩnh viễn; đá tiếp tục khóc nhưng không ai nghe. Gieo mầm E-02, không khóa ending.

## Handoff summary

CH-04 cần bốn lớp bàn giao:

- **Narrative:** scene flow, dialogue, choice effects, boss fate, hidden boss `HB-04`, reveal huyết thống.
- **Gameplay hook:** verticality, bệ đá hẹp, gió đổi hướng, đòn bổ nhào, đứt gãy trọng lực, `Lôi Kích`/`Thế Đột`, màn ẩn leo khe đá.
- **Art/audio hook:** đá - sương - lông vũ - lệ đá, bia không tên, tiếng nhiều giọng chồng lên nhau, gió làm méo âm thanh.
- **Cultural hook:** chủ đề "bộ tộc bị xóa tên" là bi kịch lịch sử có thật; cần cultural review, xử lý trang trọng, không khai thác như trang trí.

Thông số damage, map coordinates, animation frame, model topology và VFX implementation để `TBD` ở phase sau.
