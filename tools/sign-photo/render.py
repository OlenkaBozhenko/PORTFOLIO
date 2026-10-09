"""Brand the sign monolith in the Figma AI photo (base.png) for the Styupan "Signage" block.

base.png: generated with Figma AI (gpt-image-2.5), 2026-10-09, a plain purple sign
monolith among ornamental grasses in front of a glass office entrance. Layout after
her Seraj Law reference: name at the top, small lines of text below, more lower down.
This script draws the sign face flat, warps it onto the front face and paints it as a
layer under the grass: each pixel takes print by how purple it is.

Fonts and the mark come from ../folder-photo (fonts/ not committed, see that script).
Run: python render.py  ->  ../../assets/work/styupan/sign-1536.webp + sign-1200.webp
"""
import io
import numpy as np
import resvg_py
from PIL import Image, ImageDraw, ImageFilter, ImageFont

YELLOW = (255, 247, 72)
DEEP = (46, 19, 71)        # #2E1347, the scattered letters, as on the business card
W, H = 600, 1720           # flat sign face
SS = 2

# Front face corners in base.png (TL, TR, BR, BL), measured from the purple mask.
QUAD = [(434, 73), (716, 112), (716, 884), (434, 912)]

# Letter, centre x, centre y, size, rotation (deg), face. Some are cut by the edges.
SCATTER = [
    ("R", 60, 1250, 150, 14, "ct600"), ("A", 210, 1180, 90, -22, "ct600"), ("E", 380, 1230, 120, 35, "ct600"),
    ("S", 545, 1150, 170, 8, "ct700"), ("u", 120, 1420, 130, -30, "ct600"), ("T", 300, 1380, 100, -48, "ct600"),
    ("V", 470, 1420, 190, -12, "ct600"), ("I", 30, 1600, 110, 62, "ct600"), ("Å", 220, 1590, 140, -8, "ct600"),
    ("n", 390, 1610, 110, 40, "ct600"), ("B", 560, 1640, 150, -16, "ct700"), ("s", 300, 1100, 70, 50, "ct600"),
]


def font(name, size):
    return ImageFont.truetype(f"../folder-photo/fonts/{name}.ttf", size * SS)


def spaced(d, xy, text, f, fill, tracking):
    """Draw text with letter-spacing (tracking in flat px)."""
    x, y = xy
    for ch in text:
        d.text((x, y), ch, font=f, fill=fill)
        x += d.textlength(ch, font=f) + tracking * SS


def flat_art():
    art = Image.new("RGBA", (W * SS, H * SS), (0, 0, 0, 0))
    d = ImageDraw.Draw(art)
    m = 52 * SS

    # Scattered letters first, so the text sits over them.
    for ch, x, y, size, rot, face in SCATTER:
        cell = Image.new("RGBA", (size * 2 * SS, size * 2 * SS), (0, 0, 0, 0))
        ImageDraw.Draw(cell).text((size * SS, size * SS), ch, font=font(face, size), fill=DEEP, anchor="mm")
        cell = cell.rotate(rot, resample=Image.BICUBIC)
        art.alpha_composite(cell, (x * SS - cell.width // 2, y * SS - cell.height // 2))

    svg = open("../folder-photo/mark.svg", encoding="utf-8").read()
    mark = Image.open(io.BytesIO(bytes(resvg_py.svg_to_bytes(svg_string=svg, width=120 * SS)))).convert("RGBA")
    art.alpha_composite(mark, (m, 70 * SS))

    d.text((m, 215 * SS), "Stiupan\nTranslations", font=font("ct700", 66), fill=YELLOW, spacing=6 * SS)
    d.rectangle((m, 392 * SS, m + 44 * SS, 395 * SS), fill=YELLOW)
    spaced(d, (m, 420 * SS), "OVERSETTELSESBURÅ", font("it600", 19), YELLOW, 2.2)

    body = font("it500", 21)
    d.text((m, 540 * SS), "Oversettelse\nKorrekturlesing\nLokalisering", font=body, fill=YELLOW, spacing=12 * SS)
    d.text((m, 700 * SS), "Norsk · English · Українська\nРусский · Deutsch · Polski", font=body, fill=YELLOW, spacing=12 * SS)
    d.text((m, 860 * SS), "nortranslations.no", font=font("it600", 21), fill=YELLOW)
    return art


def perspective_coeffs(dst, src):
    """Coefficients for Image.transform: maps output (dst) points back to input (src)."""
    m = []
    for (x, y), (u, v) in zip(dst, src):
        m.append([x, y, 1, 0, 0, 0, -u * x, -u * y])
        m.append([0, 0, 0, x, y, 1, -v * x, -v * y])
    return np.linalg.solve(np.array(m, float), np.array(src, float).reshape(8))


def main():
    src = Image.open("base.png").convert("RGB")
    base = src.resize((src.width * 2, src.height * 2), Image.LANCZOS)
    a = np.asarray(base).astype(np.int32)
    r, g, b = a[..., 0], a[..., 1], a[..., 2]

    quad = [(x * 2, y * 2) for x, y in QUAD]
    face = Image.new("L", base.size, 0)
    ImageDraw.Draw(face).polygon(quad, fill=255)
    face = face.filter(ImageFilter.MinFilter(5))
    # The face is bluer than green (b - g ~ +33); grass and its seed heads are not.
    cover = np.clip((b - g - 4) / 18, 0, 1)
    mask = np.minimum(np.asarray(face).astype(float), cover * 255)
    mask = Image.fromarray(mask.astype("uint8")).filter(ImageFilter.GaussianBlur(0.6))

    art = flat_art()
    flat = [(0, 0), (art.width, 0), (art.width, art.height), (0, art.height)]
    warped = art.transform(base.size, Image.PERSPECTIVE, perspective_coeffs(quad, flat), Image.BICUBIC)

    lum = np.asarray(base.convert("L").filter(ImageFilter.GaussianBlur(3))).astype(float)
    inside = np.asarray(face) > 0
    ref = np.median(lum[inside & (cover > 0.9)])
    shade = np.clip(lum / ref, 0.5, 1.2)[..., None]
    ink = np.asarray(warped).astype(float)
    rgb = np.clip(ink[..., :3] * shade * 0.97, 0, 255)
    alpha = ink[..., 3:] / 255 * (np.asarray(mask).astype(float)[..., None] / 255) * 0.97
    out = a * (1 - alpha) + rgb * alpha
    img = Image.fromarray(out.astype("uint8")).resize(src.size, Image.LANCZOS)

    img.save("sign-branded.png")
    dst = "../../assets/work/styupan/"
    img.save(dst + "sign-1536.webp", quality=92)
    img.resize((1200, 800), Image.LANCZOS).save(dst + "sign-1200.webp", quality=90)


if __name__ == "__main__":
    main()
