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
