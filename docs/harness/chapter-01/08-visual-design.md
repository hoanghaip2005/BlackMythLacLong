# CH-01 Visual Design Harness

## Purpose

Đây là nguồn chuẩn cho ngoại hình và cách đọc hình ảnh của các nhân vật quan trọng trong CH-01. Tài liệu khóa hướng art direction ở mức đủ để dựng, review và thay asset; chưa khóa topology, texture resolution, animation frame hoặc engine implementation.

## Shared art direction

### Visual thesis

CH-01 là một ký ức bị nhấn chìm: hình khối phải nặng, ướt, chịu áp lực nước, nhưng vẫn có dấu vết của một nền văn hóa từng sống quanh sông biển. Mọi nhân vật phải đọc được trong silhouette trước khi người chơi nhìn thấy chi tiết.

### Vietnamese visual language

Được phép dùng các nguồn cảm hứng đã ghi nhận:

- Hoa văn hình học Đông Sơn: tia mặt trời, vòng tròn đồng tâm, răng cưa, đường ziczac, hình chim cách điệu có tiết chế.
- Áo giao lĩnh, áo tứ thân và cấu trúc vải quấn phù hợp vận động; chỉ dùng như cảm hứng thiết kế, không sao chép trang phục nghi lễ hiện đại một cách máy móc.
- Đồng đỏ, đá, vỏ sò, ngọc sông, dây dệt đỏ và vật liệu thuyền biển.
- Bảng màu đất nung, đồng oxy hóa, xanh nước sâu, đỏ son và hổ phách.

Không được dùng:

- Mây cuộn, long văn, đế hiệu, giáp cung đình hoặc hoa văn nhận diện rõ từ mỹ thuật đế chế Trung Hoa.
- Hanfu, cổ áo và tay áo mô phỏng Trung Hoa; kimono, samurai hoặc motif Nhật.
- Rồng bốn móng, đầu rồng cung đình, phượng hoàng cung đình hay biểu tượng không có lý do trong canon.
- Ornament phủ kín bề mặt làm mất silhouette, đặc biệt ở khoảng cách camera gameplay.

### Shared technical rules

- Mọi phụ kiện gameplay phải có `attachment/socket` rõ ràng.
- Tay và chân phải tuân theo anatomical pose trung tính; không dùng mesh mirror sai trục để chữa lỗi hướng bàn chân.
- Vũ khí phải có trục lưỡi, điểm cầm và hướng sheath được ghi trước khi rig.
- Asset nguồn chỉ là nền. Không coi provenance của asset là canon văn hóa; mọi chi tiết lấy từ asset phải được lọc qua mục motif cấm.
- Preview dùng để review design intent, không thay thế kiểm tra file `.blend` và rig.

## Character card: Long Nhân

### Identity

- **ID:** `PLAYER-LONG-NHAN`
- **Role:** Player character; silent witness becoming an active bearer of memory.
- **Visual thesis:** Một người sống sót từ đáy biển, thân thể chưa thuộc về đất liền, mang dấu vết rồng như một vết sẹo đang học cách phát sáng.
- **Player read:** Nhân vật humanoid trẻ trưởng thành, nhanh và thấp trọng tâm; silhouette có vai gọn, vạt áo tách lớp, vũ khí lớn hơn vẻ ngoài của người cầm.

### Silhouette and proportion

- Tỷ lệ gần người thật, hơi dài tay để đọc rõ đòn đánh; không dùng tỷ lệ thần tiên hoặc giáp phồng.
- Vai và hông lệch nhẹ theo tư thế chiến đấu; trọng tâm ở giữa bàn chân, sẵn sàng đổi stance.
- Vạt áo giao lĩnh/tứ thân tách thành hai mảng để tạo nhịp khi xoay người; sash đỏ là đường nhận diện ngang thân.
- Trong gameplay, ba điểm phải đọc trước: đầu và tóc buộc, sash đỏ, Rìu Thần Thạch Sơn.
- Bàn chân hướng theo trục di chuyển; ngón chân không xoay ngược, gót không xuyên nền, hai đầu gối không khóa cứng trong pose trung tính.

### Face, hair, eyes

- Gương mặt người Việt trẻ trưởng thành: xương mặt mềm nhưng có cạnh gò má và hàm rõ; không stylize theo mỹ thuật Trung Hoa.
- Da nâu ấm, có lạnh xanh ở vùng thiếu sáng dưới biển; không trắng sứ.
- Tóc đen dài vừa, buộc gọn sau gáy bằng dây dệt đỏ; vài lọn tóc ướt rơi trước trán sau khi thức tỉnh.
- Mắt nâu đậm ở trạng thái thường; ánh hổ phách rất mảnh chỉ xuất hiện khi Long Khí hoặc ký ức phản ứng.
- Biểu cảm mặc định: cảnh giác, thiếu ký ức, không phải vẻ mặt “thiên mệnh” tự tin.

### Outfit layers

| Layer | Mô tả | Chức năng đọc hình ảnh |
| --- | --- | --- |
| `LN-L01` | Lớp áo lót vải thô màu chàm đen, ôm vừa thân | Chống phản sáng, tạo nền cho lớp ngoài |
| `LN-L02` | Áo giao lĩnh biến thể vận động, vải nâu đất pha xanh biển, tà xẻ | Gợi cấu trúc Việt cổ, không thành hanfu; tách silhouette khi chạy |
| `LN-L03` | Dải vải đỏ son quấn eo, nút buộc lệch trái | Điểm nhận diện player; liên kết với dây tóc và các dấu buộc Lạc |
| `LN-L04` | Mảnh bảo hộ vai/cẳng tay bằng da sẫm và đồng oxy hóa | Bảo vệ khi cận chiến; không tạo thành giáp cung đình |
| `LN-L05` | Quần vải tối màu, bó vừa ở cổ chân | Giữ chân đọc rõ; hỗ trợ animation và nước |
| `LN-L06` | Phụ kiện chân bằng dây dệt và miếng đồng nhỏ | Nhịp chuyển động thấp; không dùng giày võ Trung Hoa |

### Weapon and accessories

- **Starting weapon:** `WEAPON-CH01-RUSTED-SHORTSWORD`. Đoản kiếm rỉ sét chỉ là vật sống sót ban đầu, lưỡi hẹp, chuôi quấn vải; không dùng guard kiểu kiếm Trung Hoa.
- **Chapter weapon:** `WEAPON-DONGSON-THACHSON-AXE`. Rìu Thần Thạch Sơn có đầu rìu đá/đồng lớn, sống rìu bất đối xứng, cán gỗ tối và dây buộc đỏ; mặt rìu có vòng tia mặt trời Đông Sơn tối giản.
- **Accessory:** `ACC-LN-RIVER-JADE`. Mảnh ngọc sông đục, đeo gần xương ức bằng dây đỏ; là vật dẫn ký ức, không phải huy hiệu quyền lực.
- **Attachment sockets:** `hand_r_weapon`, `back_weapon`, `waist_sash_left`, `chest_jade`, `hair_tie`, `forearm_guard_l`, `forearm_guard_r`.
- **Stance read:** Trảm mở vai và đưa cán ngang; Đột thu hẹp silhouette, mũi rìu hướng trước; Ngự kéo cán về gần thân, hai cẳng tay tạo khung chắn.

### Palette and material

| Token | Hex | Use |
| --- | --- | --- |
| `LN_INDIGO` | `#172A32` | Áo nền, bóng nước |
| `LN_EARTH` | `#6B4435` | Vải ngoài, da |
| `LN_LAC_RED` | `#A9352B` | Sash, dây buộc, nhịp nhận diện |
| `LN_OXIDIZED_BRONZE` | `#6E7764` | Bảo hộ, chi tiết Đông Sơn |
| `LN_RIVER_JADE` | `#628F87` | Ngọc và phản xạ ký ức |
| `LN_AMBER` | `#D88B35` | Mắt khi thức tỉnh, Long Khí |

Vải hút sáng, da bán mờ, đồng xước và oxy hóa; ngọc có độ trong thấp. Trạng thái mới tỉnh: nước nhỏ, rong mảnh, bùn ở gấu áo. Không biến Long Nhân thành sinh vật biển hoàn toàn.

### Asset and production record

- **Source asset library:** MPFB `2.0.17` + MakeHuman System Assets `CC0`; dùng làm base human mesh, thay outfit, tóc, phụ kiện và pose theo card này.
- **Weapon source:** `assets/weapons/dong_son_weapons.blend`.
- **Character blend:** `assets/characters/long_nhan/long_nhan_v3.blend`.
- **Preview:** `assets/characters/long_nhan/long_nhan_v3_hero.png` (hero) và `assets/characters/long_nhan/long_nhan_v3_portrait.png` (portrait).
- **Build script:** `tools/build_long_nhan_v3.py`.
- **License rule:** CC0 cho base asset; mọi texture/material mới phải ghi nguồn trong asset manifest trước khi đưa vào production.
- **Modification rule:** được thay mesh, material, outfit, tóc và attachment; không giữ ornament nguồn nếu vi phạm motif cấm.

### Rig and animation notes

- Giữ skeleton humanoid chuẩn từ base asset nếu tương thích; socket gameplay là contract, tên bone có thể map ở integration.
- Kiểm tra FK pose trung tính, stance pose, chạy, né và rút vũ khí với hai chân không đảo trục.
- Rìu phải xoay quanh grip thực, không quanh origin hình học đầu rìu.
- Nước làm vải nặng hơn qua animation/VFX hook; không cần đổi silhouette cơ bản ở Chapter 1.

## Character card: B-01 Ngư Tinh

### Identity

- **ID:** `B-01`
- **Role:** Chapter 1 boss; ancient fish yokai amplified by yêu khí and abandonment.
- **Visual thesis:** Một con cá vực sâu đã biến lời hứa bảo hộ thành bản năng giam giữ; thân thể là vết thương, đuôi lửa là ký ức bị ép cháy.
- **Player read:** Boss có hai hình thái chiến đấu rõ ràng: người lai cá có chủ ý và cá vực sâu khổng lồ mất kiểm soát; không dùng silhouette rồng Trung Hoa.

### Silhouette and anatomy

- Hình thái người lai cá cao khoảng 2.5 lần Long Nhân: thân trên dựng, vai rộng, hai tay có màng và móng; từ hông trở xuống là đuôi cá khỏe dùng để quật và trườn trên bệ ướt.
- Đầu vẫn là đầu cá vực sâu với hàm mở sâu, mắt tách hai bên và mang lộ; không gắn sừng, râu hoặc bờm rồng.
- Hình thái lai có vây lưng thấp, vây tay và màng cổ; các vây phải ôm thân khi di chuyển để giữ silhouette gọn.
- Da đen xanh ướt, mảng bụng xám chì; mang mở đóng rõ để telegraph và thể hiện nhịp thở bị ép.
- Hàm có răng không đều, vài răng gãy; mắt hổ phách là điểm đọc cảm xúc, không phải đèn trang trí.
- Đuôi tái mọc từ vết chém ngang: mô sẹo đỏ sẫm nối với đuôi lửa cam. Phần lửa là yêu khí bám trên mô sống, không phải đuôi rồng.
- `LG-01` nằm trong vùng ngực/họng được bảo vệ; không làm nó giống viên ngọc gắn trán hoặc ngực rồng.

### Human-fish form: visual contract

- **Combat role:** Phase 1; hình thái này đọc được ý chí, ký ức và khả năng bắt chước người canh giữ đền.
- **Posture:** thân trên hơi gập về trước, trọng tâm ở gốc đuôi; hai tay mở để đọc đòn quét, chụp và đập xuống.
- **Face:** giữ nét cá, không tạo mặt người đẹp hoặc mặt nạ nhân hình; biểu cảm đến từ mắt, mang, hàm và độ nghiêng đầu.
- **Costume elements:** mảnh dây buộc đỏ và vòng đồng oxy hóa mắc ở mang/vai như di vật bảo hộ; không mặc áo giáp hoặc trang phục giống người để tránh biến thành nhân vật người hoàn chỉnh.
- **Readable attacks:** móng/tay để cận chiến, đuôi để quét thấp, mang phun nước để đẩy lùi; đuôi lửa chưa bung toàn bộ ở phase này.
- **Transformation beat:** Long Ngọc nóng lên trong lồng ngực; thân cá bị kéo dựng thành hình lai, vảy rách theo đường sẹo, không có biến hình thành rồng.

### Boss phase variants

| Phase | Visual change | Narrative read |
| --- | --- | --- |
| `B01-P0` | Mắt và đuôi lửa lộ dưới mặt nước; thân bị cột đền che | Quy mô và sự quan sát trước khi chiến đấu; không tính là combat phase |
| `B01-P1-HYBRID` | Thân trên dựng thành người lai cá, hai tay có màng, đuôi lửa ngắn và bị khóa bởi sẹo | Ngư Tinh còn nhận biết, thử bắt chước người canh giữ |
| `B01-P2-ABYSSAL` | Hình lai vỡ ra; thân cá khổng lồ trồi lên, sẹo đuôi đỏ sáng, lửa kéo thành cung trên mặt nước | Vết thương và nỗi sợ nuốt mất phần người |
| `B01-RELEASED` | Lửa tắt trước; vảy trở lại xanh đen; nguyên thần tách sạch khỏi thân | Giải phóng, không phải chiến thắng tuyệt đối |
| `B01-ABSORBED` | Long Ngọc và lửa bị kéo vào người chơi; thân rơi xuống nước tối | Cưỡng đoạt tạo lợi ích nhưng làm ký ức nhiễu |

### Materials, palette, wear

| Token | Hex | Use |
| --- | --- | --- |
| `NGU_DEEP_BLUE` | `#0B1E2A` | Da và bóng thân |
| `NGU_SLATE_BELLY` | `#52616A` | Bụng, sẹo cũ |
| `NGU_AMBER_EYE` | `#D58A2D` | Mắt và điểm khóa mục tiêu |
| `NGU_SCAR_RED` | `#7A241E` | Sẹo đuôi, mô bị nhiễm |
| `NGU_YEU_FIRE` | `#F0642D` | Đuôi lửa, telegraph nguy hiểm |
| `NGU_JADE` | `#75B5A0` | Long Ngọc, vùng memory reveal |

Da phản sáng ướt nhưng không kim loại. Vết chém cũ phải đọc ở close range lẫn khi đuôi phát sáng. Yêu khí dùng lửa, bọt đen và nhiễu màu tiết chế; tránh khói mây cuộn hoặc râu rồng.

### Arena attachments and combat readability

- **Boss blend:** `assets/bosses/chapter_01_ngutinh/ngu_tinh_ch01.blend`.
- **Preview:** `assets/bosses/chapter_01_ngutinh/ngu_tinh_ch01_preview.png`.
- **Build script:** `tools/build_ngutinh_ch01.py`.
- **Rig:** `Ngu_Tinh_Combat_Rig`, 5 bones; rig là combat blockout, cần animation/art review trước production lock.
- **Required sockets/hooks:** `jaw_upper`, `jaw_lower`, `fin_dorsal`, `tail_scar`, `tail_fire`, `gill_l`, `gill_r`, `long_ngoc_core`.
- Đuôi lửa phải luôn cho người chơi đoán được sweep radius; lửa không được che toàn bộ vết sẹo trước đòn lớn.
- `LG-01` phải nhìn thấy trong các cửa sổ narrative đã ghi ở `05-boss-encounter.md`, nhưng không trở thành weak-point UI giả.

### Source and license record

- **Source strategy:** boss hiện là asset procedural/custom dựng trong repository; không gắn license bên thứ ba cho mesh hiện hành.
- **External asset policy:** nếu thay bằng source library, chỉ nhận asset có license thương mại hoặc CC0 tương thích; ghi URL, phiên bản, tác giả và phạm vi sửa trong manifest.
- **Cultural review:** cần review trước khi thêm motif bề mặt. Sinh học cá vực sâu được ưu tiên hơn ornament để giữ bản sắc CH-01.

## Acceptance checklist

- [ ] Long Nhân đọc được như nhân vật lấy cảm hứng Việt Nam qua cấu trúc và vật liệu, không phụ thuộc logo hay chữ.
- [ ] Không có mây cuộn, long văn, hanfu, giáp cung đình Trung Hoa hoặc motif Nhật trong asset final.
- [ ] Long Nhân có outfit theo lớp, vũ khí và accessory tách được để thay thế độc lập.
- [ ] Chân, bàn chân, grip và weapon socket không đảo hướng trong pose trung tính và combat pose.
- [ ] Ngư Tinh đọc là cá vực sâu; đuôi lửa và sẹo không biến nó thành rồng Trung Hoa.
- [ ] Intro `B01-P0` không bị tính nhầm thành combat phase.
- [ ] Hai combat phase của B-01 phân biệt rõ: người lai cá và cá vực sâu khổng lồ.
- [ ] Source, license, `.blend`, preview và build script được ghi và resolve.
- [ ] Cultural review hoàn tất trước khi content chuyển `approved` hoặc `locked`.

## Dependencies and handoff

| Owner | Dependency | Status |
| --- | --- | --- |
| Art | Final outfit modularization, material pass, cultural review | `draft` |
| Animation | Humanoid retarget, stance poses, boss jaw/gill/tail controls | `draft` |
| VFX | Thủy Ảnh, đuôi lửa, Long Ngọc reveal, yêu khí | `hook-only` |
| Gameplay | Socket names, phase readability, targetable regions | `hook-only` |
| Narrative | Phase lines, fate variants, release/absorb state | `approved-source` |
