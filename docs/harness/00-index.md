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

- `chapter-01/README.md` - package chi tiết của CH-01.
- `chapter-01/08-visual-design.md` - visual contract cho Long Nhân và Ngư Tinh.
- `templates/visual-character.yaml` - template visual character dùng cho các chương sau.
