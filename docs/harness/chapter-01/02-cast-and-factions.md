# CH-01 Cast and Factions

## Long Nhân

- ID: `PLAYER-LONG-NHAN`
- Chapter function: nhân vật không tên để người chơi đặt câu hỏi về huyết thống.
- Starting desire: sống sót và tìm hiểu tiếng gọi dưới đáy biển.
- Chapter need: nhận ra mỗi sức mạnh đều có người bị bỏ lại phía sau.
- Voice rule: đầu chapter gần như không nói; sau khi nhận nguyên thần chỉ nói những câu ngắn, cụ thể.
- Forbidden: không tự kể quá khứ của mình, không gọi bản thân là hậu duệ “cao quý”, không biết toàn bộ sự thật.

## Linh - người giữ đèn

- ID: `NPC-CH01-LINH`
- Faction: Thủy tộc Biển Đông.
- Chức năng: nhân chứng sống cho bond của `LG-01`, không phải companion combat cố định.
- Tuổi/diện mạo: người trưởng thành trẻ, bị thương ở chân, mang đèn vỏ sò.
- Bề mặt: cảnh giác, thực tế, không tin huyết thống.
- Nhu cầu: giữ cho đèn đền còn sáng để người chết dưới đáy không bị lãng quên.
- Bí mật: cô từng định rời vùng biển trước khi đền sập; mặc cảm khiến cô bám vào nhiệm vụ.
- Arc CH-01: con mồi bị cứu -> người dẫn đường -> người đặt giới hạn cho Long Nhân.
- Nếu bị bỏ lại: vẫn sống, nhưng không trở thành người bảo chứng cho Long Nhân.
- Cấm viết: không biến Linh thành người ngưỡng mộ Long Nhân sau một lựa chọn duy nhất.

## Bà Từ Hải - người giữ bia

- ID: `NPC-CH01-BA-TU-HAI`
- Faction: Thủy tộc Biển Đông.
- Trạng thái: có thể sống, chết hoặc chỉ còn tiếng vọng tùy content scope; vertical slice ưu tiên xuất hiện qua bia và tiếng chuông.
- Chức năng: nguồn lịch sử không hoàn hảo, xác nhận rằng lời hứa từng có thật.
- Giọng: bình tĩnh, nói như người đã quá quen với việc chờ đợi.
- Câu lõi: “Biển không quên. Biển chỉ giữ mọi thứ ở nơi không ai còn nghe thấy.”
- Cấm viết: không cho bà xác nhận phong ấn đã vỡ; bà chỉ biết đền không còn hoạt động đúng.

## Ngư Tinh

- ID: `B-01`
- Faction: sinh vật bị yêu khí khuếch đại; không đại diện toàn bộ thủy tộc.
- Hình thái chiến đấu: hai phase; `B01-P1-HYBRID` là người lai cá có chủ ý, `B01-P2-ABYSSAL` là cá vực sâu khổng lồ mất kiểm soát. `B01-P0` chỉ là intro lộ diện.
- Bề mặt: ban đầu dựng thân người lai cá với đuôi cá, sau đó vỡ hình thành quái ngư khổng lồ với đuôi lửa mọc lại; cả hai hình thái đều làm dâng nước và săn mọi thứ có huyết mạch rồng.
- Vết thương: bị chém đứt đuôi, bị bỏ lại cùng lời hứa bảo hộ.
- Mong muốn: giữ Long Ngọc và giữ tất cả dưới biển để không ai có thể bỏ rơi nó lần nữa.
- Sợ hãi: Long Nhân chỉ là một Lạc Long Quân mới, đến lấy ngọc rồi rời đi.
- Mâu thuẫn: nó ghét lời hứa nhưng vẫn dùng toàn bộ đời mình để chứng minh lời hứa từng tồn tại.
- Cấm viết: không cho nó xin tha mạng dễ dàng; `released` phải là kết quả của hành động người chơi.

## Tiếng Vọng Lạc Long

- ID: `ECHO-LAC-LONG-01`
- Faction: ký ức biểu tượng.
- Xuất hiện: phản chiếu trên vỏ trứng, mặt bia, hoặc lưỡi rìu; không có cơ thể.
- Chức năng: đặt câu hỏi, không đưa đáp án.
- Giọng: không chắc là nam hay nữ; tránh bắt chước giọng một vị thần toàn tri.
- Câu hỏi CH-01: “Con muốn nhớ điều gì, hay chỉ muốn mạnh hơn?”

## Thủy tộc Biển Đông

- Mong muốn tập thể: giữ đèn đền, cứu người sống, chấm dứt nước dâng.
- Chia rẽ nội bộ:
  - Nhóm muốn giao `LG-01` cho bất kỳ ai đủ mạnh để giết Ngư Tinh.
  - Nhóm muốn giữ ngọc vì sợ lịch sử bị lấy đi lần nữa.
- Phản hồi lựa chọn:
  - `tribal_trust >= 1`: trao thông tin và đường tắt.
  - `tribal_trust = 0`: cho phép đi qua nhưng giấu một phần sự thật.
  - `boss_fates[B-01] = absorbed`: không gọi Long Nhân là người bảo hộ.

## Yêu tộc phụ

Không đặt tên riêng trong CH-01. Chúng là sinh vật bị biến dạng để tutorial truyền đạt sự bất thường của biển. Không dùng chúng làm vật chứa lore về Hỗn Mang; lore đó thuộc Ngư Tinh, bia và Tiếng Vọng.
