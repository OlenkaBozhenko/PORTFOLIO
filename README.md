# PORTFOLIO — Olena Bozhenko, Senior Product Designer

Personal portfolio of **Olena Bozhenko**, a senior product designer based in Oslo who designs B2B and B2C products and crowdfunding platforms end to end: research and user interviews, prototypes, design systems and analytics, with AI tools built into the work.

**Live site →** https://olenkabozhenko.github.io/PORTFOLIO/
**Resume (PDF) →** [assets/Olena-Bozhenko-Resume.pdf](assets/Olena-Bozhenko-Resume.pdf)

## Case studies
| Case | What it is | Page |
|---|---|---|
| Warmy | Email deliverability platform with an AI agent (B2B SaaS, 2021 – present) | [Warmy.html](https://olenkabozhenko.github.io/PORTFOLIO/Warmy.html) |
| AnyBiz | AI sales platform that finds leads and books meetings (B2B, AI SaaS, 2021 – present) | [AnyBiz.html](https://olenkabozhenko.github.io/PORTFOLIO/AnyBiz.html) |
| Sport Guardian | Crowdfunding that keeps every child in sport (B2B, B2C, 2024) | [SportGuardian.html](https://olenkabozhenko.github.io/PORTFOLIO/SportGuardian.html) |
| School | Remote learning that works like a social feed (iOS concept, 2020) | [school.html](https://olenkabozhenko.github.io/PORTFOLIO/school.html) |
| Styupan Translation | A mark for an Oslo translation studio (branding, 2023) | [styupan.html](https://olenkabozhenko.github.io/PORTFOLIO/styupan.html) |
| Book | A 432-page family history hardcover (book design, 2023 – 2024) | [book.html](https://olenkabozhenko.github.io/PORTFOLIO/book.html) |

DRON (drone services) is parked for now and comes back later; its landing row is kept in [`tools/dron/parked/`](tools/dron/parked/).

## What is on the landing page
- **Hero** — a large headline the visitor can finish by dropping a phrase into it, surrounded by drifting interface and code blocks (desktop); on phones, the headline alone.
- **Case Studies** — six projects, each with a description and a large preview.
- **About**, **Testimonials**, **Learning** (courses, certificates, conferences) and **Contact** (email, LinkedIn, resume).
- Built mobile first: a burger menu with contacts, swipeable testimonials, layouts reworked for phones on every case page.

## How it is built
- Plain HTML and CSS with a little vanilla JavaScript; no framework and no build step. Hosted on GitHub Pages from the `master` branch; [`index.html`](index.html) opens the landing page.
- Every page is checked against **WCAG 2.2 AA** (contrast, keyboard, target size, reduced motion); the checks and the reasoning are recorded in the `.md` files.

## Files
| File | Role |
|---|---|
| [`Olena Bozhenko.html`](Olena%20Bozhenko.html) | The landing page |
| [`Warmy.html`](Warmy.html), [`AnyBiz.html`](AnyBiz.html), [`SportGuardian.html`](SportGuardian.html), [`school.html`](school.html), [`styupan.html`](styupan.html), [`book.html`](book.html) | Case study pages |
| [`site.md`](site.md) and the case `.md` files ([`warmy.md`](warmy.md), [`anybiz.md`](anybiz.md), [`sportguardian.md`](sportguardian.md), [`school.md`](school.md), [`styupan.md`](styupan.md), [`book.md`](book.md)) | Source of truth for each page: structure, copy, standards |
| [`cv.md`](cv.md) | CV facts, learning, testimonials |
| [`resume.md`](resume.md) → [`resume.html`](resume.html) → [`assets/Olena-Bozhenko-Resume.pdf`](assets/Olena-Bozhenko-Resume.pdf) | Black-and-white one-page resume |
| [`inspiration.md`](inspiration.md) / [`inspiration.html`](inspiration.html) | Visual references and the designer's decisions |
| [`research/market-research.md`](research/market-research.md) | Senior Product Designer job market: Ukraine, Norway, Europe, USA |
| [`CLAUDE.md`](CLAUDE.md) | Project brief and working rules |

## Working rules
- `.md` files are the source of truth; HTML is the display layer and is updated after the `.md`.
- All file contents are in English.
- Every design decision is checked against WCAG 2.2 AA and Apple HIG.
