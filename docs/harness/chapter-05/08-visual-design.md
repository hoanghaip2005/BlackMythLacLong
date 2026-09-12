# CH-05 Visual Design Harness

## Purpose

Nguồn chuẩn cho ngoại hình và cách đọc hình ảnh của các nhân vật/sinh vật quan trọng trong CH-05 (Ngã Ba Hạc). Khóa hướng art direction đủ để dựng, review và thay asset; **chưa** khóa topology, texture resolution, animation frame hay engine implementation.

## Shared art direction

### Visual thesis

CH-05 là một **ngã ba không chịu hòa**: nước phù sa đục, lũ lên, bè mảng trôi, và hai dòng luôn chực va nhau. Hình khối phải đọc được *hai lực kéo ngược* và *một nỗi đau chìm dưới đáy* (người mẹ). Mọi sinh vật phải đọc được trong silhouette trước khi thấy chi tiết; "giao" là **thuồng luồng/giao long bản địa** (rắn nước lớn), **không** phải rồng Trung Hoa.

### Vietnamese visual language

Được phép dùng các nguồn cảm hứng đã ghi nhận:

- Hoa văn hình học Đông Sơn: tia mặt trời, vòng tròn đồng tâm, răng cưa, đường ziczac, hình chim cách điệu (chim Lạc/Hạc — gợi "Ngã Ba Hạc") có tiết chế.
- Vật liệu sông nước: bè gỗ, dây chão, cọc nhà sàn, lưới, phù sa, vảy giao, ngọc sông.
- Áo giao lĩnh/tứ thân biến thể vận động cho người làng nổi; khố/váy ngắn tiện lội nước.
- Bảng màu: phù sa đục, nâu lụt, xanh nước sâu, đồng oxy hóa, đỏ son (dây buộc Lạc), và ánh ngọc lạnh.

Không được dùng:

- Mây cuộn, long văn, đế hiệu, giáp cung đình hoặc hoa văn nhận diện rõ từ mỹ thuật đế chế Trung Hoa.
- **Rồng bốn móng, đầu rồng cung đình, râu/bờm rồng Đông Á, phượng hoàng cung đình.** "Giao" phải là rắn nước/thuồng luồng bản địa: thân dài, vảy cá/sông, đầu thuồng luồng (không sừng đế vương), vây lưng thấp.
- Hanfu, cổ áo/tay áo mô phỏng Trung Hoa; kimono, samurai hay motif Nhật.
- Ornament phủ kín làm mất silhouette, đặc biệt ở khoảng cách camera gameplay.
- Biến Hợp Thể Hắc Giao Long thành "rồng hắc ám" kiểu Đông Á; nó là **hai thuồng luồng bị ép nhập**, còn đau, còn giãy.

### Shared technical rules

- Mọi phụ kiện gameplay phải có `attachment/socket` rõ ràng.
- Tay/chân (và vây/đuôi sinh vật) tuân theo trục giải phẫu trung tính; không mirror sai trục để chữa hướng.
- Vũ khí có trục lưỡi, điểm cầm, hướng sheath ghi trước khi rig.
- Asset nguồn chỉ là nền; provenance không phải canon văn hóa — mọi chi tiết lọc qua mục motif cấm.
- Preview dùng để review design intent, không thay thế kiểm tra `.blend` và rig.

## Character card: Long Nhân (CH-05 context)

### Identity

- **ID:** `PLAYER-LONG-NHAN`
- **Role:** Player character; người mang ký ức, từ chối làm trọng tài bằng bạo lực.
- **Canonical card:** ngoại hình gốc khóa ở `docs/harness/chapter-01/08-visual-design.md#character-card-long-nhan` (cùng asset `assets/characters/long_nhan/long_nhan_v3.blend`). CH-05 **không** đổi identity; chỉ thêm wear theo bối cảnh lũ.
- **Visual thesis CH-05:** một người lội giữa ngã ba nước đục, mang đủ năm mảnh ngọc như mang *nợ của năm vùng*, vạt áo nặng phù sa, sash đỏ là điểm nhận diện giữa màu lụt.

### CH-05-specific wear & read

- Gấu áo/quấn ướt, bám phù sa; dây buộc đỏ sẫm lại vì nước lũ (không đổi silhouette cơ bản).
- Năm mảnh `LG-01..LG-05` có thể đọc như năm điểm sáng nhỏ trên người/vật dẫn ký ức (không phải "năm viên ngọc gắn giáp"); `LG-05` chỉ nhập vào người sau `B05-B`.
- Ba điểm đọc trước trong gameplay: đầu/tóc buộc, sash đỏ, Rìu Thần Thạch Sơn.
- Ánh hổ phách mảnh ở mắt chỉ lóe khi Long Khí/ký ức phản ứng (giống card gốc).

### Palette (kế thừa card gốc)

| Token | Hex | Use |
| --- | --- | --- |
| `LN_INDIGO` | `#172A32` | Áo nền, bóng nước |
| `LN_EARTH` | `#6B4435` | Vải ngoài, da |
| `LN_LAC_RED` | `#A9352B` | Sash, dây buộc |
| `LN_RIVER_JADE` | `#628F87` | Ngọc, phản xạ ký ức |
| `LN_AMBER` | `#D88B35` | Mắt khi thức tỉnh, Long Khí |

Wear CH-05: thêm lớp phù sa đục (`#5A4B37`) ở gấu áo/ống quần; vải hút nước nặng hơn qua animation/VFX hook.

## Character card: B-05 Song Giao → Hắc Giao Long

### Identity

- **ID:** `B-05`
- **Role:** Chapter 5 boss; hai thuồng luồng (giao) anh em bị yêu khí bóp méo ký ức, cưỡng ép hợp thể.
- **Visual thesis:** hai dòng nước cùng một mẹ nhưng đánh nhau; khi bị ép nhập thành một khối đen giãy giụa, vừa mạnh vừa đau. Không bên nào "ác"; cả hai là nạn nhân của một ký ức bị tráo.
- **Player read:** Phase A = **hai** sinh vật thuồng luồng riêng biệt, mỗi con một sắc nước (đục/trong), đọc được như hai lực kéo ngược. Phase B = **một** Hắc Giao Long lớn hơn, thân còn hai đầu cố nhập, chuyển động mất đồng bộ.

### Silhouette and anatomy

- **Giao = thuồng luồng bản địa:** thân rắn nước dài, vảy cá/sông, bốn chân ngắn có màng (không phải chân rồng 4 móng đế vương), vây lưng thấp chạy dọc sống lưng, đuôi dẹt bơi. Đầu thuồng luồng: mõm dài, hàm rộng, mắt hai bên, **không sừng đế vương, không râu/bờm rồng Đông Á, không mây cuộn**.
- Phase A: hai con kích thước gần bằng nhau, đủ khác để người chơi phân biệt (xem palette) và đọc hướng tấn công của từng con.
- Phase B: khối hợp thể dài hơn, thân phình, **hai đầu còn cố nhập** (một đầu rõ, một đầu chìm nửa vào vai/cổ — đọc là "hai con trong một xác"); chuyển động lệch pha (đầu này vung thì đuôi kia trễ một nhịp) để thể hiện đây là hợp thể cưỡng ép, không thuần nhất.
- `LG-05` nằm ở vùng "ngực/họng" hợp thể, lóe khi hai đầu lệch pha (cửa sổ đọc ký ức), không phải weak-point UI.

### Boss phase variants

| Phase | Visual change | Narrative read |
| --- | --- | --- |
| `B05-P0` | Hai cột nước dựng ở hai nhánh ngã ba; hai cặp mắt dưới mặt nước; bè trôi bị kéo hai hướng | Quy mô và thế kẹt giữa, trước khi đánh; không tính combat phase |
| `B05-A-SONG-GIAO` | Hai thuồng luồng tách biệt: Giao Anh (vảy sẫm, vây rách — "người anh gánh em"), Giao Em (vảy sáng hơn, nhanh — "người em bị bỏ lại") | Hai ký ức đối nghịch; mỗi con tin mảnh ngọc/lòng sông là của mình |
| `B05-MERGE` (transformation beat) | Yêu khí/Hỗn Mang kéo hai thân va vào nhau, vảy chồng vảy, hai đầu cố nhập thành một; nước quanh đen đặc | Hợp thể **cưỡng ép**, đau đớn — không phải power-up tự nguyện |
| `B05-B-HAC-GIAO-LONG` | Một Hắc Giao Long lớn, thân đen phù sa, hai đầu còn giãy nhập, `LG-05` lóe trong họng | Khối xung đột bị dồn nén; mạnh hơn nhưng mất tự chủ |
| `B05-RELEASED` | Khối đen lắng; hai giao **tách lại** thành hai dòng êm; một bóng mẹ (Giao Mẫu) thoáng giữa chúng nếu `CH05_MOTHER_REMEMBERED` | Hòa giải: nhớ lại mẹ, hết tranh giành |
| `B05-ABSORBED` | `LG-05` + nguyên thần hợp thể bị kéo vào người chơi; hai thân giao rơi xuống nước tối, vệt đen chạy ngược lên tay Long Nhân | Cưỡng đoạt tạo lợi ích nhưng làm ký ức nhiễu |

### Materials, palette, wear

| Token | Hex | Use |
| --- | --- | --- |
| `GIAO_SILT_BLACK` | `#10231F` | Thân hợp thể, bóng nước đục |
| `GIAO_ELDER_SCALE` | `#2C4A44` | Vảy Giao Anh (sẫm) |
| `GIAO_YOUNG_SCALE` | `#4E7A6E` | Vảy Giao Em (sáng hơn) |
| `GIAO_FLOOD_BROWN` | `#5A4632` | Phù sa, lũ, mòn vảy |
| `GIAO_EYE_AMBER` | `#D58A2D` | Mắt, điểm khóa mục tiêu |
| `GIAO_YEU_INK` | `#0A0F14` | Yêu khí/Hỗn Mang (vệt đen nuôi xung đột) |
| `GIAO_JADE` | `#75B5A0` | `LG-05`, vùng memory reveal |

Vảy phản sáng ướt nhưng không kim loại; phù sa bám ở bụng/vây; yêu khí dùng vệt mực đen + bọt đục tiết chế, **không** khói mây cuộn hay long văn.

### Arena attachments and combat readability

- **Arena:** Ngã Ba Hạc — mặt nước lũ, **bè gỗ trôi** (nền đứng đổi vị trí), hai nhánh sông (hai hướng giao tiếp cận), một **nguồn nước đen** (thứ nuôi xung đột) ở đáy ngã ba.
- **Required sockets/hooks:** `head_giao_anh`, `head_giao_em`, `spine_fin`, `tail_paddle`, `merge_seam` (đường hai thân nhập), `long_ngoc_core`, `ink_source` (nguồn nuôi xung đột).
- Phase A phải luôn cho người chơi một bè/vùng an toàn đủ để đọc telegraph và một hướng nguy hiểm thể hiện *hai* lực kéo.
- Hai giao phải đọc được hướng tấn công riêng (đầu này vung = đuôi kia trễ) để counterplay "đứng giữa dẫn va chạm" khả thi.
- `LG-05` nhìn thấy trong các cửa sổ narrative đã ghi ở `05-boss-encounter.md`, không thành weak-point UI giả.
- **Asset:** procedural/custom dựng trong repository (`assets/bosses/chapter_05_songgiao/` — `TBD`); rig là combat blockout, cần art/animation review trước production lock.

### Source and license record

- **Source strategy:** boss hiện là asset procedural/custom dựng trong repository; không gắn license bên thứ ba cho mesh hiện hành.
- **External asset policy:** nếu thay bằng source library, chỉ nhận asset license thương mại hoặc CC0 tương thích; ghi URL, phiên bản, tác giả, phạm vi sửa trong asset manifest.
- **Cultural review:** bắt buộc trước khi thêm motif bề mặt; ưu tiên sinh học thuồng luồng/rắn nước bản địa + hoa văn Đông Sơn tiết chế hơn ornament; xác nhận "giao" không bị đọc nhầm thành rồng Trung Hoa.

## Character card: HB-05 Giao Mẫu (boss ẩn)

### Identity

- **ID:** `HB-05`
- **Role:** Hidden boss (ADR-004) — mẹ của hai Song Giao, nạn nhân thứ ba bị lãng quên.
- **Visual thesis:** một thuồng luồng mẹ đã bị xé nát, nay chỉ còn là bóng nước đục hình dáng mẹ, nửa thân chìm trong phù sa; bà **không** giận dữ — bà *mệt* và *buồn*, là nỗi đau bị quên mà Hỗn Mang lợi dụng.
- **Player read:** nhỏ hơn và tĩnh hơn hai con; silhouette mềm, gãy (vây rách, thân có vết xé cũ), đọc là "người mẹ" chứ không phải "quái vật". Không đe dọa bằng quy mô; đe dọa bằng *sự im lặng bị bỏ quên*.

### Silhouette and anatomy

- Thuồng luồng cái, thân dài nhưng **mỏng/mòn** hơn hai con; nhiều vết rách cũ dọc thân (dấu bị xé khi hai con tranh nhau).
- Đầu thuồng luồng hiền (mõm ngắn hơn, mắt lớn, không hàm đe dọa); vây lưng thấp, rách.
- Một phần thân chìm trong phù sa/đá miếu; di chuyển chậm, gần như neo tại chỗ (encounter thiên về *lắng nghe* hơn cơ động).
- Không sừng, không long văn, không mây cuộn. Có thể mang một dấu Đông Sơn mờ (vòng tròn đồng tâm) như "người từng được thờ".

### Hidden encounter variants

| Variant | Visual change | Narrative read |
| --- | --- | --- |
| `HB05-DORMANT` | Bóng mẹ chìm trong phù sa, gần như bất động, chỉ mắt hé | Một nỗi đau bị bỏ quên, không chủ động tấn công |
| `HB05-REMEMBERED` | Khi hai giao nhớ lại mẹ (release), bóng mẹ **sáng dịu**, thân lành lại thoáng chốc | Được công nhận → được an nghỉ |
| `HB05-RELEASED` | Bà tan thành dòng nước trong hòa vào ngã ba; hai giao tách êm | Hóa giải nạn nhân thứ ba |
| `HB05-ABSORBED` | Bóng mẹ bị kéo vào người chơi; ngã ba đục hơn, hai giao mất cơ hội nhớ mẹ | Cưỡng đoạt: lợi ích + cost narrative rõ |

### Materials, palette

| Token | Hex | Use |
| --- | --- | --- |
| `MAU_SILT` | `#3A3226` | Thân chìm trong phù sa |
| `MAU_PALE_SCALE` | `#6E8C80` | Vảy mòn, sáng dịu hơn hai con |
| `MAU_TEAR_JADE` | `#8FC3B4` | Nước mắt/ngọc sông, điểm ký ức |
| `MAU_YEU_INK` | `#0A0F14` | Vết Hỗn Mang bám quanh nỗi đau bị quên |

### Arena attachments (hidden)

- **Hidden arena:** `CH-05-HIDDEN` Miếu chìm ở ngã ba nước — một miếu nhỏ nửa chìm, tượng/bia người mẹ bị phù sa lấp, nước tĩnh khác hẳn lũ bên ngoài.
- **Required sockets/hooks:** `mother_body`, `torn_seam` (vết xé cũ), `shrine_silt`, `tear_jade`, `ink_trace`.
- **Asset:** procedural/custom (`assets/bosses/chapter_05_giaomau_hidden/` — `TBD`); cultural review bắt buộc (hình tượng "mẹ" cần tôn trọng, không gợi cảm/phản cảm).

### Source and license record

- **Source strategy:** asset procedural/custom; license `TBD`.
- **Cultural review:** hình tượng Giao Mẫu là "người mẹ bị lãng quên" — phải tôn trọng, không trang trí vô nghĩa; mọi biểu tượng cần chức năng nhân vật/chủ đề (01 §11).

## Acceptance checklist

- [ ] Long Nhân đọc được như nhân vật lấy cảm hứng Việt Nam qua cấu trúc/vật liệu, không phụ thuộc logo/chữ; wear CH-05 không đổi identity gốc.
- [ ] Hai giao (Phase A) phân biệt được bằng silhouette + palette; đọc là **thuồng luồng bản địa**, không phải rồng Trung Hoa.
- [ ] Hắc Giao Long (Phase B) đọc là **hai con bị ép nhập** (hai đầu, lệch pha), không phải "rồng hắc ám" Đông Á.
- [ ] Transformation beat đọc được là cưỡng ép/đau, không phải power-up tự nguyện.
- [ ] Giao Mẫu (HB-05) đọc là "người mẹ mệt mỏi/bị quên", nhỏ và tĩnh hơn hai con, không đe dọa bằng quy mô.
- [ ] Không có mây cuộn, long văn, hanfu, giáp cung đình Trung Hoa hay motif Nhật trong asset final.
- [ ] `B05-P0` không bị tính nhầm thành combat phase.
- [ ] Bè trôi/nguồn nước đen/`LG-05` reveal đọc được ở khoảng cách camera gameplay.
- [ ] Source, license, `.blend`, preview và build script được ghi và resolve (hoặc `TBD` rõ ràng).
- [ ] Cultural review hoàn tất trước khi content chuyển `approved` hoặc `locked`.

## Dependencies and handoff

| Owner | Dependency | Status |
| --- | --- | --- |
| Art | Final hai giao modular (đọc riêng ở Phase A), hợp thể Phase B, Giao Mẫu, material pass, cultural review | `draft` |
| Animation | Thuồng luồng rig (bơi/quật/đâm), beat hợp thể, lệch pha hai đầu, Giao Mẫu tĩnh | `draft` |
| VFX | Lũ/phù sa, vệt mực Hỗn Mang, `LG-05` reveal, Thủy Ảnh, nước rút lộ bậc tế đàn | `hook-only` |
| Gameplay | Bè trôi, arena hai boss + va chạm, nguồn nước đen, socket/tử huyệt đọc được | `hook-only` |
| Narrative | Phase lines hai giao + hợp thể, fate variants, hidden Giao Mẫu, release/absorb state | `approved-source` |
