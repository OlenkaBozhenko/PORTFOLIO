"""'Where the money comes from' as its own block across the page (2026-10-13, her request, after her reference 24:
flows drawn as fields of thin vertical lines on a dark ground, one node highlighted). In the project's colours: deep
teal ground, white line fields, the One-time fee path in the brand green. Identity is never colour alone: every node
has a text label and a value, and a table with the same numbers sits under the chart for screen readers.
Writes the SVG and the table into SportGuardian.html between <!-- flow:start --> and <!-- flow:end -->.
The split between private persons and companies is made up for the mockup; the totals match the admin cards.
Run: python flow_svg.py
"""
import os, re
from sankey import FLOWS
HERE = os.path.dirname(os.path.abspath(__file__)); PAGE = os.path.join(HERE, '..', '..', 'SportGuardian.html')

W, H = 1200, 560
SRC = ['Private persons', 'Companies']
FRQ = ['Monthly', 'Quarterly', 'Annually', 'One-time fee']
HI = 'One-time fee'
xL, xM, xR, NW = 210, 590, 960, 16
TOP, BOT, GAP = 120, 520, 26
total = sum(FLOWS.values())
k = (BOT-TOP-GAP*3)/total
h = lambda v: max(v*k, 4)
nok = lambda v: f'{v:,}'.replace(',', ' ')+' NOK'

def stack(names, vals, gap):
    tot = sum(h(v) for v in vals)+gap*(len(vals)-1); y = TOP+((BOT-TOP)-tot)/2; out = {}
    for n, v in zip(names, vals):
        out[n] = [y, y+h(v)]; y += h(v)+gap
    return out

sv = [sum(v for (a, b), v in FLOWS.items() if a == n) for n in SRC]
fv = [sum(v for (a, b), v in FLOWS.items() if b == n) for n in FRQ]
P = stack(SRC, sv, 60); M = stack(FRQ, fv, GAP)
ry0 = TOP+((BOT-TOP)-total*k)/2; R = [ry0, ry0+total*k]

def ribbon(x0, a0, a1, x1, b0, b1):
    c = (x1-x0)*.5
    return (f'M{x0:.1f},{a0:.1f} C{x0+c:.1f},{a0:.1f} {x1-c:.1f},{b0:.1f} {x1:.1f},{b0:.1f} '
            f'L{x1:.1f},{b1:.1f} C{x1-c:.1f},{b1:.1f} {x0+c:.1f},{a1:.1f} {x0:.1f},{a1:.1f} Z')

paths = []
pc = {n: P[n][0] for n in SRC}; mc = {n: M[n][0] for n in FRQ}
for f in FRQ:
    for s in SRC:
        v = FLOWS.get((s, f))
        if not v: continue
        hh = max(v*k, 2); a0 = pc[s]; pc[s] += hh; b0 = mc[f]; mc[f] += hh
        paths.append((f, s, v, ribbon(xL+NW, a0, a0+hh, xM, b0, b0+hh)))
rc = R[0]
for f, v in zip(FRQ, fv):
    hh = max(M[f][1]-M[f][0], 2); a0 = M[f][0]; b0 = rc; rc += M[f][1]-M[f][0]
    paths.append((f, 'Raised', v, ribbon(xM+NW, a0, a0+hh, xR, b0, b0+hh)))

svg = [f'<svg class="flowsvg" viewBox="0 0 {W} {H}" role="img" aria-labelledby="fl-t fl-d">',
       '<title id="fl-t">Where the money comes from</title>',
       '<desc id="fl-d">Private persons give 228 000 NOK and companies 132 000 NOK. By frequency: monthly 30 000, quarterly 28 500, annually 1 500 and one-time 300 000 NOK, together 360 000 NOK raised. The same numbers are in the table below.</desc>',
       '<defs>',
       '<pattern id="hatch" width="6" height="8" patternUnits="userSpaceOnUse"><rect x="0" width="1.3" height="8" fill="#fff" fill-opacity=".55"/></pattern>',
       '<pattern id="hatch-hi" width="6" height="8" patternUnits="userSpaceOnUse"><rect x="0" width="1.6" height="8" fill="#15EDA3"/></pattern>',
       '</defs>',
       # a quiet guide line for each column
       *[f'<line x1="{x+NW/2}" y1="96" x2="{x+NW/2}" y2="{BOT+18}" stroke="#fff" stroke-opacity=".08"/>' for x in (xL, xM, xR)],
       f'<text class="col" x="{xL}" y="80">Who gives</text><text class="col" x="{xM}" y="80">How often</text><text class="col" x="{xR}" y="80">Raised</text>']
for f, s, v, d in paths:
    hi = f == HI
    svg.append(f'<path class="fl{" hi" if hi else ""}" data-f="{f}" data-s="{s}" data-v="{nok(v)}" d="{d}" fill="url(#{"hatch-hi" if hi else "hatch"})"/>')
for n, v in zip(SRC, sv):
    a, b = P[n]; ym = (a+b)/2
    svg.append(f'<g class="nd" data-s="{n}"><rect x="{xL}" y="{a:.1f}" width="{NW}" height="{b-a:.1f}" rx="3" fill="#CFE3E4"/>'
               f'<text class="nm" x="{xL-18}" y="{ym-6:.1f}" text-anchor="end">{n}</text>'
               f'<text class="vl" x="{xL-18}" y="{ym+16:.1f}" text-anchor="end">{nok(v)}</text></g>')
for n, v in zip(FRQ, fv):
    a, b = M[n]; b = max(b, a+4); ym = (a+b)/2; hi = n == HI
    svg.append(f'<g class="nd" data-f="{n}"><rect x="{xM}" y="{a:.1f}" width="{NW}" height="{b-a:.1f}" rx="3" fill="{"#15EDA3" if hi else "#CFE3E4"}"/>'
               f'<text class="nm{" g" if hi else ""}" x="{xM+NW+16}" y="{ym+5:.1f}">{n} <tspan class="vl">{nok(v)}</tspan></text></g>')
a, b = R; ym = (a+b)/2
svg.append(f'<rect x="{xR}" y="{a:.1f}" width="{NW}" height="{b-a:.1f}" rx="3" fill="#fff"/>'
           f'<text class="big" x="{xR+NW+22}" y="{ym+6:.1f}">360 000</text>'
           f'<text class="vl" x="{xR+NW+24}" y="{ym+36:.1f}">NOK raised · 83% one-time</text>')
svg.append('</svg>')

rows = ''.join(f'<tr><th scope="row">{s}</th>'+''.join(f'<td>{nok(FLOWS.get((s, f), 0))}</td>' for f in FRQ)+f'<td>{nok(v)}</td></tr>' for s, v in zip(SRC, sv))
table = ('<table class="vh"><caption>Where the money comes from, in NOK</caption><thead><tr><th scope="col">Who gives</th>'
         + ''.join(f'<th scope="col">{f}</th>' for f in FRQ) + '<th scope="col">Total</th></tr></thead><tbody>' + rows
         + '<tr><th scope="row">Total</th>' + ''.join(f'<td>{nok(v)}</td>' for v in fv) + f'<td>{nok(total)}</td></tr></tbody></table>')

block = ('<!-- flow:start -->\n      <figure class="c1-12 rv flowfig"><div class="flowpanel">'
         '<div class="flowhead"><h3>Where the money comes from</h3><p>Who gives, how often, and what it adds up to, one campaign after 30 days.</p></div>'
         '<div class="flowscroll" tabindex="0" aria-label="Where the money comes from, chart">' + ''.join(svg) + '<div class="fltip" aria-hidden="true"></div></div>'
         + table + '</div><figcaption>Every krone traced from the donor to the total: most of it comes as one-time gifts, and companies give over a third.</figcaption></figure>\n      <!-- flow:end -->')
page = open(PAGE, encoding='utf-8').read()
if '<!-- flow:start -->' in page:
    page = re.sub(r'<!-- flow:start -->.*?<!-- flow:end -->', lambda m: block, page, flags=re.S)
else:
    i = page.index('<div class="browser" style="max-width:1000px">')
    anchor = page.index('</figure>', i)+len('</figure>')  # right after the admin statistics
    page = page[:anchor] + '\n      ' + block + page[anchor:]
open(PAGE, 'w', encoding='utf-8', newline='').write(page)
print('ok', len(paths), 'flows')
