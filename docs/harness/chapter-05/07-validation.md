# CH-05 Validation

## Narrative acceptance

- [ ] Opening cho thấy Ngã Ba Hạc là một *cuộc tranh chấp*, và làng nổi kẹt giữa hai thế lực.
- [ ] Người chơi hiểu mục tiêu trước mắt (qua ngã ba, thu `LG-05`) trước khi hiểu lore toàn cục.
- [ ] Cả hai giao đều được trình bày là **tin mình tự vệ**; không bên nào là "ác tuyệt đối".
- [ ] Reveal "ký ức hai giao bị bóp méo" đến qua *hành động điều tra* (đối chiếu hai ký ức cùng một ngày), không qua độc thoại giảng giải.
- [ ] `TRUTH_CONFLICT_WAS_FED` được **gieo** (thấy thứ nuôi xung đột không thuộc hai giao) và **xác nhận** (đủ 5 mảnh ghép thành con đường duy nhất), không khẳng định phong ấn vỡ.
- [ ] Hỗn Mang chỉ hiện diện như *lực nuôi xung đột*, chưa gọi tên đầy đủ (để dành CH-06).
- [ ] Long Nhân không trở thành "người phân xử duy nhất" như một mặc định chiến thắng; chủ đề này được đặt câu hỏi.
- [ ] Chương khép với hook cụ thể sang CH-06 (bậc tế đàn lộ ra → Nghĩa Lĩnh).

## Branch acceptance

- [ ] `C-CH05-001` (nghe bên nào trước) đổi thoại/anchor mà không hard-lock bên còn lại.
- [ ] `C-CH05-002` (`pit` vs `cut`) đổi cách vào `released` (dễ hơn vs thẳng) và đổi hậu quả (mất `CH05_BOSS_NAMED_WOUND` ở nhánh pit-tới-cùng); không đổi thành nhãn đạo đức.
- [ ] `C-CH05-003` resolve thành **đúng một** boss fate cho `B-05`.
- [ ] `released` đòi hành động (đủ neo + nghe cả hai + gọi tên nỗi đau), không phải một câu thoại.
- [ ] Force victory hoàn thành được và trung thực; absorption cho lợi ích cảm nhận ngay + cost narrative rõ.
- [ ] Mọi choice quan trọng có đủ 5 trường (ý định / thông tin / hậu quả gần / hậu quả xa / tín hiệu phản hồi).

## Boss acceptance

- [ ] `B05-P0` (intro) không bị tính là combat phase.
- [ ] Phase A (Song Giao) và Phase B (Hắc Giao Long) có narrative trigger, visual read, telegraph và counterplay **khác nhau**.
- [ ] Transformation beat A→B đọc được là **cưỡng ép/đau**, không phải power-up tự nguyện.
- [ ] Phase A cho phép "đứng giữa, dẫn hai giao va nhau" như một counterplay hợp lệ (không bắt parry hoàn hảo).
- [ ] `Thủy Ảnh` có khoảnh khắc dùng bắt buộc (hai luồng chồng) và optional mastery.
- [ ] Ba neo ký ức đọc được bằng hình ảnh/âm thanh, không cần HUD-only.
- [ ] Boss không "chết" trước khi fate được ghi; hợp thể không phải "boss mới" mà là một thực thể bị ép.

## Hidden content acceptance (ADR-004)

- [ ] `CH-05-HIDDEN` là optional; bỏ qua không block `LG-05` hay ending, chỉ khóa `E-04` trọn vẹn.
- [ ] `HB-05` (Giao Mẫu) có bi kịch riêng, là **nạn nhân thứ ba** của cuộc tranh chấp, không phải trở ngại thuần.
- [ ] Giải thoát `HB-05` cho hai giao **nhớ lại mẹ** (hậu quả nhìn thấy được trong phase B: hợp thể khựng, hai đầu thôi cãi).
- [ ] `released` HB-05 ⇒ `hidden_released +1`, `mercy_marks +1`; absorb/force ⇒ `dragon_hunger +1`, **không** tăng `hidden_released`.
- [ ] `hidden_released` chỉ tăng tối đa 1 ở CH-05 và chỉ khi HB-05 released.
- [ ] Boss ẩn không phá `boss_fates[B-05]`, không tạo Long Ngọc, không đổi thứ tự 6 chương.
- [ ] Boss ẩn không phải một trong "Ba Nguyên thần phụ" (`NGUYEN-THAN-*`); hai hệ thống không chồng ID.

## Continuity acceptance

- [ ] `LG-05` được trao **đúng một lần** trong CH-05; sau CH-05 người chơi có đủ 5 mảnh, không có mảnh 6.
- [ ] `TRUTH_CONFLICT_WAS_FED` gieo + xác nhận đúng chỗ; không mâu thuẫn các truth flag trước.
- [ ] Không có thoại nào trước CH-06 khẳng định chắc chắn phong ấn đã vỡ.
- [ ] Không có sự xuất hiện vật lý trực tiếp của Lạc Long Quân.
- [ ] Rìu Thần Thạch Sơn không bị mô tả là "mới thức tỉnh" (đã có từ CH-01).
- [ ] `boss_fates[B-05]` và (nếu có) `boss_fates[HB-05]` được ghi; `hidden_released` clamp 0..5.
- [ ] Hook ra CH-06 khớp `08-continuity-matrix` (đường lên Nghĩa Lĩnh; Hỗn Mang CH-06 "sao chép Long Nhân").

## Vertical slice acceptance

CH-05 vertical slice sẵn sàng cho cross-discipline review khi:

1. S01–S02 chơi được với placeholder environment (làng nổi, hai cột nước) và placeholder giao silhouette.
2. Người chơi trải nghiệm được cả hai outcome của `C-CH05-001` (nghe Giao Anh trước / Giao Em trước) ở hai test run.
3. Phase A (Song Giao) cho phép ít nhất một lần "dẫn hai giao va nhau" thành công bằng placeholder.
4. Transformation beat A→B chạy được như một scripted beat đọc được là cưỡng ép.
5. Phase B (Hắc Giao Long) hỗ trợ ít nhất một force victory path và một release path.
6. `CH-05-HIDDEN` (Giao Mẫu) chơi được như một encounter tĩnh với hai outcome (release/absorb).
7. State log ghi đủ flag bắt buộc + đúng một `boss_fates[B-05]` + (nếu vào ẩn) `hidden_released`.
8. S05 cho thấy aftermath **khác nhau rõ** cho released / force / absorbed, và lộ bậc tế đàn dẫn CH-06.
