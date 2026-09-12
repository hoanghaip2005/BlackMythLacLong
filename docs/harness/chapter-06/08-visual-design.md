# CH-06 Visual Design Harness

## Purpose

Nguồn chuẩn cho ngoại hình và cách đọc hình ảnh của Đỉnh Nghĩa Lĩnh, `B-06 Hỗn Mang`, lớp chứng-nhân full-completion và bốn ending card. Khóa art direction ở mức đủ dựng/review/thay asset; **chưa** khóa topology, texture resolution, animation frame, shader node hay engine implementation (R-05).

## Shared art direction

### Visual thesis

CH-06 là **tế đàn của ký ức bị gom lại**. Hình khối phải trang nghiêm, trống trải, "không có bóng" — một nơi mà lịch sử bị nén thành một kẻ thù duy nhất. Hỗn Mang không phải quái vật ngoại lai: nó là **bóng của chính Long Nhân và của đám đông oan khuất**. Mọi thứ phải đọc được trong silhouette trước khi thấy chi tiết.

### Vietnamese visual language

Được phép dùng (cảm hứng, đã ghi nhận):

- Hoa văn hình học Đông Sơn: tia mặt trời, vòng tròn đồng tâm, răng cưa, ziczac, hình chim Lạc cách điệu **tiết chế**.
- Tế đàn đá bậc thang kiểu Nghĩa Lĩnh/Đền Hùng cảm hứng; cột đá, trống đồng, dây dệt đỏ, đồng oxy hóa.
- Bảng màu: đá xám lạnh, đồng oxy hóa, đỏ son (`LN_LAC_RED`), ngọc sông đục, và "lửa xanh" của yêu khí khi bị nén.
- Năm Long Ngọc (`LG-01..05`) phát sáng theo **ngũ hành ký ức** của năm vùng (nước, sương/bóng, rễ/máu, lông vũ/sương đá, lũ/hợp thể) — nhưng là ký ức, không phải ngọc loot.

Không được dùng (motif cấm):

- Mây cuộn, long văn, đế hiệu, giáp cung đình hoặc hoa văn nhận diện rõ từ mỹ thuật đế chế Trung Hoa.
- Hanfu, cổ áo/tay áo mô phỏng Trung Hoa; kimono, samurai hay motif Nhật.
- Rồng bốn móng, đầu rồng cung đình, phượng hoàng cung đình không có lý do canon.
- **Quỷ vương sáo rỗng** (sừng, cánh dơi, ngai xương, lửa địa ngục) cho Hỗn Mang — nó phải là *bản sao méo của Long Nhân*, không phải demon-lord.
- Ornament phủ kín làm mất silhouette ở khoảng cách camera gameplay.

### Shared technical rules

- Phụ kiện gameplay có `attachment/socket` rõ ràng.
- Tay/chân theo anatomical pose trung tính; không mirror mesh sai trục.
- Vũ khí (Rìu Thần Thạch Sơn) có trục lưỡi, điểm cầm, hướng sheath ghi trước khi rig.
- Asset nguồn chỉ là nền; provenance không phải canon văn hóa; mọi chi tiết lọc qua motif cấm.
- Preview dùng để review design intent, không thay kiểm tra `.blend` + rig.

## Environment card: Đỉnh Nghĩa Lĩnh (tế đàn)

- **ID:** `ENV-CH06-NGHIA-LINH`
- **Visual thesis:** bậc đá không có bóng; năm bệ ngọc quanh một đàn trống; bầu trời nửa sáng nửa tối (ranh giới thực/mộng).
- **Readable beats:** năm bệ `LG-01..05` phát sáng tuần tự ở `CH-06-S02`; đàn trống ở giữa là nơi Hỗn Mang trồi lên; không gian mở cho đấu tay đôi (không chướng ngại che silhouette).
- **Palette token:** `NL_STONE #6A6E73`, `NL_DUSK #2C3A44`, `NL_BRONZE #6E7764`, `NL_LAC_RED #A9352B`, `NL_YEU_BLUE #3FA9A0` (lửa xanh yêu khí nén).
- **Forbidden:** không biến tế đàn thành "thiên đình"/Olympus; giữ chất Lạc Việt/Đông Sơn (glossary `01 §10`: Nghĩa Lĩnh ≠ thiên đình).
- **Dependency:** art `ART-ENV-NGHIA-LINH` (TBD), audio `AUD-CH06-ALTAR` (TBD).

## Character card: B-06 Hỗn Mang

### Identity

- **ID:** `B-06`
- **Role:** phản diện cuối; oán nghiệp tập thể mang hình **bản sao Long Nhân**.
- **Visual thesis:** "chiếc bóng biết nói" — cùng vóc dáng Long Nhân nhưng **bị méo bởi ký ức chồng lấn**: nhiều lớp mặt/tay/vảy chồng mờ, vừa là Long Nhân vừa là đám đông oan khuất. Không sừng, không cánh, không ngai.
- **Player read:** người chơi phải nhận ra "đây là mình, nhưng là phiên bản đã từ bỏ lựa chọn" — rùng mình vì quen, không vì lạ.

### Silhouette and anatomy

- Vóc gần Long Nhân (humanoid, trọng tâm thấp, vũ khí lớn hơn vẻ ngoài) để đọc là **bản sao**, không phải quái mới.
- Méo có chủ đích: đường viền **nhân đôi/lệch pha** (như ảnh chồng mờ); vai/hông lệch nhẹ; một nửa mặt giữ nét Long Nhân, nửa kia là những khuôn mặt khác chồng lên.
- Vảy rồng ẩn (ấn rồng) xuất hiện **quá mức** — bò lan như vết nứt, thể hiện "huyết thống bị tôn thành quyền cai trị".
- Rìu của Hỗn Mang là **bản sao lệch** của Rìu Thần Thạch Sơn: cùng hình, nhưng vòng tia mặt trời Đông Sơn bị **đảo ngược/méo** (đọc là "ký ức bị bẻ").
- Không có bóng đổ dưới chân (khớp beat `CH-06-S01` "bậc đá không có bóng").

### Phase variants

| Phase | Visual change | Narrative read |
| --- | --- | --- |
| `B06-P0` | Trồi lên từ đàn trống, mang đúng hình Long Nhân, im lặng | "Kẻ đến sau ta" — quy mô tâm lý, không phải thể xác |
| `B06-P1-MIRROR` | Bản sao ổn định; sao chép stance/đòn **đã thấy**; méo nhẹ theo nhịp | Nó là tấm gương kỹ thuật |
| `B06-P2-CHOIR` | Nhiều lớp mặt/tay/vảy chồng rõ; hiện **dư ảnh** năm boss theo `boss_fates` quá khứ (tha → ánh ngọc ấm; absorb → vệt đen) | Nó là đám đông oan khuất đọc lại lựa chọn của bạn |
| `B06-EXPOSED` (sau `C-CH06-002`) | Lớp chồng **nứt ra**, lộ lõi trống rỗng không bản ngã; im tiếng | Điểm yếu: không sao chép được lựa chọn chưa thực hiện |
| `B06-DISSOLVE` | Không "chết"; tan thành ký ức trả về, nhường chỗ cho `final_decision` | Kết cục là lựa chọn, không phải xác boss |

### Materials, palette, wear

| Token | Hex | Use |
| --- | --- | --- |
| `HM_VOID` | `#15181C` | thân bóng, khoảng trống bản ngã |
| `HM_COPY_SKIN` | `#6B4435` (mượn `LN_EARTH`) | phần giống Long Nhân |
| `HM_LAC_RED_DISTORT` | `#7E2A22` | sash/dây buộc bản méo |
| `HM_YEU_BLUE` | `#3FA9A0` | lửa xanh yêu khí nén, viền ký ức |
| `HM_JADE_STOLEN` | `#75B5A0` | ánh ngọc khi tái hiện boss đã tha |
| `HM_CHAR` | `#2A211E` | vệt đen khi tái hiện boss đã absorb |

Vật liệu: bóng bán trong, mép nhiễu nhẹ; **không** kim loại quỷ; không khói mây cuộn. Yêu khí dùng lửa xanh + nhiễu chồng lớp tiết chế.

### Arena attachments and combat readability

- **Boss blend:** `assets/bosses/chapter_06_honmang/hon_mang_ch06.blend` (TBD).
- **Preview:** `assets/bosses/chapter_06_honmang/hon_mang_ch06_preview.png` (TBD).
- **Build script:** `tools/build_honmang_ch06.py` (TBD).
- **Rig:** dùng lại skeleton humanoid của Long Nhân (vì là bản sao) + socket chồng lớp `overlay_face_*`, `overlay_arm_*`; rig là combat blockout, cần art/animation review trước production lock.
- **Required sockets/hooks:** `hand_r_weapon`, `overlay_face_l`, `overlay_face_r`, `overlay_arm_l`, `overlay_arm_r`, `core_void`, `long_ngoc_echo`.
- Bản sao phải **đọc được** là "cùng moveset với người chơi" để cơ chế mirror công bằng; đòn sao chép có telegraph giống hệt đòn người chơi.
- Dư ảnh năm boss phải phân biệt được "tha" (ấm) vs "absorb" (đen) bằng màu, không chỉ bằng lời.

### Source and license record

- **Source strategy:** boss procedural/custom dựng trong repo (như Ngư Tinh); không gắn license bên thứ ba cho mesh hiện hành.
- **External asset policy:** nếu thay bằng source library, chỉ nhận asset license thương mại/CC0 tương thích; ghi URL, phiên bản, tác giả, phạm vi sửa trong asset manifest.
- **Cultural review:** **bắt buộc** trước khi `approved`/`locked` — đặc biệt vì Hỗn Mang mượn hình Long Nhân và motif Đông Sơn; phải đảm bảo không thành quỷ vương ngoại lai, không lai Trung/Nhật.

## Full-completion witness layer (visual)

- **ID:** `VIS-CH06-FULL-WITNESS`
- Khi `hidden_released=5`, ở `CH-06-FULL`/`CH-06-S05` năm **Oan Khuất Ẩn** (HB-01..05) hiện về làm chứng: mỗi oan khuất một hình ảnh chủ đạo gắn vùng của nó — `HB-01` Ma Da (bọt biển/vong đáy), `HB-02` Bóng Vô Danh (mặt nạ/bóng lấy lại tên), `HB-03` Tướng Quân Vô Đầu (rễ/lời thề), `HB-04` Tù Trưởng Lệ Đá (sương đá/lệ), `HB-05` Giao Mẫu (lũ/hợp thể dịu lại).
- Đọc hình ảnh: họ **không chiến đấu**; đứng thành vòng chứng-nhân quanh đàn, ánh ngọc ấm; đối lập với dư ảnh đen của boss đã absorb.
- Đây là phần thưởng thị giác của "làm full" (ADR-004) và là tín hiệu `E-04` trọn vẹn.

## Ending cards (visual contract)

Mỗi ending một hình ảnh chủ đạo + một dòng text; không cutscene dài.

| Ending | Hình ảnh chủ đạo | Tông màu | Ghi chú |
| --- | --- | --- | --- |
| `E-01 LONG_VUONG` | Long Nhân đứng canh Long Mạch trên tế đàn, ngọc sáng **ổn định hoặc chập chờn** tùy `relics_purified` | vàng đồng ấm, nhưng một vệt tối nhỏ ở chân trời nếu `<3` (hook phần tiếp) | chiến thắng truyền thống, còn câu hỏi quyền bảo hộ |
| `E-02 TAN_HON_MANG` | Long Nhân hóa rồng **tối**, ngồi vào chỗ Hỗn Mang vừa ngồi; trật tự mới đẹp mà lạnh | đỏ son + đen, ánh sáng gắt | đẹp hình thức, nguy hiểm bản chất |
| `E-03 DOAN_TUYET_LONG_MACH` | Năm ngọc **vỡ**; phép màu rút khỏi thế giới; con người tự bước đi | xám tro + ánh ngày thường | giải phóng, không bảo đảm hòa bình |
| `E-04 HOA_GIAI_BACH_TOC` | Ký ức **trả về** trăm họ; tế đàn thành nơi hòa giải; năm oan khuất + cộng đồng hiện diện; Long Nhân là con người giữa đồng bào | ngọc sông ấm + đỏ son + lửa xanh dịu | kết thúc thật (cần full); thiêng, ấm |
| `E-04-PARTIAL` | Như E-04 nhưng **thiếu** năm chứng-nhân; vài bóng oan khuất còn lơ lửng chưa siêu thoát | ấm nhưng còn mảng tối | hòa giải một phần |
| `E-03-BITTER` | Ngọc vỡ nhưng cộng đồng **quay lưng**, chưa thấy sự thật | xám lạnh hơn E-03 | bi kịch của reconcile thiếu lõi |

- **Forbidden cho ending card:** không minh họa Lạc Long Quân như một vị thần hiện thân ban phát kết cục (Canon Lock 9) — tối đa là ánh sáng/tiếng vọng biểu tượng.

## Acceptance checklist

- [ ] Long Nhân và Hỗn Mang đọc được như "người và bóng của người" qua cấu trúc/vật liệu, không phụ thuộc logo/chữ.
- [ ] Hỗn Mang **không** thành quỷ vương sáo rỗng; không sừng/cánh/ngai xương/lửa địa ngục.
- [ ] Không mây cuộn, long văn, hanfu, giáp cung đình Trung Hoa hay motif Nhật trong asset final.
- [ ] Đuôi lửa/vảy/yêu khí không biến Hỗn Mang thành rồng Trung Hoa.
- [ ] `B06-P0` không bị tính nhầm thành combat phase.
- [ ] Hai combat phase phân biệt rõ: MIRROR (bản sao kỹ thuật) vs CHOIR (đám đông đọc lựa chọn).
- [ ] Dư ảnh năm boss phân biệt "tha" (ấm) vs "absorb" (đen) bằng màu.
- [ ] Lớp chứng-nhân full-completion chỉ hiện khi `hidden_released=5`.
- [ ] Bốn ending card có hình ảnh + tông riêng; E-04 khác E-04-PARTIAL ở chỗ có/không năm chứng-nhân.
- [ ] Nghĩa Lĩnh không bị vẽ thành thiên đình/Olympus.
- [ ] Source, license, `.blend`, preview, build script được ghi và resolve (hoặc TBD có chủ đích).
- [ ] Cultural review hoàn tất trước khi content chuyển `approved`/`locked`.

## Dependencies and handoff

| Owner | Dependency | Status |
| --- | --- | --- |
| Art | Tế đàn Nghĩa Lĩnh, bản sao Long Nhân (B-06), 4 ending card, lớp chứng-nhân | `draft` |
| Animation | Reuse rig Long Nhân cho bản sao; phase MIRROR/CHOIR; overlay chồng lớp | `draft` |
| VFX | Lửa xanh yêu khí nén, dư ảnh boss theo `boss_fates`, ngọc vỡ (E-03), ký ức trả về (E-04) | `hook-only` |
| Gameplay | Mirror moveset đọc được; `C-CH06-002` un-copy trigger; resolve `final_decision`→ending | `hook-only` |
| Cinematic | Ending card + hậu cảnh thế giới cho 4 ending + 2 tag | `draft` |
| Audio | Giọng Hỗn Mang = giọng Long Nhân + chồng lấn nhiều giọng; tiếng tế đàn; stinger từng ending | `hook-only` |
| Narrative | Phase lines, boss-lines-by-state, thoại 4 quyết định, ending line | `approved-source` |
