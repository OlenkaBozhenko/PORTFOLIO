"""Frames for the phone that plays the donor flow (2026-10-13, her request: show the flow from the
tablet on the mobile view, with the bottom bar and its Donate button). 750 x 1624 each (375 x 812 at 2x).

Sources (her Figma file My-projects-new, 2x exports): view_idrettsfader_doner 3:82411 (the campaign
page with her bottom bar: Our donors, Donate; and the browser toolbar), 3:82469 (the donation form:
Private person / Company, Recurring, the amounts, Back and Donate), the main page 3:82273 (for the
scroll, via fix_screens.py), the payment cards 3:75350, 3:75437, 3:75581 and the Vipps card 3:75438 shown at full phone width
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
# the donation form, redrawn with 16 pt side margins (2026-10-13, her request): in her frame 3:82469 the content
# is 362 pt wide from x 18, so it runs past the right edge, and Figma clips every export of it. Same layout, type
# (Open Sans), sizes and colours as her frame, drawn 343 pt wide from x 16 (686 px at 2x from x 32).
FT = lambda w, n: ImageFont.truetype(os.path.join(HERE, 'fonts', f'OpenSans-{w}.ttf'), n)
INK, LINE, MUTE, FIELD = (28, 28, 26), (227, 232, 229), (154, 161, 162), (251, 252, 251)
def ctext(d, box, t, f, fill):
    b = d.textbbox((0, 0), t, font=f); d.text(((box[0]+box[2]-(b[2]-b[0]))/2-b[0], (box[1]+box[3]-(b[3]-b[1]))/2-b[1]), t, font=f, fill=fill)
def pair(d, y, left, right, sel):
    for k, t in enumerate((left, right)):
        x0 = 32+k*343; box = (x0, y, x0+343, y+80); on = k == sel
        d.rounded_rectangle(box, 8, fill=TEAL if on else (255, 255, 255), outline=TEAL if on else LINE, width=2, corners=(k == 0, k == 1, k == 1, k == 0))
        ctext(d, box, t, FT('Regular', 30), (255, 255, 255) if on else INK)
def form_frame(freq=None, sel600=False, amount=False):
    """freq: None (placeholder), 'open' (the list is open) or the chosen frequency; amount: 600 typed in the field."""
    im = form.copy(); d = ImageDraw.Draw(im); d.rectangle((0, 284, 750, 1338), fill=(255, 255, 255))
    d.rounded_rectangle((32, 300, 718, 436), 16, fill=TEAL)
    d.text((64, 314), '2200 NOK', font=FT('Bold', 46), fill=(255, 255, 255)); d.text((64, 378), '200 donors', font=FT('Regular', 30), fill=(255, 255, 255))
    pair(d, 498, 'Private person', 'Company', 0)
    pair(d, 594, 'One-time fee', 'Recurring', 1)
    d.rounded_rectangle((32, 690, 718, 770), 8, fill=(255, 255, 255), outline=TEAL if freq == 'open' else LINE, width=2)
    d.text((64, 712), freq if freq not in (None, 'open') else 'Select donation frequency', font=FT('SemiBold', 30), fill=INK)
    chev = [(668, 736), (682, 722), (696, 736)] if freq == 'open' else [(668, 722), (682, 736), (696, 722)]
    d.line(chev, fill=(120, 126, 128), width=3)
    f = FT('Regular', 24)
    d.text((36, 786), 'This donation is non-binding and you can cancel', font=f, fill=TEAL)
    d.text((36, 818), 'the subscription at any time.', font=f, fill=TEAL)
    d.text((32, 880), 'Choose an amount', font=FT('SemiBold', 30), fill=INK)
    w = 686/3
    for k, t in enumerate(('150 NOK', '300 NOK', '600 NOK')):
        box = (round(32+k*w), 932, round(32+(k+1)*w), 1012); on = sel600 and k == 2
        d.rounded_rectangle(box, 8, fill=TEAL if on else FIELD, outline=TEAL if on else LINE, width=2, corners=(k == 0, k == 2, k == 2, k == 0))
        ctext(d, box, t, FT('Bold', 31), (255, 255, 255) if on else MUTE)
    b = d.textbbox((0, 0), 'or enter your own amount', font=f); tw = b[2]-b[0]
    d.line([(32, 1056), (375-tw/2-16, 1056)], fill=LINE, width=2); d.line([(375+tw/2+16, 1056), (718, 1056)], fill=LINE, width=2)
    ctext(d, (32, 1040, 718, 1072), 'or enter your own amount', f, MUTE)
    d.rounded_rectangle((32, 1092, 718, 1172), 8, fill=FIELD, outline=TEAL if amount else LINE, width=2)
    if amount:  # choosing 600 NOK fills the amount field (her request)
        d.text((56, 1110), '600', font=FT('SemiBold', 30), fill=INK)
        nb = d.textbbox((0, 0), 'NOK', font=FT('Regular', 30)); d.text((694-(nb[2]-nb[0]), 1112), 'NOK', font=FT('Regular', 30), fill=MUTE)
    else:
        d.text((56, 1112), 'NOK', font=FT('Regular', 30), fill=MUTE)
    if freq == 'open':  # the frequency list, open over the hint and the amounts
        sh = Image.new('L', im.size, 0); ImageDraw.Draw(sh).rounded_rectangle((36, 784, 714, 784+4*72+8), 10, fill=70)
        from PIL import ImageFilter
        im.paste(Image.new('RGB', im.size, (30, 60, 64)), (0, 0), sh.filter(ImageFilter.GaussianBlur(12))); d = ImageDraw.Draw(im)
        d.rounded_rectangle((32, 776, 718, 776+4*72+8), 10, fill=(255, 255, 255), outline=LINE, width=2)
        for k, t in enumerate(('Monthly', 'Quarterly', 'Biannually', 'Annually')):
            y = 780+k*72
            if k == 0: d.rectangle((34, y, 716, y+72), fill=(232, 243, 243))
            d.text((64, y+18), t, font=FT('Regular', 30), fill=INK)
    return im
save(form_frame(), 'm-form-1')
save(form_frame('open'), 'm-form-open')
save(form_frame('Monthly'), 'm-form-2')
save(form_frame('Monthly', True, True), 'm-form-3')
# the payment steps: status + address bar on top, the card at full width, the toolbar at the bottom
top = page.crop((0, 0, 750, 186)); tool = page.crop((0, 1458, 750, 1624))
def phone_card(c):
    c = c.resize((750, 1193), Image.LANCZOS)
    im = Image.new('RGB', (750, 1624), (255, 255, 255)); im.paste(top, (0, 0)); im.paste(c, (0, 186)); im.paste(tool, (0, 1458)); return im
for n, card in [(3, 'card-payment-method'), (4, 'card-credit-card'), (5, 'card-congrats')]:
    save(phone_card(Image.open(os.path.join(F, card+'.png')).convert('RGB').crop((90, 90, 910, 1394))), f'm-step-{n}')
# paying with Vipps (her request): her card_ pay by vipps 3:75438 at 2x, states 1 (the form) and 3 (Åpne Vipps).
# Her frames say "Pay 630 NOK" and "60 USD"; the total on Payment options is 603 NOK, so both read 603 NOK here.
vc = Image.open(os.path.join(F, 'vipps-column.png')).convert('RGB')
ORANGE = (238, 96, 46)
def pay_btn(c):
    d = ImageDraw.Draw(c); d.rounded_rectangle((48, 1138, 771, 1225), 8, fill=ORANGE)
    ctext(d, (48, 1138, 771, 1225), 'Pay 603 NOK', FT('Bold', 30), (255, 255, 255)); return c
v1 = pay_btn(vc.crop((130, 120, 950, 1424)))
save(phone_card(v1), 'm-vipps-1')
v2 = v1.copy(); d = ImageDraw.Draw(v2)
for (y0, y1), t in [((177, 255), '912 34 567'), ((304, 382), 'ingrid.solberg@mail.no')]:
    d.rectangle((52, y0+4, 767, y1-4), fill=(251, 252, 251)); d.text((83, (y0+y1)//2-21), t, font=FT('Regular', 30), fill=INK)
save(phone_card(v2), 'm-vipps-2')
v3 = vc.crop((130, 2848, 950, 4152)); d = ImageDraw.Draw(v3)
d.rectangle((200, 482, 620, 535), fill=(255, 255, 255))
ctext(d, (0, 486, 820, 530), '603 NOK to Sport Guardian', ImageFont.truetype('C:/Windows/Fonts/arial.ttf', 34), (110, 104, 150))
save(phone_card(v3), 'm-vipps-3')
