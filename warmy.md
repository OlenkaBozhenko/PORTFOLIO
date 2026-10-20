# Warmy — project page content

**Source of truth for** [`Warmy.html`](Warmy.html), the page that opens from row 2 of the landing's work list (first build 2026-10-20).
Her brief (2026-10-20): show how complex the product is and her part in it as the designer: she designed features and user flows, built dynamic prototypes, prepared hypotheses for A/B tests and ran user interviews; the rules and best practice for writing hypotheses and for preparing and running interviews belong in the copy. Add a Customer Journey Map built on her CJM artifact, with made-up data and rewritten text. Start like every project page (header), then a first screen after her Figma frame 207:95960 (the AI loading screen): "Warmy magic is on the way" in large capitals across the whole background, typed like an AI. Then block titles and feature presentation after Ramos (ramos-app.webflow.io): headlines with round icon chips and grey words, a sliding text in a pill, an accordion of features next to a laptop and a phone, feature cards with stacked UI pieces on a gridded panel; a grid of different blocks placed differently, with blocks and text lining up across sections; the patterns of the other portfolio pages; the animations of Ramos. The public warmy.io design is not a reference (her words): the site was read only to understand the product. References: [`inspiration.md`](inspiration.md) 2.10.

---

## Facts
| | |
|---|---|
| What it is | Warmy.io, an email deliverability platform: it warms up mailboxes and domains, tests where emails land (inbox, spam, promotions), checks DNS and templates, and explains the results through its AI agent, Adeline |
| Her role | Product designer, part-time: features, user flows, dynamic prototypes, A/B test hypotheses, user interviews (her brief, 2026-10-20) |
| Years | Aug 2021 – present ([`cv.md`](cv.md), LinkedIn) |
| Platform | Web SaaS, desktop and mobile web |
| Product UI type | Figtree (her Figma variables: `text-base/Regular` 14/17 and the rest) |
| Product colours | brand #FF7658; text #334155; muted #64748B; lines #E2E8F0; primary button #030712; the logo bars yellow, orange, red (#FFD15C, #FFA53A, #FF453A, sampled from her Figma frames) |
| Product numbers (vendor-reported, warmy.io, read 2026-10-20) | 35,000+ businesses and marketers; 650,000+ domains with better deliverability; 35+ email service providers connected; G2 rating 4.9 of 5 |

Sources: her Figma file My-projects-new (`YlGWlsWWjKSCxhONMzGG2F`), section Warmy 207:93444: Sender tracker desktop and mobile (207:95979, 207:95975), Template score (207:96089, 207:96099), Spintax detected (207:96108), Adeline AI (207:97381, 207:97391, 207:97328), the voice input on mobile (207:97352), the Stripe custom plan checkout (207:96121), the loading screen (207:95960), the iGaming social posts (207:97396, 207:97825, 207:97697, 207:97932) and the print ad (207:93445); read 2026-10-20. The product modules from warmy.io (read 2026-10-20).

**Privacy in the screens.** Her success manager's name and photo in the sidebar are replaced by an invented person, "Mia Larsen", with initials; the design-file placeholders `{Workspace}` and `{Name}` read "Northwind Mail" and "Jamie Cole" (made up). Done by [`tools/warmy/export_assets.py`](tools/warmy/export_assets.py), which also carries the sidebar of the tall Sender tracker frame down to the bottom. The raw Figma exports in `tools/warmy/figma/` stay out of git (`.gitignore`), since they still show the real name and photo; export them again from the nodes above to rerun the script.

## Page copy
No em dashes in visible text (her rule).
- **Back link:** ← All work
- **Eyebrow:** Email deliverability SaaS
- **Headline:** Getting every email into the inbox, not into spam.
- **Meta row:** Role · UI/UX designer (as on the landing and in the resume) · Years · 2021 – present · Platform · Web, mobile web · Product · Warmy.io

### 1. First screen: "Warmy magic is on the way"
After her loading frame 207:95960, simplified (her requests, 2026-10-20: no letters and no lines in the background; faster; the caret close to the text; bigger sparkles; a glow under the text so it reads as an AI writing; her logo): a plain cream ground (#FFF8EE); in the middle her Warmy logotype icon (Figma "Logotype / Icon", I207:95973;19711:154723, 48 × 48, `assets/work/warmy/warmy-logo-icon.svg`) breathing as the loader, and under it "Warmy magic is on the way" in large Figtree SemiBold (30–64 px), typed letter by letter (38 ms a letter) with an orange caret right after the last letter, then five dots appear one by one and start again; a soft orange and pink glow breathes under the line, and larger sparkles sit at its top right.
Motion (WCAG 2.2.2): it plays only on screen, stops while the pointer is over it, and a click, a tap or Enter / Space stops or starts it (screen readers hear how); with reduced motion it stands still, typed out.

### 2. About / Problem / Solution (label left, text right)
- **About:** Warmy keeps email out of spam. It warms up new mailboxes and domains by sending and answering real-looking mail, tests where campaigns land at Gmail, Outlook and Yahoo, checks DNS records and templates, and explains what it finds through Adeline, its AI agent.
- **Problem:** Deliverability fails quietly. An email service provider reports "delivered" even when the email went to spam, and the cause can be a DNS record, a blacklisted link, a sudden jump in volume or a template that reads like a sales blast. Senders see the drop in replies weeks later, with no idea which of these broke.
- **Solution:** One product that turns every signal into a next step: warm-up that runs by itself, placement tests on live campaigns, a sender tracker that shows what happens outside Warmy, a template score with fixes ranked by impact, and an AI agent that answers in plain words. Each screen ends with an action, not a chart.

### 3. How complex it is
- **Headline (Ramos style, grey words, round chips):** One email [bolt chip] passes a dozen checks [chart chip] before it reaches the inbox
- **Counters (vendor-reported, warmy.io, read 2026-10-20):** 35,000+ businesses and marketers · 650,000+ domains · 35+ email service providers · 4.9 of 5 on G2. A note under them: "Numbers as Warmy reports them, warmy.io, October 2026."
- **What sits behind one inbox** (six groups, each a card of chips):
  - Authentication: SPF, DKIM, DMARC, BIMI, MX records
  - Reputation: domain and IP reputation, blacklists, Google Postmaster, spam complaints
  - Sending: warm-up volume, ramp-up schedule, sending windows, seed lists
  - Content: templates, spintax, links and images, unsubscribe link, AI optimisation
  - Mailbox providers: Gmail, Outlook, Yahoo, Google Workspace, Microsoft 365, 35+ ESPs
  - People and plans: founders with one domain, agencies with hundreds of mailboxes, iGaming CRM teams, AI SDRs; custom plans paid through Stripe

### 4. Product (accordion and devices, Ramos)
Title: **Turning signals into next steps.** Five items, the first open; opening one shows its screens in a browser frame and a phone screen beside the list (crossfade). The frames are the ones of the Sport Guardian page (her request, 2026-10-20: the laptop and phone bezels were too heavy): a light browser bar with three grey dots and app.warmy.io, 10 px corners and a soft shadow; the phone as a rounded screen with a soft shadow, no bezel.
1. **Sender tracker:** What you send outside Warmy, from any tool: opens, clicks, bounces, spam and unsubscribes in one chart, a warning line when campaign mail falls under the at-risk mark, and the biggest risk named by provider. (`tracker-desktop`, `tracker-mobile`)
2. **Template score:** A score out of 100 before the email reaches a real inbox, with failed, warning and passed checks by section, and suggestions ranked High and Medium. (`template-desktop`, `template-mobile`)
3. **Spintax check:** For templates that change in every send: Warmy scores one of 18 variations and asks to preview the rest, so nobody trusts a score that covers one version. (`spintax-desktop`, `template-mobile`)
4. **Adeline AI:** The AI agent answers in plain words, with three starting questions, a call with an advisor or a human chat one tap away, and a reminder that the AI can be wrong. (`adeline-desktop`, `adeline-mobile`)
5. **Voice and thinking states:** Asking by voice on the phone, and a Thinking state on desktop, so the wait reads as work, not as a frozen screen. (`adeline-thinking`, `chat-mobile`)
Accessibility: the list is real buttons with aria-expanded; the screens change with the open item and carry alt text; keyboard and screen readers get the same content.

### 5. Feature cards (gridded panels with stacked UI pieces, Ramos)
Two cards side by side, each a pale gridded panel with two overlapping UI pieces drawn in HTML in Warmy's style (Figtree, its colours), title and text centred under them. Figures are made up for the mockup.
- **Placement you can prove.** Inbox 91% (+12 this week); by provider: Gmail 94%, Outlook 86%, Yahoo 92%; Spam 6%, Promotions 3%. Text: A seed test sends the real campaign to test inboxes at each provider and reports where it landed, so "delivered" finally means something.
- **Warm-up that knows when it is done.** Health 82 of 100, Day 18 of 21, a rising line; "Ready to send 1,200 a day". Text: Warm-up ramps volume step by step and shows a finish line, so senders know when the domain is ready and what keeps it safe after.

### 6. My part (her role)
Headline (Ramos): I designed [pen chip] the features, tested [flask chip] the ideas and asked [chat chip] the people who use them
Five numbered items:
- 01 **Features.** From the problem to the shipped screen: Sender tracker, Template score with spintax, Adeline AI, the custom plan checkout, on desktop and mobile.
- 02 **User flows.** Every path mapped before a screen is drawn, with the empty, loading, error and limit states, so developers build the edges too.
- 03 **Dynamic prototypes.** Clickable prototypes with real states (typing, thinking, voice, scores filling in) to test with users and to show developers how a screen moves.
- 04 **A/B test hypotheses.** Written before anything ships, with one change, one metric and a decision rule.
- 05 **User interviews.** Planned, run and synthesised into the journey map below.

### 7. Dynamic prototype (live, in a phone)
A phone playing the Adeline flow in HTML, as her prototypes do, in the thin outline of the Sport Guardian phone (1.5 px, no heavy bezel): the start screen with three questions; a tap on "Why are my emails landing in spam?"; the question as a bubble; Thinking…; the answer typing in: "Your spam rate at Outlook rose to 14% this week. Two things stand out: your DMARC policy is set to none, and the template Spring offer has three links. Fix DMARC first, then I will check the template." with two buttons, Open DMARC check and Analyze template. Then it starts again. Same motion rules as the first screen. Caption: **A prototype, not a picture.** Prototypes in Warmy carry the real states: the typing, the wait, the answer, the next step. Users react to how it behaves, and developers see the timing they need to build. (The figures in the answer are made up.)

### 8. How I write an A/B hypothesis
Intro: A test is only as good as the sentence written before it. I write it down before the design is final, and the team agrees on it before launch.
**The template:** Because we saw [evidence], we believe that [one change] for [segment] will [move one metric] by [expected size]. We will know after [sample or time]. We ship it if [decision rule], unless [guardrail] gets worse.
**The rules:**
1. Start from evidence: an interview quote, a drop in the funnel, a support ticket. Never from taste.
2. Change one thing, so the result points to a cause.
3. Pick one primary metric that the change can move within the test, and name it in advance.
4. Say the direction and the size you expect. "Better" cannot be wrong, so it teaches nothing.
5. Work out the sample size and the run time before launch, and do not stop early when the numbers look good.
6. Add guardrails: the metrics that must not get worse (spam complaints, cancellations, support load).
7. Write the decision rule before launch: what we ship, what we drop, what we test next.
8. Keep a log of every result, the losing ones too. A failed test still answers a question.
**Example (made up for the portfolio):** Because interviews and cancel reasons showed that senders cancel warm-up when they cannot tell whether it worked, we believe that showing a finish line on the warm-up screen ("Day 18 of 21, ready to send 1,200 a day") for new accounts will lower 60-day cancellations from 18% to 14%. We will know after 2 × 1,500 new accounts, about 6 weeks. We ship it if cancellations drop by at least 3 points, unless upgrades fall. Variant A: progress in percent. Variant B: the finish line with the daily volume. Shown as two small cards with an "Example" label.
Sources for the method: Ron Kohavi, Diane Tang, Ya Xu, *Trustworthy Online Controlled Experiments* (2020); Nielsen Norman Group on A/B testing.

### 9. How I prepare and run a user interview
Three columns, Before, During, After:
- **Before:** Write the goal and three to five research questions: what we need to learn, not what we want to hear. Recruit five to eight people per segment with a short screener, current users and people who left. Write a discussion guide: a warm-up, open questions about past behaviour, and the topics to cover, not a script. Pilot the guide once, ask for consent to record, and bring a second person to take notes.
- **During:** Ask about the past, not the future: "Tell me about the last time a campaign went to spam." Keep questions open and neutral, never leading ("Would you use…" teaches nothing). Listen more than you talk, and let silences run. Dig with "why" and "what happened next" until you reach the real reason. Do not pitch or demo, and do not defend the product. Write down exact quotes and what people do, not only what they say.
- **After:** Write a summary the same day, while it is fresh. Tag the notes and group them on an affinity map across interviews. Count how many people said a thing before calling it a pattern. Turn the patterns into journey map changes, A/B hypotheses and backlog items, and share them with the team with the quotes attached.
Sources: Steve Portigal, *Interviewing Users* (2nd ed., 2023); Rob Fitzpatrick, *The Mom Test* (2013); Nielsen Norman Group, user interviews.

### 10. Customer Journey Map (made-up data)
After her CJM artifact "Who We Build Warmy For" (claude.ai, 2026-10): personas, then a journey map per persona with the stages Attraction, Activation, Involvement, Retention and the rows Goal, Thoughts and feelings, Problems, Drop-off, Solution. All names, quotes, sizes and amounts here are made up and the text is rewritten; it shows the method, not Warmy's data. A note says so on the page.
Title: **Who we design for.** Text: Four personas from interviews and cancel reasons, and the journey each one takes. Pick a persona to see its map.

**Personas** (name · what they want · goal · role · size · story · why they cancel · average paid, made up)
1. **The Rescuer** · One-off · Fix one broken domain fast, then stop paying. · A marketing lead or COO whose domain landed in spam before a launch. · 20–300 employees, one or two domains · As a Rescuer, I want my domain back in the inbox within weeks, with a clear moment when the job is done, so I can return to sending. · Leaves happy when the fix works: "We're back in the inbox, thanks, we'll call you if it breaks again." · ≈ $700
2. **The Seasonal Sender** · One-off · Get mailboxes ready for a campaign, then pause. · A sales or marketing lead who sends cold email in campaigns, not all year. · 200+ employees, few mailboxes for their size · As a Seasonal Sender, I want mailboxes ready when a campaign starts and an easy pause when it ends, so I only pay while we send. · Cancels between campaigns: "We'll be back for the autumn push." · ≈ $900
3. **The Proof Seeker** · Long-term · See placement improve, with numbers to show the boss. · A head of growth or RevOps who has to justify the spend every quarter. · 50–200 employees, several sending domains · As a Proof Seeker, I want to see inbox placement rise within weeks, and why when it does not, so I can defend the budget. · Leaves when the numbers stall: "Opens didn't move, and I couldn't explain why." · ≈ $1,500
4. **The Agency Captain** · Long-term · Run many mailboxes and domains at a cost they can predict. · An agency owner sending for many clients across many tools. · 5–20 employees, 50+ mailboxes · As an Agency Captain, I want warm-up and seed tests to work with every tool my clients use, at volume, so I never build my own. · Leaves for an in-house tool or when a client's tool will not connect. · ≈ $3,200

**Journey map** (stage → Goal / Thoughts and feelings / Problems / Drop-off / Solution)
- **The Rescuer**
  - Attraction: Find a fix for this week. / "Our launch emails are in spam. Who can fix this now?" / Arrives in a hurry from search; needs proof Warmy fixes this exact case. / Low: they know what they need. / A landing page per problem, "domain in spam", with a realistic timeline.
  - Activation: Start the fix today. / "Just tell me what to do first." / DNS settings feel like a different language. / Medium if setup stalls. / A guided DNS check that says which record to change, in plain words.
  - Involvement: See the domain recover. / "Is it working yet?" / No visible finish line. / Medium: they guess when it's enough. / A progress line to a target placement and a clear "done" moment.
  - Retention: Nothing left to fix, keep costs down. / "Good service, but we don't need it now." / Warmy looks like a one-time repair. / High: the main drop-off. / A low-cost monitoring plan with alerts, and one click to come back.
- **The Seasonal Sender**
  - Attraction: Be ready before the next campaign. / "Last campaign half of it went to spam." / Compares many warm-up tools on price. / Medium: price shoppers. / Pricing by campaign length, shown up front.
  - Activation: Warm up the mailboxes in time. / "Will they be ready by the 1st?" / Unclear how many days warm-up needs. / Low. / A calculator: start date, volume, ready date.
  - Involvement: Run the campaign with no surprises. / "So far so good." / No warning before a mailbox gets tired. / Low during the campaign. / A daily health check per mailbox with alerts.
  - Retention: Pay only while sending. / "We'll pause until the autumn push." / No pause, only cancel. / High after each campaign. / A pause plan that keeps the reputation warm at a small cost.
- **The Proof Seeker**
  - Attraction: Find a tool that shows real placement. / "Our ESP says 99% delivered. I don't believe it." / Every tool claims better open rates. / Medium. / Case studies with before and after placement by provider.
  - Activation: Get the first proof within days. / "Show me something I can put in a report." / The first useful numbers come too late. / High if nothing shows in week one. / A seed test on day one, with a shareable report.
  - Involvement: Watch placement rise. / "Why did Outlook drop on Tuesday?" / Charts without reasons. / Medium. / Adeline explains each drop and links the fix.
  - Retention: Defend the budget each quarter. / "Can I show this was worth it?" / No summary of the value over time. / High when numbers stall. / A quarterly report: placement, revenue at risk, what was fixed.
- **The Agency Captain**
  - Attraction: One tool for every client's setup. / "Will it work with all our ESPs?" / Has to check integrations one by one. / Medium. / An integrations page searchable by tool, with limits listed.
  - Activation: Connect 50 mailboxes without pain. / "I can't add these one at a time." / Bulk import breaks on odd SMTP settings. / Medium. / Bulk import with a check that names each failed mailbox and why.
  - Involvement: Watch every client at a glance. / "Which client is in trouble today?" / Too many dashboards. / Low. / One view of all workspaces, sorted by risk.
  - Retention: Keep the cost predictable as they grow. / "Every new client raises the bill." / Price per mailbox grows faster than their fees. / Medium: may build in-house. / Volume plans for agencies and a client-billing export.

### 11. Campaign visuals
A moving row of her social posts and the print ad for iGaming CRM teams (the tiger mascot in a Warmy T-shirt), over WARMY repeated as a running line, as the mosaic on the Sport Guardian page, with the same 6 px tile corners and no frame around the tiles; same motion rules. Caption: **Campaign visuals.** Social posts and a print ad for iGaming CRM teams, in the brand's dark orange.

### 12. Back to all work.
