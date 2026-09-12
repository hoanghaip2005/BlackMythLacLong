# Branching Harness: Lựa chọn và Kết thúc

## 1. Mục tiêu thiết kế

Nhánh truyện không tách thành sáu đường độc lập. Sáu chương vẫn giữ thứ tự chính, còn lựa chọn thay đổi:

- cách boss được nhìn nhận và kết thúc;
- NPC nào còn sống, tin tưởng hoặc đối đầu;
- lượng ký ức Long Nhân thu hồi;
- mức Hỗn Mang bám vào Long Khí;
- hình ảnh và luật chiến đấu của trận cuối;
- kết thúc tại Đỉnh Nghĩa Lĩnh.

## 2. Biến số runtime narrative

Các giá trị dùng trong tài liệu, chưa phải code runtime.

| ID | Miền | Khởi tạo | Ý nghĩa |
|---|---:|---:|---|
| `memory_recovered` | 0..5 | 0 | Số lớp ký ức đã mở đúng cách |
| `mercy_marks` | 0..8 | 0 | Số lần giải thoát hoặc tha mạng có chủ đích |
| `tribal_trust` | 0..6 | 0 | Mức tin tưởng tổng hợp của các cộng đồng |
| `dragon_hunger` | 0..8 | 0 | Mức Long Nhân dùng quyền lực để chiếm đoạt |
| `relics_purified` | 0..5 | 0 | Số Long Ngọc được thanh tẩy thay vì cưỡng đoạt |
| `truth_flags` | set | rỗng | Các sự thật đã xác nhận |
| `boss_fates` | map | rỗng | Kết cục riêng của từng boss |
| `final_decision` | enum | null | Quyết định tại tế đàn |

### Quy tắc tăng giảm

- Cứu hoặc giải thoát một cộng đồng: `tribal_trust +1`.
- Hoàn thành bond của một Long Ngọc: `relics_purified +1`, `memory_recovered +1`.
- Cưỡng đoạt nguyên thần: `dragon_hunger +1`.
- Thu hồi nguyên thần sau khi giải thoát boss: `mercy_marks +1`.
- Hạ boss không tìm hiểu nguyên nhân: không cộng `memory_recovered`, có thể giảm `tribal_trust`.
- Lựa chọn vì lợi ích ngắn hạn nhưng gây hại cho cộng đồng: `dragon_hunger +1`.
- Không phạt người chơi chỉ vì chọn chiến đấu; phạt vì bỏ qua chủ ý và hậu quả đã được cho thấy.
- Mọi biến số phải clamp trong miền đã khai báo; không âm thầm wrap hoặc reset giữa các chương.

## 3. Bond của năm Long Ngọc

| Mảnh | Boss giữ | Bond cần giải quyết | Truth flag |
|---|---|---|---|
| `LG-01` | Ngư Tinh | Đối diện lời hứa bảo hộ bị bỏ mặc của Thủy tộc | `truth_seal_was_never_broken` |
| `LG-02` | Hồ Tinh | Trả lại tên thật cho người bị biến thành bóng | `truth_fox_was_a_refuge` |
| `LG-03` | Mộc Tinh | Giải thoát vong linh khỏi lời thề chiến tranh | `truth_old_army_was_bound` |
| `LG-04` | Đại Bàng Tinh | Gọi tên tội lỗi của các bộ tộc bị ruồng bỏ | `truth_exile_was_erased` |
| `LG-05` | Song Giao | Chấm dứt vòng tranh giành quyền kiểm soát dòng nước | `truth_conflict_was_fed` |

## 4. Lựa chọn cấp scene

Mỗi lựa chọn quan trọng cần ghi đủ năm trường:

1. **Ý định:** người chơi đang chấp nhận, từ chối, hy sinh hay điều tra điều gì?
2. **Thông tin:** người chơi biết gì trước khi chọn?
3. **Hậu quả gần:** thay đổi trong scene tiếp theo.
4. **Hậu quả xa:** thay đổi trong chương sau hoặc ending.
5. **Tín hiệu phản hồi:** game cho người chơi thấy hậu quả bằng thoại, hình ảnh, NPC, combat hoặc reward nào?

## 5. Boss fate enum

Mỗi boss có một trong các trạng thái sau:

- `defeated_by_force`: thắng bằng sức mạnh, chưa giải quyết bond.
- `released`: giải thoát nguyên nhân oán nghiệp trước hoặc trong trận.
- `absorbed`: Long Nhân cưỡng đoạt nguyên thần.
- `sacrificed`: boss hoặc NPC tự hy sinh để phá vòng lặp.
- `escaped`: boss rút lui; dùng cho nhánh mở rộng, không phải kết thúc chương.

## 6. Quyết định cuối

Tại Đỉnh Nghĩa Lĩnh, Long Nhân chọn một trong bốn hành động:

- `restore`: dùng Long Ngọc khôi phục mạng lưới Long Khí.
- `absorb`: hấp thụ toàn bộ Hỗn Mang vào bản thân.
- `destroy`: phá năm mảnh Long Ngọc và chấm dứt huyết mạch siêu nhiên.
- `reconcile`: trả ký ức về cho các cộng đồng, biến tế đàn thành nơi hòa giải.

## 7. Resolution Rules

Kiểm tra theo thứ tự, từ trên xuống. Chỉ chọn một ending.

### Ending E-04: Hòa Giải Bách Tộc, kết thúc thật

Điều kiện:

- `final_decision = reconcile`.
- `memory_recovered = 5`.
- `mercy_marks >= 4`.
- `tribal_trust >= 5`.
- Có đủ năm `truth_flags`.
- Không có quá hai boss ở trạng thái `absorbed`.

Kết quả: Hỗn Mang không bị đánh bại bằng quyền lực. Các cộng đồng nhìn thấy phần lịch sử của mình, Long Ngọc mất chức năng cai trị và trở thành vật chứng sống.

### Ending E-02: Tân Hỗn Mang

Điều kiện:

- `final_decision = absorb`, hoặc
- `dragon_hunger >= 4` và Long Nhân chọn `restore`.

Kết quả: Văn Lang được cứu khỏi yêu khí bên ngoài nhưng Long Nhân trở thành trung tâm của một trật tự mới, đẹp hơn về hình thức và nguy hiểm hơn về bản chất.

### Ending E-03: Đoạn Tuyệt Long Mạch

Điều kiện:

- `final_decision = destroy`.

Kết quả: Long Ngọc vỡ, Hỗn Mang mất nguồn khuếch đại, Long Nhân mất Long Khí. Các thế lực phải sống bằng năng lực của chính mình. Đây là kết thúc giải phóng nhưng không bảo đảm hòa bình.

### Ending E-01: Long Vương

Điều kiện:

- `final_decision = restore`.
- Không thỏa điều kiện E-02.
- Nếu `relics_purified >= 3`, Long Nhân khôi phục mạng lưới với tổn thất thấp hơn.
- Nếu `relics_purified < 3`, mạng lưới được khôi phục không ổn định và hậu cảnh để lại dấu hiệu cho phần tiếp theo.

Kết quả: Long Nhân trở thành người canh giữ Long Mạch. Đây là kết thúc chiến thắng truyền thống, nhưng vẫn đặt câu hỏi về việc một người có nên nắm quyền bảo hộ toàn cõi.

### Fallback khi chọn `reconcile` nhưng thiếu điều kiện

Nếu chọn `reconcile` nhưng thiếu bất kỳ điều kiện E-04 nào, nghi lễ thất bại một phần. Hệ thống chuyển sang `destroy` ở mức bi kịch: Long Ngọc vỡ, nhưng các cộng đồng chưa kịp nhìn thấy sự thật. Gắn tag `E-03-BITTER` để khác với E-03 chuẩn.

## 8. Nguyên tắc chống nhánh giả

- Không gọi một lựa chọn là “quan trọng” nếu không thay đổi ít nhất một biến, cờ, scene, reward hoặc lời thoại hậu quả.
- Không giấu toàn bộ điều kiện ending; người chơi cần nhận biết các giá trị đang được xây dựng qua fiction.
- Không dùng đạo đức nhị nguyên “tốt/xấu”. Một lựa chọn có thể vừa cứu cộng đồng vừa làm tăng nguy cơ tập trung quyền lực.
- Mỗi chương phải có ít nhất một hậu quả xuất hiện trước khi chương sau kết thúc.
