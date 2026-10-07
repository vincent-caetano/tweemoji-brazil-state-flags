export function normalize(value) { return value.normalize('NFD').replace(/\p{Diacritic}/gu, '').toLowerCase().trim(); }
const codes = new Set('AC AL AP AM BA CE DF ES GO MA MT MS MG PA PB PR PE PI RJ RN RS RO RR SC SP SE TO'.toLowerCase().split(' '));
export function matches(state, query) { if (codes.has(normalize(query))) return normalize(state.code) === normalize(query); return normalize(`${state.code} ${state.name} ${state.region}`).includes(normalize(query)); }
export function pngPath(state, resolution) { if (!['36', '72', '144', '512'].includes(String(resolution))) throw new RangeError('Invalid PNG resolution'); return state.png[String(resolution)]; }
