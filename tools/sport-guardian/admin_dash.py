"""The admin campaign dashboard, rebuilt after her reference (2026-10-14, "Orbit Dashboard"): one header card with the
campaign, the amount raised with its progress and the time left; the Sankey "Where the money comes from" with a date
range and controls in its header (her own dotted flows kept, her request); the donor table with search, Filter and
Export in its header and the column headers in the same card. Light, in the admin's colours and Open Sans.
The admin nav strip is her own (figma/1x/statistik.png, 0-65 px, with the club logo from fix_screens.club_logo).
All figures are made up for the mockup; the totals match each other (360 000 NOK, 1200 donors).
Run: python admin_dash.py -> ../../assets/work/sport-guardian/screen-statistik(-head, -body).webp
"""
import os
from PIL import Image, ImageDraw, ImageFilter
from stat_cards import FONT, TEAL, GREEN, club_logo, _tracked
from sankey import FLOWS
HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(HERE, '..', '..', 'assets', 'work', 'sport-guardian')
S = 2
W = 1440; X0, X1 = 132, 1308
BG, CARD, LINE, INK, MUT, LAB = (247, 249, 250), (255, 255, 255), (230, 236, 238), (22, 30, 32), (106, 118, 122), (52, 112, 118)
UP, DEEP = (8, 150, 100), (14, 34, 37)
nok = lambda v: f'{v:,}'.replace(',', ' ')

head = club_logo(Image.open(os.path.join(HERE, 'figma', '1x', 'statistik.png')).convert('RGB')).crop((0, 0, W, 65))
H = 1520
im = Image.new('RGB', (W*S, H*S), BG); im.paste(head.resize((W*S, 65*S), Image.LANCZOS), (0, 0))
d = ImageDraw.Draw(im)
f = lambda w, n: FONT(w, n*S)
P = lambda *v: tuple(int(x*S) for x in v)

def card(x0, y0, x1, y1, r=16):
    sh = Image.new('L', im.size, 0); ImageDraw.Draw(sh).rounded_rectangle(P(x0+2, y0+6, x1-2, y1+3), r*S, fill=26)
    im.paste(Image.new('RGB', im.size, (40, 70, 80)), (0, 0), sh.filter(ImageFilter.GaussianBlur(10*S)))
    d.rounded_rectangle(P(x0, y0, x1, y1), r*S, fill=CARD)

def text(x, y, t, font, fill=INK, anchor='la'):
    d.text(P(x, y), t, font=font, fill=fill, anchor=anchor)

def pill(x, y, w, h, t, font, fg, bg, outline=None, r=None):
    d.rounded_rectangle(P(x, y, x+w, y+h), (r or h/2)*S, fill=bg, outline=outline, width=S)
    text(x+w/2, y+h/2, t, font, fg, 'mm')

def arrow(x, y, dirn, col, size=7):
    # a small arrow: 'up', 'down' or 'left', centred on x, y
    if dirn == 'up': d.line(P(x, y+size, x, y-size), fill=col, width=2*S); d.line([P(x-size*.6, y-size*.4), P(x, y-size), P(x+size*.6, y-size*.4)], fill=col, width=2*S)
    if dirn == 'down': d.line(P(x, y-size, x, y+size), fill=col, width=2*S); d.line([P(x-size*.6, y+size*.4), P(x, y+size), P(x+size*.6, y+size*.4)], fill=col, width=2*S)
    if dirn == 'left': d.line(P(x+size, y, x-size, y), fill=col, width=2*S); d.line([P(x-size*.4, y-size*.6), P(x-size, y), P(x-size*.4, y+size*.6)], fill=col, width=2*S)
# back link
arrow(X0+8, 92, 'left', TEAL); text(X0+24, 92, 'Back to campaigns', f('SemiBold', 15), TEAL, 'lm')

# 1. the header card: the campaign on the left, raised and time left on the right
y0, y1 = 118, 236; card(X0, y0, X1, y1)
cx, cy, r = X0+58, (y0+y1)/2, 34
d.ellipse(P(cx-r, cy-r, cx+r, cy+r), fill=(236, 244, 245))
logo = head.crop((24, 8, 72, 56)).resize((int(52*S), int(52*S)), Image.LANCZOS)
m = Image.new('L', logo.size, 0); ImageDraw.Draw(m).ellipse((0, 0, logo.width-1, logo.height-1), fill=255)
im.paste(logo, P(cx-26, cy-26), m)
text(X0+110, cy-14, 'Become a sports guardian', f('Bold', 24), INK, 'ls')
text(X0+110, cy+14, 'Swimming for everyone · Fjordby Svømmeklubb · started 15 Sep 2024', f('Regular', 14), MUT, 'ls')
# raised
rx = 760
_tracked(d, P(rx, y0+24), 'RAISED', f('SemiBold', 11), LAB, 1.6*S)
text(rx, y0+70, '360 000', f('Bold', 30), INK, 'ls')
nw_ = d.textlength('360 000', font=f('Bold', 30))/S
text(rx+nw_+8, y0+70, 'NOK', f('SemiBold', 13), MUT, 'ls')
text(rx+nw_+48, y0+70, '+18% this week', f('Bold', 13), UP, 'ls')
bl, br, by, bh, n = rx, rx+268, y0+84, 14, 40; step = (br-bl)/n; on = round(n*.72)
for k in range(n):
    if k < on:
        t = k/max(on-1, 1); col = tuple(int(TEAL[j]+(GREEN[j]-TEAL[j])*t) for j in range(3))
    else:
        g = (k-on)/max(n-on-1, 1); col = tuple(int(212+(238-212)*g) for _ in range(3))
    d.rounded_rectangle(P(bl+k*step, by, bl+k*step+step*.42, by+bh), S, fill=col)
text(br+14, by+bh/2, '72%', f('Bold', 22), INK, 'lm')
text(rx, by+bh+20, 'of the 500 000 NOK goal', f('Regular', 12), MUT, 'ls')
d.line(P(rx+352, y0+22, rx+352, y1-22), fill=LINE, width=S)
# time left
tx = rx+384
_tracked(d, P(tx, y0+24), 'TIME LEFT', f('SemiBold', 11), LAB, 1.6*S)
text(tx, y0+70, '60', f('Bold', 30), INK, 'ls'); text(tx+40, y0+70, 'days', f('SemiBold', 13), MUT, 'ls')
text(tx, y0+96, 'of 90 · ends 13 Dec', f('Regular', 12), MUT, 'ls')
ccx, ccy, cr = X1-52, cy, 28
d.ellipse(P(ccx-cr, ccy-cr, ccx+cr, ccy+cr), outline=(234, 240, 241), width=6*S)
d.arc(P(ccx-cr, ccy-cr, ccx+cr, ccy+cr), -90, -90+240, fill=TEAL, width=6*S)
text(ccx, ccy, '67%', f('Bold', 12), INK, 'mm')

# tabs, as in the reference
ty = 268
tabs = ['Overview', 'Donors', 'Payouts', 'Posters and sharing', 'Settings']; x = X0
for i, t in enumerate(tabs):
    fn = f('SemiBold', 15); w = d.textlength(t, font=fn)/S
    text(x, ty, t, fn, TEAL if i == 0 else (70, 80, 84), 'lm')
    if i == 0: d.rectangle(P(x-2, ty+20, x+w+2, ty+23), fill=TEAL)
    x += w+40
d.line(P(X0, ty+23, X1, ty+23), fill=LINE, width=S)
text(X1, ty, 'Latest update: 13.10.2024, 09:41', f('Regular', 13), MUT, 'rm')

# 2. the Sankey card
y0 = 316; y1 = 806; card(X0, y0, X1, y1)
text(X0+30, y0+40, 'Where the money comes from', f('Bold', 19), INK, 'ls')
text(X0+30, y0+64, 'Who gives, how often, and what it adds up to', f('Regular', 13), MUT, 'ls')
# date range and controls in the header
pill(X1-330, y0+22, 214, 38, '15.09.2024 – 13.10.2024', f('SemiBold', 13), INK, CARD, outline=LINE, r=8)
for k, cxx in enumerate([X1-88, X1-50]):
    d.rounded_rectangle(P(cxx-17, y0+24, cxx+17, y0+58), 8*S, outline=LINE, width=S)
d.line(P(X1-96, y0+35, X1-80, y0+35), fill=INK, width=2*S); d.line(P(X1-96, y0+41, X1-80, y0+41), fill=INK, width=2*S); d.line(P(X1-96, y0+47, X1-80, y0+47), fill=INK, width=2*S)
for dy in (-7, 0, 7): d.ellipse(P(X1-52, y0+41+dy-2, X1-48, y0+41+dy+2), fill=INK)
d.line(P(X0, y0+86, X1, y0+86), fill=LINE, width=S)
# the flows: her dotted (hatched) bands, the one-time path in green
SRC = ['Private persons', 'Companies']; FRQ = ['Monthly', 'Quarterly', 'Annually', 'One-time fee']
total = sum(FLOWS.values()); top, bot = y0+124, y1-74; gap = 22
k_ = (bot-top-gap*3)/total; hh = lambda v: max(v*k_, 4)
def stack(names, vals, g):
    tot = sum(hh(v) for v in vals)+g*(len(vals)-1); y = top+((bot-top)-tot)/2; o = {}
    for nme, v in zip(names, vals): o[nme] = [y, y+hh(v)]; y += hh(v)+g
    return o
sv = [sum(v for (a, b), v in FLOWS.items() if a == nme) for nme in SRC]
fv = [sum(v for (a, b), v in FLOWS.items() if b == nme) for nme in FRQ]
Pn = stack(SRC, sv, 70); Mn = stack(FRQ, fv, gap); R = [top+((bot-top)-total*k_)/2, top+((bot-top)-total*k_)/2+total*k_]
xL, xM, xR, NW = X0+70, X0+540, X1-330, 12
def band(x0, a0, a1, x1, b0, b1, steps=60):
    t_, b_ = [], []
    for kk in range(steps+1):
        t = kk/steps; e = t*t*(3-2*t); xx = x0+(x1-x0)*t
        t_.append((xx, a0+(b0-a0)*e)); b_.append((xx, a1+(b1-a1)*e))
    return t_+b_[::-1]
hatch_t = Image.new('RGB', im.size, (255, 255, 255)); hd = ImageDraw.Draw(hatch_t)
for xx in range(0, W*S, 6*S//1 if False else 12): hd.rectangle((xx, 0, xx+2, H*S), fill=TEAL)
hatch_g = Image.new('RGB', im.size, (255, 255, 255)); gd = ImageDraw.Draw(hatch_g)
for xx in range(0, W*S, 12): gd.rectangle((xx, 0, xx+3, H*S), fill=(13, 181, 122))
mask_t = Image.new('L', im.size, 0); mask_g = Image.new('L', im.size, 0)
pc = {nme: Pn[nme][0] for nme in SRC}; mc = {nme: Mn[nme][0] for nme in FRQ}
for fq in FRQ:
    for sname in SRC:
        v = FLOWS.get((sname, fq))
        if not v: continue
        h_ = max(v*k_, 2); a0 = pc[sname]; pc[sname] += h_; b0 = mc[fq]; mc[fq] += h_
        ImageDraw.Draw(mask_g if fq == 'One-time fee' else mask_t).polygon([P(*p) for p in band(xL+NW, a0, a0+h_, xM, b0, b0+h_)], fill=150 if fq == 'One-time fee' else 120)
rc = R[0]
for fq, v in zip(FRQ, fv):
    h_ = max(Mn[fq][1]-Mn[fq][0], 2); a0 = Mn[fq][0]; b0 = rc; rc += Mn[fq][1]-Mn[fq][0]
    ImageDraw.Draw(mask_g if fq == 'One-time fee' else mask_t).polygon([P(*p) for p in band(xM+NW, a0, a0+h_, xR, b0, b0+h_)], fill=190 if fq == 'One-time fee' else 150)
im.paste(hatch_t, (0, 0), mask_t); im.paste(hatch_g, (0, 0), mask_g); d = ImageDraw.Draw(im)
# nodes and labels: "name · share (amount)", as in the reference
for nme, v in zip(SRC, sv):
    a, b = Pn[nme]; d.rounded_rectangle(P(xL, a, xL+NW, b), 3*S, fill=(52, 72, 76))
    l1 = f'{nme} · {round(v/total*100)}%'; wl = max(d.textlength(l1, font=f('Bold', 15)), d.textlength(f'{nok(v)} NOK', font=f('Regular', 13)))/S
    d.rounded_rectangle(P(xL+NW+6, a+4, xL+NW+20+wl, a+48), 6*S, fill=(255, 255, 255))
    text(xL+NW+12, a+22, l1, f('Bold', 15), INK, 'ls'); text(xL+NW+12, a+41, f'{nok(v)} NOK', f('Regular', 13), MUT, 'ls')
for nme, v in zip(FRQ, fv):
    a, b = Mn[nme]; b = max(b, a+4); hi = nme == 'One-time fee'
    d.rounded_rectangle(P(xM, a, xM+NW, b), 3*S, fill=(13, 181, 122) if hi else TEAL)
    sh_ = round(v/total*100); lab_ = f'{nme} · {sh_ if sh_ else "<1"}% ({nok(v)})'
    ym = (a+b)/2 if b-a > 30 else (a+b)/2
    fn = f('Bold', 14); wl = d.textlength(lab_, font=fn)/S
    d.rounded_rectangle(P(xM+NW+8, ym-12, xM+NW+20+wl, ym+12), 6*S, fill=(255, 255, 255))
    text(xM+NW+14, ym, lab_, fn, (8, 120, 82) if hi else INK, 'lm')
d.rounded_rectangle(P(xR, R[0], xR+NW, R[1]), 3*S, fill=DEEP)
ym = (R[0]+R[1])/2
text(xR+NW+18, ym-24, 'Raised', f('SemiBold', 14), MUT, 'ls')
text(xR+NW+18, ym+10, '360 000 NOK', f('Bold', 28), INK, 'ls')
text(xR+NW+18, ym+34, '83% one-time · 17% recurring', f('Regular', 13), MUT, 'ls')
# a tooltip, as on hover in the reference
tx0, ty0 = xL+150, Pn['Private persons'][0]+88
d.rounded_rectangle(P(tx0, ty0, tx0+232, ty0+86), 10*S, fill=(255, 255, 255), outline=LINE, width=S)
text(tx0+16, ty0+22, 'Who gives', f('Regular', 11), MUT, 'ls'); text(tx0+16, ty0+40, 'Private persons · 63% (228 000)', f('SemiBold', 13), INK, 'ls')
text(tx0+16, ty0+60, 'How often', f('Regular', 11), MUT, 'ls'); text(tx0+16, ty0+78, 'One-time fee · 79% (180 000)', f('SemiBold', 13), INK, 'ls')
# column names along the bottom, with arrows, as in the reference
for xx, t, a in [(xL, 'Who gives', 'l'), (xM, 'How often', 'l'), (xR+NW, 'Raised', 'r')]:
    fn = f('SemiBold', 14); w = d.textlength(t, font=fn)/S
    if a == 'l': arrow(xx+5, y1-35, 'up', (70, 80, 84), 6); text(xx+18, y1-30, t, fn, (70, 80, 84), 'ls')
    else: arrow(xx-5, y1-35, 'up', (70, 80, 84), 6); text(xx-18, y1-30, t, fn, (70, 80, 84), 'rs')

# 3. the donor table: search, Filter and Export in its header, the column headers in the same card
y0 = 838; rows = [('Ingrid Solberg', 'One-time fee', 'Refund', '450', '21.09.2024', '–'),
                  ('Magnus Hansen', 'Annually', 'Active', '6 600', '20.09.2024', '20.09.2025'),
                  ('Sofie Lie', 'Annually', 'Active', '6 600', '18.09.2024', '18.09.2025'),
                  ('Oliver Berg', 'Monthly', 'Active', '600', '17.09.2024', '17.11.2024'),
                  ('Frida Andersen', 'Quarterly', 'Paused', '900', '16.09.2024', '–'),
                  ('Nordlys Rør AS', 'One-time fee', 'Active', '25 000', '15.09.2024', '–'),
                  ('Olivia Bjørn', 'Monthly', 'Active', '300', '15.09.2024', '15.11.2024')]
rh = 64; y1 = y0+86+46+rh*len(rows)+12; card(X0, y0, X1, y1)
text(X0+30, y0+48, 'Donors', f('Bold', 19), INK, 'ls'); d.ellipse(P(X0+108, y0+33, X0+124, y0+49), outline=MUT, width=S); text(X0+116, y0+41, 'i', f('Bold', 10), MUT, 'mm')
sx = X1-500; d.rounded_rectangle(P(sx, y0+22, sx+250, y0+60), 8*S, outline=LINE, width=S)
d.ellipse(P(sx+14, y0+33, sx+28, y0+47), outline=MUT, width=2*S); d.line(P(sx+26, y0+45, sx+31, y0+50), fill=MUT, width=2*S)
text(sx+40, y0+41, 'Search for a donor…', f('Regular', 13), MUT, 'lm')
fx = sx+270; text(fx+22, y0+41, 'Filter', f('SemiBold', 14), TEAL, 'lm')
d.polygon([P(fx+2, y0+33), P(fx+16, y0+33), P(fx+11, y0+41), P(fx+11, y0+49), P(fx+7, y0+47), P(fx+7, y0+41)], outline=TEAL, width=2*S)
ex = fx+92; pill(ex, y0+22, 108, 38, '', f('SemiBold', 14), TEAL, CARD, outline=TEAL, r=8); arrow(ex+30, y0+41, 'down', TEAL, 6); text(ex+44, y0+41, 'Export', f('SemiBold', 14), TEAL, 'lm')
# header row
hy = y0+86; d.rectangle(P(X0, hy, X1, hy+46), fill=(243, 247, 248))
cols = [(X0+30, ''), (X0+80, 'Donor'), (X0+300, 'Frequency'), (X0+460, 'Status'), (X0+610, 'Amount, NOK'), (X0+760, 'Since'), (X0+890, 'Next payment')]
d.rounded_rectangle(P(X0+30, hy+14, X0+48, hy+32), 4*S, outline=(160, 170, 174), width=S)
for x, t in cols[1:]:
    text(x, hy+23, t, f('SemiBold', 13), TEAL if t == 'Amount, NOK' else (70, 80, 84), 'lm')
arrow(cols[4][0]+d.textlength('Amount, NOK', font=f('SemiBold', 13))/S+12, hy+23, 'down', TEAL, 5)
STATUS = {'Active': ((8, 120, 82), (221, 248, 236)), 'Refund': ((176, 20, 74), (253, 230, 238)), 'Paused': ((150, 98, 0), (255, 241, 214))}
for i, (nme, fq, st, amt, since, nxt) in enumerate(rows):
    y = hy+46+i*rh
    if i: d.line(P(X0+20, y, X1-20, y), fill=LINE, width=S)
    ym = y+rh/2
    d.rounded_rectangle(P(X0+30, ym-9, X0+48, ym+9), 4*S, outline=(160, 170, 174), width=S)
    text(X0+80, ym, nme, f('SemiBold', 15), INK, 'lm')
    text(cols[2][0], ym, fq, f('Regular', 14), (70, 80, 84), 'lm')
    fg, bg = STATUS[st]; lab_ = st.upper(); wl = d.textlength(lab_, font=f('Bold', 12))/S
    px = cols[3][0]; pill(px, ym-14, wl+40, 28, '', f('Bold', 12), fg, bg); d.ellipse(P(px+12, ym-4, px+20, ym+4), fill=fg); text(px+28, ym, lab_, f('Bold', 12), fg, 'lm')
    text(cols[4][0], ym, amt, f('SemiBold', 15), INK, 'lm')
    text(cols[5][0], ym, since, f('Regular', 14), (70, 80, 84), 'lm'); text(cols[6][0], ym, nxt, f('Regular', 14), (70, 80, 84), 'lm')
    text(X1-70, ym, 'See details', f('SemiBold', 14), TEAL, 'rm')
    for dy in (-6, 0, 6): d.ellipse(P(X1-40, ym+dy-2, X1-36, ym+dy+2), fill=MUT)
H2 = y1+40
im = im.crop((0, 0, W*S, H2*S)).resize((W, H2), Image.LANCZOS)
im.save(os.path.join(OUT, 'screen-statistik.webp'), quality=88)
im.crop((0, 0, W, 65)).save(os.path.join(OUT, 'screen-statistik-head.webp'), quality=88)
im.crop((0, 65, W, H2)).save(os.path.join(OUT, 'screen-statistik-body.webp'), quality=88)
print('ok', im.size)
