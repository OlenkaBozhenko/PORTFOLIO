# Sport Guardian — project page content

**Source of truth for** [`SportGuardian.html`](SportGuardian.html), the page that opens from row 3 of the landing's work list (first build 2026-10-13).
Her brief (2026-10-13): a first screen in a rectangle of the thumbnail's teal, the logo on the left, a tilted tablet on the right playing a short donation flow (Cuberto, Zelt; later the same day replaced by the brand pieces first and the flow on a phone); then a grid of product images and brand goods like Reino Studio's GEN and Berrics cases and Maria Vasilyeva's DIIR (hoodie, cap, skateboards, an athlete drinking from a branded bottle on a football pitch, a poster), all in the project colours; at the end a moving mosaic of product screens and brand pieces (Reino Studio, GEN). References: [`inspiration.md`](inspiration.md) 2.8 and 2.9.

---

## Facts
| | |
|---|---|
| What it is | Idrettsfadder ("sports guardian"), a crowdfunding solution from Supporter.no: a sports club starts a campaign, private people and companies give once or every month, and the money covers what keeps children out of sport |
| English name | Sport Guardian (her choice, 2026-10-10) |
| Client | Scale Group AS (her answer, 2026-10-13); the product is sold under the Supporter.no name |
| Her role | UX, UI *(estimate from her Figma files: she drew every flow, from the donor form to the admin panel; to confirm)* |
| Year | 2023 *(estimate: the donor list in the screens is dated 21.09.2023; to confirm)* |
| Platform | Web, desktop and mobile, with an admin panel for clubs |
| Colours | Teal #418B91, Green #15EDA3 (Figma variables `418b91_idrettsfadder`, `idrettsfader`), white |
| Typefaces | Candal (the logo and the name), Open Sans (the product UI and the tagline) |
| Product URL in the screens | produkter.supporter.no/idrettsfadder |

Sources: her Figma file My-projects-new (`YlGWlsWWjKSCxhONMzGG2F`), section 3:71632 (all flows: Campaign_donor form, create campaign, image picker, club page, mobile, global donations page, crowdfunding, log in, admin panel) and 198:59192 ("material for presentation": the supporter.no product page and two annotated campaign pages), read 2026-10-13; her prototype in Scale-Development-AS (`0Wj3xZjV5rvwioVgaXGLRb`, node 1:31554) could not be read through Figma MCP (Starter plan limit), the same flows are in My-projects-new.

## Page copy
No em dashes in visible text (her rule).
- **Back link:** ← All work
- **Eyebrow:** Web platform for Scale Group AS
- **Headline:** A fundraising page any sports club can open in minutes, so no child leaves sport because of money.
- **Meta row:** Role — UX, UI · Year — 2023 · Platform — Web, mobile web · Client — Scale Group AS
- **About:** Sport Guardian (Idrettsfadder in Norwegian) is a crowdfunding solution from Supporter.no. A club starts a campaign, and private people and companies become its sports guardians: they give once or every month, and the money covers fees, gear and travel for children whose families cannot pay.
- **Problem:** Sport costs money, and the cost is what makes children quit first. 185,000 Norwegians cancelled a sports club membership last year, and the drop was largest among children and young people *(figure as quoted on produkter.supporter.no/idrettsfadder in her presentation frame 198:59192; the page shows no date)*. Clubs had no simple way to ask their community for help.
- **Solution:** A campaign page that shows the countdown, the amount raised and the people behind it, and a donation that takes four choices: private person or company, once or recurring, the amount, then card or Vipps. Behind it, a builder that lets a club publish a campaign without help, and an admin panel with donors, refunds and statistics.

## Blocks
Order (2026-10-13, her request, last change): header → the moving mosaic → About / Problem / Solution → Product → the hoodie photo as a divider → Brand. Every block stays inside the page's grid, like every other block on her site.
1. **Header** — back link, eyebrow, headline, meta row; the page starts with it, like every other project page.
2. **Mosaic** (first under the header, her request) — after GEN: on a teal ground, the title SPORT GUARDIAN · PRODUCT AND BRAND in very large capitals as a running line, then **two** rows of straight tiles sliding sideways, the second the other way (her request: one row less, its tiles moved into the second row; the whole SG mark replaces the cropped lockup tile; the clubs overview tile is replaced by two mobile payment screens, Payment options and Payment by card). One Pause button stops the title and the rows; with reduced motion they stand still.
3. **About / Problem / Solution** — label left, text right, as on the School page.
4. **Product** (from the donor to the club's admin), on 12 columns:
   - the phone (1–4) playing the donor flow in a loop: the campaign page scrolls down and back under its fixed status bar, address bar and menu bar, with her fixed bottom bar (Our donors, Donate) and the browser toolbar always on screen; a tap on Donate; the donation form (Private person, Recurring); a tap on 600 NOK; a tap on Donate; Payment options; a tap on Credit card; Payment by card; a tap on Pay; Thank you. A small round pointer moves between the taps and rings on each one. A Pause button under the phone (WCAG 2.2.2); with reduced motion the phone shows the page, still. Frames: `m-bar.webp`, `m-form-1.webp`, `m-form-2.webp`, `m-step-3.webp` … `m-step-5.webp` (750 × 1624), built with [`tools/sport-guardian/mobile_frames.py`](tools/sport-guardian/mobile_frames.py) from her mobile frames 3:82411 (the page with her bottom bar) and 3:82469 (the donation form, redrawn in Open Sans with 16 pt side margins on both sides, her request: in her frame the content runs past the right edge; the total "2200 NOK, 200 donors" becomes a teal card with the same margins), and the payment cards shown at full phone width (there are no mobile frames for those steps); the page itself is `screen-mobile-head.webp` + `screen-mobile-body.webp`. The phone panel grows with the phone, so the phone is never cut on narrow screens. (The earlier tablet version, `tablet_frames.py`, is retired; its images are deleted.)
   - the desktop campaign page in a browser frame, scrolling slowly under its fixed header, on a pale panel (5–12);
   - caption "Three steps after Donate" (1–4); the three payment cards staggered on a pale panel (5–12);
   - the donor list on a teal panel (1–4); the campaign builder's "Accept donations from / Select donation frequency" block on a pale panel (5–12): single elements, as she asked, since the full builder page is not its best side;
   - the campaign statistics in the admin panel in a browser frame, scrolling under the fixed admin nav (1–12). The five frequency cards are redrawn as modern dashboard cards ("like crypto dashboards, with charts"): label and donor count, the amount, a growth chip, a small area chart with a gradient; One-time fee is the highlighted dark card with a green chart; chart data is made up ([`tools/sport-guardian/stat_cards.py`](tools/sport-guardian/stat_cards.py)). The caption runs in two lines (64ch).
   Fixed headers: each long screen is cut into a header strip and a body (`*-head.webp`, `*-body.webp`) by [`tools/sport-guardian/fix_screens.py`](tools/sport-guardian/fix_screens.py). The same script replaces placeholder texts in the admin screens with made-up names: the statistics title "Become a sports guardian" and donors Ingrid Solberg, Magnus Hansen, Sofie Lie; the campaigns "Swimming for everyone", "Junior squad 2024"; the clubs Fjordby Svømmeklubb, Nordlys Fotball, Elvebakken Tennis. Not real people or clubs.
5. **Divider** — the hoodie photo (the mark alone on its back) across the full width of the grid, 16:8, between Product and Brand (her request).
6. **Brand** (mockups, not a real campaign):
   - the logo banner: the lockup (mark, SPORT GUARDIAN, GIVE SPORTS ENJOYMENT, left-aligned on the trail's left edge) on the brand teal (1–12), alt "Sport Guardian, give sports enjoyment…"; the green tagline on teal is part of the logo, which WCAG 1.4.3 exempts; under it the caption "The mark" (1–5);
   - caption "On the street" (1–4), the poster (5–8), the bottle photo (9–12), the small mark on her shirt set on the chest;
   - caption "In the club" (1–3), the skateboards (4–12);
   - the cap (1–8), the mark alone, centred on the front panel between the top seam and the brim.
   Photos: AI images generated with Figma AI (gpt-image-2.5, her Pro plan, 2026-10-13), not real people or places; the SG mark is printed on them from the vector master with [`tools/sport-guardian/print_photo.py`](tools/sport-guardian/print_photo.py) (it takes the light of the fabric or surface). The poster line "Back a young athlete near you." is placeholder copy written for the mockup.
7. **Back to all work.**

## Logo
- Vector master: [`tools/sport-guardian/sg_svg.py`](tools/sport-guardian/sg_svg.py) → `sg-mark.svg` (white S, green G), `sg-mark-teal.svg` (teal S, green G, for white grounds), `sg-mark-on-green.svg` (teal S, white G, for green grounds). Built from the Candal glyph outlines (OFL), so no font is needed to show it.
- The landing thumbnail (`sport-guardian-mark.webp`) is the same construction.
