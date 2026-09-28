import base64,sys,json
from PIL import Image
src,out=sys.argv[1],sys.argv[2]
t=open(src,encoding='utf-8').read().strip()
if t.startswith('"'): t=json.loads(t)
b=base64.b64decode(t.split(',',1)[1])
open(out,'wb').write(b)
im=Image.open(out); print(im.size, im.mode)
