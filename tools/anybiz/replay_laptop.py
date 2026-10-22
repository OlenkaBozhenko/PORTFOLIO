"""Put the Personas screen on the laptop of the session-replay photo.

The photo is her Figma AI image (node 253:2, gpt-image-2.5; it replaced 252:2, her request): a woman with curly hair at a laptop whose screen is a flat
green. This finds the green screen, maps the Personas screen onto it in perspective, and prints the four
corners (in % of the photo) that AnyBiz.html uses to lay the moving cursor over the same screen.

    python tools/anybiz/replay_laptop.py
"""
from pathlib import Path
import numpy as np
from PIL import Image, ImageFilter

HERE = Path(__file__).parent
OUT = HERE.parent.parent / "assets" / "work" / "anybiz"

photo = Image.open(HERE / "figma" / "laptop.png").convert("RGB")
a = np.asarray(photo).astype(int)
green = (a[..., 1] > 150) & (a[..., 0] < 140) & (a[..., 2] < 140)
ys, xs = np.nonzero(green)
s, d = xs + ys, xs - ys
quad = [(xs[s.argmin()], ys[s.argmin()]), (xs[d.argmax()], ys[d.argmax()]),
        (xs[s.argmax()], ys[s.argmax()]), (xs[d.argmin()], ys[d.argmin()])]  # TL, TR, BR, BL

screen = Image.open(OUT / "personas-app.webp").convert("RGB")
W, H = screen.size


def coeffs(dst, src):
    """The 8 coefficients that map output (photo) points to input (screen) points."""
    m, v = [], []
    for (x, y), (u, w) in zip(dst, src):
        m += [[x, y, 1, 0, 0, 0, -u * x, -u * y], [0, 0, 0, x, y, 1, -w * x, -w * y]]
        v += [u, w]
    return np.linalg.solve(np.array(m, float), np.array(v, float))


c = coeffs(quad, [(0, 0), (W, 0), (W, H), (0, H)])
warped = screen.transform(photo.size, Image.PERSPECTIVE, tuple(c), Image.BICUBIC)
# a touch dimmer than the source, as a lit screen reads in a dusk room
warped = Image.blend(warped, Image.new("RGB", photo.size, (2, 6, 23)), 0.06)
mask = Image.fromarray((green * 255).astype("uint8")).filter(ImageFilter.MaxFilter(5)).filter(ImageFilter.GaussianBlur(0.8))
out = Image.composite(warped, photo, mask)
out.save(OUT / "replay-laptop.webp", quality=86, method=6)
out.resize((photo.width // 2, photo.height // 2), Image.LANCZOS).save(OUT / "replay-laptop-768.webp", quality=86, method=6)
print("size", photo.size)
print("quad %", [(round(x / photo.width * 100, 2), round(y / photo.height * 100, 2)) for x, y in quad])
