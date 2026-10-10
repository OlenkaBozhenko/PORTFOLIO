# Puts a new view (a drone strike, burning buildings) into the window of the School Context photo, keeping the room.
# base.png (the room: a student and a schoolboy in masks) and view.png (the city): Figma AI, Gemini 3.1 Flash Image, 2026-10-10.
# Run from this folder; writes ../../assets/work/school/war-home-strike-1376.webp and -688.webp.
from PIL import Image, ImageDraw, ImageFilter, ImageOps, ImageEnhance, ImageChops
base = Image.open('base.png').convert('RGB')
view = ImageOps.mirror(Image.open('view.png').convert('RGB'))   # mirrored: the strike lands in the left pane
s, ox, oy = 0.75, 150, -107
view = view.resize((round(view.width * s), round(view.height * s)), Image.LANCZOS)
layer = Image.new('RGB', base.size)
layer.paste(view, (ox, oy))
layer = ImageEnhance.Contrast(layer.filter(ImageFilter.GaussianBlur(0.9))).enhance(0.93)

L = (472, 36, 752, 410)    # left glass
R = (828, 36, 1060, 408)   # right glass
m = Image.new('L', base.size, 0); d = ImageDraw.Draw(m)
d.rectangle(L, fill=255); d.rectangle(R, fill=255)
d.rectangle((420, 250, 545, 420), fill=0)    # lamp shade and pole
d.rectangle((545, 338, 752, 420), fill=0)    # plants on the sill
d.rectangle((828, 362, 1060, 420), fill=0)   # the boy's head
m = m.filter(ImageFilter.GaussianBlur(8))
clip = Image.new('L', base.size, 0); c = ImageDraw.Draw(clip)
c.rectangle(L, fill=255); c.rectangle(R, fill=255)
m = ImageChops.multiply(m, clip)
out = Image.composite(layer, base, m)
out.save('../../assets/work/school/war-home-strike-1376.webp', quality=84, method=6)
out.resize((688, 384), Image.LANCZOS).save('../../assets/work/school/war-home-strike-688.webp', quality=80, method=6)
out.crop((380, 0, 1110, 470)).save('preview.png')
