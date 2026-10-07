const fs = require('node:fs/promises');
const path = require('node:path');
const sharp = require('sharp');
const root = path.resolve(__dirname, '..', 'cities');
(async () => {
 let count = 0;
 for (const item of await fs.readdir(root, {recursive:true, withFileTypes:true})) {
  if (!item.isFile() || item.name !== 'flag.svg') continue;
  const file = path.join(item.parentPath, item.name);
  const dir = path.dirname(file);
  await fs.mkdir(path.join(dir, 'png'), {recursive:true});
  for (const size of [36,72,144,512]) await sharp(file).resize(size,size).png().toFile(path.join(dir,'png',`${size}.png`));
  count++;
 }
 console.log(`Exported ${count} city flags at four resolutions.`);
})().catch(error => {console.error(error); process.exitCode=1;});
