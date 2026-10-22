# AGENTS.md

Rules for anyone (or any agent) working on this repository.

## Scope

This repository holds the survivor library: articles, their images, the static app and the build. Keep the code, the content and the docs in English.

## Articles

- One file per article in `documents/<SECTION>/`. The section codes are fixed: WTR, FIR, SHL, FOD, MED, COM, PWR, NAV, SEC, TLS, HYG, PSY.
- Frontmatter keys, in this order: `id` (`<SECTION>-NN`), `type: guide`, `title`, `description`, `section`, `tags`, `timestamp`, `origin` (`generated` or `converted`), `review: pending`. Quote any value that contains `: `.
- Body: one `#` title, then `##` sections, numbered steps, bullets, bold for key warnings, and one closing `**Warning:**` line.
- Length: 800 to 1000 words of body text for a new article. Do not publish stubs under 700 words.
- Images: each article has 3 to 5 markers, each as its own blockquote line placed next to the text it illustrates:
  - `> @svg <description>` for a diagram still to compose. Once composed, the line becomes `![<description>](assets/<doc>-<n>.svg)` and the file lives in `assets/<SECTION>/`.
  - `> @image <description of the real photo or source drawing needed>` for a photo or a source drawing.
  - A real image is written as `![alt](assets/<name>.png)` directly after its marker, and its file lives in `assets/<SECTION>/`.
- Medical content uses `@image` only for source drawings, never AI-generated images.

## Content rules

- No citations, no source names, no "according to", no links to the original sources.
- No recipes (ingredient lists and method for a dish). General preservation methods are fine.
- Do not invent facts. Where a claim needs checking, say so in the review note, not in the article.
- Cross-references use the exact title of an existing article, or plain text.
- No code comments in any file.
- `review: pending` stays until a person has reviewed the article. Do not change it.

## Diagrams

- Diagrams are generated, not hand-drawn. Each one is a function in `tools/diagrams/designs_*.py`, keyed `<SECTION>/<doc>-<n>`, where `n` counts the diagram markers of the article from the top.
- `python3 tools/diagrams/build.py [key-prefix] [--preview DIR]` writes the SVG files into `assets/<SECTION>/`. `--preview` also renders a PNG per diagram (macOS Quick Look). Look at every changed diagram rendered before shipping it: no overlapping or clipped text, no floating leaders.
- Objects come only from the piece catalog, `assets/elements/<board>/<name>.svg`. The generator may draw only structure: arrows, lines, leaders, numbered badges, tick and cross marks, tables, text boxes and text. Never draw an object. If a piece is missing, name it in a text label and add the piece to the catalog first.
- New pieces come from the design boards: `python3 tools/diagrams/extract_elements.py <boards_dir>` adds the pieces that are not in the catalog yet.
- `tools/diagrams/pending.txt` lists the diagram markers that still have no design, with their description.
- `python3 -m unittest discover -s tools/diagrams -p "test_*.py"` must pass.

## Build and deploy

- `python3 tools/build.py` must finish without errors before any change is considered done.
- `docker compose up -d --build` deploys the site.
- Do not add generated files (`dist/`, indexes) to git.

## Git

- Do not commit or push unless the maintainer asks in the same turn.
