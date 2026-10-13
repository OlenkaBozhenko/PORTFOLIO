# Sport Guardian — project page content

**Source of truth for** [`SportGuardian.html`](SportGuardian.html), the page that opens from row 3 of the landing's work list (first build 2026-10-13).
Her brief (2026-10-13): a first screen in a rectangle of the thumbnail's teal, the logo on the left, a tilted tablet on the right playing a short donation flow (Cuberto, Zelt); then a grid of product images and brand goods like Reino Studio's GEN and Berrics cases and Maria Vasilyeva's DIIR (hoodie, cap, skateboards, an athlete drinking from a branded bottle on a football pitch, a poster), all in the project colours; at the end a moving mosaic of product screens and brand pieces (Reino Studio, GEN). References: [`inspiration.md`](inspiration.md) 2.8 and 2.9.

---

## Facts
| | |
|---|---|
| What it is | Idrettsfadder ("sports guardian"), a crowdfunding solution from Supporter.no: a sports club starts a campaign, private people and companies give once or every month, and the money covers what keeps children out of sport |
| English name | Sport Guardian (her choice, 2026-10-10) |
| Client | Supporter.no, product built at Scale Development AS *(her Figma file is named Scale-Development-AS; to confirm with her)* |
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
- **Eyebrow:** Web platform for Supporter.no
- **Headline:** A fundraising page any sports club can open in minutes, so no child leaves sport because of money.
- **Meta row:** Role — UX, UI · Year — 2023 · Platform — Web, mobile web · Client — Supporter.no
- **About:** Sport Guardian (Idrettsfadder in Norwegian) is a crowdfunding solution from Supporter.no. A club starts a campaign, and private people and companies become its sports guardians: they give once or every month, and the money covers fees, gear and travel for children whose families cannot pay.
- **Problem:** Sport costs money, and the cost is what makes children quit first. 185,000 Norwegians cancelled a sports club membership last year, and the drop was largest among children and young people *(figure as quoted on produkter.supporter.no/idrettsfadder in her presentation frame 198:59192; the page shows no date)*. Clubs had no simple way to ask their community for help.
- **Solution:** A campaign page that shows the countdown, the amount raised and the people behind it, and a donation that takes four choices: private person or company, once or recurring, the amount, then card or Vipps. Behind it, a builder that lets a club publish a campaign without help, and an admin panel with donors, refunds and statistics.

## Blocks
1. **First screen** — a rectangle in the brand teal with rounded corners, wide (the page's 12 columns). Left: the logo lockup (the chosen "Speed" SG mark, SPORT GUARDIAN in Candal, GIVE SPORTS ENJOYMENT in Open Sans Bold Italic), one image, `sg-lockup.webp`, alt "Sport Guardian, give sports enjoyment"; the green tagline on teal is part of the logo, which WCAG 1.4.3 exempts. Right: a tablet tilted in perspective after the Zelt reference, playing the donor flow in a loop: the campaign page; a tap on Recurring; a tap on 600 NOK; a tap on Donate; Payment options (600 NOK monthly, cover the transaction cost); a tap on Credit card; Payment by card; a tap on Pay; Thank you. A small round pointer moves between the taps and rings on each one. Frames: `flow-1.webp` … `flow-6.webp` (1440 × 900), built with [`tools/sport-guardian/tablet_frames.py`](tools/sport-guardian/tablet_frames.py) from her Figma exports (campaign page 3:72548 at 2x; cards 3:75350, 3:75437, 3:75581 at 2x over the page header of 3:71652); the selected Recurring and 600 NOK states are redrawn in Open Sans. A Pause button stops it (WCAG 2.2.2); with reduced motion it shows the campaign page, still.
2. **Header** — back link, eyebrow, headline, meta row.
3. **About / Problem / Solution** — label left, text right, as on the School page.
4. **Product and brand grid** — after GEN (a wide photo overlapping a teal band, then images set off to the right of an empty column) and the DIIR wireframe (images of different sizes on different columns, UI pieces on pale panels). On 12 columns:
   - teal band behind the top; the hoodie photo wide (columns 1–9), a short caption in columns 10–12;
   - an empty column with a caption (1–4), the poster tall (5–8), the mobile campaign page in a phone outline, scrolling slowly (9–12);
   - the desktop campaign page in a browser frame, scrolling slowly, on a pale panel (1–8); the donor list on a teal panel (9–12);
   - a caption (1–3), the skateboards wide (4–12);
   - the bottle photo tall (1–5); the three payment cards staggered on a pale panel (6–12);
   - the cap (1–6); the campaign builder's "Accept donations from / Select donation frequency" block on a pale panel (7–12): single elements, as she asked, since the full builder page is not its best side;
   - the campaign statistics in the admin panel, wide on a pale panel (1–12).
   Photos: AI images generated with Figma AI (gpt-image-2.5, her Pro plan, 2026-10-13), not real people or places; the SG mark is printed on them from the vector master with [`tools/sport-guardian/print_photo.py`](tools/sport-guardian/print_photo.py) (it takes the light of the fabric or surface). The poster line "Back a young athlete near you." is placeholder copy written for the mockup (2026-10-13). Mockups, not a real campaign.
5. **Closing mosaic** — after GEN: on a teal ground, three rows of tiles sliding sideways, the middle row the other way; product screens (campaign page, club campaigns, shop, crowdfunding, admin campaigns, clubs overview, statistics, the campaign published screen, image picker, the payment cards) mixed with the brand pieces (hoodie, cap, decks, bottle, poster, the mark). A Pause button; with reduced motion the rows stand still.
6. **Back to all work.**

## Logo
- Vector master: [`tools/sport-guardian/sg_svg.py`](tools/sport-guardian/sg_svg.py) → `sg-mark.svg` (white S, green G), `sg-mark-teal.svg` (teal S, green G, for white grounds), `sg-mark-on-green.svg` (teal S, white G, for green grounds). Built from the Candal glyph outlines (OFL), so no font is needed to show it.
- The landing thumbnail (`sport-guardian-mark.webp`) is the same construction.
