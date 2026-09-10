#!/usr/bin/env node
/**
 * Round-3 artboard probe.
 * Renders scratch copies (support.js line stripped) at each file's own frame width and reports:
 *   overflow (scrollWidth vs frame), root height, min font-size, min hit-target, WCAG contrast.
 * Prints its own EXAMINED count — a probe reporting PASS on zero files is the failure
 * cag-gate-integrity.md exists to catch.
 */
import { chromium } from 'playwright';
import fs from 'fs'; import path from 'path';

const FOLDER = 'docs/design/homepage-variations-r3';
const SCRATCH = '/tmp/r3-probe';
const WIDTH = { Mobile: 390, Tablet: 768, Desktop: 1440 };
const only = process.argv[2] || '';

fs.rmSync(SCRATCH, { recursive: true, force: true });
fs.mkdirSync(SCRATCH, { recursive: true });
for (const f of fs.readdirSync(FOLDER)) {
  if (f.endsWith('.webp')) fs.copyFileSync(path.join(FOLDER, f), path.join(SCRATCH, f));
}

const files = fs.readdirSync(FOLDER)
  .filter(f => f.endsWith('.dc.html') && f !== 'Main.dc.html')
  .filter(f => !only || f.startsWith(only))
  .sort();

const srgb = c => { c /= 255; return c <= 0.03928 ? c / 12.92 : Math.pow((c + 0.055) / 1.055, 2.4); };
const lum = ([r, g, b]) => 0.2126 * srgb(r) + 0.7152 * srgb(g) + 0.0722 * srgb(b);

const browser = await chromium.launch();
const rows = [];
let examined = 0;

for (const file of files) {
  const vp = file.includes('-Mobile') ? 'Mobile' : file.includes('-Tablet') ? 'Tablet' : 'Desktop';
  const w = WIDTH[vp];
  const src = fs.readFileSync(path.join(FOLDER, file), 'utf8')
    .replace(/\s*<script src="\.\/support\.js"><\/script>\s*/g, '\n');
  const scratch = path.join(SCRATCH, file);
  fs.writeFileSync(scratch, src);

  const page = await browser.newPage({ viewport: { width: w, height: 900 } });
  try {
    await page.goto('file://' + path.resolve(scratch), { waitUntil: 'load', timeout: 20000 });
    await page.waitForTimeout(350);
    const r = await page.evaluate(() => {
      const parse = s => { const m = (s || '').match(/\d+(\.\d+)?/g); return m ? m.slice(0, 3).map(Number) : null; };
      // Composite the alpha stack: a translucent tint is NOT its own opaque colour.
      // Reading rgba(45,106,79,.08) as solid forest faked a 1:1 finding on 2026-09-10.
      const alphaOf = c => { const m = (c || '').match(/rgba?\(([^)]+)\)/);
        if (!m) return 1; const parts = m[1].split(',').map(s => parseFloat(s));
        return parts.length > 3 ? parts[3] : 1; };
      const bgOf = el => { const stack = []; let n = el;
        while (n && n !== document.documentElement) {
          const c = getComputedStyle(n).backgroundColor, p = parse(c), a = alphaOf(c);
          if (p && a > 0) { stack.push([p, a]); if (a >= 0.999) break; }
          n = n.parentElement; }
        let out = [250, 247, 244];
        for (let i = stack.length - 1; i >= 0; i--) { const [c, a] = stack[i];
          out = [0, 1, 2].map(k => a * c[k] + (1 - a) * out[k]); }
        return out; };
      const root = document.getElementById('root') || document.body.firstElementChild;
      let minFont = 999, minHit = 999, worst = { ratio: 99, need: 4.5, margin: 99, text: '' };
      const srgb = c => { c /= 255; return c <= 0.03928 ? c / 12.92 : Math.pow((c + 0.055) / 1.055, 2.4); };
      const lum = ([r, g, b]) => 0.2126 * srgb(r) + 0.7152 * srgb(g) + 0.0722 * srgb(b);
      for (const el of document.querySelectorAll('*')) {
        const cs = getComputedStyle(el);
        if (cs.display === 'none' || cs.visibility === 'hidden' || +cs.opacity === 0) continue;
        const direct = [...el.childNodes].some(n => n.nodeType === 3 && n.textContent.trim());
        if (direct) {
          const fs_ = parseFloat(cs.fontSize); if (fs_ < minFont) minFont = fs_;
          const bold = (parseInt(cs.fontWeight, 10) || 400) >= 700;
          const large = fs_ >= 24 || (bold && fs_ >= 18.66);   // WCAG 1.4.3 large text => 3:1
          const need = large ? 3 : 4.5;
          const fg = parse(cs.color), bg = bgOf(el);
          if (fg && bg) { const L1 = lum(fg), L2 = lum(bg);
            const ratio = (Math.max(L1, L2) + 0.05) / (Math.min(L1, L2) + 0.05);
            const margin = ratio - need;
            if (margin < worst.margin) worst = { ratio: +ratio.toFixed(2), need, margin,
              text: el.textContent.trim().slice(0, 34) }; }
        }
        if (/^(A|BUTTON|SUMMARY)$/.test(el.tagName)) {
          const h = el.getBoundingClientRect().height; if (h > 0 && h < minHit) minHit = h;
        }
      }
      return { scrollW: document.documentElement.scrollWidth,
               rootH: Math.round(root ? root.getBoundingClientRect().height : 0),
               rootW: Math.round(root ? root.getBoundingClientRect().width : 0),
               minFont: minFont === 999 ? null : +minFont.toFixed(1),
               minHit: minHit === 999 ? null : Math.round(minHit),
               worst };
    });
    rows.push({ file, vp, w, ...r });
    examined++;
  } catch (e) {
    rows.push({ file, vp, w, error: String(e).slice(0, 80) });
  }
  await page.close();
}
await browser.close();

// ---- report ----
const fail = [];
console.log(`\nEXAMINED: ${examined} / ${files.length} artboards\n`);
console.log('file'.padEnd(34), 'vp'.padEnd(8), 'rootH'.padEnd(7), 'ovf'.padEnd(5), 'font'.padEnd(6), 'hit'.padEnd(5), 'contrast');
for (const r of rows) {
  if (r.error) { console.log(r.file.padEnd(34), 'ERROR', r.error); fail.push([r.file, 'render error']); continue; }
  const ovf = r.scrollW > r.w ? `+${r.scrollW - r.w}` : 'ok';
  console.log(r.file.padEnd(34), r.vp.padEnd(8), String(r.rootH).padEnd(7), ovf.padEnd(5),
              String(r.minFont ?? '-').padEnd(6), String(r.minHit ?? '-').padEnd(5),
              `${r.worst.ratio}/${r.worst.need}  "${r.worst.text}"`);
  if (r.scrollW > r.w) fail.push([r.file, `overflow +${r.scrollW - r.w}px`]);
  if (r.rootW > r.w) fail.push([r.file, `root ${r.rootW}px wider than frame ${r.w}px`]);
  if (r.vp === 'Mobile' && r.minFont !== null && r.minFont < 12) fail.push([r.file, `font ${r.minFont}px < 12px`]);
  if (r.vp === 'Mobile' && r.minHit !== null && r.minHit < 44) fail.push([r.file, `hit target ${r.minHit}px < 44px`]);
  if (r.worst.margin < 0) fail.push([r.file, `contrast ${r.worst.ratio}:1 (needs ${r.worst.need}:1) on "${r.worst.text}"`]);
  if (r.file.startsWith('Hero-') && r.vp === 'Desktop' && (r.rootH < 350 || r.rootH > 400))
    fail.push([r.file, `hero desktop ${r.rootH}px outside 350-400 band`]);
  if (r.file.startsWith('Faq-') && r.vp === 'Mobile' && r.rootH >= 1400)
    fail.push([r.file, `faq mobile ${r.rootH}px >= 1400 target`]);
}
console.log(`\n--- ${fail.length} FINDING(S) ---`);
for (const [f, m] of fail) console.log(`  ${f}: ${m}`);
fs.writeFileSync('/tmp/r3-probe-results.json', JSON.stringify({ examined, rows, fail }, null, 2));
console.log(`\nexamined=${examined} findings=${fail.length} -> /tmp/r3-probe-results.json`);
