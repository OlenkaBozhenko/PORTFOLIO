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
- **Work-list thumbnail:** three hardcover copies fanned in a stack, seen from above at an angle, filling about three quarters of the card height. Each copy shows the board thickness (2.5 mm) above and below the page block, the 3 mm square where the boards overhang the pages, the rounded spine and the hinge groove; each copy casts a contact shadow on the one below, and the stack casts a long soft shadow to the left.
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
