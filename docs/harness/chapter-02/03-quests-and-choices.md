# CH-02 Quests and Choices

## Quest map

| ID | Loại | Tên | Bắt buộc | Tác động |
|---|---|---|---|---|
| `Q-CH02-001` | Main | Tên thật dưới đầm | Có | Mở đường tới boss và `LG-02` |
| `Q-CH02-002` | Optional | Đối chiếu ba khuôn mặt | Không | Cải thiện đọc arena; mở lore thật/giả |
| `Q-CH02-003` | Bond | Gọi lại tên cho bóng | Có để `released` | Giải quyết bond của `LG-02` |
| `Q-CH02-004` | Exploration | Dấu vết kẻ ăn tên | Không | Gieo mồi Hỗn Mang và màn ẩn |
| `Q-CH02-00H` | Hidden | Cái tên bị ăn đầu tiên | Không (ADR-004) | Giải thoát `HB-02`; `hidden_released +1`; sâu `TRUTH_FOX_WAS_A_REFUGE` |

## Q-CH02-001: Tên thật dưới đầm

### Intent

Đưa Long Nhân từ "theo tiếng hát" sang "chọn tin một cộng đồng không còn mặt". Quest không yêu cầu hiểu toàn bộ lore.

### Giver

Không có giver duy nhất. Quest tự mở khi Long Nhân vào làng không bóng ở `CH-02-S01`.

### Steps

1. **Vào làng không bóng:** nhận ra mặt nạ/đất sét và cái sai của phản chiếu.
2. **Theo tiếng hát:** xác định nguồn ở `CH-02-S02`.
3. **Đối chiếu ba khuôn mặt:** tìm mặt nạ thật ở `CH-02-S03`.
4. **Chọn phía với đạo sĩ:** quyết định ở `CH-02-S04`.
5. **Đọc gương nước:** xác nhận `TRUTH_FOX_WAS_A_REFUGE` ở `CH-02-S05`.
6. **Xử lý Hồ Tinh:** kết thúc encounter `B-02`.
7. **Trả tên / rời đầm:** ghi `CH02_END_*`, mở hướng Phong Châu.

### Completion

Hoàn thành khi `CH02_END_*` được ghi và `boss_fates[B-02]` xác định. Không hoàn thành chỉ bằng giảm HP boss.

### Failure/cost

Không có game over narrative do nghi ngờ sai hoặc theo đạo sĩ. Cost là thông tin, `tribal_trust`, telegraph và aftermath khác nhau.

## Q-CH02-002: Đối chiếu ba khuôn mặt

### Premise

Ba khuôn mặt Hồ Tinh hiện ở ba nơi trong đầm. Chỉ một là thật; hai là Phân Thân. Người chơi thu ba "dấu đối chiếu" (bóng, phản chiếu gương, tiếng hát) để biết mặt nào khớp.

### Objectives

- Tìm `CLUE-BONG` (bóng thật) ở làng.
- Tìm `CLUE-GUONG` (phản chiếu không khớp) ở mặt nước.
- Tìm `CLUE-HAT` (chỗ đứt nhịp bài hát) trong sương.
- Đối chiếu đủ ba ở `CH-02-S03`.

### Effects

- `Q_CH02_002_COMPLETE = true`; `CH02_FACES_CROSSCHECKED = true`.
- Trong boss fight, mặt nạ thật được đánh dấu sớm (telegraph), không đổi ending condition.
- Mở thoại Cụ Đàm về việc "ngày xưa người ta đổi tên để sống".
- Không tăng `mercy_marks` trực tiếp; quest chỉ cung cấp hiểu biết.

## Q-CH02-003: Gọi lại tên cho bóng

### Unlock

Mở khi người chơi đọc gương nước ở `CH-02-S05` (xác nhận cáo từng che chở).

### Bond objective

Không thuyết phục Hồ Tinh bằng lời. Người chơi phải hoàn thành ba hành động cho thấy mình đến để trả tên, không phải để săn:

1. Không giết bóng bằng lực; học cách gọi một cái tên ở `CH-02-S01`.
2. Không đứng về phía đạo sĩ để "diệt tà" (`C-CH02-002 != side_daosi`).
3. Đứng lại nghe trọn ký ức Hồ Tinh ở `CH-02-S05`.

### Completion condition for release

- `CH02_NAMES_LEARNED >= 1` (biết ít nhất một tên thật).
- `CH02_BOSS_LISTENED = true`.
- Trong encounter, gọi đúng mặt nạ thật thay vì chém mọi bản sao (`CH02_FOX_NAMED = true`).
- Hạ phase cuối mà không dùng `C-CH02-003: absorb`.

### Incomplete bond

Nếu thiếu điều kiện, người chơi vẫn có thể hạ boss, nhưng nguyên thần không đồng thuận. Kết quả là `defeated_by_force`, không phải `released`.

## Q-CH02-004: Dấu vết kẻ ăn tên

### Premise

Một dấu đen không có hình hài kéo lê qua đầm, ăn mất tên khỏi bia và khỏi ký ức. Nó không khớp với Hồ Tinh.

### Purpose

Gieo mồi rằng chính Hỗn Mang mới là kẻ ăn tên, nhưng không nêu tên nó quá sớm.

### Reward

- Lore fragment: "cái bóng không mặt đã ở đây trước con cáo".
- Nếu hoàn thành, mở manh mối vị trí `CH-02-HIDDEN` và thêm một câu hỏi của Tiếng Vọng ở `CH-02-S06`.

## Q-CH02-00H: Cái tên bị ăn đầu tiên (hidden - ADR-004)

### Unlock (tùy chọn)

Mở khi `Q-CH02-004_COMPLETE` và người chơi đối chiếu đủ clue để tìm miệng `CH-02-HIDDEN` sau gương nước.

### Hidden bond objective

Tìm **tên thật của Bóng Vô Danh** (gợi ý: bia không tên, bài hát, và ký ức Hồ Tinh). Người chơi phải **gọi tên nó trước khi Phân Thân chiếm mặt Long Nhân**.

### Completion condition for release

- `CH02_HIDDEN_NAME_KNOWN = true`.
- `CH02_HIDDEN_FACED = true` (không chém bằng lực).
- Gọi tên ở đúng cửa sổ bond → `HB02-RELEASED`, `hidden_released +1`, `mercy_marks +1`.

### Incomplete / wrong

- Hạ/cưỡng đoạt `HB-02` → `dragon_hunger +1`, không tăng `hidden_released`, đầm không sáng đèn.

## Choice registry

### `C-CH02-001`: Tiếng hát và hình cáo

| Lựa chọn | Ý định | Người chơi biết | State | Feedback gần | Hậu quả xa |
|---|---|---|---|---|---|
| Theo tiếng hát | Tin một người cụ thể | tiếng hát ở giữa đầm; bóng không mặt | `CH02_SINGER_TRUSTED`, `tribal_trust +1` | Người Hát chỉ chỗ mặt nạ thật | Dễ đạt `released`; mở bond |
| Săn hình cáo mạnh nhất | Ưu tiên diệt "quái" | vệt lông cáo lớn, đầm động | `CH02_FOX_HUNTED` | Hồ Tinh coi Long Nhân là kẻ săn | Khó `released`; thiếu một neo tên |
| Đối chiếu trước khi tin | Hoài nghi có phương pháp | ba khuôn mặt không khớp | `CH02_FACES_CROSSCHECKED`, `memory_recovered` (clue) | đọc được mặt thật | Mở `Q-CH02-002`, telegraph boss |

### `C-CH02-002`: Đạo sĩ bị thao túng

| Lựa chọn | Ý định | State | Feedback | Hậu quả xa |
|---|---|---|---|---|
| Đứng về phía đạo sĩ | Tin "trừ tà" | `CH02_DAOSI_SIDED` | một nhóm dân đầm theo; bóng bị đốt | `tribal_trust` giảm; Hồ Tinh thù địch; khó `released` |
| Vạch trần thao túng | Tìm kẻ đứng sau | `CH02_DAOSI_EXPOSED` | mắt đạo sĩ phản chiếu mặt mượn | đạo sĩ tỉnh, về sau giúp gọi tên |
| Không chọn phe | Từ chối cả hai | `CH02_DAOSI_REFUSED` | cả hai đều không tin Long Nhân | trung tính; bond phải tự chứng minh bằng hành động |

### `C-CH02-003`: Cách nhận nguyên thần Hồ Tinh

| Lựa chọn | Điều kiện | State | Ending signal |
|---|---|---|---|
| Gọi đúng tên (release) | Bond hoàn tất | `released`, `memory_recovered +1`, `mercy_marks +1`, `relics_purified +1` | sương tan; mặt nạ chìm; tên sáng |
| Diệt (force) | Boss đã hạ | `defeated_by_force` | đầm vẫn không tên; ký ức khuyết |
| Cưỡng đoạt (absorb) | Luôn có sau boss | `absorbed`, `dragon_hunger +1` | vệt đen dưới da; Phân Thân mạnh nhưng nhiễu |

### `C-CH02-00H`: Bóng Vô Danh (hidden)

| Lựa chọn | Điều kiện | State | Feedback |
|---|---|---|---|
| Gọi tên nó (release) | biết tên + không chém | `HB02-RELEASED`, `hidden_released +1`, `mercy_marks +1` | bóng thành người; đầm sáng đèn |
| Cưỡng đoạt/hạ | luôn có | `HB02-ABSORBED`/`HB02-KILLED`, `dragon_hunger +1` | gương vỡ; không tăng `hidden_released` |

## Choice design rules for CH-02

- Không hiển thị nhãn đạo đức; biểu hiện bằng fiction (sương tan hay đặc, dân đầm gọi tên hay quay lưng).
- Theo đạo sĩ không phải nhánh "ác"; nó là lựa chọn hợp lý nếu người chơi tin lời đồn và ưu tiên diệt mối đe dọa ngay.
- Đối chiếu không bắt buộc để thắng, nhưng bắt buộc để hiểu và để `released` dễ hơn.
- Cưỡng đoạt cho lợi ích cảm nhận ngay (Phân Thân mạnh) và cost thật (dân đầm sợ, `dragon_hunger`, mầm E-02).
