#!/usr/bin/env python3
"""Validate that distributed SVGs contain only local, passive vector artwork."""
from pathlib import Path
import re
import xml.etree.ElementTree as ET

root = Path(__file__).resolve().parents[1]
allowed = {'svg', 'title', 'desc', 'defs', 'clipPath', 'g', 'rect', 'path', 'polygon', 'circle', 'ellipse'}
files = sorted((root / 'svg').glob('*.svg')) + sorted((root / 'cities').rglob('*.svg'))
for file in files:
    source = file.read_text()
    assert '<!DOCTYPE' not in source.upper() and '<!ENTITY' not in source.upper(), file.name
    document = ET.fromstring(source)
    ids = {node.attrib['id'] for node in document.iter() if 'id' in node.attrib}
    for node in document.iter():
        tag = node.tag.rsplit('}', 1)[-1]
        assert tag in allowed, (file.name, tag)
        for key, value in node.attrib.items():
            attr = key.rsplit('}', 1)[-1].lower()
            assert not attr.startswith('on'), (file.name, key)
            assert attr not in {'href', 'src', 'style'}, (file.name, key)
            assert 'javascript:' not in value.lower() and 'data:' not in value.lower(), file.name
            for match in re.findall(r'url\(([^)]+)\)', value):
                assert match.startswith('#') and match[1:] in ids, (file.name, match)
    assert len(ids) == len([node for node in document.iter() if 'id' in node.attrib]), file.name
print(f'Verified passive SVG elements, unique IDs, and local-only references in {len(files)} masters.')
