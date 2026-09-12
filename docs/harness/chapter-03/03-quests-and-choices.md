# CH-03 Quests and Choices

## Quest map

| ID | Loại | Tên | Bắt buộc | Tác động |
|---|---|---|---|---|
| `Q-CH03-001` | Main | Lời thề dưới rễ | Có | Mở đường qua Phong Châu tới Mộc Tinh |
| `Q-CH03-002` | Optional | Ba tấm bia thề | Không | Mở điều kiện bond, cải thiện đọc arena |
| `Q-CH03-003` | Bond | Người chết có tên | Có để `released` | Giải quyết bond của `LG-03` |
| `Q-CH03-004` | Exploration | Dấu móng trên bia | Không | Gieo mồi Hỗn Mang và CH-04 |
| `Q-CH03-00H` | Hidden | Gò mộ dưới rễ | Không | Mở `HB-03`; giải thoát -> `hidden_released +1` |

## Q-CH03-001: Lời thề dưới rễ

### Intent

Đưa Long Nhân từ "chạy theo ánh ngọc" sang "quyết định số phận một đội quân chết". Quest không yêu cầu hiểu toàn bộ lore.

### Giver

Không có giver duy nhất. Quest tự mở khi Long Nhân qua cổng Phong Châu ở `CH-03-S01`.

### Steps

1. **Qua cổng bị nuốt:** đi vào kinh đô cũ (`S01`).
2. **Đối mặt hàng ngũ:** gặp lính gác không mặt và Hiến (`S02`).
3. **Đọc bia lời thề:** tìm ba bia ở nghĩa địa dưới rễ (`S03`).
4. **Nghe hai phía:** chứng kiến Hiến và Trưởng cãi nhau về lời thề (`S04`).
5. **Tới lõi đỏ:** đi qua `S05` để mở arena.
6. **Xử lý Mộc Tinh:** kết thúc encounter `B-03`.
7. **Rời rừng:** xác nhận hậu quả ở `S06`, mở hướng CH-04.

### Completion

Hoàn thành khi `CH03_END_*` được ghi. Không hoàn thành chỉ bằng giảm HP Mộc Tinh; phải ghi `boss_fates[B-03]`.

### Failure/cost

Không có game over narrative do bỏ Hiến hoặc bỏ bia. Cost là thông tin, trust, telegraph và aftermath khác nhau. Người chơi không bị ép vào một "đáp án đạo đức đúng".

## Q-CH03-002: Ba tấm bia thề

### Premise

Ba bia lời thề nằm trong nghĩa địa, mỗi bia bị rễ ký sinh quấn. Bia không phải chìa khóa bắt buộc; nó là cách người chơi học "ngôn ngữ lời thề" của vong linh.

### Objectives

- Đọc `STELE-01` (lời thề bảo vệ đất).
- Đọc `STELE-02` (lời thề với người sống sót).
- Đọc `STELE-03` (lời thề không tên - bia khắc chưa xong).
- Không chẻ bia nào để mở đường nhanh.

### Effects

- `Q_CH03_002_COMPLETE = true`.
- Trong boss encounter, ba bia giúp đọc trước nhịp "rễ trói" và giữ các nút rễ không bị Mộc Tinh thu hồi.
- Mở dialogue sâu của Hiến/Trưởng về việc lời thề từng là tự nguyện.
- Không tăng `mercy_marks` trực tiếp; quest chỉ cung cấp hiểu biết và giữ đường `released` mở.

## Q-CH03-003: Người chết có tên

### Unlock

Mở khi người chơi đọc ít nhất hai trong ba bia ở `CH-03-S03`.

### Bond objective

Không thuyết phục Mộc Tinh bằng lời. Người chơi phải hoàn thành ba hành động cho thấy mình không đến chỉ để lấy ngọc:

1. Gọi đúng tên Hiến (hoặc một vong linh) ít nhất một lần.
2. Không chẻ bia lời thề để mở đường nhanh.
3. Đứng lại nghe trọn lời thề của người chết ở `CH-03-S04` (`CH03_OATH_HEARD_FULL`).

### Completion condition for release

- `CH03_GAVE_NAME = true`.
- `CH03_STELES_INTACT >= 3` (hoặc ít nhất không phá bia để đi tắt).
- `CH03_OATH_HEARD_FULL = true`.
- Trong encounter, cắt/ giải thoát các nút rễ thay vì đốt sạch chúng.
- Đánh bại phase cuối mà không dùng `C-CH03-003: force_absorb`.

### Incomplete bond

Nếu thiếu một điều kiện, người chơi vẫn có thể nói đúng câu cần nói, nhưng nguyên thần không đồng thuận. Kết quả là `defeated_by_force`, không phải `released`.

### Sacrifice variant

Nếu người chơi đã xây đủ ân nghĩa với Hiến, ở `S05`/`B03` Hiến có thể tự hy sinh (`boss_fates[HIEN] = sacrificed`) để phá một vòng rễ cứu Long Nhân - mở một biến thể aftermath riêng, không thay `released` của Mộc Tinh.

## Q-CH03-004: Dấu móng trên bia

### Premise

Một vết móng đen trên bia không khớp với Mộc Tinh. Nó nằm gần một phù điêu đã bị cào mất phần đầu.

### Purpose

Gieo mồi rằng yêu khí có tác động chủ động lên ký ức, nhưng không giới thiệu tên Hỗn Mang quá sớm.

### Reward

- Lore fragment: "một bóng đen không hình hài kéo lời thề đi ngược về phía núi".
- Nếu hoàn thành, Tiếng Vọng ở `CH-03-B03-FATE` thêm một câu hỏi về "thứ đứng sau lời thề".
- Gieo mồi `LG-04`/CH-04 (bộ tộc bị ruồng bỏ, lông vũ).

## Q-CH03-00H: Gò mộ dưới rễ (hidden, ADR-004)

### Type / requirement

`hidden`, `required: false`. Mở khi tìm ra mộ cổ ở `CH-03-S03` và theo dấu rễ TỰ NGUYỆN (khác rễ ký sinh) tới `CH-03-HIDDEN`.

### Objective

Đối diện `HB-03` Tướng Quân Vô Đầu; đọc kiếm khắc lời thề để hiểu ông tự trói; quyết định giúp ông buông (gọi tên) hay cưỡng đoạt/hạ.

### Effects

| Lựa chọn | State |
|---|---|
| `released` | `CH03_HIDDEN_RELEASED`, `hidden_released +1`, `mercy_marks +1`; đào sâu `TRUTH_OLD_ARMY_WAS_BOUND` |
| `defeated_by_force` | không tăng `hidden_released`; mất một phần ký ức `S06` |
| `absorbed` | `dragon_hunger +1`, không tăng `hidden_released`; khóa đường E-04 trọn vẹn |

### Completion signal

Mộ yên, hàng nút rễ trung tâm buông, kiếm khắc tên chìm vào đất (released) - hoặc mộ sụp đen (absorbed).

## Choice registry

### `C-CH03-001`: Giải thoát hay giữ hàng ngũ (`CH-03-S02`)

| Lựa chọn | Người chơi biết | State | Feedback gần | Hậu quả xa |
|---|---|---|---|---|
| Giải thoát Hiến | Một vong linh còn ý chí, bị rễ cắm gáy | `CH03_RESCUED_HIEN`, `tribal_trust +1`, `mercy_marks +1` | Hiến tỉnh, dẫn đường, chỉ cách đọc nút rễ | Dễ đạt `released`; mở nhánh ân nghĩa/sacrifice |
| Giữ hàng ngũ | Rễ trói có thể mở đường nhanh hơn | `CH03_USED_OATHS`, `dragon_hunger +1` | Rừng mở lối nhanh, nhưng xác-rẽ ùa theo | Trưởng coi Long Nhân là "kẻ cầm dây mới"; khóa một phần bond |

### `C-CH03-002`: Lời thề của người chết (`CH-03-S04`)

| Lựa chọn | Ý định | State | Feedback |
|---|---|---|---|
| Nghe trọn, gọi tên | Công nhận họ là người, không phải công cụ | `CH03_OATH_HEARD_FULL`, `CH03_GAVE_NAME` | Vong linh lắng; Hiến/Trưởng đổi thái độ |
| Phán xét lời thề | Ưu tiên phá vòng, coi thề là xiềng | `CH03_OATH_JUDGED` | Trưởng đối đầu; mở đường nhanh hơn nhưng mất tin cậy |
| Im lặng/Thế Ngự | Quan sát trước khi cam kết | `CH03_OATH_OBSERVED` | Mở counterplay phản đòn rễ và line ký ức |

### `C-CH03-003`: Cách nhận nguyên thần (`CH-03-B03`, Fate resolution)

| Lựa chọn | Điều kiện | State | Ending signal |
|---|---|---|---|
| Tiếp nhận có chủ ý | Bond hoàn tất | `released`, `memory_recovered +1`, `mercy_marks +1`, `relics_purified +1` | Lõi đỏ dịu, rễ buông, `LG-03` sáng ấm |
| Cưỡng đoạt | Luôn có sau boss | `absorbed`, `dragon_hunger +1` | Vệt đen chạy dưới da; rừng rên; `LG-03` sáng lạnh |
| Không chạm | Boss đã hạ nhưng không release | `defeated_by_force` | Nguyên thần tự hòa vào ngọc; ký ức khuyết |

### `C-CH03-00H`: Tướng Quân Vô Đầu (`CH-03-HIDDEN`)

| Lựa chọn | Ý định | State | Feedback |
|---|---|---|---|
| Gọi tên, giúp buông | Trả danh tính cho chỉ huy | `CH03_HIDDEN_RELEASED`, `hidden_released +1`, `mercy_marks +1` | Mộ yên, nút rễ trung tâm buông |
| Cưỡng đoạt nguyên thần | Lấy sức mạnh | `dragon_hunger +1`, không tăng `hidden_released` | Kiếm khắc tên nứt; rừng siết chặt hơn |
| Hạ bằng vũ lực | Dẹp chướng ngại | không tăng `hidden_released` | Mộ sụp; mất một phần ký ức `S06` |

## Choice design rules for CH-03

- Không hiển thị nhãn "Mercy"/"Hunger" như điểm đạo đức; biểu hiện bằng fiction và hậu quả.
- Giải thoát Hiến không biến encounter thành dễ; nó chỉ cung cấp thông tin và một hỗ trợ đọc pattern.
- Giữ hàng ngũ không phải nhánh "ác"; nó là lựa chọn hợp lý nếu người chơi ưu tiên tốc độ/ngăn thảm họa, nhưng có cost thật (Long Nhân thành "kẻ cầm dây").
- Cưỡng đoạt không cho phần thưởng narrative giả tạo; game phải cho thấy sức mạnh có lợi ích thật và cost thật.
- Mỗi choice đủ năm trường: ý định, thông tin, hậu quả gần, hậu quả xa, tín hiệu phản hồi (02 §4).
