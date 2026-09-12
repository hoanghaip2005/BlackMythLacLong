# CH-02 Cast and Factions

## Long Nhân

- ID: `PLAYER-LONG-NHAN`
- Chapter function: người mang khuôn mặt thật duy nhất trong một nơi mọi khuôn mặt đều đáng ngờ; học rằng nghi ngờ không đồng nghĩa với săn đuổi.
- Starting desire: theo tiếng hát để hiểu ai đang gọi mình và vì sao.
- Chapter need: nhận ra "kẻ săn" và "người che chở" có thể bị tráo nhãn, và sức mạnh mượn mặt là một cái bẫy.
- Voice rule: đã nói nhiều hơn CH-01 nhưng vẫn ngắn; bắt đầu đặt câu hỏi thay vì chỉ gọi tên vật thể.
- Forbidden: không biết toàn bộ sự thật về Hỗn Mang; không tự tin mình phân biệt được thật/giả chỉ vì có huyết mạch.

## Hồ Tinh - Cửu Vĩ

- ID: `B-02`
- Faction: sinh vật bị yêu khí khuếch đại; không đại diện cho mọi "yêu".
- Hình thái chiến đấu: hai phase; `B02-P1-MASK` là ba khuôn mặt mượn (ảo ảnh/Phân Thân), `B02-P2-CUUVI` là cáo chín đuôi thật lộ diện. `B02-P0` chỉ là intro lộ diện qua mặt gương.
- Bề mặt: xuất hiện dưới nhiều khuôn mặt người (đứa trẻ, dân làng, và cả Long Nhân); hình thật là một con cáo đầm lớn, lông ướt bết, chín đuôi, mỗi đuôi cuộn một mặt nạ.
- Vết thương: từng che chở người chạy loạn, rồi bị chính họ nghi ngờ và bị đời sau gọi là quái ăn thịt người.
- Mong muốn: giữ tên thật của những người nó đã giấu, để không ai bị gọi nhầm và bị tìm ra.
- Sợ hãi: Long Nhân là một kẻ săn mới, đến "giải phóng" bằng cách giết những cái bóng nó đang giữ.
- Mâu thuẫn: nó ghét bị nghi ngờ nhưng vẫn đeo mặt nạ, vì mặt nạ là cách duy nhất nó từng bảo vệ được ai.
- Cấm viết: không biến thành hồ ly quyến rũ sáo rỗng; không cho nó xin tha dễ dàng; `released` phải là kết quả của việc người chơi gọi đúng tên, không phải giảm HP.

## Người Hát

- ID: `NPC-CH02-SINGER`
- Faction: Dân đầm Tây Hồ (đã thành bóng).
- Chức năng: nhân chứng cho bond của `LG-02`; là tiếng hát hook từ CH-01; không phải Hồ Tinh.
- Diện mạo: một cái bóng người phụ nữ không có mặt ổn định; chỉ giọng hát là nhất quán.
- Bề mặt: xa cách, hát tên người khác nhưng quên tên mình.
- Nhu cầu: được ai đó gọi lại tên thật của chính mình.
- Bí mật: cô là một trong những người Hồ Tinh từng giấu; cô tự nguyện quên tên để kẻ săn không tìm ra con mình.
- Arc CH-02: mồi dẫn (bị nghi là yêu) -> nhân chứng -> người đầu tiên lấy lại tên (ở `released`).
- Nếu `tribal_trust >= 3` và `released`: có thể đi cùng Long Nhân một đoạn (đồng hành ngắn hạn, không combat cố định).
- Cấm viết: không biến cô thành phần thưởng tình cảm; không cho cô biết toàn bộ âm mưu Hỗn Mang.

## Đạo sĩ

- ID: `NPC-CH02-DAO-SI`
- Faction: người ngoài đến đầm; tự nhận bảo hộ.
- Trạng thái: sống, tỉnh hoặc bị nuốt tùy lựa chọn; không chết mặc định.
- Chức năng: cho thấy Hỗn Mang dùng người tốt làm công cụ; là "khuôn mặt thật bị đội lốt".
- Bề mặt: quyết liệt trừ tà, tin Hồ Tinh ăn thịt người, được một nhóm dân đầm tin theo.
- Nhu cầu: chuộc lỗi vì một lần ông đã không cứu được người.
- Bí mật: mắt ông phản chiếu một khuôn mặt mượn - Hỗn Mang nói qua ông. Ông không biết mình bị đội lốt.
- Arc CH-02: kẻ săn được tin -> bị vạch trần là con rối -> (nếu được tha) tỉnh lại và giúp gọi tên.
- Cấm viết: không biến ông thành ác nhân chủ động; ông là nạn nhân của lời đồn và của chính nỗi sợ.

## Cụ Đàm

- ID: `NPC-CH02-CU-DAM`
- Faction: Dân đầm Tây Hồ (người gốc, còn bóng, nửa nhớ nửa quên).
- Chức năng: nguồn lịch sử không hoàn hảo; giữ những mảnh tên rời rạc.
- Giọng: chậm, nói lẫn giữa tên người và tên chỗ.
- Câu lõi: "Đầm này không chôn cáo. Đầm này chôn những cái tên không ai gọi nữa."
- Cấm viết: không cho cụ xác nhận phong ấn đã vỡ; cụ chỉ biết "ngày xưa người ta chạy tới đây rồi mất tên".

## Tiếng Vọng Lạc Long

- ID: `ECHO-LAC-LONG-02`
- Faction: ký ức biểu tượng.
- Xuất hiện: trong mặt gương nước, trong mắt phản chiếu của mặt nạ; không có cơ thể.
- Chức năng: đặt câu hỏi về bản ngã và mặt nạ, không đưa đáp án.
- Câu hỏi CH-02: "Nếu mặt nạ là đất, con có dám nặn mặt mình không?"

## Dân đầm Tây Hồ

- Mong muốn tập thể: lấy lại tên, hoặc được yên; không thống nhất.
- Chia rẽ nội bộ:
  - Nhóm theo đạo sĩ, muốn giết "con cáo" để hết mất bóng.
  - Nhóm im lặng, nửa nhớ rằng cáo từng che chở họ, sợ nói ra sẽ bị tìm.
- Phản hồi lựa chọn:
  - `tribal_trust >= 1`: chỉ chỗ mặt nạ thật và đường xuống hang gương.
  - `tribal_trust = 0`: để Long Nhân đi qua nhưng giấu clue đối chiếu.
  - `boss_fates[B-02] = absorbed`: gọi Long Nhân là "cái bóng biết đi", không giao bond.

## Bóng (dân đầm mất tên)

- Không phải enemy mặc định. Chúng là người, bị rỗng tên. Đánh chúng bằng lực là thất bại bond; gọi tên mới là counterplay.
- Không dùng chúng làm vật chứa lore về Hỗn Mang; lore đó thuộc Hồ Tinh, Người Hát, Cụ Đàm và màn ẩn.

## Yêu tộc phụ

- Mặt nạ nổi, cáo đất sét, ma trơi. Chúng là yêu khí mượn hình để dạy cơ chế thật/giả. Không đặt tên riêng; không phải nguồn lore chính.
