"""Screen fixes for the Sport Guardian page (2026-10-13, her requests):
- placeholder texts in the admin screens get made-up names (Open Sans SemiBold): the statistics title and donor rows
  ("Campaign long long name", "First name Last name......"), the campaign list ("Become a spoooooorts guardian"), the clubs ("Club name");
- the product headers are cut off into their own strips so they stay fixed while the screen scrolls under them:
  campaign page (desktop) header 120 px of 1440, mobile status bar + address bar + menu bar 284 px of 750,
  admin nav 65 px of 1440.
Run after export_assets.py: python fix_screens.py
"""
import os
from PIL import Image, ImageDraw, ImageFont
HERE = os.path.dirname(os.path.abspath(__file__)); F = os.path.join(HERE, 'figma')
OUT = os.path.join(HERE, '..', '..', 'assets', 'work', 'sport-guardian')
SEMI = ImageFont.truetype(os.path.join(HERE, 'fonts', 'OpenSans-SemiBold.ttf'), 16)

def save(im, name, q=86): im.convert('RGB').save(os.path.join(OUT, name+'.webp'), quality=q); print(name, im.size)

def retext(im, items, size, bold=SEMI):
    """items: (box to clear, text, (x, y centre)); the ground colour is sampled just left of the box."""
    d = ImageDraw.Draw(im); f = ImageFont.truetype(os.path.join(HERE, 'fonts', 'OpenSans-SemiBold.ttf'), size)
    for box, text, (x, yc) in items:
        bg = im.getpixel((box[0]-4, (box[1]+box[3])//2)); d.rectangle(box, fill=bg)
        b = d.textbbox((0, 0), text, font=f); d.text((x-b[0], yc-(b[3]-b[1])/2-b[1]), text, font=f, fill=(30, 30, 30))
    return im

ac = retext(Image.open(os.path.join(F, '1x', 'admin-campaigns.png')).convert('RGB'),
            [((288, 350, 520, 404), 'Swimming for everyone', (292, 366)), ((288, 514, 520, 568), 'Junior squad 2024', (292, 530))], 16)
save(ac, 'screen-admin-campaigns')
ab = retext(Image.open(os.path.join(F, '1x', 'admin-business.png')).convert('RGB'),
            [((366, 370, 600, 397), 'Fjordby Svømmeklubb', (369, 383)), ((366, 534, 600, 561), 'Nordlys Fotball', (369, 547)),
             ((366, 698, 600, 725), 'Elvebakken Tennis', (369, 711))], 16)
save(ab, 'screen-admin-business')

from stat_cards import club_logo
from sankey import dashboard_sankey
st = Image.open(os.path.join(F, '1x', 'statistik.png')).convert('RGB'); d = ImageDraw.Draw(st)
for y, name in [(611, 'Ingrid Solberg'), (703, 'Magnus Hansen'), (795, 'Sofie Lie')]:
    d.rectangle((212, y-16, 525, y+16), fill=(255, 255, 255))
    b = d.textbbox((0, 0), name, font=SEMI); d.text((217-b[0], y-(b[3]-b[1])/2-b[1]), name, font=SEMI, fill=(30, 30, 30))
retext(st, [((128, 165, 560, 207), 'Become a sports guardian', (133, 186))], 26)
st = club_logo(dashboard_sankey(st, H_BLOCK=511))  # after the names: the new block pushes the donor list down
save(st, 'screen-statistik')
save(st.crop((0, 0, 1440, 65)), 'screen-statistik-head'); save(st.crop((0, 65, 1440, st.height)), 'screen-statistik-body')

camp = Image.open(os.path.join(F, '2x', 'campaign-page.png')).convert('RGB').resize((1440, 2641), Image.LANCZOS)
save(camp.crop((0, 0, 1440, 120)), 'screen-campaign-head'); save(camp.crop((0, 120, 1440, 2641)), 'screen-campaign-body')
mob = Image.open(os.path.join(F, '2x', 'mobile-main.png')).convert('RGB')
save(mob.crop((0, 0, 750, 284)), 'screen-mobile-head'); save(mob.crop((0, 284, 750, mob.height)), 'screen-mobile-body')
