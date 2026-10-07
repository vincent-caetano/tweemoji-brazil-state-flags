const fs = require('node:fs');
const path = require('node:path');
const root = path.resolve(__dirname, '..');
const dest = path.join(root, '_site');
fs.mkdirSync(dest, {recursive:true});
for (const file of fs.readdirSync(path.join(root, 'gallery'))) fs.copyFileSync(path.join(root, 'gallery', file), path.join(dest, file));
for (const dir of ['svg', 'png', 'metadata']) fs.cpSync(path.join(root, dir), path.join(dest, dir), {recursive:true});
console.log('Built static gallery in _site/');
