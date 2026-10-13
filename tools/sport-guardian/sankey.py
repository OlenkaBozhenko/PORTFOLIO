"""One row of cards and a Sankey under it, for the admin statistics (2026-10-13, her request: "one row of cards
and a modern chart under it"). Who gives (private persons, companies) -> how often -> raised. The split is made up
for the mockup; the totals match the cards (360 000 NOK, 1200 donors). The categorical palette was checked with the
dataviz validator (light surface): lightness band, chroma, CVD and normal-vision separation pass; contrast is a
WARN, so every node carries a direct text label.
"""
from PIL import Image, ImageDraw, ImageFilter
from stat_cards import FONT, S, TEAL, GREEN, _tracked, _spark

FREQ = [('Monthly', (10, 127, 176)), ('Quarterly', (34, 179, 196)), ('Annually', (208, 138, 28)), ('One-time fee', (13, 181, 122))]
FLOWS = {('Private persons', 'Monthly'): 24000, ('Private persons', 'Quarterly'): 22500, ('Private persons', 'Annually'): 1500,
         ('Private persons', 'One-time fee'): 180000, ('Companies', 'Monthly'): 6000, ('Companies', 'Quarterly'): 6000,
         ('Companies', 'One-time fee'): 120000}
INKD, MUT, LAB, UP = (20, 30, 32), (112, 124, 128), (52, 112, 118), (8, 150, 100)


def _ribbon(d, x0, a0, a1, x1, b0, b1, col, steps=48):
    top, bot = [], []
    for k in range(steps+1):
        t = k/steps; e = t*t*(3-2*t); x = x0+(x1-x0)*t
        top.append((x, a0+(b0-a0)*e)); bot.append((x, a1+(b1-a1)*e))
    d.polygon(top+bot[::-1], fill=col)


def dashboard_sankey(im, H_BLOCK=470, chart=True):
    """Returns a new, taller screen: the top of the screen, the new block, then the rest from the donor list."""
    top = im.crop((0, 0, im.width, 207)); rest = im.crop((0, 470, im.width, im.height))
    bg = im.getpixel((10, 300))
    out = Image.new('RGB', (im.width, 207+H_BLOCK+rest.height), bg)
    out.paste(top, (0, 0)); out.paste(rest, (0, 207+H_BLOCK))

    def card(x, y, w, h):
        sh = Image.new('L', out.size, 0); ImageDraw.Draw(sh).rounded_rectangle((x+3, y+8, x+w-3, y+h+4), 18, fill=22)
        out.paste(Image.new('RGB', out.size, (40, 70, 80)), (0, 0), sh.filter(ImageFilter.GaussianBlur(9)))
        c = Image.new('RGBA', (w*S, h*S), (0, 0, 0, 0))
        ImageDraw.Draw(c).rounded_rectangle((0, 0, w*S-1, h*S-1), 18*S, fill=(255, 255, 255))
        return c

    def put(c, x, y):
        c = c.resize((c.width//S, c.height//S), Image.LANCZOS); out.paste(c, (x, y), c)

    lab = FONT('SemiBold', 10*S); big = FONT('Bold', 26*S); unitf = FONT('SemiBold', 11*S)
    # one row of four cards
    x0, y0, h0, gap = 132, 212, 106, 12; w4 = (1305-x0-3*gap)//4
    specs = [('RAISED', '360 000', 'NOK', '+18%', 'of the 500 000 NOK goal', 'bar', .72),
             ('DONORS', '1 200', '', '+17', '17 new this week', 'spark', [900, 940, 960, 1000, 1020, 1060, 1080, 1110, 1140, 1160, 1183, 1200]),
             ('RECURRING', '60 000', 'NOK', '+9%', '200 guardians give monthly or quarterly', 'spark', [30, 32, 33, 36, 38, 41, 44, 47, 50, 54, 57, 60]),
             ('TIME LEFT', '60', 'days', '', 'of 90 · ends 12 Dec', 'ring', 60/90)]
    for i, (name, val, unit, ch, sub, kind, data) in enumerate(specs):
        x = x0+i*(w4+gap); c = card(x, y0, w4, h0); d = ImageDraw.Draw(c)
        _tracked(d, (18*S, 14*S), name, lab, LAB, 1.6*S)
        d.text((18*S, 27*S), val, font=big, fill=INKD); vw = d.textlength(val, font=big)
        uw = 0
        if unit: d.text((18*S+vw+6*S, 39*S), unit, font=unitf, fill=MUT); uw = d.textlength(unit, font=unitf)+6*S
        if ch: d.text((18*S+vw+uw+8*S, 39*S), ch, font=FONT('Bold', 11*S), fill=UP)
        d.text((18*S, 84*S), sub, font=FONT('Regular', 11*S), fill=MUT)
        if kind == 'bar':
            pf = FONT('Bold', 24*S); pt = f'{round(data*100)}%'; pw = d.textlength(pt, font=pf)
            bl, br, by, bh = 18*S, (w4-18)*S-pw-14*S, 64*S, 14*S; n = 34; step = (br-bl)/n; on = round(n*data)
            pb = d.textbbox((0, 0), pt, font=pf); d.text(((w4-18)*S-pw, by+bh/2-(pb[3]-pb[1])/2-pb[1]), pt, font=pf, fill=INKD)
            for k in range(n):
                tx = bl+k*step
                if k < on:
                    t = k/max(on-1, 1); col = tuple(int(TEAL[j]+(GREEN[j]-TEAL[j])*t) for j in range(3))
                else:
                    f = (k-on)/max(n-on-1, 1); col = tuple(int(214+(240-214)*f) for _ in range(3))
                d.rounded_rectangle((tx, by, tx+step*.42, by+bh), 1*S, fill=col)
        elif kind == 'spark':
            _spark(d, ((w4-100)*S, 20*S, (w4-18)*S, 52*S), data, TEAL, None, 2*S)
        else:
            cx, cy, r = (w4-42)*S, 44*S, 22*S
            d.ellipse((cx-r, cy-r, cx+r, cy+r), outline=(234, 240, 241), width=5*S)
            d.arc((cx-r, cy-r, cx+r, cy+r), -90, -90+360*data, fill=TEAL, width=5*S)
            f = FONT('Bold', 10*S); b = d.textbbox((0, 0), '67%', font=f)
            d.text((cx-(b[2]-b[0])/2-b[0], cy-(b[3]-b[1])/2-b[1]), '67%', font=f, fill=INKD)
        put(c, x, y0)

    if not chart:
        return out
    # the Sankey card
    s = S; y1 = y0+h0+16; w1 = 1305-x0; h1 = H_BLOCK-(y1-207)-12
    c = card(x0, y1, w1, h1); d = ImageDraw.Draw(c)
    d.text((22*s, 16*s), 'Where the money comes from', font=FONT('Bold', 15*s), fill=INKD)
    d.text((22*s, 38*s), 'Who gives, how often, and what it adds up to, since the campaign started 30 days ago', font=FONT('Regular', 11*s), fill=MUT)
    ct, cb, gapn = 74*s, (h1-24)*s, 12*s
    total = sum(FLOWS.values()); kk = ((cb-ct)-gapn*3)/total
    hgt = lambda v: max(v*kk, 3*s)

    def stack(names, vals):
        y = ct+((cb-ct)-(sum(hgt(v) for v in vals)+gapn*(len(vals)-1)))/2; pos = {}
        for n, v in zip(names, vals):
            pos[n] = [y, y+hgt(v), y, y]; y += hgt(v)+gapn
        return pos
    srcs = ['Private persons', 'Companies']; sv = [sum(v for (a, b), v in FLOWS.items() if a == n) for n in srcs]
    fr = [n for n, _ in FREQ]; fv = [sum(v for (a, b), v in FLOWS.items() if b == n) for n in fr]
    xL, xM, xR, nw = 200*s, 610*s, (w1-260)*s, 12*s
    P = stack(srcs, sv); M = stack(fr, fv)
    ry = ct+((cb-ct)-total*kk)/2; R = [ry, ry+total*kk, ry]
    col = dict(FREQ)
    lay = Image.new('RGBA', c.size, (0, 0, 0, 0)); ld = ImageDraw.Draw(lay)
    for f in fr:
        for sname in srcs:
            v = FLOWS.get((sname, f))
            if not v: continue
            h = max(v*kk, 2*s); a0 = P[sname][2]; P[sname][2] += h; b0 = M[f][2]; M[f][2] += h
            _ribbon(ld, xL+nw, a0, a0+h, xM, b0, b0+h, col[f]+(72,))
    for f in fr:
        h = max(M[f][1]-M[f][0], 2*s); a0 = M[f][0]; b0 = R[2]; R[2] += (M[f][1]-M[f][0])
        _ribbon(ld, xM+nw, a0, a0+h, xR, b0, b0+h, col[f]+(118,))
    c = Image.alpha_composite(c, lay); d = ImageDraw.Draw(c)
    nf, vf = FONT('SemiBold', 12*s), FONT('Bold', 12*s)
    for n, v in zip(srcs, sv):
        a, b = P[n][0], P[n][1]; d.rounded_rectangle((xL, a, xL+nw, b), 3*s, fill=(52, 72, 76)); ym = (a+b)/2
        d.text((xL-14*s-d.textlength(n, font=nf), ym-17*s), n, font=nf, fill=INKD)
        t = f'{v:,}'.replace(',', ' ')+' NOK'; d.text((xL-14*s-d.textlength(t, font=vf), ym+1*s), t, font=vf, fill=MUT)
    for n, v in zip(fr, fv):
        a, b = M[n][0], max(M[n][1], M[n][0]+3*s); d.rounded_rectangle((xM, a, xM+nw, b), 2*s, fill=col[n]); ym = (a+b)/2
        d.text((xM+nw+10*s, ym-9*s), n, font=nf, fill=INKD); tw = d.textlength(n, font=nf)
        d.text((xM+nw+10*s+tw+8*s, ym-9*s), f'{v:,}'.replace(',', ' ')+' NOK', font=vf, fill=MUT)
    d.rounded_rectangle((xR, R[0], xR+nw, R[1]), 3*s, fill=(14, 34, 37)); ym = (R[0]+R[1])/2
    d.text((xR+nw+16*s, ym-34*s), 'Raised', font=nf, fill=MUT)
    d.text((xR+nw+16*s, ym-15*s), '360 000 NOK', font=FONT('Bold', 21*s), fill=INKD)
    d.text((xR+nw+16*s, ym+16*s), '83% one-time, 17% recurring', font=FONT('Regular', 11*s), fill=MUT)
    put(c, x0, y1)
    return out
