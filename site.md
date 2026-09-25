# Site — landing page content and structure

**Source of truth for the landing page** `Olena Bozhenko.html` (first build 2026-09-25).
Built from [`inspiration.md`](inspiration.md) (decisions D1–D9) and [`cv.md`](cv.md). Content changes go here first.

---

## Structure
1. **Nav** — name on the left; Work · About · Contact · Resume on the right. Resume opens `assets/Olena-Bozhenko-Resume.pdf` in a new tab (joshmateo.com pattern; source `resume.md` → `resume.html`).
2. **Hero** (D9, page-grid.com) — one large headline; around it, outlined interface blocks with small blue labels that drift slowly. The blocks name what she does: *Design system · Prototype · User interview · Analytics · AI tools · WCAG 2.2*. A visible **Pause motion** button (WCAG 2.2.2); motion is off under `prefers-reduced-motion`.
   - *Revised 2026-09-25 (designer):* the **Pause motion** button becomes a **music** control — **Play** / **Pause** (accessible name "Play music" / "Pause music"). Music never starts on its own; it loops `assets/music.mp3` from the first Play. The button is hidden when the file is missing and, as before, on phones (≤ 900 px).
   - *Standards — a recorded departure, the designer's call:* WCAG 1.4.2 Audio Control passes — sound starts only on Play and stops on Pause. **WCAG 2.2.2 Pause, Stop, Hide now fails:** the blocks drift for longer than 5 s and nothing on the page pauses them; only `prefers-reduced-motion` stops them, which does not satisfy 2.2.2. Options offered were two buttons, or one button for music and motion; she chose music only.
   - *Revised 2026-09-25 (designer):* every design block's label carries the **Figma component icon** (four diamonds) before its name. **Code blocks** join them in the same outlined frames, labelled with a **code icon** `</>`: `<Button variant="primary" />`, a design token from `tokens.css`, and a Claude Code prompt.
   - *Revised 2026-09-25 (designer):* **every block can be dragged** with mouse or touch pen and stays inside the first screen — it cannot be pushed off the edge. A dragged block stops drifting and stays where it was dropped. On phones (≤ 900 px) blocks sit in the page flow and are not draggable, so a finger on a block still scrolls the page.
   - *Standards:* the blocks are decoration (`aria-hidden`), so dragging them carries no information and no function — WCAG 2.5.7 Dragging Movements and 2.1.1 Keyboard apply to functionality, and none is lost for a keyboard or single-pointer user. The label blue `#2B3BD6` on white is 7.78:1, the icons use the same colour.
3. **Work** (D2–D5; karoliskosas.com titles + rmd-studio.com rows) — seven rows. Left: "Name — descriptor", one-paragraph description, meta (Role · Year · Platform), a **View {project} project** link on a full-width rule. Right: a large image on a pale background, no device mockup. SaaS projects show UI fragments on a gridded panel (ramos-app).
4. **About** (D6, joshmateo.com) — photo, short bio, personal qualities, link to the full About page.
5. **Testimonials** (D6) — quote, name, role.
6. **Learning** — courses, certificates, conferences.
7. **Contact** — email (selectable text + Copy), LinkedIn, Behance, Resume (PDF).
8. **Cursor** (designer, 2026-09-25) — on a mouse or trackpad the system pointer is replaced by a **circle** that follows it with a short, smooth lag. 16 px, filled ink `#0E0E0E`. Over a link or button it grows into a **64 px circle** — ink ring, 10 % ink fill, so the link text stays readable through it (revised 2026-09-25: the 44 px ring read as too subtle; the first build used `mix-blend-mode: difference`, which does not blend with the white page canvas and left the circle invisible on white); over a draggable hero block it becomes a 48 px ring with a **drag** label; while dragging it shrinks. Hidden when the pointer leaves the window.
   - Touch screens keep no cursor at all (`hover: none` / `pointer: coarse`): the circle is never drawn there.
   - `prefers-reduced-motion`: the circle follows the pointer exactly, with no lag and no size transition.
   - *Standards:* no WCAG 2.2 criterion covers the pointer's appearance, so this conforms. The only risk is legibility for low-vision users who enlarge the system pointer — their enlarged pointer is hidden too. Keyboard focus is untouched (2.4.7): the focus ring still shows on every control.

## Hero copy
- Eyebrow: Olena Bozhenko · Senior Product Designer · Oslo
- Headline: **I design B2B products from the first interview to the design system.**
- Sub: Senior product designer working remotely with a Ukrainian product team. Research, prototypes, design systems and AI tools, for SaaS used every day.

## Work — in the designer's order (D3)

| # | Title | Description | Role | Year | Platform | Image |
|---|---|---|---|---|---|---|
| 1 | AnyBiz — AI sales outreach | A B2B platform that finds prospects and reaches them by email, LinkedIn and phone, with AI sales agents, drip campaigns and CRM integration. | Product Designer | 2021 – present | Web SaaS | UI fragments: campaign sequence, channels, prospect list *(placeholder until her real screens)* |
| 2 | Warmy — email deliverability | Warms up mailboxes and domains automatically so campaigns land in the inbox, not in spam. | UI/UX Designer | 2021 – present | Web SaaS | UI fragments: mailbox health, inbox placement *(placeholder)* |
| 3 | Idretsfader | *to fill* | *to fill* | *to fill* | *to fill* | *to come* |
| 4 | Book — a family history in print | Layout and design of a 432-page family history book with more than 300 images, printed by LOS DIGITAL AS in 2024. | Book design, layout | 2023 – 2024 | Print | *to come* |
| 5 | Styupan Translation — brand mark | Logo for Stiupan Translations ENK, an Oslo translation and copywriting company, followed by UI/UX and book work over more than a year. | Logo, UI/UX | 2023 – 2024 | Brand | *to come* |
| 6 | School — personal project | *to fill* | *to fill* | *to fill* | *to fill* | *to come* |
| 7 | DRON — drone services, end to end | A drone-as-a-service platform taken from research to a 134-page clickable prototype, a token-based design system, and a WCAG and HIG check on every decision — built with Claude Code. | Research, UX, UI, design system | 2026 | Mobile web | DRON order screen + drone render (`assets/work/dron/`) |

Maya logo removed 2026-09-25 (designer): it is the Styupan Translation mark, already row 5.

Research note, for her to decide: hiring managers spend about 10 s on the homepage, so the strongest cases usually go first. The order above is hers and is kept.

## About (teaser)
- Photo: black-and-white portrait from her Figma file (My projects, node 159:59103), 2026-09-25 — `assets/about/olena-bozhenko.jpg` (720 × 935, served) and `olena-bozhenko-master.jpg` (986 × 1280). Shown uncropped at its own 986:1280 ratio.
- Bio: the About draft in `cv.md`, shortened to two paragraphs.
- Qualities: loves learning · goes to design and AI conferences · precise and accountable (seven years in law) · works in Ukrainian, English and Norwegian.

## Testimonials
Maiia Stiupan (Owner, Stiupan Translations ENK) and Amund Gulsvik (Professor emeritus, University of Bergen) — quotes from `cv.md`. Tor Martin Olsen (Scale Group AS) — **draft quote, not his words yet; needs his approval and job title before launch** (`cv.md`). **Contacts are not shown on the landing; consent to publish names is still to be confirmed.**

## Learning
Anthropic — Subagents, Agent skills (Jun 2026), Claude (Mar 2026) · Warmy — Email deliverability expert (Nov 2025) · AI in Web Design Conf 23 (Jun 2023) · UI UX Online Summit 23 (Feb 2023) · Google — Foundations of UX Design · Awwwards Academy (2020).

## Type and colour
- **Typeface: Inter Tight** (Google Fonts, open licence) as a **stand-in** for Aeonik / Neue Haas Grotesk (D8) until she chooses; swapping it is one line.
- White page (D1). Ink `#0E0E0E` (19.3:1). Muted `#6B6B6B` (5.33:1 on white, passes 1.4.3). Rules `#E6E6E6`. Image wells `#F3F3F1`. Hero label blue `#2B3BD6` (7.78:1 on white, 7.0:1 on the wells). Muted on the wells: 4.8:1. Outline strokes of hero blocks use ink, so they carry 1.4.11 (≥ 3:1) with room to spare.

## Standards applied (WCAG 2.2 AA)
- 2.2.2: **not met since 2026-09-25** — the Pause button now controls music; hero motion stops only under `prefers-reduced-motion` (see Structure → Hero).
- 1.4.2: music starts only on Play and has a Pause.
- 2.4.4: each work link reads "View {project} project".
- 1.1.1: every image has alt text; decorative hero blocks are `aria-hidden`.
- 2.4.7 / 2.4.11: visible focus ring, never hidden by sticky nav.
- 1.4.10: one column at 320 px, no horizontal scroll.
