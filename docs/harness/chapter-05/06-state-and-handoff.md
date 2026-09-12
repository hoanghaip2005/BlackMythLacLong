# CH-05 State and Handoff

## Initial state

```yaml
chapter: CH-05
location: nga_ba_hac_flood
weapon: riu_than_thach_son
long_ngoc: [LG-01, LG-02, LG-03, LG-04]   # LG-05 chưa thu; đây là mảnh cuối
variables:
  memory_recovered: <=4      # carried from CH-01..04; CH-05 có thể đưa lên 5
  mercy_marks: carried
  tribal_trust: carried
  dragon_hunger: carried
  relics_purified: <=4
  hidden_released: <=4       # carried từ boss ẩn CH-01..04
flags:
  - CH05_STARTED
  - LONG_NHAN_UNNAMED        # vẫn chưa có tên thật
boss_fates: {}               # B-05 chưa ghi
final_decision: null
```

> Giá trị "carried" là trạng thái kế thừa từ CH-01..04; CH-05 không reset. Mọi biến clamp trong miền đã khai báo (`02-branching §2`), không âm thầm wrap.

## Required flags

| Flag | Set at | Meaning |
|---|---|---|
| `CH05_STARTED` | S01 | Chương bắt đầu |
| `LONG_NHAN_UNNAMED` | carried | Danh tính Long Nhân vẫn mở |
| `CH05_VILLAGE_TRUSTED` | S01 | Làng nổi chịu nói thật cả hai phía |
| `CH05_HEARD_GIAO_ANH` | S02 | Nghe ký ức Giao Anh |
| `CH05_HEARD_GIAO_EM` | S02 | Nghe ký ức Giao Em |
| `CH05_MEMORY_MISMATCH` | S02 | Thấy hai ký ức cùng một ngày không khớp |
| `CH05_PITTED` | S03/B05-A | Người chơi kích hai giao đánh nhau |
| `CH05_SOURCE_CUT` | S03/B05-A | Người chơi phá điểm phù sa nuôi xung đột |
| `CH05_ANCHOR_1_ACTIVE` | B05-A | Neo ký ức 1 kích hoạt |
| `CH05_ANCHOR_2_ACTIVE` | B05-A | Neo ký ức 2 kích hoạt |
| `CH05_ANCHOR_3_ACTIVE` | B05-B | Neo ký ức 3 (bàn tay chia nước) kích hoạt |
| `CH05_BOSS_NAMED_WOUND` | S04/B05 | Gọi đúng tên nỗi đau ("các ngươi bị lừa") |
| `CH05_BOSS_PITTED` | B05-A | Boss ưu tiên đánh nhau hơn đánh người chơi |
| `Q_CH05_002_COMPLETE` | S02 | Quest tùy chọn "Hai tiếng, một ký ức" xong |
| `Q_CH05_003_COMPLETE` | S04/B05 | Bond LG-05 hoàn tất (điều kiện `released`) |
| `Q_CH05_00H_COMPLETE` | CH-05-HIDDEN | Quest ẩn "Người mẹ bị quên" xong |
| `CH05_MOTHER_REMEMBERED` | CH-05-HIDDEN | Giao Mẫu được giải thoát; hai giao nhớ lại mẹ |
| `CH05_HIDDEN_RELEASED` | CH-05-HIDDEN | `hidden_released +1` (boss ẩn released) |
| `TRUTH_CONFLICT_WAS_FED` | S04 (seed) / B05 (confirm) | Sự thật: xung đột bị nuôi bởi nỗi đau thứ ba |
| `CH05_END_RELEASED` | B05-B | Hợp thể được giải thoát |
| `CH05_END_FORCE` | B05-B | Hợp thể bị hạ bằng sức mạnh |
| `CH05_END_ABSORBED` | B05-B | Nguyên thần hợp thể bị cưỡng đoạt |
| `LG05_ACQUIRED` | B05-B | Mảnh ngọc thứ năm (cuối) thu được |
| `CH05_COMPLETE` | S05 | Chương hoàn thành; mở đường CH-06 |

## State transition matrix

| Event | Variables | Flags | Player-facing feedback |
|---|---|---|---|
| Vào làng nổi, không chọn phe | none | `CH05_STARTED` | Hai cột nước lộ diện ở hai nhánh |
| Giúp làng giữa lũ | `tribal_trust +1` | `CH05_VILLAGE_TRUSTED` | Ông Chài kể chuyện "hồi còn một mẹ" |
| Nghe cả hai ký ức | none | `CH05_HEARD_GIAO_ANH/EM`, `CH05_MEMORY_MISMATCH` | Hai câu chuyện cùng một ngày không khớp |
| Kích hai giao đánh nhau (`C-CH05-002 pit`) | none (hunger chỉ nếu đẩy tới chết) | `CH05_PITTED`, `CH05_BOSS_PITTED` | Hai giao quên người chơi, lao vào nhau |
| Phá điểm phù sa (`C-CH05-002 cut`) | none | `CH05_SOURCE_CUT` | Phù sa đen loãng; lộ "thứ nuôi" không thuộc hai giao |
| Kích neo ký ức | none | `CH05_ANCHOR_*` | Chuông nước / ký ức hai giao con / bàn tay chia nước |
| Giải thoát Giao Mẫu (`C-CH05-00H release`) | `hidden_released +1`, `mercy_marks +1` | `CH05_HIDDEN_RELEASED`, `CH05_MOTHER_REMEMBERED`, `Q_CH05_00H_COMPLETE` | Miếu trong lại; hai giao (dù đang hợp thể) khựng một nhịp |
| Cưỡng đoạt Giao Mẫu (`C-CH05-00H absorb`) | `dragon_hunger +1` | (không set `CH05_HIDDEN_RELEASED`) | Miếu tối; mất chìa khóa hòa giải thật của chương |
| Release hợp thể B-05 | `memory_recovered +1`, `mercy_marks +1`, `relics_purified +1` | `CH05_END_RELEASED`, `LG05_ACQUIRED`, `TRUTH_CONFLICT_WAS_FED` | Hai giao tách, nhận ra nhau; ngọc sáng ấm |
| Hạ hợp thể bằng sức mạnh | none | `CH05_END_FORCE`, `LG05_ACQUIRED` | Ngọc sáng lạnh; hai dòng đục không nhận nhau |
| Absorb hợp thể | `dragon_hunger +1` | `CH05_END_ABSORBED`, `LG05_ACQUIRED` | Vệt đen dưới da; hai tiếng cãi trong đầu Long Nhân |
| Nước rút, lộ bậc tế đàn | none | `CH05_COMPLETE` | Đủ 5 ngọc sáng cùng nhịp; đường lên Nghĩa Lĩnh mở |

## State invariants

- `LG-05` chỉ được thu **đúng một lần**; sau CH-05 người chơi có **đủ năm mảnh** (`LG-01..LG-05`). Không tồn tại mảnh thứ sáu.
- Chỉ **một** trong `CH05_END_RELEASED`, `CH05_END_FORCE`, `CH05_END_ABSORBED` được true.
- `CH05_END_RELEASED` đòi hoàn tất bond (đủ neo + nghe cả hai + `CH05_BOSS_NAMED_WOUND`); không đến từ một câu thoại đơn lẻ.
- `hidden_released` tăng **tối đa 1** trong CH-05, và **chỉ** khi `HB-05` được `released`.
- `memory_recovered` tăng **tối đa 1** trong CH-05 (từ `released` của B-05); boss ẩn không tăng `memory_recovered` (theo ADR-004, hidden truth đào sâu truth flag, không phải mảnh ký ức chính).
- `relics_purified` chỉ tăng khi `released`, không tăng ở force/absorb.
- `dragon_hunger` không giảm trong CH-05.
- `TRUTH_CONFLICT_WAS_FED` là clue/flag sau CH-05; proof đầy đủ của "Hỗn Mang nuôi xung đột" chỉ hoàn tất ở CH-06.
- Rìu Thần Thạch Sơn và các ability (Thủy Ảnh, ba Thế, Lôi Kích, Phân Thân, Long Khí, Chân Long) đã khả dụng từ các chương trước; CH-05 không mở vũ khí định mệnh mới.

## Handoff: gameplay

### Required experience

- Combat trên **bè gỗ trôi** giữa ngã ba lũ; nền đứng tạm, đổi vị trí theo dòng.
- Arena **hai boss đồng thời** (phase A): đọc hai luồng nước, đứng giữa, dẫn đòn để hai giao va nhau.
- **Transformation beat** cưỡng ép (A→B) phải đọc được là "bị ép hợp thể", không phải power-up.
- Phase B **một boss hợp thể** lớn hơn, có cửa sổ "hai ý chí cãi nhau" để phản đòn.
- `Thủy Ảnh` thành thạo (mở từ CH-01) dùng như hình ảnh "không kẹt về phe nào" khi hai luồng chồng.
- `Thế Ngự` gắn chủ đề "nghe cả hai bên": phản đòn để một giao nói hết câu, mở ký ức.
- Ba neo ký ức trong arena; kích neo thay vì phá chúng.
- **Màn ẩn `CH-05-HIDDEN`**: một encounter tĩnh (Giao Mẫu), gần như không cần đánh; chiến thắng là "nói thật".
- Boss phải hỗ trợ cả đường force victory và đường release.

### Explicitly deferred

- Damage, health, stamina, resource numbers.
- Hitbox/frame data; physics của bè trôi và dòng chảy.
- Save serialization; cách lưu `hidden_released` và `boss_fates` runtime.
- Behavior-tree của hai boss AI phối hợp/va chạm.

## Handoff: art

- **Hai giao = thuồng luồng/giao long bản địa**: thân rắn nước lớn, vảy phù sa, vây lưng thấp, đầu thuồng luồng. **Không** rồng Trung Hoa (không bốn móng, không mây cuộn, không long văn cung đình, không râu bờm).
- Hai giao phân biệt bằng silhouette (Giao Anh sẹo mạn sườn, Giao Em đuôi chẻ) trước khi phân biệt bằng màu.
- **Hợp thể Hắc Giao Long**: hai thân xoắn, phù sa đen bọc như lớp da thứ hai, hai mắt lệch nhịp — đọc được là *cưỡng ép*, đau.
- **Giao Mẫu (HB-05)**: trong mờ, lắng, hiền; đối lập thị giác với hợp thể đen.
- Nước phù sa: hai luồng đen (Giao Anh) và đục (Giao Em); điểm "nuôi xung đột" đen quy tụ, không thuộc con nào.
- Bậc tế đàn lộ ra khi nước rút: đá Đông Sơn tối giản, dẫn mắt lên cao (hướng Nghĩa Lĩnh).
- `LG-05` là vật chứng ký ức, không phải chiến lợi phẩm phát sáng.

## Handoff: audio

- Nền lũ: nước chảy, bè va, gỗ rên; khoảng lặng cho thoại.
- **Hai giọng giao** đối nhau (một trầm khăng khăng, một cao uất ức), đến từ hai hướng stereo.
- Hợp thể: hai giọng chồng, lệch nhịp, có lúc cãi nhau trong một cổ họng.
- Giao Mẫu: giọng người mẹ mệt, gần, không vọng; đối lập với tiếng vọng méo của hai giao.
- Transformation beat: tiếng nước bị ép, không phải stinger "power-up" hào hùng.
- Release: hai tiếng giao hòa thành một rồi tách; nước trong dần.
- Absorb: xung tần số thấp dưới thoại, không "evil sting" to.

## Handoff: localization

- Giữ glossary: `Long Nhân`, `Long Ngọc`, `Long Khí`, `Song Giao`, `Hắc Giao Long`, `Giao Mẫu`, `Thủy Ảnh`, `Thế Ngự`, `Rìu Thần Thạch Sơn`, `Ngã Ba Hạc`, `Nghĩa Lĩnh`.
- "Giao" = thuồng luồng/giao long bản địa; **không** dịch thành "dragon" theo nghĩa rồng Trung Hoa; ưu tiên "water-serpent/giao" có chú giải.
- Phân biệt rõ **"tự vệ"** (cả hai giao tin vậy) và **"xâm lược"** (không bên nào là xâm lược tuyệt đối) — đây là lõi theme.
- Phân biệt **"bị bóp méo ký ức"** (nạn nhân) và **"nói dối"** (chủ ý) — hai giao là nạn nhân.
- `Ngã Ba Hạc` là địa danh cảm hứng; tách lớp lịch sử hư cấu khỏi địa danh thật (theo `01-story-bible §11`).
- Thoại hai giao ngắn để đọc giữa combat; thoại Giao Mẫu và reveal cần cinematic subtitle budget.
