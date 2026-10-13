"""Export the Sport Guardian case page images to ../../assets/work/sport-guardian/ as WebP.

Screens come from her Figma file My-projects-new (YlGWlsWWjKSCxhONMzGG2F), exported 2026-10-13:
1x screenshots in figma/1x, 2x exports in figma/2x. Photos: photos/*.png (print_photo.py).
"""
import os
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__)); F = os.path.join(HERE, 'figma')
OUT = os.path.join(HERE, '..', '..', 'assets', 'work', 'sport-guardian')

def save(im, name, widths, q=84):
    im = im.convert('RGB')
    for i, w in enumerate(widths):
        x = im if im.width == w else im.resize((w, round(im.height*w/im.width)), Image.LANCZOS)
        x.save(os.path.join(OUT, f'{name}-{w}.webp' if len(widths) > 1 else f'{name}.webp'), quality=q)
        print(name, w, x.size)

op = lambda *p: Image.open(os.path.join(*p))
# brand photos (AI base photos with the printed mark)
for n in ['hoodie', 'cap', 'decks']: save(op(HERE, 'photos', n+'.png'), n, [1536, 768])
save(op(HERE, 'photos', 'bottle.png'), 'bottle', [1024, 640])
save(op(HERE, 'photos', 'poster.png'), 'poster', [1024, 640], q=95)  # high quality, so the QR code still scans at 640 px
# product screens
save(op(F, '2x', 'campaign-page.png'), 'screen-campaign', [1440])
save(op(F, '2x', 'mobile-main.png'), 'screen-mobile', [750])
for n in ['club-campaigns', 'shop', 'crowdfunding', 'statistik', 'admin-campaigns', 'admin-business', 'congrats-instagram', 'image-picker']:
    save(op(F, '1x', n+'.png'), 'screen-'+n, [1440])
for n in ['card-payment-method', 'card-credit-card', 'card-congrats']:
    save(op(F, '2x', n+'.png').crop((90, 90, 910, 1394)), n, [820])
save(op(F, '2x', 'create-campaign.png').crop((528, 3538, 2352, 5336)), 'el-create-donations', [1200])
save(op(F, '2x', 'our-donors.png').crop((130, 120, 950, 1198)), 'el-donors', [820])
