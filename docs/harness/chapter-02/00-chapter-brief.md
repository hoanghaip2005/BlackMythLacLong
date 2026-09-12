# CH-02: Ảo Ảnh Đầm Cáo

## Trạng thái

- ID: `CH-02`
- Version: `0.1`
- Status: `draft`
- Vùng: Tây Hồ - Đầm Xác Cáo, làng chài ven hồ, sương không tan và gương nước.
- Thời lượng narrative mục tiêu: 90-120 phút cho first playthrough, chưa tính khám phá tùy chọn và màn ẩn.
- Mảnh Long Ngọc: `LG-02`
- Boss: `B-02`, Hồ Tinh - Cửu Vĩ
- Boss ẩn: `HB-02`, Bóng Vô Danh (ADR-004)
- Truth flag: `TRUTH_FOX_WAS_A_REFUGE`

## Chapter promise

Người chơi đến Đầm Xác Cáo với một tiếng hát dẫn đường và một niềm tin rằng có con hồ ly ăn thịt người. Cuối chương, người chơi hiểu ba điều:

1. Không thể tin một khuôn mặt khi tên thật đã bị lấy đi; thật/giả phải được đối chiếu, không được ban phát.
2. Hồ Tinh không bắt người - nó từng giấu người chạy loạn; chính nỗi sợ và lời đồn đã tạo nên lớp mặt nạ.
3. Kẻ ăn tên thật không phải con cáo. Có một thứ khác đứng sau, đội lốt nỗi sợ.

## Dramatic question

**Khi mọi khuôn mặt đều có thể là mặt nạ, Long Nhân sẽ tin vào hình hài mạnh nhất trước mắt, hay chịu khó trả lại tên cho những cái bóng?**

## Emotional arc

| Chặng | Trạng thái Long Nhân | Cảm xúc người chơi | Hình ảnh chủ đạo |
|---|---|---|---|
| Mở đầu | Mang rìu nhưng chưa mang ký ức | Lạnh, bất an, bị theo dõi | Làng không đổ bóng, ma trơi lập lòe |
| Khám phá | Bắt đầu nghi ngờ khuôn mặt | Tò mò, hoang mang | Tiếng hát dưới sương, gương nước |
| Điều tra | Nhận ra lời đồn là vũ khí | Hoài nghi, thương cảm | Mặt nạ nổi trên đầm, bia không tên |
| Đối đầu | Bị Cửu Vĩ gọi là "kẻ săn mới" | Giận dữ, phân vân | Chín đuôi xòe như chín cái bóng |
| Hậu quả | Tự chọn cách nhận nguyên thần | Trách nhiệm, dự cảm | Tên được gọi lại, hoặc bóng nuốt tên |

## Chapter non-goals

- Chưa giải thích Hỗn Mang đầy đủ; CH-02 chỉ cho thấy nó *dùng giả dạng để phá niềm tin*.
- Chưa mở hệ thống ba stance như một bộ hoàn chỉnh; CH-02 giới thiệu `Phân Thân` qua tình huống bản ngã, không phải qua menu.
- Chưa cho người chơi gặp Mộc Tinh, Đại Bàng Tinh hoặc Song Giao.
- Chưa xác nhận phong ấn đã vỡ; mọi lời về "con hồ ly phá làng" ở đây là lời đồn hoặc diễn giải sai.
- Không biến Hồ Tinh thành hồ ly tinh quyến rũ kiểu sáo rỗng; nó là kẻ che chở bị nghi ngờ.

## Canon lock riêng cho CH-02

1. Long Nhân đến Đầm Xác Cáo với Rìu Thần Thạch Sơn đã thức tỉnh (sau CH-01); không có Long Ngọc nào ngoài `LG-01` nếu người chơi đã nhận.
2. Hồ Tinh - Cửu Vĩ từng biến đầm thành nơi trú ẩn cho người chạy loạn chiến tranh; nó giữ tên thật của họ thay họ.
3. Lớp mặt nạ và những cái bóng không hồn sinh ra từ nỗi sợ và sự hoài nghi của chính dân đầm, được Hỗn Mang khuếch đại - không phải do Hồ Tinh chủ động nguyền.
4. `LG-02` nằm trong Hồ Tinh như một "neo ký ức" về thời đầm là nơi trú ẩn; thu hồi mà không giải bond sẽ khiến Long Khí mạnh lên nhưng tăng nguy cơ Hỗn Mang bám.
5. Tiếng hát nữ dẫn vào CH-02 (hook từ `CH-01-S08`) là mồi của một cái bóng mất tên, không phải Hồ Tinh xuất hiện trực tiếp ở đầu chương.
6. `Phân Thân` (ảo ảnh đất sét) chỉ mở sau khi người chơi hiểu "hình hài có thể là mặt nạ"; không mở trước `CH-02-S03`.
7. Không có lựa chọn nào khiến người chơi bỏ qua `LG-02`; lựa chọn chỉ đổi cách thu hồi và trạng thái của mảnh ngọc.
8. Chương kết thúc khi tên thật được gọi lại (hoặc bị nuốt), tại bờ đầm, không phải khi rời Tây Hồ.

## Chapter end states

### `CH02_END_RELEASED`

Hồ Tinh được giải thoát khỏi vai kẻ bị săn. Những cái tên nó giữ được trả về; dân đầm lấy lại bóng và tên. Long Nhân nhận `LG-02` qua sự đồng thuận của nguyên thần. Nếu `tribal_trust` đủ, Người Hát trở thành NPC đồng hành ngắn hạn; nếu không, cô chỉ còn là tiếng hát trong sương.

### `CH02_END_FORCE`

Cửu Vĩ bị hạ nhưng bond chưa giải quyết. Những cái tên vẫn thất lạc; dân đầm còn là bóng nửa vời và không tin Long Nhân. `LG-02` hoạt động không ổn định. Người chơi lấy sức mạnh nhưng mất một phần ký ức của đầm.

### `CH02_END_ABSORBED`

Long Nhân cưỡng đoạt nguyên thần, nuốt luôn năng lực "mượn mặt". `dragon_hunger` tăng. `Phân Thân` mạnh hơn nhưng hình ảnh nhiễu; dân đầm nhìn Long Nhân như một kẻ ăn tên mới. Gieo mầm E-02, không khóa ending.

## Handoff summary

CH-02 cần ba lớp bàn giao:

- **Narrative:** scene flow, dialogue, choice effects, boss fate, hidden boss fate.
- **Gameplay hook:** phân biệt thật/giả qua đối chiếu, `Phân Thân`, gương nước làm bề mặt đọc clue, arena đầm đổi theo sương, phase telegraph của Cửu Vĩ.
- **Art/audio hook:** ma trơi, sương, mặt nạ nổi, đầm xác cáo, tiếng hát trễ vọng, chín đuôi như chín cái bóng.

Thông số damage, map coordinates, animation frame, model topology và VFX implementation để `TBD` ở phase sau.
