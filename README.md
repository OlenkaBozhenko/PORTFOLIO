# PORTFOLIO — Olena Bozhenko, Senior Product Designer

Personal portfolio website of **Olena Bozhenko**, a senior product designer based in Oslo, working remotely with a Ukrainian product team on B2B SaaS. The site is built for her Senior Product Designer job search in Ukraine, Norway, Europe and the USA.

**Live preview → [Olena Bozhenko](https://claude.ai/artifact/TZajshUY8roLsqNuWBmrZV)** · source: [`Olena Bozhenko.html`](Olena%20Bozhenko.html)

The preview is a private Claude Artifact: it opens for the owner and for people she shares it with from the page's Share menu. It is built from the landing by `tools/build-preview.py`, which also leaves out any testimonial marked DRAFT. After changing the landing, rebuild and republish the preview so the link shows the current version.

## What is on the landing page
- **Hero** — a large headline surrounded by outlined interface and code blocks (Figma component icons, `</>` code icons) that drift and can be dragged within the first screen; a Play / Pause music control.
- **Selected work** — AnyBiz, Warmy, Idretsfader, Book, Styupan Translation, School and DRON: name, description, role, year, platform and a large preview.
- **About** — portrait, short bio and personal qualities.
- **Testimonials** — clients and collaborators.
- **Learning** — certificates and conferences.
- **Contact** — email, LinkedIn, Behance and the **[resume PDF](assets/Olena-Bozhenko-Resume.pdf)**.
- A circle cursor on mouse and trackpad; mobile-first layout; WCAG 2.2 AA checks recorded in `site.md`.

## Files
| File | Role |
|---|---|
| [`Olena Bozhenko.html`](Olena%20Bozhenko.html) | The landing page |
| [`site.md`](site.md) | Source of truth for the landing: structure, copy, standards |
| [`cv.md`](cv.md) | CV facts, learning, testimonial candidates |
| [`resume.md`](resume.md) → [`resume.html`](resume.html) → [`assets/Olena-Bozhenko-Resume.pdf`](assets/Olena-Bozhenko-Resume.pdf) | Black-and-white one-page resume |
| [`inspiration.md`](inspiration.md) / [`inspiration.html`](inspiration.html) | Visual references and the designer's decisions |
| [`research/market-research.md`](research/market-research.md) | Senior Product Designer job market: Ukraine, Norway, Europe, USA |
| [`tools/build-preview.py`](tools/build-preview.py) | Builds the preview copy of the landing for the Claude Artifact |
| [`CLAUDE.md`](CLAUDE.md) | Project brief and working rules |

## Working rules
- `.md` files are the source of truth; HTML is the display layer and is updated after the `.md`.
- All file contents are in English.
- Every design decision is checked against WCAG 2.2 AA.
