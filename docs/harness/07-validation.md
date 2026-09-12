# Validation Harness

## 1. Canon validation

- [ ] Long Nhân không bị gọi hoặc mô tả như Lạc Long Quân.
- [ ] Chỉ có năm Long Ngọc.
- [ ] Phong ấn chưa từng bị phá được giữ đúng trước reveal cuối.
- [ ] Hỗn Mang có nguồn gốc từ oán nghiệp chiến tranh.
- [ ] Boss có inner wound và desire riêng.
- [ ] Tên địa danh, thuật ngữ và ID khớp glossary.

## 2. Branch validation

- [ ] Mỗi choice quan trọng có state change.
- [ ] State change có feedback gần và/hoặc feedback xa.
- [ ] Không có ending condition mâu thuẫn với Resolution Rules.
- [ ] `reconcile` thiếu điều kiện lõi chuyển đúng sang `E-03-BITTER`; nếu chỉ thiếu `hidden_released = 5` (đủ các điều kiện lõi khác) thì chuyển sang `E-04-PARTIAL` (ADR-004).
- [ ] `absorb` hoặc `dragon_hunger >= 4` có dấu hiệu được gieo trước ending.
- [ ] Người chơi có cách suy luận điều kiện ending qua fiction.

## 3. Scene validation

- [ ] Scene có entry state và exit state.
- [ ] Có một dramatic question duy nhất.
- [ ] Có ít nhất một hành động hoặc quan sát dành cho người chơi.
- [ ] Mỗi beat làm thay đổi thông tin, quan hệ hoặc mục tiêu.
- [ ] Không lặp lại lore mà gameplay đã truyền đạt.
- [ ] Có transition rõ sang scene kế.

## 4. Quest validation

- [ ] Player goal dùng động từ cụ thể.
- [ ] Fictional reason thuyết phục.
- [ ] Cost/fail state không phải phạt ngẫu nhiên.
- [ ] Reward có ít nhất một tác động narrative hoặc state.
- [ ] Quest phụ liên kết theme, phe, boss hoặc ending.

## 5. Boss validation

- [ ] Mỗi phase có narrative trigger.
- [ ] Boss có đúng hai combat phase; intro không bị tính thành phase chiến đấu.
- [ ] Phase 1 là người lai cá; phase 2 là cá vực sâu khổng lồ.
- [ ] Telegraph và counterplay được mô tả ở mức trải nghiệm.
- [ ] Arena kể được một phần lịch sử của boss.
- [ ] Điểm yếu có ý nghĩa biểu tượng và chức năng chiến đấu.
- [ ] Có ít nhất hai boss fate khác nhau.
- [ ] Aftermath thay đổi theo fate hoặc state liên quan.

## 5b. Hidden boss validation (Oan Khuất Ẩn — ADR-004)

- [ ] Mỗi chương `CH-01..CH-05` có đúng một boss ẩn `HB-0X` và một màn ẩn `CH-0X-HIDDEN` (tùy chọn). `CH-06` không có boss ẩn.
- [ ] Boss ẩn có `inner_wound`, `desire` và `bond_resolution`; không mô tả như ác tuyệt đối.
- [ ] Bỏ boss ẩn vẫn hoàn thành chương; không khóa `CH0X_END_*` hay tiến độ chính.
- [ ] Chỉ `released` cộng `hidden_released` (+`mercy_marks`); `defeated_by_force` không cộng; `absorbed` cộng `dragon_hunger` và không cộng `hidden_released`.
- [ ] `hidden_truth` chỉ đào sâu `TRUTH_*` của chương; không tạo truth flag toàn cục mới, không tạo Long Ngọc thứ sáu.
- [ ] `hidden_released` clamp 0..5; `E-04` đòi `hidden_released = 5`.
- [ ] Boss ẩn chạm tín ngưỡng dân gian (vd `HB-01` ma da) có ghi chú nhạy cảm và cultural review.

## 6. AI output validation

- [ ] Có `CONTENT_ID`, `STATUS`, `DEPENDENCIES`, `SELF_CHECK`.
- [ ] Không tự tạo canon mới mà không gắn `proposed`.
- [ ] Không thêm implementation chưa yêu cầu.
- [ ] Không dùng từ “tốt/xấu” làm nhãn duy nhất cho choice.
- [ ] Các câu hỏi review thật sự không thể giải bằng context đã nạp.

## 7. Cultural review

- [ ] Phân biệt cảm hứng hư cấu và tuyên bố lịch sử.
- [ ] Không dùng biểu tượng văn hóa khác như đồ trang trí ngẫu nhiên.
- [ ] Nhân vật và cộng đồng có agency, không chỉ làm nền cho Long Nhân.
- [ ] Bi kịch không biến thành lời biện hộ cho mọi hành vi của boss.
- [ ] Có ghi chú nhạy cảm nếu scene chạm vào chiến tranh, mất mát hoặc tín ngưỡng.

## 8. Visual harness review

- [ ] Silhouette của nhân vật đọc được ở khoảng cách gameplay.
- [ ] Outfit, vũ khí, phụ kiện và attachment/socket được mô tả độc lập.
- [ ] Bàn chân, grip và hướng vũ khí không đảo trục trong pose trung tính hoặc combat pose.
- [ ] Palette, material, wear và corruption phục vụ đúng identity và phase narrative.
- [ ] Motif Việt Nam được ghi nguồn cảm hứng; motif Trung Hoa/Nhật bị cấm không xuất hiện.
- [ ] Source asset, license, modification scope, `.blend`, preview và asset IDs resolve.
- [ ] Cultural review hoàn tất trước khi visual card chuyển `approved` hoặc `locked`.

## 9. Acceptance criteria cho narrative vertical slice

Vertical slice đầu tiên nên gồm CH-01 từ thức tỉnh đến hậu quả boss. Đạt khi:

- Người chơi hiểu mục tiêu thu hồi Long Ngọc mà chưa cần biết toàn bộ lore.
- Người chơi nhận thấy Ngư Tinh không chỉ là quái vật.
- Có ít nhất hai cách giải quyết bond với hậu quả khác nhau.
- Hệ thống ghi được `boss_fates[NGU_TINH]`, `LG-01`, `memory_recovered`, `mercy_marks`, `dragon_hunger`.
- Scene cuối chương cho thấy một phần ký ức và mở động lực sang CH-02.
- Không cần asset hoàn chỉnh để review logic narrative; placeholder được chấp nhận.
