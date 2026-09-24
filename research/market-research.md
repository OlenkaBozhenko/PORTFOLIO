# Senior Product Designer — Job Market Research

**Date:** 2026-09-24 · **Purpose:** decide what the portfolio site must prove, and to whom.
**Markets:** Ukraine · Norway · Europe (Germany, Netherlands, Poland, UK) · USA.
**Detail and every source link:** [`sources/ukraine.md`](sources/ukraine.md) ·
[`sources/norway-europe.md`](sources/norway-europe.md) · [`sources/usa.md`](sources/usa.md) ·
[`sources/portfolio-expectations.md`](sources/portfolio-expectations.md).

**How to read the numbers.** Every figure comes from a named source in the detail files, tagged
`[read]` (read on the page), `[snippet]` (search-engine summary only — the site blocked access) or
`[calc]` / `[est]` (our own arithmetic or estimate). Currency: ECB rates of 2026-09-23 —
1 EUR = 1.1411 USD = 10.799 NOK = 0.8595 GBP = 4.3765 PLN.
**Not reached:** robota.ua and work.ua (HTTP 403 to automated requests), Glassdoor/StepStone pages
(snippets only), LinkedIn when logged out ignores the work-format filter.

---

## 1. Comparison table

| | 🇺🇦 Ukraine | 🇳🇴 Norway | 🇩🇪 Germany | 🇳🇱 Netherlands | 🇵🇱 Poland | 🇬🇧 UK (London) | 🇺🇸 USA |
|---|---|---|---|---|---|---|---|
| **Salary, senior (median)** | **$3,400 / month net** [calc from DOU raw data, n=46]; Djinni hired median **$3,300** | **NOK 780–863k / yr** gross | **€77.5–90k / yr** | **€81.6–87k / yr** | **PLN 257k / yr**; B2B ads PLN 20–28k / month | **£75–93k / yr** | **Base $150–210k**; total comp median **$210k** |
| **≈ EUR / year, gross** | **≈ €36–38k** [calc] | ≈ €72–80k (≈ €57k net after ~29% tax) [calc] | €77–90k | €82–87k | ≈ €55–59k | ≈ €87–108k | base ≈ €131–184k; TC ≈ €184k |
| **Range** | Q1–Q3 $2,760–4,330 / month; Lead median $4,200 | NOK 711k–1.01M | €67k–131k | €75k–127k | €50k–80k | £57k–188k | TC $160k–400k (Big Tech $250–360k) |
| **Sources** | DOU June 2026 survey, Djinni 30-day stats | levels.fyi (n=16), Glassdoor | levels.fyi (n=63), Glassdoor (n=550) | levels.fyi (n=22) | levels.fyi, Just Join IT ads | levels.fyi (n=58), IT Jobs Watch | levels.fyi (n=992), Built In, 16 live postings with pay |
| **Open roles (30 days)** | DOU: 11 "senior product designer"; Djinni: ~14 at 5+ yrs | LinkedIn: 53; NAV: ~4 true senior ads | LinkedIn: 515 | LinkedIn: 200 | LinkedIn: 199 | LinkedIn: 1,000+ | very large; 21 sampled |
| **Competition** | **~46 applications per vacancy**; employers' market | small market | 200+ applicants on JetBrains role | — | — | — | remote roles draw most applicants |
| **Experience asked** | 5+ yrs (11 of 15) | 5+ (lead 8+) | 5–8+ | 5+ | senior | mid–senior | 5–8+, median ~6 |
| **Language** | English **B2** usual, C1 in ~4 of 15 | English OK at product cos; **Norwegian required in ~2 of 5** | English | English | business English; some ads **Polish C1** | English | English |
| **Top hard skills** | Design systems (13/15), advanced Figma — variables, tokens (12/15), end-to-end ownership, **AI tools (9/15)**, prototyping, research, analytics | Design systems, research, prototyping, AI | Design systems (~17/20), Figma, **AI (~13/20)**, research, B2B data-dense UI | same as DE | same as DE | UX, Figma, **accessibility (29% of ads)**, interaction design | Visual craft (20/21), **metrics & experimentation (19/21)**, **AI (19/21)**, research, strategy, prototyping |
| **Top soft skills** | Cross-functional work (13/15), defending decisions (11/15), stakeholders, ownership, mentoring | Clear point of view, open to evidence | Cross-functional (~18/20), defending rationale, ownership, ambiguity | same | same | same | Storytelling (18/21), PM + engineering partnership (17/21), influence (14/21), ambiguity (13/21) |
| **AI expectation** | Claude Code / Cursor for **live prototypes** in ~6 of 15 ads | rising | named in most ads | named in most ads | named in most ads | rising | 8/21 expect AI in workflow; 5/21 want **AI-product** design; Decagon requires coding prototypes in Cursor / Claude Code |
| **Work format** | **Remote ~60%** (9 of 15), hybrid / office ~33%; remote and hybrid pay the same | onsite / hybrid in Oslo | hybrid 2–3 office days is the default; some fully remote (Jimdo) | hybrid 2–3 days | hybrid; B2B remote | only 4 of 41 ads remote | tech: remote ~35–40% [est]; all US ads: 87% onsite, trend toward the office |
| **Contract** | ФОП, Diia City (highest median, $3,000), staff | employment; foreign employer needs a Norwegian entity | employment; EU Blue Card from €50.7k | employment; HSM visa from €5,942 / month | **B2B (JDG)** dominant; needs Polish business registration | employment; Skilled Worker visa | employment; non-US via Deel contractor ($49 / month to employer) |
| **Realistic from Ukraine?** | yes | only with relocation (Ukrainian collective protection, 1-year renewals) | yes — EU-remote roles or relocation (temporary protection to Mar 2027) | via relocation | via relocation or B2B | rare | **"Remote US" = US residents only.** Realistic: global-remote companies (Remote.com $60–140k), EMEA roles at US companies (Linear, n8n, Canonical). Kyiv is +7h from New York |
| **Hiring process** | live critique / workshop 30–60 min | — | portfolio → take-home → panel (Finom) | — | — | — | **live 25-min Figma problem** in round one; portfolio walkthrough |

---

## 2. Salary at a glance (≈ EUR per year, gross, median)

```
USA (total comp)  ████████████████████████████████████  ≈ €184k
UK (London)       █████████████████████                 ≈ €106k
Germany           █████████████████                     ≈ €85k
Netherlands       ████████████████                      ≈ €84k
Norway            ███████████████                       ≈ €76k   (net ≈ €57k)
Poland            ███████████                           ≈ €57k
Ukraine           ███████                               ≈ €37k
```

**Takeaway.** A Ukrainian senior working for a Ukrainian company earns roughly half a Polish
senior and a fifth of a US senior. The realistic lift from Ukraine without relocating is
**EU-remote or global-remote roles** (≈ €55–120k), not "Remote US" postings.

---

## 3. What is the same in every market

1. **5+ years**, owning a product area end to end — discovery to release.
2. **Design systems** are the most-requested hard skill everywhere (13 of 15 in Ukraine, ~17 of 20 in Europe).
3. **AI fluency is the 2026 differentiator.** It is not the tool names — it is **working prototypes built in Cursor / Claude Code**, AI in the team's workflow, or experience designing AI products.
   Designer Fund 2026: 91% of designers use AI weekly, half have shipped AI-generated code; 50% of leaders weigh AI fluency when hiring.
4. **Metrics and business impact** — almost every US posting (19/21) and all serious Ukrainian product roles.
5. **Defending decisions** to stakeholders — the most common soft skill after collaboration.
6. **Accessibility (WCAG)** — a clear signal in regulated domains (health, fintech) and in 29% of UK ads.

---

## 4. What recruiters want to see in a senior portfolio

| Topic | What the sources say |
|---|---|
| **Number of cases** | **3–5**, focused (NN/g, Tom Scott). Figma's recruiter: 2–3 end-to-end. |
| **Case structure** (NN/g, 204 hiring managers) | Problem → your role and team → how solutions were developed → how they solved it → **challenges and rejected concepts** → user and business impact → lessons. |
| **Time spent** | ~10 s on the homepage, then 2–3 min per case if it earns it; 6–8 s first scan (UX Playbook). |
| **Outcomes first** | "Lead with outcomes, not process" (Tom Scott, 2026). Metrics or, failing that, concrete consequences. |
| **Seniority signals** | Initiative (co-writing the brief with the PM), product thinking (problem ≠ solution), scope (a product or vertical, several teams), trade-offs under uncertainty, influence across teams, mentoring. |
| **Recent and shipped** | "Show your most recent work, not your most polished old work." Shipped, traceable work beats concept redesigns. |
| **AI signal** | Interactive prototypes in Cursor / Claude, a case about **how you changed the team's workflow** (Buzz Usborne), Loom walkthroughs. "No AI signals" is a red flag. |
| **Homepage** | Say what you do in one line; projects one click away; nav = Work / About / Resume / Contact. |
| **NDA work** | Show artefacts, redact, or rebuild generically; put the password **in the application**; never a bare "can't share" slide. A fully locked site is a red flag. |
| **Web + mobile** | Poor mobile layout, uncompressed images, slow prototypes, no HTTPS — all on red-flag lists. |
| **Accessibility** | WCAG 2.2 AA baseline: one H1, semantic headings, keyboard access, visible focus, 4.5:1 contrast, alt text. |
| **Interview reality** | Live 25-min Figma problem in round one (US); 30–60 min critique or workshop (Ukraine); take-home + panel (EU). |

**Red flags:** "we" everywhere with no personal role · process theatre (double-diamond diagrams without outcomes) · no shipped work ·
a template more impressive than the work · too much text · heavy animation · typos and broken links · title claims Senior / Lead but shows feature-level scope · sameness.

---

## 5. Top 10 live senior portfolios (verified 2026-09-24)

| # | Designer | Role, region | Borrow this |
|---|---|---|---|
| 1 | [Josh Mateo](https://joshmateo.com) | Sr Manager, Design Systems, Netflix · US | Subtitle pattern: "Company · Project — the thesis"; case ends at org-level impact. |
| 2 | [Helena Stening](https://www.helenastening.com) | Google Meet, ex-Lead Spotify · Stockholm | Names rejected concepts and why; hard numbers (1.1% lift, ~250k subscribers / yr). |
| 3 | [Buzz Usborne](https://buzzusborne.com) | Principal, Help Scout · Sydney | The best "AI signal" case: design system rebuilt for AI, prompt-to-code tool. |
| 4 | [Bethany Heck](https://heckhouse.com) | Ex-Head of Product Design, Tumblr · US | Business case before design; clean dated index with type tags. |
| 5 | [Olivia Truong](https://www.oliviatruong.design) | Senior PD (Shopify work) · US | Case titles as the user's question; links to the live product; Cursor + Figma. |
| 6 | [Atul Khola](https://www.atulkhola.com) | Head of Design, Zero, ex-CRED · India | An "Influence" section (talks, mentoring, design system). ⚠ Desktop-only — do not copy that. |
| 7 | [Brian Lovin](https://brianlovin.com) | Designer, Notion AI · US | Portfolio as a product: shipped tools, writing, open source. |
| 8 | [Anthony Hobday](https://anthonyhobday.com) | Independent senior PD · UK | Fast plain HTML (~15 KB, 0.13 s) — performance as craft. |
| 9 | [Karolis Kosas](https://karoliskosas.com) | OpenAI, ex-Stripe · London | Tight index, one strong image per project. ⚠ Cases are 2014–16. |
| 10 | [Alexander Vilinskyy](https://www.vilinskyy.com) | Ex-Lead Grammarly, ex-Readdle · London | Named testimonials from collaborators as proof of influence. |

Not placed: Simon Pan (site fully password-locked, HTTP 401), Paul Stamatiou (own work page says "old, broken"),
Adrian Zumbrunnen (HTTP 410, gone). No Ukraine-based senior with a verifiable case-study site was found.

---

## 6. What this means for the PORTFOLIO site (implications, not decisions)

These follow from the research. Each is for the designer to decide.

1. **Target market.** The biggest salary lift without relocating is EU-remote and global-remote roles; Ukrainian product companies are the strongest local option ($3,400 vs outsourcing $2,500). The site's language and positioning follow from this choice.
2. **3–4 case studies, outcome first**, in the NN/g structure — with a visible "what I cut and why" block.
3. **DRON as the AI-and-systems case.** A design system with tokens, a measured contrast table, WCAG 2.1 AA and HIG conformance, and a clickable prototype built with Claude Code match three of the top requirements at once (design systems, accessibility, AI-built prototypes). Its domain also matches real openings (Six Robotics, Oslo — drone autonomy; Swarmer, Ukraine — defence tech).
4. **The site itself is evidence.** Mobile-first, fast, WCAG 2.2 AA, no heavy animation — the red-flag lists are about exactly this.
5. **Homepage: one line on who and what**, then the cases; Resume and Contact one click away. English primary; a Ukrainian version is optional for local applications.
6. **NDA work** shown redacted or rebuilt, with any password given in the application — not a locked site.
