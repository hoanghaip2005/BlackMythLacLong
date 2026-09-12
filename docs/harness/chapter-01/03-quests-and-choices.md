# CH-01 Quests and Choices

## Quest map

| ID | Loại | Tên | Bắt buộc | Tác động |
|---|---|---|---|---|
| `Q-CH01-001` | Main | Lời hứa dưới vực | Có | Mở đường tới đền và boss |
| `Q-CH01-002` | Optional | Ba hồi chuông | Không | Cải thiện khả năng đọc arena, mở lore |
| `Q-CH01-003` | Bond | Người bị bỏ lại | Có để `released` | Giải quyết bond của `LG-01` |
| `Q-CH01-004` | Exploration | Dấu móng trên đá | Không | Gieo mồi cho Hỗn Mang và CH-02 |
| `Q-CH01-00H` | Hidden | Vong đáy vực | Không | Mở `HB-01`; cộng `hidden_released` nếu giải thoát (ADR-004) |

## Q-CH01-001: Lời hứa dưới vực

### Intent

Đưa Long Nhân từ “đi theo ánh sáng” sang “chọn tin một cộng đồng chưa biết mình là ai”. Quest không yêu cầu người chơi hiểu toàn bộ lore.

### Giver

Không có giver duy nhất. Quest tự mở khi Long Nhân nhặt đoản kiếm ở `CH-01-S01`.

### Steps

1. **Rời trứng đá:** đi qua rạn san hô héo.
2. **Theo dấu đèn:** xác định nguồn tín hiệu từ đền chìm.
3. **Gặp Linh:** quyết định cứu người giữ đèn hoặc đuổi theo dấu vảy lửa.
4. **Vào đền:** tìm ba ký hiệu của lời hứa.
5. **Đối mặt tiếng gọi:** đi qua xoáy vực.
6. **Xử lý Ngư Tinh:** kết thúc encounter `B-01`.
7. **Rời vùng nước chết:** xác nhận hậu quả và mở hướng đất liền.

### Completion

Quest hoàn thành khi `CH01_END_*` được ghi. Không hoàn thành chỉ bằng việc giảm HP Ngư Tinh; phải ghi `boss_fates[B-01]`.

### Failure/cost

Không có game over narrative do bỏ Linh hoặc bỏ qua bia. Cost là thông tin, trust, telegraph và aftermath khác nhau. Người chơi không bị ép vào một “đáp án đạo đức đúng”.

## Q-CH01-002: Ba hồi chuông

### Premise

Ba mảnh chuông nằm trong rạn san hô, mỗi mảnh bị một dạng thủy quái giữ. Chuông không phải chìa khóa bắt buộc; nó là cách người chơi học ngôn ngữ cảnh báo của Thủy tộc.

### Objectives

- Tìm `BELL-01` ở xác thuyền.
- Tìm `BELL-02` trong hốc san hô có dòng nước ngược.
- Tìm `BELL-03` sau một đàn cá quay đầu đồng loạt.
- Đặt ba mảnh vào bệ chuông ở `CH-01-S04`.

### Effects

- `Q-CH01-002_COMPLETE = true`.
- Trong boss encounter, ba hồi chuông báo trước xoáy lớn.
- Mở dialogue của Linh về việc đền từng dẫn đường cho cả người sống lẫn người chết.
- Không tăng `mercy_marks` trực tiếp; quest chỉ cung cấp hiểu biết.

## Q-CH01-003: Người bị bỏ lại

### Unlock

Mở khi người chơi đọc ít nhất hai trong ba ký hiệu ở `CH-01-S04`.

### Bond objective

Không thuyết phục Ngư Tinh bằng lời. Người chơi phải hoàn thành ba hành động cho thấy mình không đến chỉ để lấy ngọc:

1. Cứu hoặc thắp lại một đèn đền.
2. Không phá bia lời hứa để mở đường nhanh.
3. Đứng lại nghe toàn bộ ký ức của Ngư Tinh ở `CH-01-S05`.

### Completion condition for release

- `CH01_LINH_RESCUED = true`.
- `CH01_GLYPHS_READ >= 3`.
- `CH01_BOSS_LISTENED = true`.
- Trong encounter, người chơi kích hoạt ít nhất hai neo lời hứa thay vì phá chúng.
- Đánh bại phase cuối mà không dùng `C-CH01-003: force_absorb`.

### Incomplete bond

Nếu thiếu một điều kiện, người chơi vẫn có thể nói đúng câu cần nói, nhưng nguyên thần không đồng thuận. Kết quả là `defeated_by_force`, không phải `released`.

## Q-CH01-004: Dấu móng trên đá

### Premise

Một vết móng đen trên đá không khớp với Ngư Tinh. Nó nằm gần một bức phù điêu đã bị cào mất phần đầu.

### Purpose

Gieo mồi rằng yêu khí có tác động chủ động lên ký ức, nhưng không giới thiệu tên Hỗn Mang quá sớm.

### Reward

- Lore fragment: “một bóng đen không có hình hài kéo tiếng gọi đi ngược dòng”.
- Nếu hoàn thành, Tiếng Vọng Lạc Long ở `CH-01-S07` thêm một câu hỏi về “thứ đứng sau nỗi oán”.

## Q-CH01-00H: Vong đáy vực (Oan Khuất Ẩn — ADR-004)

### Premise

Quest ẩn tùy chọn mở màn ẩn `CH-01-HIDDEN` và boss ẩn `HB-01` (Ma Da — Vong Đáy Vực). Không bắt buộc; không chặn `CH01_END_*`.

### Unlock

- Sau `CH-01-S06`, trước khi rời vùng nước chết (`CH-01-S08`).
- Gợi mở khi `CH01_GLYPHS_READ_3` hoặc `Q_CH01_002_COMPLETE`: khi xoáy rút, một dòng tối kéo *xuống dưới vực* thay vì lên bờ.

### Objectives

1. Lặn xuống bãi xác thuyền dưới vực.
2. Nhận ra `ma da` kéo người sống vì muốn được *nhớ tên*, không phải vì đói.
3. Tìm hồi chuông “không-về” (hồi thứ ba) hoặc một cái tên khắc trên xác thuyền.
4. Chọn: giải thoát (đánh chuông + gọi tên) hay dẹp/cưỡng đoạt khối vong.

### Effects

- `released`: `boss_fates[HB-01] = released`, `hidden_released +1`, `mercy_marks +1`, `CH01_HIDDEN_RELEASED`; mở `hidden_truth` đào sâu `TRUTH_SEAL_WAS_NEVER_BROKEN`.
- `defeated_by_force`: `boss_fates[HB-01] = defeated_by_force`; không tăng `hidden_released`.
- `absorbed`: `boss_fates[HB-01] = absorbed`, `dragon_hunger +1`; không tăng `hidden_released`.

### Cost / fail

Bỏ qua quest hoàn toàn hợp lệ; cost duy nhất là không có `hidden_released` từ CH-01 (ảnh hưởng điều kiện `E-04` về sau). Không có game over.

## Choice registry

### `C-CH01-001`: Linh và dòng kéo

| Lựa chọn | Người chơi biết | State | Feedback gần | Hậu quả xa |
|---|---|---|---|---|
| Cứu Linh | Có người mắc trong lưới; dấu vảy lửa đang biến mất | `tribal_trust +1`, `CH01_LINH_RESCUED` | Linh giữ đèn, đọc được chuông | Dễ đạt `released`; Thủy tộc cởi mở hơn |
| Đuổi theo | Dấu vảy có thể dẫn thẳng tới nguồn nước dâng | Chưa tăng hunger ngay; `CH01_LINH_ABANDONED` | Linh tự cắt lưới, đèn tắt | Thiếu cảnh báo arena; Linh giữ khoảng cách |

### `C-CH01-002`: Cách gọi Ngư Tinh

| Lựa chọn | Ý định | State | Feedback |
|---|---|---|---|
| Gọi nỗi đau | Công nhận bị bỏ lại | `CH01_BOSS_NAMED_WOUND` | Ngư Tinh ngừng một nhịp trước khi tấn công |
| Gọi quái vật | Ưu tiên an toàn và phán xét hành vi | `CH01_BOSS_CONDEMNED` | Boss vào phase 1 ngay |
| Im lặng/Thế Ngự | Quan sát trước khi cam kết | `CH01_BOSS_HEARD` | Mở counterplay phản đòn và line ký ức |

### `C-CH01-003`: Cách nhận nguyên thần

| Lựa chọn | Điều kiện | State | Ending signal |
|---|---|---|---|
| Tiếp nhận có chủ ý | Bond hoàn tất | `released`, `memory_recovered +1`, `mercy_marks +1`, `relics_purified +1` | Nước trong lại từng mảng; ngọc sáng ấm |
| Cưỡng đoạt | Luôn có sau boss | `absorbed`, `dragon_hunger +1` | Vệt đen chạy dưới da; ngọc sáng lạnh |
| Không chạm | Boss đã hạ nhưng không release | `defeated_by_force` | Nguyên thần tự hòa vào ngọc; ký ức bị khuyết |

## Choice design rules for CH-01

- Không hiển thị nhãn “Mercy” hoặc “Hunger” cho người chơi như điểm đạo đức; biểu hiện bằng fiction và hậu quả.
- Cứu Linh không biến toàn bộ encounter thành dễ; nó chỉ cung cấp thông tin và một hỗ trợ đọc pattern.
- Đuổi theo không phải nhánh “ác”; nó là lựa chọn hợp lý nếu người chơi ưu tiên ngăn thảm họa ngay.
- Cưỡng đoạt không cho phần thưởng narrative giả tạo; game phải cho thấy sức mạnh có lợi ích thật và cost thật.
