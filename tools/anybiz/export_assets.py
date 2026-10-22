"""Turn the raw AnyBiz Figma exports into the web images of AnyBiz.html.

Raw exports (2x) sit in tools/anybiz/figma/ and stay out of git: the mobile menu
shows her real work email. Export them again from the nodes listed in anybiz.md
to rerun this script.

    python tools/anybiz/export_assets.py
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).parent
RAW = HERE / "figma"
OUT = HERE.parent.parent / "assets" / "work" / "anybiz"
FONT = HERE.parent / "folder-photo" / "fonts" / "it500.ttf"

# name: (raw file, width on the page)
FRAMES = {
    "messaging": ("messaging.png", 1600),
    "setup": ("setup.png", 1600),
    "generating": ("generating.png", 1600),
    "integrations": ("integrations.jpg", 1600),
    "insights": ("insights.png", 1600),
    "mobile": ("mobile.png", 1600),
    "sequence": ("sequence.png", 1280),
    "personas": ("personas.jpg", 1600),
    "performance": ("performance.png", 1600),
    "persona-modal": ("persona-modal.jpg", 1600),
    "posts": ("posts.png", 1600),
    "poster": ("poster.png", 1050),
    "deliverability": ("deliverability.png", 1600),
}


def redact_mobile(im):
    """Her work email under the avatar in the mobile menu becomes an invented one."""
    d = ImageDraw.Draw(im)
    box = (925, 1798, 1110, 1836)
    bg = im.getpixel((box[0] - 6, (box[1] + box[3]) // 2))
    d.rectangle(box, fill=bg)
    d.text((932, 1803), "jamie@northwind.io", font=ImageFont.truetype(str(FONT), 24), fill=(167, 139, 250, 255))
    return im


def clear_corners(im):
    """The presentation frames have rounded corners filled white in the export: make them transparent."""
    if im.getpixel((2, 2))[:3] != (255, 255, 255):
        return im.convert("RGB")
    k = 0
    while im.getpixel((k, k))[:3] == (255, 255, 255):
        k += 1
    r = round(k / 0.293)  # the diagonal of a quarter circle leaves the corner at r(1 - 1/sqrt 2)
    mask = Image.new("L", (im.width * 2, im.height * 2), 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, mask.width - 1, mask.height - 1), radius=r * 2, fill=255)
    out = im.convert("RGBA")
    out.putalpha(mask.resize(im.size, Image.LANCZOS))
    return out


def square_top_corners(im, r=64):
    """The Deliverability frame has rounded top corners in the night colour; in the browser mockup they show as
    notches beside the top bar (her note), so they are filled with the bar's own colour."""
    px = im.load()
    bar = px[r * 2, r // 2]
    for y in range(r):
        for x in list(range(r)) + list(range(im.width - r, im.width)):
            if sum(abs(c - n) for c, n in zip(px[x, y], (2, 6, 23))) < 40:
                px[x, y] = bar
    return im


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for name, (src, w) in FRAMES.items():
        im = clear_corners(Image.open(RAW / src).convert("RGBA"))
        if name == "mobile":
            im = redact_mobile(im)
        h = round(im.height * w / im.width)
        im = im.resize((w, h), Image.LANCZOS)
        im.save(OUT / f"{name}.webp", quality=84, method=6)
        half = im.resize((w // 2, h // 2), Image.LANCZOS)
        half.save(OUT / f"{name}-{w // 2}.webp", quality=84, method=6)
        print(name, w, h)
    # crops for the browser and phone mockups of the Product section: the app frames cut to a 16:10 window,
    # and the two phone screens cut out of the mobile presentation shot (after the email is replaced)
    mobile = redact_mobile(clear_corners(Image.open(RAW / "mobile.png").convert("RGBA"))).convert("RGB")
    crops = {
        "personas-app": (Image.open(RAW / "personas.jpg").convert("RGB"), (0, 0, 2560, 1600), 1600),
        "performance-app": (Image.open(RAW / "perf-app.jpg").convert("RGB"), (0, 0, 2560, 1600), 1600),
        "integrations-app": (Image.open(RAW / "integrations.jpg").convert("RGB"), (0, 128, 2560, 1700), 1920),
        "deliverability-app": (Image.open(RAW / "deliverability.png").convert("RGB"), (0, 0, 2560, 1600), 1600),
        "phone-menu": (mobile, (762, 540, 1500, 1992), 600),
        "phone-settings": (mobile, (1702, 292, 2448, 1912), 600),
    }
    for name, (im, box, w) in crops.items():
        im = im.crop(box)
        if name == "deliverability-app":
            im = square_top_corners(im)
        im = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
        im.save(OUT / f"{name}.webp", quality=86, method=6)
        print(name, im.size)


if __name__ == "__main__":
    main()
