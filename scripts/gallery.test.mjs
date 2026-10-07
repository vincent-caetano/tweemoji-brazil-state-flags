import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync, existsSync} from 'node:fs';
import {matches, pngPath} from '../gallery/model.mjs';
const states = JSON.parse(readFileSync(new URL('../metadata/states.json', import.meta.url)));
test('search handles accents, codes, names, regions and empty results', () => {
 assert.equal(states.filter(s => matches(s, ' sao paulo '))[0].code, 'SP');
 assert.deepEqual(states.filter(s => matches(s, 'RN')).map(s=>s.code), ['RN']);
 assert.equal(states.filter(s => matches(s, 'RJ'))[0].name, 'Rio de Janeiro');
 assert.equal(states.filter(s => matches(s, 'sudeste')).length, 4);
 assert.equal(states.filter(s => matches(s, '')).length, 27);
 assert.equal(states.filter(s => matches(s, 'Atlantis')).length, 0);
});
test('every download resolves to a local asset at every supported resolution', () => {
 for (const s of states) {assert.ok(existsSync(new URL('../'+s.svg, import.meta.url))); for (const size of [36,72,144,512]) assert.ok(existsSync(new URL('../'+pngPath(s,size), import.meta.url)));}
 assert.throws(() => pngPath(states[0], 999), RangeError);
});
