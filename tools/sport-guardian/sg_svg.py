"""The SG "Speed" mark as a vector SVG, built from the Candal glyph outlines (OFL).

Same construction as the chosen raster variant (render-variants.py, V2): Candal S and G at
760 px, centres 460 px apart, slanted forward (x' = x - 0.3 (y - 500)), the S cut back 12 px
around the G, both letters sliced by 20 px strips every 86 px, a checkered trail of slanted
parallelograms on rows 2 to 5 at the left. Run: python sg_svg.py -> sg-mark*.svg
"""
import os
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.recordingPen import DecomposingRecordingPen
HERE = os.path.dirname(os.path.abspath(__file__))
TEAL, GREEN, WHITE = '#418B91', '#15EDA3', '#FFFFFF'
K, CY, PX = 0.3, 500, 760
font = TTFont(os.path.join(HERE, 'fonts', 'Candal.ttf')); gs = font.getGlyphSet(); cmap = font.getBestCmap()
S_ = PX/font['head'].unitsPerEm

def glyph(ch, cx, cy):
    name = cmap[ord(ch)]; p = SVGPathPen(gs); gs[name].draw(p)
    b = BoundsPen(gs); gs[name].draw(b); x0, y0, x1, y1 = b.bounds
    tx, ty = cx-(x0+x1)/2*S_, cy+(y0+y1)/2*S_
    rec = DecomposingRecordingPen(gs); gs[name].draw(rec)
    pts = [(tx+x*S_, ty-y*S_) for op, args in rec.value for (x, y) in args]
    return p.getCommands(), f'translate({tx:.2f},{ty:.2f}) scale({S_:.5f},{-S_:.5f})', pts, (cy-(y1-y0)/2*S_, cy+(y1-y0)/2*S_)

def skx(x, y): return x-K*(y-CY)

def build(s_col=WHITE, g_col=GREEN, trail_col=None, trail=True, bg=None, pad=0):
    trail_col = trail_col or s_col
    sd, st, spts, (st_top, st_bot) = glyph('S', 620, CY); gd, gt, gpts, (gt_top, gt_bot) = glyph('G', 1080, CY)
    top, bot = min(st_top, gt_top), max(st_bot, gt_bot)
    left = min(skx(x, y) for x, y in spts); right = max(skx(x, y) for x, y in gpts)
    ys = list(range(int(top)+64, int(bot), 86))
    pieces = []
    if trail:
        rowsy = [top]+[y+20 for y in ys]
        for i, y0 in enumerate(rowsy[:-1]):
            y1 = ys[i] if i < len(ys) else bot
            if not (2 <= i <= 5): continue
            x = left+60
            for j in range([3, 4, 3, 2][i-2]):
                wd = [60, 42, 30, 20][j]; x -= wd+[34, 40, 46, 52][j]
                ya, ht = y0+4, (y1-y0)-8
                pieces.append([(x+K*ht, ya), (x+wd+K*ht, ya), (x+wd, ya+ht), (x, ya+ht)])
    xs = [p[0] for pc in pieces for p in pc] + [left, right]
    vx0, vx1, vy0, vy1 = min(xs)-pad, max(xs)+pad, top-pad, bot+pad
    sk = f'matrix(1,0,{-K},1,{K*CY},0)'; big = f'x="{vx0-50:.0f}" y="{vy0-50:.0f}" width="{vx1-vx0+100:.0f}" height="{vy1-vy0+100:.0f}"'
    gw = 24/S_; lw = 20/S_
    stripes = ''.join(f'<rect x="{vx0-50:.0f}" y="{y}" width="{vx1-vx0+100:.0f}" height="20"/>' for y in ys)
    trail_svg = ''.join('<path d="M'+' L'.join(f'{x:.1f},{y:.1f}' for x, y in pc)+' Z"/>' for pc in pieces)
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="{vx0:.1f} {vy0:.1f} {vx1-vx0:.1f} {vy1-vy0:.1f}" width="{vx1-vx0:.0f}" height="{vy1-vy0:.0f}" role="img" aria-label="Sport Guardian">
<defs>
<path id="sg-s" d="{sd}"/><path id="sg-g" d="{gd}"/>
<mask id="sg-cut" maskUnits="userSpaceOnUse" {big}><rect {big} fill="#fff"/><use xlink:href="#sg-g" transform="{gt}" fill="#000" stroke="#000" stroke-width="{gw:.1f}" stroke-linejoin="round"/></mask>
<mask id="sg-strips" maskUnits="userSpaceOnUse" {big}><rect {big} fill="#fff"/><g fill="#000">{stripes}</g></mask>
<mask id="sg-clear" maskUnits="userSpaceOnUse" {big}><rect {big} fill="#fff"/><g transform="{sk}"><use xlink:href="#sg-s" transform="{st}" fill="#000" stroke="#000" stroke-width="{lw:.1f}"/><use xlink:href="#sg-g" transform="{gt}" fill="#000" stroke="#000" stroke-width="{lw:.1f}"/></g></mask>
</defs>
{f'<rect x="{vx0}" y="{vy0}" width="{vx1-vx0}" height="{vy1-vy0}" fill="{bg}"/>' if bg else ''}
<g mask="url(#sg-strips)"><g transform="{sk}"><g mask="url(#sg-cut)"><use xlink:href="#sg-s" transform="{st}" fill="{s_col}"/></g><use xlink:href="#sg-g" transform="{gt}" fill="{g_col}"/></g></g>
<g mask="url(#sg-clear)" fill="{trail_col}">{trail_svg}</g>
</svg>'''
    return svg

if __name__ == '__main__':
    for name, kw in [('sg-mark.svg', {}), ('sg-mark-teal.svg', dict(s_col=TEAL, g_col=GREEN)),
                     ('sg-mark-on-green.svg', dict(s_col=TEAL, g_col=WHITE, trail_col=TEAL))]:
        open(os.path.join(HERE, name), 'w', encoding='utf-8').write(build(**kw))
    print('ok')
