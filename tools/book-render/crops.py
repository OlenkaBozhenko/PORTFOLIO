# Crops of a render for checking details: python crops.py big.png
import sys
from PIL import Image
im=Image.open(sys.argv[1] if len(sys.argv)>1 else 'big.png')
bg=Image.new('RGBA',im.size,(233,233,230,255)); bg.alpha_composite(im)
bg.resize((800,600),Image.LANCZOS).save('prev.png')
bg.crop((1950,1650,2350,2050)).save('crop_br.png')
bg.crop((850,250,1450,850)).save('crop_tl.png')
bg.crop((1950,300,2350,700)).save('crop_tr.png')
