# AnyBiz — project page content

**Source of truth for** [`AnyBiz.html`](AnyBiz.html), the page that opens from row 3 of the landing's work list (first build 2026-10-22).
Her brief (2026-10-22): a page for AnyBiz in exactly the style of the Warmy page, but in AnyBiz's own look. Start like every project page (header); the first screen is a greeting from the AI agent after her Figma frame 247:78026 ("Create messaging instructions"); the product shown in mockups as on Warmy. The main accent: she built an AI tool and ran many user interviews, which let the team test features before they were built, improve the product, understand the users, and sometimes drop a feature the audience did not need or build a different one that really strengthened the product. The key finding of the interviews: users did not trust AI agents and were afraid to delegate everything to them, so the product gives them clear instructions to set for the agent, and then they can trust it with their company. She studied behaviour through session recordings, which showed the moments that need attention. An accent on integrations: many integrations make the product a favourite for users who like having all their tools in one place. Professional senior-designer language. Some blocks may take other layouts so the page is not one to one with Warmy (her references: a dark overview with My role and Responsibilities pills next to a tilted dashboard; a bento of phone mockups; glass AI components next to a phone; Genesis by Cuberto, a small panel and caption next to a tall tilted tablet, and a title, a rule and a small label left with text right; Zelt by Cuberto for the accent on her role). **No round icon chips in the headlines** (her request, 2026-10-22: unlike Warmy). Fonts and sizes as on her other project pages.

---

## Facts
| | |
|---|---|
| What it is | AnyBiz.io, a B2B platform that hires out AI sales agents: they find prospects, write to them by email and LinkedIn, call them, post for the brand and book meetings, and report the results as insights |
| Her role | Product Designer (landing and resume); the AI agent experience, user interviews with dynamic prototypes, session recording analysis, integrations, data-heavy screens (her brief, 2026-10-22) |
| Years | 2021 – present (landing). The timeline is open question 3 in `CLAUDE.md`: one continuous role or two periods |
| Platform | Web SaaS, desktop and mobile web |
| Product UI type | Inter (read from her Figma screens) |
| Product colours (sampled from her Figma exports, 2026-10-22) | ground #020617; panels #0F172A, cards #1E293B, lines #334155; text #E2E8F0, muted #94A3B8; violet #8B5CF6 (buttons), light violet #A78BFA; teal #5EEAD4 / #2DD4BF; sky #38BDF8; rose #FB7185; the logo arrow a pink to violet gradient |
| Accent on the page | the logo gradient #EC4899 → #8B5CF6, decorative only. Small white text sits on #7C3AED (5.7:1), never on #8B5CF6 (4.2:1, fails AA for small text) |
| Product facts (vendor-reported, anybiz.io/product, read 2026-10-22) | AI cold calling, AI email and AI LinkedIn channels, personalised AI landing pages, website visitor detection, Warmy warm-up included; CRM integrations HubSpot, Monday, Intercom, Asana; notifications in WhatsApp, SMS and Slack. The site gives two different database sizes (300M and 450M prospects), so no database figure is on the page |

Sources: her Figma file My-projects-new (`YlGWlsWWjKSCxhONMzGG2F`), section 247:77772, read 2026-10-22: Messaging, empty state (247:78026 inside 247:78008), Messaging instructions with the email example (247:78046), account set-up (247:78797), "magic is on the way" (247:79444), Integrations (247:78229), AnyBiz insights (247:79472), mobile menu (247:79007), Sequence builder (247:78151), Personas (247:78364), Personas performance (247:79366), Persona details (247:79425), Manage automated posts (247:78840), the expo back wall with the octopus (247:77773). The product site anybiz.io/product (read 2026-10-22).

**Privacy in the screens.** Her work email in the mobile menu (247:79007) is replaced by an invented one, "jamie@northwind.io", by [`tools/anybiz/export_assets.py`](tools/anybiz/export_assets.py). The raw Figma exports in `tools/anybiz/figma/` stay out of git (`.gitignore`); export them again from the nodes above (2x) to rerun the script. The persona photo in the email example is not used: the live prototype draws initials.

**Corners and captions:** as on the Warmy page: panels have sharp corners; only the screens and UI pieces inside keep their rounded corners. Captions sit under their panel, left-aligned.

## Page copy
No em dashes in visible text (her rule).
- **Back link:** ← All work
- **Eyebrow:** B2B, AI SaaS (the project category only; B2B added on her request, 2026-10-22)
- **Headline:** An AI sales platform that finds leads and books meetings.
- **Meta row:** Role · Product Designer · Years · 2021 – present · Platform · Web, mobile web · Product · AnyBiz.io

### 1. First screen: the AI agent says hello
After her frame 247:78026: the deep night ground of the product (#020617) with violet and sky glows and twinkling four-point stars (the stars of her frames). In the middle the AnyBiz orb (three rings in violet, rose, sky and teal, exported from the frame as `assets/work/anybiz/orb.svg`) turns slowly while "Create messaging instructions" types in letter by letter with a violet caret (34 ms a letter, as on Warmy); then "Provide instructions to ensure your AI Agent communicates exactly as you wish" fades in, and the four channel cards rise one by one: Email introduction, Email follow-up, LinkedIn message (Connect +), Phone calls (Get access +). The first card lights up as if chosen, and everything stands still. Plays once.
**Softer, with a prompt field** (her request, 2026-10-22: more delicate, more air, not bulky; thin lines, no heavy shadows or glows; the logo is animated; a message field in place of the cards, after the DRON prompt bar, in the project's violet): the title is small and light again, as in her frame (Inter Medium 22–32 px), the subtitle 14–16 px, with wide margins all round; the glows of the ground and the stars are fainter and smaller. The orb is drawn inline and its three rings orbit at their own speeds (8, 11 and 14 s, the middle one the other way) round a breathing violet dot, for as long as the screen is in view. In place of the four cards: a pill-shaped field with a thin violet line (no shadow), "Tell your AI Agent how to write..." and a round violet send button with an arrow; under it the four channels as thin outlined chips (Email introduction, Email follow-up, LinkedIn message, Phone calls). After the title and the subtitle, the field types "Keep it short and friendly, mention our case study, and offer a 15-minute call." and the button presses once; then the typing stops for good.
**A wide rectangle** (her request, 2026-10-22: rectangular, not square): the first screen is 21 : 9 on wide screens (it was 84% of the window height), with the orb, the margins and the gaps tightened to fit; under 900 px it takes the height of its content. Tiny stars in the brand colours follow the mouse pointer (not on touch, not with reduced motion).
**Still title and field** (her request, 2026-10-22): only the logo and the text typed in the field move. "Create messaging instructions", the line under it, the field and the channel chips are in place from the start; after a short pause the field types the instruction and the button presses once.
Motion (WCAG 2.2.2): plays only on screen; a click, a tap or Enter / Space stops or starts it; with reduced motion it stands still, complete.

### 2. About / Problem / Solution (as on every project page, her request 2026-10-22)
The pattern of the Warmy page: the title left, the text right. (Was a Genesis row with a small label; she asked for the common pattern back.)
- **About:** AnyBiz is a B2B platform that hires out AI sales agents. They find prospects, write to them by email and LinkedIn, call them, keep the brand visible with posts, and book meetings into the calendar.
- **Problem:** Outreach eats a sales team's week: finding the right people, writing to each of them, following up, calling, and keeping the CRM current. AI can do all of it, but the people who own a company's reputation are afraid to let it speak for them.
- **Solution:** AI agents that work across email, LinkedIn and phone under instructions the customer writes: who to reach, in which language and tone, with which call to action and signature. The customer sees an example before anything goes out, and every result comes back as insights.

**Order of the page** (her request, 2026-10-22: the pattern of her portfolio, the header, then the product, then her role and what she did there): 1 first screen · 2 About / Problem / Solution · 3 Product (with Integrations) · 4 My part (the role, the five items, Research, Key insight, Behaviour) · 5 Campaign visuals. **Showing the product** (her request, the same day): every screen sits on a pale panel inside a mockup (a browser or a phone), or, in a card, as separate UI pieces drawn in HTML; no small unreadable screenshots. The Genesis panels and the bento of presentation shots were taken out.

### 3. Product (the feature list next to a browser and a phone, as on the Warmy page)
Section label **Product**, note **Hire AI agents** (the product's own tagline, from her poster 247:77773).
Headline: A salesperson that works 24/7, *set up in one place*
On a pale violet panel (#F1EEFB) a browser frame (app.anybiz.io) and a phone; the list beside it opens one item at a time and the screens crossfade. The open button turns violet (#7C3AED, a white plus).
1. **Messaging instructions** (247:78046, `messaging.webp`; the phone shows the settings menu cut from 247:79007, `phone-settings.webp`): The rules the agent writes by, channel by channel: persona, language, tone of voice, call to action, signature, guidelines and case studies. The agent shows an example before anything is sent.
2. **Personas** (247:78364 cut to 16:10, `personas-app.webp`; the phone shows the main menu, `phone-menu.webp`): Who the agent should reach, found in the database or imported from a file, LinkedIn, HubSpot, Zapier or Salesforce, each with its offering, channels, source and status.
3. **Sequence builder** (247:78151, `sequence.webp`, scrolling slowly in the browser; no phone): Email, LinkedIn and phone steps in one timeline, each with its own sending window and instructions. Language, tone and offering are set once, at the top.
4. **Performance** (247:78078 cut to 16:10, `performance-app.webp`; no phone): Engaged prospects, actions per channel, reply and opportunity rates for every persona, so the budget follows the audience that answers.
Two cards of separate UI pieces in the product's dark style on the pale panel, the caption under each (figures from her design mockups, said in a note):
- **A brand awareness agent** (after 247:78840): the "Enable LinkedIn auto-posts" row with its toggle on; the schedule, Monday 2:15 PM Text only, Tuesday 10:00 AM off, Wednesday 2:15 PM Text + image. Caption: The agent writes and publishes LinkedIn posts for the brand on a schedule the customer controls, day by day and by format.
- **Personas, not lists** (after 247:79472 and 247:79366): a persona recommendation, John Anderson, From Database, United States, Matching prospects 10K, with a signal meter; total actions 4.5K, 3.3K and 500 by channel, reply rate 1.2%, opportunity rate 0.1%. Caption: The agent recommends who to reach and shows how many prospects match before a campaign starts; afterwards, every persona reports its own results.

#### Integrations (inside Product, under a thin sub-head: Integrations · Every tool in one place)
Headline: The tools our users already love, *in one place*
Two rows of integration pills sliding in opposite directions (Ramos pill marquee): HubSpot, Salesforce, Zapier, Calendly, Make, Monday, SalesLoft, Asana, Slack, Intercom, LinkedIn, Gmail, Outlook, WhatsApp, Warmy. Each pill carries a small monogram in the tool's colour (no logos).
Text left: Integrations are a big part of why many users love AnyBiz: their CRM, calendar, automation and messaging tools work from one place, and leads, meetings and replies stay in sync on their own. I designed every integration as one pattern, so a new one never needs a new idea: a status (Connected, Incomplete, Inactive, Coming soon), one button to connect, the docs a click away, and early access for what is next.
Right, three integration cards drawn as separate pieces on the pale panel (from her screen 247:78229): HubSpot, Incomplete; Zapier, Connected; Salesforce, Inactive, with Connect. Caption: Three of the integration cards, drawn from her design: one status, one action, the same pattern for every tool. (Was the whole Integrations screen in a browser frame.)


### 4. My part (her role and what she did; Research, Key insight and Behaviour now sit inside it, each under a thin sub-head)
Section label **My part**, note **What I brought to AnyBiz**.
Headline (no chips): I designed the AI agent, *tested* every idea and *watched* how people use it
Five rows, the number left, the title, the text right:
- 01 **AI agent experience.** Messaging instructions, the brand awareness agent, persona building and the onboarding states, on desktop and mobile.
- 02 **User interviews.** Dynamic prototypes tested with users before development, to sharpen, drop or replace a feature.
- 03 **Session recordings.** Real sessions reviewed to find hesitation, dead ends and drop-offs, and turned into fixes.
- 04 **Integrations.** CRM, scheduling, automation and messaging tools designed as one consistent pattern.
- 05 **Data-heavy interfaces.** Personas, prospect tables, sequences and performance analytics that stay readable at scale, built on a shared design system.
Under the headline, before the five items, the challenge and her role:
On the white page, no background panel (her request, 2026-10-22): text left; at the right her Deliverability insights screen (Figma 247:79006, `deliverability.webp`; replaced the Insights screen 247:79472, her request) tilted in 3D, with rounded corners and a soft shadow.
- **Text:** The challenge was to let a company hand its outreach to an AI without losing control of its voice, and to keep a product with many channels, personas and integrations clear enough to set up and easy to trust.
- **My role:** Product Designer
- **Responsibilities (pills, pale grey):** AI agent UX · User interviews · Prototyping · Session recordings · Information architecture · Integrations · Data-heavy interfaces · Design system

#### Research (sub-head: Research · Tested before it was built)
Section label **Research**, note **Tested before it was built**.
Headline: Every feature met our users *before it met the developers*
Intro: I built dynamic prototypes of the AI tools and ran user interviews on them before anything went into development. People worked through real tasks on the prototype, so we saw how they behaved, not what they promised. It made the product better and taught us who our users are. Three outcomes kept coming back:
- 01 **Sharpened.** Most ideas survived, but not as drawn. Where people hesitated, misread a label or expected a different next step, the fix went into the design before a line of code was written.
- 02 **Dropped.** Some features never reached the backlog. When interviews showed that our audience did not need them, we stopped them at the prototype and saved the team weeks of building.
- 03 **Replaced.** Sometimes the interviews pointed to a different need. We set the planned feature aside and designed the one that really strengthened the product.
(No feature names here: she can add the real examples, open question below.)

#### Key insight (sub-head: Key insight · Trust is designed)
Section label **Key insight**, note **Trust is designed**.
Headline: Users did not want to hand their company to AI. *They wanted to instruct it.*
Text: The interviews showed it again and again: people did not trust AI agents and were afraid to let one speak for their company. So we did not ask them to trust a black box. We gave them clear instructions to set for the agent, channel by channel: the persona, the language, the tone of voice, the call to action, the signature, message guidelines and case studies. Before anything goes out, the agent writes an example; the customer can regenerate it or save it and train the AI. With the rules in their hands, customers hand the outreach of their company to the agent.
Dark panel. Left, glass UI pieces drawn in HTML in the product style: the instruction checklist (Persona, Language, Tone of voice, Call to action, Signature ticked; Message guidelines and Case studies with an amber note), the setting pills (English (United States), Professional, Offering), and the buttons Regenerate and Save and train the AI. Right, a live prototype of the instructions screen in HTML: "{AnyBiz} magic is on the way..." with a filling bar, then the example email types in (her Figma copy, 247:78046: Subject: Unlock the potential for growth! / Hi [Recipient's Name], / I'm Martin from Anybiz, and I believe we can help [Company Name] improve its cold email outreach. / Our platform helps teams like yours by: automating and personalizing email campaigns; improving deliverability and avoiding spam filters; providing insights to optimize conversions. / Would love to chat and learn more about your goals.), the Save button pulses, and it starts again. Same motion rules as the first screen.
Caption: **An example before anything is sent.** The agent shows what it will write from the customer's own instructions. Nothing leaves until the customer is happy with it.

#### Behaviour (sub-head: Behaviour · What people do, not what they say)
Section label **Behaviour**, note **What people do, not what they say**.
Headline: Recordings show *what people do* when nobody is asking
Text left: Interviews tell you what people think. Session recordings show what they actually do. I watched real sessions to find the moments that need attention: where people hesitate, click something that does nothing, click again in frustration, or leave a flow half done. Each moment became a design fix, a question for the next interview, or a hypothesis to test.
Visual right: a session replay drawn over the Personas screen (247:78364, cut to 16:10) inside a browser frame: a cursor moves along a path, a hesitation ring, a rage click ripple and a dead click appear where they happen; under it a player bar with a timeline and coloured markers, and a legend: Hesitation, Rage click, Dead click, Drop-off. Note under it: An illustration of the method, not a recorded session.

### 5. Campaign visuals
A moving mosaic on the night ground over "anybiz" repeated as a running line, as on the Warmy page: the expo back wall with the octopus mascot, "A Salesperson That Works 24/7" (247:77773), and the presentation shots of the product. Same motion rules.
Caption: Marketing design around the product: an expo back wall with the octopus mascot and presentation shots of the AI agents.

### 6. **View next work:** Sport Guardian (`SportGuardian.html`), in the order of the landing's work list. Warmy's next work is now AnyBiz.

## Open questions for her
1. Research outcomes: name one real feature for each of Sharpened, Dropped and Replaced, if she can share them.
2. Her role and responsibilities on the page: confirm the eight pills and the five items in My part.
3. Session recordings: which tool (Hotjar, Clarity, other)? Not named on the page until she says.
4. The AnyBiz timeline (CLAUDE.md, question 3) also sets the Years in the meta row.
