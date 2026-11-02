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
H = im.height; side = im.crop((0, 0, 241, 1024)); bg = side.getpixel((120, 800)); line = side.getpixel((240, 800))
foot = side.crop((0, 905, 241, 1024))
ImageDraw.Draw(im).rectangle((0, 905, 239, H), fill=bg); ImageDraw.Draw(im).line((240, 905, 240, H), fill=line)
im.paste(foot, (0, H-119)); save(im, 'tracker-nofilter')

# the sidebar as its own fixed strip for the phone frame's first view (1440 x 1024): the page scrolls, the sidebar stays (her note)
side = Image.new('RGB', (241, 1024)); side.paste(im.crop((0, 0, 241, 905)), (0, 0)); side.paste(im.crop((0, H-119, 241, H)), (0, 905))
save(side, 'tracker-nofilter-side')
