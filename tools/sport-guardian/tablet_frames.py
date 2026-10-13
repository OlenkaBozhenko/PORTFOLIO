"""Frames for the tablet on the Sport Guardian first screen: the donor flow, 1440 x 900 each.

Sources (her Figma file My-projects-new, YlGWlsWWjKSCxhONMzGG2F, exported 2026-10-13):
  figma/2x/campaign-page.png   view_idrettsfader_doner 3:72548 at 2x
  figma/1x/modal-payment-method.png  view_idrettsfader_doner 3:71652 (page header behind the card)
  figma/2x/card-*.png          card_payment method 3:75350, card_pay by credit card 3:75437,
                               card_ congratulations 3:75581, at 2x
The selected states of the widget (Recurring, 600 NOK) are redrawn in Open Sans over the export.
Run: python tablet_frames.py -> ../../assets/work/sport-guardian/flow-1..6.webp
(flow-1..3: the page body, 1440 x 2521; flow-4..6: the payment cards over the page, 1440 x 900)
"""
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter
HERE = os.path.dirname(os.path.abspath(__file__)); F = os.path.join(HERE, 'figma')
OUT = os.path.join(HERE, '..', '..', 'assets', 'work', 'sport-guardian'); os.makedirs(OUT, exist_ok=True)
TEAL = (65, 139, 145); LINE = (218, 222, 221)
REG = os.path.join(HERE, 'fonts', 'OpenSans-Regular.ttf'); BOLD = os.path.join(HERE, 'fonts', 'OpenSans-Bold.ttf')

def text_c(d, box, s, font, fill):
    b = d.textbbox((0, 0), s, font=font); x = (box[0]+box[2]-(b[2]-b[0]))/2-b[0]; y = (box[1]+box[3]-(b[3]-b[1]))/2-b[1]
    d.text((x, y), s, font=font, fill=fill)

def chip(d, box, s, on, font, r=6, corners=None):
    d.rounded_rectangle(box, r, fill=TEAL if on else (255, 255, 255), outline=TEAL if on else LINE, width=2, corners=corners)
    text_c(d, box, s, font, (255, 255, 255) if on else (18, 18, 18))

def save(im, n): im.convert('RGB').save(os.path.join(OUT, f'flow-{n}.webp'), quality=88)

# the campaign page frames are the whole page (1440 x 2521 under the fixed 120 px header, screen-campaign-head.webp),
# so the page can scroll before the taps
page = Image.open(os.path.join(F, '2x', 'campaign-page.png')).convert('RGB')
body = lambda im: im.resize((1440, 2641), Image.LANCZOS).crop((0, 120, 1440, 2641))
save(body(page), 1)
f = ImageFont.truetype(REG, 30); fb = ImageFont.truetype(BOLD, 31)
p2 = page.copy(); d = ImageDraw.Draw(p2)
chip(d, (1729, 826, 2091, 905), 'One-time fee', False, f, corners=(True, False, False, True))
chip(d, (2091, 826, 2453, 905), 'Recurring', True, f, corners=(False, True, True, False))
save(body(p2), 2)
p3 = p2.copy(); d = ImageDraw.Draw(p3)
chip(d, (2213, 990, 2453, 1069), '600 NOK', True, fb, corners=(False, True, True, False))
save(body(p3), 3)

base = Image.open(os.path.join(F, '1x', 'modal-payment-method.png')).convert('RGB')
ImageDraw.Draw(base).rectangle((470, 125, 970, 870), fill=(255, 255, 255))
for n, card in [(4, 'card-payment-method'), (5, 'card-credit-card'), (6, 'card-congrats')]:
    # the export has a 90 px black margin (the shadow area): keep the card itself, 820 x 1304 at 2x
    c = Image.open(os.path.join(F, '2x', card+'.png')).convert('RGB').crop((90, 90, 910, 1394)).resize((410, 652), Image.LANCZOS)
    sh = Image.new('L', base.size, 0); ImageDraw.Draw(sh).rounded_rectangle((515, 172, 925, 824), 8, fill=60)
    sh = sh.filter(ImageFilter.GaussianBlur(18))
    im = Image.composite(Image.new('RGB', base.size, (40, 70, 72)), base, sh); im.paste(c, (515, 160)); save(im, n)
print('ok')
