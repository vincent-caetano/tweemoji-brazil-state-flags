const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const os = require('node:os');
const path = require('node:path');
const {spawnSync} = require('node:child_process');
const root = path.resolve(__dirname,'..');
test('city contribution exports correctly and rejects broken identity, missing exports and active SVG', () => {
 const temp = fs.mkdtempSync(path.join(os.tmpdir(),'flag-city-test-'));
 try {
  fs.mkdirSync(path.join(temp,'scripts')); fs.mkdirSync(path.join(temp,'svg'));
  fs.symlinkSync(path.join(root,'node_modules'),path.join(temp,'node_modules'),'dir');
  for(const name of ['export-cities.cjs','verify-cities.cjs','verify-svg.py']) fs.copyFileSync(path.join(__dirname,name),path.join(temp,'scripts',name));
  const run = (name) => spawnSync(name.endsWith('.py')?'python3':process.execPath,[path.join(temp,'scripts',name)],{encoding:'utf8'});
  fs.mkdirSync(path.join(temp,'cities'));
  assert.equal(run('verify-cities.cjs').status,0,'Empty collection must work');
  const city = path.join(temp,'cities','BR','SP','3509502'); fs.mkdirSync(city,{recursive:true});
  const svg = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 36 36"><title>Test fixture</title><desc>Neutral test shape, not a real flag.</desc><rect y="5" width="36" height="26" rx="4" fill="#FFFFFF"/></svg>';
  fs.writeFileSync(path.join(city,'flag.svg'),svg);fs.writeFileSync(path.join(city,'README.md'),'Test fixture only.');
  const meta={id:'br-sp-3509502',country:'BR',state:'SP',ibgeCode:'3509502',name:'Test fixture',license:'CC-BY-4.0',contributor:{name:'Test',url:'https://github.com/test'},sources:[{title:'IBGE record',url:'https://www.ibge.gov.br/cidades-e-estados/sp/campinas.html',accessed:'2026-10-07'}],simplification:'Neutral test shape.'};
  const save = value=>fs.writeFileSync(path.join(city,'metadata.json'),JSON.stringify(value)); save(meta);
  assert.equal(run('verify-svg.py').status,0);
  assert.equal(run('export-cities.cjs').status,0);
  assert.equal(run('verify-cities.cjs').status,0,'Complete contribution must pass');
  save({...meta,ibgeCode:'3309502'});assert.notEqual(run('verify-cities.cjs').status,0,'Wrong UF prefix must fail');save(meta);
  save({...meta,sources:[]});assert.notEqual(run('verify-cities.cjs').status,0,'Missing sources must fail');save(meta);
  fs.unlinkSync(path.join(city,'png','36.png'));assert.notEqual(run('verify-cities.cjs').status,0,'Missing PNG must fail');
  fs.writeFileSync(path.join(city,'flag.svg'),svg.replace('</svg>','<script>alert(1)</script></svg>'));
  assert.notEqual(run('verify-svg.py').status,0,'Active SVG must fail before rasterizing');
 } finally {fs.rmSync(temp,{recursive:true,force:true});}
});
