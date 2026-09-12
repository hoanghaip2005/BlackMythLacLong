# CH-06 Scene Flow

## Flow tổng

`S01 Bậc đá không có bóng`
`-> S02 Năm ký ức mở đồng thời`
`-> S03 Hỗn Mang sao chép Long Nhân`
`-> S04/B06 Đấu tay đôi`
`-> [FULL] CH-06-FULL Chứng nhân oan khuất (chỉ khi hidden_released = 5)`
`-> S05 Quyết định cuối (final_decision)`
`-> END Ending card + hậu cảnh`

> `S04` là encounter `B-06`, mô tả chi tiết ở `05-boss-encounter.md`. `CH-06-FULL` là lớp tùy chọn đặt giữa duel và quyết định; nó không đổi `final_decision`, chỉ nâng `E-04-PARTIAL` lên `E-04` chuẩn khi đủ điều kiện.

## CH-06-S01: Bậc đá không có bóng

### Purpose

Đặt Long Nhân lên đỉnh Nghĩa Lĩnh, tách khỏi mọi đồng minh, và gieo cảm giác "nơi này không phản chiếu ai". Thiết lập sự im lặng trước bão.

### Entry

- Người chơi mang đủ năm mảnh `LG-01..LG-05` (điều kiện mở tế đàn).
- Toàn bộ biến tích lũy (`memory_recovered`, `mercy_marks`, `tribal_trust`, `dragon_hunger`, `relics_purified`, `hidden_released`, `truth_flags`, `boss_fates`) được GIỮ NGUYÊN, không reset.
- Rìu Thần Thạch Sơn đã thức tỉnh (từ CH-01).

### Beats

1. Bậc đá dẫn lên tế đàn; không vật nào đổ bóng, kể cả Long Nhân - tế đàn "không ghi nhận" ai là trung tâm.
2. Năm bệ đá xếp thành vòng, mỗi bệ khắc ký hiệu một vùng (biển, đầm, rừng, núi, ngã ba nước).
3. Tiếng Vọng Lạc Long vang lần cuối, chỉ hỏi, không dẫn: "Con đến để giữ, để ăn, để phá, hay để trả lại?"
4. Nếu `tribal_trust >= 4`, thấp thoáng bóng những cộng đồng đã tin Long Nhân đứng xa dưới chân bậc (không can thiệp).

### Exit

Long Nhân đứng giữa vòng năm bệ. Người chơi hiểu: đây là nơi quyết định, và không ai quyết định thay.

### Choice

Không có choice chính. Khám phá tùy chọn: đặt từng mảnh ngọc lên bệ tương ứng để mở lore fragment (không đổi state), hoặc đi thẳng vào giữa vòng.

## CH-06-S02: Năm ký ức mở đồng thời

### Purpose

XÁC NHẬN reveal trung tâm: phong ấn chưa từng vỡ. Năm mảnh ngọc chiếu lại năm ký ức bị cắt khỏi lịch sử, và người chơi thấy chúng không phải "mảnh phong ấn" mà là "neo ký ức".

### Beats

1. Năm bệ sáng khi Long Nhân bước vào giữa; năm quầng ký ức nổi lên đồng thời (biển bỏ rơi, đầm mất tên, rừng trói lời thề, núi xóa bộ tộc, ngã ba nước tranh giành).
2. Các ký ức KHÔNG rời rạc - chúng nối thành một mẫu: nhiều cuộc chiến tranh giành lãnh thổ, mỗi cuộc để lại một lớp oán.
3. Reveal: không có "phong ấn cổ đại bị phá". Câu chuyện phong ấn là lớp ngụy trang để gom nợ lịch sử tản mạn thành MỘT kẻ thù. `TRUTH_SEAL_WAS_NEVER_BROKEN` chuyển từ clue thành xác nhận.
4. Nếu thiếu một `truth_flag` (người chơi bỏ sót bond), quầng ký ức tương ứng bị MẤT TIẾNG/mờ - người chơi thấy rõ cái giá của việc bỏ qua (`memory_recovered` phản ánh số lớp đã mở đúng).

### Exit

Long Nhân (và người chơi) hiểu bản chất thật của kẻ thù sắp đối diện: nó là tổng oán nghiệp, không phải một con quái.

### Choice

Không có choice khóa state. Đây là cảnh "lĩnh hội"; tốc độ/ngắn dài tùy lượng truth người chơi đã gom.

## CH-06-S03: Hỗn Mang sao chép Long Nhân

### Purpose

Giới thiệu `B-06` không như quái vật mà như tấm gương. Hỗn Mang dựng hình từ chính ký ức và dáng dấp Long Nhân, đưa ra lập luận tư tưởng của nó.

### Situation

Giữa vòng năm bệ, yêu khí tụ lại thành một hình người - giống Long Nhân, nhưng các đường nét chồng lấn nhiều khuôn mặt từng bị lịch sử bỏ quên. Nó nói bằng giọng Long Nhân pha giọng nhiều người.

### Key reveal

- Hỗn Mang tin thật lòng: "Mọi trật tự đều cần một kẻ thống trị; hòa giải chỉ là trì hoãn xung đột."
- Nó không sao chép được một lựa chọn Long Nhân CHƯA thực hiện (Canon Lock 8) - nó chỉ lặp lại những gì đã xảy ra.
- Nó mời Long Nhân "chấm dứt vòng lặp bằng cách trở thành kẻ duy nhất quyết định".

### Choice: `C-CH06-001`

**Phủ nhận:** "Ta không phải ngươi."

- Hỗn Mang đáp bằng cách liệt kê chính xác những lần Long Nhân đã đoạt/giết (`dragon_hunger`, các `boss_fates=absorbed/defeated_by_force`) - "ngươi đã là ta nhiều lần".
- Mở đường duel thiên về đối đầu trực diện.

**Chất vấn:** "Ngươi muốn gì?"

- Mở thêm một lớp ký ức về nguồn gốc Hỗn Mang (nó là ai trước khi thành oán).
- Không khóa ending; cho người chơi thêm thông tin để quyết định ở S05.

**Im lặng, giữ Thế Ngự:**

- Hỗn Mang không đọc được "lựa chọn chưa thực hiện" từ sự im lặng; nó khựng một nhịp.
- Dạy trước cơ chế phá mirror sẽ dùng ở `C-CH06-002`.

## CH-06-S04 / B-06: Đấu tay đôi

Encounter mô tả chi tiết ở `05-boss-encounter.md`.

### Player objective

Không "giảm HP boss". Người chơi phải nhận ra Hỗn Mang chỉ sao chép được những gì ĐÃ xảy ra, và thắng bằng một lựa chọn/hành động CHƯA từng thực hiện - thứ nó không đoán được.

### Exit

Hỗn Mang bị "vỡ mirror" (không chết theo nghĩa thường). Yêu khí tản ra, để lộ lõi oán nghiệp không hình hài. Tế đàn mở trạng thái chờ `final_decision`.

## CH-06-FULL: Chứng nhân oan khuất (tùy chọn, R-09/ADR-004)

### Unlock

Chỉ hiện diện khi `hidden_released = 5` (đã giải thoát cả năm Oan Khuất Ẩn HB-01..05).

### Purpose

Thưởng cho "làm full": năm oan khuất đã hóa giải hiện về làm CHỨNG NHÂN cho nghi lễ, biến hòa giải từ "một phần" thành "trọn vẹn".

### Beats

1. Năm bóng đã được Long Nhân trả lại danh tính (Ma Da, Bóng Vô Danh, Tướng Quân Vô Đầu, Tù Trưởng Lệ Đá, Giao Mẫu) hiện quanh tế đàn - không phải để chiến đấu, mà để LÀM CHỨNG.
2. Mỗi chứng nhân xác nhận một phần sự thật mà cộng đồng của họ từng bị cướp mất.
3. Sự hiện diện của họ là điều kiện fiction cho `E-04` chuẩn: hòa giải cần người bị hại có mặt để nhận lại ký ức, không thể làm thay họ.

### Exit

Nếu `final_decision = reconcile` và đủ điều kiện lõi: có chứng nhân => `E-04` chuẩn; không có (`hidden_released < 5`) => `E-04-PARTIAL`.

## CH-06-S05: Quyết định cuối

### Purpose

Điểm hội tụ của toàn bộ hệ nhánh. Người chơi chọn `final_decision`; hệ thống resolve ending theo `02 §7`.

### Staging

Lõi oán nghiệp của Hỗn Mang lơ lửng giữa năm bệ. Rìu Thần Thạch Sơn và năm mảnh ngọc đều "sẵn sàng". Tiếng Vọng Lạc Long không khuyên; chỉ chứng kiến. Bốn ý định hiện ra như bốn cách đặt tay lên tế đàn - không nhãn "đúng/sai".

### Choice: `C-CH06-003` (final_decision)

> Mỗi lựa chọn cần đủ năm trường (ý định / thông tin / hậu quả gần / hậu quả xa / tín hiệu phản hồi) - chi tiết ở `03-quests-and-choices.md`.

- **`restore`:** khôi phục mạng lưới Long Khí, Long Nhân làm người canh giữ. -> `E-01` (hoặc `E-02` nếu `dragon_hunger>=4`).
- **`absorb`:** hấp thụ Hỗn Mang vào bản thân. -> `E-02`.
- **`destroy`:** phá năm ngọc, chặt đứt huyết mạch siêu nhiên. -> `E-03`.
- **`reconcile`:** trả ký ức về cho các cộng đồng. -> `E-04` (chuẩn nếu `hidden_released=5`; `E-04-PARTIAL` nếu thiếu; `E-03-BITTER` nếu thiếu điều kiện lõi).

### Exit

`final_decision` được set đúng một lần. Cảnh chuyển sang ending tương ứng.

## CH-06-END: Ending card và hậu cảnh

### Purpose

Đóng game bằng hình ảnh và hậu cảnh đúng với ending đã resolve; không xóa hậu quả lựa chọn trước, chỉ định nghĩa chúng.

### Variants (một card + một hậu cảnh cho mỗi ending)

- **`E-01 LONG_VUONG`:** Long Nhân trên ngai người canh giữ; đất yên nhưng cô độc; nếu `relics_purified<3`, một vết nứt nhỏ còn nhấp nháy (hook phần tiếp).
- **`E-02 TAN_HON_MANG`:** Long Nhân hóa trung tâm trật tự mới; đẹp, lạnh; bóng Hỗn Mang vẫn còn trong mắt người chơi.
- **`E-03 DOAN_TUYET_LONG_MACH`:** ngọc vỡ, Long Khí tắt; thế giới phàm trần, tự do và bất định; Long Nhân là một con người vô danh.
- **`E-03-BITTER`:** như E-03 nhưng các cộng đồng CHƯA kịp thấy sự thật - ngọc vỡ trong im lặng oán hận; nặng nề hơn.
- **`E-04 HOA_GIAI_BACH_TOC`:** tế đàn thành nơi trăm họ nhận lại ký ức; năm chứng nhân oan khuất đứng giữa cộng đồng của họ; ngọc thành vật chứng, không thành vương miện; ấm, viên mãn, thiêng.
- **`E-04-PARTIAL`:** như E-04 nhưng vắng một vài chứng nhân (oan khuất chưa giải thoát); hòa giải còn một chỗ trống chưa lành.

### Chapter close

Camera rời tế đàn. Tùy ending, máy quay kết ở ngai / ở đôi mắt rồng / ở bàn tay không ngọc / ở vòng tròn trăm họ. Cắt khi người chơi đã hiểu cái giá của lựa chọn mình.
