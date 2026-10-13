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
    # the flow card (2026-10-13, her request: the "Where the money comes from" chart on the dashboard too, drawn like
    # the page's own chart as fields of thin vertical lines, One-time fee in green, the rest grey; the amounts are not
    # written on the chart but in a legend with markers on the right)
    s = S; y1 = y0+h0+16; w1 = 1305-x0; h1 = H_BLOCK-(y1-207)-12
    c = card(x0, y1, w1, h1); d = ImageDraw.Draw(c)
    d.text((22*s, 16*s), 'Where the money comes from', font=FONT('Bold', 15*s), fill=INKD)
    d.text((22*s, 38*s), 'Who gives, how often, and what it adds up to, since the campaign started 30 days ago', font=FONT('Regular', 11*s), fill=MUT)
    ct, cb, gapn = 96*s, (h1-22)*s, 14*s
    total = sum(FLOWS.values()); kk = ((cb-ct)-gapn*3)/total
    hgt = lambda v: max(v*kk, 4*s)

    def stack(names, vals):
        y = ct+((cb-ct)-(sum(hgt(v) for v in vals)+gapn*(len(vals)-1)))/2; pos = {}
        for n, v in zip(names, vals):
            pos[n] = [y, y+hgt(v), y, y]; y += hgt(v)+gapn
        return pos
    srcs = ['Private persons', 'Companies']; sv = [sum(v for (a, b), v in FLOWS.items() if a == n) for n in srcs]
    fr = [n for n, _ in FREQ]; fv = [sum(v for (a, b), v in FLOWS.items() if b == n) for n in fr]
    xL, xM, xR, nw = 170*s, 470*s, 770*s, 12*s
    P = stack(srcs, sv); M = stack(fr, fv)
    ry = ct+((cb-ct)-total*kk)/2; R = [ry, ry+total*kk, ry]
    GREY, HI = (128, 150, 155), (13, 181, 122)
    m_grey = Image.new('L', c.size, 0); m_hi = Image.new('L', c.size, 0)
    dg, dh = ImageDraw.Draw(m_grey), ImageDraw.Draw(m_hi)
    for f in fr:
        for sname in srcs:
            v = FLOWS.get((sname, f))
            if not v: continue
            h = max(v*kk, 2*s); a0 = P[sname][2]; P[sname][2] += h; b0 = M[f][2]; M[f][2] += h
            _ribbon(dh if f == 'One-time fee' else dg, xL+nw, a0, a0+h, xM, b0, b0+h, 255)
    for f in fr:
        h = max(M[f][1]-M[f][0], 2*s); a0 = M[f][0]; b0 = R[2]; R[2] += (M[f][1]-M[f][0])
        _ribbon(dh if f == 'One-time fee' else dg, xM+nw, a0, a0+h, xR, b0, b0+h, 255)
    # thin vertical lines, 6 px apart, as on the page's chart
    stripes = Image.new('L', c.size, 0); sd = ImageDraw.Draw(stripes)
    for x in range(0, c.width, 6*s): sd.rectangle((x, 0, x+int(1.4*s)-1, c.height), fill=255)
    from PIL import ImageChops
    for m, colr in ((m_grey, GREY), (m_hi, HI)):
        lay = Image.new('RGBA', c.size, colr+(0,)); lay.putalpha(ImageChops.multiply(m, stripes)); c = Image.alpha_composite(c, lay)
    d = ImageDraw.Draw(c)
    hf = FONT('SemiBold', 10*s)
    for x, t in ((xL, 'WHO GIVES'), (xM, 'HOW OFTEN'), (xR, 'RAISED')):
        _tracked(d, (x, 70*s), t, hf, LAB, 1.6*s)
    nf = FONT('SemiBold', 12*s); NODE = (52, 72, 76)
    for n in srcs:
        a, b = P[n][0], P[n][1]; d.rounded_rectangle((xL, a, xL+nw, b), 3*s, fill=NODE); ym = (a+b)/2
        d.text((xL-12*s-d.textlength(n, font=nf), ym-9*s), n, font=nf, fill=INKD)
    for n in fr:
        a, b = M[n][0], max(M[n][1], M[n][0]+4*s); hi = n == 'One-time fee'
        d.rounded_rectangle((xM, a, xM+nw, b), 2*s, fill=HI if hi else NODE); ym = (a+b)/2
        tw = d.textlength(n, font=nf)  # a white label plate so the name reads over the lines
        d.rounded_rectangle((xM+nw+5*s, ym-11*s, xM+nw+15*s+tw, ym+11*s), 5*s, fill=(255, 255, 255))
        d.text((xM+nw+10*s, ym-9*s), n, font=nf, fill=INKD)
    d.rounded_rectangle((xR, R[0], xR+nw, R[1]), 3*s, fill=(14, 34, 37))
    # the legend: every amount next to a marker that matches its flow
    lx, rx = 860*s, (w1-24)*s
    d.line((lx-26*s, ct, lx-26*s, cb), fill=(230, 236, 238), width=s)
    y = ct+4*s
    d.text((lx, y), 'Raised', font=nf, fill=MUT)
    d.text((lx, y+18*s), '360 000 NOK', font=FONT('Bold', 21*s), fill=INKD)
    d.text((lx, y+48*s), '83% one-time, 17% recurring', font=FONT('Regular', 11*s), fill=MUT)
    vf = FONT('Bold', 12*s)

    def mark(x, yc, kind):
        box = (x, yc-6*s, x+12*s, yc+6*s)
        if kind == 'node':
            d.rounded_rectangle(box, 2*s, fill=NODE); return
        col = HI if kind == 'hi' else GREY
        d.rounded_rectangle(box, 2*s, outline=(226, 232, 234), width=s)
        for k in range(3): d.rectangle((x+(2+4*k)*s, yc-5*s, x+(2+4*k)*s+int(1.4*s)-1, yc+5*s), fill=col)

    y += 84*s
    rows = [('HOW OFTEN', None, None)] + [(n, v, 'hi' if n == 'One-time fee' else 'grey') for n, v in zip(fr, fv)] \
         + [('WHO GIVES', None, None)] + [(n, v, 'node') for n, v in zip(srcs, sv)]
    for n, v, kind in rows:
        if v is None:
            y += 6*s; _tracked(d, (lx, y), n, hf, LAB, 1.6*s); y += 22*s; continue
        yc = y+8*s; mark(lx, yc, kind)
        d.text((lx+20*s, yc-9*s), n, font=nf, fill=INKD)
        t = f'{v:,}'.replace(',', ' ')+' NOK'; d.text((rx-d.textlength(t, font=vf), yc-9*s), t, font=vf, fill=INKD)
        y += 24*s
    put(c, x0, y1)
    return out
