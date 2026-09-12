# CH-05 Package

Gói phát triển chi tiết của chương năm: **Song Giao Tế Thủy** (Ngã Ba Hạc).

## Đọc theo thứ tự

1. `00-chapter-brief.md` - mục tiêu, canon lock và end states.
2. `01-scene-flow.md` - flow cảnh từ làng nổi đến bậc tế đàn.
3. `02-cast-and-factions.md` - nhân vật, hai Song Giao, Giao Mẫu và Làng nổi.
4. `03-quests-and-choices.md` - quest, choice, state effect (kể cả nhánh ẩn).
5. `04-dialogue-script.md` - thoại chủ đạo và biến thể nhánh.
6. `05-boss-encounter.md` - encounter Song Giao -> Hắc Giao Long theo hai giai đoạn boss.
7. `06-state-and-handoff.md` - state machine narrative và handoff liên ngành.
8. `07-validation.md` - checklist nghiệm thu CH-05.
9. `08-visual-design.md` - visual contract cho Song Giao, Hắc Giao Long và Giao Mẫu.

## Nội dung đã khóa

- Chapter arc: làng nổi giữa lũ -> hai tiếng gọi -> bè chiến -> hợp thể cưỡng ép -> nước rút lộ tế đàn.
- Boss chính `B-05` có hai giai đoạn: `B05-A` Song Giao (đánh giữa hai boss) và `B05-B` Hắc Giao Long (hợp thể cưỡng ép). `B05-P0` là intro không chiến đấu.
- Boss ẩn `HB-05` Giao Mẫu (ADR-004): màn ẩn `CH-05-HIDDEN`, cờ `CH05_HIDDEN_RELEASED`, tăng `hidden_released`.
- Boss fate: `released`, `defeated_by_force`, `absorbed`.
- Ba choice chính: `C-CH05-001`, `C-CH05-002`, `C-CH05-003`; choice ẩn `C-CH05-00H`.
- Mảnh Long Ngọc: `LG-05` (mảnh thứ năm và cuối cùng).
- Truth flag: `TRUTH_CONFLICT_WAS_FED`.
- Visual language: Đông Sơn/Lạc Việt, giao long bản địa (thuồng luồng), vật liệu sông nước phù sa, cultural review bắt buộc.

## Nội dung chưa khóa

- Thời lượng chính xác từng encounter.
- Combat tuning và số liệu.
- Layout map, model, animation, VFX, SFX cụ thể.
- Cách lưu state trong runtime.
- Vị trí gameplay của encounter `NGUYEN-THAN-THUONG-LUONG` (chỉ là narrative hook ở CH-05).
- Tên đầy đủ và backstory sâu của các NPC phụ ngoài CH-05.
- Topology, texture resolution, animation frame và final asset lock.
