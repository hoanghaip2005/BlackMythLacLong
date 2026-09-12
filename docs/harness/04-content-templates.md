# Content Templates

Các template dưới đây là hợp đồng nội dung. Mẫu YAML tương ứng nằm trong `templates/`. Mọi field bắt buộc phải có giá trị hoặc ghi `TBD` kèm owner và deadline.

## 1. Scene Card

Dùng cho một cảnh có camera, gameplay transition, exploration hoặc dialogue.

Bắt buộc:

- `id`, `chapter`, `status`.
- `purpose`: cảnh thay đổi điều gì.
- `entry_state`, `exit_state`.
- `dramatic_question`.
- `beats`: tối đa 5 beat chính.
- `player_knowledge_before`, `player_knowledge_after`.
- `branch_hooks`.
- `dependencies`.
- `validation`.

Không ghi thông số animation hoặc asset cụ thể nếu chưa có production owner. Dùng hook như `water_whirlpool_vfx` hoặc `boss_phase_2_reveal`.

## 2. Quest Card

Dùng cho nhiệm vụ chính, phụ hoặc nhiệm vụ bond.

Bắt buộc:

- `id`, `type`, `chapter`, `giver`.
- `player_goal` bằng động từ cụ thể.
- `fictional_reason`.
- `steps`.
- `fail_or_cost`.
- `choice_points`.
- `rewards` chia `narrative`, `system_hook`, `item`.
- `state_changes`.
- `completion_signal`.

Quest phụ chỉ được tồn tại nếu làm rõ theme, phe phái, boss hoặc ending. Không thêm quest chỉ để kéo thời lượng.

## 3. Dialogue Card

Bắt buộc:

- `id`, `speaker`, `listener`, `context`.
- `intent` của người nói.
- `subtext`.
- `lines` có `line_id`, `text`, `condition`.
- `choice_response` nếu có lựa chọn.
- `voice_direction`.
- `localization_notes`.

Không nhồi lore vào một lượt thoại. Mỗi lượt thoại nên làm một trong ba việc: đổi quan hệ, đổi thông tin, hoặc đổi quyết định.

## 4. Boss Card

Bắt buộc:

- `id`, `name`, `chapter`, `myth_inspiration`.
- `surface_role`, `inner_wound`, `desire`.
- `arena_story`.
- `phases` có `narrative_trigger`, `combat_hook`, `telegraph`, `player_counterplay`.
- `bond_resolution`.
- `boss_fates`.
- `memory_reveal`.
- `long_ngoc`.
- `aftermath_variants`.

Boss card không chứa damage number, hitbox hoặc behavior-tree node. Các phần đó thuộc gameplay design document sau.

## 5. Choice Card

Mọi choice card phải có:

- `choice_id`.
- `prompt_to_player` không thao túng bằng nhãn tốt/xấu.
- `known_cost`.
- `hidden_long_term_risk` chỉ được ẩn một phần, không được lừa người chơi vô lý.
- `effects` lên biến số và cờ.
- `next_content`.
- `feedback_scene`.

## 6. Asset/gameplay handoff hook

Narrative chỉ yêu cầu trải nghiệm, ví dụ:

- `player must recognize the real fox among three false silhouettes`.
- `arena must communicate that roots are the boss health gate`.
- `phase change must reveal the boss wound before the attack pattern escalates`.

Không yêu cầu công nghệ cụ thể trước khi có design owner.
