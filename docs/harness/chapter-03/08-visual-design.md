# CH-03 Visual Design Harness

## Purpose

Đây là nguồn chuẩn cho ngoại hình và cách đọc hình ảnh của các nhân vật/sinh vật quan trọng trong CH-03. Tài liệu khóa hướng art direction ở mức đủ để dựng, review và thay asset; chưa khóa topology, texture resolution, animation frame hoặc engine implementation.

> **Long Nhân** dùng lại character card đã khóa tại `docs/harness/chapter-01/08-visual-design.md#character-card-long-nhan` (không định nghĩa lại ở đây). CH-03 chỉ bổ sung **wear theo chương**: vết cào của rễ, nhựa máu khô sẫm ở lưỡi rìu/gấu áo, bùn rừng Phong Châu, và (ở nhánh absorbed) vệt đen dưới da cẳng tay. Silhouette, outfit layers, socket và palette của Long Nhân không đổi.

## Shared art direction

### Visual thesis

CH-03 là một **nghĩa địa bị rừng ăn từ bên trong**: hình khối phải nặng, ẩm, bị rễ trói và kéo lệch trục; dấu vết kinh đô cũ (đá tảng, chân cột, bia) bị thân cây nuốt một nửa. Mọi sinh vật phải đọc được trong silhouette trước khi người chơi thấy chi tiết: **rễ = dây trói**, **lõi đỏ = trái tim vay máu**, **xác = còn giữ thế lính**.

### Vietnamese visual language

Được phép dùng các nguồn cảm hứng đã ghi nhận:

- Hoa văn hình học Đông Sơn trên bia/vòng đồng/when khiên: tia mặt trời, vòng tròn đồng tâm, răng cưa, ziczac, hình chim cách điệu tiết chế.
- Giáp/vũ khí Lạc Việt cổ: vòng đồng oxy hóa, khiên, giáo, dấu thắt nút dây thề; vải thô quấn phù hợp vận động.
- Vật liệu rừng nhiệt đới: gỗ mục, rễ, rêu, dây leo, lá rộng, bùn; đá kinh đô cũ rêu phủ.
- Bảng màu: vỏ cây xám nâu, gỗ ẩm, rêu lục sẫm, **đỏ máu lõi** (điểm nhấn), đồng oxy hóa, và màu "nhựa máu" nâu đen.

Không được dùng:

- Mây cuộn, long văn, đế hiệu, giáp cung đình hoặc hoa văn nhận diện rõ từ mỹ thuật đế chế Trung Hoa.
- Hanfu, cổ áo/tay áo mô phỏng Trung Hoa; kimono, samurai hay motif Nhật.
- Rồng bốn móng, đầu rồng cung đình, phượng hoàng cung đình, biểu tượng không có lý do trong canon.
- **Biến Mộc Tinh thành "ent"/"người cây" fantasy phương Tây** có mặt người hiền từ, râu rêu, tay cành đối xứng trang trí. Mộc Tinh là **cây cổ thụ ăn máu/quân hóa xác**, đáng sợ và vô nhân xưng.
- Ornament phủ kín làm mất silhouette, đặc biệt ở khoảng cách camera gameplay.

### Shared technical rules

- Mọi phụ kiện gameplay phải có `attachment/socket` rõ ràng.
- Tay/chân (và rễ dùng như chi) tuân theo pose trung tính; không mirror sai trục để chữa hướng.
- Vũ khí (rìu, giáo, khiên) phải có trục lưỡi/mũi, điểm cầm và hướng sheath ghi trước khi rig.
- Asset nguồn chỉ là nền; provenance không phải canon văn hóa; mọi chi tiết lọc qua mục motif cấm.
- Preview dùng để review design intent, không thay kiểm tra file `.blend` và rig.

## Character card: B-03 Mộc Tinh

### Identity

- **ID:** `B-03`
- **Role:** Chapter 3 boss; cổ thụ yêu khí ăn máu và quân hóa xác chết.
- **Visual thesis:** Một cây tổ đã nuốt nghĩa địa và kinh đô cũ; mỗi vong linh nó giữ là một nút rễ; lõi đỏ của nó đập như một trái tim đi vay máu.
- **Player read:** Boss thực vật ký sinh, nhiều "chi" là rễ, có **lõi đỏ** là trung tâm; không phải ent phương Tây, không mặt người.

### Silhouette and anatomy

- Dáng cổ thụ khổng lồ, gốc phình, nhiều rễ lớn trồi lên như chi; thân chính có các **hốc rễ** chứa xác (đầu lâu/giáp lộ ra một phần).
- Không có mặt người; "đầu" là tán cây và một **khối lõi đỏ** thấp trong thân (chỉ lộ rõ ở phase 2).
- Vong binh xác-rễ là phần mở rộng của boss trong arena: dáng còn giữ thế lính (cầm giáo/khiên mục), rễ xuyên qua giáp.
- Phân biệt rõ **rễ ký sinh** (căng, bóng, đỏ-nâu, siết) với **rễ tự-nguyện** của `HB-03` (mềm, sáng nhạt, buông) — hai ngôn ngữ silhouette khác nhau.

### Boss phase variants

| Phase | Visual change | Narrative read |
| --- | --- | --- |
| `B03-P0` | Chỉ có rễ động và bóng khối lớn trong sương; lõi chưa lộ | Quy mô và sự "rừng đang thức"; không tính combat phase |
| `B03-P1-GRAFT` | Thân dựng, hốc rễ mở, xác-rẽ trồi lên như chi | Mộc Tinh còn "chăn" vong binh, đọc được ý chí giữ lời thề |
| `B03-P2-CORE` | Vỏ nứt, **lõi đỏ** lộ, rễ thành roi, arena sụp thành mạng rễ | Phần "cây" nuốt phần "tỉnh táo"; máu vay phải trả |
| `B03-RELEASED` | Lõi đỏ dịu thành ánh vàng nâu; rễ buông xác; tán khép lại như buông | Giải phóng, không phải chiến thắng tuyệt đối |
| `B03-ABSORBED` | Lõi đỏ bị kéo vào người chơi; thân rỗng, vệt đen chạy dưới da Long Nhân | Cưỡng đoạt: lợi ích + cost, "kẻ cầm dây mới" |

### Materials, palette, wear

| Token | Hex | Use |
| --- | --- | --- |
| `MOC_BARK_GREY` | `#4A4238` | Vỏ cây, bóng thân |
| `MOC_WOOD_WET` | `#6B4F36` | Gỗ ẩm, mặt cắt rễ |
| `MOC_MOSS` | `#3C4A2E` | Rêu, tán lá bệnh |
| `MOC_BLOOD_CORE` | `#7E2018` | Lõi đỏ, nhựa máu, telegraph nguy hiểm |
| `MOC_ROOT_FIBER` | `#8A6A4A` | Rễ ký sinh căng |
| `MOC_BRONZE_OX` | `#6E7764` | Vòng đồng/vật tùy táng Đông Sơn |
| `MOC_JADE` | `#75B5A0` | `LG-03`, vùng memory reveal |

Vỏ cây hút sáng, gỗ bán ẩm, lõi đỏ phát sáng yếu từ bên trong (không như đèn neon). Nhựa máu đặc, không loang như máu tươi. Yêu khí dùng rễ, bào tử tiết chế và nhiễu màu nâu-đỏ; tránh khói mây cuộn kiểu rồng.

### Arena attachments and combat readability

- **Boss blend:** `TBD` (chưa có asset; dependency `ART-BOSS-MOC-TINH`).
- **Preview:** `TBD`.
- **Build script:** `TBD`.
- **Rig:** đề xuất `Moc_Tinh_Combat_Rig` (blockout; cần art/animation review trước production lock).
- **Required sockets/hooks:** `core_red`, `root_limb_l`, `root_limb_r`, `graft_nodule_*` (nút rễ), `bark_plate`, `long_ngoc_core`.
- Lõi đỏ phải luôn cho người chơi đoán được khi nào lộ (sau nhịp đập mạnh/đợt quét); không biến thành weak-point UI giả.
- `LG-03` nhìn thấy trong cửa sổ narrative (đã ghi ở `05-boss-encounter.md`), gắn với `core_red`, không phải ngọc gắn trán.

### Source and license record

- **Source strategy:** dự kiến asset procedural/custom dựng trong repository (như Ngư Tinh); chưa có mesh. Không gắn license bên thứ ba cho tới khi có asset.
- **External asset policy:** nếu thay bằng source library, chỉ nhận asset license thương mại hoặc CC0 tương thích; ghi URL, phiên bản, tác giả, phạm vi sửa trong manifest.
- **Cultural review:** bắt buộc trước khi thêm motif bề mặt. Ưu tiên sinh học cây/rễ nhiệt đới + di vật Đông Sơn hơn ornament; giữ bản sắc CH-03, tránh "ent phương Tây".

## Character card: HB-03 Tướng Quân Vô Đầu

### Identity

- **ID:** `HB-03`
- **Role:** Hidden boss (Oan Khuất Ẩn, ADR-004); chỉ huy quân Lạc Việt cũ, **tự** trói mình vào lời thề.
- **Visual thesis:** Một thân tướng không đầu, giáp đồng Lạc Việt, quỳ giữ một nút rễ do chính mình chọn; chỗ đáng ra là đầu chỉ còn một gông rễ tự-nguyện buông.
- **Player read:** Dáng người (không phải cây), **thiếu đầu**, rễ quanh ông **mềm/sáng** (tự nguyện) khác hẳn rễ ký sinh của Mộc Tinh.

### Silhouette and anatomy

- Tỷ lệ người trưởng thành, vai rộng, thế quỳ/đứng găm giáo; **cổ cụt** không máu tươi (đã khô thành gỗ/đồng).
- Giáp: vòng đồng oxy hóa, mảnh giáp Lạc Việt, thắt nút dây thề ở ngực/vai; không giáp cung đình Trung Hoa.
- Rễ tự-nguyện: sáng nhạt, mềm, buông xuống như đặt xuống, không siết; một **nút thề** lớn ở ngực là điểm đọc.
- "Đầu" bị mất: có thể gợi một **hốc đầu bằng rễ** trống, hoặc mũ giáp rỗng đặt cạnh — danh tính còn thiếu.

### Hidden boss phase variants

| Phase | Visual change | Narrative read |
| --- | --- | --- |
| `HB03-P0` | Quỳ bất động trong gò mộ; rễ tự-nguyện buông | Sự hiện diện, không phải tấn công; intro không-đánh |
| `HB03-P1-OATHGUARD` | Đứng dậy, giáo/khiên, rễ tự-nguyện đỡ đòn | Ông giữ lời thề vì sợ bị quên, không vì bị ép |
| `HB03-RELEASED` | Đặt giáo, nút thề ở ngực mở, hốc đầu đầy ánh sáng mờ; thân tan thành rễ sáng | Buông lời thề, trả lại danh tính |
| `HB03-ABSORBED` | Nút thề bị kéo vào người chơi; thân sụp thành gỗ rỗng, vệt đen dưới da Long Nhân | Cưỡng đoạt: "chủ nợ" lời thề cũ |

### Materials, palette, wear

| Token | Hex | Use |
| --- | --- | --- |
| `TUONG_BRONZE_OX` | `#6E7764` | Giáp/vòng đồng oxy hóa |
| `TUONG_LAC_RED` | `#8E3A2C` | Dây thề, vải buộc cũ (đỏ son phai) |
| `TUONG_BONE_DRY` | `#9A8C6E` | Cổ cụt khô hóa gỗ/xương |
| `TUONG_ROOT_FREE` | `#A9B79A` | Rễ **tự-nguyện** (sáng, mềm) |
| `TUONG_JADE` | `#75B5A0` | Điểm memory reveal (`hidden_truth`) |

Giáp xước, đồng oxy hóa, vải thề phai màu; rễ tự-nguyện phát sáng rất nhẹ để phân biệt với rễ ký sinh (`MOC_ROOT_FIBER`). Không máu me như phần thưởng.

### Arena attachments and combat readability

- **Boss blend:** `TBD` (dependency `ART-BOSS-TUONG-VO-DAU`).
- **Preview:** `TBD`. **Build script:** `TBD`.
- **Rig:** đề xuất `Tuong_Vo_Dau_Combat_Rig` (humanoid blockout + root attachment).
- **Required sockets/hooks:** `neck_stump`, `chest_oath_knot`, `hand_r_spear`, `arm_l_shield`, `root_free_base`, `head_socket` (trống), `memory_core`.
- Rễ tự-nguyện phải đọc khác rễ ký sinh ngay ở silhouette/material để người chơi hiểu "ông không bị Mộc Tinh ép".

### Source and license record

- **Source strategy:** dự kiến procedural/custom (như Ngư Tinh); chưa có mesh.
- **External asset policy:** như B-03 (CC0/thương mại tương thích; ghi manifest).
- **Cultural review:** bắt buộc; "không đầu" xử lý trang trọng (mất danh tính/lời thề chưa trọn), không horror khai thác.

## Acceptance checklist

- [ ] Long Nhân giữ đúng card CH-01; CH-03 chỉ thêm wear theo chương.
- [ ] Không có mây cuộn, long văn, hanfu, giáp cung đình Trung Hoa hay motif Nhật trong asset final.
- [ ] Mộc Tinh đọc là **cây cổ thụ ăn máu/quân hóa xác**, KHÔNG phải ent fantasy phương Tây có mặt người.
- [ ] Rễ ký sinh (B-03) và rễ tự-nguyện (HB-03) phân biệt rõ bằng silhouette/material/màu.
- [ ] `HB-03` đọc là tướng Lạc Việt **không đầu** (mất danh tính), không phải horror chặt đầu khai thác.
- [ ] Intro `B03-P0` và `HB03-P0` không bị tính nhầm thành combat phase.
- [ ] Hai combat phase của B-03 phân biệt rõ: GRAFT (chăn xác-rễ) và CORE (lõi đỏ).
- [ ] Lõi đỏ và `LG-03` có socket rõ, không thành weak-point UI giả.
- [ ] Source, license, `.blend`, preview, build script được ghi (hoặc `TBD` có dependency) và resolve trước lock.
- [ ] Cultural review hoàn tất trước khi content chuyển `approved`/`locked`.

## Dependencies and handoff

| Owner | Dependency | Status |
| --- | --- | --- |
| Art | Mộc Tinh + Tướng Quân Vô Đầu concept, modular roots, material pass, cultural review | `draft` |
| Animation | Root-limb rig, xác-rễ thế lính, humanoid `HB-03`, stance poses | `draft` |
| VFX | Lõi đỏ, nhựa máu, bào tử, rễ ký sinh vs tự-nguyện, Long Ngọc reveal | `hook-only` |
| Gameplay | Socket names, phase readability, targetable nodule/core, arena rễ chuyển động | `hook-only` |
| Narrative | Phase lines, fate variants, release/absorb/sacrificed state, hidden_truth | `approved-source` |
