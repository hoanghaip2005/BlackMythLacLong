# ADR-002: Dùng ngôn ngữ hình ảnh Đông Sơn - Lạc Việt cho CH-01

## Status

Accepted

## Date

2026-09-12

## Context

CH-01 đã có blockout nhân vật Long Nhân và boss Ngư Tinh. Blockout trước đó cho thấy rủi ro khi lấy asset humanoid hoặc ornament có sẵn mà không có visual contract: outfit dễ lệch văn hóa, vũ khí thiếu điểm cầm, bàn chân sai hướng, còn boss cá dễ bị đọc thành rồng fantasy chung chung. Dự án cần thay asset linh hoạt nhưng vẫn giữ bản sắc Việt Nam.

## Decision

Dùng ngôn ngữ hình ảnh lấy cảm hứng từ Đông Sơn và đời sống sông biển Lạc Việt làm trục chung cho CH-01:

- Hình khối ưu tiên silhouette, trọng lượng vật liệu và dấu vết nước/bùn.
- Vật liệu chủ đạo là vải, da, đồng oxy hóa, đá, vỏ sò và ngọc sông.
- Motif được phép gồm hình học Đông Sơn tiết chế, dây dệt đỏ, tia mặt trời, chim cách điệu và cấu trúc áo giao lĩnh/tứ thân đã chuyển hóa cho gameplay.
- Cấm mây cuộn, long văn, giáp cung đình/hán phục, rồng bốn móng và các motif Trung Hoa hoặc Nhật dễ gây đọc nhầm.
- Boss Ngư Tinh giữ anatomy cá vực sâu; đuôi lửa biểu đạt yêu khí và vết thương, không dùng anatomy rồng.
- Mọi nhân vật quan trọng có visual harness riêng, asset provenance và acceptance checklist.

## Alternatives Considered

### Dùng fantasy Đông Á tổng quát

- Ưu: tìm asset nhanh, thư viện lớn.
- Nhược: mất bản sắc dự án, tăng nguy cơ trộn motif Trung Hoa/Nhật.
- Bác bỏ: không đáp ứng định hướng Việt Nam.

### Dựng mọi mesh thủ công từ đầu

- Ưu: kiểm soát toàn bộ hình dạng.
- Nhược: tốn thời gian, khó đạt chất lượng humanoid/rig sớm.
- Bác bỏ: dùng base asset CC0 được phép, sau đó thay lớp outfit, vũ khí và phụ kiện theo harness.

### Khóa chi tiết kỹ thuật trong narrative harness

- Ưu: dễ giao việc ngay.
- Nhược: khóa topology, shader và animation trước khi owner xác nhận.
- Bác bỏ: harness chỉ khóa visual intent, socket contract, provenance và acceptance; implementation để production owner.

## Consequences

- Asset source có thể thay thế mà không làm mất identity của nhân vật.
- Art, animation, VFX và gameplay có chung vocabulary để review.
- Cần cultural review khi thêm ornament hoặc thay source asset.
- Các file `.blend` hiện hành là blockout/reference; chưa được xem là final production asset.
- Thay đổi identity, motif cấm hoặc silhouette chủ đạo phải cập nhật visual harness và ADR/change request.
