# CH-06 Validation

## Narrative acceptance

- [ ] Opening đặt Long Nhân ở Nghĩa Lĩnh với đủ năm Long Ngọc, không mảnh thứ sáu.
- [ ] Reveal "phong ấn chưa từng vỡ" được **xác nhận tại đây**, không trước (Canon Lock 3).
- [ ] Hỗn Mang hiện hình là **oán nghiệp tập thể**, không phải ác quỷ vô nguồn gốc (Canon Lock 4).
- [ ] Hỗn Mang sao chép hình dáng/kỹ thuật nhưng **không** sao chép lựa chọn chưa thực hiện (Canon Lock 8); đây là chìa khóa thắng.
- [ ] Lạc Long Quân chỉ là Tiếng Vọng (`ECHO-LAC-LONG-06`), không xuất hiện trực tiếp giải quyết xung đột ở bất kỳ ending nào (Canon Lock 9).
- [ ] Câu hỏi theme "ai có quyền quyết định tương lai vùng đất" được đặt và **để người chơi trả lời**, không auto-trả lời.
- [ ] Cả bốn ending đều có **giá phải trả**; không ending nào là "thiện tuyệt đối" (Canon Lock 10).

## Branch acceptance

- [ ] `C-CH06-001` (đối đáp) đổi thoại mở đầu/đọc trận, **không** đổi ending.
- [ ] `C-CH06-002` (hành động không sao chép) là điều kiện mở `C-CH06-003`; có nhiều cách hợp lệ, không QTE-chữ đơn nhất.
- [ ] `C-CH06-003` set `final_decision` **đúng một lần**; bốn lựa chọn khác biệt về ý định + hậu quả (đủ 5 trường theo `02 §4`).
- [ ] Không dùng nhãn tốt/xấu cho bốn quyết định; hiển thị lợi ích + giá phải trả.
- [ ] Người chơi **nhận biết** các giá trị đang xây ending (không giấu hoàn toàn điều kiện, `02 §8`).

## Boss acceptance

- [ ] `B06-P0` là intro không chiến đấu, không tính vào tổng phase.
- [ ] Mỗi combat phase có narrative trigger + visual/audio telegraph riêng.
- [ ] Phase "sao chép" đọc được bằng hình ảnh (bản sao làm đúng đòn người chơi vừa làm).
- [ ] Phase "đọc lựa chọn" phản ánh **thật** `boss_fates`/`dragon_hunger`/`mercy_marks` quá khứ (dư ảnh boss đã tha khác đã absorb).
- [ ] Có đường thắng không cần perfect combat; có đường dẫn tới cả bốn `final_decision`.
- [ ] Hỗn Mang **không "chết"** theo nghĩa thường; kết cục dẫn tới `final_decision`.
- [ ] Không damage/HP/frame data/shader/asset path (R-05).

## Ending acceptance

- [ ] `E-01 LONG_VUONG`: đạt khi `restore` + `dragon_hunger<4`; `relics_purified>=3` → ổn định, `<3` → không ổn định + hook phần tiếp.
- [ ] `E-02 TAN_HON_MANG`: đạt khi `absorb`, **hoặc** `restore` + `dragon_hunger>=4`.
- [ ] `E-03 DOAN_TUYET_LONG_MACH`: đạt khi `destroy`.
- [ ] `E-04 HOA_GIAI_BACH_TOC` (thật): đạt **chỉ khi** `reconcile` + `memory_recovered=5` + `mercy_marks>=4` + `tribal_trust>=5` + đủ 5 `truth_flags` + `hidden_released=5` (ADR-004) + `absorbed<=2`.
- [ ] `E-04-PARTIAL`: `reconcile` đủ điều kiện lõi nhưng `hidden_released<5` → hòa giải một phần, còn dư oán ẩn.
- [ ] `E-03-BITTER`: `reconcile` thiếu điều kiện lõi → chuyển `destroy` mức bi kịch, cộng đồng chưa thấy sự thật.
- [ ] Resolution Rules kiểm tra **từ trên xuống**, chọn **đúng một** ending; không ending nào chồng nhau.
- [ ] Mỗi ending có ending card + hậu cảnh thế giới riêng, phản ánh lựa chọn thật.

## Continuity acceptance

- [ ] Đúng năm `LG-01..05` được dùng; **không** mảnh thứ sáu; `long_ngoc: null` cho CH-06 ở registry.
- [ ] `TRUTH_SEAL_WAS_NEVER_BROKEN` chỉ **confirm** ở CH-06 (đã gieo mồi từ CH-01).
- [ ] `hidden_released` chỉ đọc ở CH-06, không tăng; năm oan khuất HB-01..05 quyết định ở CH-01..05.
- [ ] Không thoại nào trước CH-06 khẳng định chắc chắn phong ấn đã vỡ.
- [ ] Ending **không xóa** hậu quả lựa chọn trước; chỉ tổng hợp và định nghĩa chúng (`08-continuity-matrix`).
- [ ] `boss_fates` của năm boss chính phản ánh đúng vào phase 2 và vào điều kiện `absorbed<=2` của E-04.
- [ ] ID nhất quán: scene `CH-06-S01..S05`, `CH-06-B06`, `CH-06-FULL`, `CH-06-END`; choice `C-CH06-001..003`; ending `E-01..E-04` + tag `E-04-PARTIAL`/`E-03-BITTER`.

## Vertical slice acceptance

CH-06 vertical slice sẵn sàng cho cross-discipline review khi:

1. S01→S02→S03 chơi được với placeholder tế đàn + placeholder bản sao.
2. `B-06` chạy được phase "sao chép" với một bộ đòn test, và phase "đọc lựa chọn" phản ánh ít nhất hai trạng thái `boss_fates` khác nhau.
3. `C-CH06-002` (un-copy) trigger được và mở `C-CH06-003`.
4. Cả **bốn** `final_decision` resolve đúng ending theo Resolution Rules trong hai lượt test riêng.
5. `E-04` chỉ nổ khi đủ `hidden_released=5` + điều kiện lõi; `E-04-PARTIAL` nổ khi thiếu `hidden_released`; `E-03-BITTER` nổ khi thiếu lõi.
6. Ending card + state log ghi đúng một `CH06_ENDING_*` và `final_decision`.
