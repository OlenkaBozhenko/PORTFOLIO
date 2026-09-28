from PIL import Image
im=Image.open('.render/big.png')
bg=Image.new('RGBA',im.size,(233,233,230,255)); bg.alpha_composite(im)
bg.crop((1900,1500,2400,2100)).save('.render/crop_br.png')
bg.crop((850,200,1350,800)).save('.render/crop_tl.png')
bg.resize((800,600),Image.LANCZOS).save('.render/prev.png')
