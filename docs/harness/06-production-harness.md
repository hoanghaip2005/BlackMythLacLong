# Production Harness

## 1. Mục tiêu

Tách narrative khỏi implementation nhưng vẫn đủ rõ để đội gameplay, art, audio, cinematic và localization nhận việc sau này.

## 2. ID convention

| Loại | Mẫu | Ví dụ |
|---|---|---|
| Chương | `CH-##` | `CH-01` |
| Scene | `CH-##-S##` | `CH-02-S04` |
| Quest | `Q-CH##-###` | `Q-CH02-001` |
| Dialogue | `D-CH##-S##-##` | `D-CH02-S04-01` |
| Boss | `B-##` | `B-02` |
| Long Ngọc | `LG-##` | `LG-02` |
| Choice | `C-CH##-###` | `C-CH02-003` |
| Ending | `E-##` | `E-04` |
| Truth flag | `TRUTH_*` | `TRUTH_FOX_WAS_A_REFUGE` |
| Narrative variable | `snake_case` | `dragon_hunger` |

ID không đổi khi đổi tiêu đề. Đổi nghĩa ID cần tạo ID mới và đánh dấu ID cũ `deprecated`.

## 3. Ownership

- Narrative: canon, theme, scene, quest, dialogue, boss motivation, choice effects.
- Quest/gameplay design: mục tiêu tương tác, encounter flow, reward system hook.
- Combat design: phase, telegraph, counterplay, balance và frame data.
- Art: visual brief, silhouette, environment story, VFX brief.
- Audio: voice direction, ambience, musical reveal, stinger.
- Engineering: runtime state, save/load, branching integration, telemetry.
- Localization: glossary, character voice, text constraints và cultural review.

Nếu một card có field thuộc owner khác, ghi hook và dependency thay vì giả định chi tiết.

## 4. Dependency labels

- `narrative`: cần canon hoặc content card khác.
- `gameplay`: cần encounter/system design.
- `art`: cần visual asset hoặc environment layout.
- `audio`: cần voice/music/SFX.
- `localization`: cần glossary hoặc character limit.
- `engineering`: cần runtime flag/save support.

## 5. Visual asset handoff

Visual character card là contract giữa narrative, art và các owner downstream. Card phải ghi:

- identity, visual thesis, silhouette và forbidden confusions;
- anatomy, outfit layers, weapon grip/sheath và attachment/socket;
- palette, material, wear/corruption và motif Việt Nam được phép/cấm;
- source asset, license, modification scope, `.blend`, preview và asset IDs;
- rig/animation notes, phase variants, cultural review và acceptance checklist.

Không ghi topology, texture resolution, shader node hoặc frame data nếu owner chưa chấp nhận. Khi dùng asset có sẵn, provenance và license là dependency bắt buộc, không phải ghi chú tùy chọn.

## 6. Review gates

### Gate A - Story intent

Kiểm tra scene/quest có purpose, dramatic question và exit state.

### Gate B - Canon and branch

Kiểm tra thuật ngữ, ID, truth flags, biến số, boss fate và ending impact.

### Gate C - Experience handoff

Kiểm tra người chơi nhận biết mục tiêu, cost, feedback và phase change bằng trải nghiệm.

### Gate D - Content lock

Chỉ lock khi dependency của owner khác đã được chấp nhận hoặc được ghi rõ là out of scope.

## 7. Versioning

Mỗi content card có `content_version`:

- `0.x`: draft, cấu trúc còn thay đổi.
- `1.0`: approved, có thể làm nguồn cho card khác.
- `1.x`: sửa câu chữ hoặc mở rộng không đổi state.
- `2.0`: đổi state, canon, branch hoặc player-facing behavior.

Đổi ending rule, Long Ngọc, identity nhân vật hoặc truth flag bắt buộc có ADR.

## 8. Handoff packet

Một packet bàn giao tối thiểu gồm:

- Content cards ở trạng thái `approved`.
- Context và canon sections được dùng.
- State changes và điều kiện.
- Dependencies theo owner.
- Acceptance criteria.
- Known risks.
- Localization notes nếu có thoại.

## 9. Không khóa sai phạm vi

Ở giai đoạn narrative pre-production, các câu sau là hợp lệ:

- “Cần một khoảnh khắc người chơi nhận ra rễ là cổng máu của Mộc Tinh.”
- “Cần ba silhouette để phân biệt thật/ảo trong phase 1 của Hồ Tinh.”
- “Cần feedback rõ khi Long Ngọc chuyển từ vật chiếm đoạt thành vật chứng.”

Các câu sau chưa hợp lệ nếu chưa có owner:

- “Dùng animation asset X ở frame 18.”
- “Boss có 100000 HP.”
- “Dùng shader cụ thể Y.”
- “Lưu flag bằng class Z.”
