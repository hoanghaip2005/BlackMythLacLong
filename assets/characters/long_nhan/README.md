# Long Nhân — nhân vật chính

| Phiên bản | Script | File | Trạng thái |
|---|---|---|---|
| v1 | `tools/build_long_nhan.py` | `long_nhan_concept.blend` | blockout hình khối, deprecated |
| v2 | `tools/build_long_nhan_mpfb.py` | `long_nhan_mpfb_v2.blend` | deprecated — xem "Lỗi của v2" |
| **v3** | `tools/build_long_nhan_v3.py` | `long_nhan_v3.blend` | **hiện hành** |

Dựng lại:

```bash
.tools/blender-4.5.9/blender-4.5.9-windows-x64/blender.exe -b -P tools/build_long_nhan_v3.py
```

Xuất ra `long_nhan_v3.blend`, `long_nhan_v3_hero.png`, `long_nhan_v3_portrait.png`.

## Lỗi của v2 và cách v3 sửa

1. **Thân hình nữ.** v2 đặt `gender = 0.94` nhưng để `cupsize` ở mặc định 0.5,
   nên base mesh giữ ngực nữ dưới lớp da nam. v3 đặt đủ mọi macro slider.

2. **Toạ độ sai hệ qui chiếu.** MPFB tạo hình cơ thể bằng shape key, nên
   `mesh.vertices[i].co` là mesh *chưa* biến dạng. v2 (và các bản v3 đầu) đọc
   toạ độ khớp và dựng KD-tree từ đó, trong khi tia đo lại bắn vào cơ thể đã
   biến dạng — đo một cơ thể, may cho một cơ thể khác. `shaped_coords()` giải
   shape key trước khi dùng.

3. **Tia đo trúng cánh tay.** Base mesh đứng tư thế A-pose, tia ngang ở tầm
   ngực chạm cánh tay trước khi tới sườn: đo được 1.89 đơn vị thay vì 0.95.
   Mọi món trang phục phần thân vì thế phồng gấp đôi. `build_ray_targets()`
   tách ra một BVH chỉ có thân mình cho các món ở thân.

4. **Trang phục cắt từ mesh cơ thể.** v2 cắt quần áo bằng lát cắt theo trục Z
   thế giới, để lại vai trần, nách hở và viền răng cưa. v3 không cắt gì: mỗi
   món được loft — chạy một polyline dọc chi hoặc cột sống, bắn tia đo tiết
   diện thật, làm mượt profile, rồi dựng ống quad tại bán kính đó cộng khoảng
   hở may đo.

5. **Rìu không nằm trong tay.** v2 đặt rìu theo toạ độ thế giới rồi mong tay IK
   chạm tới. v3 tạo dáng trước, đo ma trận lòng bàn tay rồi mới lắp rìu vào.
   Kèm theo một lỗi `matrix_world` đọc giá trị cũ khi chưa cập nhật depsgraph —
   lỗi này từng làm rìu rơi về gốc toạ độ.

6. **Ánh sáng giết màu da.** v2 chiếu gần như toàn bộ bằng rim teal và cyan.
   v3 để key ấm gánh phần đọc hình, đẩy ánh sáng lạnh xuống vai trò viền.

7. **Khuôn mặt vô hồn.** Chỉ macro slider thì mặt luôn mềm và không tuổi. v3
   áp 46 detail target của MakeHuman (`DETAIL_TARGETS`): gờ mày nặng, gò má
   rộng, hàm vuông, cổ dày, thân chữ V, tay chân có cơ.

## Tư thế: bỏ IK, dùng FK

Bàn chân từng chỉ ngược về phía sau (`foot_l` đuôi xương ở y = +0.43,
`foot_r` ở +0.93, trong khi nhân vật quay mặt về -Y) và tay trông như bị xoắn.
Thủ phạm là `pole_angle` của ràng buộc IK: nó xoay cả chuỗi chi quanh trục của
chính nó. Ở đây không có gì cần "giải" cả — hướng của từng chi đã biết trước —
nên IK bị bỏ hoàn toàn. `aim_bone()` hướng từng xương theo một vector trong
không gian thế giới kèm một vector tham chiếu khoá độ xoay, nên không thể xoắn.
`ground_rig()` sau đó hạ rig xuống cho đế giày chạm bệ đá.

Một lỗi liên quan: `parent_to_bone` đọc `matrix_world` trước khi depsgraph kịp
cập nhật, nên chụp phải ma trận cũ — đó là lý do các ngôi sao đồng ở vai bay
lơ lửng cạnh nhân vật, và trước đó là lý do cây rìu rơi về gốc toạ độ.

## Trang phục từ thư viện CC0

Quần, giày và tóc nay lấy từ các gói CC0 của MakeHuman Community thay vì dựng
bằng code — đó là những món chung chung, không có lý do gì phải tự sinh. Xem
`assets/libraries/makehuman-mpfb/README.md` để biết gói nào dùng, gói nào
không và vì sao.

Áo vẫn dựng bằng code: **không gói CC0 nào có áo giao lĩnh Việt**, mà đó lại
chính là món cần đúng nhất.

## Còn tồn đọng

- Còn khe hở nhỏ lộ da ở đỉnh vai, chỗ ống vai (yoke) gặp tay áo.
- Lưỡi rìu vẫn đọc như một khối đá hơn là một lưỡi rìu cong.
- Cổ áo giao lĩnh (vạt chéo) đã bỏ: qua nhiều lần thử nó luôn đâm xuyên thân
  áo. Cần dựng như một mesh riêng có đường viền, không phải ribbon cắt từ ring.
- Chưa có UV/texture bake, chưa tối ưu poly cho game engine.

## Nguồn asset

MPFB 2.0.17 + MakeHuman System Assets (CC0), cùng các gói CC0 `pants01`,
`shoes01`, `hair01` (xem `assets/libraries/makehuman-mpfb/README.md`). Da
`young_asian_male`, rig `game_engine`. Không dùng motif mây, hoa văn cung đình hay hanfu Trung Hoa;
hoạ tiết là vòng tia trống đồng Đông Sơn, thắt lưng đỏ Lạc, ngọc sông.
