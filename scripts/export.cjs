#!/usr/bin/env node
// npm install, then npm run export. SVG masters remain the source of truth.
const fs = require('node:fs/promises');
const path = require('node:path');
const sharp = require('sharp');
const root = path.resolve(__dirname, '..');
(async () => {
  const states = JSON.parse(await fs.readFile(path.join(root, 'metadata/states.json'), 'utf8'));
  for (const size of [36, 72, 144, 512]) {
    await fs.mkdir(path.join(root, 'png', String(size)), {recursive:true});
    for (const state of states) {
      await sharp(path.join(root, state.svg), {density: 72 * size / 36})
        .resize(size,size).png().toFile(path.join(root,state.png[String(size)]));
    }
  }
  await fs.mkdir(path.join(root,'preview'),{recursive:true});
  const escape = s => s.replace(/&/g,'&amp;').replace(/</g,'&lt;');
  for (const dark of [false,true]) {
    const bg = dark ? '#17212B' : '#F5F7FA';
    const ink = dark ? '#F5F7FA' : '#263445';
    const muted = dark ? '#AAB8C5' : '#5C6B7B';
    let sheet = `<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="1110"><rect width="1200" height="1110" fill="${bg}"/><g font-family="Helvetica,Arial,sans-serif"><text x="48" y="62" fill="${ink}" font-size="29" font-weight="700">Brazil · 27 state flags</text><text x="48" y="94" fill="${muted}" font-size="16">Original SVG artwork · Twemoji-inspired · simplified for UI use</text>`;
    const composites=[];
    states.forEach((s,i)=>{
      const x=48+(i%6)*185,y=135+Math.floor(i/6)*185;
      composites.push({input:path.join(root,s.png['144']),left:x+12,top:y});
      sheet+=`<text x="${x+84}" y="${y+145}" fill="${ink}" font-size="17" font-weight="700" text-anchor="middle">${s.code}</text><text x="${x+84}" y="${y+166}" fill="${muted}" font-size="12" text-anchor="middle">${escape(s.name)}</text>`;
    });
    sheet+='</g></svg>';
    await sharp(Buffer.from(sheet)).composite(composites).png().toFile(path.join(root,'preview',dark?'brazil-state-flags-dark.png':'brazil-state-flags-contact-sheet.png'));
  }
  // Review at actual UI pixel sizes; PNG avoids browser-dependent scaling.
  let tiny='<svg xmlns="http://www.w3.org/2000/svg" width="540" height="1040"><rect width="540" height="1040" fill="#F5F7FA"/><g font-family="Helvetica,Arial,sans-serif" fill="#263445"><text x="28" y="40" font-size="22">Actual-size review</text>';
  const composites=[];
  [18,24,36].forEach((s,i)=>tiny+=`<text x="${145+i*115}" y="76" font-size="13">${s}px</text>`);
  for(let i=0;i<states.length;i++){
    const st=states[i],y=92+i*33;
    tiny+=`<text x="28" y="${y+20}" font-size="13">${st.code}</text>`;
    for(let j=0;j<3;j++){
      const sz=[18,24,36][j];composites.push({input:await sharp(path.join(root,st.svg),{density:288}).resize(sz,sz).png().toBuffer(),left:145+j*115,top:y});
    }
  }
  tiny+='<text x="28" y="1010" font-size="12">See pilot sheet for larger 72px / 144px renders.</text></g></svg>';
  await sharp(Buffer.from(tiny)).composite(composites).png().toFile(path.join(root,'preview','small-size-review.png'));
  let pilot='<svg xmlns="http://www.w3.org/2000/svg" width="920" height="690"><rect width="920" height="690" fill="#F5F7FA"/><g font-family="Helvetica,Arial,sans-serif" fill="#263445"><text x="32" y="44" font-size="23">Pilot flags · PA / MG / RJ</text>';
  const p=[];
  for(let i=0;i<3;i++){
    const st=states.find(x=>x.code===['PA','MG','RJ'][i]);const y=95+i*180;
    pilot+=`<text x="32" y="${y+28}" font-size="18">${st.code}</text>`;
    for(let j=0;j<5;j++){
      const size=[18,24,36,72,144][j];const x=130+j*150;
      pilot+=`<text x="${x}" y="${y-8}" font-size="12">${size}px</text>`;
      p.push({input:await sharp(path.join(root,st.svg),{density:288}).resize(size,size).png().toBuffer(),left:x,top:y});
    }
  }
  pilot+='</g></svg>';
  await sharp(Buffer.from(pilot)).composite(p).png().toFile(path.join(root,'preview','pilot-review.png'));
  console.log('Exported 108 transparent PNGs and 4 review sheets.');
})().catch(e=>{console.error(e);process.exitCode=1});
