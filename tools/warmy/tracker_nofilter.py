"""Sender tracker with no filters applied (her Figma frame 207:95979, exported at 2x on 2026-11-02 and scaled to 1x
into figma/tracker-desktop-nofilter.png), for the phone view of the Warmy page: the same clean-up as export_assets.py
(made-up workspace name, an invented success manager and user instead of the real colleague and the placeholders),
the sidebar carried down to the bottom. Run: python tracker_nofilter.py -> ../../assets/work/warmy/tracker-nofilter.webp
"""
import os
from PIL import ImageDraw, Image
src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'export_assets.py'), encoding='utf-8').read()
exec(src[:src.index("\nfor n in ('template-desktop'")])  # the helpers only: f, patch, avatar, sidebar_people, workspace, save
im = Image.open(os.path.join(SRC, 'tracker-desktop-nofilter.png')).convert('RGB'); workspace(im); sidebar_people(im)

# the open Templates dropdown in the Figma frame is closed (her note 2026-11-03): the rows under it are rebuilt
# from the identical rows below (row 4 -> row 3, row 3 -> rows 1 and 2), the two Not checked chips redrawn whole,
# and the table header and the card top under it filled with their own grounds
def close_dropdown(im, OX=240, OY=1300):
    X0, X1 = OX+880, OX+1167                       # from the chips to the card's right border (kept)
    row = lambda r: OY+122+72*r                     # rows are 72 px apart, the first starts at 122
    for src_r, dst_r in ((3, 2), (2, 0), (2, 1)):
        im.paste(im.crop((X0, row(src_r), X1, row(src_r)+72)), (X0, row(dst_r)))
    d = ImageDraw.Draw(im)
    d.rectangle((OX+880, OY+83, OX+1166, OY+120), fill=im.getpixel((OX+800, OY+100)))   # header ground
    d.rectangle((OX+880, OY+62, OX+1166, OY+81), fill=im.getpixel((OX+800, OY+72)))     # card top under the select
    for y in (OY+82, OY+121):                                                            # the header's top and bottom rules
        d.line((OX+880, y, OX+1166, y), fill=im.getpixel((OX+800, y)))
    for r in (0, 1):
        y0 = row(r)
        def chip(dd, P, y0=y0):
            ft = f(12, 'SemiBold'); w = dd.textlength('Not checked', font=ft)/K; x1 = OX+971; x0 = x1-w-16
            dd.rounded_rectangle((*P(x0, y0+23), *P(x1, y0+47)), 4*K, fill=(241, 245, 249))
            dd.text(P((x0+x1)/2, y0+35), 'Not checked', font=ft, fill=(30, 41, 59), anchor='mm')
        patch(im, (OX+780, y0+18, OX+990, y0+54), chip)
    b = (OX+1124, OY+33, OX+1143, OY+52); im.paste(im.crop(b).transpose(Image.FLIP_TOP_BOTTOM), b[:2])   # the select's chevron points down again
close_dropdown(im)
H = im.height; side = im.crop((0, 0, 241, 1024)); bg = side.getpixel((120, 800)); line = side.getpixel((240, 800))
foot = side.crop((0, 905, 241, 1024))
ImageDraw.Draw(im).rectangle((0, 905, 239, H), fill=bg); ImageDraw.Draw(im).line((240, 905, 240, H), fill=line)
im.paste(foot, (0, H-119)); save(im, 'tracker-nofilter')

# the sidebar as its own fixed strip for the phone frame's first view (1440 x 1024): the page scrolls, the sidebar stays (her note)
side = Image.new('RGB', (241, 1024)); side.paste(im.crop((0, 0, 241, 905)), (0, 0)); side.paste(im.crop((0, H-119, 241, H)), (0, 905))
save(side, 'tracker-nofilter-side')

# the top bar of the page (Figma "Frame 5", 1200 x 64 right of the sidebar) as its own fixed strip: it stays while the page scrolls (her note 2026-11-03)
save(im.crop((241, 0, 1440, 64)), 'tracker-nofilter-head')
