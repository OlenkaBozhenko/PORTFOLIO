# Styupan Translation — project page content

**Source of truth for** [`styupan.html`](styupan.html), the page that opens from the **Styupan Translation** row of the landing's work list (first build 2026-09-29).
Layout follows [`book.md`](book.md): the header (back link, eyebrow, headline, meta row), a large first image on a pale stage, then About / Objective and the brand pieces one after another. References she sent on 2026-09-29 are in Notion *For Portfolio* → "Styupan brand page".

---

## Facts
| | |
|---|---|
| Client | Stiupan Translations ENK, Oslo |
| What they do | A multilingual translation studio: translation, proofreading, localisation, copywriting |
| Languages | Norwegian, English, Ukrainian, Russian, German, Polish |
| Tagline | "Lost words found here" |
| Size | 2–10 employees |
| Website | nortranslations.no |
| Her role | Logo and brand identity, then UI/UX and book design for the same client |
| Year | 2023 – 2024 |
| Typeface | Crimson Text (Bold for the name, Regular in capitals for OVERSETTELSESBURÅ) |

Sources: Instagram [@nortranslations](https://www.instagram.com/nortranslations/) bio (services, languages, Oslo, website) and the LinkedIn company page [stiupan-translations](https://www.linkedin.com/company/stiupan-translations/) (tagline, size, Oslo), both read 2026-09-29; her Figma file MY-PROJECTS (logo, colours, typeface); Maiia Stiupan's reference letter (`cv.md`).

## Page copy
- **Eyebrow:** Brand mark
- **Headline:** A mark for an Oslo translation studio.
- **Meta row:** Role — Logo, brand identity · Year — 2023 – 2024 · Client — Stiupan Translations ENK, Oslo · Typeface — Crimson Text
- **About:** Stiupan Translations is a multilingual translation studio in Oslo. The small team translates, proofreads, localises and writes copy in Norwegian, English, Ukrainian, Russian, German and Polish, under the line "Lost words found here".
- **Objective** *(draft — to confirm with her)*: a mark that says "language and text" at a glance, reads at favicon size and in print, and works in one colour as well as two.
- **Idea:** the initials S and T sit on the two pages of an open book. The left page is solid and the S is cut out of it; the right page is open and carries the T. Because the S is always the colour of the ground, the mark swaps cleanly between light and dark.
- **Quote:** "She played a decisive role in creating the company's logo." — Maiia Stiupan, owner (translated from her reference letter; consent to publish her name still to confirm, see `cv.md`).

## Sections, in order
1. **Intro** — her Figma frame 462:2703 (the purple cover with the round logo, the name, OVERSETTELSESBURÅ and scattered letters), exported at 2×. No grey stage (2026-09-29): the purple band fills the full content width and the grey strip below it is dropped, so the round logo (Figma 462:2742, exported on its own and completed at the bottom, where the frame had clipped it) hangs below the purple edge onto the white page. Transparent WebP, 3072 × 970: `assets/work/styupan/intro-3072.webp` + `intro-1536.webp`.
2. **About / Objective / Idea / Quote.**
3. **Construction** — the mark on a construction grid, built in SVG from the logo vectors (Figma 881:83892, 169 × 127 units). Guides follow the real geometry: the outer box, the spine at 84.5, the right page 84.5–153.6 × 15–112, the S and T boxes, cap line 37 and baselines 85 / 90.2, the two page-top arcs, each a circle of radius 85.3 through the page corners, and two more circles of the same radius below the book (centres at y 201.1, the top arcs shifted down 115.8) that draw the page bottoms (added 2026-09-29). Yellow mark on the purple ground, dashed light guides, a large faint copy of the mark behind (references: Bexel, RR and octopus grids).
4. **Colour and type** — Purple #3C1A5B (RGB 60, 26, 91), Yellow #FFF748 (RGB 255, 247, 72), Paper #F5F5F5 (RGB 245, 245, 245), with CMYK as a plain RGB-to-CMYK conversion, marked as an estimate (Purple 34 71 0 64, Yellow 0 3 72 0, Paper 0 0 0 4; not a print-proofed profile); the Crimson Text specimen, laid out as in her reference (a close-up of an open white book with a quote beside it, 2026-09-29): a rendered open book fills the tile, a large purple "Aa" sits on the left, the name, OVERSETTELSESBURÅ and a Norwegian line on the right, the font name small below. The book is a three.js render, no stock photo ([`tools/book-render/open-book.html`](tools/book-render/open-book.html)): 46 curved sheets per side that rise from the gutter and fan out, a ribbon bookmark, soft light averaged over 96 passes, the table fading to white; `assets/work/styupan/type-book-2400.webp` + `-1200.webp`.
5. **On light and dark** — the lockup (mark + name + OVERSETTELSESBURÅ) on Paper and on Purple, then the round seals (Figma 882:83893 purple, 882:83894 yellow): `seal-purple.svg` on Paper, `seal-yellow.svg` on Purple. In the yellow seal the S is purple, the colour of the ground (2026-09-29).
6. **Signage** — the office sign, as in her Seraj Law reference. *Waiting for her decision on the image* (a photo she provides, or a rendered mockup).
7. **In use** — the folder photo, her Figma frame 881:83891, 2× export scaled to `folder-2400.webp` + `folder-1200.webp`.
8. **Stationery** — letterhead, business cards and envelope laid out flat on a dark ground (reference: broot). Built in HTML and CSS from the brand; names and contacts are placeholders, not real people. Letterhead (2026-09-29): the footer divider is purple; a made-up handwritten signature (an SVG scribble, not a real person's) to the right of the sign-off lines, on a layer under the purple round seal (about 21 % of the letterhead width), which is stamped partly over it, where a Norwegian company stamp goes. Envelope (2026-09-29): yellow ground, the lockup and the stripe in purple; OVERSETTELSESBURÅ on it in Crimson Text SemiBold so it reads at that size. Business card back (2026-09-29): purple ground, all text in bold yellow. Layout after her reference (a white mockup card, 2026-09-29): across the top, the full lockup (mark, Stiupan Translations, OVERSETTELSESBURÅ), as in the brand lockup she sent; the name (larger, Crimson Text) and title left-aligned low on the card, close above the contact lines (city, website), no divider.
9. **Badge and metro** (added 2026-09-29, her request) — two squares side by side, then one wide block, all built in HTML, CSS and SVG from the brand:
   - *Badge on the lanyard* (Paper): a purple staff badge on a purple lanyard printed "STIUPAN TRANSLATIONS · LOST WORDS FOUND HERE" in yellow; on the badge the yellow mark, the name, OVERSETTELSESBURÅ, a placeholder name and Oversetter.
   - *Lanyard close-up* (Yellow): the purple strap across the square with the yellow mark, the name and the tagline.
   - *Metro billboard*: a concrete underpass with a lit frame holding two posters, laid out after the broot subway reference (Notion *For Portfolio* → "Styupan brand page", images 35–36). Left poster purple, after her cover (Figma 462:2703): scattered letters, name, OVERSETTELSESBURÅ, the round yellow logo, a line about the six languages. Right poster yellow: the purple lockup over a purple bar, "Lost words found here", the yellow mark on a purple panel, the languages and the website. A mockup, not a real campaign.

## Accessibility
- Each image has a text alternative; the construction grid and stationery have one description each.
- Yellow #FFF748 on purple #3C1A5B: 12.5 : 1. Purple on Paper: 12.9 : 1. Yellow on Paper fails (1.03 : 1), so the yellow seal is shown only on purple.
