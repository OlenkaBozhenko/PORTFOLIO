# PORTFOLIO — Project Brief

**Product:** a personal portfolio website for a **Senior Product Designer** job search.
**Platform:** web, mobile-first and fully responsive (phone → tablet → desktop).
**Standards:** WCAG 2.2 AA for the whole site; performance and mobile layout are treated as evidence of craft (see research §4).

## Working process

1. Research → `research/` (done 2026-09-24: [`research/market-research.md`](research/market-research.md))
   - CV and testimonials → [`cv.md`](cv.md); visual references → [`inspiration.md`](inspiration.md)
2. Positioning and content (target market, case selection, copy)
3. Structure / wireframes
4. Visual design
5. Build
6. Publish

## Content rules

- `.md` files are the single source of truth; HTML is the display layer, generated from `.md`.
- All file contents are written in English.
- Every figure carries its source and date; estimates are labelled as estimates.

## Where the work stands (2026-09-25)

**Built:** the Warmy case page [`Warmy.html`](Warmy.html) (source [`warmy.md`](warmy.md), 2026-10-20); the landing page [`Olena Bozhenko.html`](Olena%20Bozhenko.html) (source [`site.md`](site.md)); a black-and-white one-page resume PDF ([`resume.md`](resume.md) → [`resume.html`](resume.html) → `assets/Olena-Bozhenko-Resume.pdf`); the market research; the inspiration board. Open the landing locally at `file:///C:/Users/Olena/PORTFOLIO/Olena%20Bozhenko.html#top`.

**Rules she has set:**
- The site is white on every page (inspiration D1). The resume is black and white only.
- Commit every change locally; **push to GitHub only when she says so, each time.** The repo is private: https://github.com/OlenkaBozhenko/PORTFOLIO
- **No Claude Artifacts for the site** — it is a plain HTML page. Public hosting (GitHub Pages needs a public repo on her plan; Vercel works with a private one) waits for her choice.
- Every reference she sends is also added, with its screenshot, to the Notion page [For Portfolio](https://app.notion.com/p/For-Portfolio-39e64a1387ca80e98e48d4e879cc2649).

**Open questions for her:**
1. Sport Guardian (Idretsfader): page built 2026-10-13 ([`sportguardian.md`](sportguardian.md)); confirm her role (UX, UI) (year 2024 and client Scale Group AS, her answers 2026-10-13/14). School: confirm the year (2020 is an estimate from the screens) and the case copy in [`school.md`](school.md).
2. Scale Development AS: what she did there, for the resume.
3. AnyBiz timeline on the site: one continuous role (Aug 2021 – present) or two periods.
4. Typeface: Inter Tight is a stand-in for Aeonik / Neue Haas Grotesk.
5. Tor Martin Olsen's testimonial is a DRAFT on the landing — needs his approval before the site goes public; referee contacts in `cv.md` and the phone in the resume PDF need a decision before the repo is public.
6. `assets/music.mp3` is missing, so the Play / Pause music button stays hidden.
