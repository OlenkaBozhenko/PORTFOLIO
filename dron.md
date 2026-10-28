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
