# CH-05 Quests and Choices

## Quest map

| ID | Loại | Tên | Bắt buộc | Tác động |
|---|---|---|---|---|
| `Q-CH05-001` | Main | Ngã ba không trọng tài | Có | Mở đường tới `LG-05` và boss `B-05` |
| `Q-CH05-002` | Optional | Hai tiếng, một ký ức | Không | Mở clue ký ức lệch; tăng `tribal_trust` một nhánh |
| `Q-CH05-003` | Bond | Nguồn nuôi xung đột | Có để `released` | Giải quyết bond của `LG-05` |
| `Q-CH05-004` | Exploration | Bậc đá trong bùn | Không | Gieo mồi Hỗn Mang và CH-06 |
| `Q-CH05-00H` | Hidden (ADR-004) | Người mẹ bị quên | Không | Mở `HB-05`; cộng `hidden_released` nếu giải thoát |

## Q-CH05-001: Ngã ba không trọng tài

### Intent

Đưa Long Nhân từ "người đi thu mảnh ngọc cuối" sang "kẻ bị cả hai phe muốn biến thành trọng tài — và phải từ chối vai đó". Quest không yêu cầu người chơi hiểu toàn bộ lore Hỗn Mang.

### Giver

Không có giver duy nhất. Quest tự mở khi Long Nhân tới Làng nổi ở `CH-05-S01` và nghe hai tiếng gọi.

### Steps

1. **Tới làng nổi:** quan sát cộng đồng kẹt giữa hai nhánh sông.
2. **Nghe hai tiếng gọi:** xác định mỗi giao đều tự nhận là người giữ ngọc.
3. **Vượt bè chiến:** đi qua `CH-05-S03` giữa hai luồng tấn công.
4. **Chạm mảnh ngọc:** chứng kiến `LG-05` lộ diện và hai giao bị ép hợp thể.
5. **Xử lý Song Giao:** kết thúc encounter `B-05` (hai giai đoạn).
6. **Rời ngã ba khi nước rút:** xác nhận hậu quả và mở bậc tế đàn.

### Completion

Quest hoàn thành khi `CH05_END_*` được ghi. Không hoàn thành chỉ bằng việc giảm HP hợp thể; phải ghi `boss_fates[B-05]`.

### Failure/cost

Không có game over narrative do chọn phe hay bỏ màn ẩn. Cost là thông tin, `tribal_trust`, telegraph arena và aftermath khác nhau. Người chơi không bị ép vào một "đáp án đạo đức đúng".

## Q-CH05-002: Hai tiếng, một ký ức

### Premise

Hai giao kể *cùng một ký ức* với chi tiết lệch nhau. Người chơi có thể thu cả hai lời kể và đối chiếu để nhận ra ký ức đã bị chỉnh sửa — bước đầu của `TRUTH_CONFLICT_WAS_FED`.

### Objectives

- Nghe lời kể của Giao Anh ở nhánh thượng.
- Nghe lời kể của Giao Em ở nhánh hạ.
- Đối chiếu hai dị bản trước `Ông Chài` hoặc tại miếu chìm (nếu đã mở màn ẩn).

### Effects

- `Q_CH05_002_COMPLETE = true`.
- Mở cờ `CH05_MEMORY_MISMATCH` (cần cho `released`).
- Trong boss encounter, người chơi nhận diện được khoảnh khắc hai giao "nhầm" nhau là anh em.
- Không tăng `mercy_marks` trực tiếp; quest chỉ cung cấp hiểu biết.

## Q-CH05-003: Nguồn nuôi xung đột

### Unlock

Mở khi người chơi chọn hướng "phá nguồn nước nuôi xung đột" ở `C-CH05-002`, hoặc đối chiếu đủ hai ký ức ở `Q-CH05-002`.

### Bond objective

Không thuyết phục hai giao bằng lời. Người chơi phải hoàn thành ba hành động cho thấy mình không đến để làm trọng tài hay chiếm ngọc:

1. Lội theo dòng phù sa đen tới điểm neo ký ức dưới ngã ba.
2. Không đẩy hai giao vào chỗ chết để thắng nhanh (tránh `dragon_hunger`).
3. Đứng lại nghe trọn ký ức của cả hai ở `CH-05-S02`/`S04`.

### Completion condition for release

- `CH05_MEMORY_MISMATCH = true`.
- `CH05_SOURCE_FOUND = true`.
- `CH05_BOSS_LISTENED = true`.
- Trong encounter, người chơi kích hoạt ít nhất hai neo ký ức thay vì phá chúng.
- Đánh bại `B05-B-MERGED` mà không dùng `C-CH05-003: force_absorb`.
- *(Lý tưởng, không bắt buộc tuyệt đối)* `HB-05 = released` để mở "nhớ lại mẹ" ngay trong trận.

### Incomplete bond

Nếu thiếu điều kiện, người chơi vẫn có thể nói đúng câu cần nói, nhưng hợp thể không tách ra. Kết quả là `defeated_by_force`, không phải `released`.

## Q-CH05-004: Bậc đá trong bùn

### Premise

Khi nước rút, một bậc tế đàn bằng đá lộ ra trong bùn, khắc hoa văn Đông Sơn, dẫn về phía Đỉnh Nghĩa Lĩnh.

### Purpose

Gieo mồi rằng có một nơi "tổng hợp" mọi ký ức đang chờ, và rằng xung đột ở ngã ba chỉ là một mạch của oán nghiệp lớn hơn; không giới thiệu tên Hỗn Mang quá sớm.

### Reward

- Lore fragment: "năm mảnh ngọc từng được đặt trên bậc đá này, bởi những bàn tay khác nhau, ở những thời khác nhau."
- Nếu hoàn thành, Tiếng Vọng Lạc Long ở `CH-05-S05` thêm một câu hỏi về "kẻ quyết định sau cùng".

## Q-CH05-00H: Người mẹ bị quên (hidden — ADR-004)

### Premise

Một miếu nhỏ chìm ở đáy ngã ba, thờ một người mẹ đã chia nước cho hai con rồi bị chính cuộc tranh chấp xé nát. Không thuộc tuyến chính.

### Objectives

- Đi theo dòng phù sa đen tới điểm neo cố định (gợi ý từ `S01`/`S03`).
- Vào `CH-05-HIDDEN`; nhận ra Giao Mẫu (`HB-05`).
- Quyết định cách đối xử với bà (`C-CH05-00H`).

### Effects

- `released`: `boss_fates[HB-05] = released`, `hidden_released +1`, `mercy_marks +1`; mở `CH05_HIDDEN_RELEASED`; trao "ký ức người mẹ" dùng được trong `B05-B`.
- `absorbed`/`defeated_by_force`: `boss_fates[HB-05]` tương ứng, `dragon_hunger +1`, KHÔNG tăng `hidden_released`.

### Purpose

Biến `TRUTH_CONFLICT_WAS_FED` từ clue thành sự thật sống: xung đột có một nạn nhân thứ ba bị cả hai bên quên. Đây là "hòa giải thật" của chương — không phải chọn phe thắng.

## Choice registry

### `C-CH05-001`: Nghe bên nào trước

| Lựa chọn | Người chơi biết | State | Feedback gần | Hậu quả xa |
|---|---|---|---|---|
| Nghe Giao Anh trước | Nhánh thượng sợ mất nguồn | `CH05_HEARD_ELDER_FIRST`; `tribal_trust +1` nếu bênh | Giao Anh bớt hung hăng tạm thời | Nhánh hạ giữ khoảng cách; thiếu một phần ký ức |
| Nghe Giao Em trước | Nhánh hạ sợ mất cửa biển | `CH05_HEARD_YOUNGER_FIRST`; `tribal_trust +1` nếu bênh | Giao Em bớt hung hăng tạm thời | Nhánh thượng giữ khoảng cách; thiếu một phần ký ức |
| Nghe cả hai, không bênh | Hai ký ức lệch nhau | `CH05_MEMORY_MISMATCH` | Cả hai đều hé một mảnh sự thật | Mở đường `released`; không tăng `tribal_trust` bên nào |

### `C-CH05-002`: Narrative gate — kích chiến hay phá nguồn

| Lựa chọn | Ý định | Thông tin trước chọn | State | Feedback gần | Hậu quả xa |
|---|---|---|---|---|---|
| Kích hai giao đánh nhau | Thắng nhanh, lợi dụng xung đột | Người chơi thấy chúng đang quần nhau | `dragon_hunger +1` nếu cố đẩy chúng vào chỗ chết; `CH05_PIT_FIGHT` | Hai giao tự làm yếu nhau; arena dễ thở hơn | Củng cố vòng tranh giành; khó `released`; không mở clue nguồn |
| Phá nguồn nước nuôi xung đột | Tìm gốc thay vì chọn phe | Người chơi thấy dòng phù sa đen quy về một điểm | `CH05_SOURCE_FOUND`; mở `TRUTH_CONFLICT_WAS_FED` (clue) | Mở lối xuống miếu chìm (`Q-CH05-00H`) | Dễ `released`; mở màn ẩn; arena khó hơn vì không có lợi thế |

### `C-CH05-003`: Cách nhận nguyên thần hợp thể

| Lựa chọn | Điều kiện | State | Ending signal |
|---|---|---|---|
| Tiếp nhận có chủ ý (released) | Bond hoàn tất (và lý tưởng `HB-05 released`) | `boss_fates[B-05]=released`, `memory_recovered +1`, `mercy_marks +1`, `relics_purified +1` | Hợp thể tách thành hai giao bơi song song; nước trong |
| Cưỡng đoạt (absorbed) | Luôn có sau khi hạ boss | `boss_fates[B-05]=absorbed`, `dragon_hunger +1` | Vệt đen dưới da; hai tiếng gọi im bặt |
| Không chạm (defeated_by_force) | Boss đã hạ nhưng không release | `boss_fates[B-05]=defeated_by_force` | Hợp thể tan thành hai dòng đục; ký ức khuyết |

### `C-CH05-00H`: Cách đối xử với Giao Mẫu (hidden)

| Lựa chọn | Ý định | State | Feedback |
|---|---|---|---|
| Nói thật bà đã bị quên | Công nhận nạn nhân thứ ba | `HB-05` hướng `released`; `CH05_MOTHER_REMEMBERED` | Giao Mẫu trao ký ức; hai giao sau này "nhớ mẹ" |
| Lợi dụng bà khống chế hai giao | Biến nỗi đau thành công cụ | `HB-05` hướng `absorbed`/`defeated_by_force`; `dragon_hunger +1` | Bà không chống cự, chỉ im lặng; mất chìa khóa hòa giải |

## Choice design rules for CH-05

- Không hiển thị nhãn "Đúng/Sai" hoặc "Hòa giải/Phá hoại" cho người chơi; biểu hiện bằng fiction và hậu quả.
- Kích hai giao đánh nhau không phải nhánh "ác"; nó là lựa chọn hợp lý nếu người chơi ưu tiên sống sót và chấm dứt nhanh — nhưng nó có giá phải trả về `released`.
- Nghe cả hai bên không tự động cho `released`; nó mở *khả năng*, vẫn cần hành động trong encounter.
- Cưỡng đoạt cho lợi ích sức mạnh cảm nhận ngay (Long Khí bùng), đồng thời gieo cost narrative rõ (hai tiếng gọi im bặt, làng sợ).
- Màn ẩn không bắt buộc nhưng là con đường duy nhất để "hòa giải thật" của chương và góp vào `hidden_released` cho E-04.
