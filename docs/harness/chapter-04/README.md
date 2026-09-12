# CH-04 Package

Đây là gói phát triển chi tiết của chương 4 — **Lệ Đá Đỉnh Sương** (Núi Thạch Môn).

## Đọc theo thứ tự

1. `00-chapter-brief.md` - mục tiêu, canon lock và end states.
2. `01-scene-flow.md` - flow cảnh từ chân núi tới đỉnh Thạch Môn.
3. `02-cast-and-factions.md` - nhân vật, boss và các bộ tộc bị ruồng bỏ.
4. `03-quests-and-choices.md` - quest, choice, state effect.
5. `04-dialogue-script.md` - thoại chủ đạo và biến thể nhánh.
6. `05-boss-encounter.md` - encounter Đại Bàng Tinh theo phase.
7. `06-state-and-handoff.md` - state machine narrative và handoff liên ngành.
8. `07-validation.md` - checklist nghiệm thu CH-04.
9. `08-visual-design.md` - visual contract cho Đại Bàng Tinh và Tù Trưởng Lệ Đá.

## Nội dung đã khóa

- Chapter arc: leo đỉnh -> điều tra lời chứng -> phán quyết -> boss -> hậu quả.
- Boss chính: `B-04` Đại Bàng Tinh; boss fate `released`, `defeated_by_force`, `absorbed`.
- Boss ẩn (ADR-004): `HB-04` Tù Trưởng Lệ Đá ở màn ẩn `CH-04-HIDDEN`; giải thoát cộng `hidden_released`.
- Bốn choice chính: `C-CH04-001`, `C-CH04-002`, `C-CH04-003`, `C-CH04-004`.
- Mảnh Long Ngọc: `LG-04` (mảnh thứ tư).
- Truth flag: `TRUTH_EXILE_WAS_ERASED`; hidden truth: tên bộ tộc bị xóa **có chủ đích**.
- Reveal xác nhận: Long Nhân **không phải** Lạc Long Quân; huyết thống không phải giấy phép cai trị.
- Visual language: Đông Sơn/Lạc Việt, đá - sương - lông vũ - lệ đá, cultural review bắt buộc.

## Nội dung chưa khóa

- Thời lượng chính xác từng encounter.
- Combat tuning và số liệu (R-05).
- Layout map, model, animation, VFX, SFX cụ thể.
- Cách lưu state trong runtime.
- Tên đầy đủ và backstory sâu của các NPC phụ ngoài CH-04.
- Topology, texture resolution, animation frame và final asset lock.
