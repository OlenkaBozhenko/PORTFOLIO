"""Frames for the phone that plays the donor flow (2026-10-13, her request: show the flow from the
tablet on the mobile view, with the bottom bar and its Donate button). 750 x 1624 each (375 x 812 at 2x).

Sources (her Figma file My-projects-new, 2x exports): view_idrettsfader_doner 3:82411 (the campaign
page with her bottom bar: Our donors, Donate; and the browser toolbar), 3:82469 (the donation form:
Private person / Company, Recurring, the amounts, Back and Donate), the main page 3:82273 (for the
scroll, via fix_screens.py), and the payment cards 3:75350, 3:75437, 3:75581 shown at full phone width
between the status/address bar and the browser toolbar (there are no mobile frames for these steps).
Run: python mobile_frames.py -> ../../assets/work/sport-guardian/m-*.webp
"""
import os
from PIL import Image, ImageDraw, ImageFont
HERE = os.path.dirname(os.path.abspath(__file__)); F = os.path.join(HERE, 'figma', '2x')
OUT = os.path.join(HERE, '..', '..', 'assets', 'work', 'sport-guardian')
TEAL = (65, 139, 145)
BOLD = ImageFont.truetype(os.path.join(HERE, 'fonts', 'OpenSans-Bold.ttf'), 31)

def save(im, name): im.convert('RGB').save(os.path.join(OUT, name+'.webp'), quality=86); print(name, im.size)

page = Image.open(os.path.join(F, 'mobile-82411.png')).convert('RGB')
form = Image.open(os.path.join(F, 'mobile-82469.png')).convert('RGB')
# the bottom bar (Our donors, Donate) and the browser toolbar stay fixed over the scrolling page
save(page.crop((0, 1334, 750, 1624)), 'm-bar')
# the donation form, Recurring already chosen in her frame; then 600 NOK chosen
save(form, 'm-form-1')
f2 = form.copy(); d = ImageDraw.Draw(f2)
d.rectangle((519, 931, 750, 1008), fill=TEAL)
b = d.textbbox((0, 0), '600 NOK', font=BOLD); d.text((640-(b[2]-b[0])/2-b[0], 970-(b[3]-b[1])/2-b[1]), '600 NOK', font=BOLD, fill=(255, 255, 255))
save(f2, 'm-form-2')
# the payment steps: status + address bar on top, the card at full width, the toolbar at the bottom
top = page.crop((0, 0, 750, 186)); tool = page.crop((0, 1458, 750, 1624))
for n, card in [(3, 'card-payment-method'), (4, 'card-credit-card'), (5, 'card-congrats')]:
    c = Image.open(os.path.join(F, card+'.png')).convert('RGB').crop((90, 90, 910, 1394)).resize((750, 1193), Image.LANCZOS)
    im = Image.new('RGB', (750, 1624), (255, 255, 255)); im.paste(top, (0, 0)); im.paste(c, (0, 186)); im.paste(tool, (0, 1458))
    save(im, f'm-step-{n}')
