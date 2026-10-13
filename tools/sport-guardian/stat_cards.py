"""Modern dashboard cards for the admin statistics (2026-10-13, her request: "more modern, like crypto
dashboards, with charts"). Redraws the five frequency cards of the statistics screen (1x, x 132-1305,
y 299-451) as cards with the amount, a growth chip, the donor count and a small area chart.
The chart data is made up for the mockup. Used by fix_screens.py: cards(im) draws onto the 1x screen.
"""
import os, math
from PIL import Image, ImageDraw, ImageFont, ImageFilter
HERE = os.path.dirname(os.path.abspath(__file__))
FONT = lambda w, s: ImageFont.truetype(os.path.join(HERE, 'fonts', f'OpenSans-{w}.ttf'), s)
TEAL, GREEN, INK, DARK = (65, 139, 145), (21, 237, 163), (24, 32, 34), (14, 42, 45)
S = 3  # supersampling

# label, amount, donors, change, series (12 points, made up), highlighted
DATA = [
    ('Monthly', '30 000', 100, '+12%', [8, 9, 9, 11, 12, 12, 14, 15, 15, 17, 18, 20], False),
    ('Quarterly', '28 500', 95, '+8%', [10, 10, 11, 10, 12, 13, 13, 12, 14, 15, 15, 16], False),
    ('Biannually', '0', 0, '0%', [0]*12, False),
    ('Annually', '1 500', 5, '+3%', [3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5], False),
    ('One-time fee', '300 000', 1000, '+24%', [5, 7, 6, 9, 12, 11, 15, 18, 17, 22, 26, 30], True),
]
X0, Y0, W, H, GAP = 132, 299, 225, 152, 12

def card(label, amount, donors, change, series, hi):
    w, h = W*S, H*S
    im = Image.new('RGBA', (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    bg = DARK if hi else (255, 255, 255)
    d.rounded_rectangle((0, 0, w-1, h-1), 14*S, fill=bg, outline=None if hi else (228, 234, 238), width=S)
    fg = (255, 255, 255) if hi else INK; mut = (167, 196, 198) if hi else (106, 119, 124)
    line = GREEN if hi else TEAL
    # top: label and donors
    d.text((14*S, 12*S), label, font=FONT('SemiBold', 12*S), fill=mut)
    dn = f'{donors} donors'; f = FONT('SemiBold', 11*S); b = d.textbbox((0, 0), dn, font=f)
    d.text((w-14*S-(b[2]-b[0]), 13*S), dn, font=f, fill=mut)
    # amount and change chip
    fa = FONT('Bold', 20*S); d.text((14*S, 32*S), amount, font=fa, fill=fg)
    aw = d.textbbox((0, 0), amount, font=fa)[2]
    d.text((14*S+aw+5*S, 40*S), 'NOK', font=FONT('SemiBold', 11*S), fill=mut)
    up = change != '0%'
    chip_bg = ((17, 77, 70) if hi else (221, 251, 240)) if up else ((40, 64, 67) if hi else (238, 241, 243))
    chip_fg = (GREEN if hi else (10, 143, 98)) if up else mut
    fc = FONT('Bold', 10*S); cb = d.textbbox((0, 0), change, font=fc); cw = cb[2]-cb[0]+16*S
    cx = w-14*S-cw; d.rounded_rectangle((cx, 36*S, cx+cw, 54*S), 9*S, fill=chip_bg)
    d.text((cx+8*S-cb[0], 45*S-(cb[3]-cb[1])/2-cb[1]), change, font=fc, fill=chip_fg)
    # area chart along the bottom
    top, bot, l, r = 70*S, h-12*S, 14*S, w-14*S
    mx = max(max(series), 1)
    pts = [(l+(r-l)*i/(len(series)-1), bot-(bot-top)*(v/mx if max(series) else 0)*0.92-2*S) for i, v in enumerate(series)]
    # smooth with a simple Catmull-Rom pass
    sm = []
    for i in range(len(pts)-1):
        p0, p1, p2, p3 = pts[max(i-1, 0)], pts[i], pts[i+1], pts[min(i+2, len(pts)-1)]
        for t in [k/8 for k in range(8)]:
            t2, t3 = t*t, t*t*t
            sm.append(tuple(.5*((2*p1[j])+(-p0[j]+p2[j])*t+(2*p0[j]-5*p1[j]+4*p2[j]-p3[j])*t2+(-p0[j]+3*p1[j]-3*p2[j]+p3[j])*t3) for j in (0, 1)))
    sm.append(pts[-1])
    fill = Image.new('RGBA', (w, h), (0, 0, 0, 0)); grad = Image.new('L', (1, h), 0)
    for y in range(h): grad.putpixel((0, y), int(max(0, min(1, (bot-y)/(bot-top)))*(110 if hi else 80)) if top <= y <= bot else 0)
    mask = Image.new('L', (w, h), 0); ImageDraw.Draw(mask).polygon(sm+[(r, bot), (l, bot)], fill=255)
    alpha = Image.composite(grad.resize((w, h)), Image.new('L', (w, h), 0), mask)
    fill = Image.new('RGBA', (w, h), line+(0,)); fill.putalpha(alpha); im = Image.alpha_composite(im, fill)
    d = ImageDraw.Draw(im)
    if max(series): d.line(sm, fill=line+(255,), width=int(2*S), joint='curve')
    else: d.line([(l, bot-2*S), (r, bot-2*S)], fill=mut+(255,), width=int(1.5*S))
    ex, ey = sm[-1]; d.ellipse((ex-4*S, ey-4*S, ex+4*S, ey+4*S), fill=bg+(255,), outline=line+(255,), width=int(2*S))
    return im.resize((W, H), Image.LANCZOS)

def cards(im):
    d = ImageDraw.Draw(im); d.rectangle((X0-6, Y0-6, X0+5*W+4*GAP+6, Y0+H+8), fill=im.getpixel((X0-10, Y0+20)))
    sh = Image.new('L', im.size, 0); sd = ImageDraw.Draw(sh)
    for i, row in enumerate(DATA):
        x = X0+i*(W+GAP); sd.rounded_rectangle((x+2, Y0+6, x+W-2, Y0+H+2), 14, fill=40 if row[5] else 18)
    sh = sh.filter(ImageFilter.GaussianBlur(6)); im.paste(Image.new('RGB', im.size, (30, 60, 70)), (0, 0), sh)
    for i, row in enumerate(DATA):
        c = card(*row); im.paste(c, (X0+i*(W+GAP), Y0), c)
    return im

# ---- the header of the statistics screen (2026-10-13, her request): the club's own logo instead of the "Logo"
# placeholder, and the time left and the amount raised as dashboard stats, not as button-like chips.
# The 90-day length, the 500 000 NOK goal and "+18% this week" are made up for the mockup.
def club_logo(im):
    page = Image.open(os.path.join(HERE, 'figma', '2x', 'campaign-page.png')).convert('RGB')
    sw = page.crop((156, 84, 294, 150))  # the swim club's swimmer mark in the campaign page header (2x)
    c = Image.new('RGB', (48*S, 48*S), (255, 255, 255)); m = Image.new('L', c.size, 0)
    ImageDraw.Draw(m).ellipse((0, 0, 48*S-1, 48*S-1), fill=255)
    lw = 36*S; sw = sw.resize((lw, round(sw.height*lw/sw.width)), Image.LANCZOS)
    c.paste(sw, ((48*S-lw)//2, (48*S-sw.height)//2+S))
    ring = Image.new('RGBA', c.size, (0, 0, 0, 0)); ImageDraw.Draw(ring).ellipse((0, 0, 48*S-1, 48*S-1), outline=(220, 228, 232, 255), width=S)
    c = Image.composite(c, Image.new('RGB', c.size, (255, 255, 255)), m).convert('RGBA'); c = Image.alpha_composite(c, ring)
    mask = m.resize((48, 48), Image.LANCZOS); c = c.resize((48, 48), Image.LANCZOS).convert('RGB')
    bg = im.getpixel((10, 32)); ImageDraw.Draw(im).ellipse((22, 6, 74, 58), fill=bg)
    im.paste(c, (24, 8), mask)
    return im

def kpis(im):
    X, Y, W2, H2 = 132, 214, 780, 72
    w, h = W2*S, H2*S; bg = im.getpixel((X-8, Y+10))
    k = Image.new('RGB', (w, h), bg); d = ImageDraw.Draw(k)
    mut = (106, 119, 124)
    # time left: a progress ring, 60 of 90 days
    r0, cx, cy = 26*S, 30*S, 36*S
    d.ellipse((cx-r0, cy-r0, cx+r0, cy+r0), outline=(226, 233, 236), width=5*S)
    d.arc((cx-r0, cy-r0, cx+r0, cy+r0), -90, -90+360*60/90, fill=TEAL, width=5*S)
    ctext = lambda box, t, f, fill: (lambda b: d.text(((box[0]+box[2]-(b[2]-b[0]))/2-b[0], (box[1]+box[3]-(b[3]-b[1]))/2-b[1]), t, font=f, fill=fill))(d.textbbox((0, 0), t, font=f))
    ctext((cx-r0, cy-r0, cx+r0, cy+r0), '67%', FONT('Bold', 11*S), INK)
    x = 70*S
    d.text((x, 12*S), 'Time left', font=FONT('SemiBold', 11*S), fill=mut)
    d.text((x, 27*S), '60 days', font=FONT('Bold', 20*S), fill=INK)
    d.text((x, 52*S), 'of 90 · ends 12 Dec', font=FONT('SemiBold', 11*S), fill=mut)
    d.line([(222*S, 14*S), (222*S, 62*S)], fill=(226, 233, 236), width=S)
    # raised: the amount, a growth chip and a progress bar to the goal
    x = 246*S
    d.text((x, 12*S), 'Raised', font=FONT('SemiBold', 11*S), fill=mut)
    fa = FONT('Bold', 20*S); d.text((x, 27*S), '360 000', font=fa, fill=INK)
    aw = d.textbbox((0, 0), '360 000', font=fa)[2]
    d.text((x+aw+6*S, 35*S), 'NOK', font=FONT('SemiBold', 11*S), fill=mut)
    cx0 = x+aw+40*S; fc = FONT('Bold', 10*S); cb = d.textbbox((0, 0), '+18% this week', font=fc)
    d.rounded_rectangle((cx0, 31*S, cx0+cb[2]-cb[0]+16*S, 49*S), 9*S, fill=(221, 251, 240))
    d.text((cx0+8*S-cb[0], 40*S-(cb[3]-cb[1])/2-cb[1]), '+18% this week', font=fc, fill=(10, 143, 98))
    bx0, bx1, by = x, x+300*S, 58*S
    d.rounded_rectangle((bx0, by, bx1, by+6*S), 3*S, fill=(226, 233, 236))
    fill_w = int((bx1-bx0)*0.72); grad = Image.new('RGB', (fill_w, 6*S))
    for i in range(fill_w):
        t = i/max(fill_w-1, 1); grad.paste(tuple(int(TEAL[j]+(GREEN[j]-TEAL[j])*t) for j in range(3)), (i, 0, i+1, 6*S))
    gm = Image.new('L', grad.size, 0); ImageDraw.Draw(gm).rounded_rectangle((0, 0, fill_w-1, 6*S-1), 3*S, fill=255)
    k.paste(grad, (bx0, by), gm)
    d.text((bx1+12*S, by-5*S), '72% of 500 000 NOK goal', font=FONT('SemiBold', 11*S), fill=mut)
    d2 = ImageDraw.Draw(im); d2.rectangle((X-6, Y, X+W2+6, Y+H2+4), fill=bg)
    im.paste(k.resize((W2, H2), Image.LANCZOS), (X, Y))
    return im
