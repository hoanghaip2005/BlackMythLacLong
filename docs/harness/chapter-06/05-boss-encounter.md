# CH-06 Boss Encounter: Hỗn Mang

> **Ghi chú ADR-004:** CH-06 **không có boss ẩn** (`HB-06` không tồn tại). Thay vào đó là **màn full-completion tùy chọn** (`CH-06-FULL`, xem `01-scene-flow.md`): khi `hidden_released = 5`, năm Oan Khuất Ẩn (`HB-01..05`) hiện về làm chứng, nâng `reconcile` từ `E-04-PARTIAL` lên `E-04` trọn vẹn.

## Encounter identity

- ID: `B-06`
- Name: Hỗn Mang (trong hình dạng Long Nhân)
- Arena: đỉnh tế đàn Nghĩa Lĩnh; năm bệ ngọc quanh một vòng tròn trung tâm; ký ức chồng lấn hiển thị như lớp ảnh mờ trên đá.
- Player objective: không "giết trùm". Người chơi phải **làm một điều Hỗn Mang chưa từng thấy** (Canon Lock 8) để phá thế sao chép, rồi **chọn `final_decision`** tại tế đàn.
- Emotional promise: người chơi nhận ra kẻ thù cuối là **phần tối của chính mình và của cả một vùng đất**, và rằng chiến thắng thật là một *lựa chọn*, không phải một cú chém.

## Arena storytelling

Arena chia ba lớp đọc:

1. **Lớp bản ngã:** tế đàn phản chiếu Long Nhân; bóng của người chơi và bóng của Hỗn Mang chồng lên nhau, khó phân biệt ai là thật.
2. **Lớp ký ức:** năm bệ ngọc phát lại năm sự thật của năm chương khi người chơi đứng gần; nếu `hidden_released` cao, có thêm ánh sáng của các oan khuất đã được tha.
3. **Lớp phủ nhận:** Hỗn Mang xóa/méo các lớp ký ức khi nó thắng thế, cố thuyết phục rằng "lựa chọn" là ảo tưởng.

Không cần map/coordinate cố định. Arena phải luôn giữ một vùng trung tâm để đối diện và năm bệ ngọc ở rìa để người chơi "đọc" lại ký ức giữa trận.

## Boss desire in combat

Hỗn Mang không cố giết Long Nhân. Nó cố **chứng minh Long Nhân không có lựa chọn thật** - rằng mọi hành động đều quy về bản năng chiếm đoạt, và trật tự nào cũng cần một kẻ thống trị (chính nó, hoặc chính Long Nhân trở thành nó).

- Khi người chơi chỉ đánh: Hỗn Mang càng tin "ngươi cũng như ta", sao chép hoàn hảo.
- Khi người chơi đọc ký ức / tha / làm điều phi tối ưu: Hỗn Mang **lúng túng** - nó không sao chép được lựa chọn chưa từng xảy ra.

`B06-P0` là intro không chiến đấu, không tính vào tổng phase.

## Intro: Bản sao (`B06-P0`)

### Narrative trigger

Sau `CH-06-S03`, yêu khí tụ thành hình Long Nhân. Nó bước ra từ chính bóng của người chơi.

### Experience hook

Người chơi đối diện **chính mình** - cùng silhouette, cùng vũ khí, nhưng mắt trống và bóng chồng nhiều bóng khác. Cảm giác "đánh nhau với gương".

### Player counterplay

Không đánh được trong intro. Người chơi quan sát năm bệ ngọc và nhận ra Hỗn Mang **chưa** đứng ở tư thế nào của riêng nó - nó chỉ đứng thế của Long Nhân.

## Combat Phase 1: Bản Sao (`B06-P1-MIRROR`)

### Narrative trigger

Hỗn Mang xác nhận nó thuộc mọi thói quen chiến đấu của Long Nhân. Nó đánh **y hệt** những gì người chơi đã dùng suốt năm chương.

### Visual read

- Hình dạng Long Nhân nhưng **lệch trục**: khớp đảo ngược nhẹ, bóng đi trước thân một nhịp, đường vảy rồng phát sáng như nứt.
- Dùng lại đúng ba thế (Trảm/Đột/Ngự) và các đòn đã mở (Thủy Ảnh, Lôi Kích, Phân Thân) - nhưng *thiếu* hơi người: chuyển động quá hoàn hảo, vô cảm.
- `LG` không nằm trong nó; nó rỗng - dấu hiệu nó chỉ là bản sao, không phải nguồn.

### Combat hook

- Hỗn Mang **phản đòn theo đúng thói quen** của người chơi: nếu người chơi quen spam Trảm, nó Ngự rồi trừng phạt; nếu quen Đột, nó né ngang.
- Nó sao chép cả `Thủy Ảnh`/`Lôi Kích` đã mở.
- Đòn của nó *đọc được* vì chính là đòn của người chơi - nhưng nhanh và không có khoảng nghỉ nhân tính.

### Telegraph

- Trước khi sao chép một đòn, nó **nháy lại tư thế** người chơi vừa dùng (một "echo" mờ).
- Bóng của nó tách khỏi thân nửa nhịp trước đòn mạnh - đọc hướng từ bóng, không từ thân.

### Player counterplay

- **Đổi thói quen:** làm ngược pattern mình hay dùng để Hỗn Mang đoán sai (nó chỉ sao chép cái *đã thấy*).
- `Thế Ngự` để phản chính đòn của mình; `Thế Đột` vào khoảnh khắc nó lặp lại tư thế.
- Đứng gần một bệ ngọc để ký ức làm nó nhiễu một nhịp.

### Narrative interaction

Khi người chơi **cố tình làm một đòn chưa từng dùng** (hoặc không đánh), Hỗn Mang khựng lại - hé lộ giới hạn của nó. Đây là mồi cho cao trào `B06-P2`.

## Combat Phase 2: Hợp Xướng (`B06-P2-CHOIR`)

### Narrative trigger

Hỗn Mang thôi chỉ sao chép Long Nhân; nó **đọc lại lựa chọn quá khứ** của người chơi và triệu hồi **dư ảnh của năm boss** theo đúng cách chúng bị xử lý.

### Visual read

- Thân nó **chồng nhiều lớp**: thoáng dáng Ngư Tinh, Hồ Tinh, Mộc Tinh, Đại Bàng, Song Giao - tùy `boss_fates`.
- Nếu người chơi đã `absorbed` boss nào, dư ảnh boss đó **đen và dữ** hơn, và Hỗn Mang nói bằng giọng boss ấy.
- Nếu người chơi đã `released`/tha nhiều (`mercy_marks` cao), dư ảnh **sáng và bình an**, và Hỗn Mang **khó sao chép** chúng - nó phải "diễn" lại, lộ rõ là giả.

### Combat hook

- Hỗn Mang dùng **biến thể đòn của năm boss** (quét nước, ảo ảnh, rễ trói, bổ nhào, sóng giao) - mỗi đòn gợi lại một chương.
- Nó **phủ nhận** lựa chọn của người chơi bằng lời giữa trận ("ngươi tha ư? rồi ngươi cũng cầm rìu tới đây").
- Khi `dragon_hunger` cao, nó mạnh lên và *mời gọi* ("ngươi giống ta rồi đấy").

### Telegraph

- Trước mỗi "dư ảnh boss", bệ ngọc tương ứng **tối lại** một nhịp.
- Giọng chồng lấn **tách ra** thành một giọng đơn lẻ ngay trước đòn vay mượn từ boss đó.

### Player counterplay

- Nhận ra đòn vay mượn từ boss nào và dùng counterplay đã học ở chương đó.
- `Chân Long` (trạng thái bùng nổ, miễn nhiễm nguyên tố ngắn hạn) để sống sót qua đợt hợp xướng - nhưng **không** kết thúc trận; nó chỉ câu giờ.
- Kích hoạt lại ký ức ở bệ ngọc để làm dịu dư ảnh đã được tha.

### Narrative interaction

Đây là lúc người chơi thấy **hậu quả của cả hành trình** hiện hình. Hỗn Mang mạnh hay yếu, đáng sợ hay đáng thương, tùy cách người chơi đã chơi (R-04).

## Cao trào: Nhát chém không sao chép được (`C-CH06-002`)

### Trigger

Khi Hỗn Mang dồn Long Nhân vào thế "mọi thứ đều đã thấy", người chơi phải làm **một điều chưa từng xảy ra**:

- **Hạ vũ khí** (từ chối vòng bạo lực), hoặc
- **Che cho một dư ảnh đã được tha** thay vì né, hoặc
- **Chém vào tế đàn / năm bệ ngọc** thay vì chém bản sao.

### Resolution

Hỗn Mang **không sao chép được** hành động này (Canon Lock 8). Nó khựng lại, lớp bản sao nứt ra, để lộ **khoảng trống** - nó không có lựa chọn của riêng nó, nó chỉ là tổng của những gì đã xảy ra. Trận đấu **dừng**, không phải vì boss "chết", mà vì nó **cạn luận cứ**. Tế đàn mở cho `final_decision`.

## Defeat state

Hỗn Mang **không nổ tung, không "chết"**. Bản sao tan thành yêu khí lơ lửng, năm bệ ngọc sáng lên, và Long Nhân đứng giữa tế đàn với **bốn khả năng**. Người chơi có toàn quyền di chuyển và đưa ra `C-CH06-003`. Không có "chiến thắng" trước khi `final_decision` được ghi.

## Fate resolution: `final_decision` → ending

Không dùng `boss_fates[B-06]` theo nghĩa tha/giết. Thay vào đó, `final_decision` (set ở `C-CH06-003`) quyết định ending theo **Resolution Rules** (`02 §7`):

| `final_decision` | Điều kiện kèm theo | Ending |
|---|---|---|
| `restore` | `dragon_hunger >= 4` | `E-02 TAN_HON_MANG` |
| `restore` | `dragon_hunger < 4` | `E-01 LONG_VUONG` (`relics_purified>=3` → ổn định; `<3` → không ổn định, hook phần tiếp) |
| `absorb` | - | `E-02 TAN_HON_MANG` |
| `destroy` | - | `E-03 DOAN_TUYET_LONG_MACH` |
| `reconcile` | đủ E-04 (incl. `hidden_released=5`) | `E-04 HOA_GIAI_BACH_TOC` |
| `reconcile` | thiếu `hidden_released=5`, đủ lõi khác | `E-04-PARTIAL` |
| `reconcile` | thiếu điều kiện lõi | `E-03-BITTER` (chuyển `destroy` mức bi kịch) |

## Boss lines by player state

| State | Line direction |
|---|---|
| `dragon_hunger >= 4` | "Ngươi đã ăn bao nhiêu nguyên thần rồi? Thêm một cái nữa thôi." |
| `mercy_marks >= 4` | "Ngươi tha nhiều thế. Vậy tại sao tay ngươi vẫn chưa buông rìu?" |
| `boss_fates` nhiều `absorbed` | "Chúng ở trong ta cũng như ở trong ngươi. Ta chỉ nói hộ chúng." |
| `hidden_released = 5` | "Những kẻ ngươi tha... chúng không đứng về phía ta nữa. Ngươi đã làm ta yếu đi từ trước khi lên đây." |
| `memory_recovered < 5` | "Ngươi còn chưa nhớ hết. Ngươi lấy tư cách gì mà chọn?" |
| Sau `C-CH06-003` (un-copied) | "...Cái đó ta chưa học được." |

## Combat-to-story acceptance

- [ ] Hỗn Mang đọc được như **bản sao của chính người chơi**, không phải quỷ vương sáo rỗng.
- [ ] Phase 1 sao chép thói quen chiến đấu; phase 2 đọc lại lựa chọn quá khứ (khác biệt rõ).
- [ ] Có đường thắng bằng **hành động không sao chép được** (Canon Lock 8), không phải bằng damage.
- [ ] `Chân Long` chỉ là burst, không thay thế quyết định cuối.
- [ ] Boss **không "chết"** trước khi `final_decision` được ghi.
- [ ] Mỗi ending đều là một lựa chọn có giá phải trả; không ending nào là "thiện tuyệt đối".
- [ ] `hidden_released=5` mở màn chứng nhân (`CH-06-FULL`) và nâng `reconcile` lên `E-04` chuẩn.
- [ ] Không damage/HP/frame/shader/asset path (R-05).
- [ ] Lạc Long Quân không xuất hiện trực tiếp; chỉ có Tiếng Vọng (Canon Lock 9).
