# CH-02 State and Handoff

## Initial state

```yaml
chapter: CH-02
location: tay_ho_fox_corpse_marsh
weapon: WEAPON-DONGSON-THACHSON-AXE   # đã thức tỉnh sau CH-01
long_ngoc: [LG-01]                      # LG-01 đã thu ở CH-01 (trạng thái tùy CH01_END_*)
variables:
  memory_recovered: <kế thừa CH-01, 0..1>
  mercy_marks: <kế thừa CH-01>
  tribal_trust: <kế thừa CH-01>
  dragon_hunger: <kế thừa CH-01>
  relics_purified: <kế thừa CH-01, 0..1>
  hidden_released: 0
flags:
  - CH02_STARTED
  - LONG_NHAN_UNNAMED          # vẫn chưa có tên thật
  - LG01_ACQUIRED
boss_fates: {B-01: <kế thừa>}
final_decision: null
```

> Ghi chú: `tribal_trust` là biến **tổng hợp跨 chương** (miền 0..6). CH-01 góp tối đa +1 (cứu Linh). CH-02 có thể góp thêm qua các choice/quest dân đầm.

## Required flags

| Flag | Set at | Meaning |
|---|---|---|
| `CH02_STARTED` | S01 | Chương bắt đầu |
| `CH02_SINGER_TRUSTED` | S02 | Tin/đi theo tiếng hát có đối chiếu |
| `CH02_SINGER_DOUBTED` | S02 | Coi tiếng hát là mồi, bỏ qua |
| `CH02_FACE_CLUE_<n>` | S01/S02/S04 | Mỗi clue thật/giả được đối chiếu |
| `CH02_FACES_CROSSCHECKED` | S03 | Đọc ≥2 clue ⇒ loại được mặt nạ ở B02-P1 |
| `CH02_DAOSI_SIDED` | S04 | Đứng về phía Khâu đạo sĩ |
| `CH02_DAOSI_EXPOSED` | S04 | Lật mặt kẻ mượn miệng đạo sĩ |
| `CH02_DAOSI_REFUSED` | S04 | Không chọn phe |
| `CH02_DEVOURER_CLUES_<n>` | S04/hidden | Clue về kẻ ăn tên (Hỗn Mang) |
| `CH02_BOSS_NAMED_WOUND` | S05/B02 | Gọi đúng bản chất Hồ Tinh |
| `CH02_BOSS_CONDEMNED` | S05/B02 | Kết tội "quái vật" trước |
| `CH02_BOSS_HEARD` | S05 | Im lặng, giữ Thế Ngự, nghe hết |
| `CH02_BOSS_LISTENED` | S05 | Nghe trọn ký ức tiền-boss |
| `CH02_NAMES_RETURNED` | S06/quest | Trả tên cho dân đầm (một phần bond) |
| `CH02_PHANTHANH_AWAKENED` | S05/B02 | Mở khả năng Phân Thân |
| `Q_CH02_002_COMPLETE` | optional | Ba mặt nạ soi gương |
| `Q_CH02_003_COMPLETE` | bond | Đủ điều kiện bond để release |
| `Q_CH02_004_COMPLETE` | exploration | Dấu kẻ ăn tên |
| `CH02_END_RELEASED` | S06 | Hồ Tinh released |
| `CH02_END_FORCE` | S06 | Hồ Tinh defeated_by_force |
| `CH02_END_ABSORBED` | S06 | Hồ Tinh absorbed |
| `CH02_HIDDEN_FOUND` | hidden | Vào Hang gương |
| `CH02_HIDDEN_RELEASED` | hidden | Giải thoát HB-02 (`hidden_released +1`) |
| `CH02_HIDDEN_ABSORBED` | hidden | Cưỡng đoạt HB-02 (`dragon_hunger +1`) |
| `CH02_HIDDEN_KILLED` | hidden | Kết liễu HB-02 |
| `CH02_COMPLETE` | S06 | Chương hoàn thành, mở CH-03 |

## State transition matrix

| Event | Variables | Flags | Player-facing feedback |
|---|---|---|---|
| Tin tiếng hát (có đối chiếu) | `tribal_trust +1` (nếu dẫn tới giúp dân đầm) | `CH02_SINGER_TRUSTED` | Ma trơi đổi màu lạnh→ấm |
| Bỏ tiếng hát | none | `CH02_SINGER_DOUBTED` | Người Hát chỉ còn là giọng |
| Đối chiếu ≥2 clue | none | `CH02_FACES_CROSSCHECKED` | Ở B02-P1 loại được bản sao |
| Đứng về đạo sĩ | `dragon_hunger +1` (nếu đốt đầm hại dân) | `CH02_DAOSI_SIDED` | Boss vào phase mạnh; dân đầm khép |
| Lật mặt kẻ mượn miệng | `tribal_trust +1` | `CH02_DAOSI_EXPOSED` | Mở clue kẻ ăn tên; Hồ Tinh bớt thù |
| Gọi đúng bản chất Hồ Tinh | none | `CH02_BOSS_NAMED_WOUND` | Boss ngừng một nhịp |
| Trả tên cho dân đầm | `tribal_trust +1`, góp bond | `CH02_NAMES_RETURNED` | Bóng có mặt; feedback E-04 |
| Release boss | `memory_recovered +1`, `mercy_marks +1`, `relics_purified +1` | `CH02_END_RELEASED` | Ma trơi ấm; gương trong |
| Force boss | none | `CH02_END_FORCE` | LG-02 chập chờn |
| Absorb boss | `dragon_hunger +1` | `CH02_END_ABSORBED` | Phản chiếu không khớp |
| Mở Phân Thân | none | `CH02_PHANTHANH_AWAKENED` | Ảo ảnh đất sét khả dụng |
| Release HB-02 | `hidden_released +1`, `mercy_marks +1` | `CH02_HIDDEN_RELEASED` | Bóng thành người rồi tan; tên hiện |
| Absorb HB-02 | `dragon_hunger +1` | `CH02_HIDDEN_ABSORBED` | Gương vỡ; trượt E-04 |
| Chapter exit | none | `CH02_COMPLETE`, `LG02_ACQUIRED` | Mở hook CH-03 |

## State invariants

- `LG-02` chỉ được thu một lần.
- Chỉ một trong `CH02_END_RELEASED/FORCE/ABSORBED` đúng.
- `CH02_END_RELEASED` đòi `CH02_BOSS_NAMED_WOUND` + `CH02_FACES_CROSSCHECKED`; không đến từ một câu thoại đơn lẻ.
- `memory_recovered` tăng tối đa một lần trong CH-02.
- `relics_purified` chỉ tăng khi release, không tăng khi force/absorb.
- `hidden_released` chỉ tăng khi `boss_fates[HB-02] = released`.
- `dragon_hunger` không giảm trong CH-02.
- `CH02_DEVOURER_CLUES_*` không được khẳng định "phong ấn đã vỡ"; chỉ gieo Hỗn Mang là kẻ ăn tên.
- Không gọi `LG-02` là "mảnh 2 trong 6".

## Handoff: gameplay

### Required experience

- Di chuyển đầm lầy: bệ sình lún, sương giới hạn tầm nhìn, ma trơi dẫn hướng (đúng/sai).
- Cơ chế thật/giả: đọc bóng + gương nước để phân biệt bản thể và Phân Thân của boss.
- Mở/khai thác `Phân Thân` (ảo ảnh đất sét) như một công cụ đối chiếu/đánh lạc, không chỉ là DPS.
- Ba stance hook dùng lại: `Thế Ngự` (phản đòn → lộ bóng thật), `Thế Đột` (xuyên bản thể/ức), `Thế Trảm` (dọn bóng trồi).
- Arena boss có vùng gương an toàn đổi vị trí.
- Hidden boss không thể "thuần DPS" ra `released`; phải đọc gương + gọi tên.

### Explicitly deferred

- Damage, health, stamina, resource numbers.
- Hitbox/frame data; cách render phản chiếu/gương trong engine.
- Save serialization cho biến跨 chương.
- Số lượng bản sao Phân Thân tối đa (tuning).

## Handoff: art

- Đầm xác cáo: sương, ma trơi (will-o'-wisp), mặt nước gương, bệ cỏ/sình; không dùng rừng rậm nhiệt đới sáo rỗng.
- Hồ Tinh: cáo đầm lớn, chín đuôi, KHÔNG nhân hình quyến rũ; mặt nạ đất sét mượn mặt.
- Bóng Vô Danh: bóng không mặt, khoác mặt người; vệt đen trên gương.
- Hang gương: vô số mặt phản chiếu; mỗi gương một khuôn mặt mất tên.
- Long Ngọc LG-02: vật chứng ký ức (một cái tên), không phải loot gem.
- Ma trơi đổi màu lạnh→ấm như một ngôn ngữ trạng thái nhất quán toàn chương.

## Handoff: audio

- Nền sương đầm có khoảng lặng cho thoại; tiếng hát Người Hát là motif dẫn đường/đánh lạc (phải phân biệt được "hát thật" và "hát mượn").
- Hồ Tinh: giọng hai nghĩa, có tầng echo; khi nói thật bớt echo.
- Bóng Vô Danh: giọng chắp vá từ nhiều mảnh (như ghép từ các giọng đã mất).
- Ma trơi: âm cao lạnh khi lừa, ấm khi thật.
- Release: hát rõ lời, gương ngân. Absorb: tiếng hát bị bóp nghẹt, không "evil sting" lộ liễu.

## Handoff: localization

- Giữ glossary: `Long Nhân`, `Long Ngọc`, `Hồ Tinh`, `Cửu Vĩ`, `Phân Thân`, `Rìu Thần Thạch Sơn`, `ma trơi`.
- Phân biệt "tên thật" (true name) và "mặt nạ" (mask) — hai khái niệm chủ đề, không dịch lẫn.
- "bị mất tên" khác "bị lãng quên"; giữ khác biệt vì nối CH-04 (bị xóa khỏi lịch sử).
- Không dịch `Dân đầm Tây Hồ` thành "water monsters".
- Thoại Hồ Tinh phải giữ tính hai nghĩa khi dịch; ưu tiên mơ hồ có chủ đích hơn là rõ ràng.
