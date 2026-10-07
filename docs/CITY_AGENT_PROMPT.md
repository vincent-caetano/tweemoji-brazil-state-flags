# Bring your city flag to the collection

Replace the two values below and give the entire prompt to your coding agent. An IBGE code or official flag reference is optional at the start; the agent must verify them before drawing. This prompt authorizes the agent to publish **one ready-for-review PR from your fork**, never to push directly to the upstream repository or merge its own PR.

```text
CITY = "YOUR CITY"
STATE = "UF"

Contribute an original Twemoji-inspired flag for CITY, STATE, Brazil, to:
https://github.com/vincent-caetano/tweemoji-brazil-state-flags

Complete one focused contribution from research through a ready-for-review
pull request. Follow the repository's current AGENTS.md if present,
CONTRIBUTING.md, docs/DESIGN.md, cities/README.md, metadata example and PR
template. Repository instructions win if this prompt becomes outdated.

1. SETUP AND DUPLICATE CHECK
Use git for local work and the authenticated gh CLI for GitHub operations.
Inspect the local checkout before changing files. Clone into a separate
folder if the current project is unrelated. Fetch upstream main. Search
cities/, issues and open PRs by city name, UF and IBGE code. If the locality
already exists, review it and propose a focused correction instead of a
duplicate. Do not overwrite other work, expose credentials, or change
repository settings. Use a branch named feat/city-<uf>-<ibge-code>.

2. VERIFY THE LOCALITY AND FLAG
Confirm the official locality name and seven-digit IBGE identifier from
IBGE. Confirm the UF. Find the original flag in a prefeitura publication,
municipal law, official manual or another primary source. Record source
URLs, titles and access dates. Inspect the actual reference image, not
only a search snippet. Wikimedia may help locate and compare a reference,
but prefer a primary source. If the city is ambiguous, sources conflict,
or an official flag cannot be established, ask me the smallest necessary
question and do not invent a flag or claim verification.

3. DRAW AN ORIGINAL VECTOR
Inspect several existing flags, including a simple field and a detailed
crest, and match the documented design system. Write editable SVG geometry;
do not use an image generator or embed a raster. Use viewBox="0 0 36 36",
a flag body from y=5 to y=31, width 36 and rounded corners rx=4, with
transparent padding. Preserve field order, canton, stripes, distinctive
symbols and important star counts. Simplify tiny heraldry for 18–36px.
Use flat colors from the existing palette, no shadows, gradients, outer
outlines, fonts, scripts, foreignObject or external resources. SVG IDs must
be unique within the file, and references must be local. Add a title and
description identifying the locality and meaningful simplifications.
Do not copy or trace third-party SVG paths. If reuse is genuinely needed,
establish compatible licensing, retain attribution and disclose it; do
not assume official publication makes a digital illustration free to copy.

4. ADD THE CONTRIBUTION
Use cities/BR/<UF>/<IBGE-code>/ with:
- flag.svg: the editable city master
- metadata.json: fill every required field from docs/CITY_METADATA.example.json
- README.md: locality identity, linked original source, simplification notes,
  and a small original-versus-emoji comparison at 36px
- png/36.png, png/72.png, png/144.png, png/512.png: generated exports
Keep original reference images external. Do not add a website or hosting.
Do not add cities to the 27-entry state metadata, state generator or
React Native state component. Credit me as contributor only after checking
my GitHub identity; ask if my preferred public name is unknown. Use
CC-BY-4.0 for my original artwork and MIT for my code/documentation, as
required by the contribution policy. Never accept licensing on my behalf
for third-party artwork I do not own.

5. EXPORT, TEST AND VISUALLY REVIEW
Install with npm ci --ignore-scripts. Run npm run export:cities and npm run
verify. Inspect the actual output at 18, 24 and 36px against the original,
on light and dark backgrounds. Fix incorrect composition and muddy symbols.
Keep the local README comparison at 36px and include visual review evidence
in the PR. Report exactly which checks ran and any remaining uncertainty.
The checks do not certify the official design or the locality identity.
Avoid unrelated dependencies, broad refactors or edits to other cities.

6. SUBMIT ONE PULL REQUEST
Review the diff and check for secrets, machine paths and temporary files.
Commit only the city's assets, metadata and documentation. Create or use my
fork with gh, keep upstream pointing to the original repository, and push
the task branch to my fork. Open a non-draft PR against upstream main with
an explicit base/head and the repository PR template. Title it:
"Add <CITY>, <UF> city flag (<IBGE-code>)".
Include primary sources, original/emoji comparison, preserved and omitted
details, contributor credit, licensing statement and actual validation.
Use gh pr create with --body-file to preserve Markdown. Attach the PR to
this chat if the environment provides that capability. Verify the PR URL
and checks. Do not merge, change upstream settings, create a release or
push directly to upstream main. If authentication or publishing permission
is unavailable, leave a complete reviewed local contribution and explain
the exact remaining step. End with the preview, checks and PR link.
```

The prompt is a starting point, not an accuracy guarantee. Review the generated artwork and PR before sharing it. No flag should be fabricated merely to increase coverage.
