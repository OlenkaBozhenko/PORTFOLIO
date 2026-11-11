# My impact section: spec

Source of truth for the "My impact" section on the case pages (her brief and calls, 2026-11-10/11). It began as a modal (2026-11-10); on 2026-11-11 she moved it into the page as its own section, after a look at NN/g and Apple HIG guidance on modals, popups and scrolljacking. The early modal mockup is `tools/impact/mockup.html`; the site version is `assets/impact/impact.js`.

## Why

A rejection (2026-11-09) said the cases tell too much about the product and too little about her role: what she found out, what she decided, what changed. The section puts her impact on every case in one place, in one style. Research: [`research/case-study-role-examples.md`](research/case-study-role-examples.md).

## Behaviour (her calls)

- A section of the page, right after the story block that ends with **Solution** (her call 2026-11-11). Nothing pops up or blocks the page.
- **Desktop:** the word MY IMPACT spans the full content width; below it the contributions sit as numbered blocks (01, 02, ...), three to a row, like the "My part" list on Warmy (her call 2026-11-11). No slides. Every title breaks into two lines of about the same length, so the texts below start level across the row (her call 2026-11-11); on phones the titles run on. A case with two contributions shows them in two wider columns (her call 2026-11-11). The gap between the columns is 48 px on desktop, the same as on every numbered list of the site (her call 2026-11-11).
- **Phones (720px and below):** the word on top, then the same numbered blocks one under another; no slider, no dashes (her call 2026-11-11).
- The opening animation plays once, the first time the word scrolls into view (her call 2026-11-11).
- **Buttons:** on desktop the OB-logo button left of the dock, in the project's primary colour, expands on hover or focus to show "My impact", like To the top; on phones one round menu button in place of To the top opens two pills, My impact and To the top. My impact scrolls to the section.
- Accessibility (WCAG 2.2): the word is the section's h2 ("My impact" for screen readers, the drawn letters hidden from them); the contributions are an ordered list; reduced motion shows the word settled, with no animation.

## Look (her calls)

- The word: **MY IMPACT** (her pick of four, 2026-11-10), set in two rows, MY and IMPACT, the second a little taller (1.3 to 1), each row stretched to the full width.
- The letters are drawn for this, in the manner of her OB logo: ultra heavy, circles and rectangles, small round counters, flat tops and bottoms (her call 2026-11-10), small rounded corners (radius 16 on a 100-unit letter, her call 2026-11-10) and narrow slit counters. Stretching a row squeezes or widens the letters (the effect of Resn's "Sculpting Harmony", the BOX block).
- White background, black letters, no coloured stripes (her call).
- Opening animation, after Resn's "Sculpting Harmony" (her call 2026-11-10): the letters rise one by one in a single row; their widths swap twice; the row breaks into lines; the lines settle into MY / IMPACT.

## Slides per case

On the site since 2026-11-10 (her call: "do it for every project, we fix the texts later"). Warmy and AnyBiz come from her texts of 2026-11-09; the others are drafts written from each page's own facts, to be checked by her. The 20% figure on Warmy still needs its source and date.

Built by `assets/impact/impact.js`; each page carries its contributions in a `<script type="application/json" id="impact-data">` block before `</body>`; `after` names the block after which the section is placed (after the story block that holds it) (DRON: `#made`, the How it was made row; Stiupan: `#idea`; Book: `#objective`; the others: `#solution`). DRON's block lives in `tools/dron/build/dron-main.html`.

### Warmy

Order and the third title: her call 2026-11-11 (the "Several audiences" block dropped).

- **20% less load on sales, more time to win clients** Many booked sales calls turned out to be support questions. I redesigned the booking form: it shows what the call will cover and lets people switch to the right consultant. Sales got 20% more time for customers ready to buy.
- **AI email optimization, shipped as an MVP** The business wanted far more than engineering could build in time. I interviewed users to find what mattered most, and we agreed on an MVP that worked for users, the business and engineering.
- **Charts and terms our target audience actually understands** Feedback showed that good-looking charts did not mean users followed the logic behind them. I rebuilt the dashboards around the metrics users rely on.

### AnyBiz

- **Users trust the agent to write for them** Interviews showed that people did not trust an AI to write in their company's name. I designed the interface where users work with the AI agent and instruct it how to write their emails: tone, language, call to action, signature and custom prompts it keeps following. Users set the rules once instead of checking every message.
- **Gaps nobody mentioned, fixed** Session recordings showed where people got stuck, what they searched for and where they expected to set things up. Among other things, I added the missing filters and information, and redesigned the onboarding flow so a new user gets to the first campaign faster.
- **Features users asked for, not the ones we assumed** Before development, I tested new features on prototypes: which tools help, which only clutter the screen, where people look for them and what they call them. We dropped some features before a line of code, built the ones users kept asking for, and renamed things in users' own words.

### DRON

Her brief 2026-11-11: 01 shows she built the design system for Claude Code, and that AI tools can build any product on brand when it has a clear system made for it; 02 is her text; 03 is the handoff, written from `handoff/README.md` in the DRON repo.

- **A design system Claude Code builds from** I designed DRON's design system to be read by an AI agent as well as by people: 372 tokens, 53 component files and 13 patterns, written as code with documented rules, light and dark themes, and every colour pair checked against WCAG AA. Claude Code reuses what exists instead of guessing. With a system like this behind it, an AI tool can build any product and keep it true to the brand.
- **Written rules, a unified voice** A product created through numerous sessions utilising artificial intelligence loses its coherence if the rules are not set out in writing. Every string comes from a single file, ensuring that the user sees a consistent tone and terminology across 134 screens, whilst anyone on the team can add new features that sound the same.
- **A handoff anyone can pick up** Released as v1.0.0, the handoff holds everything a developer needs: a map of every screen, how each flow behaves, accessibility as built, every string with its key, the design system, and what ships versus what is reference. It runs with one command from a fresh clone, so a developer can join at any stage and keep building without asking me.

### Sport Guardian

- **A donation in four choices** Sport Guardian asks people to give to a club's children. I designed the donation as four choices: a private person or a company, once or every month, the amount, then card or Vipps.
- **Clubs publish on their own** Clubs had no simple way to ask their community for help. I designed a builder that lets a club publish a campaign without help, and an admin panel with donors, refunds and statistics.
- **A campaign page that shows who helps** I designed the campaign page around the countdown, the amount raised and the people behind it, so a visitor sees a club with a community, not a request for money.

### School

- **Learning that works like a social network** During the quarantine, lessons moved online and young pupils quickly lost interest. I designed an app where pupils and teachers share one space, like a social network.
- **Challenges pupils set for each other** I designed challenges: small goals that run for a set time and can come from anyone in the class, so pupils build good habits together.
- **Teachers keep control** Lessons and homework come from the teacher, and teachers control the content, so the social side never takes over the learning.

### Stiupan

Her brief 2026-11-11: show that brand design is more than drawing a logo; it gives the company a base to build recognition and digital products on. Grounded in Jenni Romaniuk, *Building Distinctive Brand Assets* (Oxford University Press, 2018): a logo is a distinctive asset whose job is to trigger the brand name, and it works once it is both famous and unique, learnt through repetition; and Alina Wheeler, *Designing Brand Identity*: the logo is the fastest form of brand communication, and identity is a system applied across touchpoints, favicons and websites among them.

- **A mark people learn to recognise** A logo is a brand's fastest signal. I designed Stiupan's as a distinctive asset: the initials S and T on an open book, so it says language and text at a glance, belongs only to Stiupan and still reads at favicon size. Seen again and again, it lets clients recognise the company before they read its name.
- **One mark for every product** The S is cut out of the solid left page, so the mark takes the colour of any ground: light or dark, one colour or two, print or screen. The company can build its website, documents and digital products on it without redrawing the logo, and every new piece adds to the same recognition.

The owner's quote was dropped from this section (her call 2026-11-11): it is already on the page, and the section is about her own work.

### Book

- **300+ photos, one calm read** I laid out a long family history with more than 300 archive photographs and maps, so it reads calmly from the title page to the list of sources.
- **From the layout to print** I designed the cover and the layout and prepared the print files for LOS DIGITAL AS.

The author's quote was dropped from this section (her call 2026-11-11): it is already on the page, and the section is about her own work.

On Book only (her call 2026-11-11), the titles stay on one line and the texts wrap in balanced lines (`"titles":"one"` in its data); the other cases keep two-line titles.
