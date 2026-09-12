# CH-06 Cast and Factions

## Long Nhân

- ID: `PLAYER-LONG-NHAN`
- Chapter function: người mang đủ năm ký ức và là người duy nhất có thể đưa ra lựa chọn mà Hỗn Mang không sao chép được.
- Starting desire (CH-06): chấm dứt vòng lặp, hiểu mình là ai ngoài huyết thống.
- Chapter need: tự chịu trách nhiệm cho định nghĩa "cứu thế giới" - không giao quyền đó cho sức mạnh hay cho một kẻ thống trị.
- Voice rule: câu ngắn, đã bớt dò dẫm hơn CH-01 nhưng KHÔNG toàn tri; ở S05 gần như không nói - hành động là lời thoại.
- Trạng thái phản ánh hành trình: `boss_fates`, `dragon_hunger`, `mercy_marks`, `tribal_trust`, `hidden_released` quyết định Hỗn Mang "đọc" Long Nhân thế nào và ending nào khả dụng về mặt cảm xúc.
- Forbidden: không cho Long Nhân một câu trả lời "đúng" được canon xác nhận; không biến nhân vật thành đấng cứu thế vô tội.

## Hỗn Mang

- ID: `B-06`
- Faction: không phải phe; là tổng oán nghiệp có tính chủ động của nhiều cuộc chiến tranh giành lãnh thổ.
- Hình thái chiến đấu: SAO CHÉP hình dáng và kỹ thuật Long Nhân (`B06-P1-MIRROR`), rồi chồng lấn ký ức/nhiều khuôn mặt (`B06-P2-CHOIR`). Không có hình hài gốc cố định; lõi là một khoảng tối không gương mặt.
- Bề mặt: nói bằng giọng Long Nhân pha giọng nhiều người; lập luận mạch lạc, thuyết phục, TIN rằng mình đúng.
- Vết thương: nó là phần dư của vô số kẻ bị lịch sử làm câm lặng; không ai từng "nghe" nó, chỉ "dập" nó.
- Mong muốn: chứng minh mọi trật tự đều cần một kẻ thống trị; kết thúc xung đột bằng cách gom tất cả về một ý chí.
- Điểm yếu (Canon Lock 8): sao chép được thứ ĐÃ xảy ra, KHÔNG sao chép được lựa chọn CHƯA thực hiện; không hiểu hành động không tối ưu cho bản thân nhưng bảo vệ người khác.
- Mâu thuẫn: nó nhân danh những kẻ bị quên lãng, nhưng phương pháp của nó (gom về một kẻ thống trị) lại tiếp tục làm câm lặng chính họ.
- Cấm viết: không biến Hỗn Mang thành "ác quỷ vô nguồn gốc" hay "quỷ vương" sáo rỗng; không cho nó bị thuyết phục chỉ bằng một câu thoại - nó chỉ "vỡ" khi người chơi HÀNH ĐỘNG khác điều nó dự đoán.

## Tiếng Vọng Lạc Long

- ID: `ECHO-LAC-LONG-06`
- Faction: ký ức biểu tượng của thủy tổ.
- Xuất hiện: phản chiếu trên mặt bệ đá/ngọc/lưỡi rìu; không cơ thể.
- Chức năng: đặt câu hỏi cuối ("giữ, ăn, phá, hay trả lại?"), chứng kiến, KHÔNG phán quyết và KHÔNG chọn thay.
- Giọng: ít lời, hình ảnh, có khoảng trống.
- Cấm viết: không xuất hiện như Lạc Long Quân bằng xương bằng thịt; không trực tiếp giải quyết Hỗn Mang hay ban ending.

## Các cộng đồng (chứng nhân tùy trust)

Đại diện ký ức của năm vùng, hiện ở S01/S02/S05 tùy `tribal_trust` và `boss_fates`:

- **Thủy tộc Biển Đông** (có thể gồm `NPC-CH01-LINH` nếu đã cứu): mang ký ức "lời hứa bảo hộ bị bỏ mặc".
- **Dân đầm Tây Hồ:** mang ký ức "mất tên"; nghi ngờ mọi hình hài giống người - kể cả Long Nhân.
- **Vong linh Lạc Việt:** chia rẽ - một số muốn được giải thoát, một số muốn giữ lời thề.
- **Các bộ tộc bị ruồng bỏ:** mang bằng chứng về những cuộc chiến "thống nhất" từng là chiến tranh xóa tên.
- **Song Giao / dư âm Ngã Ba Hạc:** mang ký ức "tranh chấp được nuôi bởi bên thứ ba vô hình".

Phản hồi lựa chọn:

- `tribal_trust >= 5`: các cộng đồng hiện diện đầy đủ ở S05, là nền fiction cho `reconcile` thành công.
- `tribal_trust` thấp: tế đàn vắng; `reconcile` khó đạt `E-04` (thiếu người nhận lại ký ức).
- Nhiều `boss_fates = absorbed`: một vài cộng đồng rút lui, không chứng nhận Long Nhân.

## Năm Oan Khuất Ẩn (chứng nhân full completion)

- IDs: `HB-01..HB-05` (Ma Da, Bóng Vô Danh, Tướng Quân Vô Đầu, Tù Trưởng Lệ Đá, Giao Mẫu).
- Điều kiện hiện diện: `hidden_released = 5`.
- Chức năng CH-06: KHÔNG chiến đấu; hiện về làm CHỨNG NHÂN ở `CH-06-FULL`, xác nhận phần sự thật mà cộng đồng họ từng bị cướp. Là điều kiện fiction nâng `E-04-PARTIAL` -> `E-04` chuẩn.
- Cấm viết: không biến họ thành "phần thưởng sức mạnh"; họ là bằng chứng sống rằng hòa giải cần người bị hại có mặt.

## Yêu tộc phụ

Không xuất hiện như trash mob ở CH-06. Đỉnh Nghĩa Lĩnh "không đổ bóng" - không có sinh vật vô danh nào; mọi thứ trên đỉnh đều là ký ức hoặc là lựa chọn.
