# My impact modal: spec

Source of truth for the "My impact" modal on the case pages (her brief and calls, 2026-11-10). Nothing is on the site yet; the mockup is `tools/impact/mockup.html`.

## Why

A rejection (2026-11-09) said the cases tell too much about the product and too little about her role: what she found out, what she decided, what changed. The modal puts her impact on every case in one place, in one style. Research: [`research/case-study-role-examples.md`](research/case-study-role-examples.md).

## Behaviour (her calls)

- Opens by itself once the reader has scrolled past **Solution**.
- Once closed, it never opens by itself again on that page (remembered in the browser); it folds into a button.
- **Desktop:** the button carries her OB logo, sits left of the bottom dock, in the project's primary colour.
- **Phones:** one round button, centred, with a menu icon, in place of To the top; it opens two pills: My impact (OB logo) and To the top.
- **Slides:** one per contribution, a title and a short text; they change as the reader scrolls (swipe on phones). The dashes at the bottom only show the position; they are not buttons. A case with one contribution has no slides and no dashes.
- Accessibility (WCAG 2.2): focus moves into the modal, Esc and the close button close it, the page behind is inert, focus returns to the button on close; the arrow keys change slides too (keyboard users cannot scroll-flip); reduced motion shows the modal settled, with no animation.

## Look (her calls)

- The word: **MY IMPACT** (her pick of four, 2026-11-10), set in rows MY / IM / PACT.
- The letters are drawn for this, in the manner of her OB logo: ultra heavy, circles and rectangles, small round counters, flat tops and bottoms (her call 2026-11-10: the round-bottomed P, A, C of the first draft looked wrong), small rounded corners (radius 16 on a 100-unit letter, her call 2026-11-10: the first radius was too big) and narrow slit counters. Each row is stretched to fill the panel width, so narrow letters squeeze and the round counters turn into slits (the effect of Resn's "Sculpting Harmony", the BOX block).
- White background, black letters. **No coloured stripes between the rows** (her call).
- Phones: full screen, white; the letters sit at the top **inside the screen edges** (her call: the bleed on her sketch was only a render that did not fit); title and text below; the close button and the dashes at the bottom. The phone close button is a black circle with a white cross (her call 2026-11-10).
- Opening animation, after Resn's "Sculpting Harmony" (her call 2026-11-10): the letters rise one by one in a single row across the modal; their widths swap twice (one letter grows as the others squeeze); the row breaks into lines; the lines settle into the left panel (phones: the top band). On each slide change the letters shift their widths a little, so the word breathes with the slides.

## Slides per case

Drafts, from her texts of 2026-11-09; to be agreed before they go live.

- **Warmy:** AI email optimization shipped as an MVP · Charts people actually understand · 20% more sales time for buyers (source and date of the figure still needed) · Several audiences, not one.
- **AnyBiz:** Users trust the agent to write for them · Gaps nobody mentioned in interviews, fixed · Features users asked for, not the ones we assumed.
- **DRON:** The design system as the brief for AI (one slide, so no dashes).
