"""The Warmy banner on an expo booth (her request, 2026-10-20; reference: an expo booth mockup on Pinterest,
inspiration/32-expo-booth-firewall.png). The empty booth is an AI image made with Figma AI (gpt-image-2.5,
photos/expo-booth-blank.png, node 226:2 in her file); her banner (Figma 225:72619, figma/banner.png) is printed on
its blank grey panel, keeping the light of the panel; the TV shows the Sender tracker and the lit totem carries
the Warmy logotype icon. Not a real event.
The panel is wider than the banner (1.74 : 1 against 1.21 : 1), so the banner sits at the right of the panel and
its dark left edge runs on to the panel's left end.
Run: python expo_booth.py -> ../../assets/work/warmy/expo-booth(-768).webp
"""
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(HERE, '..', '..', 'assets', 'work', 'warmy')
K = 2  # work at twice the size of the booth image, so the banner keeps its detail
base = Image.open(os.path.join(HERE, 'photos', 'expo-booth-blank.png')).convert('RGB')
base = base.resize((base.width*K, base.height*K), Image.LANCZOS)
X0, Y0, X1, Y1 = [v*K for v in (120, 230, 840, 643)]   # the blank panel, measured from the grey run
PW, PH = X1-X0, Y1-Y0

# the banner, fitted to the panel height, at its right end; its left column runs on to the left end of the panel
ban = Image.open(os.path.join(HERE, 'figma', 'banner.png')).convert('RGB')
bw = round(ban.width*PH/ban.height); ban = ban.resize((bw, PH), Image.LANCZOS)
art = Image.new('RGB', (PW, PH))
edge = ban.crop((0, 0, 2, PH)).resize((PW-bw+2, PH), Image.BILINEAR)
art.paste(edge, (0, 0)); art.paste(ban, (PW-bw, 0))

# keep the light that falls on the grey panel: its brightness, relative to its mean, scales the print
light = np.asarray(base.crop((X0, Y0, X1, Y1)).convert('L').filter(ImageFilter.GaussianBlur(6*K))).astype(float)
light = np.clip(light/light.mean(), .82, 1.18)[..., None]
art = Image.fromarray(np.clip(np.asarray(art).astype(float)*light, 0, 255).astype('uint8'))
base.paste(art, (X0, Y0))

# the TV: the Sender tracker, a little dimmed, under a soft diagonal glare
TX0, TY0, TX1, TY1 = [v*K for v in (912, 315, 1230, 494)]
scr = Image.open(os.path.join(OUT, 'tracker-desktop.webp')).convert('RGB')
scr = scr.crop((0, 0, scr.width, round(scr.width*(TY1-TY0)/(TX1-TX0)))).resize((TX1-TX0, TY1-TY0), Image.LANCZOS)
scr = Image.blend(scr, Image.new('RGB', scr.size, (20, 22, 26)), .12)
gl = Image.new('L', scr.size, 0); ImageDraw.Draw(gl).polygon([(scr.width*.55, 0), (scr.width*.8, 0), (scr.width*.45, scr.height), (scr.width*.2, scr.height)], fill=26)
scr = Image.composite(Image.new('RGB', scr.size, (255, 255, 255)), scr, gl.filter(ImageFilter.GaussianBlur(20*K)))
base.paste(scr, (TX0, TY0))

# the lit totem: the Warmy logotype icon (her Figma "Logotype / Icon", 48 x 48 geometry) near its top
d = ImageDraw.Draw(base)
cx, top, s = 1444*K, 196*K, 1.15*K
for (x, y0, col) in [(3, 13, (255, 212, 96)), (17, 7, (253, 162, 47)), (31, 3, (245, 56, 56))]:
    d.rounded_rectangle((cx+(x-24)*s, top+y0*s, cx+(x-24+14)*s, top+45*s), radius=7*s, fill=col)

full = base.resize((1536, 1024), Image.LANCZOS)
full.save(os.path.join(OUT, 'expo-booth.webp'), quality=86, method=6)
full.resize((768, 512), Image.LANCZOS).save(os.path.join(OUT, 'expo-booth-768.webp'), quality=84, method=6)
print('ok', full.size)
