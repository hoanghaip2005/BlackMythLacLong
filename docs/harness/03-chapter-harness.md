# Chapter Harness: Sáu chương

## Cấu trúc chung mỗi chương

1. **Arrival:** người chơi thấy vết thương của vùng đất.
2. **Pressure:** một lực lượng ép Long Nhân chọn tốc độ hoặc sự thật.
3. **Investigation:** mở một phần bond và truth flag.
4. **Escalation:** boss hoặc phe phái bóp méo vấn đề.
5. **Confrontation:** chiến đấu có mục tiêu cảm xúc, không chỉ giảm HP.
6. **Aftermath:** Long Ngọc, hậu quả nhánh và hướng sang chương kế.

## CH-01: Trầm Thủy Ngư Tinh

- Vùng: Vực Biển Đông.
- Câu hỏi: Long Nhân là ai nếu không có ký ức?
- Mảnh: `LG-01`.
- Boss: Ngư Tinh.
- Biểu hiện yêu khí: áp lực nước, biến dạng, bản năng săn mồi.
- Gameplay hook: nước dâng, xoáy hút, bờ chiến đấu thay đổi.
- Narrative gate: người chơi chọn cưỡng đoạt nguyên thần hoặc trả lại lời hứa bảo hộ cho Thủy tộc.
- Reveal: câu chuyện “phong ấn bị phá” chỉ là một ký hiệu bị đọc sai.
- Aftermath: thanh đoản kiếm rỉ sét tan vỡ; Rìu Thần Thạch Sơn thức tỉnh.
- Boss ẩn (`HB-01`, ADR-004): **Ma Da — Vong Đáy Vực** ở màn ẩn `CH-01-HIDDEN` (bãi xác thuyền dưới vực). Giải thoát mở `hidden_truth`: lời hứa bảo hộ từng *thất bại* trước cả khi đền chìm; cộng `hidden_released`.

### Beat chính

`CH01-S01` Trứng đá mở mắt -> `CH01-S02` Rạn san hô héo -> `CH01-S03` Đền chìm và tiếng gọi -> `CH01-S04` Thủy tộc tranh cãi -> `CH01-S05` Xoáy vực -> `CH01-BOSS` Ngư Tinh -> `CH01-AFTER` Lời hứa đầu tiên.

Chi tiết triển khai narrative của chương nằm tại `docs/harness/chapter-01/`.

## CH-02: Ảo Ảnh Đầm Cáo

- Vùng: Tây Hồ - Đầm Xác Cáo.
- Câu hỏi: Có thể tin một khuôn mặt khi tên thật đã mất?
- Mảnh: `LG-02`.
- Boss: Hồ Tinh, Cửu Vĩ.
- Biểu hiện yêu khí: lặp ký ức, giả dạng, bóng không hồn.
- Gameplay hook: nhân vật và landmark có thể là ảo ảnh; clue thật cần được đối chiếu.
- Narrative gate: cứu tên thật của người bị biến thành bóng hoặc truy đuổi hình cáo mạnh nhất.
- Reveal: Hồ Tinh từng biến đầm thành nơi trú ẩn cho người chạy loạn; chính sự sợ hãi của họ đã tạo lớp mặt nạ.
- Aftermath: một NPC có thể đi cùng hoặc chỉ xuất hiện qua tiếng hát, tùy `tribal_trust`.
- Boss ẩn (`HB-02`, ADR-004): **Bóng Vô Danh** ở màn ẩn `CH-02-HIDDEN` (hang gương dưới đầm). Giải thoát mở `hidden_truth`: Hồ Tinh từng *giữ tên* cho người chạy loạn; cộng `hidden_released`.

### Beat chính

`CH02-S01` Làng không bóng -> `CH02-S02` Bài hát dưới sương -> `CH02-S03` Ba khuôn mặt của Hồ Tinh -> `CH02-S04` Đạo sĩ bị thao túng -> `CH02-S05` Tên thật trong gương nước -> `CH02-BOSS` Cửu Vĩ hiện hình -> `CH02-AFTER` Người sống gọi lại tên mình.

## CH-03: Huyết Mộc Đoạt Mệnh

- Vùng: Rừng Rậm Phong Châu.
- Câu hỏi: Giải phóng người chết có đồng nghĩa phản bội lời thề của họ?
- Mảnh: `LG-03`.
- Boss: Mộc Tinh.
- Biểu hiện yêu khí: rễ ký sinh, thân cây ăn máu, quân đội hóa xác.
- Gameplay hook: đấu trường rễ chuyển động; phá rễ để mở đường và lộ lõi.
- Narrative gate: giải thoát vong linh hoặc giữ họ chiến đấu để mở đường nhanh hơn.
- Reveal: nhiều chiến binh không bị ép hoàn toàn; họ bám vào lời thề vì sợ lịch sử quên mình.
- Aftermath: `TRUTH_OLD_ARMY_WAS_BOUND`; mở ký ức về chiến tranh giành lãnh thổ.
- Boss ẩn (`HB-03`, ADR-004): **Tướng Quân Vô Đầu** ở màn ẩn `CH-03-HIDDEN` (gò mộ dưới rễ). Giải thoát mở `hidden_truth`: một phần vong binh *tự nguyện* ở lại vì sợ bị lịch sử quên; cộng `hidden_released`.

### Beat chính

`CH03-S01` Cổng Phong Châu bị nuốt -> `CH03-S02` Lính gác không mặt -> `CH03-S03` Nghĩa địa dưới rễ -> `CH03-S04` Lời thề của người chết -> `CH03-S05` Lõi đỏ thức dậy -> `CH03-BOSS` Mộc Tinh -> `CH03-AFTER` Tiếng binh khí im.

## CH-04: Lệ Đá Đỉnh Sương

- Vùng: Núi Thạch Môn.
- Câu hỏi: Công lý bị trì hoãn có biến thành trả thù không?
- Mảnh: `LG-04`.
- Boss: Đại Bàng Tinh.
- Biểu hiện yêu khí: lưu đày, phẫn nộ, đứt gãy trọng lực.
- Gameplay hook: verticality, bệ đá hẹp, đòn bổ nhào, gió đổi hướng.
- Narrative gate: lấy mảnh ngọc bằng cách săn boss hoặc nghe lời kể của bộ tộc bị ruồng bỏ.
- Reveal: Đại Bàng Tinh là vật chứa cho phẫn nộ của những người bị xóa khỏi lịch sử triều đại.
- Aftermath: Long Nhân biết Lạc Long Quân từng rời đi khi con người bắt đầu dùng huyết thống làm lý do cai trị.
- Boss ẩn (`HB-04`, ADR-004): **Tù Trưởng Lệ Đá** ở màn ẩn `CH-04-HIDDEN` (khe đá dựng, rừng bia không tên). Giải thoát mở `hidden_truth`: tên bộ tộc bị xóa *có chủ đích* bởi triều đại "thống nhất"; cộng `hidden_released`.

### Beat chính

`CH04-S01` Đường đá vỡ -> `CH04-S02` Hồn bị bắt trong lông vũ -> `CH04-S03` Bản đồ bộ tộc mất tên -> `CH04-S04` Phán quyết trên vực -> `CH04-BOSS` Đại Bàng Tinh -> `CH04-AFTER` Lệ đá rơi xuống mây.

## CH-05: Song Giao Tế Thủy

- Vùng: Ngã Ba Hạc.
- Câu hỏi: Có thể chấm dứt tranh chấp nếu mọi bên đều tin mình đang tự vệ?
- Mảnh: `LG-05`.
- Boss: Song Giao, sau đó hợp thể thành Hắc Giao Long.
- Biểu hiện yêu khí: lũ lụt, tranh chấp, hợp thể cưỡng ép.
- Gameplay hook: bè gỗ trôi, chiến đấu giữa hai boss, tận dụng va chạm và địa hình nước.
- Narrative gate: kích hai giao đánh nhau để lấy lợi thế, hoặc phá nguồn nước nuôi xung đột.
- Reveal: Hỗn Mang đã làm méo ký ức của cả hai giao để chúng tin rằng mảnh ngọc thuộc về mình.
- Aftermath: năm mảnh đủ để mở đường lên Nghĩa Lĩnh; tất cả truth flag có thể hoàn thành.
- Boss ẩn (`HB-05`, ADR-004): **Giao Mẫu** ở màn ẩn `CH-05-HIDDEN` (miếu chìm ở ngã ba nước). Giải thoát mở `hidden_truth`: có *nạn nhân thứ ba* của cuộc tranh chấp mà cả hai giao đã quên; cộng `hidden_released`.

### Beat chính

`CH05-S01` Làng nổi -> `CH05-S02` Hai tiếng gọi dưới lũ -> `CH05-S03` Bè chiến giữa song giao -> `CH05-S04` Mảnh ngọc lộ diện -> `CH05-BOSS-A` Song Giao -> `CH05-BOSS-B` Hắc Giao Long -> `CH05-AFTER` Nước rút để lộ bậc tế đàn.

## CH-06: Hỗn Mang Tế Đàn

- Vùng: Đỉnh Nghĩa Lĩnh.
- Câu hỏi: Ai có quyền quyết định tương lai của một vùng đất mang quá nhiều ký ức?
- Mảnh: dùng đủ năm mảnh, không có mảnh thứ sáu.
- Boss: Hỗn Mang trong hình dạng Long Nhân.
- Biểu hiện yêu khí: sao chép, phủ nhận, ký ức chồng lấn.
- Gameplay hook: đấu tay đôi thuần túy; boss đọc lại các thói quen chiến đấu và lựa chọn trước đó.
- Narrative gate: bốn quyết định cuối `restore`, `absorb`, `destroy`, `reconcile`.
- Reveal: phong ấn chưa từng vỡ; câu chuyện phong ấn là lớp ngụy trang giúp Hỗn Mang biến nợ lịch sử thành một kẻ thù duy nhất.
- Aftermath: một trong bốn ending theo Resolution Rules.
- Boss ẩn: không có `HB-06`. Full completion (`hidden_released = 5`, ADR-004) mở **lớp hòa giải trọn vẹn** của `E-04`; thiếu nó thì `reconcile` chỉ đạt `E-04-PARTIAL` (xem `02` §7).

### Beat chính

`CH06-S01` Bậc đá không có bóng -> `CH06-S02` Năm ký ức mở đồng thời -> `CH06-S03` Hỗn Mang sao chép Long Nhân -> `CH06-S04` Đấu tay đôi -> `CH06-S05` Quyết định cuối -> `CH06-END` Ending card và hậu cảnh.

## Phân bố reveal

| Reveal | Chương mở mồi | Chương xác nhận |
|---|---|---|
| Long Nhân không phải Lạc Long Quân | CH-01 | CH-04 |
| Phong ấn chưa từng vỡ | CH-01 | CH-06 |
| Mỗi boss có một phần bi kịch | CH-01 | CH-05 |
| Hỗn Mang là oán nghiệp tập thể | CH-02 | CH-06 |
| Long Ngọc là neo ký ức | CH-02 | CH-05 |
| Sức mạnh không quyết định nhân cách | CH-03 | Ending |
