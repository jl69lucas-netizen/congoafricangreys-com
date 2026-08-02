#!/usr/bin/env node
/**
 * Measure the width every <img> on a page ACTUALLY paints at, across a viewport sweep.
 *
 * Why this exists: the first attempt at fixing this site's oversized images applied one
 * blanket `sizes="(max-width:640px) 45vw, 356px"` to every image, guessed from how the
 * images looked. It conflated gallery cells (genuinely ~45vw) with full-width feature
 * images (343px at a 375 viewport, which is ~92vw), so the browser loaded a 168px file
 * into a 343px box and shipped visible blur. That change was reverted.
 *
 * `sizes` is a promise to the browser about geometry. A guessed promise is a lie, and the
 * browser pays it out in blur. So measure first: this prints, per image, the painted CSS
 * width at every viewport in the sweep, plus the ratio to viewport width, which is what
 * tells you whether the box is fluid (constant vw) or fixed (constant px).
 *
 *   node scripts/measure_painted_widths.mjs <slug> [<slug>...]
 *   node scripts/measure_painted_widths.mjs --json <slug>     # machine-readable
 *
 * Reads dist/ through the same static server the render harness uses, so what it measures
 * is what ships.
 */
import { chromium } from '@playwright/test';
import { spawn } from 'node:child_process';
import { writeFileSync } from 'node:fs';

const SWEEP = [375, 414, 480, 640, 768, 900, 1024, 1280, 1440];
const PORT = 4319;

const args = process.argv.slice(2);
const asJson = args.includes('--json');
const outIdx = args.indexOf('--out');
const outFile = outIdx >= 0 ? args[outIdx + 1] : null;
// `outIdx + 1` is only a value-of-a-flag position when --out was actually passed;
// with outIdx === -1 it is index 0, which silently ate the first slug.
const skipIdx = outIdx >= 0 ? outIdx + 1 : -1;
const slugs = args.filter((a, i) => !a.startsWith('--') && i !== skipIdx);
if (!slugs.length) {
  console.error('usage: measure_painted_widths.mjs [--json] [--out FILE] <slug> [<slug>...]');
  process.exit(2);
}

const server = spawn('python3', ['-m', 'http.server', String(PORT), '-d', 'dist'], {
  stdio: 'ignore',
});
const stop = () => server.kill();
process.on('exit', stop);
await new Promise((r) => setTimeout(r, 700));

const browser = await chromium.launch();
/** slug -> src -> { perViewport: {vp: [widths]}, natural, sizes, srcset, cid } */
const out = {};

for (const slug of slugs) {
  const page = await browser.newPage({ deviceScaleFactor: 1 });
  const bySrc = {};
  for (const vp of SWEEP) {
    await page.setViewportSize({ width: vp, height: 900 });
    await page.goto(`http://127.0.0.1:${PORT}/${slug}/`, { waitUntil: 'load' });
    // Same de-lazying the harness does — a lazy image below the fold has no box yet.
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
    await page.waitForTimeout(400);

    const rows = await page.evaluate(() => {
      const seen = [];
      for (const img of Array.from(document.images)) {
        const box = img.getBoundingClientRect();
        if (box.width < 1) continue;
        // The FILE the tag names, not the candidate the browser chose: currentSrc moves
        // when srcset changes and would make a before/after comparison meaningless.
        const declared = (img.getAttribute('src') || img.currentSrc || '').split('/').pop();
        const cid = Array.from(img.attributes)
          .map((a) => a.name)
          .find((n) => n.startsWith('data-astro-cid-'));
        seen.push({
          declared,
          chosen: (img.currentSrc || '').split('/').pop(),
          painted: Math.round(box.width * 100) / 100,
          natural: img.naturalWidth,
          sizes: img.getAttribute('sizes') || '',
          srcset: img.getAttribute('srcset') || '',
          cid: cid || '',
          cls: (img.getAttribute('class') || '').slice(0, 70),
        });
      }
      return seen;
    });

    for (const r of rows) {
      const k = r.declared;
      bySrc[k] ??= { natural: r.natural, sizes: r.sizes, srcset: r.srcset, cid: r.cid, cls: r.cls, vp: {} };
      (bySrc[k].vp[vp] ??= []).push(r.painted);
      if (r.natural) bySrc[k].natural = Math.max(bySrc[k].natural, r.natural);
    }
  }
  out[slug] = bySrc;
  await page.close();
}
await browser.close();
stop();

if (outFile) writeFileSync(outFile, JSON.stringify(out, null, 1));
if (asJson) {
  console.log(JSON.stringify(out, null, 1));
} else {
  for (const [slug, bySrc] of Object.entries(out)) {
    console.log(`\n=== /${slug}/`);
    const entries = Object.entries(bySrc).sort(
      (a, b) => Math.max(...vals(b[1])) / b[1].natural - Math.max(...vals(a[1])) / a[1].natural,
    );
    for (const [src, d] of entries) {
      const widest = Math.max(...vals(d));
      const worst = (d.natural / Math.min(...vals(d))).toFixed(2);
      const sweep = SWEEP.map((v) => (d.vp[v] ? `${v}:${max(d.vp[v])}` : `${v}:-`)).join(' ');
      // vw ratio at the narrow end tells fluid from fixed at a glance.
      const vwLow = d.vp[375] ? ((max(d.vp[375]) / 375) * 100).toFixed(0) : '?';
      const vwHigh = d.vp[1280] ? ((max(d.vp[1280]) / 1280) * 100).toFixed(0) : '?';
      console.log(
        `  ${src}\n    natural=${d.natural} widest=${widest} worstRatio=${worst}x  ` +
          `vw@375=${vwLow}% vw@1280=${vwHigh}%  n/vp=${countBoxes(d)}\n` +
          `    ${sweep}\n` +
          (d.srcset ? `    srcset=${d.srcset.slice(0, 110)}\n` : '') +
          (d.sizes ? `    sizes=${d.sizes}\n` : ''),
      );
    }
  }
}

function vals(d) {
  return Object.values(d.vp).map(max);
}
function max(a) {
  return Math.max(...a);
}
function countBoxes(d) {
  return Math.max(...Object.values(d.vp).map((a) => a.length));
}
