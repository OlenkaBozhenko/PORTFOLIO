# Book — project page content

**Source of truth for** [`book.html`](book.html), the page that opens from the **Book** row of the landing's work list (first build 2026-09-26).
Presentation follows [`inspiration.md`](inspiration.md) §2.7: the cover as a 3D mockup first (Architecture Portfolio 2023), the open spreads after it; the work-list thumbnail is a stack of copies (Fabric Book Cover Mockup).

---

## Facts
| | |
|---|---|
| Title | *Røtter i Blix – Thomesen – Inderberg – Johansen Stamsund* |
| Author and client | Amund Gulsvik |
| Her role | Book design and layout, cover |
| Year | 2023 – 2024 (work started 16 May 2023; printed spring 2024) |
| Format | Hardcover, A4 portrait, 210 × 297 mm; 34 mm spine |
| Extent | 432 pages, more than 300 images |
| Printer | LOS DIGITAL AS, Larvik |
| Language | Norwegian |

Sources: the print files (`omslag_34_18.pdf`, `Slekstbok_Røtter i Blix_for utskrift_.pdf`), measured 2026-09-26, and Amund Gulsvik's reference letter, January 2024 (`cv.md`).

## Page copy
- **Eyebrow:** Book design (the project category only, her request 2026-10-22)
- **Headline:** The history of four Lofoten families, set as a 432-page hardcover.
- **Meta row:** Role — Book design, layout, cover · Year — 2023 – 2024 · Author — Amund Gulsvik · Printer — LOS DIGITAL AS
- **About:** *Røtter i Blix – Thomesen – Inderberg – Johansen Stamsund* follows the families behind Haldis Blix Gulsvik, who grew up in the fishing village of Stamsund in Lofoten; the families are traced back to the 1500s, and through these generations a part of the history of Norway unfolds as well. The author, Amund Gulsvik, gathered the family stories, archive photographs and maps, and wrote the book for the coming generations who look for their roots. *(Adapted from the back-cover text.)*
- **Objective** *(draft — to confirm with her)*: turn a long family history, more than 300 archive photographs and maps, into a book that reads calmly from the title page to the list of sources, and prepare it for print.
- **Quote:** "She has done the work on the book to our great satisfaction and with great accuracy." — Amund Gulsvik, author (translated from his reference letter).

## 3D mockup
Built in CSS from her own cover file, no stock mockup: front, spine and back panels are cut from `omslag_34_18.pdf` at its fold marks — back 43.4–253.4 mm, hinge, spine 263.6–297.4 mm (34 mm), hinge, front 307.4–517.4 mm; height 43.4–340.4 mm (18 mm turn-in). Files in `assets/work/book/`: `cover-front.jpg`, `cover-spine.jpg`, `cover-back.jpg`.
- **Reference:** her photos of the printed book (2026-09-26, Notion *For Portfolio* → "Book mockup: the real hardcover"): matte white case binding, rounded spine with a hinge groove, boards overhanging the page block, a sewn block that curves into the gutter.
- **Light and shadow (2026-09-28):** light from the right on every mockup, as in the landing render. Shadows are dark grey (#4a4a46), never black, and fade out smoothly into the ground: the spreads and the back cover use six stacked shadow layers of growing blur and falling opacity, offset to the left; the standing cover has a soft grey shade on the backdrop to its left and a soft ground shade where it stands (no hard floor line).
- **Project page:** one closed book standing, turned three-quarters to show the front and the spine (CSS 3D, it turns a little under the pointer, so it may stand at an angle), and the back cover beside it. Both are the same size and share the top and base lines. The spine has no rounded cap, so its head lines up with the boards. Front and back have smoothly rounded fore corners with no marks on the face (the turn-in folds show only on edges, not on a cover seen face-on), one smooth bend from the spine into the board (highlight on the bend, a gentle hinge shade); on the front the photo starts 4.1 % from the spine edge, where she marked it (the rest of the print is unchanged), and the light and shade by the spine copy her photo of the printed book (2026-09-28), measured against the title (1 % of the width = 8 px on the photo): no dark line at the edge (removed at her request), a highlight (1.1-1.5 %), a valley (deepest at 2.9 %), a thin light line (3.4 %), a second shallower valley (4.2 %), flat board from 5.6 %; the light falls on the spine's edge next to the front. The spine (`cover-spine.jpg`, rebuilt at 10 px/mm from the print file) has the same placement as the back: 96.6 %, lettering starting 14.6 mm below the head, so it has a top margin and reads clearly. The back cover is unchanged and light catching the board edge; soft grey shadows as on the spreads.
- **Back cover (2026-09-28):** laid out as printed, not as cut at the fold marks. On the printed book the design sits on the board with margins: the painting about 8.8 mm from the fore edge and 14.6 mm from the head, the whole back at 96.6 % (measured from her photo of the printed back). `cover-back.jpg` is rebuilt that way from the print file; in `omslag_34_18.pdf` the painting starts right at the panel edge, which left no margin on the left and top.
- **Work-list thumbnail (since 2026-09-28):** one hardcover lying face up, seen almost from above, thickness showing on the right (fore edge) and bottom (tail); references in Notion *For Portfolio* → "Book thumbnail: one book, lying face up" and "Book render: hinge shadow and corner turn-ins". Rendered offline in three.js ([`tools/book-render/render.html`](tools/book-render/render.html)), not CSS. The cover texture is the print file itself (`omslag_34_18.pdf` at 10 px/mm → `tools/book-render/cover-wrap.jpg`, InDesign frame hairlines removed), laid on the case by arc length at the print measures: front 307.4–517.4 mm, a 10 mm hinge, the 34 mm spine; past the fore edge and the head and tail the 18 mm turn-in continues, so the cover art wraps round the board edge instead of stopping at it. Case: 2.8 mm boards with rounded edges and corners, 3 mm squares, a wide soft hinge groove, a rounded spine; fore corners rounded in plan (2.6 mm) and a little thicker where the turn-ins overlap, with a diagonal fold across the board edge and a mitre inside; a slightly concave page block with fine page lines; matte laminate grain. The book rests on the table (no gap). The camera looks straight down, so the book stays a true rectangle; the frame is shifted like a shift lens, and the offset camera position still shows the fore edge and the tail. Light: a large softbox on the right plus open sky, 128 passes with the light moved across that area and averaged, so the shadow falls left and fades out smoothly into the ground; shadows are dark grey (#4a4a46), not black, with only a soft contact shade and no dark line along the edges; light bounced from the pale table onto the edges that face down (references in Notion → "Book render: thick corner and natural soft shadows"). Output `assets/work/book/book-mockup.webp`, 1600 × 1200, transparent, rendered at 2400 × 1800 and downscaled (3200 × 2400 with 128 passes runs out of GPU memory in the headless browser). To re-render: `npm install` in the tool folder, serve the repo root, open `/tools/book-render/render.html?w=2400&h=1800`, save the canvas (`decode.py`, `crops.py` help check details).
- **Spreads:** each spread sits on the white cover board, which shows around the pages as the square. Page edges stack at the outer sides and the tail, thicker on the side that holds more pages (left share = first page ÷ 432); they read through light and shade, lighter by the page and a little deeper toward the board, with the leaves only hinted, not drawn as lines. The pages curve down into a sewn gutter: the top and bottom edges dip toward the spine, the gutter shade is soft, wide and light grey, with a soft crease shade instead of a drawn line: blurred so it has no hard edge and melts into the white, slightly wavy, a little denser at the stitches of the sewn signatures and more diffuse between them (photo of the printed spread, 2026-09-28) (as on the photo of the printed spread, 2026-09-28), a little stronger on the right page, which faces away from the light. The board has rounded corners with light catching its edge, and at each of the four corners the turn-in shows as a diagonal fold (a thin shade with a light edge beside it); the standing cover and the back cover have the same rounded fore corners.

## Spreads (her selection)
Rendered from the print PDF (trim box, 420 × 297 mm) at 3600 px wide, about 218 dpi, so the text stays sharp on high-density screens (2026-09-28): `assets/work/book/spread-LLL-RRR-3600.webp` and a 1800 px version for smaller screens (`-1800.webp`), served with `srcset`. The 150 dpi JPGs they replace made the body text soft. In the print file, PDF page *n* holds book pages 2(*n* − 2) and 2(*n* − 2) + 1.

| Pages | What is on it |
|---|---|
| 2–3 | Title page and colophon, opposite portraits |
| 10–11 | Family photographs and the foreword (*Forord*) |
| 24–25 | Running text with a map of the area |
| 42–43 | Generation II, archive photographs |
| 196–197 | Houses in Stamsund, archive photographs |
| 286–287 | A portrait opposite a chapter of text |
| 324–325 | Two portraits, one per page |
| 416–417 | The list of sources (*Kilder*) |

## Standards (WCAG 2.2 AA)
- 1.1.1: every spread has alt text naming its pages and content; the 3D mockup has one text alternative for the whole book.
- 1.4.10: spreads scale to the screen width; at phone width they stay whole and are not cropped.
- The book's own pages are images of print, so their small type is not live text; that is accepted for a print showcase, and the page copy around them carries the information.
- Motion: the mockup does not animate on its own; it tilts slightly under the pointer and stays still under `prefers-reduced-motion`.

## Consent
The spreads show family photographs and names of private people. **Before the site is public, confirm with Amund Gulsvik that these spreads may be shown.**

## End of the page
**Back to all work** (the last page of the list; every other page ends with View next work). Her request, 2026-10-20.
