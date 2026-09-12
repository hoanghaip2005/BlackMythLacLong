# CH-06 Dialogue Script

## Voice rules

- **Long Nhân:** ở chương cuối, đã có "tiếng nói" riêng - câu ngắn, chắc, không còn hỏi trống không; nhưng vẫn không tự xưng anh hùng. Khi đối diện Hỗn Mang, Long Nhân nói như nói với chính phần tối của mình.
- **Hỗn Mang (`B-06`):** nói bằng **giọng của chính Long Nhân**, chồng lấn **nhiều giọng khác** (những kẻ nó đã gom). Không gào; nó *thuyết phục*, nó TIN nó đúng. Câu giàu logic lạnh, đôi khi trích lại đúng lời Long Nhân đã nói ở chương trước.
- **Tiếng Vọng Lạc Long:** chỉ hỏi, không phán quyết, không cứu. Câu ngắn, nhiều khoảng trống. Ở CH-06 đặt câu hỏi về quyền quyết định.
- **Năm cộng đồng / chứng nhân:** mỗi người một câu ngắn, cụ thể, không đại diện tuyệt đối; họ nói phần sự thật của họ.
- **Kết thúc:** giọng trang trọng, mỗi ending một tông (E-01 lạnh trang nghiêm, E-02 quyến rũ nguy hiểm, E-03 trống lặng, E-04 ấm nhiều tiếng nói).

## CH-06-S01: bậc đá không bóng

### `D-CH06-S01-01`

**[Bậc đá dài. Không có bóng đổ, dù trời có nguồn sáng. Những dấu chân chồng lấn, không dấu chân rời.]**

**Tiếng Vọng Lạc Long:** "Nhiều kẻ đã lên đây."

**Long Nhân:** "Họ đâu?"

**Tiếng Vọng Lạc Long:** "Con đang giẫm lên câu trả lời."

Ghi chú: Không giải thích. Để người chơi tự thấy dấu chân không có đường về.

## CH-06-S02: năm ký ức mở đồng thời

### `D-CH06-S02-01`

**[Năm mảnh Long Ngọc nâng lên. Năm lớp ký ức hiện đồng thời: biển, đầm, rừng, núi, ngã ba nước.]**

**Tiếng Vọng Lạc Long:** "Nhìn kỹ. Có mảnh phong ấn nào bị phá không?"

**Long Nhân:** "Không. Chưa từng có phong ấn."

**Tiếng Vọng Lạc Long:** "Vậy ai đã kể cho con câu chuyện phong ấn?"

### `D-CH06-S02-02` (reveal)

**Hỗn Mang (vọng, chưa hiện hình):** "Ta kể. Vì nợ của trăm cuộc chiến khó mang quá. Nên ta gom lại, đặt cho một cái tên, và bảo các ngươi: có một kẻ thù duy nhất."

**Hỗn Mang:** "Các ngươi luôn muốn một kẻ để đổ lỗi. Ta chỉ đưa cho các ngươi đúng thứ các ngươi xin."

Ghi chú: Đây là xác nhận toàn cục của `TRUTH_SEAL_WAS_NEVER_BROKEN`. Set `CH06_TRUTH_SEAL_CONFIRMED`.

## CH-06-S03: Hỗn Mang sao chép Long Nhân

### `D-CH06-S03-01`

**[Yêu khí tụ lại thành một hình người. Nó là Long Nhân - nhưng mắt trống, và bóng của nó chồng nhiều bóng khác.]**

**Hỗn Mang (giọng Long Nhân):** "Ta là phần ngươi không chịu nhận. Mỗi nhát chém, mỗi lần ngươi đoạt thay vì tha - ta ở đó."

**Long Nhân:** "Ngươi không phải ta."

**Hỗn Mang:** "Chưa. Nhưng mọi kẻ lên đây đều kết thúc bằng cách cho ta một cái tên. Ngươi cũng sẽ vậy."

### `C-CH06-001` responses

**Lắng nghe (`D-CH06-S03-02-H`):**

**Long Nhân:** "Nói đi. Ta nghe."

**Hỗn Mang:** "Lạ thật. Ít kẻ chịu nghe. Vậy nghe này: trật tự nào cũng cần một kẻ cầm đầu. Hòa giải chỉ là chiến tranh nghỉ lấy hơi."

**Bác bỏ (`D-CH06-S03-02-D`):**

**Long Nhân:** "Ngụy biện. Ngươi cần kẻ thống trị vì ngươi không tin nổi ai khác."

**Hỗn Mang:** "Ta không tin. Ta *biết*. Lịch sử của các ngươi viết bằng máu kẻ thắng - ta chỉ đọc to nó lên."

**Im lặng / Thế Ngự (`D-CH06-S03-02-S`):**

**[Long Nhân hạ thấp rìu, không tiến.]**

**Hỗn Mang:** "Ngươi lại im lặng. Giống hệt lần đầu tiên ta gặp ngươi dưới đáy biển. Nhưng lần đó ngươi chưa có lý do để im lặng."

Ghi chú: `D-CH06-S03-02-S` callback tới CH-01 (silent/Thế Ngự). Không khẳng định phong ấn đã vỡ ở bất kỳ line nào trước đây.

## CH-06-S04 / B-06: phase transition lines

### `D-CH06-B06-P1-MIRROR`

**Hỗn Mang:** "Ba thế - Trảm, Đột, Ngự. Ta thuộc từ trước khi ngươi kịp nhớ."

**Hỗn Mang:** "Đánh đi. Ta sẽ đánh lại y hệt, để ngươi thấy ngươi tầm thường thế nào."

### `D-CH06-B06-P2-CHOIR`

**Hỗn Mang:** "Ngươi muốn xem lại chính mình không?"

**[Nếu người chơi đã `absorbed` boss trước - Hỗn Mang hiện nguyên thần của boss đó:]** "Ngươi gọi đây là sống sót. Ta gọi đây là ăn thịt đồng loại."

**[Nếu người chơi đã `released` nhiều - Hỗn Mang chế giễu:]** "Ngươi tha thứ nhiều đến vậy. Thế mà ngươi vẫn cầm rìu tới đây."

### `D-CH06-B06-UNCOPIED` (cao trào `C-CH06-002`)

**[Long Nhân làm điều Hỗn Mang chưa từng thấy - hạ vũ khí / che cho người khác / chém vào tế đàn.]**

**Hỗn Mang:** "...Cái đó ta chưa học được."

**Hỗn Mang:** "Ngươi lấy đâu ra một hành động chưa từng có? Ngươi cũng chỉ là..."

**Tiếng Vọng Lạc Long:** "Nó là lựa chọn. Con chưa bao giờ sao chép được lựa chọn, phải không?"

Ghi chú: Hiện thực hóa Canon Lock 8 bằng thoại. Hỗn Mang KHÔNG bị giết; nó bị dồn tới điểm nhường lời cho quyết định cuối.

## CH-06-S05: bốn quyết định (`C-CH06-003`)

### `restore` (`D-CH06-S05-01-RES`)

**Long Nhân:** "Ta sẽ giữ. Không phải vì ta xứng - vì chưa ai chịu giữ mà không đòi cai trị."

**Hỗn Mang:** "Rồi ngươi sẽ mệt. Rồi ngươi sẽ giống ta."

### `absorb` (`D-CH06-S05-01-ABS`)

**Long Nhân:** "Ta gom tất cả về ta. Kể cả ngươi."

**Hỗn Mang (cười):** "Cuối cùng. Ngươi hiểu rồi đấy."

### `destroy` (`D-CH06-S05-01-DES`)

**Long Nhân:** "Không ai nên giữ thứ này. Kể cả ta."

**[Long Nhân nâng rìu lên năm mảnh ngọc.]**

**Hỗn Mang:** "Ngươi sẽ xóa cả ta lẫn chính ngươi. Ngươi gọi đó là công bằng?"

### `reconcile` (`D-CH06-S05-01-REC`)

**Long Nhân:** "Ký ức không thuộc về ta. Nó thuộc về những người đã bị lấy mất nó."

**Hỗn Mang:** "Trả lại? Rồi họ sẽ lại đánh nhau vì nó."

**Long Nhân:** "Có thể. Nhưng lần này là họ tự quyết - không phải ta, và không phải ngươi."

### `CH-06-FULL` variant (`D-CH06-S05-02-FULL`, chỉ khi `hidden_released = 5`)

**[Năm chứng nhân oan khuất hiện về: vong đáy biển, bóng vô danh, tướng không đầu, tù trưởng lệ đá, giao mẫu.]**

**Vong Đáy Biển:** "Biển đã nghe tên mình."

**Giao Mẫu:** "Hai con ta không còn phải chọn bên."

**Tiếng Vọng Lạc Long:** "Đủ năm tiếng nói bị lãng quên. Bây giờ tế đàn không cần một người giữ nữa."

Ghi chú: Chỉ hiện khi full completion (ADR-004). Nâng `reconcile` từ `E-04-PARTIAL` lên `E-04` chuẩn.

## CH-06-END: ending card lines

### `E-01 LONG_VUONG`

**Dòng kết:** "Một người canh giữ Long Mạch. Trật tự trở lại - và câu hỏi cũ vẫn còn đó: một người có nên giữ cả cõi không?"

### `E-02 TAN_HON_MANG`

**Dòng kết:** "Yêu khí tan. Văn Lang yên. Trên đỉnh Nghĩa Lĩnh, một hình rồng mới mở mắt - và nó nói bằng giọng của rất nhiều người."

### `E-03 DOAN_TUYET_LONG_MACH`

**Dòng kết:** "Ngọc vỡ. Rồng lặn về huyền thoại. Thế giới nhẹ đi một gánh - và nặng thêm một nỗi không ai bảo hộ. Từ nay, con người tự lo lấy mình."

### `E-04 HOA_GIAI_BACH_TOC` (kết thúc thật)

**Dòng kết:** "Không ai thắng. Không ai cai trị. Năm mảnh ngọc thành vật chứng, không thành vương miện. Các cộng đồng lần đầu nhìn thấy phần lịch sử của chính mình - và tế đàn thành nơi họ học cách nhớ cùng nhau."

### `E-04-PARTIAL`

**Dòng kết:** "Hòa giải đã bắt đầu, nhưng còn những oan khuất chưa được gọi tên. Tế đàn mở - chưa trọn."

### `E-03-BITTER`

**Dòng kết:** "Long Nhân muốn hòa giải nhưng chưa đủ. Ngọc vẫn vỡ. Các cộng đồng chưa kịp thấy sự thật đã mất luôn chỗ dựa. Một kết thúc giải phóng - nhưng đến quá sớm."

Ghi chú cuối: Không ending nào có Lạc Long Quân xuất hiện trực tiếp. Tiếng Vọng chỉ vọng, không bước ra giải quyết.
