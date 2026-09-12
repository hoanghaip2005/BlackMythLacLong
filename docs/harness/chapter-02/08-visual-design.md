# CH-02 Visual Design Harness

## Purpose

Nguồn chuẩn cho ngoại hình và cách đọc hình ảnh của các nhân vật/sinh vật quan trọng trong CH-02. Khóa art direction ở mức đủ để dựng, review và thay asset; **chưa** khóa topology, texture resolution, animation frame hay engine implementation. CH-02 **chưa có asset dựng sẵn** (khác CH-01); mọi `source/license` ở đây là `procedural/TBD` và cần cultural review trước khi `approved`.

## Shared art direction

### Visual thesis

CH-02 là một **ký ức bị làm giả**: đầm nước lặng, sương dày, mọi khuôn mặt đều có thể là mặt nạ. Hình khối phải **mềm, nhòe, phản chiếu** — ranh giới thật/giả chỉ đọc được qua **bóng** và **gương nước**, không qua chi tiết bề mặt. Đọc được trong silhouette trước khi thấy chi tiết.

### Vietnamese visual language

Được phép (tiết chế, có lý do canon):

- Hoa văn hình học Đông Sơn: tia mặt trời, vòng tròn đồng tâm, răng cưa, ziczac, chim Lạc cách điệu — trên rìu, gốm nỏ, bùa.
- Áo giao lĩnh / tứ thân biến thể vận động; vải quấn; dây dệt đỏ.
- Vật liệu đầm Việt: lau sậy, bùn, gỗ mục, gốm nỏ, bùa giấy, **ma trơi** (fox-fire / lửa trấu xanh), nước đục, sương.
- Bảng màu: sương xám bạc, đầm xanh đen, ma trơi xanh lục, cáo sẫm, ngọc sông, son đỏ mờ.
- Hình ảnh **cáo chín đuôi** lấy từ truyền thuyết Hồ Tinh Tây Hồ (Lạc Long Quân), không từ hồ ly tinh Đông Á.

**Motif CẤM** (giữ như CH-01, `08` global + ADR-002):

- Mây cuộn, long văn, đế hiệu, giáp cung đình hay hoa văn nhận diện rõ từ mỹ thuật đế chế Trung Hoa.
- Hanfu, cổ áo/tay áo mô phỏng Trung Hoa; kimono, samurai hay motif Nhật.
- **Hồ ly tinh quyến rũ sáo rỗng** (mỹ nhân cáo gợi tình kiểu Á Đông đại chúng) — Hồ Tinh ở đây là *kẻ che chở bi kịch*, không phải yêu nữ seductress.
- Rồng bốn móng, đầu rồng cung đình, phượng hoàng cung đình vô lý do canon.
- Ornament phủ kín làm mất silhouette ở khoảng cách camera gameplay.

### Shared technical rules

- Phụ kiện gameplay có `attachment/socket` rõ.
- Tay/chân theo anatomical pose trung tính; không mirror sai trục.
- Vũ khí có trục lưỡi, điểm cầm, hướng sheath ghi trước khi rig.
- Asset nguồn chỉ là nền; provenance không phải canon văn hóa; lọc mọi chi tiết qua mục motif cấm.
- Preview dùng để review design intent, không thay kiểm tra `.blend`/rig.

## Character card: B-02 Hồ Tinh – Cửu Vĩ

### Identity

- **ID:** `B-02`
- **Role:** Chapter 2 boss; một con cáo đầm lớn bị oan, từng giữ tên cho người chạy loạn; yêu khí khuếch đại lớp mặt nạ.
- **Visual thesis:** Một **con cáo già của đầm**, thân là sinh vật có thật, chín đuôi là **chín cái tên nó giữ**; những khuôn mặt người chỉ là **mặt nạ vay** — mượn, không phải bản chất.
- **Player read:** Boss có hai hình thái chiến đấu rõ: **kẻ đội lốt** (nhân hình vay mặt, nhiều bản sao) và **cáo chín đuôi thật** (đầm thú khổng lồ). Không phải hồ ly quyến rũ; không phải rồng.

### Silhouette and anatomy

- **Hình thái thật (P2):** cáo đầm khổng lồ, dài và thấp trọng tâm, bộ lông sẫm ướt; **chín đuôi** xòe như rễ lau, mỗi đuôi cuộn giữ một điểm sáng (một cái tên). Đầu cáo thật: mõm dài, tai dựng, mắt vàng-lục đọc được cảm xúc. Không thêm sừng, bờm rồng, hay vây.
- **Hình thái đội lốt (P1):** dáng người khoác "mặt nạ" — nhưng mặt nạ là **khuôn mặt vay** (Người Hát, đạo sĩ, Linh, và chính Long Nhân), cơ thể dưới lớp áo vẫn lộ nét cáo (bàn tay có móng, gấu áo lẫn lông, bóng in hình cáo).
- **Bóng:** bóng của Hồ Tinh **luôn là cáo** kể cả khi thân mang mặt người — đây là cơ chế đọc thật/giả, phải rõ ở gameplay distance.
- Không biến Hồ Tinh thành mỹ nhân; kể cả mặt nạ vay cũng lệch/không trọn, gợi "gần người nhưng sai".

### Boss phase variants

| Phase | Visual change | Narrative read |
| --- | --- | --- |
| `B02-P0` | Một bóng người trong sương; ba ma trơi dẫn vào đầm; mặt chưa rõ | Quy mô đánh lừa; khuôn mặt đầu tiên chưa phải thật; không tính combat phase |
| `B02-P1-MASK` | Tách thành **ba bản sao** mang mặt vay (Người Hát / đạo sĩ / Long Nhân); bóng in hình cáo; thân thật lẫn giữa ảo ảnh `Phân Thân` | Hồ Tinh *thử* xem Long Nhân có bị mặt nạ lừa như đám đông từng lừa nó |
| `B02-P2-CUUVI` | Bỏ hết mặt nạ; hiện **cáo chín đuôi** thật; đầm dâng; ma trơi tụ thành chín ngọn lửa giữ tên | Vết thương lộ ra: nó là *cáo giữ tên*, không phải *cáo ăn thịt người* |
| `B02-RELEASED` | Chín đuôi hạ; mỗi tên sáng lên rồi bay về phía bóng người tương ứng; xác cáo tan thành sương trong | Giải phóng — trả tên, không phải chiến thắng tuyệt đối |
| `B02-ABSORBED` | Chín ngọn lửa-tên bị kéo vào Long Nhân; mặt nạ vỡ vụn; đầm đen đặc lại | Cưỡng đoạt: lấy sức mạnh của khuôn mặt, bỏ mặc những cái tên |

### Materials, palette, wear

| Token | Hex | Use |
| --- | --- | --- |
| `HO_MIST_SILVER` | `#AEB9BC` | Sương, viền ảo ảnh, phản chiếu gương nước |
| `HO_MARSH_BLACK` | `#16211F` | Đầm, bóng, thân cáo ướt |
| `HO_FOXFIRE` | `#5FD0A0` | Ma trơi, chín ngọn lửa-tên, telegraph nguy hiểm |
| `HO_FOX_EYE` | `#D9C24A` | Mắt cáo, điểm khóa mục tiêu thật |
| `HO_BORROWED_SKIN` | `#9C8A78` | Mặt nạ vay (da người mượn), luôn hơi lệch tông |
| `HO_JADE` | `#6FA496` | `LG-02`, vùng memory reveal |

Lông cáo ướt, phản sáng nhẹ, không kim loại. Mặt nạ vay phải đọc là "gần người nhưng sai" (lệch tỷ lệ, thiếu bóng người, mắt vô hồn). Ma trơi là lửa lạnh xanh lục, không phải lửa trại. Yêu khí dùng sương + phản chiếu + nhiễu silhouette; tránh khói mây cuộn hay long văn.

### Arena attachments and combat readability

- **Boss blend:** `assets/bosses/chapter_02_hotinh/ho_tinh_ch02.blend` *(chưa dựng — dependency `ART-BOSS-HO-TINH`, `TBD`)*.
- **Preview:** *chưa có*; dựng preview sau khi blockout được duyệt.
- **Build script:** *chưa có* (`tools/build_hotinh_ch02.py` đề xuất, `TBD`).
- **Rig:** `Ho_Tinh_Combat_Rig` (đề xuất): spine cáo + 9 tail bones riêng (mỗi tail một socket tên), jaw, ears, mask-socket cho mặt nạ vay.
- **Required sockets/hooks:** `tail_01..tail_09`, `tail_name_core` (mỗi đuôi), `mask_face`, `jaw`, `eye_l`, `eye_r`, `long_ngoc_core`, `reflection_anchor`.
- Chín đuôi phải luôn cho người chơi đoán được hướng quét; ngọn lửa-tên không che mất silhouette thật trước đòn lớn.
- Ở `P1-MASK`, **bóng** của bản sao thật phải in hình cáo — đây là tín hiệu đọc thật/giả, không được mập mờ.
- `LG-02` nhìn thấy trong cửa sổ narrative đã ghi ở `05`, không thành weak-point UI giả.

### Source and license record

- **Source strategy:** boss sẽ là asset procedural/custom dựng trong repository (giống Ngư Tinh); chưa gắn license bên thứ ba.
- **External asset policy:** nếu thay bằng source library, chỉ nhận license thương mại hoặc CC0 tương thích; ghi URL, phiên bản, tác giả, phạm vi sửa trong manifest.
- **Cultural review:** bắt buộc trước khi thêm motif bề mặt — đặc biệt để **không** trượt thành hồ ly tinh Đông Á sáo rỗng; ưu tiên sinh học cáo đầm + chất liệu Việt (ma trơi, lau sậy).

## Character card: HB-02 Bóng Vô Danh

### Identity

- **ID:** `HB-02`
- **Role:** Hidden boss (Oan Khuất Ẩn, ADR-004); người tị nạn đầu tiên Hồ Tinh che chở, bị Hỗn Mang ăn mất tên thật, nay thành bóng không mặt đi vay/mượn tên người khác.
- **Visual thesis:** Một **cái bóng không mặt** — silhouette người nhưng **trống** ở chỗ khuôn mặt; nó đắp lên mình những khuôn mặt vay (kể cả mặt Long Nhân) để "có thật". Bi kịch: nó không ác, nó **đói một cái tên**.
- **Player read:** Sinh vật bóng, phi vật chất một phần; đọc bằng **gương nước** (bóng thật của nó là một người tị nạn, không phải quái).

### Silhouette and anatomy

- Hình người cao bằng Long Nhân nhưng **thiếu chiều sâu**: dẹt, hút sáng, viền chảy như mực loang trong nước.
- **Mặt trống**: một khoảng lõm không ngũ quan; khi nó vay mặt, một khuôn mặt (Người Hát / đạo sĩ / Long Nhân / đứa trẻ làng) hiện lên như mặt nạ mờ, luôn trượt/lệch.
- Khi soi **gương nước**, bóng thật là một **người tị nạn gầy, bế một bọc** — hình ảnh của người chạy loạn đầu tiên (đọc được sự thật: nó từng là người, không phải quỷ).
- Không sừng, không móng vuốt khoa trương; mối đe dọa đến từ việc nó **mặc khuôn mặt người quen** để dụ.

### Phase variants

| Phase | Visual change | Narrative read |
| --- | --- | --- |
| `HB02-P1-BORROWED-FACE` | Bóng đắp lần lượt mặt Người Hát → đạo sĩ → **mặt Long Nhân**; chuyển động giống hệt người bị nhại | Nó thử "mặc" Long Nhân; người chơi đối diện bản sao rỗng của chính mình |
| `HB02-P2-NAMELESS-TIDE` | Trút hết mặt nạ vay; bóng tràn thành triều mực; mặt thật chỉ lộ thoáng trong gương nước | Không còn tên để bám; nó tan thành đói khát thuần — phải được *gọi tên* để dừng |

### Materials, palette, wear

| Token | Hex | Use |
| --- | --- | --- |
| `HB_INK_VOID` | `#0C0F12` | Thân bóng, khoảng trống không mặt |
| `HB_STOLEN_FACE` | `#C7CDD0` | Mặt nạ vay (mờ, trượt) |
| `HB_MIRROR_GLEAM` | `#7FE3C0` | Gương nước tiết lộ bóng thật; tên thật khi được gọi |
| `HB_YEU_COLD` | `#2A6E72` | Yêu khí lạnh, viền chảy của bóng |

Bóng **hút sáng** (không phát sáng); điểm sáng duy nhất là gương nước và tên thật khi được gọi. Tránh "evil red glow"; mối nguy đọc bằng sự *thiếu* (mặt trống, bóng sai) chứ không bằng màu ác.

### Arena attachments and readability

- **Boss blend:** *chưa dựng* (`ART-HB-BONG-VO-DANH`, `TBD`).
- **Rig:** `Bong_Vo_Danh_Rig` (đề xuất): skeleton người tối giản + shader-billboard phẳng (hook-only, không khóa shader).
- **Required sockets/hooks:** `face_mask_socket`, `mirror_anchor`, `shadow_core`, `name_glyph`.
- Khi nó mặc mặt Long Nhân, silhouette phải **gần** người chơi nhưng bóng in ra **rỗng** — tín hiệu đọc thật/giả.

### Source and license record

- **Source strategy:** procedural/custom; shader bóng là hook, không khóa.
- **Cultural review:** đảm bảo "bóng không mặt" không vay motif kinh dị ngoại lai; bám chất "mất tên" của đầm Tây Hồ.

## Acceptance checklist

- [ ] Hồ Tinh đọc là **cáo đầm Việt** (ma trơi, lau sậy), không phải hồ ly tinh Đông Á quyến rũ.
- [ ] Bóng Vô Danh đọc là **người mất tên**, không phải quỷ kinh dị vô cớ.
- [ ] Không mây cuộn/long văn/hanfu/giáp cung đình Trung Hoa/motif Nhật trong asset final.
- [ ] Cơ chế "bóng in hình cáo" (thật/giả) đọc được ở gameplay distance.
- [ ] `B02-P0` không bị tính nhầm thành combat phase; hai combat phase phân biệt rõ.
- [ ] Chín đuôi có socket tên riêng; ngọn lửa-tên không che silhouette trước đòn lớn.
- [ ] Source, license, `.blend`, preview, build script được ghi (dù hiện là `TBD`).
- [ ] Cultural review hoàn tất trước khi content chuyển `approved`/`locked`.

## Dependencies and handoff

| Owner | Dependency | Status |
| --- | --- | --- |
| Art | Blockout Hồ Tinh (2 silhouette) + Bóng Vô Danh; chất liệu đầm/ma trơi; cultural review | `draft` |
| Animation | Rig cáo 9 đuôi; mask-swap cho mặt vay; bóng phẳng billboarding | `draft` |
| VFX | Sương, ma trơi, `Phân Thân` (ảo ảnh đất sét), gương nước, bóng chảy | `hook-only` |
| Gameplay | Socket tên (9 đuôi), cơ chế đọc bóng/gương, targetable region | `hook-only` |
| Audio | Tiếng hát không tên; giọng Hồ Tinh chồng nhiều mặt; tiếng "gọi tên" | `draft` |
| Narrative | Phase lines, fate variants, release/absorb state, hidden truth | `approved-source` |
