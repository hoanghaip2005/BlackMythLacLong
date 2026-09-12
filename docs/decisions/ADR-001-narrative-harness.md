# ADR-001: Dùng bộ harness tài liệu làm nguồn chuẩn cho kịch bản

## Status

Accepted

## Date

2026-09-11

## Context

Huyết Mạch Lạc Long bắt đầu từ một sườn truyện lớn, có sáu chương, nhiều boss, nhiều biến số và nhiều kết thúc. Assets, models và gameplay chưa được phát triển. Nếu viết trực tiếp theo từng cảnh riêng lẻ, dự án dễ gặp các lỗi:

- Mâu thuẫn giữa canon, ký ức và sự thật cuối game.
- Nhánh lựa chọn chỉ đổi thoại nhưng không đổi trạng thái thế giới.
- AI sinh nội dung lệch giọng, sai tên riêng hoặc quên điều kiện mở khóa.
- Narrative phụ thuộc sớm vào implementation chưa tồn tại.

## Decision

Dùng `docs/harness/` làm nguồn chuẩn duy nhất cho narrative pre-production. Harness gồm:

- Story Bible: canon, luật thế giới, nhân vật, phe phái và thuật ngữ.
- Branching Harness: biến số, lựa chọn, điều kiện và thứ tự ưu tiên kết thúc.
- Chapter Harness: mục tiêu, beat, boss, reveal và hậu quả cho từng chương.
- Content Templates: cấu trúc chuẩn cho scene, quest, dialogue và boss.
- AI Writing Harness: context pack, prompt, output contract và self-check.
- Production Harness: ID, trạng thái, dependency, review và bàn giao.
- Validation: kiểm tra canon, nhánh, continuity, văn hóa, pacing và khả năng triển khai.

## Alternatives Considered

### Viết tự do trong một tài liệu duy nhất

- Ưu: khởi đầu nhanh.
- Nhược: khó truy vết điều kiện nhánh, khó tái sử dụng cho AI và đội sản xuất.
- Bác bỏ: không phù hợp với game nhiều chương, nhiều trạng thái.

### Xây data schema/gameplay trước

- Ưu: sớm có cấu trúc kỹ thuật.
- Nhược: khóa quyết định khi narrative chưa ổn định; gây phụ thuộc giả vào hệ thống chưa tồn tại.
- Bác bỏ: dự án đang ở narrative pre-production.

### Dùng wiki không có ID và validation

- Ưu: dễ viết.
- Nhược: không có kiểm tra tham chiếu, version hoặc tính đầy đủ.
- Bác bỏ: không đủ an toàn cho AI và production handoff.

## Consequences

- Biên kịch có một nguồn chuẩn để phát triển thêm từ sườn gốc.
- AI có context pack giới hạn, giảm việc tự bịa canon.
- Đội gameplay/art/audio nhận được hook và dependency rõ ràng nhưng không bị ép implementation sớm.
- Visual character harness giữ identity, provenance và cultural constraints khi thay asset.
- Mọi thay đổi lớn phải cập nhật nhiều lớp tài liệu và chạy validation checklist.
- YAML hiện là template trao đổi, chưa phải runtime schema.
