"""Shared by tracker_nofilter.py and tracker_desktop.py: closes the open Templates dropdown baked into her Figma frames."""
from PIL import ImageDraw, Image

# the open Templates dropdown in the Figma frame is closed (her note 2026-11-03): the rows under it are rebuilt
# from the identical rows below (row 4 -> row 3, row 3 -> rows 1 and 2), the two Not checked chips redrawn whole,
# and the table header and the card top under it filled with their own grounds
def close_dropdown(im, f, patch, K, OX=240, OY=1300):
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
