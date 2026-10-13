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
    """One card across the cards row (2026-10-13, her request): a gradient ground so it stands out; on the left the
    amount raised with a progress bar to the goal, on the right a stopwatch whose ring shows the time left."""
    import math
    X, Y, H2 = 132, 214, 74; W2 = 5*W+4*GAP
    w, h = W2*S, H2*S; bg = im.getpixel((X-8, Y+10))
    # deep teal to teal, with a soft green glow on the right
    g = Image.new('RGB', (w, h)); px = g.load()
    A, B = (14, 42, 45), (47, 106, 111)
    for x in range(0, w, 2):
        t = x/w; col = tuple(int(A[j]+(B[j]-A[j])*t) for j in range(3))
        for y in range(h): px[x, y] = col
        if x+1 < w:
            for y in range(h): px[x+1, y] = col
    glow = Image.new('L', (w, h), 0); ImageDraw.Draw(glow).ellipse((int(w*.62), -h, int(w*1.05), 2*h), fill=90)
    g = Image.composite(Image.new('RGB', (w, h), GREEN), g, glow.filter(ImageFilter.GaussianBlur(40*S)))
    m = Image.new('L', (w, h), 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, w-1, h-1), 14*S, fill=255)
    k = Image.new('RGBA', (w, h), (0, 0, 0, 0)); k.paste(g, (0, 0), m); d = ImageDraw.Draw(k)
    WH, mut = (255, 255, 255), (178, 210, 212)
    x = 20*S
    d.text((x, 9*S), 'Raised', font=FONT('SemiBold', 11*S), fill=mut)
    fa = FONT('Bold', 21*S); d.text((x, 22*S), '360 000', font=fa, fill=WH)
    aw = d.textbbox((0, 0), '360 000', font=fa)[2]
    d.text((x+aw+6*S, 31*S), 'NOK', font=FONT('SemiBold', 11*S), fill=mut)
    fc = FONT('Bold', 10*S); cb = d.textbbox((0, 0), '+18% this week', font=fc); cx0 = x+aw+42*S
    d.rounded_rectangle((cx0, 27*S, cx0+cb[2]-cb[0]+16*S, 45*S), 9*S, fill=(17, 77, 70))
    d.text((cx0+8*S-cb[0], 36*S-(cb[3]-cb[1])/2-cb[1]), '+18% this week', font=fc, fill=GREEN)
    last = 4*(W+GAP)*S                      # the left edge of the One-time fee card below, in card pixels
    bx0, bx1, by = x, last-28*S, 55*S
    d.rounded_rectangle((bx0, by, bx1, by+6*S), 3*S, fill=(52, 92, 96))
    fw = int((bx1-bx0)*0.72); grad = Image.new('RGB', (fw, 6*S))
    for i in range(fw):
        t = i/max(fw-1, 1); grad.paste(tuple(int((120, 230, 210)[j]+(GREEN[j]-(120, 230, 210)[j])*t) for j in range(3)), (i, 0, i+1, 6*S))
    gm = Image.new('L', grad.size, 0); ImageDraw.Draw(gm).rounded_rectangle((0, 0, fw-1, 6*S-1), 3*S, fill=255)
    k.paste(grad, (bx0, by), gm)
    # the goal, level with the amount and brighter (her request)
    gl = FONT('Bold', 12*S); gt = '72% of 500 000 NOK goal'; gb = d.textbbox((0, 0), gt, font=gl)
    d.text((bx1-(gb[2]-gb[0])-gb[0], 38*S-(gb[3]-gb[1])), gt, font=gl, fill=GREEN)
    # time left, centred over the One-time fee card, no divider (her request)
    r = 19*S; tx = FONT('Bold', 19*S); tw = max(d.textbbox((0, 0), '60 days', font=tx)[2], d.textbbox((0, 0), 'of 90 · ends 12 Dec', font=FONT('SemiBold', 10*S))[2])
    gw = 2*r+15*S+tw; cx = last+W*S//2-gw//2+r; cy = 41*S
    d.rounded_rectangle((cx-4*S, cy-r-9*S, cx+4*S, cy-r-3*S), 2*S, fill=WH)
    d.line([(cx+r*0.72, cy-r*0.72-1*S), (cx+r*0.92, cy-r*0.92-1*S)], fill=WH, width=3*S)
    d.ellipse((cx-r, cy-r, cx+r, cy+r), fill=(24, 74, 78), outline=(72, 122, 126), width=4*S)
    d.arc((cx-r, cy-r, cx+r, cy+r), -90, -90+360*60/90, fill=GREEN, width=4*S)
    a = math.radians(-90+360*60/90); d.line([(cx, cy), (cx+math.cos(a)*r*0.62, cy+math.sin(a)*r*0.62)], fill=WH, width=2*S)
    d.ellipse((cx-2.5*S, cy-2.5*S, cx+2.5*S, cy+2.5*S), fill=WH)
    x = cx+r+15*S
    d.text((x, 10*S), 'Time left', font=FONT('SemiBold', 11*S), fill=mut)
    d.text((x, 24*S), '60 days', font=tx, fill=WH)
    d.text((x, 48*S), 'of 90 · ends 12 Dec', font=FONT('SemiBold', 10*S), fill=mut)
    ImageDraw.Draw(im).rectangle((X-6, Y-2, X+W2+6, Y+H2+6), fill=bg)
    sh = Image.new('L', im.size, 0); ImageDraw.Draw(sh).rounded_rectangle((X+2, Y+6, X+W2-2, Y+H2+2), 14, fill=40)
    im.paste(Image.new('RGB', im.size, (30, 60, 70)), (0, 0), sh.filter(ImageFilter.GaussianBlur(6)))
    k = k.resize((W2, H2), Image.LANCZOS); im.paste(k, (X, Y), k)
    return im

# ---- the whole statistics block, redrawn after her sales dashboard reference (2026-10-13, inspiration 22):
# light rounded cards, soft shadows, small uppercase letter-spaced labels, big numbers with the change in green,
# one line of context and a small sparkline; One-time fee is the dark highlighted card with a bright bar.
def _tracked(d, xy, text, font, fill, track):
    x, y = xy
    for ch in text:
        d.text((x, y), ch, font=font, fill=fill); x += d.textlength(ch, font=font)+track
    return x

def _spark(d, box, series, col, fill_col, width):
    l, t, r, b = box; mx = max(max(series), 1); mn = min(series)
    pts = [(l+(r-l)*i/(len(series)-1), b-(b-t)*((v-mn)/(mx-mn) if mx > mn else 0)) for i, v in enumerate(series)]
    sm = []
    for i in range(len(pts)-1):
        p0, p1, p2, p3 = pts[max(i-1, 0)], pts[i], pts[i+1], pts[min(i+2, len(pts)-1)]
        for tt in [k/8 for k in range(8)]:
            t2, t3 = tt*tt, tt*tt*tt
            sm.append(tuple(.5*((2*p1[j])+(-p0[j]+p2[j])*tt+(2*p0[j]-5*p1[j]+4*p2[j]-p3[j])*t2+(-p0[j]+3*p1[j]-3*p2[j]+p3[j])*t3) for j in (0, 1)))
    sm.append(pts[-1])
    if fill_col: d.polygon(sm+[(r, b), (l, b)], fill=fill_col)
    d.line(sm, fill=col, width=width, joint='curve')

def dashboard(im):
    bg = im.getpixel((10, 300)); D = ImageDraw.Draw(im); D.rectangle((118, 207, 1322, 470), fill=bg)
    INKD, MUT, LAB, UP = (20, 30, 32), (112, 124, 128), (52, 112, 118), (8, 150, 100)
    DARK = (14, 34, 37)
    def card(x, y, w, h, dark=False):
        sh = Image.new('L', im.size, 0); ImageDraw.Draw(sh).rounded_rectangle((x+3, y+8, x+w-3, y+h+4), 18, fill=34 if dark else 22)
        im.paste(Image.new('RGB', im.size, (40, 70, 80)), (0, 0), sh.filter(ImageFilter.GaussianBlur(9)))
        c = Image.new('RGBA', (w*S, h*S), (0, 0, 0, 0))
        ImageDraw.Draw(c).rounded_rectangle((0, 0, w*S-1, h*S-1), 18*S, fill=DARK if dark else (255, 255, 255))
        return c, ImageDraw.Draw(c)
    def put(c, x, y): c = c.resize((c.width//S, c.height//S), Image.LANCZOS); im.paste(c, (x, y), c)
    lab = FONT('SemiBold', 10*S)
    # row 1: raised (wide) and time left (over the One-time fee card)
    x0, y0, h0 = 132, 212, 84; wT = W; xT = X0+4*(W+GAP); wR = xT-GAP-x0
    c, d = card(x0, y0, wR, h0)
    _tracked(d, (20*S, 14*S), 'RAISED', lab, LAB, 1.6*S)
    big = FONT('Bold', 28*S); d.text((20*S, 26*S), '360 000', font=big, fill=INKD)
    bw = d.textlength('360 000', font=big)
    d.text((20*S+bw+8*S, 39*S), 'NOK', font=FONT('SemiBold', 12*S), fill=MUT)
    d.text((20*S+bw+44*S, 38*S), '+18% this week', font=FONT('Bold', 12*S), fill=UP)
    # the goal: a bar with its label, on the right half
    bl, br, by = 470*S, (wR-24)*S, 52*S
    gt = '72% of the 500 000 NOK goal'; gf = FONT('SemiBold', 11*S)
    d.text((bl, 32*S), gt, font=gf, fill=MUT)
    d.rounded_rectangle((bl, by, br, by+8*S), 4*S, fill=(234, 240, 241))
    fw = int((br-bl)*.72); g = Image.new('RGB', (fw, 8*S))
    for i in range(fw):
        t = i/max(fw-1, 1); g.paste(tuple(int(TEAL[j]+(GREEN[j]-TEAL[j])*t) for j in range(3)), (i, 0, i+1, 8*S))
    gm = Image.new('L', g.size, 0); ImageDraw.Draw(gm).rounded_rectangle((0, 0, fw-1, 8*S-1), 4*S, fill=255); c.paste(g, (bl, by), gm)
    d.text((20*S, 64*S), '200 donors · 17 new this week', font=FONT('Regular', 11*S), fill=MUT)
    put(c, x0, y0)
    c, d = card(xT, y0, wT, h0)
    _tracked(d, (18*S, 14*S), 'TIME LEFT', lab, LAB, 1.6*S)
    d.text((18*S, 26*S), '60', font=big, fill=INKD); nw = d.textlength('60', font=big)
    d.text((18*S+nw+6*S, 39*S), 'days', font=FONT('SemiBold', 12*S), fill=MUT)
    d.text((18*S, 64*S), 'of 90 · ends 12 Dec', font=FONT('Regular', 11*S), fill=MUT)
    cx, cy, r = (wT-38)*S, 44*S, 20*S
    d.ellipse((cx-r, cy-r, cx+r, cy+r), outline=(234, 240, 241), width=5*S)
    d.arc((cx-r, cy-r, cx+r, cy+r), -90, -90+360*60/90, fill=TEAL, width=5*S)
    b = d.textbbox((0, 0), '67%', font=FONT('Bold', 10*S)); d.text((cx-(b[2]-b[0])/2-b[0], cy-(b[3]-b[1])/2-b[1]), '67%', font=FONT('Bold', 10*S), fill=INKD)
    put(c, xT, y0)
    # row 2: the five frequencies
    y1, h1 = 308, 142; total = 360000
    rows = [('MONTHLY', '30 000', 30000, '+12%', '100 donors', DATA[0][4]), ('QUARTERLY', '28 500', 28500, '+8%', '95 donors', DATA[1][4]),
            ('BIANNUALLY', '0', 0, '0%', 'no donors yet', DATA[2][4]), ('ANNUALLY', '1 500', 1500, '+3%', '5 donors', DATA[3][4]),
            ('ONE-TIME FEE', '300 000', 300000, '+24%', '1000 donors', DATA[4][4])]
    for i, (name, amt, val, ch, sub, ser) in enumerate(rows):
        x = X0+i*(W+GAP); dark = i == 4
        c, d = card(x, y1, W, h1, dark)
        fg = (255, 255, 255) if dark else INKD; mut = (150, 180, 182) if dark else MUT
        d.ellipse((16*S, 18*S, 23*S, 25*S), fill=GREEN if dark else TEAL)
        _tracked(d, (30*S, 14*S), name, lab, (170, 205, 205) if dark else LAB, 1.4*S)
        f = FONT('Bold', 22*S); d.text((16*S, 32*S), amt, font=f, fill=fg); aw = d.textlength(amt, font=f)
        d.text((16*S+aw+5*S, 43*S), 'NOK', font=FONT('SemiBold', 10*S), fill=mut)
        up = ch != '0%'
        d.text((16*S+aw+36*S, 43*S), ch, font=FONT('Bold', 10*S), fill=(GREEN if dark else UP) if up else mut)
        d.text((16*S, 70*S), sub, font=FONT('Regular', 11*S), fill=mut)
        if max(ser): _spark(d, (118*S, 66*S, (W-16)*S, 94*S), ser, GREEN if dark else TEAL, None, 2*S)
        else: d.line([(118*S, 90*S), ((W-16)*S, 90*S)], fill=mut, width=S)
        # share of all money raised
        bl, br, by = 16*S, (W-16)*S, 112*S; share = val/total
        d.rounded_rectangle((bl, by, br, by+6*S), 3*S, fill=(40, 64, 66) if dark else (234, 240, 241))
        if share > 0: d.rounded_rectangle((bl, by, bl+max(int((br-bl)*share), 6*S), by+6*S), 3*S, fill=GREEN if dark else TEAL)
        d.text((16*S, 122*S), (('<1' if 0 < share < .01 else str(round(share*100)))+'% of all raised'), font=FONT('SemiBold', 9*S), fill=mut)
        put(c, x, y1)
    return im
