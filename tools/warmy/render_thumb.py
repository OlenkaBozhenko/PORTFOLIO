"""Turn the rendered thumb.html (a 1600 x 1200 browser screenshot saved as thumb-render.png) into the landing images.
Render: open http://127.0.0.1:8001/tools/warmy/thumb.html at 1600 x 1200 and save a screenshot as thumb-render.png.
Run: python render_thumb.py -> ../../assets/work/warmy/warmy-thumb.webp (1600 x 1200) and warmy-thumb-800.webp
"""
import os
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(HERE, '..', '..', 'assets', 'work', 'warmy')
im = Image.open(os.path.join(HERE, 'thumb-render.png')).convert('RGB')
im.save(os.path.join(OUT, 'warmy-thumb.webp'), quality=86, method=6)
im.resize((800, 600), Image.LANCZOS).save(os.path.join(OUT, 'warmy-thumb-800.webp'), quality=84, method=6)
print('ok', im.size)
