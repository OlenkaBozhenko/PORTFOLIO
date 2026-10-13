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
    # the flow card (2026-10-13, her requests: the "Where the money comes from" chart on the dashboard too; then
    # "more refined, each flow its own colour", no wide label column on the left, and a tooltip like her node-network
    # reference: the screen shows the chart as if the pointer rests on One-time fee, with a dark tooltip card)
    from PIL import ImageChops
    s = S; y1 = y0+h0+16; w1 = 1305-x0; h1 = H_BLOCK-(y1-207)-12
    c = card(x0, y1, w1, h1); d = ImageDraw.Draw(c)
    d.text((24*s, 18*s), 'Where the money comes from', font=FONT('Bold', 15*s), fill=INKD)
    d.text((24*s, 40*s), 'Who gives, how often, and what it adds up to', font=FONT('Regular', 11*s), fill=MUT)
    # period switch, top right of the chart area
    pf = FONT('SemiBold', 11*s); px = 668*s
    for k, t in enumerate(['7 days', '30 days', 'All']):
        tw = d.textlength(t, font=pf); on = k == 1
        if on: d.rounded_rectangle((px-10*s, 18*s, px+tw+10*s, 42*s), 8*s, fill=(238, 244, 245), outline=(214, 226, 228), width=s)
        d.text((px, 23*s), t, font=pf, fill=INKD if on else MUT); px += tw+26*s
    ct, cb, gapn = 92*s, (h1-24)*s, 16*s
    total = sum(FLOWS.values()); kk = ((cb-ct)-gapn*3)/total
    hgt = lambda v: max(v*kk, 4*s)

    def stack(names, vals):
        y = ct+((cb-ct)-(sum(hgt(v) for v in vals)+gapn*(len(vals)-1)))/2; pos = {}
        for n, v in zip(names, vals):
            pos[n] = [y, y+hgt(v), y, y]; y += hgt(v)+gapn
        return pos
    srcs = ['Private persons', 'Companies']; sv = [sum(v for (a, b), v in FLOWS.items() if a == n) for n in srcs]
    fr = [n for n, _ in FREQ]; fv = [sum(v for (a, b), v in FLOWS.items() if b == n) for n in fr]
    col = dict(FREQ); FOCUS = 'One-time fee'
    xL, xM, xR, nw = 24*s, 420*s, 806*s, 10*s
    P = stack(srcs, sv); M = stack(fr, fv)
    ry = ct+((cb-ct)-total*kk)/2; R = [ry, ry+total*kk, ry]
    masks = {f: Image.new('L', c.size, 0) for f in fr}
    for f in fr:
        md = ImageDraw.Draw(masks[f])
        for sname in srcs:
            v = FLOWS.get((sname, f))
            if not v: continue
            h = max(v*kk, 2*s); a0 = P[sname][2]; P[sname][2] += h; b0 = M[f][2]; M[f][2] += h
            _ribbon(md, xL+nw, a0, a0+h, xM, b0, b0+h, 255)
    for f in fr:
        h = max(M[f][1]-M[f][0], 2*s); a0 = M[f][0]; b0 = R[2]; R[2] += (M[f][1]-M[f][0])
        _ribbon(ImageDraw.Draw(masks[f]), xM+nw, a0, a0+h, xR, b0, b0+h, 255)
    # fine vertical lines, 1 px every 4 px; the hovered flow at full strength, the others quieter
    stripes = Image.new('L', c.size, 0); sd = ImageDraw.Draw(stripes)
    for x in range(0, c.width, 4*s): sd.rectangle((x, 0, x+s-1, c.height), fill=255)
    for f in fr:
        a = ImageChops.multiply(masks[f], stripes).point(lambda v, k=(235 if f == FOCUS else 120): v*k//255)
        lay = Image.new('RGBA', c.size, col[f]+(0,)); lay.putalpha(a); c = Image.alpha_composite(c, lay)
    d = ImageDraw.Draw(c)
    hf = FONT('SemiBold', 10*s)
    for x, t in ((xL, 'WHO GIVES'), (xM, 'HOW OFTEN')):
        _tracked(d, (x, 68*s), t, hf, LAB, 1.6*s)
    rt = 'RAISED'; _tracked(d, (xR+nw-(len(rt)*8.2)*s, 68*s), rt, hf, LAB, 1.6*s)
    lf = FONT('SemiBold', 11*s); NODE = (52, 72, 76)

    def plate(x, y, t, fill=INKD):  # a small white plate so a label reads over the lines
        tw = d.textlength(t, font=lf); d.rounded_rectangle((x-5*s, y-3*s, x+tw+5*s, y+17*s), 5*s, fill=(255, 255, 255))
        d.text((x, y), t, font=lf, fill=fill)
    for n in srcs:
        a, b = P[n][0], P[n][1]; d.rounded_rectangle((xL, a, xL+nw, b), 3*s, fill=NODE)
        plate(xL+nw+10*s, a+6*s, n)
    for n in fr:
        a, b = M[n][0], max(M[n][1], M[n][0]+4*s); ym = (a+b)/2
        d.rounded_rectangle((xM, a, xM+nw, b), 3*s, fill=col[n])
        plate(xM+nw+10*s, ym-8*s, n)
    d.rounded_rectangle((xR, R[0], xR+nw, R[1]), 3*s, fill=(14, 34, 37))

    # the tooltip, as if the pointer rests on the One-time fee flow
    a, b = M[FOCUS][0], M[FOCUS][1]; ptx, pty = 676*s, (a+b)/2+30*s
    d.ellipse((ptx-5*s, pty-5*s, ptx+5*s, pty+5*s), fill=(255, 255, 255), outline=col[FOCUS], width=2*s)
    tx, ty, tw_, th = 556*s, pty-150*s, 240*s, 132*s
    sh = Image.new('L', c.size, 0); ImageDraw.Draw(sh).rounded_rectangle((tx, ty+6*s, tx+tw_, ty+th+6*s), 12*s, fill=70)
    shl = Image.new('RGBA', c.size, (10, 25, 28, 0)); shl.putalpha(sh.filter(ImageFilter.GaussianBlur(10*s))); c = Image.alpha_composite(c, shl)
    d = ImageDraw.Draw(c); TT = (17, 27, 29); TM = (150, 168, 171)
    d.rounded_rectangle((tx, ty, tx+tw_, ty+th), 12*s, fill=TT)
    d.polygon([(ptx-8*s, ty+th), (ptx+8*s, ty+th), (ptx, ty+th+8*s)], fill=TT)
    d.text((tx+16*s, ty+12*s), 'One-time fee', font=FONT('Bold', 14*s), fill=(255, 255, 255))
    d.text((tx+16*s, ty+32*s), 'Last 30 days · 1 000 donors', font=FONT('Regular', 10*s), fill=TM)
    ch = '+24%'; cf = FONT('Bold', 10*s); cw = d.textlength(ch, font=cf)
    d.rounded_rectangle((tx+tw_-16*s-cw-16*s, ty+13*s, tx+tw_-16*s, ty+31*s), 9*s, fill=(17, 77, 70))
    d.text((tx+tw_-16*s-cw-8*s, ty+16*s), ch, font=cf, fill=GREEN)
    _spark(d, (tx+16*s, ty+52*s, tx+tw_-16*s, ty+70*s), [5, 7, 6, 9, 12, 11, 15, 18, 17, 22, 26, 30], col[FOCUS], None, 2*s)
    rf, vf2 = FONT('Regular', 11*s), FONT('Bold', 11*s)
    for k, (dot, t, v) in enumerate([(NODE, 'Private persons', '180 000 NOK'), ((150, 170, 174), 'Companies', '120 000 NOK'), (col[FOCUS], 'Share of raised', '83%')]):
        yy = ty+82*s+k*16*s
        d.rounded_rectangle((tx+16*s, yy+3*s, tx+24*s, yy+11*s), 2*s, fill=dot)
        d.text((tx+32*s, yy), t, font=rf, fill=(220, 230, 231))
        d.text((tx+tw_-16*s-d.textlength(v, font=vf2), yy), v, font=vf2, fill=(255, 255, 255))

    # the legend on the right: every amount next to a marker in its flow's colour
    lx, rx = 872*s, (w1-24)*s
    d.line((lx-28*s, 18*s, lx-28*s, cb), fill=(232, 238, 240), width=s)
    y = 18*s
    d.text((lx, y), 'Raised', font=lf, fill=MUT)
    d.text((lx, y+17*s), '360 000 NOK', font=FONT('Bold', 21*s), fill=INKD)
    d.text((lx, y+46*s), '83% one-time, 17% recurring', font=FONT('Regular', 11*s), fill=MUT)
    vf = FONT('SemiBold', 11*s)
    y += 80*s
    rows = [('HOW OFTEN', None, None)] + [(n, v, col[n]) for n, v in zip(fr, fv)] \
         + [('WHO GIVES', None, None)] + [(n, v, NODE) for n, v in zip(srcs, sv)]
    for n, v, mc in rows:
        if v is None:
            y += 8*s; _tracked(d, (lx, y), n, hf, LAB, 1.6*s); y += 22*s; continue
        yc = y+8*s
        d.rounded_rectangle((lx, yc-5*s, lx+10*s, yc+5*s), 3*s, fill=mc)
        if n == FOCUS: d.rounded_rectangle((lx-8*s, yc-12*s, rx+8*s, yc+12*s), 7*s, outline=(214, 236, 226), width=s)
        d.text((lx+20*s, yc-8*s), n, font=lf, fill=INKD)
        t = f'{v:,}'.replace(',', ' ')+' NOK'; d.text((rx-d.textlength(t, font=vf), yc-8*s), t, font=vf, fill=INKD)
        y += 26*s
    put(c, x0, y1)
    return out
