# CH-04 Quests and Choices

## Quest map

| ID | Loại | Tên | Bắt buộc | Tác động |
|---|---|---|---|---|
| `Q-CH04-001` | Main | Phán quyết trên đỉnh Thạch Môn | Có | Mở đường lên tổ Đại Bàng và `LG-04` |
| `Q-CH04-002` | Optional | Những chiếc lông giữ hồn | Không | Dạy `Lôi Kích`/`Thế Đột`, mở lore, tăng telegraph đọc arena |
| `Q-CH04-003` | Bond | Lời kể của bộ tộc mất tên | Có để `released` | Giải quyết bond của `LG-04`, mở `TRUTH_EXILE_WAS_ERASED` |
| `Q-CH04-004` | Exploration | Bản đồ bộ tộc mất tên | Không | Gieo mồi Hỗn Mang + CH-05, mở màn ẩn `CH-04-HIDDEN` |
| `Q-CH04-00H` | Hidden/bond | Khe đá dựng | Không | Giải thoát `HB-04`, `hidden_released +1`, mở tên thật bộ tộc (ADR-004) |

## Q-CH04-001: Phán quyết trên đỉnh Thạch Môn

### Intent

Đưa Long Nhân từ "leo lên lấy ngọc" sang "quyết định ai có quyền được nhớ". Quest không yêu cầu người chơi hiểu toàn bộ lore triều đại.

### Giver

Không có giver duy nhất. Quest tự mở khi Long Nhân đặt chân lên `CH-04-S01` (Đường đá vỡ) sau khi rời CH-03.

### Steps

1. **Đường đá vỡ:** leo sườn Thạch Môn, nhận ra trọng lực và gió ở đây không bình thường.
2. **Hồn trong lông vũ:** quyết định số phận những hồn bị kết tinh (`C-CH04-001`).
3. **Bản đồ bộ tộc mất tên:** gặp Bà Lệ / Hồn Tướng Lưu Đày; chọn nghe lời kể hay săn boss (`C-CH04-002`).
4. **Phán quyết trên vực:** đối mặt Đại Bàng Tinh; chọn cách gọi nó (`C-CH04-003`).
5. **Xử lý Đại Bàng:** kết thúc encounter `B-04`.
6. **Lệ đá rơi xuống mây:** chọn cách nhận nguyên thần/`LG-04` (`C-CH04-004`); nhận reveal Lạc Long Quân.

### Completion

Quest hoàn thành khi `CH04_END_*` được ghi. Không hoàn thành chỉ bằng việc giảm HP Đại Bàng; phải ghi `boss_fates[B-04]`.

### Failure/cost

Không có game over narrative do chọn force path. Cost là thông tin, `tribal_trust`, telegraph arena, và mức trọn vẹn của `released`/`E-04` về sau. Người chơi không bị ép vào một "đáp án đạo đức đúng".

## Q-CH04-002: Những chiếc lông giữ hồn

### Premise

Những hồn người bị yêu khí kết tinh quanh lông Đại Bàng, treo trên các bệ đá. Chúng không phải chìa khóa bắt buộc; chúng là cách người chơi học "ngôn ngữ" của đỉnh núi (đứt gãy trọng lực, gió đổi hướng) và nghe lỏm ký ức bộ tộc.

### Objectives

- Tìm ba cụm "lông giữ hồn" trên đường leo (`FEATHER-01`, `FEATHER-02`, `FEATHER-03`).
- Với mỗi cụm: chọn đánh thức hồn bằng `Lôi Kích` (giải thoát) hoặc cắt lấy gân yêu khí làm lợi thế (lợi dụng).
- Đặt ba "mảnh ký ức" vào bia dẫn ở `CH-04-S03`.

### Effects

- `Q_CH04_002_COMPLETE = true`.
- Trong boss encounter, hồn được giải thoát **không** hóa thành "mưa lông" gây hại; ngược lại hồn bị lợi dụng sẽ chống người chơi ở `B04-P2`.
- Mở dialogue của Bà Lệ về việc triều đại từng "dọn" cả người sống lẫn người chết.
- Giải thoát hồn: `mercy_marks +1` (tối đa một lần cho cả quest, tránh farm). Lợi dụng hồn: `dragon_hunger +1`.

## Q-CH04-003: Lời kể của bộ tộc mất tên

### Unlock

Mở khi người chơi chọn **nghe lời kể** ở `C-CH04-002`, hoặc đọc đủ ba bia ở `CH-04-S03`.

### Bond objective

Không thuyết phục Đại Bàng bằng lời. Người chơi phải hoàn thành ba hành động cho thấy mình không đến chỉ để lấy ngọc:

1. Nghe trọn lời kể của Bà Lệ (và/hoặc Hồn Tướng Lưu Đày) ở `CH-04-S03`.
2. Không đục/không cưỡng đoạt bia để mở đường nhanh lên tổ.
3. Ở `CH-04-S04`, **gọi tên tội lỗi** của việc xóa tên thay vì kết án con chim (`C-CH04-003`).

### Completion condition for release

- `CH04_TESTIMONY_HEARD = true`.
- `CH04_STELES_READ >= 3`.
- `CH04_BOSS_NAMED_CRIME = true`.
- Trong encounter, kích hoạt ít nhất hai "bia tên" thay vì phá chúng.
- Đánh bại phase cuối mà không dùng `C-CH04-004: force_absorb`.

### Incomplete bond

Nếu thiếu một điều kiện, người chơi vẫn có thể nói đúng câu cần nói, nhưng nguyên thần không đồng thuận. Kết quả là `defeated_by_force`, không phải `released`.

## Q-CH04-004: Bản đồ bộ tộc mất tên

### Premise

Những bia không tên xếp thành một "bản đồ" khi nhìn từ đúng góc; mỗi bia là một bộ tộc bị xóa. Vết móng đen không khớp với Đại Bàng xuất hiện trên bia đã bị đục (dấu Hỗn Mang).

### Purpose

Gieo mồi rằng yêu khí có tác động **chủ động** lên ký ức (đục tên), và dẫn tới màn ẩn `CH-04-HIDDEN` (tên thật nằm ở khe đá dựng, không nằm ở bia công khai). Không giới thiệu tên Hỗn Mang quá sớm.

### Reward

- Lore fragment: "một bóng không hình hài đã đục tên khỏi bia trước cả khi triều đại kịp làm".
- Mở đường vào `CH-04-HIDDEN` (khi `tribal_trust >= 1` hoặc đã nghe lời kể).
- Nếu hoàn thành, Tiếng Vọng Lạc Long ở `CH-04-S05` thêm một câu hỏi về "thứ đứng sau nỗi phẫn nộ".

## Q-CH04-00H: Khe đá dựng (màn ẩn)

### Unlock

Tùy chọn. Mở khi người chơi nhận ra dãy bia không tên **thiếu đúng một tên**, và tìm được khe đá dựng sau thác lệ đá (`CH-04-HIDDEN`).

### Objective

Đối mặt `HB-04` Tù Trưởng Lệ Đá (phi combat). Nghe lời trăn của nhân chứng cuối, rồi **khắc/đọc lại đúng tên bộ tộc** (`C-CH04-00H`).

### Effects

- Giải thoát (`released`): `CH04_HIDDEN_RELEASED`, `hidden_released +1`, `mercy_marks +1`; mở `hidden_truth`: *tên bộ tộc bị xóa có chủ đích bởi triều đại "thống nhất", không phải do thời gian* (đào sâu `TRUTH_EXILE_WAS_ERASED`); cộng hưởng bond giúp `released` của `B-04` dễ đạt hơn (vẫn cần hành động).
- Cưỡng đoạt/hạ (`absorbed`/`defeated_by_force`): `dragon_hunger +1`, **không** tăng `hidden_released`; đỉnh núi khóc dữ hơn.
- Không có `LG` hay vũ khí mới từ `HB-04` (ADR-004).

## Choice registry

### `C-CH04-001`: Hồn trong lông vũ (S02)

| Lựa chọn | Ý định | Thông tin người chơi biết | State (hậu quả gần) | Hậu quả xa | Tín hiệu phản hồi |
|---|---|---|---|---|---|
| Giải thoát hồn | Thương cảm, chấp nhận chậm | Hồn bị nhốt, không phải quái | `mercy_marks +1`, `CH04_SOULS_FREED` | Hồn không hóa "mưa lông" ở `B04-P2`; `tribal_trust` dễ tăng | Lông rụng, một khuôn mặt briefly hiện ra rồi tan; gió lặng một nhịp |
| Lợi dụng hồn | Ưu tiên sức mạnh/tốc độ | Gân yêu khí trong lông là "nhiên liệu" | `dragon_hunger +1`, `CH04_SOULS_USED` | Hồn chống người chơi ở `B04-P2`; Bà Lệ im lặng | Gân lông cháy đen bám lên rìu; Long Khí mạnh hơn nhưng nhiễu |

### `C-CH04-002`: Cổng narrative - săn hay nghe (S03)

| Lựa chọn | Ý định | Thông tin người chơi biết | State (hậu quả gần) | Hậu quả xa | Tín hiệu phản hồi |
|---|---|---|---|---|---|
| Nghe lời kể bộ tộc | Điều tra, tôn trọng nhân chứng | Đại Bàng là vật chứa phẫn nộ, không phải nguồn ác | `CH04_TESTIMONY_HEARD`, mở bond path | Mở `released`, mở màn ẩn, `tribal_trust +1` | Bà Lệ trải "bản đồ" bằng lệ đá; bia sáng tên mờ |
| Săn boss lấy ngọc | Dứt điểm mối đe dọa ngay | Boss đang giữ `LG-04` và làm núi sụp | `CH04_HUNT_PATH` | Force path; bond khó/`released` gần như khóa; vẫn thắng được | Đường tắt lên tổ mở; Đại Bàng coi Long Nhân là "kẻ cai trị mới" |

### `C-CH04-003`: Phán quyết trên vực (S04)

| Lựa chọn | Ý định | Thông tin người chơi biết | State (hậu quả gần) | Hậu quả xa | Tín hiệu phản hồi |
|---|---|---|---|---|---|
| Gọi tên tội lỗi | Công nhận việc xóa tên là tội có chủ đích | Triều đại đã xóa tên, Đại Bàng chỉ hứng phẫn nộ | `CH04_BOSS_NAMED_CRIME` | Mở đường điều tra trong boss fight; dễ `released` | Đại Bàng khựng một nhịp; nhiều giọng trong lông im lặng lắng nghe |
| Kết án Đại Bàng | Phán xét hành vi trước mắt | Nó giam hồn, làm núi sụp | `CH04_BOSS_CONDEMNED` | Boss vào `B04-P1` ngay; `released` cần điều kiện khó hơn | Đại Bàng bổ nhào; gió rít; phẫn nộ dồn thành một giọng |
| Im lặng, giữ Thế Ngự | Quan sát trước khi cam kết | Chưa đủ dữ kiện để phán xử | `CH04_BOSS_HEARD` | Mở counterplay phản đòn + line ký ức; không khóa gì | Sương lắng; một hồn trong lông cất tiếng thay boss |

### `C-CH04-004`: Cách nhận nguyên thần (S05/B04)

| Lựa chọn | Ý định | Điều kiện | State | Ending signal |
|---|---|---|---|---|
| Tiếp nhận có chủ ý | Mang ký ức đi, không sở hữu | Bond hoàn tất | `boss_fates[B-04]=released`, `memory_recovered +1`, `mercy_marks +1`, `relics_purified +1`, `TRUTH_EXILE_WAS_ERASED` | Lệ đá trong lại; một tên được đọc; ngọc sáng ấm |
| Cưỡng đoạt | Lấy sức mạnh phẫn nộ | Luôn có sau khi hạ boss | `boss_fates[B-04]=absorbed`, `dragon_hunger +1` | Nhiều giọng gào tắt dần dưới da; ngọc sáng lạnh |
| Không chạm | Từ chối cả hai | Boss đã hạ, không release | `boss_fates[B-04]=defeated_by_force` | Nguyên thần hòa vào `LG-04` không thanh tẩy; ký ức khuyết một tên |

### `C-CH04-00H`: Khắc lại tên (HIDDEN)

| Lựa chọn | Ý định | State | Tín hiệu phản hồi |
|---|---|---|---|
| Khắc/đọc tên bộ tộc | Trả danh tính cho nhân chứng cuối | `boss_fates[HB-04]=released`, `hidden_released +1`, `mercy_marks +1`, `CH04_HIDDEN_RELEASED` | Tù Trưởng Lệ Đá thôi khóc; bia trong khe hiện tên; núi lặng một nhịp |
| Cưỡng đoạt lệ đá | Lấy "nước mắt hóa đá" làm sức mạnh | `boss_fates[HB-04]=absorbed`, `dragon_hunger +1` | Lệ đá vỡ vụn; tên bộ tộc mất vĩnh viễn; đỉnh núi khóc dữ hơn |

## Choice design rules for CH-04

- Không hiển thị nhãn "Mercy"/"Hunger" như điểm đạo đức; biểu hiện bằng fiction (lệ đá, bia tên, gió) và hậu quả.
- Force path không phải nhánh "ác"; nó hợp lý nếu người chơi ưu tiên ngăn đỉnh núi sụp ngay. Nhưng nó **đóng** phần lớn đường `released` và `E-04`.
- Cứu hồn không biến encounter thành dễ; nó chỉ đổi cách `B04-P2` phản ứng và cung cấp hiểu biết.
- Cưỡng đoạt cho lợi ích cảm nhận ngay (Long Khí mạnh hơn) kèm cost narrative rõ (núi khóc, hồn chống lại, khóa hòa giải).
- `C-CH04-002` là cổng trục: nó quyết định phần lớn `tribal_trust`/bond của chương, nhưng không khóa cứng ending — người chơi force path vẫn có thể chuộc lại một phần ở các chương sau (không đủ cho `E-04` nếu bỏ `hidden_released`).
