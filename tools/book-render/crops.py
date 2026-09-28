# Crops of a render for checking details: python crops.py big.png
import sys
from PIL import Image
im=Image.open(sys.argv[1] if len(sys.argv)>1 else 'big.png')
bg=Image.new('RGBA',im.size,(233,233,230,255)); bg.alpha_composite(im)
bg.resize((800,600),Image.LANCZOS).save('prev.png')
bb=im.getchannel('A').point(lambda v:255 if v>250 else 0).getbbox(); print('book bbox',bb)
x0,y0,x1,y1=bb; c=int(im.width*0.07)
bg.crop((x1-c,y1-c,x1+c//3,y1+c//3)).resize((600,600),Image.LANCZOS).save('crop_br.png')
bg.crop((x1-c,y0-c//3,x1+c//3,y0+c)).resize((600,600),Image.LANCZOS).save('crop_tr.png')
bg.crop((x0-c,y0,x0+c,y0+2*c)).resize((600,600),Image.LANCZOS).save('crop_tl.png')
