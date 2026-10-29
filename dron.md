# DRON case page (source for DRON.html)

Built 2026-10-28 on her brief of the same day. Facts come from her DRON repository (`C:\Users\Olena\DRON`, tag `v1.0.0`, 2026-10-27); the file and section are named beside each fact. Every name, price and number on a DRON screen is synthetic demonstration data (`PRODUCT.md` § Evidence on Hand).

Live: product https://olenkabozhenko.github.io/DRON/ · whole process https://olenkabozhenko.github.io/DRON/research.html · demo https://olenkabozhenko.github.io/DRON/demo/ · design system https://olenkabozhenko.github.io/DRON/design-system/docs/overview.html · handoff https://github.com/OlenkaBozhenko/DRON/blob/master/handoff/README.md

## Her brief (2026-10-28)
- The page tells how the product was designed **with AI tools only**, one section per stage, in this order: Research, Target Audience, JTBD, User Flows, Tone of Voice, Wireframes, CJM, Design System, Handoff.
- Portfolio page on white; the product shown on dark cards in the style of the dark desktop UI.
- First screen and description like every case; on the first screen a high-quality drone image on a dark card, and on the right a preview of the dark desktop, **with only the avatar changed** (her answer: another person; the name on the screen follows the photo: Maksym K.).
- Drone photos: new AI photos, high-tech, in the spirit of her Behance reference D-A-L-Y; between the sections too (her answer: new AI photos made in Figma). Made with Figma's image generator (gpt-image), file "DRON portfolio photos" in her team "Alencik's Starter team"; originals stay in that Figma file; local PNG copies in `tools/dron/photos/` are not committed.
- Research: dark, a map with a glass card and a few charts (her references 5-7). Target Audience: dark persona cards with a portrait, quote and a metric card (her references 8-9 and Vexto on Behance). JTBD: explain the format, then two jobs. User Flows: two flows, horizontal, phone screens and the links between them (her reference 4). Tone of Voice: a block with a graphic element, why the rules exist and some rules. Wireframes: desktop and phone, clickable live, for both users. CJM: a description and a schematic picture. Design System: animated cards (Nordlys) laid out as a geometric checkerboard (The Matter of Design), with tokens, components and patterns, and what the system is. Handoff: like her desktop home, the items in the centre and visual blocks on both sides.
- Landing thumbnail: the DRON wordmark from Figma (`YlGWlsWWjKSCxhONMzGG2F`, node 261:79919, "DR N") on lime, with the animated drone of the desktop home in place of the O.

## Header
- Eyebrow: B2C, built with AI tools
- H1: Drone services, from research to handoff, designed with AI.
- Meta: Role Research, UX, UI, design system · Year 2026 · Platform Mobile web, desktop · Tools Claude Code, Figma

## Story
- **About.** DRON is a drone-as-a-service product: a person orders a delivery, an aerial shoot or an inspection, and a certified operator from DRON's own fleet does the work. There are two sides, the client and the operator, on mobile web first and on desktop. (`CLAUDE.md` § Overview, § Business Model, § Platform)
- **Problem.** People who order a drone job have never flown a drone and never will, and the drone itself is what worries them: privacy, safety, noise. Today the work is found on classifieds, where the price hides behind a quote and nobody shows the operator's licence or insurance. (`research/research.md` Findings 1, 3, 5)
- **Solution.** The operator is assigned automatically, and trust is shown, not claimed: verified, licensed and insured on the card before payment, a locked price, live tracking, and a delivery photo or an inspection report at the end. The operator gets jobs that fit one glance, a checklist on site, and is paid 2 hours after the result reaches the client. (`PRODUCT.md` § Positioning; `research/jtbd.md`)
- **How it was made.** Every stage was done with AI tools: Claude Code wrote, built and checked the research, wireframes, design system and handoff (754 of 1,972 commits carry its co-author line; five agents painted the operator side in parallel); Figma was driven from Claude Code through a local bridge; the Impeccable skill audited the design; Playwright checked every page in a browser. (`git log` 2026-10-28; `DESIGN.md` § Overview; `figmosha2/README.md`)

## 01 Research
- Lead: "0 of 8 competitors show a verified operator." Note: at this stage the field was read before drawing anything: who does drone work now, how they speak, what they hide.
- Map card (photo: top-down route): "87%" of residents positive after actually trying drone delivery, while more than half of US respondents had little or no trust before. (`research/research.md` Finding 3; SciTechDaily, Springer Future Business Journal, 2024–2025)
- Chart 1, benchmark of trust mechanics, score out of 35: Bolt/Uber 31, Airbnb 29, Zocdoc 29, TaskRabbit 27, Rover 24. (`ux-research/benchmarks.md` § Evaluation Table)
- Chart 2, trust before and after the first delivery: about 50% (more than half distrust) vs 87% positive. Shown as "more than half" and "87%", no invented exact value.
- Facts: 15 competitors in 3 groups; an 8 × 5 comparison; Kabanchik aerial photo 500–1,500 UAH a session (June 2026); Airbnb +25% bookings from trust signals on the card (`ux-research/benchmarks.md` Sources).
- AI line: Claude Code fetched and read the sources, wrote the comparison and flagged its own fabricated quote, which was withdrawn (`research/research.md` Finding 2).

## 02 Target Audience
- Two primary personas (`research.html` § User Personas; `research/target-audience.md`), desk research, no interviews:
  - **Kateryna, 31**, marketing manager, Kyiv, iPhone, never used a drone. "I want the result. I don't want to figure out drones. What matters is that it's reliable." (translated from Ukrainian). Goals: done fast; operator real, certified, insured before paying; price upfront; live tracking and proof. Metric card: "60–70% drop off at a manual registration form" (`ux-research/user-stories-cjm.md` Stage 2) → Sign in with Diia or BankID.
  - **Andrii, 26**, licensed drone pilot, Kyiv area. "I want to fly and earn. Paperwork and finding clients are not for me." Goals: steady jobs, accept in under 10 seconds, paid automatically. Metric card: "10 s to accept a job" (`research/jtbd.md` RJ-O1; countdown token `--time-10`).
- Portraits are AI-generated stand-ins (the repo's cards use emoji).

## 03 JTBD
- What it is: a job to be done is the progress a person wants to make in a situation, not a feature. Format: **When** [situation], **I want** [motivation], **so that** [result]. (`research/jtbd.md`)
- MJ-1 Client: When I need a result that only a drone can deliver, I want to hand the job to a certified professional without managing anything myself, so that I get the outcome without ever thinking about the drone or the operator.
- MJ-2 Operator: When I have the licence, equipment and capacity to do drone work, I want a steady stream of pre-qualified jobs to reach me without hunting for them, so that I can spend my time flying, not selling.
- Note: 16 jobs and 3 hypothesis jobs; the three that shaped the MVP: confirm the person is real, no void between payment and arrival, get paid without managing it.

## 04 User Flows
Two of the 14 flows (`flows.md`), phone screens from the live demo (dark):
- Client, order a delivery: Find (listings) → Choose the parcel (listings-map) → Details (order-setup) → Review and pay (order-review) → Operator revealed (order-confirmed) → Live tracking (tracking) → Delivered (delivery). Decisions: Drone free? · Payment authorised? · Result as expected? (no → report an issue).
- Operator, take a job and get paid: Jobs (operator-listings) → Offer, 10 s (job-offer) → Brief (job-brief) → Checklist (job-checklist) → Close with a photo (result-upload) → Earnings (wallet) → Withdraw (withdraw-sent). Decisions: Accept in 10 s? (no → offer goes to the next operator) · Able to fly? · Issue in 2 h? (yes → payment held).
- Honest note: the target was 3 taps to order; the build measures 5 with Apple Pay (`sitemap.md` §7.3, 2026-10-20).

## 05 Tone of Voice
- Why: a product written by many hands, and here by many AI sessions, drifts in tone unless the rules are written down; one voice file decides every string, so the client hears one calm, accountable voice on 134 screens. "Trust beats wit, every line." (`voice.md`)
- Five principles, each with a do: Name the outcome, not the drone ("Delivered. Your parcel arrived at 10:07.") · Show the proof, not the adjective ("Verified by DRON · CAA licence · Insured · 214 jobs") · State the price as a fact, before the tap ("Total · locked, no extra fees · ₴180") · Speak the user's words, not the equipment · In trouble, be plain and accountable ("Payment declined. Nothing was taken from your account.").
- Never: "Oops", exclamation marks, emoji in system messages, "successfully", the em dash.

## 06 Wireframes
- 134 phone pages and 135 desktop pages, one page per state (`handoff/counts.md`, 2026-10-27). Started in greyscale, then painted in the "Studio" direction.
- Live, clickable, in the page: switch Client / Operator and Phone / Desktop; frames load the live demo (`/demo/listings.html`, `/demo/operator-listings.html`, `/demo/desktop/listings.html`, `/demo/desktop/operator-listings.html`).

## 07 CJM
- Client journey in four stages, read through Whalen's six minds (`ux-research/user-stories-cjm.md`): Attraction (curiosity, disbelief; risk: unclear value in the first 8 seconds) → Activation (anxiety peaks at choosing an operator; registration form loses 60–70%) → Involvement (anger when there is no way to resolve an issue; no Book again) → Retention (pride, a one-tap share; risk: the deal moves off the platform).
- What changed: choosing an operator was removed (auto-dispatch); trust signals moved to the confirmation screen; Sign in with Diia or BankID; Book again; a resolution flow.

## 08 Design System
- What it is: one stylesheet the product links, with tokens, components and patterns, documented like Apple's HIG; light and dark; every pair measured against WCAG AA (`design-system/docs/overview.html`).
- Numbers (`handoff/counts.md`): 372 tokens, 53 component files, 13 patterns.
- Cards: Colour (Signal Green #9BCF4A, fill only; charcoal #1A1A1A; cream #F7F5F2), Type (SF Pro, ten steps, none below 11 pt), Spacing (base 4) and radius (10, 12, 13, 16, 22, 999), Motion (.12 s, .2 s, .32 s), Button (primary, secondary, tertiary, 44 px), Components (switch, chip, progress rail), Patterns (13), Light and dark.

## 09 Handoff
- Released as v1.0.0 on 2026-10-27; "python serve.py" from a fresh clone. Items (`handoff/README.md`): screen maps (`map.md`), behaviour of each flow (`behavior/`), accessibility as built (`a11y.md`), what ships and what is reference (`code.md`), how to contribute, generated counts, the voice and every string with keys, the design system. What ships: `tokens.css`.

## Next
- Next work: Warmy.

## Revision, her notes 2026-10-28 (second round)
- First screen: one picture, the drone photo and the dark desktop together on the dark map of Kyiv.
- Tools: Claude Code only (Figma removed from the meta).
- Landing row: a short product description like the other rows: "A drone-as-a-service app: order a delivery, an aerial shoot or an inspection, and a certified operator does the job, with the price locked and the drone tracked live."
- Chapter numbers and every "Made with" block removed. Each chapter opens with a picture: a dark schematic in thin lime lines made for that chapter (AI-generated in the Figma file, `assets/work/dron/ch-*.webp`), a DRON drone render as a layer above it (`layer-*.webp`, from the DRON repo), and the chapter's text on a dark card; picture left and right in turn.
- Research: no dark ground; the four-figure facts row removed. Target Audience: no ground; persona and metric cards in a checkerboard. User Flows: no ground; every screen in the dark theme, the light map tiles darkened (listings-map, job-brief, tracking).
- Tone of Voice: more space under the heading; the moving card has the map behind and a drone above.
- Wireframes: no big ground; two dark cards, desktop and phone, both live and dark, starting at the role choice so both sides can be clicked; no switch, no link.
- Design System: the wide card shows type, the narrow one colours.
- Handoff: the side cards hang at different angles on a dashed orbit with lime lines (her references ORBIT and Telemetry).
- Links removed (her call): Open the demo, Open the design system, Open the handoff.

## Revision 3, her notes 2026-10-28
- Chapter pictures redone as high-tech photos in the spirit of the inspection and cargo photos: the drone is in the scene, with thin lime holographic lines for the chapter (radar, two profiles, a path to a check, a route with a decision, a waveform, projected wireframes, a journey line over a valley, an exploded drone on a grid, a case opening into code). The drone layer on top is gone.
- Each picture runs the full width of the text; the chapter text sits on a glass card on the calm side of the photo, like the Market reality card. The thin-line schematics stay inside the photos.
- Deeper shadow under the mockups: the desktop on the first screen and the live frames.

## Revision 4, her notes 2026-10-28
- Target Audience: the person (portrait, quote, name) without a ground, aligned to the bottom; the metric card beside it larger; the rows mirror each other (her references: Card or Vipps, On the street, A prototype, not a picture).
- JTBD: the jobs in the shape of her Warmy "The template" card: the fixed words plain, the parts that change on lime chips.
- First screen tag: "Clickable prototype, phone and desktop".
- Tone of Voice: one AI-generated high-tech picture behind the lines (`voice-art.webp`).
- One typeface as on the rest of her site: Inter Tight everywhere; monospace only for code (file names, commands).
- Wireframes: the desktop frame now opens dark too. The desktop demo ignores `?theme=dark`, so the page stores the demo's own theme choice (`wf-theme` = dark) before loading the frames, only when the visitor has none; this works on the live site, where the demo shares the origin, not from a local file.
- Design System: buttons drawn as the product draws them (primary Signal Green, secondary warm grey, tertiary text, disabled); the numbers larger, spread across the full width, counting up once like the Warmy figures; design-system parts (colour and type atoms, a field molecule, a button) float on the chapter photo.
- Handoff: no ground; cards of different sizes and angles float around the list on a dashed orbit.

## Revision 5, her notes 2026-10-28
- User Flows: phone mockups as on her other cases, sharp 2x screens (750 px), a crisp question mark in the decisions; the native scroll bar replaced by a small Signal Green bar, and on a mouse a green "Drag" circle follows the pointer and the row can be dragged.
- First screen: the caption no longer reads as a button ("The client orders a package delivery", plain text). The desktop mockup plays the client's package delivery flow from the live demo (home, Find a service, Filters with Quadcopter picked and applied, parcel size, details, review, pay, confirmed; `dflow-0..6.webp`); a pointer moves to the next control and taps it with a Signal Green flash (white on Sport Guardian). The card-details step is skipped. Still under reduced motion.
- Target Audience: the metric cards rebuilt as small dark dashboards: a gauge for the 60–70% drop-off, "1 tap" sign-in with bars, a checklist; for the operator the 10 s ring, what one glance shows (demo data), and today's pains.
- JTBD: per person, a text about who they are and their related jobs as chips (AnyBiz challenge layout) beside the job card; the rows mirror.
- Wireframes: no captions; rounded cards; the desktop card as tall as its frame, so it is shorter than the phone.

## Revision 6, her notes 2026-10-28
- Removed: the source note under Target Audience; the dashed base line in the trust chart; the "The green is the payload" photo band; the 3 taps / 5 taps line under the flows; the lines between the voice rules.
- Flows: more room around the decisions (wider links and decision blocks); phone mockups with a gentler corner (frame 30, screen 24) so the screens' top corners are not cut; the live phone frame the same.
- Wireframes: the desktop card full width with its text under it ("On the desktop"); then the phone card with its text at the side on the bottom edge ("Phone first"), as in her Warmy "A prototype, not a picture"; every card with the same 22 px radius.

## Revision 7, her notes 2026-10-28
- Customer Journey Map without the dark ground, as a grid in the site's style after her reference (a customer journey template): rows Phases (dark headers), Actions (chips), Experience (two filled curves: before the fixes in rust, with DRON as designed in green, with callouts and mood faces), Pain points, What changed (green checks). A note says the "with DRON" line is the design's intent, not a measurement.

## Revision 8, her notes 2026-10-28
- Every phone mockup (the flows and the live phone frame) has a status bar (9:41, battery) above the screen and a small inset below, in the app's #1A1A1A, so the rounded corners never cut the content (the notification badge was cut).
- The desktop live frame: checked on github.io that the stored `wf-theme` = dark opens the desktop demo dark; from a local file the browser keeps the stores apart, so locally it stays light.

## Revision 9, her notes 2026-10-28
- The live phone renders at 1:1 (no scaling on a wide screen), so it is sharp; it follows the stored dark theme like the desktop frame (the `?theme=dark` parameter made the demo skip the stored choice).
- Removed the "Fields, roofs, facades" photo band.
- Journey map: no lines at all; rows and columns held together by space (proximity). Project colours, bright: numbered charcoal phase cards, cream action chips, the chart on a cream card with Signal Green and rust curves and pill callouts, pain points on rust-wash cards, what changed on green-wash cards.

## Revision 10, her note 2026-10-28
- Handoff: the green lines and the orbit removed; grey dashed lines join every side card to the list and to its neighbours.

## Revision 11, her note 2026-10-28
- Research: the sources line under the charts removed from the page; the sources stay recorded in this file (01 Research).

## Revision 12, her note 2026-10-28
- Flows: a 16 px gap between each phone and the arrows or decisions next to it, in both flows.

## Revision 13, her note 2026-10-28
- The product on this page is dark only: both live demos open with `?theme=dark`. The DRON repo now honours that parameter on the desktop (ui/kit.js) and the phone (wireframes/_wf-shell.js) and keeps it for every next page (DRON commit, needs a push of DRON to go live).

## Revision 14, her note 2026-10-28
- Journey map recoloured in the page UI: the chart on a charcoal card, "before" in grey, "with DRON" in Signal Green; pain points on light grey cards; what changed on charcoal cards with green checks. No rust.
- Note under the journey map removed (her call); that the "with DRON" line is intent, not measurement, stays recorded here.
- The embedded demos stay dark: in the DRON repo, a demo opened with ?theme=dark hides its theme switch (desktop sun/moon button, phone Dark theme row) on that page and every next page in the tab (sessionStorage). Needs a push of DRON.
- Opened from a file on her computer, the live frames load her local DRON copy (../DRON/demo/...), so the latest demo shows before DRON is pushed; online they load the published demo.
- JTBD: the formula chips row and the "Three jobs shaped" note removed; the formula now ends the text card; the client keeps four job chips (two rows).
- Flows: the scroll bar replaced by a slider pager, small bars in the centre, the active one green, the others grey; one bar per view of the row (2 on a wide screen, 7 on a phone); a bar takes the row to its view.
- Wireframes: "On the desktop" text above its card; the desktop card sized so text and card fit one screen height (920 x 637 at 1440 x 900); the "Phone first" text aligned to the top of the phone card.
- Flows pager: one bar per drag step (the next phone at the left edge, then the end): 5 per flow at 1440 px.
- Desktop live card full width; the window inside keeps its size (832 px at 1440 x 900), centred, with a small shadow and a hairline so its edge shows.
- Design System numbers: more space above (after the photo) and below (before the cards); labels 17-20 px with a 10 px gap under the figure.
- Design System, Motion card: the right half lists the three jobs of motion and reduced motion, with figures from DESIGN tokens (.32 s sheets, 7 s flight on tracking, press 1 px in .12 s).
- Motion card: the list removed; the chart runs the full card width on a timeline 0 to .4 s, with .12 / .2 / .32 s marked and the dot easing along the curve.
- The "Precise, accountable." motor photo band removed (her call 2026-10-28: she likes it, may add it back); parked in tools/dron/parked/motor-band.html with the images kept.
- Spacing by proximity across the page: a heading sits 32 px over its picture, the picture 88 px over the chapter content, groups inside a chapter 112 px apart, chapters 176 px apart (at 1440 px).
- The live phone card sized to the screen height (806 px at 1440 x 900), so it is seen whole in one screen; the phone scales down slightly.
- Design System photo: the two green lines between the floating parts removed.
- Live cards: a lime glow from the top and a faint lime grid on the dark ground; the desktop window and the phone frame get a soft glowing lime outline.
- Live cards: the square grid removed; the mockups sit in a drone camera viewfinder: lime corner brackets, a crosshair with ticks through the centre, small HUD labels (REC with a blinking dot, ALT 120 m, 4K 60, N 50.45 deg; decorative, hidden from screen readers, labels hidden on phones).
- The viewfinder now hugs each mockup only (brackets 22 px outside its edge, crosshair stubs, HUD labels above and below), on the first-screen desktop and on both live cards; the card grounds and glow stay.
- Type card: the scale named as Apple HIG names its text styles (Title 2 22, Headline 17, Subheadline 15, Footnote 13, Caption 2 11), on the left; the big Aa on the right.
- Handoff card subtitle: "Everything a developer needs to build DRON without asking me: what each screen is made of, how it behaves, and what ships." (was "From a fresh clone, nothing to install.")
- Type card relabelled the HIG way (her reference: the HIG text-style callouts): each row is the HIG style name with its size and weight (Title 2 22 Bold, Headline 17 Semibold, Body 15 Regular, Footnote 13 Regular, Caption 2 11 Semibold), a leader line with a dot, and a sample word from the product; rows on one 12 px rhythm.
- Type card back to the scale as before (each HIG name set in its own style), without leader lines or samples (her call).
- The live phone card only as wide as the phone and its viewfinder (446 px at 1440), on the right; the text takes the rest.
- Phone card: the viewfinder runs along the card perimeter (brackets in the card corners, labels inside them, crosshair across the card).
- Desktop card: the viewfinder along the card perimeter too.
- Live demos (desktop and phone): on a mouse, a green Click circle with a pointer icon follows the cursor beside it, like the Drag circle on the flows, to show the demo can be clicked. Online (same origin) it follows the cursor inside the frame; opened from a file it shows where the cursor came in and fades after 1.6 s.
