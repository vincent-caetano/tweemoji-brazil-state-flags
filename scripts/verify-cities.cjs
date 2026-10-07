const fs = require('node:fs/promises');
const path = require('node:path');
const assert = require('node:assert/strict');
const sharp = require('sharp');
const root = path.resolve(__dirname, '..', 'cities');
const states = new Set('AC AL AP AM BA CE DF ES GO MA MT MS MG PA PB PR PE PI RJ RN RS RO RR SC SP SE TO'.split(' '));
const prefixes = {AC:'12',AL:'27',AP:'16',AM:'13',BA:'29',CE:'23',DF:'53',ES:'32',GO:'52',MA:'21',MT:'51',MS:'50',MG:'31',PA:'15',PB:'25',PR:'41',PE:'26',PI:'22',RJ:'33',RN:'24',RS:'43',RO:'11',RR:'14',SC:'42',SP:'35',SE:'28',TO:'17'};
(async () => {
 const entries = await fs.readdir(root, {recursive:true, withFileTypes:true});
 const folders = new Set(entries.filter(e=>e.isFile()&&['flag.svg','metadata.json'].includes(e.name)).map(e=>e.parentPath));
 const ids = new Set();
 for (const dir of folders) {
  const meta = JSON.parse(await fs.readFile(path.join(dir,'metadata.json'),'utf8'));
  assert.equal(meta.country,'BR'); assert(states.has(meta.state)); assert.match(meta.ibgeCode,/^\d{7}$/);
  assert(meta.ibgeCode.startsWith(prefixes[meta.state]), 'IBGE state prefix mismatch');
  assert.equal(path.relative(root,dir),path.join('BR',meta.state,meta.ibgeCode));
  assert.equal(meta.id,`br-${meta.state.toLowerCase()}-${meta.ibgeCode}`); assert(!ids.has(meta.id)); ids.add(meta.id);
  assert.equal(meta.license,'CC-BY-4.0');
  for (const value of [meta.name,meta.simplification,meta.contributor?.name]) {assert.equal(typeof value,'string'); assert(value.trim());}
  assert(Array.isArray(meta.sources)&&meta.sources.length>0);
  for (const source of meta.sources) {assert(source.title?.trim()); assert.equal(new URL(source.url).protocol,'https:'); assert.match(source.accessed,/^\d{4}-\d{2}-\d{2}$/);}
  assert.equal(new URL(meta.contributor.url).protocol,'https:');
  await fs.access(path.join(dir,'README.md'));
  const svg = await fs.readFile(path.join(dir,'flag.svg'),'utf8');
  assert(svg.includes('viewBox="0 0 36 36"')); assert(!/linearGradient|radialGradient|filter=/.test(svg));
  assert(/<title\b/.test(svg)&&/<desc\b/.test(svg),'Add accessible title and simplification description');
  for (const size of [36,72,144,512]) {
   const image = sharp(path.join(dir,'png',`${size}.png`)); const m = await image.metadata();
   assert.equal(m.width,size);assert.equal(m.height,size);assert(m.hasAlpha);
   const {data,info} = await image.ensureAlpha().raw().toBuffer({resolveWithObject:true});
   const alpha = (x,y)=>data[(y*size+x)*info.channels+3];
   for(let x=0;x<size;x++){assert.equal(alpha(x,0),0);assert.equal(alpha(x,size-1),0);}
   assert.equal(alpha(Math.floor(size/2),Math.floor(size/2)),255);
  }
 }
 console.log(`Verified ${folders.size} city submissions: identifiers, metadata, sources and PNG exports.`);
})().catch(error => {console.error(error);process.exitCode=1;});
