# Rewrites the School "Коментарі" screen for the pull-up challenge: the post photo becomes the pull-up photo,
# the placeholder names and comments become real ones. base.png: her 2020 screen (375 x 1122);
# pullups.png: the Progress photo, the boy seen from behind (Figma AI, 2026-10-12); pullups-face.png: the earlier front view, used only for his avatar. Run from this folder.
# Writes the scrolling middle of the screen at 2x: ../../assets/work/school/screen-p-comments.webp
from PIL import Image, ImageDraw, ImageFont
base = Image.open('base.png').convert('RGB').resize((750, 2244), Image.LANCZOS)
im = base.crop((0, 180, 750, 2040))          # between the nav (0-180) and the comment field (2040-2244)
d = ImageDraw.Draw(im)
F = 'C:/Windows/Fonts/'
name_f = ImageFont.truetype(F + 'segoeuib.ttf', 29)
time_f = ImageFont.truetype(F + 'segoeui.ttf', 24)
text_f = ImageFont.truetype(F + 'segoeui.ttf', 29)
INK, GREY, WHITE = (40, 40, 36), (180, 180, 178), (255, 255, 255)

# the post photo: the boy at the bar and the calendar, rounded like the original
ph = Image.open('pullups.png').convert('RGB')
box = (30, 130, 720, 431)
w, h = box[2] - box[0], box[3] - box[1]
src = ph.crop((270, 20, 270 + 690, 20 + round(690 * h / w))).resize((w, h), Image.LANCZOS)
mask = Image.new('L', (w, h), 0); ImageDraw.Draw(mask).rounded_rectangle((0, 0, w - 1, h - 1), 12, fill=255)
im.paste(src, box[:2], mask)

# avatars: faces from the page's own photos (all AI images), cut into circles
def face(path, cx, cy, half):
    return Image.open(path).convert('RGB').crop((cx - half, cy - half, cx + half, cy + half))
A = '../../assets/work/school/'
avatars = [
    face('pullups-face.png', 393, 140, 62),                 # Maksym: his face from the earlier front-view photo
    face(A + 'kids-home-1536.webp', 878, 300, 115),         # Ostap
    face(A + 'kids-home-1536.webp', 625, 335, 100),         # Darynka
    face(A + 'kid-runs-960.webp', 347, 290, 78),            # Ivan
    face(A + 'teacher-prep-1024.webp', 527, 250, 112),      # the teacher
]
# each comment: (top of the comment, top of its text, name, time, lines); dividers at 620, 930, 1240, 1550
comments = [
    (0, 466, 'Максим', '8 год.', ['День 30: 25 разів! Місяць тому ледве', 'підтягувався 2. Дякую всім, хто', 'підтримував і коментував.']),
    (620, 776, 'Остап', '7 год.', ['Ну ти даєш! У мене сьогодні 21,', 'до кінця тижня наздожену.']),
    (930, 1086, 'Даринка', '6 год.', ['Я теж починала з 2, тепер 18.', 'Ваші фото щодня мотивують', 'не пропускати.']),
    (1240, 1396, 'Іван', '5 год.', ['Хто з 7-Б далі? Давайте продовжимо', 'челендж на наступний місяць.']),
    (1550, 1706, 'Олена Іванівна', '3 год.', ['Бачу, як ростуть ваші цифри.', 'Так тримати, ви молодці!']),
]
for (top, ttop, name, time, lines), av in zip(comments, avatars):
    ay = top + (30 if top == 0 else 46)                     # avatar top
    d.ellipse((24, ay - 6, 112, ay + 80), fill=WHITE)
    av = av.resize((74, 74), Image.LANCZOS)
    m = Image.new('L', (74, 74), 0); ImageDraw.Draw(m).ellipse((0, 0, 73, 73), fill=255)
    im.paste(av, (31, ay), m)
    ny = ay + 6
    d.rectangle((112, ny - 12, 724, ny + 86), fill=WHITE)   # old name and time
    d.text((124, ny - 2), name, font=name_f, fill=INK)
    d.text((124, ny + 40), time, font=time_f, fill=GREY)
    d.rectangle((24, ttop - 2, 730, ttop + 112), fill=WHITE)  # old three lines of text
    for i, line in enumerate(lines):
        d.text((32, ttop + i * 36), line, font=text_f, fill=INK)

im.save('../../assets/work/school/screen-p-comments.webp', quality=90, method=6)
im.crop((0, 0, 750, 1300)).save('preview.png')
