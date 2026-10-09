"""Brand the folder in the Figma AI photo (base.png) for the Styupan "In use" block.

base.png: generated with Figma AI (gpt-image-2.5), 2026-10-08, a plain purple
string-and-button envelope folder, hugged to the chest with the arm around it. This script draws the folder face flat, after
her Kraft Folder reference (Behance, Uneri Space), warps it onto the folder and
paints it only where the folder paper shows, so her hand, the buttons and the
string stay in front.

Fonts: Crimson Text and Inter Tight TTFs from Google Fonts in fonts/ (not committed).
Run: python render.py  ->  ../../assets/work/styupan/folder-1536.webp + folder-1200.webp
"""
import io
import numpy as np
import resvg_py
from PIL import Image, ImageDraw, ImageFilter, ImageFont

YELLOW = (255, 247, 72)
W, H = 1000, 1375          # flat folder face; the flap ends near y = 205
SS = 2                     # supersampling for the flat art

# Folder corners in base.png (TL, TR, BR, BL), measured from the purple mask.
QUAD = [(481, 462), (814, 397), (889, 866), (541, 935)]


# Letter, centre x, centre y, size, rotation (deg), face. Some are cut by the edges.
SCATTER = [
    ("R", 40, 1210, 130, 14, "ct600"), ("A", 165, 1250, 80, -22, "ct600"), ("E", 280, 1205, 100, 35, "ct600"),
    ("T", 395, 1260, 75, -48, "ct600"), ("S", 520, 1215, 120, 8, "ct700"), ("u", 105, 1335, 105, -30, "ct600"),
    ("I", 240, 1320, 90, 62, "ct600"), ("V", 360, 1345, 140, -12, "ct600"), ("n", 480, 1330, 80, 40, "ct600"),
    ("Å", 10, 1320, 95, -8, "ct600"), ("E", 600, 1350, 95, 24, "ct600"), ("B", 190, 1400, 110, -16, "ct700"),
    ("s", 650, 1240, 70, 50, "ct600"), ("R", 300, 1150, 60, -35, "ct600"), ("O", 60, 1110, 70, 20, "ct600"),
]


def font(name, size):
    return ImageFont.truetype(f"fonts/{name}.ttf", size * SS)


def flat_art():
    art = Image.new("RGBA", (W * SS, H * SS), (0, 0, 0, 0))
    d = ImageDraw.Draw(art)

    # Huge vertical wordmark, read bottom to top, along the right edge.
    big = font("ct700", 330)
    word = "Stiupan"
    bw = d.textlength(word, font=big)
    x0, y0, x1, y1 = d.textbbox((0, 0), word, font=big)
    strip = Image.new("RGBA", (x1 - x0, y1 - y0), (0, 0, 0, 0))
    ImageDraw.Draw(strip).text((-x0, -y0), word, font=big, fill=YELLOW)
    strip = strip.rotate(90, expand=True)
    # Whole word on the folder, its foot (the descender of p) a margin in from the right edge.
    art.alpha_composite(strip, (W * SS - strip.width - 8 * SS, H * SS - strip.height - 40 * SS))

    # The mark and the descriptor on the flap.
    png = resvg_py.svg_to_bytes(svg_string=open("mark.svg", encoding="utf-8").read(), width=104 * SS)
    mark = Image.open(io.BytesIO(bytes(png))).convert("RGBA")
    art.alpha_composite(mark, (70 * SS, 62 * SS))
    d.text((70 * SS, 150 * SS), "OVERSETTELSESBURÅ", font=font("it600", 19), fill=YELLOW, spacing=0)

    # Headline and the languages, left, above where her hand sits.
    head = font("ct600", 64)
    d.text((70 * SS, 300 * SS), "Stiupan\nTranslations.", font=head, fill=YELLOW, spacing=4 * SS)
    small = font("it500", 19)
    d.text((72 * SS, 480 * SS), "NORSK · ENGLISH · УКРАЇНСЬКА\nРУССКИЙ · DEUTSCH · POLSKI", font=small, fill=YELLOW, spacing=10 * SS)
    d.text((72 * SS, 570 * SS), "nortranslations.no", font=font("it600", 20), fill=YELLOW)

    # Scattered letters in the bottom left corner, paper at low opacity (as on the billboard).
    ghost = (245, 245, 245, 78)
    for ch, x, y, size, rot, face in SCATTER:
        f = font(face, size)
        cell = Image.new("RGBA", (size * 2 * SS, size * 2 * SS), (0, 0, 0, 0))
        ImageDraw.Draw(cell).text((size * SS, size * SS), ch, font=f, fill=ghost, anchor="mm")
        cell = cell.rotate(rot, resample=Image.BICUBIC)
        art.alpha_composite(cell, (x * SS - cell.width // 2, y * SS - cell.height // 2))
    return art  # kept at SS x the flat size; the warp scales it


def perspective_coeffs(dst, src):
    """Coefficients for Image.transform: maps output (dst) points back to input (src)."""
    m = []
    for (x, y), (u, v) in zip(dst, src):
        m.append([x, y, 1, 0, 0, 0, -u * x, -u * y])
        m.append([0, 0, 0, x, y, 1, -v * x, -v * y])
    return np.linalg.solve(np.array(m, float), np.array(src, float).reshape(8))


def main():
    # Work at twice the photo size, then scale down: smooth edges where her hand covers the print.
    src = Image.open("base.png").convert("RGB")
    base = src.resize((src.width * 2, src.height * 2), Image.LANCZOS)
    a = np.asarray(base).astype(np.int32)
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    paper = (b > r - 15) & (r > g + 15) & (b > g + 15) & (r < 140) & (g < 70)
    # Print covers the whole folder face, shadows included, and stops only at what lies on top:
    # her hand (skin) and the yellow buttons and string. Like a layer under the hand, not around it.
    quad = [(x * 2, y * 2) for x, y in QUAD]
    face = Image.new("L", base.size, 0)
    ImageDraw.Draw(face).polygon(quad, fill=255)
    face = face.filter(ImageFilter.MinFilter(5))
    # How much of each pixel is folder: the purple paper is bluer than green (b - g ~ +29),
    # her skin and sleeve are warmer (b - g < -15), the shirt is bright. Edge pixels that mix
    # skin and folder get partial print, so the hand covers the letters with no gap and no fringe.
    lum = (r + g + b) / 3
    cover = np.clip((b - g + 4) / 26, 0, 1) * np.clip((175 - lum) / 25, 0, 1)
    skin = Image.fromarray((((r - b > 22) & (r > g) & (b - g < 4)) * 255).astype("uint8"))
    skin = skin.filter(ImageFilter.MedianFilter(3)).filter(ImageFilter.MaxFilter(3))
    cover[np.asarray(skin) > 0] = 0
    button = (r > 150) & (g > 130) & (b < 140)
    cover[np.asarray(Image.fromarray((button * 255).astype("uint8")).filter(ImageFilter.MaxFilter(5))) > 0] = 0
    mask = np.minimum(np.asarray(face).astype(float), cover * 255)
    mask = Image.fromarray(mask.astype("uint8")).filter(ImageFilter.GaussianBlur(0.6))

    art = flat_art()
    flat = [(0, 0), (art.width, 0), (art.width, art.height), (0, art.height)]
    warped = art.transform(base.size, Image.PERSPECTIVE, perspective_coeffs(quad, flat), Image.BICUBIC)

    # Print takes the light of the paper: scale the ink by local brightness.
    lum = np.asarray(base.convert("L").filter(ImageFilter.GaussianBlur(3))).astype(float)
    ref = np.median(lum[paper])
    shade = np.clip(lum / ref, 0.5, 1.15)[..., None]
    ink = np.asarray(warped).astype(float)
    rgb = np.clip(ink[..., :3] * shade * 0.97, 0, 255)
    alpha = ink[..., 3:] / 255 * (np.asarray(mask).astype(float)[..., None] / 255) * 0.96
    out = a * (1 - alpha) + rgb * alpha
    img = Image.fromarray(out.astype("uint8")).resize(src.size, Image.LANCZOS)

    img.save("folder-branded.png")
    dst = "../../assets/work/styupan/"
    img.save(dst + "folder-1536.webp", quality=92)
    img.resize((1200, 800), Image.LANCZOS).save(dst + "folder-1200.webp", quality=90)


if __name__ == "__main__":
    main()
