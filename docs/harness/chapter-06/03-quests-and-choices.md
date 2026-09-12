# CH-06 Quests and Choices

## Quest map

| ID | Loại | Tên | Bắt buộc | Tác động |
|---|---|---|---|---|
| `Q-CH06-001` | Main | Quyết định tại Nghĩa Lĩnh | Có | Mở S05 và `final_decision` -> ending |
| `Q-CH06-002` | Exploration | Bậc đá không bóng | Không | Gieo sự bất thường; lore về đỉnh tế đàn |
| `Q-CH06-003` | Recap/Bond | Năm ký ức mở đồng thời | Có để `memory_recovered` được "chốt" | Xác nhận `TRUTH_SEAL_WAS_NEVER_BROKEN` |
| `Q-CH06-004` | Hidden/Bond | Chứng nhân oan khuất | Chỉ mở khi `hidden_released = 5` | Nâng `E-04-PARTIAL` -> `E-04` chuẩn |

## Q-CH06-001: Quyết định tại Nghĩa Lĩnh

### Intent

Đưa Long Nhân từ "người thu thập ngọc" thành "người định nghĩa cứu thế giới". Quest không yêu cầu người chơi hiểu toàn bộ lore trước đó, nhưng đọc lại hành trình của chính họ qua lời Hỗn Mang.

### Giver

Không có giver duy nhất. Quest tự mở khi Long Nhân đặt chân lên bậc đá Nghĩa Lĩnh ở `CH-06-S01`.

### Steps

1. **Lên đỉnh:** đi qua bậc đá không bóng (`CH-06-S01`).
2. **Mở năm ký ức:** đặt/đối chiếu đủ `LG-01..05` (`CH-06-S02`).
3. **Đối diện bản sao:** Hỗn Mang hiện hình dạng Long Nhân (`CH-06-S03`).
4. **Đấu tay đôi:** kết thúc encounter `B-06` (`CH-06-S04`).
5. **Chọn quyết định cuối:** một trong `restore/absorb/destroy/reconcile` (`CH-06-S05`).
6. **Chứng kiến ending:** `CH-06-END`.

### Completion

Quest hoàn thành khi `final_decision` được ghi và `CH06_END_*` được resolve. Không hoàn thành chỉ bằng việc hạ HP Hỗn Mang; boss KHÔNG chết theo nghĩa thường - nó bị dồn tới điểm phải nhường lời cho quyết định cuối.

### Failure/cost

Không có game over narrative. "Cost" là ending nào khả dụng và hậu cảnh nào hiện ra. Người chơi không bị ép vào một đáp án đạo đức đúng.

## Q-CH06-002: Bậc đá không bóng

### Premise

Đỉnh Nghĩa Lĩnh không đổ bóng - một bất thường vật lý báo hiệu nơi ký ức bị gom lại. Trên bậc đá có dấu chân của nhiều người đã lên đây trước, nhưng không có dấu chân rời đi.

### Purpose

Gieo cảm giác "đã có nhiều kẻ lên đây và không trở lại", chuẩn bị cho câu hỏi về quyền quyết định. Không giới thiệu cơ chế mới.

### Reward

- Lore fragment: những dấu chân chồng lấn - gợi ý Hỗn Mang đã "gom" nhiều kẻ mang ngọc trước Long Nhân.
- Không đổi biến số; chỉ mở thoại của Tiếng Vọng ở `CH-06-S03`.

## Q-CH06-003: Năm ký ức mở đồng thời

### Unlock

Tự mở ở `CH-06-S02` khi Long Nhân mang đủ năm mảnh.

### Objective

Không phải puzzle lấy ngọc. Người chơi lần lượt CHỨNG KIẾN năm lớp ký ức (`memory` của mỗi `LG-0X`) hiện lên đồng thời, và nhận ra chúng không phải "mảnh phong ấn bị phá" mà là năm món nợ lịch sử bị cắt khỏi sử sách.

### Completion condition

- Đủ `LG-01..05` trong inventory (đã có từ CH-01..05).
- Người chơi ở lại đủ lâu để xem cả năm ký ức (không bỏ qua).

### Effects

- Set `CH06_TRUTH_SEAL_CONFIRMED` (xác nhận `TRUTH_SEAL_WAS_NEVER_BROKEN` ở mức toàn cục).
- Đây là điểm "chốt" `memory_recovered` - nếu người chơi đã bỏ sót bond ở chương trước, `memory_recovered` KHÔNG tự tăng ở đây; quest chỉ xác nhận những gì đã thu. (Không tặng `memory_recovered` miễn phí.)
- Mở điều kiện fiction cho `E-04` (cần `memory_recovered = 5`).

### Note

Quest này tôn trọng hành trình trước: người chơi đã "thu hồi ký ức đúng cách" ở các chương thì mới đủ `memory_recovered = 5`. CH-06 không sửa chữa hộ.

## Q-CH06-004: Chứng nhân oan khuất (hidden / full completion)

### Unlock

Chỉ mở khi `hidden_released = 5` (đã giải thoát đủ năm Oan Khuất Ẩn `HB-01..HB-05` ở CH-01..05, ADR-004).

### Premise

Năm oan khuất đã được gọi tên và trả sự thật hiện về đỉnh Nghĩa Lĩnh, không phải để chiến đấu mà để LÀM CHỨNG. Họ đứng ở rìa tế đàn khi Long Nhân chọn `reconcile`.

### Objective

Ở `CH-06-FULL`, người chơi (đã chọn `reconcile`) chứng kiến năm chứng nhân xác nhận phần sự thật của cộng đồng họ. Đây là hành động "trả ký ức về đúng chủ" ở quy mô đầy đủ.

### Effects

- Nâng kết quả `reconcile` từ `E-04-PARTIAL` lên `E-04` chuẩn (`CH06_END_RECONCILE_FULL`).
- Không tăng biến số chiến đấu; đây là phần thưởng tri thức/hoàn thành, đúng tinh thần ADR-004.

### Incomplete

Nếu `hidden_released < 5`, quest không mở; `reconcile` chỉ đạt `E-04-PARTIAL` (xem `02-branching §7`).

## Choice registry

> Đánh số theo thứ tự scene: `C-CH06-001` (S03 đối đáp) -> `C-CH06-002` (S04 hành động không sao chép) -> `C-CH06-003` (S05 quyết định cuối).

### `C-CH06-001`: Đối đáp với Hỗn Mang (`CH-06-S03`)

| Lựa chọn | Ý định | State | Feedback |
|---|---|---|---|
| Lắng nghe lập luận của nó | Hiểu kẻ thù trước khi đánh | `CH06_HEARD_CHAOS` | Mở thêm line ký ức; Hỗn Mang "hứng thú" |
| Bác bỏ ngay | Từ chối lý lẽ "cần một kẻ thống trị" | `CH06_DENIED_CHAOS` | Boss vào phase aggressive sớm |
| Im lặng, giữ Thế Ngự | Quan sát, chờ sơ hở | `CH06_OBSERVED_CHAOS` | Mở counterplay phản đòn bản sao |

> Không khóa ending; chỉ đổi cách đọc boss và thoại. Tôn trọng nguyên tắc "không phạt vì chọn chiến đấu".

### `C-CH06-002`: Hành động không thể sao chép (cao trào `CH-06-S04`)

> Hiện thực hóa Canon Lock 8: Hỗn Mang sao chép mọi thứ ĐÃ xảy ra, nhưng KHÔNG sao chép được một lựa chọn CHƯA từng có. Người chơi phải làm một điều Hỗn Mang không dự đoán.

| Lựa chọn | Điều kiện | State | Ý nghĩa |
|---|---|---|---|
| Hạ vũ khí, mở tay không | Luôn khả dụng | `CH06_UNCOPIED_BAREHAND` | Từ chối chơi theo luật "kẻ mạnh thắng" |
| Che chở một chứng nhân/cộng đồng thay vì tự vệ | `tribal_trust >= 3` hoặc có chứng nhân | `CH06_UNCOPIED_SHIELD` | Hành động không tối ưu cho bản thân - đúng điểm yếu Hỗn Mang |
| Chém vào tế đàn, không chém bản sao | Luôn khả dụng | `CH06_UNCOPIED_ALTAR` | Tấn công gốc (nơi gom ký ức) thay vì ngọn (bản sao) |

> Bất kỳ phương án nào cũng "phá gương" và mở `CH-06-S05`. Cách phá ảnh hưởng sắc thái thoại chuyển tiếp và gợi ý ending nào "hợp" với hành trình, nhưng KHÔNG tự khóa `final_decision` - người chơi vẫn tự chọn ở `C-CH06-003`.

### `C-CH06-003`: Quyết định cuối tại tế đàn (`final_decision`, `CH-06-S05`)

> Đây là lựa chọn trung tâm. Bốn phương án KHÁC nhau về ý định và hậu quả, không phải "bốn nút tốt/xấu". Mỗi phương án đều có giá phải trả.

| Lựa chọn | Ý định | Người chơi biết | State | Hậu quả gần | Hậu quả xa (ending) |
|---|---|---|---|---|---|
| `restore` | Khôi phục trật tự cũ, gánh vai người canh giữ | Long Ngọc có thể khôi phục mạng lưới Long Khí | `final_decision = restore` | Tế đàn sáng lại; Hỗn Mang bị dồn nén | `E-01 LONG_VUONG`, hoặc `E-02` nếu `dragon_hunger >= 4` |
| `absorb` | Gom tất cả về một mối, kể cả Hỗn Mang | Hấp thụ sẽ chấm dứt yêu khí nhưng tập trung quyền lực | `final_decision = absorb` | Long Nhân hóa rồng; Hỗn Mang cười | `E-02 TAN_HON_MANG` |
| `destroy` | Chấm dứt vòng lặp bằng cách phá nguồn sức mạnh | Phá ngọc sẽ mất luôn Long Khí và phép màu | `final_decision = destroy` | Năm ngọc vỡ; Long Khí tắt | `E-03 DOAN_TUYET_LONG_MACH` |
| `reconcile` | Trả ký ức về cho các cộng đồng, không giữ quyền cai trị | Cần đủ ký ức, mercy, trust và chứng nhân | `final_decision = reconcile` | Tế đàn thành nơi hòa giải | `E-04` (nếu đủ điều kiện), nếu thiếu `hidden_released=5` -> `E-04-PARTIAL`, thiếu điều kiện lõi -> `E-03-BITTER` |

## Choice design rules for CH-06

- Không hiển thị nhãn "Good ending / Bad ending". Cả bốn ending đều có giá phải trả và đều đặt một câu hỏi.
- `reconcile` không phải "phần thưởng cho người tử tế" - nó là kết quả của cả một hành trình có chủ ý (đủ ký ức, mercy, trust, và chứng nhân oan khuất).
- `restore` và `absorb` có thể dẫn tới cùng `E-02` nếu `dragon_hunger` cao - cho thấy ý định tốt có thể bị quyền lực bẻ cong.
- Hành động "không thể sao chép" (`C-CH06-002`) là cơ chế fiction của Canon Lock 8, không phải một QTE; nó phải đọc được như một lựa chọn đạo đức.
- Mọi choice đều đổi ít nhất một cờ/biến và có tín hiệu phản hồi (thoại, hình ảnh, ending card) - tôn trọng `02-branching §8` (chống nhánh giả).
