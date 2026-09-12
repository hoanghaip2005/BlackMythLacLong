# CH-04 State and Handoff

## Initial state

```yaml
chapter: CH-04
location: thach_mon_foothold
weapon: thach_son_axe        # Rìu Thần Thạch Sơn đã thức tỉnh từ CH-01
long_ngoc: [LG-01, LG-02, LG-03]   # kế thừa từ CH-01..03 (LG-04 chưa thu)
variables:
  memory_recovered: carry_over   # 0..3 tùy CH-01..03
  mercy_marks: carry_over
  tribal_trust: carry_over
  dragon_hunger: carry_over
  relics_purified: carry_over
  hidden_released: carry_over    # 0..3 tùy boss ẩn CH-01..03
flags:
  - CH04_STARTED
boss_fates: {}                   # B-04, HB-04 chưa ghi
final_decision: null
```

> `carry_over` nghĩa là giá trị được giữ nguyên từ cuối CH-03 (không reset). CH-04 chỉ **tăng** các biến này theo hành động trong chương; không âm thầm wrap hoặc reset (02 §2).

## Required flags

| Flag | Set at | Meaning |
|---|---|---|
| `CH04_STARTED` | S01 | Chương bắt đầu |
| `CH04_SOULS_FREE` | S02 | Người chơi giải thoát hồn trong lông vũ |
| `CH04_SOULS_USED` | S02 | Người chơi lợi dụng hồn làm mồi/vũ khí |
| `CH04_MAP_PIECES_1` | S03 | Ghép mảnh bản đồ bộ tộc thứ nhất |
| `CH04_MAP_PIECES_2` | S03 | Ghép mảnh bản đồ bộ tộc thứ hai |
| `CH04_MAP_PIECES_3` | S03 | Ghép đủ ba mảnh bản đồ |
| `CH04_HEARD_TESTIMONY` | S03/S04 | Đã nghe trọn lời kể bộ tộc (đường bond) |
| `CH04_NAMED_CRIME` | S04 | Người chơi gọi tên tội lỗi triều đại |
| `CH04_CONDEMNED` | S04 | Người chơi kết án Đại Bàng là quái vật |
| `CH04_OBSERVED` | S04 | Người chơi im lặng giữ Thế Ngự |
| `CH04_NEST_1_ACTIVE` | B04 | Neo bia/lông thứ nhất kích hoạt |
| `CH04_NEST_2_ACTIVE` | B04 | Neo bia/lông thứ hai kích hoạt |
| `CH04_NEST_3_ACTIVE` | B04 | Neo bia/lông thứ ba kích hoạt |
| `TRUTH_EXILE_WAS_ERASED` | S03 (seed) → S05 (confirm) | Sự thật về việc xóa tên |
| `Q_CH04_002_COMPLETE` | Optional | Hồn trong lông vũ được xử lý |
| `Q_CH04_003_COMPLETE` | S03/S04 | Bond "lời kể bộ tộc" hoàn tất |
| `Q_CH04_004_COMPLETE` | Optional | Bản đồ bộ tộc mất tên hoàn tất (gợi mở hidden) |
| `CH04_HIDDEN_RELEASED` | HIDDEN | Giải thoát HB-04 (khắc lại tên bộ tộc) |
| `Q_CH04_00H_COMPLETE` | HIDDEN | Quest ẩn hoàn tất (release hoặc absorb) |
| `CH04_END_RELEASED` | S05 | Đại Bàng Tinh được giải thoát |
| `CH04_END_FORCE` | S05 | Đại Bàng Tinh bị hạ bằng sức mạnh |
| `CH04_END_ABSORBED` | S05 | Người chơi cưỡng đoạt nguyên thần |
| `CH04_COMPLETE` | S05 | Chương hoàn tất |

## State transition matrix

| Event | Variables | Flags | Player-facing feedback |
|---|---|---|---|
| Đến chân Thạch Môn | none | `CH04_STARTED` | Sương lạnh, lệ đá rỉ từ vách, gió đổi hướng |
| Giải thoát hồn trong lông | `mercy_marks +1`, `tribal_trust +1` | `CH04_SOULS_FREE` | Lông hóa bia sáng; hồn thì thầm một tên |
| Lợi dụng hồn làm mồi | `dragon_hunger +1` | `CH04_SOULS_USED` | Hồn gào méo mó; phase 2 thêm mối nguy phụ |
| Ghép đủ 3 mảnh bản đồ | none | `CH04_MAP_PIECES_3` | Mở lời kể bộ tộc + gợi ý khe đá dựng (hidden) |
| Nghe lời kể bộ tộc | none (mở bond) | `CH04_HEARD_TESTIMONY` | `TRUTH_EXILE_WAS_ERASED` thành clue rõ |
| Gọi tên tội lỗi triều đại | none | `CH04_NAMED_CRIME` | Boss khựng một nhịp; bia sáng |
| Kết án Đại Bàng | none | `CH04_CONDEMNED` | Boss vào phase 1 ngay; ưu tiên phá bia |
| Kích hoạt bia/lông | none | `CH04_NEST_*` | Ký ức khắc-tên hiện; vùng an toàn mở |
| Giải thoát HB-04 (khắc tên) | `hidden_released +1`, `mercy_marks +1` | `CH04_HIDDEN_RELEASED`, `Q_CH04_00H_COMPLETE` | Lệ đá ngừng rơi; tên bộ tộc sáng; ấm |
| Cưỡng đoạt lệ đá HB-04 | `dragon_hunger +1` | `Q_CH04_00H_COMPLETE` | Lệ hóa vật dẫn Long Khí; tên mờ vĩnh viễn; lạnh |
| Release Đại Bàng | `memory_recovered +1`, `mercy_marks +1`, `relics_purified +1` | `CH04_END_RELEASED` | Đàn lông sáng tan; gió lặng; ngọc ấm |
| Hạ bằng sức mạnh | none | `CH04_END_FORCE` | Ngọc lạnh; một cái tên mất tiếng ở CH-06 |
| Cưỡng đoạt nguyên thần | `dragon_hunger +1` | `CH04_END_ABSORBED` | Vệt đen/nhiều giọng dưới da |
| Rời đỉnh | none | `CH04_COMPLETE`, `LG04_ACQUIRED` | Lệ đá rơi xuống mây; hook nước/lũ về CH-05 |

## State invariants

- `LG-04` is acquired exactly once.
- Only one of `CH04_END_RELEASED`, `CH04_END_FORCE`, `CH04_END_ABSORBED` may be true.
- `CH04_END_RELEASED` implies the bond was completed (`CH04_HEARD_TESTIMONY` + `CH04_NAMED_CRIME` + ít nhất hai `CH04_NEST_*`); it never appears from dialogue alone.
- `memory_recovered` increases at most once in CH-04.
- `relics_purified` increases only on release, never on force or absorption.
- `hidden_released` increases at most once in CH-04, and only when `HB-04` is released.
- Rìu Thần Thạch Sơn is **already available** in CH-04 (awakened in CH-01); CH-04 never re-introduces it as new.
- `dragon_hunger` cannot decrease during CH-04.
- `TRUTH_EXILE_WAS_ERASED` is seeded in CH-04 and confirmed before CH-06; it is not a complete global proof until the final altar.
- Đại Bàng Tinh is never confirmed as "dead" before `boss_fates[B-04]` is recorded.

## Handoff: gameplay

### Required experience

- **Verticality:** leo/bám giữa các mỏm đá và bệ hẹp; rơi có trọng lượng.
- **Gió đổi hướng:** một hệ gió đọc được bằng hình ảnh (cờ, sương, đá vụn) đẩy người chơi và đổi đà né.
- **Đứt gãy trọng lực:** vùng trọng lực nhẹ/nặng/đảo xuất hiện theo nhịp boss; đá và lệ đá trôi nổi.
- **Đòn bổ nhào:** telegraph rõ (cánh gập, đầu chúi) trước mỗi cú sà; có cửa né/phanh.
- Stance hooks, introduced contextually:
  - `Thế Đột`: đâm vùng ức/cổ lộ `LG-04` sau khi boss hụt đà bổ nhào (chấp nhận rủi ro trên bệ hẹp).
  - `Thế Ngự`: phản đòn vuốt quét / giữ trụ trước gió.
  - `Thế Trảm`: dọn lông/bóng quanh bệ.
- `Lôi Kích`: ngắt một lần bổ nhào/hút vực; "đánh thức" ký ức trong lông (một khoảnh khắc ngắt nhịp quyền lực).
- `Nguyên thần Tinh Vượn` (nếu đã mở ở encounter phụ): leo bám/đánh lạc hướng giữa các mỏm — tùy chọn, không bắt buộc.
- `Phân Thân` (nếu đã mở): ảo ảnh đất sét đánh lạc hướng một nhịp ở phase 2.
- Arena phải hỗ trợ **một đường thắng không cần release** và **một đường release không cần perfect combat**.
- Hidden encounter `HB-04` phải hoàn thành được **không cần giao chiến** (lắng nghe/khắc tên).

### Explicitly deferred

- Damage, health, stamina, resource numbers.
- Hitbox/frame data; exact gravity/wind tuning values.
- Save serialization implementation.
- Exact climbing/fall controller and wind-field technology.

## Handoff: art

- **Đại Bàng Tinh (`B-04`):** chim lớn bi kịch, vật chứa phẫn nộ; lông cắm mảnh bia vụn và dây buộc cũ; **không** mào phượng, vảy rồng, đại bàng huy chương hay ornament cung đình Trung/Nhật.
- **Hai silhouette phase:** "cánh lưu đày" (một con chim có chủ ý) và "vật chứa" (đàn lông nhiều bóng người) phải đọc khác nhau.
- **Hồn trong lông vũ:** mỗi chiếc lông lớn là một hồn; phát sáng khi được giải thoát, méo mó khi bị lợi dụng.
- **Bia không tên / lệ đá:** dãy bia mờ dần (đồng hồ tự nhiên của hidden encounter); lệ đá chảy ngược khi trọng lực đứt gãy.
- **Tù Trưởng Lệ Đá (`HB-04`):** tù trưởng hóa đá, khóe mắt rỉ lệ đá; trang phục/vật liệu bộ tộc miền núi, không giáp cung đình.
- **Long Ngọc `LG-04`:** xuất hiện như vật chứng ký ức (ấm) ở lõi vật chứa, không phải loot gem.
- Môi trường: sương đỉnh, vách đá dựng, mây dưới chân; bảng màu đá/sương/lông vũ xám bạc + ánh ngọc ấm.

## Handoff: audio

- Gió đỉnh núi đổi hướng (đọc được bằng âm thanh trước khi đẩy).
- Tiếng gầm **nhiều giọng chồng** của Đại Bàng Tinh; ở phase 2 rõ "nhiều người" hơn "một con chim".
- Tiếng đá/lệ đá: rò rỉ đều ở S01-S03; ngừng rơi khi khắc tên HB-04 (release).
- `Lôi Kích`: sấm khô, ngắt nhịp, gợi "ký ức bị đánh thức".
- Release: gió lặng, nhiều giọng thì thầm một cái tên rồi im.
- Absorb: nhiều giọng gào bị nén dưới da, không dùng "evil sting" ồn.
- Hidden: tiếng khắc đá lên bia; khoảng lặng khi tên được đọc trọn.

## Handoff: localization

- Giữ trong glossary: `Long Nhân`, `Long Ngọc`, `Long Khí`, `Đại Bàng Tinh`, `Tù Trưởng Lệ Đá`, `Thế Đột/Trảm/Ngự`, `Lôi Kích`, `Rìu Thần Thạch Sơn`, `Tiếng Vọng Lạc Long`.
- Phân biệt **"bị xóa tên"** (erased — có chủ đích) và **"bị lưu đày"** (exiled) và **"bị bỏ lại"** (CH-01) — ba sắc thái khác nhau, không gộp.
- "Bộ tộc bị ruồng bỏ/bị xóa tên" là hư cấu; không dịch thành một tộc người có thật; không khẳng định lịch sử chính xác.
- Không dịch `Đại Bàng Tinh` thành "Phoenix"/"Imperial Eagle"; giữ là một yêu quái chim lớn bi kịch.
- Thoại nhiều giọng của boss cần phụ đề phân biệt "một giọng" vs "hợp giọng"; dòng reveal cần cinematic subtitle budget.
