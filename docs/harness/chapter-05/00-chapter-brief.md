# CH-05: Song Giao Tế Thủy

## Trạng thái

- ID: `CH-05`
- Version: `0.1`
- Status: `draft`
- Vùng: Ngã Ba Hạc, làng nổi, miếu chìm và lòng sông mùa lũ.
- Thời lượng narrative mục tiêu: 100-130 phút cho first playthrough, chưa tính khám phá tùy chọn và màn ẩn.
- Mảnh Long Ngọc: `LG-05` (mảnh thứ năm và cuối cùng)
- Boss: `B-05`, Song Giao -> Hắc Giao Long
- Boss ẩn: `HB-05`, Giao Mẫu (ADR-004)
- Truth flag: `TRUTH_CONFLICT_WAS_FED`

## Chapter promise

Người chơi bước vào một vùng nước mà ai cũng tin mình là nạn nhân. Cuối chương, người chơi hiểu ba điều:

1. Cả hai Song Giao đều bị bóp méo ký ức; không có "kẻ xâm lược" tuyệt đối, chỉ có hai nỗi sợ đang tự vệ.
2. Xung đột được *nuôi* bởi một nỗi đau bị lãng quên — người mẹ mà cả hai giao đã quên. Muốn dứt phải tìm tới gốc, không phải chọn phe.
3. Sau khi thu đủ năm mảnh Long Ngọc, Long Nhân không còn là kẻ đi nhặt sức mạnh; người chơi đang cầm toàn bộ ký ức của Văn Lang và sắp phải quyết định số phận của nó.

## Dramatic question

**Khi cả hai phe đều tin mình đang tự vệ, Long Nhân sẽ chọn một bên để thắng nhanh, khiến chúng xé xác nhau, hay lội xuống đáy lũ tìm người mẹ mà cả hai đã quên?**

## Emotional arc

| Chặng | Trạng thái Long Nhân | Cảm xúc người chơi | Hình ảnh chủ đạo |
|---|---|---|---|
| Mở đầu | Đứng giữa hai tiếng gọi, không thuộc bên nào | Bất an, ướt, mất phương hướng | Làng nổi chao theo lũ, dây neo căng |
| Khám phá | Nghe cả hai giao tự xưng là người giữ ngọc | Hoài nghi, thương cảm lẫn lộn | Hai cột nước dựng ở hai nhánh sông |
| Điều tra | Nhận ra ký ức của cả hai bị bóp méo | Bứt rứt, muốn tìm gốc | Bè trôi giữa hai luồng săn nhau |
| Đối đầu | Chứng kiến hợp thể cưỡng ép | Kinh hoàng, đau thay cho chúng | Hai thân giao xoắn vào nhau thành một |
| Hậu quả | Cầm đủ năm mảnh, đứng trước tế đàn | Trách nhiệm, dự cảm | Nước rút, bậc đá hiện ra trong bùn |

## Chapter non-goals

- Chưa gọi tên đầy đủ Hỗn Mang; chỉ cho thấy "nguồn nuôi xung đột" là một dấu vết chủ động.
- Chưa giải thích phong ấn; mọi lời về "phong ấn" vẫn là diễn giải sai (giữ tới CH-06).
- Chưa mở bốn ending; CH-05 chỉ chốt điều kiện (đủ năm ngọc, đủ truth flag) rồi dẫn lên Nghĩa Lĩnh.
- Không biến giao thành rồng cung đình; giao là thuồng luồng/giao long bản địa.
- Không cho người chơi "chọn phe đúng"; cả hai giao đều sai và đều đáng thương như nhau.

## Canon lock riêng cho CH-05

1. `LG-05` là mảnh thứ năm và cuối cùng; sau CH-05 người chơi có đủ năm mảnh. Không tồn tại mảnh thứ sáu.
2. Hai Song Giao là anh em, con của Giao Mẫu; mỗi con tin lòng sông và mảnh ngọc thuộc về riêng mình vì ký ức đã bị bóp méo.
3. Hợp thể Hắc Giao Long là **cưỡng ép** do yêu khí, gây đau đớn cho cả hai; nó không phải sức mạnh tự nguyện hay tiến hóa vinh quang.
4. Giao Mẫu (`HB-05`) là boss ẩn tùy chọn; giải thoát bà mở "nạn nhân thứ ba" và là cách hòa giải thật sự của chương, cộng `hidden_released`.
5. Không có thoại nào trước CH-06 khẳng định chắc chắn phong ấn đã vỡ.
6. Rìu Thần Thạch Sơn và các ability (`Thủy Ảnh`, `Thế Ngự`, `Thế Trảm`, `Thế Đột`, `Lôi Kích`) đã mở từ các chương trước; CH-05 không giới hạn chúng.
7. Chương kết thúc khi nước rút để lộ bậc tế đàn và Long Nhân hướng về Nghĩa Lĩnh, không phải ngay khi Hắc Giao Long gục.

## Chapter end states

### `CH05_END_RELEASED`

Hai giao được tách khỏi hợp thể và giải thoát khỏi ký ức bị bóp méo; chúng nhớ lại Giao Mẫu. `LG-05` được trao qua đồng thuận. Nước rút êm, lộ bậc tế đàn; Làng nổi gọi Long Nhân là "người đã nghe cả hai bên". Mở đường hòa giải thật ở CH-06.

### `CH05_END_FORCE`

Hắc Giao Long bị đánh bại nhưng bond chưa giải quyết; hai giao tan mà không nhớ lại mẹ. Long Nhân lấy `LG-05` từ xác hợp thể. Nước rút nhưng đục; Làng nổi im lặng, không xác nhận Long Nhân là người hòa giải. `memory_recovered` không tăng từ mảnh này.

### `CH05_END_ABSORBED`

Long Nhân cưỡng đoạt nguyên thần của hợp thể. `dragon_hunger` tăng mạnh. Long Khí bùng lên nhưng nhiễm phù sa đen; một phần ký ức của hai giao bị nuốt, gieo mầm rõ cho Ending E-02. Bậc tế đàn vẫn lộ ra, nhưng nước quanh nó sẫm màu.

## Handoff summary

CH-05 cần ba lớp bàn giao:

- **Narrative:** scene flow, dialogue hai giọng đối nghịch, choice effects, hai giai đoạn boss, số phận boss ẩn Giao Mẫu.
- **Gameplay hook:** chiến đấu trên bè trôi, đánh giữa hai boss và lợi dụng va chạm, `Thủy Ảnh` thành thạo trong nước, `Thế Ngự` để "nghe" và phản đòn, hợp thể làm đổi luật arena giữa trận.
- **Art/audio hook:** phù sa, lũ, vảy giao ướt, miếu chìm, hai tiếng gọi chồng nhau thành một giọng méo khi hợp thể.

Thông số damage, map coordinates, animation frame, model topology và VFX implementation để `TBD` ở phase sau.
