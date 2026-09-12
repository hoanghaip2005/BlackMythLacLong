# CH-03 Validation

## Narrative acceptance

- [ ] Opening establishes Phong Châu là kinh đô cũ bị rừng nuốt, không phải rừng hoang vô danh.
- [ ] Người chơi hiểu mục tiêu trước mắt (qua rừng, tìm nguồn yêu khí) trước khi học lore toàn cục.
- [ ] Hai phe vong linh (Hiến muốn buông / Trưởng muốn giữ thề) đều có lý, không phe nào là "ác".
- [ ] Ba bia lời thề truyền tải: lời thề chính nghĩa, người bị xóa tên, và một phần TỰ NGUYỆN ở lại; không bia nào khẳng định phong ấn vỡ.
- [ ] Mong muốn của Mộc Tinh vẫn hiểu được mà không biện minh cho việc nó ăn mòn người chết.
- [ ] Rìu Thần Thạch Sơn được đối xử như vũ khí đã đồng hành từ CH-01, không "thức tỉnh lại".
- [ ] Chapter closes with a concrete hook to CH-04 (núi đá, bóng lông vũ).

## Branch acceptance

- [ ] `C-CH03-001` đổi trust/feedback mà không giết hay khóa cứng Hiến.
- [ ] `C-CH03-002` đổi cách đọc boss và thoại (nghe/gọi tên vs phán xét vs im lặng).
- [ ] `C-CH03-003` resolve vào đúng một boss fate của `B-03`.
- [ ] Release đòi hành động (giải thoát nút rễ) + nghe lời thề, không chỉ một câu thoại.
- [ ] Force victory vẫn hoàn thành được và trung thực.
- [ ] Absorption cho power fantasy ngay + cost narrative rõ (vệt đen, "kẻ cầm dây mới").
- [ ] `sacrificed` chỉ xảy ra khi đã xây ân nghĩa, không phải đường tắt mặc định.

## Hidden content acceptance (ADR-004)

- [ ] `CH-03-HIDDEN` là tùy chọn; bỏ nó vẫn hoàn thành `Q-CH03-001` và đạt `E-01/E-02/E-03`.
- [ ] `HB-03` Tướng Quân Vô Đầu có inner wound, desire và bond_resolution; không phải boss "ác".
- [ ] Rễ tự-nguyện của `HB-03` đọc khác rễ ký sinh của `B-03` (màu/hướng).
- [ ] Chỉ `released` của `HB-03` cộng `hidden_released` và `mercy_marks`; absorb/force thì không.
- [ ] Giải thoát `HB-03` mở `hidden_truth` đào sâu `TRUTH_OLD_ARMY_WAS_BOUND`, không tạo truth flag toàn cục mới.
- [ ] `HB-03` không tạo Long Ngọc mới (giữ đúng 5 mảnh).

## Boss acceptance

- [ ] Mỗi phase có một narrative trigger riêng.
- [ ] Mỗi phase có telegraph hình ảnh và âm thanh.
- [ ] Tương tác rễ/nút rễ/lõi đỏ hiểu được mà không cần HUD-only explanation.
- [ ] Không phase nào bắt mọi người chơi dùng một stance/spell duy nhất.
- [ ] `Thế Trảm` có một khoảnh khắc dạy bắt buộc và mastery tùy chọn về sau.
- [ ] Boss không chết trước khi fate choice được resolve.
- [ ] `HB-03` có intro không-đánh (`HB03-P0`) tách khỏi nhịp combat.

## Continuity acceptance

- [ ] Đúng `LG-03` được trao trong CH-03 (không mảnh nào khác).
- [ ] `TRUTH_OLD_ARMY_WAS_BOUND` được gieo (S03) và xác nhận (B03), không giải thích trọn trước CH-06.
- [ ] Không có sự xuất hiện vật lý trực tiếp của Lạc Long Quân.
- [ ] Không reveal Đại Bàng Tinh trước hook lông vũ cuối chương.
- [ ] `LG-03` không bị mô tả là "mảnh thứ sáu" hay mảnh cuối theo nghĩa sai (đúng 5 mảnh, còn LG-04/05).
- [ ] `hidden_released` chỉ tăng qua `HB-03 released`; kiểm tra không cộng nhầm ở force/absorb.
- [ ] Không thoại nào trước CH-06 khẳng định chắc chắn phong ấn đã vỡ.
- [ ] Tên riêng/ID khớp glossary (`Mộc Tinh`, `Phong Châu`, `Vong linh Lạc Việt`, `HB-03`, `LG-03`).

## Cultural acceptance

- [ ] Mộc Tinh và vong linh lấy cảm hứng Việt/Lạc Việt, không trộn biểu tượng văn hóa khác chỉ vì hiệu ứng.
- [ ] Không biến "đội quân chết" thành hình tượng phản cảm; giữ trọng lượng cảm xúc, tránh máu me như phần thưởng.
- [ ] `HB-03` "không đầu" xử lý như mất-danh-tính/lời-thề-chưa-trọn, không như horror chặt đầu.
- [ ] Cần cultural review trước khi content chuyển `approved`/`locked`.

## Vertical slice acceptance

The CH-03 vertical slice is ready for cross-discipline review when:

1. S01-S03 chơi được với environment placeholder và silhouette xác-rễ placeholder.
2. Người chơi trải nghiệm được cả hai outcome của `C-CH03-001` (giải thoát / giữ hàng ngũ) trong hai test run riêng.
3. S04-S05 truyền tải bond (lời thề + lõi đỏ) mà không lore dump.
4. `B-03` hỗ trợ ít nhất một force victory và một release test path.
5. `HB-03` chơi được như encounter tùy chọn, có cả release và absorb path.
6. State log ghi đủ mọi required flag và đúng một boss fate cho `B-03` (và `HB-03` nếu vào màn ẩn).
7. S06 cho thấy aftermath khác biệt rõ cho released, force, absorbed (và sacrificed nếu kích hoạt).
