<div align="center">

<img src="svg/br-mg.svg" width="64" height="64" alt="Minas Gerais" />
<img src="svg/br-pa.svg" width="64" height="64" alt="Pará" />
<img src="svg/br-rj.svg" width="64" height="64" alt="Rio de Janeiro" />

# Tweemoji Brazil State Flags

**A little Brazil in every interface.**

27 original, Twemoji-inspired flags for Brazil's 26 states and Distrito Federal.<br />
Editable SVGs. Transparent PNGs. One consistent visual system.

[![Validate assets](https://github.com/vincent-caetano/tweemoji-brazil-state-flags/actions/workflows/validate.yml/badge.svg)](https://github.com/vincent-caetano/tweemoji-brazil-state-flags/actions/workflows/validate.yml)
![27 flags](https://img.shields.io/badge/flags-27-269B59)
![SVG + PNG](https://img.shields.io/badge/formats-SVG_%2B_PNG-2455A4)
[![Code: MIT](https://img.shields.io/badge/code-MIT-292F33)](LICENSE)
[![Artwork: CC BY 4.0](https://img.shields.io/badge/artwork-CC_BY_4.0-FFCC33)](LICENSE-ARTWORK.md)

[Gallery](#the-collection) · [Quick start](#quick-start) · [React Native](#react-native--expo) · [Design](docs/DESIGN.md) · [Contribute](CONTRIBUTING.md)

</div>

---

## The collection

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="preview/brazil-state-flags-dark.png" />
  <img src="preview/brazil-state-flags-contact-sheet.png" alt="All 27 Brazilian state and Federal District flag illustrations, labeled with their state codes and names" width="1200" />
</picture>

Small icons deserve deliberate artwork. Every flag shares a rounded silhouette, flat colors and balanced spacing. Detailed coats of arms are redrawn into their essential shapes so the set works together at interface sizes.

These are **custom illustrations inspired by [Twemoji](https://github.com/twitter/twemoji)**. They are independent assets, not Unicode emoji, and `twemoji.parse()` will not render them. Official proportions, print colors and fine heraldic details are intentionally adapted; see [design notes](docs/DESIGN.md) and each flag's metadata.

## Quick start

[Download the collection](https://github.com/vincent-caetano/tweemoji-brazil-state-flags/releases/latest/download/brazil-state-flags.zip), or clone it:

```sh
git clone https://github.com/vincent-caetano/tweemoji-brazil-state-flags.git
```

The SVG and PNG files are ready to use. No build step or dependency installation is needed to use the artwork.

### Web

Copy the desired SVG into your application's public assets:

```html
<img src="/flags/br-mg.svg" width="24" height="24" alt="Minas Gerais" />
```

### PNG

Choose a resolution and use the same state naming convention:

```text
png/36/br-mg.png
png/72/br-mg.png
png/144/br-mg.png
png/512/br-mg.png
```

All exports have transparent backgrounds outside the flag shape. The canvas is square; the visible flag occupies 26 of its 36 vertical units.

### React Native / Expo

Copy `react-native/`, `metadata/`, and `png/144/` into your app together, preserving their relative paths:

```tsx
import { StateFlag } from './brazil-state-flags/react-native/StateFlag';

<StateFlag state="MG" size={24} />
<StateFlag state="SP" size={32} />
```

The component uses static PNG imports, `Image` from React Native, and a typed state code. It accepts `state`, `size`, and `style`; its default size is 24. It is an integration example and has not been tested inside a specific Expo application.

### Metadata

```ts
import { brazilStates, type BrazilStateCode } from './metadata/states';

const code: BrazilStateCode = 'MG';
const flag = brazilStates[code];
// flag.name → "Minas Gerais"
// flag.region → "sudeste"
// flag.svg → "svg/br-mg.svg"
```

Asset paths are relative to this repository's root. The same information is available as [JSON](metadata/states.json), including ISO subdivision codes, PNG paths, composition references and per-state simplification notes.

## What's inside

| Directory | Contents |
| :--- | :--- |
| [`svg/`](svg/) | 27 editable SVG masters, all on a 36×36 canvas |
| [`png/`](png/) | 108 transparent PNGs at 36, 72, 144 and 512px |
| [`metadata/`](metadata/) | JSON and TypeScript mappings for all 27 federative units |
| [`react-native/`](react-native/) | Reusable `StateFlag` component |
| [`preview/`](preview/) | Light/dark galleries, actual-size review and pilot renders |
| [`scripts/`](scripts/) | Vector generator, raster exporter and validation |

<details>
<summary><strong>All supported state codes</strong></summary>

| Region | Federative units |
| :--- | :--- |
| Norte | AC · AP · AM · PA · RO · RR · TO |
| Nordeste | AL · BA · CE · MA · PB · PE · PI · RN · SE |
| Centro-Oeste | DF · GO · MT · MS |
| Sudeste | ES · MG · RJ · SP |
| Sul | PR · RS · SC |

Filenames use `br-` plus the lowercase code, such as `br-ac.svg` and `br-df.svg`.

</details>

## Build and verify

Requires **Node.js 22+** and **Python 3**. Python uses only the standard library; `sharp` is the image export dependency.

```sh
npm ci --ignore-scripts
npm run build
npm run export
npm run verify
```

`build` recreates SVGs, metadata and the React Native component from `scripts/build.py`. It overwrites direct edits to generated files. For a lasting correction, change the generator first.

`export` rasterizes the SVG masters and rebuilds the preview sheets. `verify` checks state coverage, PNG dimensions and transparency, the Amazonas star count, and that SVGs contain only passive vector elements with local references. GitHub Actions also checks reproducible vector output and audits dependencies.

[Review at 18/24/36px](preview/small-size-review.png) · [Compare PA/MG/RJ pilots](preview/pilot-review.png)

## Contributing

Have a better way to simplify a crest, or spotted a flag detail to correct? [Open an issue](https://github.com/vincent-caetano/tweemoji-brazil-state-flags/issues) with the state code and a reliable reference. Read the [contribution guide](CONTRIBUTING.md) before submitting a change.

## Credits and licensing

Created by [Vincent Caetano](https://github.com/vincent-caetano).

- **Code and documentation:** [MIT](LICENSE).
- **Original flag artwork and raster exports:** [CC BY 4.0](LICENSE-ARTWORK.md), with attribution to Vincent Caetano.
- **Style reference:** [Twemoji](https://github.com/twitter/twemoji). No Twemoji code or artwork paths are included.
- **Composition references:** [Brazilian flag gallery](https://en.wikipedia.org/wiki/List_of_Brazilian_flags#First-level_administrative_divisions), with individual Wikimedia Commons links recorded in metadata. Reference thumbnails are not distributed.

A ready-to-use attribution example is included in [the artwork license](LICENSE-ARTWORK.md).
