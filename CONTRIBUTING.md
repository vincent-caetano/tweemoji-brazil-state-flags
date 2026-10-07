# Contributing

Flag corrections, clearer small-size symbols, accessibility improvements and exporter fixes are welcome.

1. Open an issue with the state code, the problem, and a link to a reliable flag reference.
2. Change geometry in `scripts/build.py`, preserving the 36×36 canvas and shared silhouette.
3. Run `npm ci --ignore-scripts`, `npm run build`, `npm run export`, and `npm run verify`.
4. Include regenerated assets and a before/after preview in your pull request.

Keep colors flat and crests readable at 18–36px. Avoid embedded images, external SVG references, font-dependent text, gradients, shadows, and additional outer strokes. Document meaningful simplifications in metadata.

For an export-only revision to existing SVG masters, skip `npm run build`: it overwrites SVG edits. Before contributing, transfer those edits into the generator so that CI can reproduce them.

Contact-sheet PNGs may differ across systems because preview labels use system fonts. SVGs, metadata and the React Native component must regenerate without changes.

Please identify the source and license of any third-party material proposed for inclusion. Reference thumbnails and copied upstream flag SVGs do not belong in the distributed set.

## City flags

Help extend the collection one locality at a time. An issue is encouraged to avoid duplicate work, but a complete PR may be submitted directly.

1. Search `cities/`, open issues and PRs for your city and IBGE code. Use the **City flag contribution** issue template to claim work.
2. Confirm the city name, UF and seven-digit identifier in [IBGE](https://www.ibge.gov.br/explica/codigos-dos-municipios.php). Locate a primary flag reference: prefeitura, municipal law or official visual manual. If sources conflict or no official flag can be established, document that in an issue before drawing.
3. Create `cities/BR/<UF>/<IBGE-code>/`. Add original geometry in `flag.svg`, a completed `metadata.json` based on [the example](docs/CITY_METADATA.example.json), and a local `README.md` with sources and a small original-versus-emoji comparison. Do not copy the example's placeholder values.
4. Match the state set: `viewBox="0 0 36 36"`, visible flag at `y=5` through `y=31`, rounded corners (`rx=4`), flat palette, transparent outside. Preserve distinctive fields and main symbols. Simplify fine heraldry deliberately; document what changes. Use paths for lettering. Add accessible `<title>` and `<desc>`.
5. Keep reference images as external links. Draw the submitted vector yourself; a coding agent may assist. Do not trace or copy third-party SVG paths without establishing compatible licensing and documenting attribution. Do not include executable SVG content or embedded raster images.
6. Run `npm ci --ignore-scripts`, `npm run export:cities`, and `npm run verify`. The exporter creates `png/{36,72,144,512}.png` alongside the city master. Existing state generation remains unchanged.
7. Inspect the flag at **18, 24 and 36px**, on light and dark backgrounds. Include an original/emoji comparison at 36px and describe the outcome in the PR. Do not add a website.
8. Submit one locality per PR from your fork to this repository's `main` branch, ready for review. Use the PR template; include your credit, sources, simplifications and validation results. State corrections may have their own focused PR.

The validator checks the identifier's format and UF prefix; it does not prove that the IBGE code belongs to the named locality, that a source is authoritative, or that the drawing is accurate. Reviewers check these details.

Your original artwork is contributed under **CC BY 4.0**, and your code/documentation under **MIT**. Contributor credit belongs in the city metadata. State artwork retains its existing credit. Document upstream attribution separately when applicable; a source link alone does not establish permission to reuse artwork.

### Let your coding agent help

Copy [the city contribution prompt](docs/CITY_AGENT_PROMPT.md) and replace the city and state. It covers reference research, vector drawing, metadata, PNG export, small-size review and submission through a fork PR. You remain responsible for reviewing your agent's output before submission.

### Scope and roadmap

Brazilian city flags are open for contributions now. The coverage target is **5,571 localities**: 5,569 municipalities plus Brasília and Fernando de Noronha. This follows [IBGE's territorial classification](https://educa.ibge.gov.br/jovens/materias-especiais/22754-um-pais-com-quase-seis-mil-municipios.html); it is not a claim that every locality has an official flag.

Other countries' subdivisions and city flags are a future direction. Open a proposal first so naming, identifiers, sources and licensing can be agreed before adding another country. This repository keeps its existing name and URLs for now.
