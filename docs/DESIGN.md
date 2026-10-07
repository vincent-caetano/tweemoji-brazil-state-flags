# Design notes

The system uses a shared 36×36 SVG canvas and a 36×26 flag silhouette starting at y=5, with a corner radius of 4. The design reference is Twemoji's flat, rounded flag vocabulary. All distributed geometry was written for this project; no Twemoji paths were copied.

## What stays

- Main fields, stripes, diagonals and identifiable symbols.
- Star counts where practical: Amazonas includes 61 small stars and its central star.
- Distinctive emblems: Amapá's fort plan, Distrito Federal's cross, Pernambuco's rainbow, and São Paulo's Brazil silhouette.

## What changes

- Official aspect ratios adapt to a shared canvas.
- Colors use a consistent emoji palette rather than official print specifications.
- Complex coats of arms retain their silhouette and main motifs; small inscriptions and fine heraldic details are omitted.
- Geometric path lettering avoids font dependencies. ES, MG, PR and PI lettering becomes decorative at the smallest sizes. Some accents are omitted.

The 512px files retain these simplifications; they are larger emoji illustrations, not full-detail official reproductions. Per-state decisions and composition reference links are in [states.json](../metadata/states.json).

## Review

[Light contact sheet](../preview/brazil-state-flags-contact-sheet.png) · [Dark contact sheet](../preview/brazil-state-flags-dark.png) · [18/24/36px sheet](../preview/small-size-review.png) · [PA/MG/RJ pilots](../preview/pilot-review.png)

For repeated inline instances of the same SVG in a web document, prefix clip/title/description IDs per instance. Ordinary `<img>` use isolates IDs automatically.
