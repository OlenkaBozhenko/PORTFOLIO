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
H = 2400  # tall enough for every block; the image is cropped to the content below
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
# back link, then the campaign title as the page title, above the card (her request, 2026-10-14)
arrow(X0+8, 88, 'left', TEAL); text(X0+24, 88, 'Back to campaigns', f('SemiBold', 15), TEAL, 'lm')
text(X0, 138, 'Become a sports guardian', f('Bold', 28), INK, 'ls')
text(X0, 164, 'Swimming for everyone · Fjordby Svømmeklubb · started 15 Sep 2024', f('Regular', 14), MUT, 'ls')

# 1. the progress card, after her reference: the numbers on top, a full-width bar of thin vertical lines, and marks
# under it for the critical minimum, the amount that is enough, and the goal. Thresholds are made up for the mockup.
GAP_B = 24
y0, y1 = 200, 380; card(X0, y0, X1, y1)
GOAL, RAISED_ = 500000, 360000
stats = [('RAISED', '360 000', 'NOK', '+18% this week'), ('GOAL', '500 000', 'NOK', ''), ('STILL NEEDED', '140 000', 'NOK', ''),
         ('DAYS LEFT', '60', 'of 90', ''), ('ENDS', '13 Dec', '2024', '')]
sx = X0+30; colw = 190
for k, (lab_, val, unit, extra) in enumerate(stats):
    x = sx+k*colw
    _tracked(d, P(x, y0+24), lab_, f('SemiBold', 11), LAB, 1.6*S)
    vf = f('Bold', 26 if k == 0 else 22); text(x, y0+68, val, vf, INK, 'ls')
    vw = d.textlength(val, font=vf)/S; text(x+vw+6, y0+68, unit, f('SemiBold', 12), MUT, 'ls')
    if extra:
        bx = x+d.textlength(lab_, font=f('SemiBold', 11))/S+len(lab_)*1.6+10; bw_ = d.textlength(extra, font=f('Bold', 11))/S+18
        d.rounded_rectangle(P(bx, y0+20, bx+bw_, y0+40), 10*S, fill=(221, 248, 236))
        text(bx+bw_/2, y0+30, extra, f('Bold', 11), UP, 'mm')
    if k: d.line(P(x-18, y0+22, x-18, y0+70), fill=LINE, width=S)
text(X1-30, y0+66, '72%', f('Bold', 34), INK, 'rs')
text(X1-30, y0+28, 'of the goal', f('Regular', 12), MUT, 'rm')
# the bar
bl, br, by, bh = X0+30, X1-30, y0+86, 30
n = 300; step = (br-bl)/n; on = round(n*RAISED_/GOAL)
for k in range(n):
    x = bl+k*step
    if k < on:
        t = k/max(on-1, 1); col = tuple(int(TEAL[j]+(GREEN[j]-TEAL[j])*t) for j in range(3))
    else:
        col = (214, 222, 224)
    d.rectangle(P(x, by, x+1.1, by+bh), fill=col)
# the raised mark at the end of the fill
xr = bl+(br-bl)*RAISED_/GOAL; d.rectangle(P(xr-1, by-6, xr+1, by+bh+6), fill=DEEP)
# marks under the bar
CRIT = (176, 20, 74)
marks = [(0, 'Start', '0 NOK · 15 Sep', (70, 82, 86)), (150000, 'Critical minimum', '150 000 · fees for 30 children', CRIT),
         (300000, 'Enough', '300 000 · the season is covered', UP), (500000, 'Goal', '500 000 · gear and travel too', INK)]  # start and end marks (her request, 2026-10-14)
ly = by+bh+26
for v, name, sub, mc in marks:
    x = bl+(br-bl)*v/GOAL; end = v == GOAL
    # two lines (her request): the secondary text first, the name under it; the line runs down to the name's baseline
    nf, sf = f('Bold', 12), f('Regular', 12)
    d.line(P(x, by+bh+2, x, ly+22), fill=mc, width=2*S)
    # the end mark reads to the left of its line
    tx_, an = (x-8, 'rs') if end else (x+8, 'ls')
    text(tx_, ly+4, sub, sf, MUT, an); text(tx_, ly+22, name, nf, mc if mc != DEEP else INK, an)

# 2. the Sankey card: deep teal with a soft glow (as before), the new header with the date range and controls, the
# chart as it was (its data, tooltip and legend, sankey.flow_body), and the column names along the bottom
from sankey import flow_body
y0 = y1+GAP_B; BODY = 420; y1 = y0+92+BODY+52
sh = Image.new('L', im.size, 0); ImageDraw.Draw(sh).rounded_rectangle(P(X0+2, y0+6, X1-2, y1+3), 16*S, fill=40)
im.paste(Image.new('RGB', im.size, (30, 60, 66)), (0, 0), sh.filter(ImageFilter.GaussianBlur(10*S)))
cw, chh = (X1-X0)*S, (y1-y0)*S
g = Image.new('RGB', (cw, chh), (11, 34, 36)); gl = Image.new('L', (cw, chh), 0)
ImageDraw.Draw(gl).ellipse((int(cw*.55), -chh//2, int(cw*1.15), chh//2), fill=255)
g = Image.composite(Image.new('RGB', (cw, chh), (29, 76, 80)), g, gl.filter(ImageFilter.GaussianBlur(90*S)))
m = Image.new('L', (cw, chh), 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, cw-1, chh-1), 16*S, fill=255)
im.paste(g, P(X0, y0), m); d = ImageDraw.Draw(im)
WK, WM, WL = (255, 255, 255), (167, 196, 198), (150, 196, 198)
text(X0+30, y0+40, 'Where the money comes from', f('Bold', 19), WK, 'ls')
text(X0+30, y0+64, 'Who gives, how often, and what it adds up to', f('Regular', 13), WM, 'ls')
d.rounded_rectangle(P(X1-330, y0+22, X1-116, y0+60), 8*S, fill=(24, 58, 62), outline=(62, 100, 104), width=S)
text(X1-223, y0+41, '15.09.2024 – 13.10.2024', f('SemiBold', 13), WK, 'mm')
for cxx in (X1-88, X1-50):
    d.rounded_rectangle(P(cxx-17, y0+24, cxx+17, y0+58), 8*S, fill=(24, 58, 62), outline=(62, 100, 104), width=S)
for dy in (-6, 0, 6): d.line(P(X1-96, y0+41+dy, X1-80, y0+41+dy), fill=WK, width=2*S)
for dy in (-7, 0, 7): d.ellipse(P(X1-52, y0+41+dy-2, X1-48, y0+41+dy+2), fill=WK)
d.line(P(X0, y0+86, X1, y0+86), fill=(40, 74, 78), width=S)
fb = flow_body(X1-X0, BODY); fb = fb.resize(((X1-X0)*S, BODY*S), Image.LANCZOS)
im.paste(fb, P(X0, y0+100), fb); d = ImageDraw.Draw(im)
xL, xM, xR, NW = X0+24, X0+420, X0+806, 10
for xx, t, a in [(xL, 'Who gives', 'l'), (xM, 'How often', 'l'), (xR+NW, 'Raised', 'r')]:
    fn = f('SemiBold', 14)
    if a == 'l': arrow(xx+5, y1-31, 'up', WM, 6); text(xx+18, y1-26, t, fn, WM, 'ls')
    else: arrow(xx-5, y1-31, 'up', WM, 6); text(xx-18, y1-26, t, fn, WM, 'rs')

# 3. the donor table: search, Filter and Export in its header, the column headers in the same card
y0 = y1+GAP_B; rows = [('Ingrid Solberg', 'One-time fee', 'Refund', '450', '21.09.2024', '–'),
                  ('Magnus Hansen', 'Annually', 'Active', '6 600', '20.09.2024', '20.09.2025'),
                  ('Sofie Lie', 'Annually', 'Active', '6 600', '18.09.2024', '18.09.2025'),
                  ('Oliver Berg', 'Monthly', 'Active', '600', '17.09.2024', '17.11.2024'),
                  ('Frida Andersen', 'Quarterly', 'Paused', '900', '16.09.2024', '–'),
                  ('Nordlys Rør AS', 'One-time fee', 'Active', '25 000', '15.09.2024', '–'),
                  ('Olivia Bjørn', 'Monthly', 'Active', '300', '15.09.2024', '15.11.2024'),
                  ('Henrik Dahl', 'Quarterly', 'Active', '750', '15.09.2024', '15.12.2024'),
                  ('Fjord Bakeri AS', 'One-time fee', 'Active', '10 000', '15.09.2024', '–'),
                  ('Emma Lunde', 'Monthly', 'Active', '200', '15.09.2024', '15.11.2024')]
rh = 64; FOOT = 68; y1 = y0+86+46+rh*len(rows)+FOOT; card(X0, y0, X1, y1)
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
# pagination after ten rows
fy = y1-FOOT/2; d.line(P(X0+20, y1-FOOT, X1-20, y1-FOOT), fill=LINE, width=S)
text(X0+30, fy, 'Showing 1–10 of 1 200 donors', f('Regular', 13), MUT, 'lm')
pages = ['‹', '1', '2', '3', '…', '120', '›']; bx = X1-30
for t in reversed(pages):
    w = 34; bx -= w
    on = t == '1'
    if t not in ('…',): d.rounded_rectangle(P(bx, fy-17, bx+w-4, fy+17), 8*S, fill=TEAL if on else CARD, outline=TEAL if on else LINE, width=S)
    if t in ('‹', '›'):
        cx_ = bx+(w-4)/2; dx = -3 if t == '‹' else 3
        d.line([P(cx_-dx, fy-6), P(cx_+dx, fy), P(cx_-dx, fy+6)], fill=INK, width=2*S)
    else:
        text(bx+(w-4)/2, fy, t, f('SemiBold', 13), (255, 255, 255) if on else INK, 'mm')
    bx -= 4
pp = '10 per page'; ppw = d.textlength(pp, font=f('SemiBold', 13))/S+40; px_ = bx-24-ppw
d.rounded_rectangle(P(px_, fy-17, px_+ppw, fy+17), 8*S, outline=LINE, width=S)
text(px_+14, fy, pp, f('SemiBold', 13), INK, 'lm'); d.line([P(px_+ppw-22, fy-3), P(px_+ppw-17, fy+2), P(px_+ppw-12, fy-3)], fill=INK, width=2*S)
H2 = y1+40
im = im.crop((0, 0, W*S, H2*S)).resize((W, H2), Image.LANCZOS)
im.save(os.path.join(OUT, 'screen-statistik.webp'), quality=88)
im.crop((0, 0, W, 65)).save(os.path.join(OUT, 'screen-statistik-head.webp'), quality=88)
im.crop((0, 65, W, H2)).save(os.path.join(OUT, 'screen-statistik-body.webp'), quality=88)
print('ok', im.size)
