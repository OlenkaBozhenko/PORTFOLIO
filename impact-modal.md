# My impact modal: spec

Source of truth for the "My impact" modal on the case pages (her brief and calls, 2026-11-10). The mockup is `tools/impact/mockup.html`; the site version is `assets/impact/impact.js` (2026-11-10).

## Why

A rejection (2026-11-09) said the cases tell too much about the product and too little about her role: what she found out, what she decided, what changed. The modal puts her impact on every case in one place, in one style. Research: [`research/case-study-role-examples.md`](research/case-study-role-examples.md).

## Behaviour (her calls)

- Opens by itself once the reader has scrolled past **Solution**.
- Once closed, it never opens by itself again on that page (remembered in the browser); it folds into a button.
- **Desktop:** the button carries her OB logo, sits left of the bottom dock, in the project's primary colour. It is a circle that expands on hover or focus to show "My impact", like To the top (her call 2026-11-11).
- **Phones:** one round button, centred, with a menu icon, in place of To the top; it opens two pills: My impact (OB logo) and To the top.
- **Slides:** one per contribution, a title and a short text; they change as the reader scrolls on desktop; on phones only a left or right swipe changes them, and the text slides sideways (her call 2026-11-11). The dashes at the bottom only show the position; they are not buttons. A case with one contribution has no slides and no dashes.
- Accessibility (WCAG 2.2): focus moves into the modal, Esc and the close button close it, the page behind is inert, focus returns to the button on close; the arrow keys change slides too (keyboard users cannot scroll-flip); reduced motion shows the modal settled, with no animation.

## Look (her calls)

- The word: **MY IMPACT** (her pick of four, 2026-11-10), set in rows MY / IM / PACT.
- The letters are drawn for this, in the manner of her OB logo: ultra heavy, circles and rectangles, small round counters, flat tops and bottoms (her call 2026-11-10: the round-bottomed P, A, C of the first draft looked wrong), small rounded corners (radius 16 on a 100-unit letter, her call 2026-11-10: the first radius was too big) and narrow slit counters. Each row is stretched to fill the panel width, so narrow letters squeeze and the round counters turn into slits (the effect of Resn's "Sculpting Harmony", the BOX block).
- Desktop: the middle row (IM) is taller than MY and PACT (1.45 to 1), and the slide title starts level with its top (her call 2026-11-10). Desktop titles break into two balanced lines, never one long line (her call 2026-11-10).
- White background, black letters. **No coloured stripes between the rows** (her call).
- Phones: full screen, white; the letters sit at the top **inside the screen edges** (her call: the bleed on her sketch was only a render that did not fit); title and text below; the close button and the dashes at the bottom. The phone close button is a black circle with a white cross (her call 2026-11-10).
- Opening animation, after Resn's "Sculpting Harmony" (her call 2026-11-10): the letters rise one by one in a single row across the modal; their widths swap twice (one letter grows as the others squeeze); the row breaks into lines; the lines settle into the left panel (phones: the top band). On each slide change the letters shift their widths a little, so the word breathes with the slides.

## Slides per case

On the site since 2026-11-10 (her call: "do it for every project, we fix the texts later"). Warmy and AnyBiz come from her texts of 2026-11-09; the others are drafts written from each page's own facts, to be checked by her. The 20% figure on Warmy still needs its source and date.

Built by `assets/impact/impact.js`; each page carries its slides in a `<script type="application/json" id="impact-data">` block before `</body>`; `after` names the block the reader scrolls past before it opens (DRON: `#made`, the How it was made row; Stiupan: `#idea`; Book: `#objective`; the others: `#solution`). DRON's block lives in `tools/dron/build/dron-main.html`.

### Warmy

- **AI email optimization, shipped as an MVP** The business wanted far more than engineering could build in time. I interviewed users to find what mattered most, and we agreed on an MVP that worked for users, the business and engineering.
- **Charts people actually understand** Feedback showed that good-looking charts did not mean users followed the logic behind them. I rebuilt the dashboards around the metrics users rely on.
- **20% more sales time for buyers** Many booked sales calls turned out to be support questions. I redesigned the booking form: it shows what the call will cover and lets people switch to the right consultant. Sales got 20% more time for customers ready to buy.
- **Several audiences, not one** A customer journey map and an audit of product analytics showed that Warmy serves several distinct groups, each relying on different features. Every team got a clear picture of how to work with each group.

### AnyBiz

- **Users trust the agent to write for them** Interviews showed that people did not trust an AI to write in their company's name. I designed Instructions: tone, language, call to action, signature and custom prompts the agent keeps following. Users set the rules once instead of checking every message.
- **Gaps nobody mentioned, fixed** Session recordings showed where people got stuck, what they searched for and where they expected to set things up. I added the missing filters and information, and redesigned onboarding so a new user gets to the first campaign fast.
- **Features users asked for, not the ones we assumed** Before development, I tested new features on prototypes: which tools help, which only clutter the screen, where people look for them and what they call them. We dropped some features before a line of code, built the ones users kept asking for, and renamed things in users' own words.

### DRON

- **The design system is the brief** With AI tools, the design system is the brief the AI works from. I built DRON's first: 372 tokens, 53 component files and 13 patterns, light and dark, every colour pair checked against WCAG AA. Every screen the agents built follows it.
- **Written rules, one voice** A product written by many AI sessions drifts unless the rules are written down. One voice file decides every string, so the client hears one calm voice on 134 screens, and anyone on the team can add a feature that fits.

### Sport Guardian

- **A donation in four choices** Sport Guardian asks people to give to a club's children. I designed the donation as four choices: a private person or a company, once or every month, the amount, then card or Vipps.
- **Clubs publish on their own** Clubs had no simple way to ask their community for help. I designed a builder that lets a club publish a campaign without help, and an admin panel with donors, refunds and statistics.
- **A campaign page that shows who helps** I designed the campaign page around the countdown, the amount raised and the people behind it, so a visitor sees a club with a community, not a request for money.

### School

- **Learning that works like a social network** During the quarantine, lessons moved to Viber and Zoom and young pupils quickly lost interest. I designed an app where pupils and teachers share one space, like a social network.
- **Challenges pupils set for each other** I designed challenges: small goals that run for a set time and can come from anyone in the class, so pupils build good habits together.
- **Teachers keep control** Lessons and homework come from the teacher, and teachers control the content, so the social side never takes over the learning.

### Stiupan

- **S and T on an open book** I drew the initials S and T on the two pages of an open book, so the mark says language and text at a glance and still reads at favicon size.
- **One mark on light and dark** The S is cut out of the solid left page, so it always takes the colour of the ground. The mark swaps cleanly between light and dark, in one colour or two.
- **The owner's word** “She played a decisive role in creating the company's logo.” Maiia Stiupan, owner of Stiupan Translations, in her reference letter (translated).

### Book

- **300+ photos, one calm read** I laid out a long family history with more than 300 archive photographs and maps, so it reads calmly from the title page to the list of sources.
- **From the layout to print** I designed the cover and the layout and prepared the book for print with LOS DIGITAL AS.
- **The author's word** “She has done the work on the book to our great satisfaction and with great accuracy.” Amund Gulsvik, author (translated from Norwegian).
