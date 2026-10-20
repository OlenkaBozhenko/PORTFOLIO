"""Warmy screens for the case page (2026-10-20): her Figma frames (My-projects-new, section 207:93444, exported
1x into figma/) with the design-file placeholders replaced by made-up ones and her success manager's name and
photo replaced by an invented person, so no real colleague is shown on a public page:
  "{Workspace}" -> "Northwind Mail", "{Name}" -> "Jamie Cole", "Alina Shpak" (photo) -> "Mia Larsen" (initials).
The tall Sender tracker frame gets its sidebar drawn down to the bottom (the frame stops the sidebar at 1024 px).
Run: python export_assets.py -> ../../assets/work/warmy/*.webp
"""
import os
from PIL import Image, ImageDraw, ImageFont
HERE = os.path.dirname(os.path.abspath(__file__)); SRC = os.path.join(HERE, 'figma')
OUT = os.path.join(HERE, '..', '..', 'assets', 'work', 'warmy'); os.makedirs(OUT, exist_ok=True)
FONT = os.path.join(HERE, 'fonts', 'Figtree.ttf')
INK, MUT = (51, 65, 85), (100, 116, 139)
K = 3  # patches are drawn at 3x and scaled down, so the new text is as smooth as the exported one


def f(size, w='Medium'):
    ft = ImageFont.truetype(FONT, round(size*K)); ft.set_variation_by_name(w); return ft


def patch(im, box, draw):
    """Paint box with the colour under its right edge, then draw(d, ox, oy) at K x and paste it back."""
    x0, y0, x1, y1 = box; bg = im.getpixel((x1-1, (y0+y1)//2))
    p = Image.new('RGB', ((x1-x0)*K, (y1-y0)*K), bg); d = ImageDraw.Draw(p)
    draw(d, lambda x, y: ((x-x0)*K, (y-y0)*K))
    im.paste(p.resize((x1-x0, y1-y0), Image.LANCZOS), (x0, y0))


def avatar(d, P, x, y, s, fill, ink, letters, size):
    d.rounded_rectangle((*P(x, y), *P(x+s, y+s)), 6*K, fill=fill)
    d.text(P(x+s/2, y+s/2), letters, font=f(size, 'SemiBold'), fill=ink, anchor='mm')


def sidebar_people(im, top=905):
    """The bottom of the sidebar: success manager and the signed-in user, made up."""
    def sm(d, P):
        avatar(d, P, 16, top+20, 28, (255, 237, 213), (194, 65, 12), 'ML', 10.5)
        d.text(P(51, top+33), 'Your Success Manager', font=f(12.25, 'Regular'), fill=MUT, anchor='ls')
        d.text(P(51, top+48), 'Mia Larsen', font=f(14), fill=INK, anchor='ls')
    patch(im, (12, top+13, 200, top+62), sm)
    def me(d, P):
        avatar(d, P, 16, top+77, 28, (148, 163, 184), (255, 255, 255), 'J', 14)
        d.text(P(51, top+96), 'Jamie Cole', font=f(14), fill=INK, anchor='ls')
    patch(im, (12, top+72, 190, top+110), me)


def workspace(im):
    patch(im, (46, 14, 172, 44), lambda d, P: d.text(P(49, 34), 'Northwind Mail', font=f(14), fill=INK, anchor='ls'))


def save(im, name, q=86):
    im.save(os.path.join(OUT, name+'.webp'), quality=q, method=6); print(name, im.size)


for n in ('template-desktop', 'spintax-desktop', 'adeline-desktop', 'adeline-thinking'):
    im = Image.open(os.path.join(SRC, n+'.png')).convert('RGB'); workspace(im); sidebar_people(im); save(im, n)

# the tall Sender tracker: carry the sidebar to the bottom and move its people block down with it
im = Image.open(os.path.join(SRC, 'tracker-desktop.png')).convert('RGB'); workspace(im); sidebar_people(im)
H = im.height; side = im.crop((0, 0, 241, 1024)); bg = side.getpixel((120, 800)); line = side.getpixel((240, 800))
foot = side.crop((0, 905, 241, 1024))
ImageDraw.Draw(im).rectangle((0, 905, 239, H), fill=bg); ImageDraw.Draw(im).line((240, 905, 240, H), fill=line)
im.paste(foot, (0, H-119)); save(im, 'tracker-desktop')

for n in ('tracker-mobile', 'template-mobile', 'adeline-mobile', 'chat-mobile', 'stripe'):
    save(Image.open(os.path.join(SRC, n+'.png')).convert('RGB'), n)
for n in ('post-1', 'post-2', 'post-roi', 'post-4', 'poster'):
    im = Image.open(os.path.join(SRC, n+'.png')).convert('RGB')
    if im.width > 1080: im = im.resize((1080, round(im.height*1080/im.width)), Image.LANCZOS)
    save(im, n, 82)
