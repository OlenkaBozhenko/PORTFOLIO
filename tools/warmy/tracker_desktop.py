"""Sender tracker for the desktop stage of the Warmy page (her Figma frame, filtered view), rebuilt on 2026-11-03 at her note:
the open Templates dropdown closed (as in the phone version), and the page top bar saved as its own strip, so it stays
put with the sidebar while the screen scrolls. The same clean-up as export_assets.py. Run: python tracker_desktop.py
"""
import os
from PIL import ImageDraw, Image
HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, 'export_assets.py'), encoding='utf-8').read()
exec(src[:src.index("\nfor n in ('template-desktop'")])  # the helpers only
exec(open(os.path.join(HERE, 'close_dropdown.py'), encoding='utf-8').read())
im = Image.open(os.path.join(SRC, 'tracker-desktop.png')).convert('RGB'); workspace(im); sidebar_people(im)
H = im.height; side = im.crop((0, 0, 241, 1024)); bg = side.getpixel((120, 800)); line = side.getpixel((240, 800))
foot = side.crop((0, 905, 241, 1024))
ImageDraw.Draw(im).rectangle((0, 905, 239, H), fill=bg); ImageDraw.Draw(im).line((240, 905, 240, H), fill=line)
im.paste(foot, (0, H-119))
close_dropdown(im, f, patch, K, OY=1365)   # this frame's Template analysis card sits 65 px lower than in the no-filter one
save(im, 'tracker-desktop')
side = Image.new('RGB', (241, 900)); side.paste(im.crop((0, 0, 241, 781)), (0, 0)); side.paste(im.crop((0, H-119, 241, H)), (0, 781))
save(side, 'tracker-desktop-side')
save(im.crop((241, 0, 1440, 64)), 'tracker-desktop-head')
