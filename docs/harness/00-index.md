# Narrative Harness Index

## Mục đích

Harness biến sườn truyện thành một hệ thống có thể mở rộng, kiểm tra và bàn giao. Nó trả lời bốn câu hỏi:

1. Điều gì luôn đúng trong thế giới này?
2. Người chơi có thể thay đổi điều gì?
3. Mỗi thay đổi xuất hiện ở đâu và trả giá thế nào?
4. AI và đội sản xuất phải nhận dữ liệu ở định dạng nào?

## Thứ tự ưu tiên nguồn

Khi hai tài liệu mâu thuẫn, áp dụng thứ tự sau:

1. ADR đã `Accepted`.
2. `01-story-bible.md` ở phần Canon Locks.
3. `02-branching-and-endings.md` ở phần Resolution Rules.
4. `03-chapter-harness.md`.
5. Content card hoặc prompt pack.
6. Draft scene, ý tưởng tự do và nội dung chưa review.

## Phạm vi hiện tại

### Có trong harness

- Premise, theme, tone và audience.
- Canon thế giới, nhân vật, phe phái, thuật ngữ.
- Sáu chương và năm mảnh Long Ngọc.
- Nhánh lựa chọn, biến số, cờ trạng thái.
- Bốn kết thúc chính và fallback.
- Lớp "Oan Khuất Ẩn" (boss ẩn mỗi chương, ADR-004) và điều kiện full completion cho kết thúc thật `E-04`.
- Template nội dung có ID.
- Prompt AI có context budget và self-check.
- Visual harness cho silhouette, anatomy, outfit, vũ khí, asset provenance và cultural review.
- Tiêu chí nghiệm thu narrative.

### Chưa triển khai

- Final model 3D, concept art, animation, VFX và audio asset.
- Asset manifest/runtime integration.
- Combat numbers, hitbox, AI behavior tree và code gameplay.
- Runtime save system.
- Localization pipeline.
- Quest editor hoặc CMS.

## Luồng làm việc chuẩn

`Sườn ý tưởng -> Story Card -> Branch Card -> Scene/Quest Card -> Draft -> Canon Review -> Branch Review -> Content Lock -> Handoff`

## Trạng thái nội dung

- `idea`: ý tưởng chưa cam kết.
- `draft`: đã có nội dung, chưa kiểm tra.
- `review`: đang kiểm tra canon và nhánh.
- `approved`: được dùng làm nguồn cho nội dung khác.
- `locked`: không đổi nếu không có ADR hoặc change request.
- `deprecated`: không dùng cho nội dung mới, giữ để truy vết.

## Nguyên tắc viết nhanh

- Một scene chỉ có một thay đổi cảm xúc hoặc thông tin chính.
- Một quest phải có mục tiêu người chơi hiểu được mà không cần đọc lore dài.
- Mỗi lựa chọn quan trọng phải ghi rõ: ý định, biến số, hậu quả gần, hậu quả xa.
- Boss phải có phase hook, reveal nhân vật và một cách đọc khác nhau tùy lựa chọn.
- Không dùng từ “canon” cho draft chưa review.

## Package đang phát triển

Mỗi chương có một package chi tiết 11 file theo khuôn `chapter-01/` (README, 00-brief, 01-scene-flow, 02-cast, 03-quests, 04-dialogue, 05-boss-encounter, 06-state-and-handoff, 07-validation, 08-visual-design, registry.yaml), gồm cả boss chính (`B-0X`) và boss ẩn Oan Khuất Ẩn (`HB-0X`, ADR-004).

- `chapter-01/` — CH-01 Trầm Thủy Ngư Tinh (boss ẩn `HB-01` Ma Da).
- `chapter-02/` — CH-02 Ảo Ảnh Đầm Cáo (boss ẩn `HB-02` Bóng Vô Danh).
- `chapter-03/` — CH-03 Huyết Mộc Đoạt Mệnh (boss ẩn `HB-03` Tướng Quân Vô Đầu).
- `chapter-04/` — CH-04 Lệ Đá Đỉnh Sương (boss ẩn `HB-04` Tù Trưởng Lệ Đá).
- `chapter-05/` — CH-05 Song Giao Tế Thủy (boss ẩn `HB-05` Giao Mẫu).
- `chapter-06/` — CH-06 Hỗn Mang Tế Đàn (không boss ẩn; full completion mở lớp hòa giải trọn vẹn của `E-04`).
- `templates/visual-character.yaml` — template visual character dùng cho các chương.
