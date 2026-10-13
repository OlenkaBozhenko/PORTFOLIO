from PIL import Image, ImageDraw, ImageFont, ImageChops, ImageFilter
W,H=1600,1200; SC=2; w,h=W*SC,H*SC
BG=(0x41,0x8b,0x91); GR=(0x15,0xed,0xa3); WH=(255,255,255); GH=(0x55,0x9c,0xa2)
C='fonts/Candal.ttf'; O='fonts/OpenSansBI.ttf'
def mask(ch,size,cx,cy):
    f=ImageFont.truetype(C,size*SC); m=Image.new('L',(w,h),0); d=ImageDraw.Draw(m)
    b=d.textbbox((0,0),ch,font=f); d.text((cx*SC-(b[2]-b[0])/2-b[0],cy*SC-(b[3]-b[1])/2-b[1]),ch,font=f,fill=255); return m
def fill(im,m,c): im.paste(c if isinstance(c,Image.Image) else Image.new('RGB',(w,h),c),(0,0),m)
def grow(m,r): return m.filter(ImageFilter.MaxFilter(2*r*SC+1))
def vtext(im,t,font,size,x,ybottom,col):
    f=ImageFont.truetype(font,size*SC); tmp=Image.new('L',(int(f.getlength(t))+40,int(size*1.6*SC)),0)
    ImageDraw.Draw(tmp).text((0,0),t,font=f,fill=255); tmp=tmp.crop(tmp.getbbox()).rotate(90,expand=True)
    L=Image.new('L',(w,h),0); L.paste(tmp,(int(x*SC),int(ybottom*SC)-tmp.size[1])); fill(im,L,col)
# placeholder "image": running track lanes in green
ph=Image.new('RGB',(w,h),GR); d=ImageDraw.Draw(ph)
for i in range(0,14): 
    r=(260+i*70)*SC; d.ellipse([ (1000*SC-r), (620*SC-r*0.7), (1000*SC+r), (620*SC+r*0.7)],outline=WH,width=6*SC)
def build(name, gx, sx, gsize, ssize, cap_x):
    im=Image.new('RGB',(w,h),BG)
    g=mask('G',gsize,gx,600); s=mask('S',ssize,sx,620)
    fill(im,g,GH)                       # guardian: pale, wraps around
    fill(im,ImageChops.subtract(grow(s,10),s),BG)
    fill(im,s,ph)                       # sport: window onto the image
    vtext(im,'SPORT GUARDIAN',C,84,cap_x,1000,WH)
    vtext(im,'GIVE SPORTS ENJOYMENT',O,40,cap_x+110,1000,WH)
    im.resize((W,H),Image.LANCZOS).save(name)
build('draft-1.png',900,1010,1150,640,170)
