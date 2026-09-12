# CH-06 State and Handoff

## Initial state

CH-06 bắt đầu với toàn bộ tiến trình tích lũy. Không reset biến nào.

```yaml
chapter: CH-06
location: nghia_linh_altar
weapon: WEAPON-DONGSON-THACHSON-AXE
long_ngoc: [LG-01, LG-02, LG-03, LG-04, LG-05]
variables:
  memory_recovered: 0..5      # mang sang từ CH-01..05
  mercy_marks: 0..8
  tribal_trust: 0..6
  dragon_hunger: 0..8
  relics_purified: 0..5
  hidden_released: 0..5       # ADR-004
flags:
  - CH06_STARTED
  - LONG_NHAN_UNNAMED
truth_flags: { }              # 5 TRUTH_* tích lũy
boss_fates: { }               # B-01..B-05 (và HB-01..05 nếu đã gặp)
final_decision: null
```

## Required flags

| Flag | Set at | Meaning |
|---|---|---|
| `CH06_STARTED` | S01 | Chương cuối bắt đầu |
| `CH06_FIVE_MEMORIES_OPEN` | S02 | Đã mở đồng thời năm ký ức Long Ngọc |
| `CH06_TRUTH_SEAL_CONFIRMED` | S02 | Xác nhận "phong ấn chưa từng vỡ" (chỉ ở CH-06) |
| `CH06_HON_MANG_REVEALED` | S03 | Hỗn Mang hiện hình dạng Long Nhân |
| `CH06_ARGUED_*` | S03 | Cách Long Nhân đối đáp Hỗn Mang (`C-CH06-001`) |
| `CH06_UNCOPIED_CHOICE` | B06 | Đã làm hành động Hỗn Mang không sao chép được (`C-CH06-002`) |
| `CH06_FULL_WITNESSES` | FULL | `hidden_released = 5`; năm oan khuất hiện về làm chứng |
| `CH06_FINAL_DECISION_SET` | S05 | `final_decision` đã được chọn (`C-CH06-003`) |
| `CH06_ENDING_E01` | S05 | `E-01 LONG_VUONG` resolve |
| `CH06_ENDING_E02` | S05 | `E-02 TAN_HON_MANG` resolve |
| `CH06_ENDING_E03` | S05 | `E-03 DOAN_TUYET_LONG_MACH` resolve |
| `CH06_ENDING_E04` | S05 | `E-04 HOA_GIAI_BACH_TOC` resolve (chuẩn) |
| `CH06_ENDING_E04_PARTIAL` | S05 | `E-04-PARTIAL` (reconcile thiếu `hidden_released=5`) |
| `CH06_ENDING_E03_BITTER` | S05 | `E-03-BITTER` (reconcile thiếu điều kiện lõi) |
| `CH06_COMPLETE` | END | Game kết thúc |

## State transition matrix

| Event | Variables | Flags | Player-facing feedback |
|---|---|---|---|
| Mở năm ký ức (S02) | none | `CH06_FIVE_MEMORIES_OPEN`, `CH06_TRUTH_SEAL_CONFIRMED` | Năm cột sáng; giọng Hỗn Mang lần đầu lộ ra là "nhiều giọng" |
| Hỗn Mang hiện hình (S03) | none | `CH06_HON_MANG_REVEALED` | Bản sao Long Nhân bước ra từ bóng |
| Đối đáp (`C-CH06-001`) | none | `CH06_ARGUED_*` | Đổi lời thoại mở đầu `B06-P1`, không đổi ending |
| Hành động không sao chép (`C-CH06-002`) | none | `CH06_UNCOPIED_CHOICE` | Bản sao nứt; trận dừng; tế đàn mở |
| Năm oan khuất hiện về (FULL, nếu `hidden_released=5`) | none | `CH06_FULL_WITNESSES` | Năm bóng sáng đứng quanh tế đàn |
| Chọn `restore` | - | `CH06_FINAL_DECISION_SET`, `final_decision=restore` | → `E-01` (hoặc `E-02` nếu `dragon_hunger>=4`) |
| Chọn `absorb` | - | `final_decision=absorb` | → `E-02 TAN_HON_MANG` |
| Chọn `destroy` | - | `final_decision=destroy` | → `E-03 DOAN_TUYET_LONG_MACH` |
| Chọn `reconcile` | - | `final_decision=reconcile` | → `E-04` / `E-04-PARTIAL` / `E-03-BITTER` theo điều kiện |
| Ending card | none | `CH06_ENDING_*`, `CH06_COMPLETE` | Hậu cảnh thế giới theo ending |

## Ending resolution (Resolution Rules, `02 §7`)

Kiểm tra **từ trên xuống**, chọn **đúng một**:

1. `final_decision = reconcile` **và** `memory_recovered=5` **và** `mercy_marks>=4` **và** `tribal_trust>=5` **và** đủ 5 `truth_flags` **và** `hidden_released=5` **và** `absorbed <= 2` ⇒ **`E-04 HOA_GIAI_BACH_TOC`** (kết thúc thật).
2. `final_decision = reconcile` **và** đủ lõi (1) nhưng `hidden_released < 5` ⇒ **`E-04-PARTIAL`** (hòa giải một phần; còn dư oán ẩn; gợi hành trình "tìm lại năm oan khuất").
3. `final_decision = reconcile` **và** thiếu điều kiện lõi (không phải chỉ thiếu `hidden_released`) ⇒ **`E-03-BITTER`** (nghi lễ thất bại; chuyển `destroy` mức bi kịch; cộng đồng chưa kịp thấy sự thật).
4. `final_decision = absorb`, **hoặc** (`final_decision = restore` **và** `dragon_hunger>=4`) ⇒ **`E-02 TAN_HON_MANG`**.
5. `final_decision = destroy` ⇒ **`E-03 DOAN_TUYET_LONG_MACH`**.
6. `final_decision = restore` **và** `dragon_hunger<4` ⇒ **`E-01 LONG_VUONG`** (`relics_purified>=3` → ổn định; `<3` → không ổn định, hook phần tiếp).

> `E-04-PARTIAL` và `E-03-BITTER` là **tag**, không phải ending thứ năm/sáu; chúng là biến thể của `reconcile` khi thiếu điều kiện.

## State invariants

- **Đúng một** ending được resolve; các cờ `CH06_ENDING_*` loại trừ lẫn nhau.
- `final_decision` được set **đúng một lần** (ở `C-CH06-003`), không đổi sau đó.
- CH-06 **không cấp Long Ngọc mới**; `long_ngoc` luôn đủ 5 khi vào S05.
- `hidden_released` **không tăng** ở CH-06 (chỉ đọc); năm oan khuất đã được quyết định ở CH-01..05.
- `CH06_TRUTH_SEAL_CONFIRMED` **chỉ** set ở CH-06 (Canon Lock: reveal "phong ấn chưa vỡ" không confirm trước đó).
- Mọi biến đọc từ tiến trình; **không reset, không wrap**.
- Lạc Long Quân không xuất hiện trực tiếp ở bất kỳ ending nào; chỉ có `ECHO-LAC-LONG-06`.

## Handoff: gameplay

### Required experience

- Đấu tay đôi thuần túy với một boss **sao chép** input người chơi (phase 1) và **đọc lại lựa chọn quá khứ** (phase 2).
- Một khoảnh khắc "làm điều chưa từng làm" (`C-CH06-002`) để phá thế sao chép - phải đọc được bằng fiction, không bằng QTE chữ.
- `Chân Long` là trạng thái bùng nổ ngắn (cường hóa tầm xa, miễn nhiễm nguyên tố tạm thời), **không** thay thế quyết định cuối.
- Bốn nút quyết định cuối (`C-CH06-003`) phải **hiển thị đủ thông tin** để người chơi hiểu mình đang đánh đổi gì (không giấu điều kiện ending, `02 §8`).
- Ending card khác nhau rõ ràng về hình ảnh/tông theo `final_decision` + điều kiện.

### Explicitly deferred

- Damage/health/stamina/frame data, hitbox.
- Cách boss "đọc" input người chơi ở tầng kỹ thuật (behavior tree, replay buffer) - chỉ ghi hook trải nghiệm.
- Save serialization của `final_decision` và các ending flag.

## Handoff: art

- Hỗn Mang là **bản sao méo của Long Nhân**: silhouette giống hệt, nhưng bóng đi trước thân, khớp đảo nhẹ, mắt trống, vảy rồng sáng như nứt. Không sừng rồng cung đình, không quỷ vương sáo rỗng.
- Phase 2 chồng **dư ảnh năm boss** tùy `boss_fates`; dư ảnh của boss đã tha thì sáng/bình an, đã absorb thì đen/dữ.
- Tế đàn Nghĩa Lĩnh: đá, năm bệ ngọc, Đông Sơn tiết chế; không "thiên đình" Trung Hoa.
- **Bốn ending card**, mỗi cái một hình ảnh chủ đạo:
  - `E-01`: ngai/bệ ngọc sáng lạnh, Long Nhân đứng một mình canh giữ.
  - `E-02`: Long Nhân hóa rồng tối, trật tự đẹp mà lạnh, bóng Hỗn Mang trong mắt.
  - `E-03`: năm mảnh ngọc vỡ, ánh sáng phép tắt dần, thế giới phàm trần.
  - `E-04`: tế đàn thành nơi hòa giải, trăm cộng đồng, năm oan khuất sáng, ngọc thành vật chứng.
  - `E-04-PARTIAL`: như E-04 nhưng thiếu năm bóng oan khuất, còn một khoảng tối.
  - `E-03-BITTER`: ngọc vỡ nhưng cộng đồng quay lưng, chưa thấy sự thật.

## Handoff: audio

- Hỗn Mang nói bằng **giọng chính Long Nhân** chồng nhiều giọng (oán nghiệp); khi bị "un-copied", lớp chồng **rơi rụng** chỉ còn một giọng đơn độc.
- Nhạc trận cuối: chủ đề của năm chương **chồng lấn**, rồi tách ra khi người chơi phá thế sao chép.
- Mỗi ending một tông nhạc: E-01 trang nghiêm-lạnh, E-02 hùng ca-méo, E-03 lặng-giải thoát, E-04 ấm-viễn mãn; E-04-PARTIAL ấm nhưng khuyết; E-03-BITTER đứt gãy.
- Không "evil sting" khi Hỗn Mang xuất hiện; nó là bi kịch, không phải ác quỷ.

## Handoff: localization

- Giữ glossary: `Long Nhân`, `Long Ngọc`, `Hỗn Mang`, `Long Khí`, `Chân Long`, `Rìu Thần Thạch Sơn`, `Nghĩa Lĩnh`, `final_decision` keys (`restore/absorb/destroy/reconcile`).
- Bốn ending phải dịch sao cho **không** ending nào nghe "đúng tuyệt đối"; giữ trọng lượng đạo đức ngang nhau.
- Giọng Hỗn Mang (nhiều giọng chồng) cần hướng dẫn voice riêng; không dịch thành một phản diện độc ác đơn giọng.
- Dòng reveal "phong ấn chưa từng vỡ" là **câu chốt toàn game** - cần subtitle budget cinematic.

## Handoff: cinematic

- Ending card là **cinematic**, không phải menu: mỗi ending một đoạn ngắn (hình ảnh chủ đạo + một dòng + hậu cảnh thế giới).
- `E-04` (và `E-04-PARTIAL`) có thêm lớp "chứng nhân" (năm oan khuất) nếu `CH06_FULL_WITNESSES`.
- Không ending nào chiếu Lạc Long Quân hiện hình giải quyết; chỉ ánh sáng/tiếng vọng biểu tượng.
