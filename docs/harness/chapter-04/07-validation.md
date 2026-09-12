# CH-04 Validation

## Narrative acceptance

- [ ] Opening chuyển ngôn ngữ di chuyển từ nước (CH-01) sang chiều thẳng đứng/gió mà vẫn giữ cảm giác cô độc, bị bỏ quên.
- [ ] Người chơi hiểu mục tiêu trước mắt (lên đỉnh, lấy `LG-04`) trước khi học lore triều đại.
- [ ] Đại Bàng Tinh được thiết lập là **vật chứa phẫn nộ của người bị xóa tên**, không phải một con thú ác.
- [ ] Bà Lệ và Hồn Tướng Lưu Đày đều có lý do chính đáng; không ai là "phe đúng tuyệt đối".
- [ ] Reveal "Lạc Long Quân rời đi khi con người dùng huyết thống làm lý do cai trị" được **xác nhận** qua lời chứng + Tiếng Vọng, không qua cutscene toàn tri.
- [ ] Chương khép bằng một hook cụ thể tới CH-05 (Ngã Ba Hạc / hai dòng nước tranh nhau).

## Branch acceptance

- [ ] `C-CH04-001` (hồn trong lông) đổi `mercy_marks`/`dragon_hunger` và phản ứng arena, không giết hay hard-lock nội dung.
- [ ] `C-CH04-002` (cổng narrative: nghe vs săn) mở/đóng bond path mà vẫn cho phép hoàn thành chương.
- [ ] `C-CH04-003` (phán quyết) đổi cách boss đọc người chơi và mở/khóa cửa sổ điều tra.
- [ ] `C-CH04-004` resolve thành đúng một boss fate (`released`/`defeated_by_force`/`absorbed`).
- [ ] Release yêu cầu **hành động + lắng nghe** (nghe lời kể + gọi tên tội + khắc/phục hồi tên), không phải một câu thoại.
- [ ] Force victory vẫn hoàn thành được và "trung thực" (không trừng phạt oan).
- [ ] Absorption cho lợi ích sức mạnh ngay kèm cost narrative rõ.

## Boss acceptance

- [ ] Mỗi phase (`B04-P1-DIVE`, `B04-P2-VESSEL`) có một narrative trigger riêng.
- [ ] Mỗi phase có telegraph hình ảnh/âm thanh (cánh gập, gió đổi hướng, đá trôi, lõi sáng).
- [ ] Verticality, gió đổi hướng và đứt gãy trọng lực đọc được mà không cần HUD-only explanation.
- [ ] Không phase nào bắt buộc một stance/spell duy nhất cho mọi người chơi.
- [ ] `Lôi Kích` có một khoảnh khắc ngắt nhịp bắt buộc (dạy) và về sau tùy chọn thành thạo.
- [ ] Boss không "chết" trước khi fate được ghi.
- [ ] Hai silhouette phase (một con chim vs đàn lông nhiều bóng) phân biệt rõ.
- [ ] Không có damage/HP/frame number trong tài liệu (R-05).

## Hidden content acceptance (ADR-004)

- [ ] `HB-04` Tù Trưởng Lệ Đá tồn tại như một **Oan Khuất Ẩn** tùy chọn ở `CH-04-HIDDEN`.
- [ ] Hidden encounter hoàn thành được **không cần giao chiến** (lắng nghe/khắc tên).
- [ ] Release `HB-04` tăng `hidden_released +1` và `mercy_marks +1`; absorb/defeat **không** tăng `hidden_released`.
- [ ] `hidden_truth` CH-04 đào sâu `TRUTH_EXILE_WAS_ERASED` (tên bị xóa **có chủ đích**), không tạo Long Ngọc mới, không tạo truth flag toàn cục mới.
- [ ] Bỏ hidden vẫn hoàn thành chương và nhận `LG-04`; chỉ lớp hòa giải trọn vẹn của `E-04` bị ảnh hưởng.
- [ ] `CH04_HIDDEN_RELEASED` và `Q_CH04_00H_COMPLETE` được ghi đúng trong state log.
- [ ] Có cultural review note cho chủ đề "bộ tộc bị xóa tên".

## Continuity acceptance

- [ ] Đúng một `LG-04` được trao ở CH-04; tổng số mảnh sau chương là 4 (không mô tả "mảnh thứ năm/sáu").
- [ ] `TRUTH_EXILE_WAS_ERASED` được gieo (S03) và xác nhận (S05), không giải thích trọn vẹn Hỗn Mang.
- [ ] CH-04 là chương **xác nhận** "Long Nhân không phải Lạc Long Quân" (03 "Phân bố reveal"); không có hồi sinh/tái nhập của Lạc Long Quân.
- [ ] Không có sự xuất hiện vật lý trực tiếp của Lạc Long Quân; chỉ Tiếng Vọng/dấu tích.
- [ ] Không thoại nào trước CH-06 khẳng định chắc chắn phong ấn đã vỡ.
- [ ] Rìu Thần Thạch Sơn được đối xử như **đã có** (từ CH-01), không "thức tỉnh lại".
- [ ] Hỗn Mang chỉ xuất hiện gián tiếp (khuếch đại phẫn nộ người bị xóa tên), không lộ diện.
- [ ] Naming khớp glossary toàn cục (`Đại Bàng Tinh`, `Tù Trưởng Lệ Đá`, `LG-04`, `TRUTH_EXILE_WAS_ERASED`, `HB-04`).
- [ ] Hậu quả của `C-CH04-001` (hồn bị lợi dụng) xuất hiện trước khi CH-04 kết thúc (nguyên tắc chống nhánh giả, 02 §8).

## Vertical slice acceptance

CH-04 vertical slice sẵn sàng cho cross-discipline review khi:

1. S01-S02 chơi được với placeholder environment (bệ đá hẹp, gió) và placeholder silhouette Đại Bàng.
2. Người chơi trải nghiệm được cả hai outcome của `C-CH04-001` (giải thoát / lợi dụng hồn) trong hai lượt test.
3. S03-S04 truyền đạt được lời chứng bộ tộc và cổng narrative (`C-CH04-002`) mà không lore dump.
4. `B-04` hỗ trợ ít nhất một đường force victory và một đường release test; hai phase đọc khác nhau.
5. `HB-04` hidden encounter chơi được không cần combat, và ghi đúng `hidden_released` khi release.
6. State log ghi đủ mọi required flag và một boss fate cho cả `B-04` lẫn `HB-04`.
7. S05 cho thấy aftermath khác biệt rõ cho released / force / absorbed, và reveal huyết thống chạy ở cả ba.
