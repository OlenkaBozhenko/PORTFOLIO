"""The SG "Speed" mark as a standalone RGBA image, for printing on photos and mockups.

Rendered from the vector master sg_svg.py (same construction as render-variants.py V2),
without background and caption. mark(scale, s_col, g_col, trail_col) -> RGBA, cropped to the mark.
"""
import random
from PIL import Image, ImageDraw, ImageFont, ImageChops, ImageFilter
import os
HERE = os.path.dirname(os.path.abspath(__file__))
C = os.path.join(HERE, 'fonts', 'Candal.ttf')
O = os.path.join(HERE, 'fonts', 'OpenSansBI.ttf')
TEAL = (0x41, 0x8b, 0x91); GREEN = (0x15, 0xed, 0xa3); WHITE = (255, 255, 255); INK = (0x0e, 0x2a, 0x2d)

def mark(SC=2, s_col=WHITE, g_col=GREEN, trail_col=None, trail=True):
    """Render the vector mark (sg_svg.py) at about 1300*SC px wide, RGBA, cropped."""
    import io, resvg_py
    from sg_svg import build
    hexc = lambda c: '#%02X%02X%02X' % c
    svg = build(hexc(s_col), hexc(g_col), hexc(trail_col) if trail_col else None, trail)
    png = bytes(resvg_py.svg_to_bytes(svg_string=svg, width=int(1300*SC)))
    im = Image.open(io.BytesIO(png)).convert('RGBA'); return im.crop(im.getbbox())

def words(text, size, col, font=C):
    f = ImageFont.truetype(font, size); b = f.getbbox(text)
    im = Image.new('RGBA', (b[2]+8, b[3]+8), (0, 0, 0, 0)); ImageDraw.Draw(im).text((4-b[0], 4-b[1]), text, font=f, fill=col+(255,))
    return im.crop(im.getbbox())

if __name__ == '__main__':
    mark().save(os.path.join(HERE, 'mark-white-green.png')); print('ok')
