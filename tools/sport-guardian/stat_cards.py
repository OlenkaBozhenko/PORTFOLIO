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
    """One card (2026-10-13, her request): on the left the amount raised with a progress bar to the goal,
    on the right a small stopwatch whose ring shows the time left."""
    X, Y, W2, H2 = 132, 214, 600, 74
    w, h = W2*S, H2*S; bg = im.getpixel((X-8, Y+10))
    k = Image.new('RGBA', (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(k)
    d.rounded_rectangle((0, 0, w-1, h-1), 14*S, fill=(255, 255, 255), outline=(228, 234, 238), width=S)
    mut = (106, 119, 124)
    # left: raised
    x = 16*S
    d.text((x, 9*S), 'Raised', font=FONT('SemiBold', 11*S), fill=mut)
    fa = FONT('Bold', 20*S); d.text((x, 22*S), '360 000', font=fa, fill=INK)
    aw = d.textbbox((0, 0), '360 000', font=fa)[2]
    d.text((x+aw+6*S, 30*S), 'NOK', font=FONT('SemiBold', 11*S), fill=mut)
    fc = FONT('Bold', 10*S); cb = d.textbbox((0, 0), '+18% this week', font=fc); cx0 = x+aw+40*S
    d.rounded_rectangle((cx0, 26*S, cx0+cb[2]-cb[0]+16*S, 44*S), 9*S, fill=(221, 251, 240))
    d.text((cx0+8*S-cb[0], 35*S-(cb[3]-cb[1])/2-cb[1]), '+18% this week', font=fc, fill=(10, 143, 98))
    bx0, bx1, by = x, 420*S, 55*S
    d.rounded_rectangle((bx0, by, bx1, by+6*S), 3*S, fill=(232, 238, 240))
    fw = int((bx1-bx0)*0.72); grad = Image.new('RGB', (fw, 6*S))
    for i in range(fw):
        t = i/max(fw-1, 1); grad.paste(tuple(int(TEAL[j]+(GREEN[j]-TEAL[j])*t) for j in range(3)), (i, 0, i+1, 6*S))
    gm = Image.new('L', grad.size, 0); ImageDraw.Draw(gm).rounded_rectangle((0, 0, fw-1, 6*S-1), 3*S, fill=255)
    k.paste(grad, (bx0, by), gm)
    g = FONT('SemiBold', 10*S); gt = '72% of 500 000 NOK goal'; gb = d.textbbox((0, 0), gt, font=g)
    d.text((bx1-(gb[2]-gb[0]), 10*S), gt, font=g, fill=mut)
    d.line([(440*S, 14*S), (440*S, h-14*S)], fill=(232, 238, 240), width=S)
    # right: a stopwatch, the ring is the time left (60 of 90 days)
    cx, cy, r = 474*S, 41*S, 19*S
    d.rounded_rectangle((cx-4*S, cy-r-9*S, cx+4*S, cy-r-3*S), 2*S, fill=INK)          # crown
    d.line([(cx+r*0.72, cy-r*0.72-1*S), (cx+r*0.92, cy-r*0.92-1*S)], fill=INK, width=3*S)  # side button
    d.ellipse((cx-r, cy-r, cx+r, cy+r), fill=(244, 248, 248), outline=(226, 233, 236), width=4*S)
    d.arc((cx-r, cy-r, cx+r, cy+r), -90, -90+360*60/90, fill=TEAL, width=4*S)
    import math
    a = math.radians(-90+360*60/90); d.line([(cx, cy), (cx+math.cos(a)*r*0.62, cy+math.sin(a)*r*0.62)], fill=INK, width=2*S)
    d.ellipse((cx-2.5*S, cy-2.5*S, cx+2.5*S, cy+2.5*S), fill=INK)
    x = 508*S
    d.text((x, 10*S), 'Time left', font=FONT('SemiBold', 11*S), fill=mut)
    d.text((x, 24*S), '60 days', font=FONT('Bold', 18*S), fill=INK)
    d.text((x, 48*S), 'ends 12 Dec', font=FONT('SemiBold', 10*S), fill=mut)
    ImageDraw.Draw(im).rectangle((X-6, Y-2, 132+5*225+4*12, Y+H2+6), fill=bg)
    sh = Image.new('L', im.size, 0); ImageDraw.Draw(sh).rounded_rectangle((X+2, Y+6, X+W2-2, Y+H2+2), 14, fill=18)
    im.paste(Image.new('RGB', im.size, (30, 60, 70)), (0, 0), sh.filter(ImageFilter.GaussianBlur(6)))
    k = k.resize((W2, H2), Image.LANCZOS); im.paste(k, (X, Y), k)
    return im
