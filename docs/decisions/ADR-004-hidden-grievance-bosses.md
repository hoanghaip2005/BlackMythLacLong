# ADR-004: Thêm lớp "Oan Khuất Ẩn" (boss ẩn mỗi chương) và gate kết thúc thật

## Status

Accepted

## Date

2026-09-12

## Context

Bộ harness hiện tại đã khóa sáu chương, năm mảnh Long Ngọc, bốn ending và Resolution Rules. Kết thúc thật `E-04 Hòa Giải Bách Tộc` vốn đã là kết thúc ẩn có điều kiện (`reconcile` + `memory_recovered = 5` + `mercy_marks >= 4` + `tribal_trust >= 5` + đủ năm `truth_flags` + không quá hai boss `absorbed`).

Tuy nhiên, yêu cầu thiết kế mới từ chủ dự án là: **mỗi chương phải có một màn ẩn và một boss ẩn tùy chọn**, và **kết thúc thật chỉ mở khi người chơi hoàn thành trọn vẹn (full completion)**, gồm cả nội dung ẩn. Hiện tại:

- `01-story-bible.md` §6 đã có "Ba Nguyên thần phụ" (`NGUYEN-THAN-THUONG-LUONG`, `NGUYEN-THAN-CHAN-TINH`, `NGUYEN-THAN-TINH-VUON`) là các encounter phụ mở đòn Hóa Thần — nhưng chúng là *hook sức mạnh chiến đấu*, không phủ đủ năm chương và không gắn với tiến trình "sự thật".
- Chưa có lớp nội dung ẩn nào gắn với việc *đào sâu truth flag* của từng chương.
- `E-04` chưa yêu cầu hoàn thành nội dung ẩn, nên "full completion" chưa thực sự là điều kiện của kết thúc thật.

Cần một lớp nội dung ẩn nhất quán, có chức năng chủ đề rõ, không phá Canon Locks, và gate được `E-04`.

## Decision

Thêm lớp canon **"Oan Khuất Ẩn"** (Hidden Grievance): mỗi chương `CH-01..CH-05` có **một màn ẩn** và **một boss ẩn** tùy chọn. `CH-06` không có boss ẩn riêng; thay vào đó, full completion của năm chương mở *lớp hòa giải trọn vẹn* của `E-04`.

### Quy tắc lớp Oan Khuất Ẩn

1. **ID:** boss ẩn `HB-01..HB-05` ( Hidden Boss, theo chương). Màn ẩn dùng scene id `CH-0X-HIDDEN` (một scene tùy chọn mỗi chương). Quest ẩn `Q-CH0X-00H`. Cờ `CH0X_HIDDEN_RELEASED`.
2. **Tùy chọn, không chặn tiến độ chính:** bỏ boss ẩn vẫn hoàn thành chương và vẫn đạt được `E-01/E-02/E-03`. Chỉ `E-04` (kết thúc thật) yêu cầu full completion.
3. **Cũng là một bi kịch (Canon Lock 7 mở rộng):** mỗi boss ẩn có `inner_wound`, `desire`, và một `bond_resolution`; không mô tả như ác tuyệt đối.
4. **Đào sâu truth flag của chương:** giải thoát boss ẩn mở một **lớp sự thật phụ** (`hidden_truth`) làm sâu thêm `TRUTH_*` của chương đó, không tạo truth flag toàn cục mới và không tạo Long Ngọc mới (giữ Canon Lock 5: đúng năm mảnh).
5. **Boss fate dùng lại enum sẵn có** (`released`, `defeated_by_force`, `absorbed`, `sacrificed`, `escaped`). Chỉ `released` mới cộng `hidden_released` và `mercy_marks`.
6. **Không trùng chức năng với Ba Nguyên thần phụ:** Oan Khuất Ẩn thiên về *sự thật + hoàn thành + mercy*; Nguyên thần phụ thiên về *mở đòn Hóa Thần*. Một chương có thể có cả hai; chúng là hai encounter khác nhau. (Khuyến nghị: về sau có thể hợp nhất từng cặp nếu production cần giảm scope — ghi ADR mới khi làm vậy.)

### Biến số mới

| ID | Miền | Khởi tạo | Ý nghĩa |
|---|---:|---:|---|
| `hidden_released` | 0..5 | 0 | Số boss ẩn (`HB-01..HB-05`) đã được **giải thoát** |

Quy tắc tăng: giải thoát một `HB-0X` ⇒ `hidden_released +1`, `mercy_marks +1`. Cưỡng đoạt/hạ boss ẩn ⇒ `dragon_hunger +1`, **không** tăng `hidden_released`.

### Năm boss ẩn (canon)

| ID | Chương | Màn ẩn | Boss ẩn | Vết thương vùng đất đào sâu | `hidden_truth` |
|---|---|---|---|---|---|
| `HB-01` | CH-01 Vực Biển Đông | Bãi xác thuyền dưới vực | **Ma Da — Vong Đáy Vực** (oan hồn người đi biển bị lời hứa bảo hộ bỏ mặc) | bị bỏ rơi | Lời hứa bảo hộ từng *thất bại trước cả khi* đền chìm; "phong ấn" chưa từng là vấn đề |
| `HB-02` | CH-02 Đầm Xác Cáo | Hang gương dưới đầm | **Bóng Vô Danh** (người tị nạn đầu tiên được Hồ Tinh che, bị Hỗn Mang ăn mất tên) | mất tên | Hồ Tinh từng *giữ tên* cho người chạy loạn; chính nỗi sợ của họ tạo lớp mặt nạ |
| `HB-03` | CH-03 Rừng Phong Châu | Gò mộ dưới rễ | **Tướng Quân Vô Đầu** (chỉ huy tự trói mình vào lời thề sau khi chết) | lời thề bị trói | Một phần vong binh *tự nguyện* ở lại vì sợ bị lịch sử quên |
| `HB-04` | CH-04 Núi Thạch Môn | Khe đá dựng (rừng bia không tên) | **Tù Trưởng Lệ Đá** (thủ lĩnh bộ tộc bị xóa tên, hóa đá, lệ thành đá núi) | bị xóa khỏi lịch sử | Tên bộ tộc bị xóa *có chủ đích* bởi triều đại "thống nhất", không phải thời gian |
| `HB-05` | CH-05 Ngã Ba Hạc | Miếu chìm ở ngã ba nước | **Giao Mẫu** (mẹ của Song Giao, chia nước cho hai con, bị xé nát khi chúng tranh nhau) | tranh quyền dòng nước | Có một *nạn nhân thứ ba* của cuộc tranh chấp mà cả hai giao đều đã quên |

`CH-06`: không có `HB-06`. Full completion (`hidden_released = 5`) mở **lớp hòa giải trọn vẹn** của `E-04` (xem dưới).

### Cập nhật Resolution Rules (E-04)

Thêm vào điều kiện `E-04 Hòa Giải Bách Tộc`:

- `hidden_released = 5` (đã giải thoát cả năm Oan Khuất Ẩn).

Cập nhật **Fallback `reconcile` thiếu điều kiện**: nếu chọn `reconcile` mà thiếu `hidden_released = 5` (nhưng vẫn đủ các điều kiện khác), nghi lễ hòa giải đạt *một phần*: các cộng đồng lớn nhìn thấy sự thật, nhưng năm oan khuất ẩn chưa được gọi tên ⇒ gắn tag `E-04-PARTIAL` (hòa giải chưa trọn, còn dư oán ẩn). Nếu thiếu các điều kiện lõi khác (memory/mercy/trust/truth) thì vẫn fallback về `E-03-BITTER` như cũ.

## Alternatives Considered

### Giữ nguyên E-04, không thêm boss ẩn

- Ưu: không đổi canon, không cần ADR.
- Nhược: không đáp ứng yêu cầu "màn ẩn + boss ẩn mỗi chương" và "full completion mới ra kết thật".
- Bác bỏ: trái yêu cầu thiết kế đã duyệt.

### Biến Ba Nguyên thần phụ thành boss ẩn

- Ưu: tái sử dụng encounter sẵn có, giảm scope.
- Nhược: chỉ có ba, không phủ năm chương; chức năng của chúng là mở đòn Hóa Thần, không phải đào sâu truth; gộp lại làm mất một lớp phần thưởng chiến đấu.
- Bác bỏ: giữ hai lớp tách biệt; có thể hợp nhất từng cặp về sau bằng ADR mới nếu cần giảm scope.

### Thưởng sức mạnh mạnh cho boss ẩn

- Ưu: khuyến khích khám phá.
- Nhược: dễ biến nội dung ẩn thành "checklist tăng power", làm loãng chủ đề *lắng nghe/ hóa giải*; xung đột tinh thần Canon Lock 6 (Long Ngọc là ký ức, không phải vật phẩm tăng sức mạnh).
- Bác bỏ: phần thưởng chính của boss ẩn là *sự thật + mercy + full completion*, không phải power creep.

## Consequences

- `02-branching-and-endings.md`: thêm biến `hidden_released`, thêm §"Oan Khuất Ẩn", cập nhật điều kiện `E-04` và fallback (`E-04-PARTIAL`).
- `03-chapter-harness.md`: mỗi chương `CH-01..CH-05` thêm mục boss ẩn + màn ẩn; `CH-06` ghi chú full completion mở lớp hòa giải trọn vẹn.
- `08-continuity-matrix.md`: thêm hàng "Oan Khuất Ẩn" và thread `hidden_released`.
- `content-registry.yaml`: thêm `hidden_released` vào `variables`, thêm mục `hidden_bosses`, thêm `package_path` cho `CH-02..CH-06`.
- `docs/harness/chapter-01/`: bổ sung `HB-01` (màn ẩn, boss ẩn, quest ẩn, cờ, validation, visual) vào package hiện có.
- Mỗi package `CH-02..CH-06`: phải gồm boss ẩn của chương.
- Không đổi: số mảnh Long Ngọc (5), danh tính boss chính, thứ tự chương, bốn ending key, Canon Locks 1-9.
- Boss ẩn là content `draft`; cần cultural review (đặc biệt `HB-01` Ma Da — tín ngưỡng dân gian về người chết đuối) trước khi `approved`.
