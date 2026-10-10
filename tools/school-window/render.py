# Puts a new view (a drone strike, burning buildings) into the window of the School Context photo, keeping the room.
# base.png (the room) and view.png (the city): Figma AI, Gemini 3.1 Flash Image, 2026-10-10. Run from this folder.
from PIL import Image, ImageDraw, ImageFilter, ImageOps, ImageEnhance
base=Image.open('war-home-masks.png').convert('RGB')
view=ImageOps.mirror(Image.open('view.png').convert('RGB'))
ox,oy=-16,-180
layer=Image.new('RGB',base.size); layer.paste(view,(ox,oy))
layer=layer.filter(ImageFilter.GaussianBlur(1.1))
layer=ImageEnhance.Contrast(layer).enhance(0.92)
m=Image.new('L',base.size,0); d=ImageDraw.Draw(m)
# left pane: above the lamp, above the plants and the boy's head
d.rectangle([333,0,767,427],fill=255)
d.rectangle([280,232,428,427],fill=0)      # lamp
d.rectangle([428,292,767,427],fill=0)      # plants, boy, pot
# right pane: above the small boy's head
d.rectangle([833,0,1034,404],fill=255)
d.rectangle([833,352,1034,404],fill=0)
m=m.filter(ImageFilter.GaussianBlur(9))
# keep the window frame crisp: hard-clip to the glass
clip=Image.new('L',base.size,0); cd=ImageDraw.Draw(clip)
cd.rectangle([333,0,767,427],fill=255); cd.rectangle([833,0,1034,404],fill=255)
from PIL import ImageChops
m=ImageChops.multiply(m,clip)
out=Image.composite(layer,base,m)
out.save('war-home-strike.png')  # then saved as assets/work/school/war-home-strike-1376.webp and -688.webp
