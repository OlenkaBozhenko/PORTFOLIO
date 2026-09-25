# Inspiration — portfolio site direction

**Source of truth for visual references.** Rendered at [`inspiration.html`](inspiration.html).
Screenshots live in [`inspiration/`](inspiration/) and are mirrored to the Notion page
[For Portfolio](https://app.notion.com/p/For-Portfolio-39e64a1387ca80e98e48d4e879cc2649).
New references are added here first, then to the HTML and to Notion.

---

## 1. Decisions set by the designer (2026-09-25)

| # | Decision |
|---|---|
| D1 | **The site is white.** Every page, in every case. |
| D2 | **Every project opens as its own page.** |
| D3 | **Project list:** AnyBiz · Warmy · Idretsfader · Book · Maya logo · Styupan Translation · **School** (personal) · **DRON** (personal). |
| D4 | **Each project in the list shows:** name, short description, **my role on the project**, a large image, and a way to open the work. |
| D5 | **Previews are large images on a background, not device mockups.** |
| D6 | **About page** follows Josh Mateo's: photo, bio, a dated journey (date + description on the right), personal qualities at the end — **plus testimonials from previous employers and clients, with their name and contacts.** |
| D7 | **Resume** opens as a classic white PDF, like Josh Mateo's. |
| D8 | **Typeface direction:** Aeonik Regular, Neue Haas Grotesk, or something close. |
| D9 | **Hero:** a large headline with animated interface elements drawn in outline, like page-grid.com. |

---

## 2. References by page

### 2.1 Home — hero
**[page-grid.com](https://page-grid.com/)** · screenshot `08-page-grid-hero.png`
- What she likes: the very large headline set in a tight grotesk, surrounded by interface elements (Image, Slider, Group, Navigation, Button, Code, Rich Text, Video) drawn as outlined boxes with small blue labels, which move.
- To borrow: the headline scale and the outlined, labelled UI blocks — for a product designer they read as "components on a canvas".

### 2.2 Home — work list
**[karoliskosas.com](https://karoliskosas.com/)** · `01-karoliskosas-work-list.png`, `02-karoliskosas-role-results.png`
- A fully white site. Each project: "Name — descriptor" as a large title, a short paragraph, one black pill button, the visual to the right.
- The case intro is one large statement sentence, then two columns: **My role** (list) and **Results** (list).
- To borrow: the whiteness, "Name — descriptor" titles, the My role / Results pair. Not to borrow: the device mockups (D5).

**[rmd-studio.com](https://rmd-studio.com/)** · `03-rmd-studio-work-list.png`
- Each row: title on the left in two lines, an underlined **View project** link at the bottom of the text column, a large image on the right at the same height.
- To borrow: the row structure — text column + large image, the link anchored at the bottom with a full-width rule.

### 2.3 Project page
**[reinostudio.com.br/works/berrics](https://reinostudio.com.br/works/berrics/)** · `04-reino-berrics-hero.png`, `05-reino-berrics-about-objective.png`, `06-reino-berrics-text-image.png`
- Small project name above a very large statement headline; one meta row (*Deliverables* · *Location*) in italic labels + bold values; a large image that starts inside the header band and runs past it.
- Then label-left / text-right sections: **About**, **Objective**.
- Then short paragraphs followed by images at text width, generous white space.
- To borrow: the order — name → statement → meta row → image → About / Objective → story. For her, the meta row becomes **Role · Year · Platform · Team**.
- Note: the Berrics header band is dark charcoal, which conflicts with D1 (white). The structure transfers; the dark band is an open question (§4).

### 2.4 SaaS projects
**[ramos-app.webflow.io/#tools](https://ramos-app.webflow.io/#tools)** · `07-ramos-saas-cards.png`
- Real UI fragments (metric cards, a chart, a yellow highlight) floating on a pale panel with a faint grid, a short heading and two lines of text beneath each panel.
- To borrow: showing SaaS work as live UI pieces on a gridded panel instead of whole screenshots — for AnyBiz, Warmy and similar.

### 2.5 About
**[joshmateo.com/about.html](https://joshmateo.com/about.html)**
- Photo, bio, a journey list with the date and description on the right, personal qualities at the end.
- Her addition: a **testimonials** block — quote, name, role, company, contact.

### 2.6 Resume
**[Josh Mateo — Resume PDF](https://joshmateo.com/media/JoshMateo-Resume.pdf)**
- A classic white one-page PDF that opens in the browser.

### 2.7 Book project — presenting a printed book (added 2026-09-26)
**[Ashwini Chacko — Architecture Portfolio 2023 (Behance)](https://www.behance.net/gallery/185093841/ARCHITECTURE-PORTFOLIO-2023)** · `09-behance-architecture-portfolio-covers.png`, `10-behance-architecture-portfolio-thumb.png`
- The closed book lies flat on a pale grey ground with a soft shadow; the cover is shown whole, then in context shots.
- Inside, the spreads are shown open, one after another, on the same calm ground.
- To borrow: **the project page for Book** — the cover as a 3D mockup first, then the open spreads in sequence.

**[Fabric Book Cover Mockup (Behance)](https://www.behance.net/gallery/229150887/Fabric-Book-Cover-Mockup)** · `11-behance-fabric-book-stack.png`
- Several identical hardcovers fanned in a stack, seen from above at an angle; the spines repeat the title.
- To borrow: **the Book thumbnail in the work list** — several copies of the same book in a stack.

**Her decisions for Book (2026-09-26):**
- The mockups are built from her own print files: the cover `omslag_34_18.pdf` and the book `Slekstbok_Røtter i Blix_for utskrift_.pdf`.
- Clicking the Book project opens its own page with the spreads **2–3, 10–11, 24–25, 42–43, 196–197, 286–287, 324–325, 416–417**.

---

## 3. Also saved in Notion, not yet annotated
These were already on the Notion page before 2026-09-25. What she likes in each is still to be written down.
- [whereisrussell.com](https://whereisrussell.com/)
- [victorberbel.work/about](https://www.victorberbel.work/about)
- [edwinle.com](https://edwinle.com/)
- [reinostudio.com.br/works](https://reinostudio.com.br/works/)
- [vandslab.com](https://vandslab.com/)
- [proweb.gr](https://www.proweb.gr/)
- [bloom3d.studio](https://www.bloom3d.studio/)

---

## 4. Standards check (WCAG 2.2 AA) — what each liked pattern needs

Every pattern above can be built to conform; none has to be dropped. What each needs:

| Pattern | Criterion | What it requires | Status |
|---|---|---|---|
| White site (D1) | WCAG 1.4.3 Contrast | Body and meta text ≥ 4.5:1 on white. The lightest grey that passes on `#FFFFFF` is `#767676` (4.54:1). | Conforms if greys stay at or below `#767676`. |
| Animated outline hero (D9) | WCAG 2.2.2 Pause, Stop, Hide | Motion that starts automatically and lasts over 5 s needs a visible pause control. | Needs a pause button, or motion that stops within 5 s. |
| | WCAG 2.3.3 (AAA, advisory) / `prefers-reduced-motion` | Honour the OS "reduce motion" setting. | Plan a still version. |
| | WCAG 1.4.3 | The small blue labels (~11px) need 4.5:1 on the page ground. | To measure once the blue is chosen. |
| Large image previews (D5) | WCAG 1.1.1 Non-text content | Each preview needs alt text naming the project and what is shown. | Content task. |
| | WCAG 1.4.3 | Text laid over a photo needs an overlay or has to sit outside the image. | Keep titles outside the image, as in the references. |
| "View project" links | WCAG 2.4.4 Link purpose | Eight identical "View project" links need unique accessible names ("View AnyBiz project"). | Add `aria-label` or visually hidden text. |
| | WCAG 2.5.8 Target size | Link or button ≥ 24 × 24 px. | Conforms at the reference sizes. |
| Dark project header (Berrics) | D1 | Conflicts with "white in every case". | Open — see question below. |
| Testimonials with contacts (D6) | Privacy / GDPR | Publishing a person's name and contact needs their consent. | Ask each referee before publishing. |
| Resume PDF (D7) | PDF/UA, WCAG 1.3.1 | Export as a tagged PDF with real text, not an image. | Export setting. |
| Typeface (D8) | Licence | Aeonik (CoType Foundry) and Neue Haas Grotesk (Commercial Type) need a paid **web** licence. Free, open-licence neo-grotesks in the same family of shapes exist on Google Fonts (for example Inter Tight, Geist, Hanken Grotesk). | Open — hers to choose. |

## 5. Open questions (for the designer, one at a time)
1. Project page header: keep it white like the rest of the site, or allow a dark band as on Berrics?
2. Typeface: buy a web licence for Aeonik / Neue Haas Grotesk, or pick a free open-licence grotesk close to them?
