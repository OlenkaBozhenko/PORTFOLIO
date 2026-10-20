"""The Warmy thumbnail for the landing's work list (her choice, 2026-10-20): her own Figma frame "video-player"
(231:72628, 600 x 398, an image fill exported at 2400 x 1592 into figma/thumb-figma-fill.png, under the frame's 15%
black overlay). The landing's card is 4:3 and the frame 3:2. Trimming the sides cut the logo's margin or the tiger's
face (her note), so the image keeps its full width and the 70 px missing at the top and the bottom are a soft
continuation of its edges: the edge rows, blurred sideways and fading into the dark ground. Nothing else is changed.
Run: python render_thumb.py -> ../../assets/work/warmy/warmy-thumb.webp (1600 x 1200) and warmy-thumb-800.webp
"""
import os
import numpy as np
from PIL import Image, ImageFilter
HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(HERE, '..', '..', 'assets', 'work', 'warmy')
im = Image.open(os.path.join(HERE, 'figma', 'thumb-figma-fill.png')).convert('RGBA')
im = Image.alpha_composite(im, Image.new('RGBA', im.size, (0, 0, 0, 38))).convert('RGB')   # the frame's 15% overlay
im = im.resize((1600, round(im.height*1600/im.width)), Image.LANCZOS)
pad = (1200-im.height)//2; GROUND = np.array([24, 14, 10], float)

def band(row, h, flip):
    """h rows that continue an edge row: blurred sideways, fading towards the dark ground away from the image."""
    strip = row.resize((1600, h)).filter(ImageFilter.GaussianBlur(28))
    a = np.asarray(strip).astype(float)
    t = np.linspace(0, 1, h)[:, None, None]
    if flip: t = t[::-1]                              # t = 0 at the image edge
    a = a*(1-t*.85)+GROUND*(t*.85)
    return Image.fromarray(a.astype('uint8'))

out = Image.new('RGB', (1600, 1200))
out.paste(band(im.crop((0, 0, 1600, 3)), pad, True), (0, 0))
out.paste(band(im.crop((0, im.height-3, 1600, im.height)), 1200-pad-im.height, False), (0, pad+im.height))
out.paste(im, (0, pad))
out.save(os.path.join(OUT, 'warmy-thumb.webp'), quality=86, method=6)
out.resize((800, 600), Image.LANCZOS).save(os.path.join(OUT, 'warmy-thumb-800.webp'), quality=84, method=6)
print('ok', out.size)
