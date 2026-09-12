# Thư viện MakeHuman / MPFB

Các file `.zip` ở đây **không được commit** (xem `.gitignore`) vì tổng ~1.3 GB.
Dựng lại môi trường bằng cách chạy lại các lệnh dưới.

## Cài đặt

MPFB đọc asset từ thư mục dữ liệu của add-on:

```
C:\Users\<user>\AppData\Roaming\Blender Foundation\Blender\4.5\extensions\user_default\mpfb\data
```

Mỗi gói giải nén thẳng vào đó (bên trong zip đã có sẵn cấu trúc `clothes/`,
`hair/`, `skins/`, `targets/`).

## Tải lại toàn bộ gói

Dùng mirror `files.` — mirror `files2.` đo được chỉ ~4 KB/s, chậm hơn khoảng
100 lần.

```bash
MPFB="C:/Users/$USER/AppData/Roaming/Blender Foundation/Blender/4.5/extensions/user_default/mpfb/data"
cd assets/libraries/makehuman-mpfb
for p in pants01 shoes01 hair01 skins02 equipment01 hats02; do
  curl -sS -L -o "${p}_cc0.zip" "https://files.makehumancommunity.org/asset_packs/$p/${p}_cc0.zip" &
done
wait
for p in pants01 shoes01 hair01 skins02 equipment01 hats02; do
  unzip -q -o "${p}_cc0.zip" -d "$MPFB"
done
```

## Gói đã tải — dùng gì, bỏ gì

Tất cả đều **CC0**: không cần ghi công, không ràng buộc thương mại.

| Gói | Trạng thái | Ghi chú |
|---|---|---|
| `pants01` | **đang dùng** | `toigo_harem_pants` — quần chùng ống rộng, hợp dáng Á Đông. Nhuộm lại màu chàm đậm. |
| `shoes01` | **đang dùng** | `culturalibre_male_boots` — thay ủng procedural vốn dựng ra khối lù xù. |
| `hair01` | **đang dùng** | `sonntag78_junglebook_hair`. Chọn sau khi render so sánh 6 ứng viên (ảnh test trong scratchpad). `rehmanpolanski_hair_bun_brown` chỉ có búi, đỉnh đầu trọc; `o4saken_long01` là các dải polygon cứng; `culturalibre_hair_02/05` quá ngắn, hở đỉnh. |
| `skins02` | *chưa dùng* | 13 bộ da nam nhưng **không có bộ nào Đông Á** (Slav, Viking, caucasian, African, Eurasian già). Vẫn giữ `young_asian_male` của gói system. |
| `equipment01` | *chưa dùng* | Vũ khí: búa chiến, kiếm thô, dao găm, cung, vuốt, quyền trượng. Không có rìu Việt — Rìu Thần Thạch Sơn vẫn dựng riêng. Có thể dùng cho NPC/quái về sau. |
| `hats02` | *chưa dùng* | Mũ giáp Corinth, Templar, M1, mũ sọ — đều thiên Tây phương/hiện đại, lệch bối cảnh Đông Sơn. |

## Vì sao không lấy từ BlendSwap

BlendSwap **bắt buộc đăng nhập tài khoản** mới tải được (5 file/ngày cho tài
khoản miễn phí). Ngoài ra phần lớn nội dung ở đó là CC-BY hoặc CC-BY-SA;
CC-BY-SA có tính lây lan giấy phép, cần cân nhắc nếu dự án thương mại. Nếu
muốn dùng, bạn tự tải `.blend` về rồi đặt vào `assets/libraries/`, sau đó bảo
tôi nối vào pipeline.

Nguồn: <https://static.makehumancommunity.org/assets/assetpacks.html>
