# CH-04 Visual Design Harness

## Purpose

Nguồn chuẩn cho ngoại hình và cách đọc hình ảnh của các nhân vật/sinh vật quan trọng trong CH-04. Khóa hướng art direction ở mức đủ để dựng, review và thay asset; **chưa** khóa topology, texture resolution, animation frame hay engine implementation. Long Nhân dùng lại card toàn cục ở `chapter-01/08-visual-design.md`; file này chỉ bổ sung ghi chú riêng cho CH-04.

## Shared art direction

### Visual thesis

CH-04 là một **đài tưởng niệm bị xóa**: hình khối phải cao, lạnh, lởm chởm đá và sương, có chiều thẳng đứng áp đảo và những khoảng trống gió. Mọi thứ phải đọc được trong **silhouette trên nền trời/nền vực** trước khi thấy chi tiết. Chủ đề thị giác: *đá biết khóc, lông vũ giam hồn, và một con chim lớn mang tiếng gào của nhiều người*.

### Vietnamese visual language

Được phép dùng các nguồn cảm hứng đã ghi nhận:

- Hoa văn hình học Đông Sơn: tia mặt trời, vòng tròn đồng tâm, răng cưa, ziczac, hình chim cách điệu (chim Lạc) **tiết chế** — dùng cho bia đá, rìu, đồ tùy táng của bộ tộc, không phủ kín.
- Cấu trúc vải quấn/giao lĩnh phù hợp vận động cho NPC bộ tộc; sash và dây buộc đỏ là điểm nhận diện Lạc Việt.
- Vật liệu: đá núi, sương, lông vũ lớn, đồng oxy hóa, gỗ bia cũ, "lệ đá" (khoáng trong mờ như nước mắt đông cứng).
- Bảng màu: xám đá lạnh, trắng sương, đồng oxy hóa, đỏ son tiết chế, và ánh hổ phách/xanh của ký ức khi được gọi tên.

Không được dùng:

- Mây cuộn, long văn, đế hiệu, giáp cung đình, hoa văn nhận diện rõ từ mỹ thuật đế chế Trung Hoa.
- **Phượng hoàng cung đình** hoặc "đại bàng huy chương/quân đội" — Đại Bàng Tinh là **yêu quái chim lớn bi kịch**, không phải biểu tượng quyền lực huy hoàng.
- Hanfu, cổ áo/tay áo mô phỏng Trung Hoa; kimono, samurai hay motif Nhật.
- Rồng bốn móng, đầu rồng cung đình, biểu tượng không có lý do trong canon.
- Ornament phủ kín làm mất silhouette, đặc biệt ở khoảng cách camera gameplay và trên nền trời.

### Shared technical rules

- Mọi phụ kiện gameplay phải có `attachment/socket` rõ ràng.
- Tay/chân tuân theo anatomical pose trung tính; không mirror sai trục để chữa hướng bàn chân.
- Vũ khí (Rìu Thần Thạch Sơn) giữ trục lưỡi, điểm cầm, hướng sheath đã ghi ở card CH-01.
- Asset nguồn chỉ là nền; provenance không phải canon văn hóa — mọi chi tiết lọc qua mục motif cấm.
- Preview dùng để review design intent, không thay thế kiểm tra `.blend` và rig.
- Chiều thẳng đứng và gió là **contract gameplay**: silhouette boss phải đọc được khi người chơi ở dưới/trên và khi gió đổi hướng.

## Character card: Long Nhân (ghi chú CH-04)

- **ID:** `PLAYER-LONG-NHAN` (card đầy đủ: `chapter-01/08-visual-design.md#character-card-long-nhan`).
- **CH-04 read:** giữ ba điểm nhận diện (đầu/tóc buộc, sash đỏ, Rìu Thần Thạch Sơn). Ở chương núi cao, sash và vạt áo phải **đọc được hướng gió** (bay theo luồng gió đổi hướng) vì gió là cơ chế.
- **Pose:** trọng tâm thấp, sẵn sàng đổi hướng trên bệ đá hẹp; có pose leo/bám (hook `NGUYEN-THAN-TINH-VUON`, optional) và pose chịu đứt gãy trọng lực.
- **Không đổi silhouette cơ bản** so với CH-01; khác biệt đến từ bối cảnh (đá/sương/gió) và trạng thái ký ức (ánh hổ phách mảnh khi `TRUTH_EXILE_WAS_ERASED` phản ứng).

## Character card: B-04 Đại Bàng Tinh

### Identity

- **ID:** `B-04`
- **Role:** Chapter 4 boss; yêu quái chim lớn, **vật chứa phẫn nộ của những người bị xóa tên**.
- **Myth inspiration:** chim lớn (Đại Bàng) trong truyện Thạch Sanh — nhưng ở đây là một oan thể tập thể, không phải con chim dữ săn công chúa theo nghĩa đen.
- **Visual thesis:** một con chim khổng lồ mà mỗi chiếc lông là một cái tên bị xóa; thân thể nó là **đài tưởng niệm bay** của một bộ tộc mất tích; nó gào bằng tiếng của nhiều người.
- **Player read:** hai hình thái chiến đấu rõ — **một con chim bổ nhào** (P1) và **đàn lông vũ hợp thành nhiều bóng** (P2). Không bao giờ đọc thành phượng hoàng/đại bàng huy chương.

### Silhouette and anatomy

- **P1 (một con chim):** sải cánh rất rộng, đọc được trên nền trời; đầu chim lớn, mỏ cong nặng, cổ dày; chân có móng bám bệ đá hẹp; đuôi dài làm bánh lái khi bổ nhào. Silhouette phải **bất đối xứng nhẹ** (một bên cánh xơ xác, rụng lông) để gợi vết thương/lưu đày, không phải chim thần hoàn mỹ.
- **P2 (đàn lông):** thân chính tan thành **vòng xoáy lông vũ** quanh một lõi sáng (`LG-04`); nhiều bóng chim nhỏ hợp-tan liên tục; trọng lực quanh lõi bị bẻ (đá và lông trôi lơ lửng). Silhouette tổng là một **cơn bão hình chim**, không phải một cá thể.
- Lông vũ lớn, có thể cắm vào bệ đá thành hazard; một số lông **gim hồn** (ánh sáng yếu, mặt người thoáng hiện) — dùng lại ngôn ngữ hình ảnh của `CH-04-S02`.
- Mắt: hổ phách khi còn "một con"; ở P2 nhiều mắt nhỏ mở trên các bóng, đồng bộ khi gào.
- Không sừng rồng, không bờm, không vảy rồng, không vân mây cuộn.

### Boss phase variants

| Phase | Visual change | Narrative read |
|---|---|---|
| `B04-P0` | Bóng cánh phủ qua vực; chỉ thấy silhouette ngược sáng và gió đổi hướng | Quy mô và sự quan sát trước khi chiến; không tính là combat phase |
| `B04-P1-DIVE` | Một con chim lớn, cánh bất đối xứng, bổ nhào và quạt gió; lông gim xuống bệ đá | Phẫn nộ còn "một mối", nhắm vào Long Nhân như kẻ cai trị mới |
| `B04-P2-VESSEL` | Thân tan thành vòng xoáy lông vũ quanh lõi sáng; đá/lông trôi trong trọng lực bị bẻ; nhiều bóng chim | Vật chứa mở ra: tiếng gào của nhiều người bị xóa tên |
| `B04-RELEASED` | Lông vũ buông hồn; vòng xoáy lắng; lõi `LG-04` sáng ấm; một bóng chim đơn độc bay lên | Phẫn nộ được gọi tên và đặt xuống |
| `B04-ABSORBED` | Lõi và lông bị kéo vào người chơi; bão sụp thành bụi đá tối; vệt đen dưới da Long Nhân | Cưỡng đoạt: lợi ích kèm cost ký ức nhiễu |

### Materials, palette, wear

| Token | Hex | Use |
|---|---|---|
| `DB_STONE_GREY` | `#4A4F55` | Lông đá, bệ núi, bóng thân |
| `DB_MIST_WHITE` | `#C9D2D6` | Sương, viền lông ngược sáng |
| `DB_BRONZE_OXIDE` | `#6E7764` | Móng, mỏ, chi tiết Đông Sơn trên bia |
| `DB_LAC_RED` | `#A9352B` | Dây buộc/dấu Lạc trên hồn được giải thoát (tiết chế) |
| `DB_AMBER_EYE` | `#D88B35` | Mắt, lõi `LG-04`, điểm khóa mục tiêu |
| `DB_STONE_TEARS` | `#7FA6A0` | Lệ đá, khoáng trong mờ |
| `DB_YEU_STATIC` | `#8C6BB1` | Nhiễu yêu khí tím-xám khi trọng lực bẻ (tiết chế, không neon) |

Lông vừa sừng vừa khoáng (cứng như đá mỏng), không lông vũ mượt kiểu chim thần. Đứt gãy trọng lực biểu hiện bằng **đá/lông trôi chậm + méo không khí nhẹ**, không bằng hiệu ứng phép rực rỡ. Yêu khí dùng bụi đá, sương và nhiễu màu tiết chế; tránh khói mây cuộn.

### Arena attachments and combat readability

- **Arena:** tổ trên đỉnh Thạch Môn — bệ đá hẹp nhiều tầng, cột đá, vực; gió đổi hướng theo chu kỳ; các "neo tổ/đàn" (3 bia/đống lông) là điểm bond.
- **Required sockets/hooks (đề xuất, chưa khóa):** `beak`, `wing_l`, `wing_r`, `tail`, `talons_l`, `talons_r`, `feather_socket_*`, `core_long_ngoc`, `eye_main`.
- **Đọc được đòn:** cánh gập + thân thuôn = telegraph bổ nhào; hướng cờ sương/đá trôi = telegraph gió; đá/lông nhấc khỏi nền = telegraph đứt gãy trọng lực; lõi sáng = cửa sổ bond.
- **Không** biến lõi thành weak-point UI giả; `LG-04` chỉ lộ trong các cửa sổ narrative đã ghi ở `05-boss-encounter.md`.

### Source and license record

- **Source strategy:** boss dự kiến là asset procedural/custom dựng trong repository (như Ngư Tinh CH-01); chưa có mesh final.
- **External asset policy:** nếu thay bằng source library, chỉ nhận asset license thương mại hoặc CC0 tương thích; ghi URL, phiên bản, tác giả, phạm vi sửa trong manifest.
- **Cultural review:** bắt buộc trước khi thêm motif bề mặt và trước khi content chuyển `approved`/`locked`. Ưu tiên sinh học chim lớn + ngôn ngữ đá/sương Đông Sơn hơn là ornament huy hoàng.

## Character card: HB-04 Tù Trưởng Lệ Đá

### Identity

- **ID:** `HB-04` (Oan Khuất Ẩn, ADR-004)
- **Role:** hidden boss tùy chọn; **nhân chứng cuối** của một bộ tộc bị xóa tên; không phải boss cổng.
- **Visual thesis:** một tù trưởng hóa đá giữa rừng bia không tên, nước mắt đông thành "lệ đá" chảy mãi; cơ thể là **tấm bia sống** chưa được khắc tên.
- **Player read:** một tượng đá-người ngồi/quỳ, rêu và sương bám, khe nứt phát sáng yếu nơi "lệ đá" rỉ ra; đọc là **trang nghiêm**, không phải quái vật.

### Silhouette and anatomy

- Hình người hóa đá, tỷ lệ gần người thật nhưng **nặng, đặc, liền khối** với bệ đá; posture quỳ/ngồi ôm một tấm bia trống.
- Khuôn mặt mòn theo thời gian nhưng còn đọc được nét một người già dignified; một **vệt lệ đá** trong mờ chạy từ khóe mắt xuống má, phát sáng yếu khi người chơi đến gần có chủ ý.
- Trang phục: khố/áo quấn bộ tộc núi, hoa văn Đông Sơn tối giản khắc nông; một vòng cổ/mão tù trưởng bằng đồng oxy hóa đã gãy một phần.
- Xung quanh: **rừng bia không tên** (các cột đá trống), mỗi bia là một người bị xóa; một số bia đã khắc lại mờ (dấu của Bà Lệ qua nhiều đời).

### Hidden phase variants

| Phase | Visual change | Narrative read |
|---|---|---|
| `HB04-P1-LAMENT` | Lệ đá rỉ mạnh, sương dày lên quanh khe đá, các bia trống rung nhẹ | Nỗi đau im lặng; không tấn công, chỉ "giữ" người vào trong ký ức |
| `HB04-P2-WITNESS` | Tù trưởng ngẩng lên; khe nứt ngực hé tên bị đục; rừng bia đồng loạt hiện chữ mờ rồi tắt | Đối mặt: đưa ra lựa chọn khắc tên hay cưỡng đoạt |
| `HB04-RELEASED` | Tên sáng lên trên bia ngực; lệ đá ngừng; thân đá nứt nhẹ và lặng đi; một bóng bộ tộc đứng thẳng lại | Tên được trả; phẫn nộ lắng |
| `HB04-ABSORBED` | Lệ đá bị kéo vào người chơi; bia ngực vỡ; rừng bia mờ hẳn | Cưỡng đoạt: sức mạnh kèm xóa thêm một lần nữa |

### Materials, palette, wear

| Token | Hex | Use |
|---|---|---|
| `HB_GRANITE` | `#5B5F63` | Thân đá, bia |
| `HB_MOSS` | `#4F5D45` | Rêu, vết thời gian (tiết chế) |
| `HB_STONE_TEARS` | `#7FA6A0` | Lệ đá trong mờ, phát sáng yếu |
| `HB_BRONZE_OXIDE` | `#6E7764` | Mão/vòng tù trưởng, hoa văn Đông Sơn |
| `HB_NAME_GLOW` | `#D8C79A` | Ánh sáng ấm khi tên được khắc/gọi đúng |

Đá bán mờ ở vệt lệ; bề mặt bia khắc nông, không chữ hiện đại. Không dùng hiệu ứng "tượng thần phát sáng" kiểu fantasy generic; ánh sáng chỉ đến khi **tên được công nhận**.

### Arena attachments and combat readability

- **Arena hidden (`CH-04-HIDDEN`):** "Khe đá dựng" — một hẻm núi hẹp đầy bia trống, gió lặng (tương phản với bão gió của B-04), ánh sáng lọt qua khe.
- **Required sockets/hooks (đề xuất):** `head`, `chest_stele`, `tear_track_l`, `tear_track_r`, `hand_offering`, `stele_field_*`.
- **Không có damage weak-point.** Tương tác là: lắng nghe, khắc/gọi tên, hoặc cưỡng đoạt lệ đá. Đọc được qua ánh sáng vệt lệ và phản ứng rừng bia.

### Source and license record

- **Source strategy:** dự kiến procedural/custom; chưa có mesh final.
- **Cultural review (bắt buộc):** chủ đề "bộ tộc bị xóa tên" là bi kịch có thật của lịch sử — xử lý **trang trọng**, không bi kịch hóa để câu cảm xúc rẻ, không gán cho một tộc người/danh tính có thật cụ thể; giữ ở mức hư cấu "lấy cảm hứng từ" (01 §11). Tránh mọi biểu tượng có thể đọc thành miệt thị một nhóm dân tộc.

## Acceptance checklist

- [ ] Long Nhân đọc được như nhân vật lấy cảm hứng Việt Nam; sash/vạt áo đọc hướng gió ở CH-04.
- [ ] Đại Bàng Tinh đọc là **yêu quái chim lớn bi kịch**, không phải phượng hoàng/đại bàng huy chương; không motif Trung/Nhật.
- [ ] Hai phase của B-04 phân biệt rõ silhouette: một con chim vs đàn lông nhiều bóng quanh lõi.
- [ ] `B04-P0` không bị tính nhầm thành combat phase.
- [ ] Lệ đá / rừng bia không tên đọc là trang nghiêm, không phải "tượng thần phát sáng" generic.
- [ ] HB-04 có visual card riêng, phân biệt với B-04; không weak-point UI.
- [ ] Đứt gãy trọng lực biểu hiện bằng đá/lông trôi + méo không khí tiết chế, không phép rực rỡ.
- [ ] Không có damage/HP/frame/shader/asset path bị khóa (R-05); source/license/provenance ghi là TBD/procedural.
- [ ] Cultural review hoàn tất (cả B-04 và HB-04) trước khi content chuyển `approved`/`locked`.

## Dependencies and handoff

| Owner | Dependency | Status |
|---|---|---|
| Art | Đại Bàng Tinh 2-phase identity, rừng bia/lệ đá, cultural review | `draft` |
| Animation | Chim: bổ nhào/quạt gió/bám bệ; P2: đàn lông hợp-tan; HB-04: tượng đá tối giản | `draft` |
| VFX | Gió, đứt gãy trọng lực (đá/lông trôi), lệ đá, lõi `LG-04` reveal, yêu khí tiết chế | `hook-only` |
| Gameplay | Bệ đá hẹp, gió đổi hướng, trọng lực bẻ, socket, targetable region (lõi) | `hook-only` |
| Narrative | Phase lines (nhiều giọng), fate variants, hidden naming interaction | `approved-source` |
| Audio | Tiếng gào nhiều lớp, gió vực, lệ đá, sấm `Lôi Kích` | `hook-only` |
