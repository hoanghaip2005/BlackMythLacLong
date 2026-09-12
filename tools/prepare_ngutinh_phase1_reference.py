"""Extract the front humanoid phase-1 silhouette from the supplied concept sheet."""

from pathlib import Path

import cv2
import numpy as np
from PIL import Image


SOURCE = Path(r"C:\Users\HOANG_~1\AppData\Local\Temp\codex-clipboard-1434f643-2c84-4793-abfd-3baf556f605d.png")
OUTPUT = Path("assets/bosses/chapter_01_ngutinh/phase_1_hybrid/generated/ngu_tinh_phase1_reference_cutout.png")


def main() -> None:
    image = cv2.imread(str(SOURCE), cv2.IMREAD_COLOR)
    if image is None:
        raise FileNotFoundError(SOURCE)

    # The large front view occupies the left-center of the sheet.
    x, y, width, height = 55, 12, 535, 760
    crop = image[y : y + height, x : x + width]
    mask = np.zeros(crop.shape[:2], np.uint8)
    rect = (18, 8, width - 36, height - 18)
    bgd = np.zeros((1, 65), np.float64)
    fgd = np.zeros((1, 65), np.float64)
    cv2.grabCut(crop, mask, rect, bgd, fgd, 8, cv2.GC_INIT_WITH_RECT)
    alpha = np.where((mask == cv2.GC_FGD) | (mask == cv2.GC_PR_FGD), 255, 0).astype(np.uint8)

    # Keep a soft edge while removing isolated background islands.
    alpha = cv2.morphologyEx(alpha, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
    # Remove the concept-sheet typography and the adjacent rear-view figure.
    alpha[:, :62] = 0
    alpha[:, 505:] = 0
    alpha[735:, :] = 0
    alpha = cv2.GaussianBlur(alpha, (5, 5), 0)
    rgba = cv2.cvtColor(crop, cv2.COLOR_BGR2RGBA)
    rgba[:, :, 3] = alpha
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    Image.fromarray(rgba).save(OUTPUT)
    print(OUTPUT)


if __name__ == "__main__":
    main()
