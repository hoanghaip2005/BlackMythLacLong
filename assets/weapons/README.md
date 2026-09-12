# Bộ vũ khí Đông Sơn

Dựng lại:

```bash
.tools/blender-4.5.9/blender-4.5.9-windows-x64/blender.exe -b -P tools/build_weapons.py
```

Xuất ra `dong_son_weapons.blend`, một bảng tổng `dong_son_weapons_sheet.png` và
ba ảnh cận cảnh.

## Vì sao phải tự dựng

Không thư viện open-source nào có vũ khí Việt thời đại đồng. Gói CC0
`equipment01` của MakeHuman Community mà ta đã tải chỉ có búa chiến, kiếm thô,
dao găm, cung và quyền trượng — đều là fantasy phương Tây. Nên bộ này được
dựng từ hiện vật Đông Sơn có thật, không phải từ quy ước game fantasy.

## Tám món

| Tên | Bám vào đâu |
|---|---|
| `dao_gam_can_tuong` | Dao găm cán tượng người — hiện vật Đông Sơn dễ nhận nhất. Cán là một người đứng chống nạnh, mặc váy, búi tóc. |
| `doan_kiem_ri_set` | **Canon CH-01**: thanh đoản kiếm Long Nhân tỉnh dậy bên cạnh. Dựng sẵn trạng thái hỏng — lưỡi sứt mẻ, mũi cụt — để đọc ra "vật sinh tồn tạm thời", đúng như `00-chapter-brief.md` ghi. Vỡ khi rìu thức tỉnh. |
| `riu_xeo_chien_binh` | Rìu lưỡi xéo — rìu chiến Đông Sơn lưỡi lệch. Bản lính thường. |
| `riu_than_thach_son` | **Canon**: vũ khí kế thừa. Cùng dáng rìu xéo nhưng cỡ nghi lễ, có mặt trời trống đồng trên má lưỡi, Long Khí cháy dọc lưỡi và mảnh Long Ngọc ở chuôi. |
| `qua_dong` | Qua đồng — lưỡi gắn vuông góc cán, dùng để móc và kéo, không phải để chặt. |
| `giao_dong` | Giáo đồng lưỡi hình lá có sống nổi, họng tra cán có băng vòng tròn tiếp tuyến. |
| `no_than` | Nỏ thần An Dương Vương. Hộp lẫy làm riêng bằng đồng — trong truyền thuyết mất lẫy là mất nước. |
| `moc_khien` | Mộc khiên mang trọn một mặt trống đồng. |

## Vốn hoa văn

`tools/dong_son_ornament.py` là module riêng, dùng lại được cho giáp, trang sức,
kiến trúc hay UI. Mỗi hoa văn là hình khối nổi thật, không phải texture vẽ:

- `sun_star` — mặt trời nhiều tia ở tâm trống (trống thật có 8, 10, 12, 14 hoặc 16 tia)
- `tangent_circles` — vòng tròn tiếp tuyến. Hay bị làm sai: các vòng **phải chạm nhau**, nối bằng đường tiếp tuyến chung, không phải xếp cạnh nhau
- `saw_tooth_band` — hoa văn răng cưa
- `dot_band` — băng chấm dải
- `lac_bird_ring` — chim Lạc bay **ngược chiều kim đồng hồ**, mỏ dài, cánh giương, đuôi xoè
- `rope_twist` — thừng bện
- `drum_face` — ghép tất cả theo đúng thứ tự băng của mặt trống thật: mặt trời ở tâm, các băng hình học, rồi băng chim ở gần vành

Cố ý **loại trừ**: mây cuộn, rồng, hoa văn cung đình và hanfu Trung Hoa, cùng
mọi motif Nhật. Đây đúng là những thứ dự án hay bị vay mượn nhầm và chúng không
phải Đông Sơn.

## Tỉ lệ

`M = 4.77` đơn vị mỗi mét, khớp rig nhân vật. Có thể append thẳng bất kỳ
collection vũ khí nào vào scene Long Nhân rồi parent vào xương tay.

## Còn yếu

- Nỏ thần là món yếu nhất: thân và cánh nỏ còn thô, cơ cấu lẫy chỉ là khối hộp.
- Lưỡi qua vẫn hơi đọc như lá cờ; cần thêm sống lưỡi.
- Mới chỉ mộc khiên mang **trọn** mặt trống; các món khác chỉ mang mô-típ mặt
  trời. Module đã đủ để thêm băng vào bất cứ đâu nếu muốn.
- Vật liệu hoàn toàn procedural, chưa UV unwrap, chưa bake texture, chưa tối ưu
  poly cho game engine.
