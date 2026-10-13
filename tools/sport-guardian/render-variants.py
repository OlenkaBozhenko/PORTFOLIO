from PIL import Image, ImageDraw, ImageFont, ImageChops, ImageFilter
import math
W,H=1600,1200; SC=2; w,h=W*SC,H*SC
BG=(0x41,0x8b,0x91); GR=(0x15,0xed,0xa3); WH=(255,255,255); GH=(0x55,0x9c,0xa2)
C='fonts/Candal.ttf'; O='fonts/OpenSansBI.ttf'
def blank(): return Image.new('L',(w,h),0)
def letter(ch,size,cx,cy):
    f=ImageFont.truetype(C,size*SC); m=blank(); d=ImageDraw.Draw(m)
    b=d.textbbox((0,0),ch,font=f); d.text((cx*SC-(b[2]-b[0])/2-b[0],cy*SC-(b[3]-b[1])/2-b[1]),ch,font=f,fill=255); return m
def skew(m,k=0.25,cy=600):  # lean forward
    return m.transform(m.size,Image.AFFINE,(1,k,-k*cy*SC,0,1,0),resample=Image.BICUBIC)
def fill(im,m,c): im.paste(Image.new('RGB',(w,h),c),(0,0),m)
def grow(m,r): return m.filter(ImageFilter.GaussianBlur(r*SC*0.6)).point(lambda v:255 if v>12 else 0)
def poly(pts): m=blank(); ImageDraw.Draw(m).polygon([(x*SC,y*SC) for x,y in pts],fill=255); return m
def band(y0,y1,k):  # slanted horizontal band, edges leaning with angle k
    return poly([(-400,y0),(W+400,y0-0),(W+400,y1),(-400,y1)])
def diag_cut(x,y,ang,width):  # a thin diagonal cut line through point
    dx,dy=math.cos(ang),math.sin(ang); nx,ny=-dy,dx; L=3000; hw=width/2
    return poly([(x-dx*L+nx*hw,y-dy*L+ny*hw),(x+dx*L+nx*hw,y+dy*L+ny*hw),(x+dx*L-nx*hw,y+dy*L-ny*hw),(x-dx*L-nx*hw,y-dy*L-ny*hw)])
def dot(cx,cy,r): m=blank(); ImageDraw.Draw(m).ellipse([(cx-r)*SC,(cy-r)*SC,(cx+r)*SC,(cy+r)*SC],fill=255); return m
def para(x,y,wd,ht,k=0.25): return poly([(x+k*ht,y),(x+wd+k*ht,y),(x+wd,y+ht),(x,y+ht)])
def caption(im,x=120,y=1080):
    f=ImageFont.truetype(C,58*SC); ImageDraw.Draw(im).text((x*SC,(y-60)*SC),'SPORT GUARDIAN',font=f,fill=WH)
    f2=ImageFont.truetype(O,30*SC); ImageDraw.Draw(im).text(((x+3)*SC,(y+12)*SC),'GIVE SPORTS ENJOYMENT',font=f2,fill=GR)
def out(im,name): im.resize((W,H),Image.LANCZOS).save(name)
sub=ImageChops.subtract; add=ImageChops.lighter; mul=ImageChops.multiply


def center(im,cx=800,cy=490):
    diff=ImageChops.difference(im,Image.new('RGB',im.size,BG)).convert('L').point(lambda v:255 if v>8 else 0)
    b=diff.getbbox(); dx=int(cx*SC-(b[0]+b[2])/2); dy=int(cy*SC-(b[1]+b[3])/2)
    return ImageChops.offset(im,dx,dy)
def bbox_center(m):
    b=m.getbbox(); return ((b[0]+b[2])/2/SC,(b[1]+b[3])/2/SC)
def shift(m,dx,dy): return ImageChops.offset(m,int(dx*SC),int(dy*SC))

# V1 Athlete: a leaning S inside the G, one diagonal slash through both, a dot for the head
im=Image.new('RGB',(w,h),BG)
g=skew(letter('G',880,800,520),.26,520); s=skew(letter('S',520,860,540),.26,540)
cut=diag_cut(800,520,math.radians(-34),24)
hd=dot(1105,250,54)
fill(im,sub(sub(g,grow(s,14)),add(cut,grow(hd,14))),WH)
fill(im,sub(s,cut),GR); fill(im,hd,GR)
im=center(im); caption(im); out(im,'V1.png')

# V2 Speed: SG slanted and sliced into strips, a short checkered trail fading to the left
im=Image.new('RGB',(w,h),BG)
s=skew(letter('S',760,620,500),.3,500); g=skew(letter('G',760,1080,500),.3,500)
gap=sub(grow(g,12),g); sx=sub(s,gap); letters=add(sx,g)
strips=blank(); d=ImageDraw.Draw(strips)
top=letters.getbbox()[1]/SC; bot=letters.getbbox()[3]/SC
ys=list(range(int(top)+64,int(bot),86))
for y in ys: d.rectangle([0,y*SC,w,(y+20)*SC],fill=255)
fill(im,sub(sx,strips),WH); fill(im,sub(g,strips),GR)
left=letters.getbbox()[0]/SC
fr=blank()
import random; random.seed(7)
rowsy=[top]+[y+20 for y in ys]
for i,y0 in enumerate(rowsy[:-1]):
    y1=ys[i] if i<len(ys) else bot
    if not (2<=i<=5): continue
    x=left+60; n=[3,4,3,2][i-2]
    for j in range(n):
        wd=[60,42,30,20][j]; x-=wd+[34,40,46,52][j]; fr=add(fr,para(x,y0+4,wd,(y1-y0)-8,.3))
fill(im,sub(fr,grow(letters,10)),WH)
im=center(im); caption(im); out(im,'V2.png')

# V3 Lift: the G cut open into a cupped hand that lifts a leaning S; a dot for the head
im=Image.new('RGB',(w,h),BG)
g=skew(letter('G',900,800,640),.22,640)
s=skew(letter('S',500,860,420),.22,420)
topcut=poly([(0,0),(W,0),(W,520),(0,700)])
gh=sub(g,topcut); hd=dot(1060,150,52)
fill(im,sub(gh,grow(s,14)),WH); fill(im,s,GR); fill(im,hd,GR)
im=center(im); caption(im); out(im,'V3.png')

tiles=[Image.open(f'V{i}.png').resize((800,600)) for i in (1,2,3)]+[Image.open('draft-1.png').resize((800,600))]
sheet=Image.new('RGB',(1640,1240),'white')
for i,t in enumerate(tiles): sheet.paste(t,((i%2)*840,(i//2)*640))
sheet.save('V.png')
