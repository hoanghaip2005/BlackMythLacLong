# CH-03 State and Handoff

## Initial state

```yaml
chapter: CH-03
location: phong_chou_ruined_capital
weapon: thach_son_axe
long_ngoc: [LG-01, LG-02]
variables:
  memory_recovered: <carry from CH-02>
  mercy_marks: <carry>
  tribal_trust: <carry>
  dragon_hunger: <carry>
  relics_purified: <carry>
  hidden_released: <carry>
flags:
  - CH03_STARTED
  - LONG_NHAN_UNNAMED
boss_fates: {}
final_decision: null
```

## Required flags

| Flag | Set at | Meaning |
|---|---|---|
| `CH03_STARTED` | S01 | Chapter started |
| `LONG_NHAN_UNNAMED` | carry | Player identity remains unresolved |
| `CH03_RESCUED_HIEN` | S02 | Hiến được giải thoát |
| `CH03_USED_OATHS` | S02 | Người chơi mượn hàng ngũ mở đường |
| `CH03_STELES_READ_1` | S03 | Bia "Giữ đất" đã đọc |
| `CH03_STELES_READ_2` | S03 | Bia "Không tên" đã đọc |
| `CH03_STELES_READ_3` | S03 | Bia "Tự ở lại" đã đọc (mở màn ẩn) |
| `CH03_STELE_BROKEN` | S03 | Người chơi chẻ bia mở đường nhanh |
| `CH03_OATH_HEARD_FULL` | S04 | Đã nghe trọn lời thề |
| `CH03_GAVE_NAME` | S03/S04 | Đã gọi đúng tên một vong linh |
| `CH03_OATH_JUDGED` | S04 | Người chơi phán xét lời thề |
| `CH03_ANCHOR_1_RELEASED` | B03 | Nút rễ 1 được giải thoát |
| `CH03_ANCHOR_2_RELEASED` | B03 | Nút rễ 2 được giải thoát |
| `CH03_ANCHOR_3_RELEASED` | B03 | Nút rễ 3 được giải thoát |
| `Q_CH03_002_COMPLETE` | Optional | Ba bia đọc trọn, không phá |
| `CH03_END_RELEASED` | B03 | Mộc Tinh được giải thoát |
| `CH03_END_FORCE` | B03 | Mộc Tinh bị hạ bằng lực |
| `CH03_END_ABSORBED` | B03 | Nguyên thần Mộc Tinh bị cưỡng đoạt |
| `CH03_END_SACRIFICED` | S05/B03 | Một vong linh/HB-03 tự hy sinh phá vòng |
| `CH03_HIDDEN_UNLOCKED` | S03 | Gò mộ cổ được tìm ra |
| `CH03_HIDDEN_RELEASED` | HIDDEN | Tướng Quân Vô Đầu được giải thoát |
| `CH03_COMPLETE` | S06 | Chapter complete |
| `TRUTH_OLD_ARMY_WAS_BOUND` | S03 (clue) / B03 (xác nhận) | Truth flag của chương |
| `LG03_ACQUIRED` | B03 | `LG-03` đã thu |

## State transition matrix

| Event | Variables | Flags | Player-facing feedback |
|---|---|---|---|
| Giải thoát Hiến | `tribal_trust +1`, `mercy_marks +1` | `CH03_RESCUED_HIEN` | Hiến tỉnh, dẫn đường, chỉ nút rễ |
| Mượn hàng ngũ mở đường | (chưa đổi hunger ngay) | `CH03_USED_OATHS` | Rừng rẽ nhanh; Hiến bị kéo lùi vào hàng |
| Đọc 3 bia | none | `CH03_STELES_READ_3` | Bond clue rõ; mở lối màn ẩn |
| Chẻ bia đi tắt | `dragon_hunger +1` | `CH03_STELE_BROKEN` | Mở nhanh; mất đường release + mất manh mối ẩn |
| Gọi tên vong linh | none | `CH03_GAVE_NAME` | Hiến/Trưởng đổi thái độ |
| Nghe trọn lời thề | none | `CH03_OATH_HEARD_FULL` | Mở ký ức sâu, gợi `HB-03` |
| Hiến tự hy sinh | none (không phải mercy của player) | `CH03_END_SACRIFICED` | Vòng rễ phá; aftermath ân nghĩa |
| Giải thoát nút rễ | none | `CH03_ANCHOR_*_RELEASED` | Trống vọng; arena đổi; ký ức hiện |
| Release boss | `memory_recovered +1`, `mercy_marks +1`, `relics_purified +1` | `CH03_END_RELEASED` | Lõi dịu, rễ buông, `LG-03` sáng ấm |
| Hạ bằng lực | none | `CH03_END_FORCE` | Ký ức khuyết, lõi tắt lạnh |
| Cưỡng đoạt | `dragon_hunger +1` | `CH03_END_ABSORBED` | Vệt đen dưới da; rừng rên |
| Giải thoát `HB-03` | `hidden_released +1`, `mercy_marks +1` | `CH03_HIDDEN_RELEASED` | Mộ yên; kiếm khắc tên chìm vào đất |
| Cưỡng đoạt `HB-03` | `dragon_hunger +1` | (không set HIDDEN_RELEASED) | Kiếm nứt; rừng siết chặt |
| Chapter exit | none | `CH03_COMPLETE`, `LG03_ACQUIRED` | CH-04 hook mở |

## State invariants

- `LG-03` is acquired exactly once.
- Chỉ một trong `CH03_END_RELEASED`, `CH03_END_FORCE`, `CH03_END_ABSORBED` là true.
- `CH03_END_RELEASED` ngụ ý đã giải thoát các nút rễ (bond), không đến chỉ từ thoại.
- `CH03_END_SACRIFICED` không thay thế fate của `B-03`; nó là cờ aftermath bổ sung (fate của Hiến/HB-03).
- `memory_recovered` tăng tối đa một lần trong CH-03.
- `relics_purified` chỉ tăng khi release, không tăng khi force/absorb.
- `hidden_released` chỉ tăng khi `HB-03` được `released`; absorb/force không tăng.
- `dragon_hunger` không giảm trong CH-03.
- `TRUTH_OLD_ARMY_WAS_BOUND` là clue/flag sau CH-03, chưa phải bằng chứng toàn cục tới CH-06.
- Rìu Thần Thạch Sơn đã có từ CH-01; CH-03 không "thức tỉnh" lại nó.

## Handoff: gameplay

### Required experience

- Điều hướng rừng rễ chuyển động; phá rễ mở đường và lộ lõi.
- `Thế Trảm` có một khoảnh khắc dạy (dọn cụm xác-rễ ở `S05`/phase 1) và sau đó là tùy chọn mastery.
- Đọc telegraph "rễ siết" bằng hình ảnh (màu rễ) và âm thanh (trống lệnh).
- Arena với các nút rễ trói vong linh ở nhiều cao độ; giải thoát nút rễ là counterplay narrative.
- Boss phải hỗ trợ đường thắng không release và đường release.
- Màn ẩn `HB-03` tùy chọn, combat nhẹ hơn, thiên `Thế Ngự` + phá rễ trung tâm.
- Hook phụ (TBD, không khóa): `Nguyên thần Chân Tinh` (phá giáp, chống sợ bị nuốt) - vị trí do production quyết, có thể ở CH-03 hoặc nơi khác.

### Explicitly deferred

- Damage, health, stamina và resource numbers.
- Hitbox/frame data.
- Save serialization implementation.
- Vị trí chính xác của hook Nguyên thần Chân Tinh.

## Handoff: art

- Kinh đô Phong Châu bị rừng nuốt: cổng đá nứt do rễ, biển chữ bị rêu che, kiến trúc Lạc Việt/Đông Sơn (không phải thành fantasy vô danh).
- Giáp mọc rêu trên xác-rễ; rễ ký sinh (nâu, cắm gáy) khác rễ tự-nguyện của `HB-03` (đỏ sẫm, tỏa từ thân giáp) - phải đọc được.
- Lõi đỏ đập như tim, quấn rễ cái; nhựa đỏ như máu loãng, tiết chế (không máu me như phần thưởng thị giác).
- Mộ cổ không bị rễ quấn (gò mộ `HB-03`).
- Mộc Tinh silhouette đọc là "cây ăn thịt/quân hóa", KHÔNG phải ent hiền lành phương Tây.
- Long Ngọc xuất hiện như vật-chứng ký ức, không phải loot gem.

## Handoff: audio

- Bed rừng thấp: gỗ căng, rễ bò trong đá, sương; có khoảng lặng cho thoại.
- "Trống lệnh" làm ngôn ngữ: nhịp đều = hàng ngũ; dồn = rễ siết/hút máu; dứt = im lặng hậu quả.
- Tiếng binh khí vọng đều nhịp ở đầu chương, thưa dần/tắt ở `S06` (released) hoặc tắt lạnh (force).
- Giọng Mộc Tinh chậm như nhựa chảy; giọng Hiến đứt gãy; Trưởng nặng mệnh lệnh.
- `HB-03`: không lời - chỉ tiếng kiếm cùn, nhịp rễ, và một tiếng vọng "cụt" (không đầu).
- Release: lõi dịu, rễ buông, trống dứt. Absorb: xung trầm dưới thoại, không "evil sting" to.

## Handoff: localization

- Giữ `Long Nhân`, `Long Ngọc`, `Long Khí`, `Mộc Tinh`, `Thế Trảm`, `Rìu Thần Thạch Sơn`, `Phong Châu`, `Tiếng Vọng Lạc Long` trong glossary.
- Phân biệt "giải thoát" (release, có chủ đích tha) và "phá/xé lời thề" (judge) - chúng là hai theme khác nhau.
- Phân biệt "tự nguyện ở lại" và "bị trói" - then chốt cho `TRUTH_OLD_ARMY_WAS_BOUND`.
- Không dịch `Vong linh Lạc Việt` thành "undead army" chung chung.
- Giữ `HB-03` "không đầu" như mất-danh-tính, không như horror chặt đầu rẻ tiền; dòng của ông là chữ khắc, cần format subtitle riêng.
- Thoại ngắn đủ cho combat subtitle; dòng reveal cần cinematic subtitle budget.
