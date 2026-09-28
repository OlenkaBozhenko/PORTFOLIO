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
- **Eyebrow:** Book
- **Headline:** The history of four Lofoten families, set as a 432-page hardcover.
- **Meta row:** Role — Book design, layout, cover · Year — 2023 – 2024 · Format — A4 hardcover, 432 pages · Printer — LOS DIGITAL AS
- **About:** *Røtter i Blix – Thomesen – Inderberg – Johansen Stamsund* follows the families behind Haldis Blix Gulsvik, who grew up in the fishing village of Stamsund in Lofoten; the families are traced back to the 1500s. The author, Amund Gulsvik, gathered the family stories, archive photographs and maps, and wrote the book for the coming generations who look for their roots. *(From the back-cover text.)*
- **Objective** *(draft — to confirm with her)*: turn a long family history, more than 300 archive photographs and maps, into a book that reads calmly from the title page to the list of sources, and prepare it for print.
- **Quote:** "She has done the work on the book to our great satisfaction and with great accuracy." — Amund Gulsvik, author (translated from his reference letter).

## 3D mockup
Built in CSS from her own cover file, no stock mockup: front, spine and back panels are cut from `omslag_34_18.pdf` at its fold marks — back 43.4–253.4 mm, hinge, spine 263.6–297.4 mm (34 mm), hinge, front 307.4–517.4 mm; height 43.4–340.4 mm (18 mm turn-in). Files in `assets/work/book/`: `cover-front.jpg`, `cover-spine.jpg`, `cover-back.jpg`.
- **Reference:** her photos of the printed book (2026-09-26, Notion *For Portfolio* → "Book mockup: the real hardcover"): matte white case binding, rounded spine with a hinge groove, boards overhanging the page block, a sewn block that curves into the gutter.
- **Light:** from the right on every mockup, so shadows fall to the left onto the ground.
- **Project page:** one closed book, turned three-quarters to show the front and the spine, on a pale well; hinge groove on the front, rounded spine, shadow on the backdrop to the left; the back cover beside it.
- **Work-list thumbnail (since 2026-09-28):** one hardcover lying face up, seen almost from above, thickness showing on the right (fore edge) and bottom (tail); references in Notion *For Portfolio* → "Book thumbnail: one book, lying face up" and "Book render: hinge shadow and corner turn-ins". Rendered offline in three.js ([`tools/book-render/render.html`](tools/book-render/render.html)), not CSS. The cover texture is the print file itself (`omslag_34_18.pdf` at 10 px/mm → `tools/book-render/cover-wrap.jpg`, InDesign frame hairlines removed), laid on the case by arc length at the print measures: front 307.4–517.4 mm, a 10 mm hinge, the 34 mm spine; past the fore edge and the head and tail the 18 mm turn-in continues, so the cover art wraps round the board edge instead of stopping at it. Case: 2.8 mm boards with rounded edges and corners, 3 mm squares, a wide soft hinge groove, a rounded spine; fore corners rounded in plan (2.6 mm) and a little thicker where the turn-ins overlap, with a diagonal fold across the board edge and a mitre inside; a slightly concave page block with fine page lines; matte laminate grain. The book rests on the table (no gap). The camera looks straight down, so the book stays a true rectangle; the frame is shifted like a shift lens, and the offset camera position still shows the fore edge and the tail. Light: a large softbox on the right plus open sky, 128 passes with the light moved across that area and averaged, so the shadow falls left and fades out smoothly into the ground; shadows are dark grey (#4a4a46), not black, with only a soft contact shade and no dark line along the edges; light bounced from the pale table onto the edges that face down (references in Notion → "Book render: thick corner and natural soft shadows"). Output `assets/work/book/book-mockup.webp`, 1600 × 1200, transparent, rendered at 2400 × 1800 and downscaled (3200 × 2400 with 128 passes runs out of GPU memory in the headless browser). To re-render: `npm install` in the tool folder, serve the repo root, open `/tools/book-render/render.html?w=2400&h=1800`, save the canvas (`decode.py`, `crops.py` help check details).
- **Spreads:** each spread sits on the white cover board, which shows around the pages as the square. Page edges stack at the outer sides, thicker on the side that holds more pages (left share = first page ÷ 432). The pages curve down into a sewn gutter: the top and bottom edges dip toward the spine, the crease is dark, and the shadow is wider on the right page, which faces away from the light.

## Spreads (her selection)
Rendered from the print PDF at 150 dpi, 2200 px wide (`assets/work/book/spread-LLL-RRR.jpg`). In the print file, PDF page *n* holds book pages 2(*n* − 2) and 2(*n* − 2) + 1.

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
