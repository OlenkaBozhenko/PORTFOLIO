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
- **About.** DRON is a drone-as-a-service product built for two users: the client and the operator. The client orders a delivery, an aerial shoot or an inspection and gets a locked price and live tracking, while DRON provides a certified operator who receives their earnings once the order is completed.
- **How it was made.** The entire project, from research to handoff, was delivered using AI tools, with Claude Code as the main tool. Large tasks were broken down and distributed across separate agents running in parallel. Multiple AI tools and services were connected into a single workflow through custom MCP integrations. The design was audited with the Impeccable skill, and custom skills were developed for the project’s specific needs. Competitor research was carried out with Playwright. (her text, 2026-10-29; Problem and Solution removed, her call)

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
- MJ-1 Client (on the page, her call 2026-10-29: a concrete job, not the outcome): When I need aerial video for a marketing campaign, I want to book a certified drone operator in a few taps, at a price I see up front, so that I get the footage on time without learning anything about drones. (The research wording: When I need a result that only a drone can deliver, I want to hand the job to a certified professional without managing anything myself, so that I get the outcome without ever thinking about the drone or the operator.)
- MJ-2 Operator (on the page, her call 2026-10-29: the point is earning in his free minutes, not finding clients): When I have a few free minutes and my drone with me, I want a paid job nearby that I can take in one tap, so that my spare time turns into money. Beside it: "A licensed pilot near Kyiv with a drone and a few free hours a week. He hires DRON to fill those hours with paid jobs, without looking for clients." (The research wording: When I have the licence, equipment and capacity to do drone work, I want a steady stream of pre-qualified jobs to reach me without hunting for them, so that I can spend my time flying, not selling.)
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
- Live demos (desktop and phone): a lime arrow cursor glides onto the first button ("I need a service done") and clicks it, on a loop, to show the demo can be clicked (her call, instead of a Click circle). It hides while the pointer is over the demo, stops after the first click inside, and is not shown on touch screens or with reduced motion.
- Live demos: on hover, a Click circle like the Drag one follows the cursor (beside it, so the button stays visible; the arrow hint stays for when the pointer is away). The viewfinder label reads "Live prototype" instead of "REC" on both demo cards (the hero keeps REC).
- Live demos, her call: one cue only. The arrow hint is gone; on hover a see-through lime circle with "Click" grows under the cursor and follows it (on the live site; from a file it shows where the cursor came in and fades), and once she clicks into a demo it disappears for good.
- First screen: the pointer that clicks through the delivery flow is lime (see-through lime fill, lime outline, a soft glow), like the Click circle on the live demos (her call).
- Flows: the Drag circle has the same style as the Click circle on the live demos (see-through lime, lime outline, the text is white over the dark screens and black over the white page, 96 px; the Click circle on the dark demos has white text), so the page has one cursor style (her call).
- Chapter glass cards: no full stop at the end, and the text wraps so the last line never holds one or two words (balanced lines, text-wrap: balance, and the last two words held together), her call.
- Target Audience, the client card (her brief 2026-10-29: show what shapes the design, as modern charts; references: dark dashboard cards with a big number, an area chart, a ring gauge, a stat row). The card "Who orders, in numbers" now holds:
  - Would order drone delivery at about twice the shipping price: 64% across six cities; Milan 72%, Barcelona 68%, Budapest 67%, Paris 61%, Øresund 59%, Hamburg 57%. EASA, Study on the societal acceptance of Urban Air Mobility in Europe, 2021, Fig. 31 (online survey, 3,690 people aged 16–75, delivery within 2 hours at about double the standard fee).
  - Bought goods or services online in the last 12 months, by age: 16–24 84%, 25–34 90%, 35–44 87%, 45–54 80%, 55–64 69%, 65–74 55%. Eurostat, E-commerce statistics for individuals, 2025 (EU internet users 16–74).
  - (Removed 2026-10-29, her call: the higher education ring, Ukraine 51.4% vs EU 34.3%.) The worries took its place as concentric rings, one ring per concern.
  - Top-three concerns about delivery drones: safety 44%, security 39%, privacy 30%, noise 28%, affordability 21%. EASA 2021, Fig. 38.
  - (Removed 2026-10-29, her call: the row of three facts, Diia 21M+ users, 94.6% cashless card payments, Kabanchik ₴500–1,500.) The persona photo sits at the top of the card.
  - Not found: a Ukrainian survey on drone services, and an amount in money people would pay. Ukraine is not in the EASA study. StatCounter shows desktop ahead of mobile in Ukrainian web traffic (Sept 2026), so it is not used as a mobile-first argument.
  - The operator card is unchanged.
  - The worries tile is titled "Top worries about delivery drones" (each person named their top three).
  - Both big numbers (64% and 90%) carry their caption beside them on the baseline, one pattern for the card (her note).
  - Tile titles, a few words each (her note): "Ready to pay 2× for drone delivery" (EASA: likely to use it at about double the standard fee); "Shop online, by age" (Eurostat: bought online in the last 12 months).
- Target Audience, the operator card (her brief 2026-10-29: the same chart style as the client card; drones and drone schools by country). "Who flies, in numbers":
  - Registered drone operators: 1.6M+ across EASA states (EASA, civil drones page, undated). By country, each with the year of its count: Germany 694,451 (LBA via drohnen.de, 2023); Poland 355,413 (ULC, Briefing Dronowy, 12 June 2025, read from a search snippet, to re-check); UK 236,709 active operator IDs (CAA CAP3035 via ARPAS-UK, 30 June 2024, to re-check); Spain 150,332 (AESA, 2025); France 148,874 (DSAC 2024 report via jechange.fr, to re-check); Italy 110,518 (EASA via Dronedesk, July 2024, to re-check). Poland has the most per capita, about 1,070 per 100,000 (EASA via money.pl, 2025).
  - Drone pilot schools: 33 organisations certified as UAV schools in Ukraine (Ministry of Defence, 21 November 2024); 23 CAA-approved training providers in the UK (CAA list, read October 2026). About 20,000 UAV operators trained in Ukraine under Army of Drones by January 2024 (Fedorov via Liga.net); these are military counts.
  - Why UK drone users fly, two rings: for work 14%, for fun 79% (CAA Drone Awareness Tracker, April 2023, to re-check).
  - Not found: a civil drone register in Ukraine (draft law No. 13600 proposes one), school counts for Germany, France, Italy, Poland, the Netherlands, and the share of pilots who are freelance.
  - The earlier operator card (10 s to accept a job, one-glance offer, today without DRON) is replaced.
- Target Audience: the sources line under the two cards is taken off the page (her call, 2026-10-29); the sources stay listed here in dron.md.
- Operator card, the two lower tiles redrawn for reading (her note): drone pilot schools as a unit chart, one dot per school (Ukraine 33 in lime, UK 23); why UK drone users fly as one donut, parts of one whole (for work 14%, for fun 79%, other 7%, the remainder of the same survey), with 14% for work in the centre.
- Operator card, schools by country as a lollipop chart, Ukraine in lime: Spain 117 entities recognised by AESA for STS practical remote-pilot training (AESA list dated 23 October 2026; a declarative regime, counted from the PDF); Ukraine 33 certified UAV schools (Ministry of Defence, 21 November 2024); Germany 24 LBA-designated test centres for remote pilots, which run the A2 exam (LBA list, read October 2026); UK 23 CAA-approved training providers (read October 2026); Ireland 3 IAA recognised training entities (read October 2026). Each country counts a slightly different kind of body, so the chart compares the order of size, not identical schools. Poland not found (the ULC list is behind a bot block).
- Why drone users fly: the title names no country, and the line below reads "Those who fly for fun can start earning with DRON" (her call). The figures are still the UK CAA survey until a Europe-wide split is found.
- Schools chart: no country singled out, every lollipop lime; the big number is the largest, 117 in Spain (her note).
- Why drone users fly, now from a registry, not a survey: of 148,874 registered drone operators, 118,196 are registered as leisure flyers (79.4%, shown as 79% for fun) and 30,678 are not (20.6%, shown as 21% for work: open and specific category operators, which in her reading are companies and professionals; DSAC gives no count of legal persons). DSAC, Rapport d'activité 2024, p. 48, 31 December 2024 (France), verified in the PDF. No Europe-wide split was found (EASA publishes totals only; Spain, UK, Germany, Poland publish no split). The title names no country (her call).
- Target Audience glass card, her call: a definition of the term itself: "A target audience is the group of people a product is made for: who they are, what they need and what holds them back. Knowing it shapes every decision, from the first screen to the price on the card"
- Chapter glass cards for Research, User Flows, Tone of Voice, Wireframes and Handoff now say what the stage is and what it is for (her call), like the Target Audience card:
  - "Research is how a team learns the field before it designs anything: who already solves the problem, how, and where they fail. For DRON it studied the competitors and the people on both sides, the clients and the drone operators"
  - "A user flow is the path a person takes through the product to finish one task, step by step and screen by screen. It shows every decision and every dead end before a single screen is drawn"
  - "Tone of voice is how a product speaks: the words it picks, how formal it is and how it sounds when something goes wrong. One set of rules keeps every screen sounding like the same company you can trust"
  - "A wireframe is a plain layout of a screen: what goes where and how it works, before colour and style. It lets the team test the structure and every state cheaply, before the visual design"
  - "Handoff is the moment the design passes to the developers: the screens, the rules and the specs they need to build it. A clean handoff means the product is built as designed, without guesswork"
- The Wireframes chapter is renamed Design (her call; the photo stays). Its glass card: "Design is where the structure gets its look and feel: colour, type, imagery and motion, on every screen and in every state. It turns a working layout into a product people trust at first glance. Below is the live demo, dark theme". The section id stays #wireframes, so old links still work.
- JTBD: no "Her jobs" / "His jobs" labels; three chips each. Client: Confirm who comes, Know the price first, Proof the job was done. Operator: Decide in seconds, A checklist on site, Paid without chasing (her call).
- Design captions ("On the desktop", "Phone first") run in shorter lines, about 40 characters (her note).
- CJM: the actions keep one row per phase (removed: See the price, Pay, Report an issue), and the legend "Before the fixes / With DRON, as designed" is taken off the chart (her call).
- Design captions in two lines (her wording, 2026-10-29): desktop "A new take on the familiar admin panel and dashboard. Try the live demo."; phone "Adaptive on every phone, so the end user is always at ease. Try the live demo."
- A section dock at the bottom of the page (her reference 2026-10-29: a bottom toolbar with tabs). A dark glass pill with an icon per chapter (Research, Audience, JTBD, Flows, Voice, Design, CJM, System, Handoff); the current chapter is lime with its name and changes as she scrolls; the others open their name on hover or keyboard focus. It slides in once the story starts. On a phone it shows icons only (the current one lime), so all nine fit.
- Dock: desktop only, no dock on the phone (her call). Icons: Research is a bar chart (a magnifier read as search), Handoff a zipped file.
- Dock labels: "Tone of Voice" and "Design System" in full (her call).
- Phone (up to 720 px): no CJM chapter and no desktop live demo (her call); the desktop demo frame is not loaded there. Desktop unchanged.
- Phone (up to 720 px): the first screen is only the live desktop flow inside its viewfinder, on the white page: no drone photo, no dark backdrop, no caption (her call). Desktop unchanged.
- Phone first screen: the demo window has the same soft shadow as the cards on the other case pages (0 1px 2px at 6%, 0 24px 48px -24px slate at 28%).
- Phone first screen: the demo is bigger (the viewfinder 8 px around it), and the window and the viewfinder corners share a 14 px radius (her note).
- Phone: each chapter photo and its glass card form one dark card; the photo on top fades into the dark and the text card sits inside it (her references: the Market reality and Tone of Voice cards). No new images needed.
- Phone: the flow phones are bigger (240 px, up to 66% of the screen width) and the rows swipe sideways with a gentle snap to each phone (her note).
- Phone: the live phone demo is bigger, filling its card inside the viewfinder (30 px side padding).
- Phone: the "Live prototype" label is centred on the top edge of the phone demo viewfinder (her note).
- Phone: the persona photos (Kateryna, Andrii) run the full width (her note).
- Phone: the "Who orders" and "Who flies" cards lose their dark backdrop; each chart tile stands on its own, full width, on the white page (her note).
- Phone: the "Who orders / Who flies, in numbers" titles are 24 px, the Client / Operator badges are hidden, and the JTBD chips are small (13 px, 6 x 12 px padding) like the Warmy chips (her notes). Desktop unchanged.
- Phone: the "Live prototype" label sits higher, on the line of the top brackets (her note).
- Phone: the first-screen crosshair line runs only 12 px past the viewfinder, top and bottom (her note).
- Phone: the live phone prototype is sized to the screen height, so the whole phone fits on one screen with room around it; then made a little wider (her notes).
- Phone and, since 2026-11-02, desktop: the viewfinder crosshair no longer runs over the phone mockup; the phone frame is solid (her notes).
- Phone: the title sits on three lines, "Drone services," / "from research to handoff," / "designed with AI.", so AI never wraps alone; on the narrowest phones the title scales down a little to keep the three lines (her notes).
- Phone: Handoff shows only the release card beside the list (tokens, components, commits, run it and what ships are hidden); the list has no dark backdrop and each file is its own dark card (her call).
- Phone: in the user flow strip, each screen's caption (1 · Find, Service, where, when…) is centred under its phone (her note).
- Phone: the step numbers in the flow captions (1 · , 2 · …) are left out; only the step name shows (her note).
- Phone: the pager under each flow has one bar per screen in the flow (7 and 7), whatever the screen width (her note).
- Desktop (2026-11-02, her call): the drone from the DRON wordmark (the one flying in place of the O on the landing thumbnail) flies after the mouse, a little behind it, leaning into the move, propellers spinning and a slow bob; dark as in the wordmark, with no lime glow around it, and it fades out over a picture, a live frame or a dark ground, coming back over the white page; it flies only from the About section down to the start of the Handoff block: never over the first screen above About, the User Flows section (it got in the way of dragging the screens), the Handoff block or anything below it (her notes); it never takes a click and fades out when the mouse leaves the page. Not on touch screens, below 900 px, or with reduced motion.

## Back link

**← Back to projects** above the eyebrow, back to the Case Studies list on the landing (her call 2026-11-03; was *← All work*). On desktop (mouse), hovering the link shows an empty see-through 64 px circle that follows the cursor, exactly like the circle on the landing View links but in the case colours: Signal Green #9BCF4A, fill at about 20% and a 1.5 px border. As on the landing View links.

## Previous and next project

At the bottom of the page (her call 2026-11-03; was *View next work*): left **← Back to projects**, right **View next project Warmy →**, in the landing order (DRON, Warmy, AnyBiz, Sport Guardian, School, Styupan, Book). Where there is no previous or next project, the link goes back to the projects. On desktop the same see-through circle as on the top back link follows the mouse over both links.

## To the top

On desktop a **↑ To the top** pill sits to the right of the section dock and shows with it, always in the page's primary dock colour (Signal Green). It scrolls to the top (instantly with reduced motion) and moves focus to the back link. Hidden on phones, like the dock.

The mouse drone also fades out while the cursor is over the section dock or To the top (her note 2026-11-03).
