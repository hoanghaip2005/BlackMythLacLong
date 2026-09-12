# CH-03: Huyết Mộc Đoạt Mệnh

## Trạng thái

- ID: `CH-03`
- Version: `0.1`
- Status: `draft`
- Vùng: Rừng Rậm Phong Châu - kinh đô cũ bị rừng nuốt, nghĩa địa dưới rễ, lõi đỏ của Mộc Tinh.
- Thời lượng narrative mục tiêu: 90-120 phút cho first playthrough, chưa tính khám phá tùy chọn và màn ẩn.
- Mảnh Long Ngọc: `LG-03`
- Boss: `B-03`, Mộc Tinh
- Boss ẩn (ADR-004): `HB-03`, Tướng Quân Vô Đầu
- Truth flag: `TRUTH_OLD_ARMY_WAS_BOUND`

## Chapter promise

Người chơi bước vào một kinh đô cũ đã bị rừng nuốt trọn, nơi người chết vẫn đứng gác. Cuối chương, người chơi hiểu ba điều:

1. Không phải vong linh nào cũng bị ép; nhiều người bám lấy lời thề vì sợ bị lịch sử quên.
2. Mộc Tinh không tạo ra đội quân; nó chỉ giữ lại đội quân đã tự nguyện ở lại.
3. Giải phóng người chết có thể là một ân huệ, cũng có thể là một sự phản bội - tùy ta hiểu lời thề của họ đến đâu.

## Dramatic question

**Khi một đội quân chết vẫn tự nguyện giữ lời thề, Long Nhân sẽ giải thoát họ hay để họ tiếp tục chiến đấu - và liệu Long Nhân có đang lặp lại chính sự trói buộc mà mình đến để phá?**

## Emotional arc

| Chặng | Trạng thái Long Nhân | Cảm xúc người chơi | Hình ảnh chủ đạo |
|---|---|---|---|
| Mở đầu | Mang theo dư âm Đầm Cáo, tiến vào rừng | Lạnh, bất an, bị theo dõi | Cổng đá bị rễ siết nứt |
| Khám phá | Nhận ra người chết vẫn "đứng gác" | Rùng mình, tò mò | Lính gác không mặt, giáp mọc rêu |
| Điều tra | Chạm vào lời thề của vong linh | Thương cảm, nghi ngờ | Nghĩa địa dưới rễ, bia không tên |
| Đối đầu | Bị Mộc Tinh gọi là "kẻ đến phá lời thề" | Giận dữ, phân vân | Lõi đỏ đập như tim giữa rừng |
| Hậu quả | Tự chọn số phận đội quân chết | Trách nhiệm, dự cảm | Rễ buông hoặc siết; tiếng binh khí im hoặc vang |

## Chapter non-goals

- Chưa giải thích Hỗn Mang đầy đủ; chỉ cho thấy nó "dùng lời thề để chứng minh người chết vẫn có thể bị cai trị".
- Chưa mở toàn bộ hệ stance; CH-03 nhấn `Thế Trảm` (càn quét đám xác-rễ) và tiếp tục `Thế Ngự`/`Thế Đột` theo tình huống.
- Chưa cho người chơi gặp Đại Bàng Tinh hoặc Song Giao.
- Không khẳng định phong ấn đã vỡ; mọi lời về "phong ấn" ở đây vẫn là lời truyền hoặc diễn giải sai.
- Không biến Mộc Tinh thành "ent fantasy phương Tây" hay một vị thần rừng hiền lành.

## Canon lock riêng cho CH-03

1. Long Nhân tới Phong Châu từ hướng CH-02, mang theo Rìu Thần Thạch Sơn (đã thức tỉnh từ CH-01) và `LG-01`, `LG-02`.
2. Mộc Tinh là một cây cổ thụ ăn máu, quân hóa người chết thành xác-rễ; nó không phải nạn nhân vô tội nhưng cũng không phải ác quỷ tuyệt đối.
3. Một phần vong linh Lạc Việt TỰ NGUYỆN ở lại vì sợ bị quên; phần khác muốn được giải thoát. Hai phe này có thật và đều có lý.
4. `LG-03` nằm trong lõi đỏ của Mộc Tinh; không lựa chọn nào cho phép bỏ qua `LG-03`, chỉ đổi cách thu hồi và trạng thái mảnh ngọc.
5. Tướng Quân Vô Đầu (`HB-03`) là chỉ huy cũ, TỰ trói mình vào lời thề sau khi chết; ông không bị Mộc Tinh ép. Đây là nội dung ẩn, không bắt buộc.
6. Rìu Thần Thạch Sơn không được mô tả là đã tồn tại trước CH-01; ở CH-03 nó là vũ khí đã đồng hành, không phải vật mới thức tỉnh.
7. Chapter kết thúc khi tiếng binh khí trong rừng im hẳn (hoặc vang lên theo nhánh giữ lời thề), không phải khi Long Nhân rời rừng.

## Chapter end states

### `CH03_END_RELEASED`

Long Nhân giải thoát lõi đỏ và phần lớn vong linh. Mộc Tinh suy kiệt; rễ buông người chết. `boss_fates[B-03] = released`. Một số vong linh chọn ở lại tự nguyện (không bị trói) để canh ký ức; đây là khác biệt then chốt với "giữ họ chiến đấu". Phong Châu im tiếng binh khí; rừng bắt đầu là rừng, không còn là doanh trại.

### `CH03_END_FORCE`

Mộc Tinh bị hạ bằng sức mạnh nhưng bond chưa giải quyết. `boss_fates[B-03] = defeated_by_force`. Long Nhân lấy `LG-03` từ lõi đỏ nứt. Vong linh không biến mất; họ đứng im, không còn bị điều khiển nhưng cũng chưa được gọi tên. Rừng còn đầy giáp rêu - hậu cảnh lạnh.

### `CH03_END_ABSORBED`

Long Nhân cưỡng đoạt nguyên thần Mộc Tinh. `boss_fates[B-03] = absorbed`, `dragon_hunger +1`. Rễ đen chạy ngược lên tay Long Nhân; Long Khí bùng mạnh nhưng nhiễu. Gieo mầm E-02, không khóa ending.

### `CH03_END_SACRIFICED`

Nhánh đặc biệt: một vong linh (hoặc Tướng Quân Vô Đầu, nếu đã mở màn ẩn) TỰ hy sinh để phá vòng lặp lời thề, mở lõi đỏ cho Long Nhân mà không cần cưỡng đoạt. `boss_fates[B-03] = released`, đồng thời `boss_fates[HB-03] = sacrificed` (nếu là Tướng Quân). Đây là kết quả của việc tôn trọng lời thề đủ sâu, không phải phần thưởng mặc định.

## Handoff summary

CH-03 cần ba lớp bàn giao:

- **Narrative:** scene flow, dialogue, choice effects, boss fate, hidden boss fate, hai phe vong linh.
- **Gameplay hook:** đấu trường rễ chuyển động, phá rễ mở đường/lộ lõi, `Thế Trảm` dọn đám xác-rễ, đọc telegraph rễ siết, tùy chọn hook Nguyên thần Chân Tinh (TBD).
- **Art/audio hook:** kinh đô bị rừng nuốt, giáp mọc rêu, nghĩa địa dưới rễ, lõi đỏ đập như tim, tiếng binh khí vọng, sương thấp.

Thông số damage, map coordinates, animation frame, model topology và VFX implementation để `TBD` ở phase sau.
