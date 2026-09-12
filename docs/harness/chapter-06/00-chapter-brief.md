# CH-06: Hỗn Mang Tế Đàn

## Trạng thái

- ID: `CH-06`
- Version: `0.1`
- Status: `draft`
- Vùng: Đỉnh Nghĩa Lĩnh - tế đàn trên đỉnh núi, nơi hội tụ Long Khí của cả năm vùng.
- Thời lượng narrative mục tiêu: 60-90 phút cho first playthrough (duel + ending), chưa tính việc xem lại các ending.
- Mảnh Long Ngọc: KHÔNG có mảnh mới. Người chơi dùng đủ năm mảnh `LG-01..LG-05`.
- Boss: `B-06`, Hỗn Mang trong hình dạng Long Nhân.
- Truth flag: `TRUTH_SEAL_WAS_NEVER_BROKEN` được XÁC NHẬN đầy đủ tại đây; tổng hợp cả năm truth flag.

## Chapter promise

Người chơi bước lên tế đàn với năm mảnh ngọc và toàn bộ hậu quả của năm chương. Cuối chương, người chơi hiểu ba điều:

1. "Phong ấn bị phá" chưa từng có thật; đó là lớp ngụy trang Hỗn Mang dùng để biến nợ lịch sử tản mạn thành MỘT kẻ thù duy nhất.
2. Hỗn Mang không phải ác quỷ vô nguồn gốc; nó là oán nghiệp tập thể của nhiều cuộc chiến tranh giành lãnh thổ, và nó sao chép chính Long Nhân.
3. Không có "ending đúng". Cứu, giải thoát hay bắt đầu lại đều là một định nghĩa về "cứu thế giới" mà người chơi phải tự chịu trách nhiệm.

## Dramatic question

**Khi kẻ thù mang khuôn mặt của chính mình và đưa ra bốn con đường, Long Nhân sẽ là người giữ Long Mạch, vật chứa oán nghiệp, kẻ chặt đứt huyết thống, hay người trả ký ức về cho trăm họ?**

## Emotional arc

| Chặng | Trạng thái Long Nhân | Cảm xúc người chơi | Hình ảnh chủ đạo |
|---|---|---|---|
| Mở đầu | Mang đủ năm ngọc, đủ (hoặc thiếu) sự thật | Lặng, nặng, dự cảm | Bậc đá không đổ bóng lên tế đàn |
| Quy tụ | Năm ký ức mở cùng lúc | Choáng, đau buồn, sáng tỏ | Năm quầng sáng ngọc chồng lên nhau |
| Đối diện | Gặp bản sao của chính mình | Bất an, bị phán xét | Hỗn Mang dựng hình từ ký ức Long Nhân |
| Đấu tay đôi | Bị đọc lại mọi lựa chọn cũ | Căng, bị soi xét | Bản sao dùng đúng đòn người chơi quen dùng |
| Quyết định | Tự chọn định nghĩa "cứu" | Trách nhiệm, mất mát, hy vọng | Tế đàn chờ một ý định |
| Ending | Trở thành điều mình chọn | Tùy ending: vinh quang lạnh / viên mãn / giải thoát / trống rỗng | Ending card riêng cho mỗi kết |

## Chapter non-goals

- Không giới thiệu mảnh Long Ngọc thứ sáu.
- Không cho Lạc Long Quân xuất hiện trực tiếp để giải quyết xung đột; chỉ là Tiếng Vọng/dấu tích.
- Không biến Hỗn Mang thành "trùm máu" thuần túy; duel là đối thoại bằng hành động.
- Không auto-grant ending hòa giải chỉ vì người chơi tử tế; `E-04` phải đạt bằng điều kiện (`02 §7`, ADR-004).
- Không khóa số liệu combat, cách boss đọc input runtime, hay cinematic implementation.

## Canon lock riêng cho CH-06

1. Tế đàn Nghĩa Lĩnh chỉ mở khi người chơi mang đủ năm mảnh `LG-01..LG-05`.
2. `TRUTH_SEAL_WAS_NEVER_BROKEN` là clue ở CH-01..05; CH-06 là nơi nó được xác nhận trọn vẹn (không có phong ấn nào từng vỡ).
3. Hỗn Mang (`B-06`) sao chép hình dáng và kỹ thuật Long Nhân ĐÃ thấy, nhưng KHÔNG sao chép được một lựa chọn người chơi CHƯA thực hiện (Canon Lock 8) - đây là chìa khóa của duel và của hòa giải.
4. Có đúng bốn quyết định cuối: `restore`, `absorb`, `destroy`, `reconcile`; mỗi cái map vào một ending theo Resolution Rules (`02 §7`).
5. `E-04 HOA_GIAI_BACH_TOC` là kết thúc thật/ẩn, đòi `final_decision=reconcile` + `memory_recovered=5` + `mercy_marks>=4` + `tribal_trust>=5` + đủ 5 `truth_flags` + `hidden_released=5` + không quá 2 boss `absorbed`.
6. Không ending nào xóa hậu quả của lựa chọn trước; ending chỉ tổng hợp và định nghĩa chúng (`08-continuity`).
7. `final_decision` được set đúng một lần, tại `CH-06-S05`.

## Chapter end states

> CH-06 resolve ĐÚNG MỘT ending. Thứ tự kiểm tra theo `02 §7` (từ trên xuống): `E-04` -> `E-02` -> `E-03` -> `E-01`, kèm hai tag fallback.

### `CH06_END_E01_LONG_VUONG` (`restore`, không thỏa E-02)

Long Nhân khôi phục mạng lưới Long Khí bằng năm mảnh ngọc, trở thành người canh giữ Long Mạch. Nếu `relics_purified >= 3`: khôi phục với tổn thất thấp, đất lành bền. Nếu `relics_purified < 3`: mạng lưới khôi phục không ổn định, hậu cảnh để hook phần tiếp. Đây là chiến thắng truyền thống nhưng vẫn đặt câu hỏi: một người có nên nắm quyền bảo hộ toàn cõi?

### `CH06_END_E02_TAN_HON_MANG` (`absorb`, hoặc `dragon_hunger>=4` + `restore`)

Long Nhân hấp thụ toàn bộ Hỗn Mang vào bản thân. Văn Lang hết yêu khí bên ngoài, nhưng Long Nhân trở thành trung tâm của một trật tự mới - đẹp hơn về hình thức, nguy hiểm hơn về bản chất. Vòng lặp quyền lực không kết thúc; nó đổi chủ.

### `CH06_END_E03_DOAN_TUYET_LONG_MACH` (`destroy`)

Long Nhân phá năm mảnh ngọc, chấm dứt huyết mạch siêu nhiên. Hỗn Mang mất nguồn khuếch đại; Long Nhân mất Long Khí. Các thế lực phải sống bằng năng lực của chính mình. Giải phóng, nhưng không bảo đảm hòa bình.

### `CH06_END_E04_HOA_GIAI_BACH_TOC` (`reconcile` + đủ điều kiện, kết thúc THẬT)

Hỗn Mang không bị đánh bại bằng quyền lực. Long Nhân trả ký ức về cho các cộng đồng, biến tế đàn thành nơi hòa giải; Long Ngọc mất chức năng cai trị, trở thành vật chứng sống. Nếu `hidden_released=5`: năm Oan Khuất Ẩn (HB-01..05) hiện về làm chứng nhân, nghi lễ trọn vẹn (`E-04` chuẩn).

### `CH06_END_E04_PARTIAL` (tag: `reconcile` + đủ điều kiện lõi nhưng `hidden_released<5`)

Nghi lễ hòa giải thành công ở phần lớn, nhưng những oan khuất bị bỏ sót (các `HB-0X` chưa giải thoát) không về làm chứng; còn dư oán âm ỉ. Đất lành, nhưng chưa trọn. Đây là biến thể của `E-04`, KHÔNG phải fallback bi kịch.

### `CH06_END_E03_BITTER` (tag: `reconcile` nhưng thiếu điều kiện lõi E-04)

Người chơi muốn hòa giải nhưng chưa đủ (thiếu `memory_recovered=5`, hoặc `mercy_marks<4`, hoặc `tribal_trust<5`, hoặc thiếu truth flag, hoặc quá 2 boss `absorbed`). Nghi lễ thất bại một phần, chuyển sang `destroy` ở mức bi kịch: ngọc vỡ nhưng các cộng đồng chưa kịp nhìn thấy sự thật. Phân biệt với `E-03` chuẩn bằng tag `E-03-BITTER`.

## Handoff summary

CH-06 cần các lớp bàn giao:

- **Narrative:** scene flow, dialogue Hỗn Mang/Tiếng Vọng, bốn quyết định, mapping final_decision -> ending, reveal "phong ấn chưa vỡ".
- **Gameplay hook:** duel tay đôi; boss mirror đọc stance/đòn đã thấy; `Chân Long` là trạng thái bùng nổ (không thay quyết định cuối); cơ chế "lựa chọn chưa từng thực hiện" để phá mirror.
- **Art/audio hook:** tế đàn không bóng, năm quầng ký ức, Hỗn Mang dạng bản sao méo, bốn ending card riêng, tiếng many-voices chồng lấn.
- **Cinematic hook:** mỗi ending một ending card + hậu cảnh; `E-04` có lớp chứng nhân oan khuất khi `hidden_released=5`.

Damage number, cách boss đọc input runtime, map coordinate, animation frame, model topology, VFX và save serialization để `TBD` ở phase sau.
