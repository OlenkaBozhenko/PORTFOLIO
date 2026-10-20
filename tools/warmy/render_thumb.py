"""The Warmy thumbnail for the landing's work list (her choice, 2026-10-20): her own Figma frame "video-player"
(231:72628, 600 x 398, an image fill exported at 2400 x 1592 into figma/thumb-figma-fill.png, under the frame's 15%
black overlay). The landing's card is 4:3 and the frame 3:2, so the image is fitted to a width of 1700, 50 px are
trimmed at each side (the logo keeps its margin), and the missing 36 px at the top and the bottom are filled by
stretching the edge rows, softened; nothing else is changed.
Run: python render_thumb.py -> ../../assets/work/warmy/warmy-thumb.webp (1600 x 1200) and warmy-thumb-800.webp
"""
import os
from PIL import Image, ImageFilter
HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(HERE, '..', '..', 'assets', 'work', 'warmy')
im = Image.open(os.path.join(HERE, 'figma', 'thumb-figma-fill.png')).convert('RGBA')
im = Image.alpha_composite(im, Image.new('RGBA', im.size, (0, 0, 0, 38))).convert('RGB')   # the frame's 15% overlay
im = im.resize((1700, round(im.height*1700/im.width)), Image.LANCZOS).crop((50, 0, 1650, 1128))
pad = (1200-im.height)//2
out = Image.new('RGB', (1600, 1200))
top = im.crop((0, 0, 1600, 2)).resize((1600, pad+8)).filter(ImageFilter.GaussianBlur(6))
bot = im.crop((0, im.height-2, 1600, im.height)).resize((1600, 1200-pad-im.height+8)).filter(ImageFilter.GaussianBlur(6))
out.paste(top, (0, 0)); out.paste(bot, (0, pad+im.height-8)); out.paste(im, (0, pad))
out.save(os.path.join(OUT, 'warmy-thumb.webp'), quality=86, method=6)
out.resize((800, 600), Image.LANCZOS).save(os.path.join(OUT, 'warmy-thumb-800.webp'), quality=84, method=6)
print('ok', out.size)
