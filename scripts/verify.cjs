#!/usr/bin/env node
const fs = require('node:fs/promises');
const path = require('node:path');
const assert = require('node:assert/strict');
const sharp = require('sharp');
const root = path.resolve(__dirname,'..');
(async()=>{
 const states=JSON.parse(await fs.readFile(path.join(root,'metadata/states.json'),'utf8'));
 const expected='AC AL AP AM BA CE DF ES GO MA MT MS MG PA PB PR PE PI RJ RN RS RO RR SC SP SE TO'.split(' ');
 assert.deepEqual(states.map(s=>s.code),expected);
 assert.equal((await fs.readdir(path.join(root,'svg'))).filter(x=>x.endsWith('.svg')).length,27);
 let count=0;
 for(const st of states){
  const svg=await fs.readFile(path.join(root,st.svg),'utf8');
  assert(svg.includes('viewBox="0 0 36 36"'));
  assert(!/<(?:image|text|script|foreignObject)\b/.test(svg),'Masters must be self-contained vectors');
  assert(!/linearGradient|radialGradient|filter=/.test(svg));
  if(st.code==='AM')assert.equal((svg.match(/<polygon/g)||[]).length,62);
  for(const size of [36,72,144,512]){
   const file=path.join(root,st.png[String(size)]);
   const meta=await sharp(file).metadata();
   assert.equal(meta.width,size);assert.equal(meta.height,size);assert(meta.hasAlpha);
   const {data,info}=await sharp(file).ensureAlpha().raw().toBuffer({resolveWithObject:true});
   const alpha=(x,y)=>data[(y*size+x)*info.channels+3];
   assert.equal(alpha(0,0),0);assert.equal(alpha(size-1,size-1),0);
   assert.equal(alpha(Math.floor(size/2),Math.floor(size/2)),255);
   // Entire top/bottom padding must remain transparent.
   for(let x=0;x<size;x++){assert.equal(alpha(x,0),0);assert.equal(alpha(x,size-1),0)}
   count++;
  }
 }
 console.log(`Verified ${states.length} self-contained SVGs, ${count} RGBA PNGs, sizes, coverage, transparency and Amazonas star count.`);
})().catch(e=>{console.error(e);process.exitCode=1});
