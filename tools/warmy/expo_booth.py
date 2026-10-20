"""The Warmy banner across the whole back wall of an expo booth (her requests, 2026-10-20: the banner on an expo
booth, then the full width of the wall and no TV; reference: an expo booth mockup on Pinterest,
inspiration/32-expo-booth-firewall.png). The empty booth is an AI image made with Figma AI (gpt-image-2.5,
photos/expo-booth-wide-blank.png, node 227:2 in her file), with one blank grey panel across the wall.
Her banner (Figma 225:72619) is rebuilt at the panel's width from its own layers, exported 1:1 from Figma into
figma/: the logo, the headline and text, the QR code with "Talk to us" (its outline and its fill), and the tiger; the dark ground and the
orange glow behind the tiger are redrawn from the banner (base #100D0C, a Gaussian glow fitted to its pixels).
So nothing is stretched: the text stays at the left, the tiger and the QR code at the right, as in the banner.
The print keeps the light of the grey panel; the chair in front of the panel stays in front. Not a real event.
Run: python expo_booth.py -> ../../assets/work/warmy/expo-booth(-768).webp
"""
import os
import numpy as np
from PIL import Image, ImageFilter
HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(HERE, '..', '..', 'assets', 'work', 'warmy')
F = lambda n: Image.open(os.path.join(HERE, 'figma', n+'.png')).convert('RGBA')
K = 2
base = Image.open(os.path.join(HERE, 'photos', 'expo-booth-wide-blank.png')).convert('RGB')
src = np.asarray(base).astype(int)
base = base.resize((base.width*K, base.height*K), Image.LANCZOS)
X0, Y0, X1, Y1 = 116, 247, 1243, 619                      # the grey panel, measured from the grey run
PW, PH = (X1-X0)*K, (Y1-Y0)*K

# the banner at the panel's proportions, in Figma units (height 2480)
H = 2480; W = round(H*PW/PH)
yy, xx = np.mgrid[0:H, 0:W]
d = np.hypot(xx-(W), yy-1700)                             # the glow sits at the right edge, as in the banner
BASE = np.array([16, 13, 12]); AT = np.array([130, 64, 21]); D0, S2 = 1171, 1353031
glow = np.exp(-(d**2-D0**2)/S2)[..., None]
ground = np.clip(BASE+(AT-BASE)*glow, 0, 255).astype('uint8')
art = Image.fromarray(ground, 'RGB').convert('RGBA')
tiger = F('banner-tiger'); art.alpha_composite(tiger, (W-tiger.width, H-tiger.height))
qr = F('banner-qr'); art.alpha_composite(qr, (W-1232+98, 198))           # same place against the tiger as in the banner
art.alpha_composite(F('banner-talk'), (W-1232+97, 271))                  # the filled "Talk to us" over its outline
art.alpha_composite(F('banner-logo'), (148, 200))
art.alpha_composite(F('banner-text'), (148, 642))
art = art.convert('RGB').resize((PW, PH), Image.LANCZOS)

# keep the light that falls on the panel, and print only where the panel is grey (the chair stays in front)
crop = src[Y0:Y1, X0:X1]
grey = (np.abs(crop-125) < 22).all(-1).astype('uint8')*255
mask = Image.fromarray(grey).resize((PW, PH), Image.LANCZOS).filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(1))
light = np.asarray(base.crop((X0*K, Y0*K, X1*K, Y1*K)).convert('L').filter(ImageFilter.GaussianBlur(6*K))).astype(float)
light = np.clip(light/np.median(light), .85, 1.15)[..., None]
art = Image.fromarray(np.clip(np.asarray(art).astype(float)*light, 0, 255).astype('uint8'))
base.paste(art, (X0*K, Y0*K), mask)

full = base.resize((1536, 1024), Image.LANCZOS)
full.save(os.path.join(OUT, 'expo-booth.webp'), quality=86, method=6)
full.resize((768, 512), Image.LANCZOS).save(os.path.join(OUT, 'expo-booth-768.webp'), quality=84, method=6)
print('ok', full.size, W)
