# CH-06 Package

Gói phát triển chương cuối của Huyết Mạch Lạc Long: **Hỗn Mang Tế Đàn**. Đây là chương quy tụ năm mảnh Long Ngọc, xác nhận reveal trung tâm ("phong ấn chưa từng vỡ") và resolve một trong bốn ending theo Resolution Rules (`02 §7`).

## Đọc theo thứ tự

1. `00-chapter-brief.md` - mục tiêu, canon lock, bốn end state + hai tag fallback.
2. `01-scene-flow.md` - flow từ bậc đá không bóng đến ending card.
3. `02-cast-and-factions.md` - Long Nhân, Hỗn Mang, Tiếng Vọng, các cộng đồng và chứng nhân oan khuất.
4. `03-quests-and-choices.md` - quest, bốn quyết định cuối, state effect.
5. `04-dialogue-script.md` - thoại Hỗn Mang (giọng bản sao), Tiếng Vọng, ending line.
6. `05-boss-encounter.md` - encounter Hỗn Mang dạng bản sao, mirror mechanic, fate→final_decision.
7. `06-state-and-handoff.md` - state machine resolve ending và handoff (gồm cinematic).
8. `07-validation.md` - checklist nghiệm thu CH-06, gồm Ending acceptance.
9. `08-visual-design.md` - visual contract cho Hỗn Mang và bốn ending card.

## Nội dung đã khóa

- Chapter arc: quy tụ ký ức -> đối diện bản sao -> đấu tay đôi -> quyết định cuối -> ending.
- Boss: `B-06` Hỗn Mang trong hình dạng Long Nhân (bản sao).
- Bốn quyết định cuối: `restore`, `absorb`, `destroy`, `reconcile` -> `final_decision`.
- Bốn ending: `E-01 LONG_VUONG`, `E-02 TAN_HON_MANG`, `E-03 DOAN_TUYET_LONG_MACH`, `E-04 HOA_GIAI_BACH_TOC`.
- Hai tag fallback: `E-04-PARTIAL` (thiếu `hidden_released=5`), `E-03-BITTER` (reconcile thiếu điều kiện lõi).
- Reveal xác nhận: `TRUTH_SEAL_WAS_NEVER_BROKEN` trở thành sự thật đầy đủ tại đây.
- Canon Lock 8: Hỗn Mang sao chép hình dáng/kỹ thuật đã thấy, KHÔNG sao chép lựa chọn người chơi chưa thực hiện.
- Full completion (ADR-004): `hidden_released=5` mở lớp "chứng nhân oan khuất" (HB-01..05 hiện về) -> `E-04` trọn vẹn.

## Nội dung chưa khóa

- Thời lượng chính xác của duel và ending cinematic.
- Combat tuning, số liệu, cách boss "đọc" input runtime.
- Layout tế đàn, model, animation, VFX, SFX cụ thể.
- Cách lưu và resolve `final_decision` trong runtime.
- Asset path, license, topology, frame data.
