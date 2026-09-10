// Probe .dc.html artboards: overflow, height, min font-size, min hit-target, contrast.
// Renders SCRATCH copies with the support.js <script> line stripped (that file is not local).
// Prints its own examined count — a probe that reports PASS having measured zero files is the
// failure cag-gate-integrity.md exists to catch.
import { chromium } from 'playwright';
import fs from 'node:fs';
import path from 'node:path';
import os from 'node:os';

const dir = process.argv[2];
if (!dir) { console.error('usage: node scripts/probe_artboards.mjs <artboard-dir> [filter]'); process.exit(2); }
const filter = process.argv[3] || '';

const files = fs.readdirSync(dir).filter(f => f.endsWith('.dc.html') && f !== 'Main.dc.html' && f.includes(filter)).sort();
const frameOf = f => f.includes('-Mobile') ? 390 : f.includes('-Tablet') ? 768 : 1440;

const scratch = fs.mkdtempSync(path.join(os.tmpdir(), 'dcprobe-'));
const browser = await chromium.launch();
const rows = [];

for (const f of files) {
  const src = fs.readFileSync(path.join(dir, f), 'utf8');
  const stripped = src.replace(/<script src="\.\/support\.js"><\/script>/, '');
  const tmp = path.join(scratch, f);
  fs.writeFileSync(tmp, stripped);

  const w = frameOf(f);
  const page = await browser.newPage({ viewport: { width: w, height: 900 } });
  await page.goto('file://' + tmp, { waitUntil: 'load' });
  await page.waitForTimeout(400); // webfont settle

  const m = await page.evaluate(() => {
    const srgb = c => { c /= 255; return c <= 0.03928 ? c / 12.92 : Math.pow((c + 0.055) / 1.055, 2.4); };
    const lum = ([r, g, b]) => 0.2126 * srgb(r) + 0.7152 * srgb(g) + 0.0722 * srgb(b);
    const parse = s => { const n = (s || '').match(/[\d.]+/g); return n ? n.slice(0, 4).map(Number) : null; };
    const opaqueBg = el => {
      for (let n = el; n; n = n.parentElement) {
        const c = parse(getComputedStyle(n).backgroundColor);
        if (c && (c.length < 4 || c[3] === 1)) return c.slice(0, 3);
      }
      return [255, 255, 255];
    };
    const ratio = (a, b) => { const [x, y] = [lum(a), lum(b)].sort((p, q) => q - p); return (x + 0.05) / (y + 0.05); };

    let minFont = Infinity, minHit = Infinity, worst = { r: 99, text: '' }, nodes = 0;
    for (const el of document.querySelectorAll('*')) {
      const cs = getComputedStyle(el);
      if (cs.display === 'none' || cs.visibility === 'hidden') continue;
      const direct = [...el.childNodes].some(n => n.nodeType === 3 && n.textContent.trim());
      if (direct) {
        nodes++;
        const fs_ = parseFloat(cs.fontSize);
        if (fs_ < minFont) minFont = fs_;
        const fg = parse(cs.color).slice(0, 3);
        const r = ratio(fg, opaqueBg(el));
        const large = fs_ >= 24 || (fs_ >= 18.66 && parseInt(cs.fontWeight) >= 700);
        const need = large ? 3 : 4.5;
        if (r < need && r < worst.r) worst = { r: +r.toFixed(2), need, text: el.textContent.trim().slice(0, 48) };
      }
      if (el.matches('a,button,[role="button"],summary,input,select')) {
        const h = el.getBoundingClientRect().height;
        if (h > 0 && h < minHit) minHit = h;
      }
    }
    const root = document.getElementById('root') || document.body.firstElementChild;
    return {
      scrollW: document.documentElement.scrollWidth,
      height: Math.round(root.getBoundingClientRect().height),
      minFont: minFont === Infinity ? null : +minFont.toFixed(1),
      minHit: minHit === Infinity ? null : Math.round(minHit),
      worst, nodes,
    };
  });

  rows.push({ file: f, frame: w, ...m });
  await page.close();
}
await browser.close();

console.log(`EXAMINED ${rows.length} artboards in ${dir}${filter ? ` (filter "${filter}")` : ''}\n`);
if (!rows.length) { console.log('NOTHING EXAMINED — do not read this as a pass.'); process.exit(1); }

console.log('file'.padEnd(34), 'frame', 'scrollW', 'height', 'minFont', 'minHit', 'worstContrast');
let fails = 0;
for (const r of rows) {
  const bad = [];
  if (r.scrollW > r.frame) bad.push('OVERFLOW');
  if (r.frame === 390 && r.minFont !== null && r.minFont < 14) bad.push('FONT<14');
  if (r.frame === 390 && r.minHit !== null && r.minHit < 44) bad.push('HIT<44');
  if (r.worst.r < 99) bad.push(`CONTRAST ${r.worst.r}`);
  if (bad.length) fails++;
  console.log(
    r.file.padEnd(34), String(r.frame).padEnd(5), String(r.scrollW).padEnd(7),
    String(r.height).padEnd(6), String(r.minFont).padEnd(7), String(r.minHit).padEnd(6),
    r.worst.r < 99 ? `${r.worst.r} "${r.worst.text}"` : 'ok', bad.length ? ' <<< ' + bad.join(' ') : ''
  );
}
console.log(`\n${rows.length} examined · ${fails} with findings · ${rows.length - fails} clean`);

if (process.env.PROBE_JSON) {
  fs.writeFileSync(process.env.PROBE_JSON,
    JSON.stringify(Object.fromEntries(rows.map(r => [r.file, r.height])), null, 2));
  console.log('heights written to', process.env.PROBE_JSON);
}
console.log('canvas h (measured +5%):');
for (const r of rows) console.log(' ', r.file.padEnd(34), Math.round(r.height * 1.05));
