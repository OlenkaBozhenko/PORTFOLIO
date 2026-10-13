"""Print the SG mark onto the Figma AI base photos in photos/ (each *-base.png is an AI image,
generated 2026-10-13 with Figma AI gpt-image-2.5 on her Pro plan; not real people or places).

The print takes the fabric's or surface's light: each printed pixel is the ink colour times the
local brightness of the photo relative to the median of the print area, then a slight blur.
Run: python print_photo.py  ->  photos/<name>.png (full size), used by the case page export.
"""
import os, numpy as np
from PIL import Image, ImageFilter
from mark import mark, words, WHITE, GREEN, TEAL, INK, O
HERE = os.path.dirname(os.path.abspath(__file__)); P = os.path.join(HERE, 'photos')

def stamp(base, art, cx, cy, width=None, strength=1.0, blur=0.6, persp=None, height=None):
    if height: width = art.width*height/art.height
    art = art.resize((int(width), int(art.height*width/art.width)), Image.LANCZOS)
    if persp: art = persp(art)
    x0, y0 = int(cx-art.width/2), int(cy-art.height/2)
    a = np.asarray(art).astype(float)/255; b = np.asarray(base.convert('RGB')).astype(float)/255
    reg = b[y0:y0+art.height, x0:x0+art.width]
    L = reg.mean(axis=2); ref = np.median(L[a[..., 3] > .5]) if (a[..., 3] > .5).any() else L.mean()
    shade = np.clip(L/ref, .55, 1.25)[..., None]
    ink = np.clip(a[..., :3]*shade, 0, 1); al = a[..., 3:4]*strength
    reg[:] = reg*(1-al)+ink*al
    out = Image.fromarray((b*255).astype(np.uint8))
    if blur: 
        soft = out.filter(ImageFilter.GaussianBlur(blur)); m = Image.new('L', out.size, 0)
        m.paste(Image.fromarray((a[..., 3]*255).astype(np.uint8)).filter(ImageFilter.MaxFilter(5)), (x0, y0))
        out.paste(soft, (0, 0), m)
    return out

def stack(*parts, gap=18, align='center'):
    W = max(p.width for p in parts); H = sum(p.height for p in parts)+gap*(len(parts)-1)
    im = Image.new('RGBA', (W, H), (0, 0, 0, 0)); y = 0
    for p in parts:
        x = (W-p.width)//2 if align == 'center' else 0; im.paste(p, (x, y), p); y += p.height+gap
    return im

def hoodie():
    base = Image.open(os.path.join(P, 'hoodie-base.png'))
    art = mark()  # the mark alone, no name or tagline (2026-10-13, her request)
    out = stamp(base, art, 770, 560, 400, strength=.93)
    out.save(os.path.join(P, 'hoodie.png'))

if __name__ == '__main__':
    hoodie(); print('ok')

def colour_mask(base, rgb, tol, box):
    b = np.asarray(base.convert('RGB')).astype(int); d = np.abs(b-np.array(rgb)).sum(axis=2)
    m = (d < tol).astype(np.uint8)*255; out = np.zeros_like(m); x0, y0, x1, y1 = box
    out[y0:y1, x0:x1] = m[y0:y1, x0:x1]
    return Image.fromarray(out).filter(ImageFilter.MinFilter(5))

def clipped(base, art_fn, clip):
    printed = art_fn(base); base = base.convert('RGB').copy(); base.paste(printed, (0, 0), clip); return base

def rot(im, a): return im.rotate(a, expand=True, resample=Image.BICUBIC)

def cap():
    base = Image.open(os.path.join(P, 'cap-base.png'))
    art = rot(mark(), 2)  # the mark alone, centred on the front panel (2026-10-13, her request)
    # centred between the top seam and the brim
    stamp(base, art, 712, 482, 300, strength=.95, blur=.5).save(os.path.join(P, 'cap.png'))

def decks():
    base = Image.open(os.path.join(P, 'decks-base.png')).convert('RGB')
    b = np.asarray(base).astype(int)
    def sample(x, y): return tuple(b[y-5:y+5, x-5:x+5].reshape(-1, 3).mean(0).astype(int))
    # left: teal deck, big white and green mark up the board
    clip = colour_mask(base, sample(410, 480), 120, (290, 60, 535, 995))
    base = clipped(base, lambda im: stamp(im, rot(mark(), 90), 410, 530, 215, blur=.4), clip)
    # middle: white deck, the name up the board in teal, the mark small in teal and green
    clip = colour_mask(base, sample(757, 480), 60, (635, 50, 880, 995))
    name = rot(words('SPORT GUARDIAN', 200, TEAL), 90)
    base = clipped(base, lambda im: stamp(stamp(im, name, 757, 475, height=380, blur=.4), rot(mark(s_col=TEAL, g_col=GREEN), 90), 757, 862, 66, blur=.4), clip)
    # right: green deck between the trucks, teal and white mark and the line
    clip = colour_mask(base, sample(1127, 480), 110, (1000, 285, 1260, 680))
    tag = rot(words('GIVE SPORTS ENJOYMENT', 90, TEAL, O), 90)
    base = clipped(base, lambda im: stamp(stamp(im, rot(mark(s_col=TEAL, g_col=WHITE, trail_col=TEAL), 90), 1112, 480, height=330, blur=.4), tag, 1205, 480, height=300, blur=.3), clip)
    base.save(os.path.join(P, 'decks.png'))

if __name__ == '__main__':
    cap(); decks(); print('ok2')

def bottle():
    base = Image.open(os.path.join(P, 'bottle-base.png')).convert('RGB')
    b = np.asarray(base).astype(int); mx, mn = b.max(2), b.min(2)
    white = ((mn > 150) & (mx-mn < 45)).astype(np.uint8)*255
    clip = np.zeros_like(white); clip[250:500, 110:480] = white[250:500, 110:480]
    clip = Image.fromarray(clip).filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(1))
    art = rot(mark(s_col=TEAL, g_col=(0x0f, 0xc4, 0x88), trail_col=TEAL), -23.5)
    base = clipped(base, lambda im: stamp(im, art, 300, 372, 250, blur=.5), clip)
    chest = rot(mark(), -4)
    stamp(base, chest, 682, 985, 120, strength=.9, blur=.5).save(os.path.join(P, 'bottle.png'))

if __name__ == '__main__':
    bottle(); print('ok3')

def poster_art(W=976, H=1862):
    """The poster face: name top left, the mark large down the right edge (cut by it), the line below."""
    im = Image.new('RGBA', (W, H), TEAL+(255,))
    m = rot(mark(), 90); m = m.resize((int(m.width*1080/m.height), 1080), Image.LANCZOS)
    im.paste(m, (W-m.width+int(m.width*.22), 340), m)
    n = words('SPORT', 120, WHITE); g = words('GUARDIAN', 120, WHITE)
    im.paste(n, (70, 70), n); im.paste(g, (70, 70+n.height+22), g)
    for k, line in enumerate(['GIVE SPORTS', 'ENJOYMENT']):
        t = words(line, 118, GREEN, O); im.paste(t, (66, 1470+k*150), t)
    s = words('Back a young athlete near you.', 44, WHITE, O); im.paste(s, (70, H-118), s)
    return im

def poster():
    base = Image.open(os.path.join(P, 'poster-base.png')).convert('RGB')
    x0, y0, x1, y1 = 268, 191, 756, 1122
    art = poster_art().resize((x1-x0, y1-y0), Image.LANCZOS)
    a = np.asarray(art.convert('RGB')).astype(float)/255; b = np.asarray(base).astype(float)/255
    reg = b[y0:y1, x0:x1]; L = reg.mean(2); shade = np.clip(L/np.median(L), .8, 1.15)[..., None]
    b[y0:y1, x0:x1] = np.clip(a*shade, 0, 1)
    Image.fromarray((b*255).astype(np.uint8)).save(os.path.join(P, 'poster.png'))

if __name__ == '__main__':
    poster(); print('ok4')
