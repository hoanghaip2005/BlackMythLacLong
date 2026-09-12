# CH-05 Boss Encounter: Song Giao → Hắc Giao Long

## Encounter identity

- ID: `B-05`
- Name: Song Giao (Giao Anh + Giao Em) → hợp thể Hắc Giao Long
- Arena: ngã ba sông mùa lũ; bè gỗ trôi, xoáy nước, hai luồng phù sa đen quy về một điểm neo ký ức.
- Player objective: sống sót giữa HAI boss, nhận ra cả hai bị bóp méo ký ức, rồi tự chọn cách nhận nguyên thần hợp thể.
- Emotional promise: người chơi phải thắng một cuộc tranh chấp mà *không bên nào là kẻ xâm lược*, và hiểu rằng chọn phe là kéo dài vòng lặp.

## Arena storytelling

Arena chia thành ba lớp đọc:

1. **Lớp sinh tồn:** bè trôi đổi vị trí, xoáy hút, hai luồng tấn công chéo nhau; vùng an toàn là khoảng nước *giữa* hai giao.
2. **Lớp ký ức:** các neo ký ức (mảnh miếu, bàn tay chia nước, hai giao con) phát sáng khi người chơi nhìn đúng hướng.
3. **Lớp phán xét:** phù sa đen quy về điểm neo — thứ *nuôi* xung đột, không nằm trong hai con giao.

Không cần map/coordinate cố định ở giai đoạn này. Arena phải luôn giữ một vùng an toàn đủ để đọc telegraph và một vùng nguy hiểm thể hiện hướng hai luồng nước.

## Boss desire in combat

Mỗi giao không cố giết Long Nhân ngay; chúng cố *biến Long Nhân thành trọng tài* — kẻ xác nhận ngọc thuộc về bên nào.

- **Giao Anh:** muốn được công nhận là kẻ giữ nguồn, là bên "đã ở đó trước".
- **Giao Em:** muốn được công nhận là bên "bị lấy mất phần", là kẻ đòi lại công bằng.
- **Hợp thể (Hắc Giao Long):** muốn *một* ý chí để không còn phải tranh — nhưng đó là ý chí bị ép, không phải hòa giải.

Khi người chơi chỉ đánh và chọn phe, boss càng tin rằng trọng tài là thứ duy nhất chấm dứt được tranh chấp. Khi người chơi kích neo ký ức và từ chối vai trọng tài, giả thuyết "cả hai là nạn nhân" mở ra. `B05-P0` chỉ là intro không chiến đấu, không tính vào tổng số phase.

## Intro: Hai cột nước (`B05-P0`)

### Narrative trigger

Long Nhân ra giữa ngã ba sau `CH-05-S04`. Hai cột nước dựng lên ở hai nhánh; `LG-05` nổi ở giữa. Hai giao lộ diện từng phần, chưa hợp thể.

### Experience hook

Người chơi nhận biết *quy mô hai boss cùng lúc* và hiểu ngay luật arena: đứng giữa là sống, đứng về một bên là bị bên kia coi là địch.

### Player counterplay

Không đánh được trong intro. Người chơi quan sát hai neo ký ức, điểm phù sa đen, và đường bè trôi; mục tiêu là đọc arena trước khi phase A bắt đầu.

## Combat Phase A: Song Giao (`B05-A-DUEL`)

### Narrative trigger

Hai giao lao vào nhau *và* vào Long Nhân. Chúng tranh `LG-05` ở giữa; người chơi bị kẹt trong cuộc tranh đó.

### Visual read

- Hai con giao long bản địa (thuồng luồng): thân rắn nước lớn, dài, vảy phù sa, vây lưng thấp, đầu thuồng luồng (không sừng rồng Trung Hoa, không râu bờm, không bốn móng).
- Giao Anh: vảy sẫm thượng nguồn, sẹo cũ ở mạn sườn (dấu "giữ nguồn").
- Giao Em: vảy nhạt hơn, thân thon, đuôi chẻ (dấu "ra cửa biển").
- Mỗi con di chuyển theo một luồng nước riêng; hai luồng cắt nhau ở giữa.

### Combat hook

- Hai giao đánh nhau *và* quét người chơi; đòn của con này có thể trúng con kia.
- Người chơi có thể **dẫn đòn** (kiting) để hai giao va vào nhau, tạo khoảng hở — nhưng lạm dụng là `dragon_hunger` nếu cố đẩy chúng vào chỗ chết.
- Bè trôi là nền đứng tạm; xoáy hút kéo người chơi về điểm phù sa đen.
- `Thủy Ảnh` là đường an toàn khi hai luồng nước chồng nhau.

### Telegraph

- Giao nào sắp quật: luồng nước của nó rút khỏi vùng trước mặt, vảy mạn sườn sáng.
- Trước đòn phối hợp (cả hai cùng lao): mặt nước lõm thành hai rãnh đối xứng.
- Trước xoáy hút: phù sa đen xoáy ngược về điểm neo.
- Khi một giao bị con kia trúng đòn: nó khựng một nhịp, lộ mạn sườn.

### Player counterplay

- `Thế Ngự` để phản đòn quét đuôi và *nghe* một giao nói hết câu (mở ký ức).
- `Thế Đột` xuyên vảy ở khoảnh khắc lộ mạn sườn.
- Kích neo ký ức trong khoảng boss khựng: neo phát sáng, cho thấy hai giao con bơi song song.
- `Thủy Ảnh` khi hai luồng chồng; đứng trong vùng neo đã kích là lựa chọn thay thế.
- Không yêu cầu parry hoàn hảo; né đúng hướng giữa hai luồng là counterplay hợp lệ.

### Narrative interaction

Kích hoạt neo thứ nhất cho thấy *hai giao từng là anh em*. Nếu người chơi đã nghe cả hai ký ức (`CH05_MEMORY_MISMATCH`), neo thứ hai cho thấy *cùng một bàn tay chia nước* — bàn tay của Giao Mẫu. Nếu đã giải thoát `HB-05`, người chơi có thể thả "ký ức người mẹ" vào nước ngay trong phase A, làm hai giao khựng lại lâu hơn.

## Transformation beat: Hợp thể cưỡng ép (`B05-A-TO-B`)

### Narrative trigger

Khi `LG-05` bị hai luồng kéo căng, hoặc khi người chơi kích hai giao đánh nhau quá đà, phù sa đen *cuộn hai thân lại*. Đây không phải biến hình tự nguyện — nó là cưỡng ép, đau đớn.

### Visual read

- Hai thân giao xoắn vào nhau, vảy chồng vảy, hai đầu chập thành một cổ họng.
- Phù sa đen bọc ngoài như một lớp da thứ hai không thuộc về con nào.
- `LG-05` bị hút vào giữa khối hợp thể, lóe lên ở "ngực".

### Experience hook

Người chơi phải *thấy* đây là cưỡng ép: hai tiếng nói trong hợp thể cãi nhau, một bên muốn tách ra. Không ăn mừng "boss mạnh hơn".

## Combat Phase B: Hắc Giao Long (`B05-B-MERGED`)

### Narrative trigger

Hợp thể hoàn tất. Một boss lớn hơn, nhanh hơn, nhưng *đau*: nó tấn công vì hai ý chí trong một thân không thống nhất được.

### Visual read

- Giao long đen khổng lồ, thân dày gấp đôi, hai đầu chập một nhưng còn dấu hai cổ.
- Phù sa đen chảy ngược trên vảy như mạch máu; `LG-05` lóe trong lồng ngực.
- Mắt: một bên hổ phách (Giao Anh), một bên trắng xanh (Giao Em) — lệch nhịp.

### Combat hook

- Quét rộng hơn phase A; bè trôi bị nghiền, arena thu hẹp.
- Lặn xuống và nổi lên từ hai hướng *cùng lúc* (dấu hai ý chí).
- Gọi xoáy lớn kéo người chơi về điểm phù sa đen rồi nối sóng ngang.
- Đòn "hai tiếng cãi nhau": hợp thể tự khựng khi hai ý chí xung đột — cửa sổ phản đòn.

### Telegraph

- Trước đòn quét: phù sa đen dồn về một phía thân.
- Trước khi lặn: hai mắt đổi hướng ngược nhau.
- Trước xoáy lớn: điểm neo phù sa sáng lên, nước rút khỏi rốn xoáy.
- Khi hợp thể tự khựng (hai ý chí cãi): một đầu cúi, một đầu ngẩng — báo hiệu cửa sổ bond.

### Player counterplay

- Đánh vào điểm phù sa đen (nguồn nuôi hợp thể) sau đòn quét để *làm yếu lớp da thứ hai* — không phải weak-point UI, mà là phá thứ cưỡng ép chúng.
- `Thế Ngự` phản đòn để "nghe" hợp thể nói hết một câu (mở ký ức mẹ).
- `Lôi Kích` ngắt một lần lặn, tạo cơ hội đọc ký ức.
- Kích neo thứ ba (nếu chưa) trong cửa sổ hợp thể tự khựng.
- `Thủy Ảnh` khi xoáy lớn chồng sóng ngang.
- Có đường thắng thuần sức mạnh (hạ hợp thể) và đường `released` (kích đủ neo + ký ức mẹ).

### Narrative interaction

Kích neo thứ ba phát lại khoảnh khắc *Giao Mẫu chia nước cho hai con*. Nếu `CH05_MOTHER_REMEMBERED` (đã giải thoát `HB-05`), người chơi có thể thả ký ức mẹ vào nước: hợp thể *im cùng một nhịp* lần đầu, hai đầu cúi xuống — cửa sổ `released`. Nếu không, hợp thể chỉ yếu đi tạm thời rồi tiếp tục; người chơi vẫn có thể thắng bằng sức mạnh.

## Defeat state

Khi Hắc Giao Long bị đánh bại, thân nó không nổ tung. Phù sa đen bong ra trước, hai thân giao tách dần, rồi nguyên thần hợp thể lộ ra. Người chơi có quyền di chuyển trong arena và đưa ra `C-CH05-003`.

## Fate resolution

### `released`

Điều kiện bond hoàn tất (và lý tưởng `HB-05 released`). Hợp thể *tự tách* thành hai giao; chúng nhận ra nhau là anh em và nhận ra mẹ. Nguyên thần dừng trước tay người chơi.

Hậu quả:

- `boss_fates[B-05] = released`.
- `memory_recovered +1`.
- `mercy_marks +1`.
- `relics_purified +1`.
- `tribal_trust` không tự tăng; làng nổi chỉ tin hơn nếu người chơi đã không đẩy hai giao vào chỗ chết.

### `defeated_by_force`

Hợp thể bị hạ nhưng bond chưa hoàn tất hoặc người chơi không chạm nguyên thần.

Hậu quả:

- `boss_fates[B-05] = defeated_by_force`.
- `LG-05` hoạt động không ổn định.
- `memory_recovered` không tăng.
- Một đoạn ký ức mất tiếng ở CH-06; hai giao tan thành hai dòng đục, không nhận ra nhau.

### `absorbed`

Người chơi nắm nguyên thần hợp thể bằng sức mạnh.

Hậu quả:

- `boss_fates[B-05] = absorbed`.
- `dragon_hunger +1`.
- Long Khí bùng mạnh lần đầu nhưng hình ảnh nhiễu (hai tiếng cãi nhau trong đầu Long Nhân).
- Không tăng `relics_purified`.

## Boss lines by player state

| State | Line direction |
|---|---|
| Chưa đọc neo nào | "Trọng tài! Nói xem ngọc thuộc về ai!" |
| Đã đọc một neo | "Đừng im lặng. Im lặng là đứng về phía kẻ mạnh." |
| Đã đọc hai neo | "Ngươi thấy rồi… chúng ta từng chung một nguồn." |
| Đã đọc ba neo | "Nếu mang ngọc đi, hãy mang cả người đã chia nó." |
| `CH05_BOSS_NAMED_WOUND` | Hợp thể khựng một nhịp trước khi phản kích |
| `CH05_BOSS_PITTED` | Hai giao ưu tiên đánh nhau hơn đánh người chơi |
| `CH05_MOTHER_REMEMBERED` | Hai đầu hợp thể cúi cùng nhịp; mở cửa sổ `released` |

## Oan Khuất Ẩn: HB-05 Giao Mẫu (`CH-05-HIDDEN`)

Encounter ẩn đầy đủ ở `01-scene-flow.md#ch-05-hidden`. Tóm tắt combat-to-story:

- `HB-05` là boss ẩn **một phase**, không hợp thể, không cưỡng ép — đối lập với `B-05`.
- Arena: lòng miếu chìm, nước đứng, phù sa lắng; không có bè trôi, không có xoáy.
- Boss desire: Giao Mẫu không giữ ngọc, không đòi công bằng — bà chỉ *chờ được nhớ*. Bà tưởng Long Nhân là con trở về.
- Bond: nói thật rằng bà đã bị quên, và rằng hai con đang giết nhau vì quên bà. Không phải "đánh thắng" bà.
- Fate: `released` → `hidden_released +1`, `mercy_marks +1`, mở `CH05_MOTHER_REMEMBERED` (dùng trong `B05-B`). `absorbed`/`defeated_by_force` → `dragon_hunger +1`, không tăng `hidden_released`, mất chìa khóa hòa giải thật của chương.
- R-05: không số liệu; chỉ hook "một encounter tĩnh, gần như không cần đánh, nơi chiến thắng là *nói thật*".

## Combat-to-story acceptance

- Người chơi đọc được ít nhất ba pattern bằng hình ảnh/âm thanh (hai luồng, phù sa đen, neo ký ức), không cần tutorial text dài.
- Intro `B05-P0` không chiến đấu, tách biệt với phase A và phase B.
- Phase A (hai boss) và phase B (hợp thể) có counterplay, telegraph và ngôn ngữ silhouette khác nhau.
- Transformation beat đọc được là *cưỡng ép*, không phải "level up".
- Có đường thắng không yêu cầu release (hạ hợp thể bằng sức mạnh).
- Có đường release không yêu cầu perfect combat (kích neo + ký ức mẹ).
- Cưỡng đoạt tạo lợi ích cảm nhận ngay, đồng thời gieo cost narrative rõ (hai tiếng cãi trong đầu).
- Boss không bị gọi là đã "chết" trước khi fate được ghi.
- Màn ẩn `HB-05` không bắt buộc; không phá nó vẫn qua chương, nhưng mất `hidden_released` và mất hòa giải thật.
