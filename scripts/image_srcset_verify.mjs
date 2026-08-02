#!/usr/bin/env node
/**
 * Acceptance for the srcset work, measured in a real browser at DPR 1.
 *
 * Checks BOTH directions, because they fail differently and only one of them is what the
 * render harness measures:
 *
 *   OVERSIZED  natural/painted > 2.0  — bytes wasted. This is `img-srcset-within-2x`.
 *   UNDERSIZED natural/painted < 0.95 — the browser fetched a file SMALLER than the box it
 *              paints into, i.e. visible blur. Nothing in the harness catches this, and it
 *              is exactly what got the 2026-08-01 attempt reverted: a blanket `sizes` put a
 *              168px file in a 343px box. A run that clears the cap by shipping blur has
 *              made the page worse while making the metric better, so the metric alone must
 *              never be the acceptance.
 *
 *   node scripts/image_srcset_verify.mjs <slug> [<slug>...]
 */
import { chromium } from '@playwright/test';
import { spawn, execFileSync } from 'node:child_process';

/** Real pixel widths of every built image, read once from disk. */
function realWidths() {
  // Concatenated with `+`. Adjacent string literals are a SyntaxError in JS, and because
  // the call sits in a try/catch the failure returned {} silently — every reading then fell
  // back to `naturalWidth`, which is the one number this function exists to avoid.
  const script = [
    'import os,json',
    'from PIL import Image',
    'out={}',
    'for root,_,fs in os.walk("dist"):',
    '    for f in fs:',
    '        if f.lower().endswith((".webp",".png",".jpg",".jpeg")):',
    '            p=os.path.join(root,f)',
    '            try:',
    '                with Image.open(p) as im: out["/"+os.path.relpath(p,"dist")]=im.width',
    '            except Exception: pass',
    'print(json.dumps(out))',
  ].join('\n');
  const out = JSON.parse(
    execFileSync('python3', ['-c', script], { encoding: 'utf8', maxBuffer: 64 * 1024 * 1024 }),
  );
  // Refuse rather than degrade: an empty map silently turns every ratio back into the
  // density-corrected `naturalWidth` reading this script was written to replace.
  if (Object.keys(out).length < 50) {
    throw new Error(`width scan found only ${Object.keys(out).length} images under dist/ — refusing to measure`);
  }
  return out;
}
const FILEW = realWidths();
console.log(`indexed ${Object.keys(FILEW).length} built image files\n`);

const SWEEP = [375, 414, 480, 639, 640, 767, 768, 900, 1023, 1024, 1280, 1440];
const PORT = 4329;
const OVER = 2.0;
const UNDER = 0.95;

const slugs = process.argv.slice(2).filter((a) => !a.startsWith('--'));
if (!slugs.length) {
  console.error('usage: image_srcset_verify.mjs <slug> [<slug>...]');
  process.exit(2);
}

const server = spawn('python3', ['-m', 'http.server', String(PORT), '-d', 'dist'], { stdio: 'ignore' });
process.on('exit', () => server.kill());
await new Promise((r) => setTimeout(r, 700));

const browser = await chromium.launch();
const over = [];
const under = [];
let measured = 0;

for (const slug of slugs) {
  const page = await browser.newPage({ deviceScaleFactor: 1 });
  for (const vp of SWEEP) {
    await page.setViewportSize({ width: vp, height: 900 });
    await page.goto(`http://127.0.0.1:${PORT}/${slug}/`, { waitUntil: 'load' });
    await page.evaluate(() => {
      for (const img of Array.from(document.images)) img.setAttribute('loading', 'eager');
    });
    await page.evaluate(async () => {
      const step = window.innerHeight;
      for (let y = 0, i = 0; y < document.body.scrollHeight && i < 400; y += step, i++) {
        window.scrollTo(0, y);
        await new Promise((r) => setTimeout(r, 20));
      }
      window.scrollTo(0, 0);
    });
    await page.waitForTimeout(300);

    const rows = await page.evaluate(() => {
      const out = [];
      for (const img of Array.from(document.images)) {
        const box = img.getBoundingClientRect();
        if (box.width < 1 || !img.naturalWidth) continue;
        out.push({
          src: img.getAttribute('src') || '',
          // The CHOSEN file's path. `naturalWidth` cannot answer the question this script
          // asks: on an image with a `w`-descriptor srcset the browser returns the
          // DENSITY-CORRECTED intrinsic width, which works out to the `sizes` value, not
          // the file's pixel width. Measured here: a 620px file reported naturalWidth 318,
          // 485 and 398 at three viewports, each exactly `sizes` at that viewport. So the
          // real pixel width is read from disk instead, and `naturalWidth` is kept only to
          // show what the gate sees.
          chosePath: new URL(img.currentSrc, location.href).pathname,
          painted: Math.round(box.width * 100) / 100,
          natural: img.naturalWidth,
        });
      }
      return out;
    });

    for (const r of rows) {
      measured++;
      // Real file pixels vs the painted box. This is the honest ratio in both directions.
      const fileW = FILEW[r.chosePath] ?? r.natural;
      r.fileW = fileW;
      r.chose = r.chosePath.split('/').pop();
      const ratio = fileW / r.painted;
      if (ratio > OVER) over.push({ slug, vp, ...r, ratio });
      else if (ratio < UNDER) under.push({ slug, vp, ...r, ratio });
    }
  }
  await page.close();
}
await browser.close();
server.kill();

console.log(`measured ${measured} image renders across ${slugs.length} page(s) x ${SWEEP.length} viewports\n`);

const groupBy = (list) => {
  const m = new Map();
  for (const x of list) {
    const k = `${x.src}`;
    if (!m.has(k) || m.get(k).ratio < x.ratio) m.set(k, x);
  }
  return [...m.values()].sort((a, b) => b.ratio - a.ratio);
};

console.log(`OVERSIZED (>${OVER}x): ${over.length} render(s), ${groupBy(over).length} distinct file(s)`);
for (const x of groupBy(over).slice(0, 15)) {
  console.log(`  ${x.ratio.toFixed(2)}x  ${x.fileW}px file into ${x.painted}px box @${x.vp}  ${x.chose}`);
}

console.log(`\nUNDERSIZED (<${UNDER}x — BLUR, the reverted attempt's failure): ${under.length} render(s)`);
for (const x of groupBy(under).slice(0, 15)) {
  console.log(`  ${x.ratio.toFixed(2)}x  ${x.fileW}px file into ${x.painted}px box @${x.vp}  ${x.chose}`);
}

process.exitCode = under.length ? 1 : 0;
