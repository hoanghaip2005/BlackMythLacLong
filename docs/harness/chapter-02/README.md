# CH-02 Package

Gói phát triển chi tiết thứ hai của Huyết Mạch Lạc Long: **Ảo Ảnh Đầm Cáo**.

## Đọc theo thứ tự

1. `00-chapter-brief.md` - mục tiêu, canon lock và end states.
2. `01-scene-flow.md` - flow cảnh từ làng không bóng đến khi tên thật được gọi lại.
3. `02-cast-and-factions.md` - nhân vật, boss, boss ẩn và dân đầm Tây Hồ.
4. `03-quests-and-choices.md` - quest, choice, state effect (kể cả nhánh ẩn).
5. `04-dialogue-script.md` - thoại chủ đạo và biến thể nhánh.
6. `05-boss-encounter.md` - encounter Cửu Vĩ (`B-02`) và Bóng Vô Danh (`HB-02`) theo phase.
7. `06-state-and-handoff.md` - state machine narrative và handoff liên ngành.
8. `07-validation.md` - checklist nghiệm thu CH-02 (gồm boss ẩn).
9. `08-visual-design.md` - visual contract cho Hồ Tinh, Bóng Vô Danh và đầm Tây Hồ.

## Nội dung đã khóa

- Chapter arc: nghi ngờ khuôn mặt -> điều tra thật/giả -> lựa chọn -> boss -> gọi lại tên.
- Boss chính: `B-02` Hồ Tinh - Cửu Vĩ. Boss fate: `released`, `defeated_by_force`, `absorbed`.
- Boss ẩn (ADR-004): `HB-02` Bóng Vô Danh; cờ `CH02_HIDDEN_RELEASED`; cộng `hidden_released`.
- Ba choice chính: `C-CH02-001`, `C-CH02-002`, `C-CH02-003`; choice ẩn `C-CH02-00H`.
- Mảnh Long Ngọc: `LG-02`. Truth flag: `TRUTH_FOX_WAS_A_REFUGE`.
- Khả năng mở trong chương: `Phân Thân` (ảo ảnh đất sét), gắn câu hỏi bản ngã.
- Visual language: Đông Sơn/Lạc Việt, vật liệu đầm lầy - sương - gương nước - ma trơi, cultural review bắt buộc.

## Nội dung chưa khóa

- Thời lượng chính xác từng encounter.
- Combat tuning và số liệu (damage/HP/frame data để `TBD`).
- Layout map, model, animation, VFX, SFX cụ thể cho đầm và Cửu Vĩ.
- Cách lưu state trong runtime.
- Tên đầy đủ và backstory sâu của NPC phụ ngoài CH-02.
- Asset `.blend`/preview cho `B-02` và `HB-02` (chưa dựng; visual contract ở mức design intent).
