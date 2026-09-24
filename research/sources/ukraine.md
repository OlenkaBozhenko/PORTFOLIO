# Ukraine — Senior Product Designer market (2026-09-24)

Sources checked: DOU, Djinni. **robota.ua and work.ua returned HTTP 403** to automated requests (their search API too) — no data from them.
**Net vs gross:** DOU figures are **net** (after tax). Djinni does not say. Gross estimate for ФОП group 3 [est]: gross ≈ net ÷ 0.95 + ~$45 social contribution.

## 1. Salary (USD / month)

### DOU salary survey, June 2026
Report: https://dou.ua/lenta/articles/salary-report-non-tech-summer-2026/ · raw data: https://github.com/devua/csv/tree/master/salaries (`2026_june_raw.csv`)

Read from the article (net):
- UI/UX / Product Design overall median **$2,475** (n=307).
- Company type: product **$2,900** · service $2,000 · non-IT $2,730.
- Company size: ≤50 $2,275 · ≤200 $2,275 · ≤1,000 $2,300 · 1,000+ $2,755.
- Employment: Diia City **$3,000** · gig contract $2,555 · ФОП $2,500 · staff $2,187.
- Format: remote $2,500 · hybrid $2,400.
- Living in Ukraine $2,400 vs abroad $3,000. 10+ years: $3,550.
- Change since winter: Senior −$150, Lead −$247, Middle +$100, Junior +$150.
- The article gives Senior medians only in chart images.

Calculated from the raw CSV [calc] (people living in Ukraine, net). Check: overall for the two roles = $2,400 vs DOU's $2,475.

| Group | n | Q1 | Median | Q3 |
|---|---|---|---|---|
| Senior Product Designer | 46 | 2,758 | **3,400** | 4,325 |
| Senior UI/UX Designer | 35 | 2,100 | 2,800 | 3,400 |
| Senior, both roles | 81 | 2,500 | 3,000 | 4,000 |
| Lead, both roles | 18 | 3,112 | **4,200** | 5,000 |
| Senior at a product company | 41 | 2,725 | 3,400 | 4,450 |
| Senior at outsourcing | 18 | 2,080 | 2,500 | 3,000 |
| Senior at outstaffing | 6 | 2,850 | 3,645 | 4,900 |
| Senior at non-IT (bank, telecom) | 11 | 2,760 | 3,500 | 4,050 |
| Senior, Advanced English | 17 | 3,145 | 3,500 | 5,000 |
| Senior, Upper-Intermediate English | 37 | 2,450 | 3,000 | 4,000 |
| Senior living abroad | 31 | 3,000 | 3,500 | 4,800 |

- Trend [calc]: December 2025 Senior Product Designer n=60, median $3,500 → about −$100 by June 2026.
- Gross estimate [est]: $3,400 net ≈ **$3,620 gross** for a ФОП.

### Djinni (rolling 30 days, read 2026-09-24)
- Product Design, 5+ yrs — https://djinni.co/salaries/?category=product_design&exp=5 : candidate expectations **$2,650–4,000**; vacancy median range $2,000–4,500; **hired median $3,300**.
- UI/UX, 5+ yrs — https://djinni.co/salaries/?category=ui_ux&exp=5 : expectations $2,000–3,300; vacancies $2,000–4,000; hired median $3,500.
- Product Design, 3–5 yrs: expectations $1,800–3,000; vacancies $2,000–3,500.
- Djinni blog, 2025-10-30 (https://blog.djinni.co/post/design-it-market): hired designers 7+ yrs $3,000 → $3,100.

### Salaries printed in vacancies
- jito.dev Sr Poker Product Designer **$4,000–8,900** — https://djinni.co/jobs/825370-sr-poker-product-designer-sr-poker-ui-ux-desi/
- jito.dev second role up to $7,000 — https://djinni.co/jobs/825411-senior-poker-product-designer/
- Miaplaza €60–90k / yr — https://djinni.co/jobs/848623-senior-product-designer-illustration-and-moti/
- bodo, 5+ yrs, ₴120,000 / month + bonuses (≈ $2,900 at an assumed 41–42 UAH/USD) — https://djinni.co/jobs/846351-product-designer/
- None of the 11 DOU senior PD vacancies showed a salary.

## 2. Vacancy volume and trend
- DOU (read 2026-09-24): Design category **260**; "product designer" **39**; "senior product designer" **11** — https://jobs.dou.ua/vacancies/?category=Design&search=senior+product+designer
- Djinni: Product Design keyword **30** jobs, ~6 senior. Product Design 5+: **14 jobs, 839 candidates, 45.6 applications per vacancy**. UI/UX 5+: 13 jobs, 867 candidates, 49.1 per vacancy.
- Djinni Oct 2025: ~7,000 designers for ~300 vacancies; seniors 25% → 35% of the pool (https://blog.djinni.co/post/design-it-market).
- Finance.ua 2026-04-27: designers get the fewest offers (~3 on average) — https://news.finance.ua/ua/rynok-praci-v-it-na-skil-ky-vakansiy-treba-vidhuknutys-shhob-znayty-robotu-v-2026

## 3. Requirements in 15 current vacancies

| Company | Link | Years | English | Domain | Tools / notable |
|---|---|---|---|---|---|
| Ciklum | https://jobs.dou.ua/companies/ciklum/vacancies/368328/ | 5+ | Fluent | BFSI, crypto, retail | Figma, design systems, discovery; HTML/CSS/JS a plus; mentoring |
| Sombra | https://jobs.dou.ua/companies/sombra/vacancies/371856/ | 5+ | — | Real estate (MENA) | AI tools for research and prototyping, data-informed design |
| Anadea | https://jobs.dou.ua/companies/anadea/vacancies/372492/ | senior | Native / full professional | US B2C | Figma variables, modes, Dev Mode; Amplitude; conversion |
| Ekreative | https://jobs.dou.ua/companies/ekreative/vacancies/361941/ | 5+ | — | iOS consumer SaaS | Figma AI, Claude, Rive, Lottie, ProtoPie; Apple HIG |
| Phenomenon Studio | https://jobs.dou.ua/companies/phenomenon-studio/vacancies/371642/ | 5+ | B2+ | SaaS, health, fintech | Figma tokens; Hotjar, Amplitude; Claude Code / Cursor prototypes; **metrics case mandatory** |
| PFP agency | https://jobs.dou.ua/companies/pfp-agency/vacancies/373796/ | 4–7+ | — | B2C mobile | A/B tests in Amplitude / Mixpanel; paywalls, onboarding |
| Binariks (part-time) | https://jobs.dou.ua/companies/binariks/vacancies/373193/ | senior | B2+ | Medical devices | WCAG 2.2, IEC 62366, FDA human factors |
| AnyHR | https://jobs.dou.ua/companies/anyhr-io/vacancies/370999/ | — | — | SaaS, D2C | Claude Code, Cursor, Next.js, React, Tailwind |
| Alliance Digital (inactive) | https://jobs.dou.ua/companies/tov-alyans-didzhital/vacancies/368471/ | 5+ | — | Mobile banking | Figma libraries, data-heavy UI |
| Swarmer | https://jobs.dou.ua/companies/swarmer/vacancies/371883/ | 5+ | EN + UA | **Autonomous systems, command and control** | Figma, Claude Code, Cursor, Codex; **military reservation offered** |
| TEAM International (Lead) | https://jobs.dou.ua/companies/team-international/vacancies/372467/ | lead | — | Fintech | WCAG 2.2 AA, design-system governance, coaching |
| Sysmetica | https://djinni.co/jobs/849640-senior-product-designer/ | 5+ | B2 | MedTech | Figma, research, WCAG 2.1 AA, AI tools |
| Gemicle | https://djinni.co/jobs/843178-senior-product-designer-only-vinnytsia/ | 5+ | C1 | Enterprise SaaS | Claude Code, Cursor, Copilot |
| jito.dev | https://djinni.co/jobs/825370-sr-poker-product-designer-sr-poker-ui-ux-desi/ | 5+ | B2 | Gambling | Analytics-heavy UX; AI interfaces |
| bodo | https://djinni.co/jobs/846351-product-designer/ | 5+ | B2 | Marketplace, travel | Figma, Claude, Cursor, A/B tests |

**Hard skills (of 15):** design systems ~13 · advanced Figma ~12 · end-to-end ownership ~11 · prototyping ~10 · AI tools ~9 (Claude Code / Cursor named in ~6) · research ~8 · analytics ~6 · HTML/CSS ~5 · mobile guidelines ~5 · A/B testing ~4 · accessibility ~4 · motion ~2.
**Soft skills (of 15):** cross-functional ~13 · defending design rationale ~11 · stakeholders ~8 · ownership / ambiguity ~8 · product & business thinking ~6 · mentoring ~5.

## 4. Work format and contract
- ~9 of 15 fully remote; ~5 hybrid / office (Kyiv, Lviv, Vinnytsia, Cherkasy).
- DOU: remote median $2,500 ≈ hybrid $2,400.
- No vacancy requires relocation; TEAM International also hires in Lisbon and Lublin.
- Military reservation mentioned only by Swarmer.
- Contract type mostly unstated; Diia City pays the highest median ($3,000), ФОП $2,500.

## 5. What Ukrainian hiring managers want in a portfolio
From current vacancies: a case with measurable metric impact (Phenomenon, mandatory); shipped live products with personal contribution spelled out (Ekreative, PFP, AnyHR); problem → solution → result (bodo); discovery-to-release cycles with AI / code prototypes (Swarmer).
- Kristina Holysheva, Hirey.io, DOU 2021 — https://dou.ua/lenta/columns/how-to-make-design-portfolio/ : 10–15 people see a portfolio; 80% of recruiters spend under 3 minutes; state role and team; problem, solution, outcome with data; ~60% text / 40% images for UX; seniors stand out through storytelling.
- Anatoly Rubtsov, DataArt, DOU 2017 — https://dou.ua/lenta/articles/designers-portfolio-as-ux-task/ : step-by-step cases; justify every decision; show business goals hit.
- ITExpert 2022 — https://itexpert.work/uk/z-chogo-pochaty-rekrutyng-seniornogo-ui-ux-dyzajnera-v-komandu-dosvid-ta-komentari-senior-team-lead-designers/ : a portfolio of only links is insufficient; interviews often include 30–60 min live critique or workshop.
