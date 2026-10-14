"""The campaign builder's donation settings, redrawn as choice cards (2026-10-14, her request, after her reference 26):
every option is a card with a line icon, a bold title and a one-line description; who can give is a single choice
(radio button in the card's corner), how often is a multiple choice (checkbox). Light, in the admin's colours and
Open Sans, from her own form (Figma 3:73342: Accept donations from, Select donation frequency, Pre-defined amounts).
Run: python create_form.py -> ../../assets/work/sport-guardian/el-create-donations.webp
"""
import os, math
from PIL import Image, ImageDraw, ImageFilter
from stat_cards import FONT, TEAL
HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(HERE, '..', '..', 'assets', 'work', 'sport-guardian')
S = 2
W, H = 640, 1000
INK, MUT, LINE, CARD, SEL = (22, 30, 32), (106, 118, 122), (226, 232, 234), (255, 255, 255), (238, 246, 246)
REQ = (196, 30, 82)
im = Image.new('RGB', (W*S, H*S), (255, 255, 255)); d = ImageDraw.Draw(im)
P = lambda *v: tuple(int(x*S) for x in v)
f = lambda w, n: FONT(w, n*S)
def text(x, y, t, font, fill=INK, anchor='la'): d.text(P(x, y), t, font=font, fill=fill, anchor=anchor)
def ln(pts, w=1.6, col=INK): d.line([P(*p) for p in pts], fill=col, width=max(1, int(w*S)), joint='curve')
def circ(cx, cy, r, w=1.6, col=INK, fill=None): d.ellipse(P(cx-r, cy-r, cx+r, cy+r), outline=col, width=max(1, int(w*S)), fill=fill)
def rect(x0, y0, x1, y1, r, w=1.6, col=INK): d.rounded_rectangle(P(x0, y0, x1, y1), r*S, outline=col, width=max(1, int(w*S)))

# line icons, 22 pt, drawn in the card's ink
def i_person(x, y, c):
    circ(x+11, y+7, 4.5, col=c); d.arc(P(x+3, y+13, x+19, y+29), 180, 360, fill=c, width=int(1.6*S))
def i_company(x, y, c):
    rect(x+3, y+4, x+15, y+21, 1.5, col=c); rect(x+15, y+10, x+20, y+21, 1.5, col=c)
    for yy in (8, 12, 16): ln([(x+6, y+yy), (x+8, y+yy)], col=c); ln([(x+10, y+yy), (x+12, y+yy)], col=c)
def i_both(x, y, c):
    circ(x+7, y+7, 3.5, col=c); d.arc(P(x+1, y+12, x+13, y+24), 180, 360, fill=c, width=int(1.6*S))
    rect(x+14, y+6, x+21, y+20, 1.2, col=c); ln([(x+16, y+10), (x+19, y+10)], col=c); ln([(x+16, y+14), (x+19, y+14)], col=c)
def i_cal(label):
    def draw(x, y, c):
        rect(x+2, y+4, x+20, y+21, 3, col=c); ln([(x+2, y+9), (x+20, y+9)], col=c); ln([(x+7, y+2), (x+7, y+6)], col=c); ln([(x+15, y+2), (x+15, y+6)], col=c)
        text(x+11, y+15.5, label, f('Bold', 7), c, 'mm')
    return draw
def i_once(x, y, c):
    circ(x+11, y+12, 8.5, col=c); text(x+11, y+12, '1×', f('Bold', 8), c, 'mm')

def choice(x, y, w, h, icon, title, sub, on, kind):
    c = TEAL if on else (70, 82, 86)
    if on:
        d.rounded_rectangle(P(x, y, x+w, y+h), 12*S, fill=SEL, outline=(150, 196, 199), width=S)  # a thin, soft outline (her request)
    else:
        d.rounded_rectangle(P(x, y, x+w, y+h), 12*S, fill=CARD, outline=LINE, width=S)
    icon(x+16, y+14, c)
    text(x+16, y+h-30, title, f('Bold', 13), INK, 'ls'); text(x+16, y+h-13, sub, f('Regular', 11), MUT, 'ls')
    cx, cy = x+w-22, y+22
    if kind == 'radio':
        circ(cx, cy, 8, w=1.6, col=TEAL if on else (176, 186, 190))
        if on: d.ellipse(P(cx-4.5, cy-4.5, cx+4.5, cy+4.5), fill=TEAL)
    else:
        if on:
            d.rounded_rectangle(P(cx-8, cy-8, cx+8, cy+8), 4*S, fill=TEAL)
            ln([(cx-4, cy), (cx-1, cy+3.5), (cx+4.5, cy-3.5)], w=2, col=(255, 255, 255))
        else:
            rect(cx-8, cy-8, cx+8, cy+8, 4, col=(176, 186, 190))

def heading(y, t, req=True, opt=False):
    text(32, y, t, f('Bold', 17), INK, 'ls'); tw = d.textlength(t, font=f('Bold', 17))/S
    if req: text(32+tw+5, y, '*', f('Bold', 17), REQ, 'ls')
    if opt: text(32+tw+6, y, '(Optional)', f('SemiBold', 15), (150, 160, 164), 'ls')
def hint(y, t): text(32, y, t, f('Regular', 12), MUT, 'ls')

# 1. who can give: one choice
heading(52, 'Accept donations from'); hint(74, 'Choose who can support your campaign.')
cw, ch, g = (W-64-2*12)/3, 116, 12
opts = [(i_both, 'Everyone', 'Private persons and companies', True), (i_person, 'Private persons', 'People only', False), (i_company, 'Companies', 'Businesses only', False)]
for k, (ic, t, sub, on) in enumerate(opts):
    choice(32+k*(cw+g), 92, cw, ch, ic, t, sub, on, 'radio')

# 2. how often: several choices
heading(264, 'Select donation frequency'); hint(286, 'Pick every way your donors can give.')
text(W-32, 280, 'Select all', f('SemiBold', 12), TEAL, 'rs')
freqs = [(i_cal('M'), 'Monthly', 'Every month', True), (i_cal('3M'), 'Quarterly', 'Every three months', True),
         (i_cal('6M'), 'Biannually', 'Twice a year', False), (i_cal('Y'), 'Annually', 'Once a year', True),
         (i_once, 'One-time fee', 'A single gift', True)]
for k, (ic, t, sub, on) in enumerate(freqs):
    row, col = divmod(k, 3)
    choice(32+col*(cw+g), 304+row*(ch+g), cw, ch, ic, t, sub, on, 'check')
# a card that says how many are chosen, in the empty sixth cell
x6, y6 = 32+2*(cw+g), 304+ch+g
d.rounded_rectangle(P(x6, y6, x6+cw, y6+ch), 12*S, fill=(247, 249, 250), outline=LINE, width=S)
text(x6+cw/2, y6+ch/2-8, '4 of 5', f('Bold', 18), INK, 'mm'); text(x6+cw/2, y6+ch/2+14, 'ways to give chosen', f('Regular', 11), MUT, 'mm')

# 3. suggested amounts: chips
heading(612, 'Pre-defined donation amounts', req=False, opt=True); hint(634, 'Suggest amounts, donors can still enter their own.')
x = 32
for a in ['150 NOK', '300 NOK', '600 NOK']:
    tw = d.textlength(a, font=f('SemiBold', 13))/S; w = tw+46
    d.rounded_rectangle(P(x, 652, x+w, 688), 18*S, fill=SEL, outline=TEAL, width=S)
    text(x+16, 670, a, f('SemiBold', 13), TEAL, 'lm')
    ln([(x+w-22, 666), (x+w-14, 674)], w=1.6, col=TEAL); ln([(x+w-22, 674), (x+w-14, 666)], w=1.6, col=TEAL)
    x += w+10
d.rounded_rectangle(P(x, 652, x+92, 688), 18*S, outline=(176, 186, 190), width=S)
ln([(x+20, 670), (x+30, 670)], col=INK); ln([(x+25, 665), (x+25, 675)], col=INK); text(x+38, 670, 'Add', f('SemiBold', 13), INK, 'lm')

Hc = 724
im = im.crop((0, 0, W*S, Hc*S))
im = im.resize((W*2 if S != 2 else W*S, Hc*2 if S != 2 else Hc*S), Image.LANCZOS)
im.save(os.path.join(OUT, 'el-create-donations.webp'), quality=90)
print('ok', im.size)
