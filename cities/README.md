# City flags

City submissions are welcome. The collection currently contains **27 federative-unit flags and no accepted city flags**. Do not count the contribution infrastructure as completed city artwork.

Use `cities/BR/<UF>/<seven-digit-IBGE-code>/`:

```text
cities/BR/SP/3509502/
├── flag.svg
├── metadata.json
├── README.md
└── png/
    ├── 36.png
    ├── 72.png
    ├── 144.png
    └── 512.png
```

The city SVG is the editable master. City assets are independent of the state generator; do not add cities to `metadata/states.json` or change its 27-unit contract.

See the [contribution guide](../CONTRIBUTING.md#city-flags), [metadata example](../docs/CITY_METADATA.example.json), and [copy/paste agent prompt](../docs/CITY_AGENT_PROMPT.md).

Brasília and Fernando de Noronha may use their IBGE locality identifiers, with their distinct administrative status documented in the local README. Do not invent a municipal flag where none exists. Existing Distrito Federal artwork remains in the state collection.
