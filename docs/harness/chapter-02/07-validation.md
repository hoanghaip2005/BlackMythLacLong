# CH-02 Validation

## Narrative acceptance

- [ ] Opening tái lập rằng Long Nhân giờ đã nghi ngờ mọi khuôn mặt (hậu quả CH-01), không quay lại tin tưởng ngây thơ.
- [ ] Người chơi hiểu mục tiêu trước mắt (theo tiếng hát / tìm nguồn mất tích) trước khi nhận lore toàn cục.
- [ ] Ba clue thật/giả đủ để một người chơi tinh ý loại được mặt nạ mà không cần HUD-only giải thích.
- [ ] Reveal "Hồ Tinh là nơi trú ẩn, không phải kẻ bắt người" đến qua hành động/đối chiếu, không qua độc thoại.
- [ ] Khâu đạo sĩ là bi kịch có nguyên nhân (người bảo hộ bị lợi dụng), không phải phản diện rơm.
- [ ] Kẻ ăn tên (Hỗn Mang) chỉ được gieo, không bị gọi tên đầy đủ hay xác nhận "phong ấn vỡ".
- [ ] Chương đóng với hook cụ thể sang CH-03 (rừng Phong Châu / tiếng binh khí / rễ nuốt).

## Branch acceptance

- [ ] `C-CH02-001` đổi trust/feedback mà không hard-lock Hồ Tinh về một số phận.
- [ ] `C-CH02-002` đổi cách boss đọc Long Nhân + thoại + lượng clue, không phải nhãn tốt/xấu.
- [ ] `C-CH02-003` resolve thành đúng một boss fate (`released`/`defeated_by_force`/`absorbed`).
- [ ] `C-CH02-00H` resolve thành đúng một fate cho HB-02.
- [ ] Release đòi hành động (đối chiếu + đọc gương + nghe) chứ không phải một lựa chọn thoại.
- [ ] Force victory vẫn hoàn thành được và trung thực (không trừng phạt chỉ vì chiến đấu).
- [ ] Absorption cho lợi ích sức mạnh ngay (Phân Thân/Long Khí) kèm cost narrative rõ.
- [ ] Mỗi choice quan trọng có đủ 5 trường (ý định / thông tin / hậu quả gần / hậu quả xa / feedback).

## Boss acceptance

- [ ] B02-P1: cơ chế "ba khuôn mặt" đọc được bằng bóng + gương; có counterplay không đòi parry hoàn hảo.
- [ ] B02-P2: chín đuôi + đầm dâng có telegraph và ngôn ngữ silhouette khác P1.
- [ ] `B02-P0` không bị tính là combat phase.
- [ ] Không phase nào bắt buộc một stance/spell duy nhất cho mọi người chơi.
- [ ] Boss không "chết" trước khi fate được ghi.
- [ ] HB-02 không thể bị "thuần DPS" ra `released`; gọi tên là điều kiện thật.
- [ ] HB-02 là bi kịch độc lập, không chỉ là reskin của B-02.

## Hidden content acceptance (ADR-004)

- [ ] `CH-02-HIDDEN` là tùy chọn; bỏ qua vẫn complete chương và vẫn tới được CH-03.
- [ ] Giải thoát HB-02 set `CH02_HIDDEN_RELEASED`, `hidden_released +1`, `mercy_marks +1`.
- [ ] Cưỡng đoạt/kết liễu HB-02 KHÔNG tăng `hidden_released`; cưỡng đoạt tăng `dragon_hunger +1`.
- [ ] `hidden_truth` đào sâu `TRUTH_FOX_WAS_A_REFUGE` (Hồ Tinh giữ tên; Hỗn Mang mới là kẻ ăn tên).
- [ ] Không tạo Long Ngọc thứ sáu từ hidden content.
- [ ] Thiếu `CH02_HIDDEN_RELEASED` khiến `hidden_released < 5` ⇒ không đạt `E-04` (chỉ `E-04-PARTIAL`).

## Continuity acceptance

- [ ] Đúng `LG-02` được trao trong CH-02; không mô tả là "mảnh 2 trong 6".
- [ ] `TRUTH_FOX_WAS_A_REFUGE` được gieo + (một phần) xác nhận, chưa phải bằng chứng toàn cục tới CH-06.
- [ ] Không có Lạc Long Quân xuất hiện vật lý; chỉ có Tiếng Vọng.
- [ ] Không khẳng định phong ấn đã vỡ.
- [ ] Rìu Thần Thạch Sơn đã có (không "thức tỉnh lại").
- [ ] `Phân Thân` lần đầu khả dụng ở CH-02 (không xuất hiện sớm hơn).
- [ ] Người Hát / dân đầm phản ứng nhất quán với `tribal_trust` và boss fate.
- [ ] Hook CH-01 (tiếng hát nữ trong sương) được nối; hook CH-03 (rễ/binh khí) được gieo.
- [ ] Thuật ngữ khớp glossary toàn cục (`01 §10`).

## Vertical slice acceptance

CH-02 vertical slice sẵn sàng cho cross-discipline review khi:

1. S01–S02 chơi được với placeholder đầm/sương và silhouette cáo placeholder.
2. Người chơi trải nghiệm được cả hai nhánh `C-CH02-001` và `C-CH02-002` ở các test run riêng.
3. S03 truyền đạt cơ chế "ba khuôn mặt / đối chiếu" mà không cần lore dump.
4. S05 truyền đạt bond (Hồ Tinh = nơi trú ẩn) bằng hành động + gương nước.
5. B-02 hỗ trợ ít nhất một force path và một release path.
6. `CH-02-HIDDEN` + HB-02 chơi được và ghi đúng `hidden_released`/`mercy_marks`.
7. State log ghi mọi required flag + đúng một boss fate cho B-02 (và cho HB-02 nếu vào hidden).
8. S06 cho thấy aftermath khác biệt rõ giữa released / force / absorbed.
