"""The logo lockup for the case page's first screen: SG mark, SPORT GUARDIAN, the tagline. Transparent WebP.
Run: python lockup.py -> ../../assets/work/sport-guardian/sg-lockup.webp (1200 px wide) + sg-mark.svg copy"""
import os, shutil
from PIL import Image
from mark import mark, words, WHITE, GREEN, O
from print_photo import stack
HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(HERE, '..', '..', 'assets', 'work', 'sport-guardian')
art = stack(mark(SC=1.6), words('SPORT GUARDIAN', 236, WHITE), words('GIVE SPORTS ENJOYMENT', 132, GREEN, O), gap=90)
art = art.resize((1200, round(art.height*1200/art.width)), Image.LANCZOS)
art.save(os.path.join(OUT, 'sg-lockup.webp'), quality=92, lossless=False); print(art.size)
shutil.copy(os.path.join(HERE, 'sg-mark.svg'), os.path.join(OUT, 'sg-mark.svg'))
