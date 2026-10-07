import {matches, pngPath} from './model.mjs';
const $ = id => document.getElementById(id);
let states = [];
function node(tag, text, className) { const el = document.createElement(tag); if (text) el.textContent = text; if (className) el.className = className; return el; }
function link(text, href, download = false) { const el = node('a', text); el.href = href; if (download) el.download = href.split('/').at(-1); return el; }
function render() {
  const visible = states.filter(state => matches(state, $('search').value));
  $('flags').replaceChildren(...visible.map(state => {
    const card = node('article', '', 'card');
    const art = node('div', '', 'art'); const img = node('img'); img.src = state.svg; img.alt = `${state.name} flag`; img.width = 36; img.height = 36; art.append(img);
    const title = node('h2', state.name); title.append(node('span', state.code, 'code'));
    const downloads = node('div', '', 'downloads'); downloads.append(link('SVG ↓', state.svg, true), link(`PNG ${$('resolution').value} ↓`, pngPath(state, $('resolution').value), true));
    const details = node('details'); details.append(node('summary', 'Design & references'), node('p', state.simplification), node('p', state.review)); details.append(link('Composition reference ↗', state.reference)); if (state.officialSource) {details.append(node('br'), link('Primary source ↗', state.officialSource));}
    card.append(art, title, node('p', state.region, 'region'), downloads, details); return card;
  }));
  $('status').textContent = `${visible.length} of 27 flags · preview at ${$('size').value}px`;
  $('empty').hidden = visible.length > 0;
}
$('search').addEventListener('input', render);
$('resolution').addEventListener('change', render);
$('size').addEventListener('change', () => { document.documentElement.style.setProperty('--preview', `${$('size').value}px`); render(); });
$('reset').addEventListener('click', () => { $('search').value = ''; render(); $('search').focus(); });
function theme(dark) {document.body.classList.toggle('dark', dark); $('theme').textContent = dark ? 'Light background' : 'Dark background'; $('theme').setAttribute('aria-pressed', String(dark));}
theme(matchMedia('(prefers-color-scheme: dark)').matches);
$('theme').addEventListener('click', () => theme(!document.body.classList.contains('dark')));
try { const response = await fetch('metadata/states.json'); if (!response.ok) throw new Error('Unavailable metadata'); states = await response.json(); render(); } catch { $('status').textContent = 'The collection could not load. Please reload the page or download the ZIP above.'; }
