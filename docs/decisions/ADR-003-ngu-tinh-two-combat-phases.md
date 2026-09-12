# ADR-003: Ngư Tinh có hai hình thái chiến đấu trong CH-01

## Status

Accepted

## Date

2026-09-12

## Context

Ngư Tinh cần vừa giữ được chiều sâu nhân vật vừa tạo trận boss dễ đọc. Một hình thái cá khổng lồ duy nhất cho thấy quy mô nhưng thiếu khoảnh khắc đối diện; nhiều phase nhỏ làm loãng nhịp trận. Hình thái người lai cá giải quyết khoảng giữa: người chơi nhìn thấy ý chí và phần ký ức của Ngư Tinh trước khi yêu khí nuốt mất khả năng tự chủ.

## Decision

Trận Ngư Tinh dùng đúng hai combat phase:

- `B01-P1-HYBRID`: người lai cá, thân trên dựng, hai tay có màng/móng, đuôi cá làm trụ; combat thiên về đọc cận chiến, mang phun nước và đuôi quét thấp.
- `B01-P2-ABYSSAL`: cá vực sâu khổng lồ, thân trên không còn giữ được hình người; combat thiên về xoáy lớn, sóng, đuôi lửa và arena sụp đổ.

`B01-P0` là intro không chiến đấu. Đợt dâng nước cuối, ba neo và cửa sổ bond nằm trong `B01-P2`, không tạo phase thứ ba.

## Alternatives Considered

### Chỉ dùng cá khổng lồ

- Ưu: silhouette đơn giản, quy mô rõ.
- Nhược: thiếu đối diện nhân vật và bước chuyển bi kịch.
- Bác bỏ: không đủ truyền tải vết thương và lời hứa bị bỏ lại.

### Ba combat phase độc lập

- Ưu: có thêm không gian cho pattern.
- Nhược: trận dài, nhịp bị vụn, phase cuối trùng chức năng với escalation của phase 2.
- Bác bỏ: dồn escalation vào phase 2 để giữ nhịp hai hồi rõ ràng.

## Consequences

- Art phải dựng một identity chung với hai silhouette biến đổi được, không phải hai boss riêng.
- Dialogue, telegraph, animation và gameplay phải dùng ID `B01-P1-HYBRID`/`B01-P2-ABYSSAL` thống nhất.
- Intro, transformation beat và aftermath cần cửa chuyển rõ để người chơi không hiểu nhầm là respawn hoặc boss mới.
- Tài liệu cũ dùng `P3` phải được xem là deprecated, không tạo asset hoặc dialogue mới theo ID đó.
