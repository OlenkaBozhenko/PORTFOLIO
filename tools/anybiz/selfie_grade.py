"""Grade her conference photo (Figma 259:79908) a little toward the AnyBiz palette for the My part block.

Shadows lean to the product's night violet, highlights stay clean, colour a touch quieter; her skin keeps
its tone. Writes assets/work/anybiz/olena-sxc.webp (and -480).

    python tools/anybiz/selfie_grade.py
"""
from pathlib import Path
import numpy as np
from PIL import Image

HERE = Path(__file__).parent
OUT = HERE.parent.parent / "assets" / "work" / "anybiz"

im = Image.open(HERE / "figma" / "selfie-export.png").convert("RGB")
a = np.asarray(im).astype(float) / 255
lum = (0.2126 * a[..., 0] + 0.7152 * a[..., 1] + 0.0722 * a[..., 2])[..., None]
grey = np.repeat(lum, 3, axis=2)
a = grey + (a - grey) * 0.9                      # a touch quieter
shadow = np.array([0x2E, 0x1F, 0x5E]) / 255       # the night violet of the product
w = np.clip(1 - lum * 1.6, 0, 1) ** 1.5 * 0.22    # only the darker tones take it
a = a * (1 - w) + shadow * w
cool = np.array([0.985, 0.99, 1.0])               # highlights a hair cooler
a = a * (cool * lum + (1 - lum))
a = np.clip((a - 0.5) * 1.04 + 0.5, 0, 1)         # a little more contrast
out = Image.fromarray((a * 255).round().astype("uint8"))
out.save(OUT / "olena-sxc.webp", quality=88, method=6)
out.resize((480, round(out.height * 480 / out.width)), Image.LANCZOS).save(OUT / "olena-sxc-480.webp", quality=88, method=6)
print(out.size)
