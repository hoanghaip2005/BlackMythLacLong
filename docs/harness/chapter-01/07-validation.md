# CH-01 Validation

## Narrative acceptance

- [ ] Opening establishes Long Nhân has no name, memory or complete weapon.
- [ ] Player understands the immediate goal before learning global lore.
- [ ] Linh has agency in both rescue and abandon variants.
- [ ] Three glyphs communicate a promise, a wound and an absence; none falsely confirms a broken seal.
- [ ] Ngư Tinh's desire remains understandable without excusing the harm it causes.
- [ ] Rìu Thần Thạch Sơn appears only after the Ngư Tinh encounter.
- [ ] Chapter closes with a concrete hook to CH-02.

## Branch acceptance

- [ ] `C-CH01-001` changes trust/feedback without killing or hard-locking Linh.
- [ ] `C-CH01-002` changes boss read and dialogue.
- [ ] `C-CH01-003` resolves into exactly one boss fate.
- [ ] Release requires actions plus listening, not a single dialogue choice.
- [ ] Force victory remains completable and honest.
- [ ] Absorption gives immediate power fantasy plus visible narrative cost.

## Boss acceptance

- [ ] Each phase has a distinct narrative trigger.
- [ ] Each phase has a visual and audio telegraph.
- [ ] Water, tail and anchor interactions are understandable without HUD-only explanation.
- [ ] No phase requires a single stance or spell for all players.
- [ ] `Thủy Ảnh` has one mandatory teaching moment and later optional mastery.
- [ ] Boss does not die before the fate choice is resolved.

## Continuity acceptance

- [ ] Exactly `LG-01` is awarded in CH-01.
- [ ] `TRUTH_SEAL_WAS_NEVER_BROKEN` is seeded, not fully explained.
- [ ] No direct physical appearance of Lạc Long Quân.
- [ ] No Hồ Tinh reveal before the final song hook.
- [ ] `LG-01` is not described as “the first of six”.
- [ ] `Rìu Thần Thạch Sơn` naming matches the global glossary.

## Vertical slice acceptance

The CH-01 vertical slice is ready for cross-discipline review when:

1. S01-S03 can be played with placeholder environment and placeholder enemy silhouettes.
2. The player can experience both C-CH01-001 outcomes in separate test runs.
3. S04-S05 can communicate the bond without a lore dump.
4. B-01 supports at least one force victory and one release test path.
5. State log records every required flag and one boss fate.
6. S08 shows a visibly different aftermath for released, force and absorbed.

## Hidden content acceptance (ADR-004)

- [ ] `CH-01-HIDDEN` là tùy chọn; bỏ qua vẫn đạt `CH01_COMPLETE` và không khóa `CH01_END_*`.
- [ ] `HB-01` Ma Da có đủ ba fate (`released`/`defeated_by_force`/`absorbed`) và chỉ `released` cộng `hidden_released`.
- [ ] `released` đòi một hành động (chuông "không-về" + gọi tên), không phải một nhãn thoại.
- [ ] `hidden_truth` đào sâu `TRUTH_SEAL_WAS_NEVER_BROKEN` mà KHÔNG tạo truth flag toàn cục mới và KHÔNG tạo Long Ngọc mới.
- [ ] `hidden_released` clamp 0..5; không tăng ở nhánh force/absorb.
- [ ] Cultural review cho `ma da` (tín ngưỡng dân gian) hoàn tất trước khi `approved`; tông bi thương, không mua vui rùng rợn.
