#!/usr/bin/env node
/**
 * Measure what every <img> on a page PAINTS at, band by band, then derive the `sizes`
 * value and the variant widths that make the browser fetch a file no more than 2x the
 * box it lands in.
 *
 * This exists because the first srcset attempt on this site was reverted for shipping
 * visible blur. It applied ONE blanket `sizes="(max-width:640px) 45vw, 356px"` to every
 * image, conflating gallery cells (genuinely ~45vw) with full-width feature images (343px
 * at a 375 viewport — 92vw). The browser did as it was told and loaded a 168px file into
 * a 343px box.
 *
 * `sizes` is a promise about geometry. The only way to keep it is to measure it, per
 * image, per occurrence, in a real browser. So:
 *
 *   1. Sweep viewports that straddle every Tailwind breakpoint (639/640, 767/768,
 *      1023/1024) so a band's edges are measured rather than interpolated. The site's
 *      layout switches AT those numbers, and painted width is NOT monotonic across them
 *      — a gallery cell paints 608px at 640 and 260px at 768. Interpolating between the
 *      two would produce a `sizes` that is wrong across the whole 640-767 band.
 *   2. Classify each band as FIXED (painted barely moves -> emit px) or FLUID (painted
 *      tracks the viewport -> emit vw). Emitting px for a fluid band is precisely the
 *      blur bug: correct at the measured point, wrong everywhere else in the band.
 *   3. Key by OCCURRENCE, not by filename. Several images appear twice on one page in
 *      different boxes; one `sizes` for both would be wrong for one of them.
 *
 * Output is a JSON plan; scripts/image_srcset_apply.mjs consumes it.
 *
 *   node scripts/image_srcset_plan.mjs --out plan.json <slug> [<slug>...]
 */
import { chromium } from '@playwright/test';
import { spawn } from 'node:child_process';
import { writeFileSync } from 'node:fs';

/** Straddles every Tailwind breakpoint so band EDGES are measured, never interpolated. */
const SWEEP = [375, 414, 480, 639, 640, 767, 768, 900, 1023, 1024, 1280, 1440];
const BANDS = [
  { lo: 0, hi: 639, pts: [375, 414, 480, 639] },
  { lo: 640, hi: 767, pts: [640, 767] },
  { lo: 768, hi: 1023, pts: [768, 900, 1023] },
  { lo: 1024, hi: Infinity, pts: [1024, 1280, 1440] },
];
const PORT = 4327; // not 4321/4322: those are the render harness's own servers
/** The check's own threshold. Stay under it with margin, never at it. */
const MAX_RATIO = 2.0;
const TARGET_RATIO = 1.7;

const args = process.argv.slice(2);
const outIdx = args.indexOf('--out');
const outFile = outIdx >= 0 ? args[outIdx + 1] : 'image-srcset-plan.json';
const skipIdx = outIdx >= 0 ? outIdx + 1 : -1;
const slugs = args.filter((a, i) => !a.startsWith('--') && i !== skipIdx);
if (!slugs.length) {
  console.error('usage: image_srcset_plan.mjs [--out FILE] <slug> [<slug>...]');
  process.exit(2);
}

const server = spawn('python3', ['-m', 'http.server', String(PORT), '-d', 'dist'], {
  stdio: 'ignore',
});
process.on('exit', () => server.kill());
await new Promise((r) => setTimeout(r, 700));

const browser = await chromium.launch();
const plan = { generated: new Date().toISOString().slice(0, 10), pages: {} };

for (const slug of slugs) {
  const page = await browser.newPage({ deviceScaleFactor: 1 });
  /** occurrenceKey -> { src, natural, painted: {vp: px}, srcset, sizes, hasWidthAttr } */
  const occ = new Map();

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
    await page.waitForTimeout(350);

    const rows = await page.evaluate(() => {
      const perSrc = new Map();
      const out = [];
      for (const img of Array.from(document.images)) {
        // The DECLARED src, never currentSrc: currentSrc moves the moment a srcset is
        // added, so keying on it would make every before/after comparison meaningless
        // and would renumber occurrences mid-fix.
        const src = img.getAttribute('src') || '';
        const n = (perSrc.get(src) || 0) + 1;
        perSrc.set(src, n);
        const box = img.getBoundingClientRect();
        if (box.width < 1) continue;
        // The astro scope id says WHICH COMPONENT rendered this tag. Card images come
        // from a data array inside a shared component, not from a literal <img> in the
        // page, so the patch has to land on the component — and every card it renders
        // shares one geometry, which is exactly what one `sizes` value wants.
        const cid = Array.from(img.attributes)
          .map((a) => a.name)
          .find((nm) => nm.startsWith('data-astro-cid-')) || '';
        out.push({
          key: `${src}#${n}`,
          src,
          nth: n,
          cid,
          cls: (img.getAttribute('class') || '').slice(0, 90),
          painted: Math.round(box.width * 100) / 100,
          natural: img.naturalWidth,
          srcset: img.getAttribute('srcset') || '',
          sizes: img.getAttribute('sizes') || '',
        });
      }
      return out;
    });

    for (const r of rows) {
      const e = occ.get(r.key) || {
        src: r.src,
        nth: r.nth,
        cid: r.cid,
        cls: r.cls,
        natural: r.natural,
        srcset: r.srcset,
        sizes: r.sizes,
        painted: {},
      };
      e.painted[vp] = r.painted;
      if (r.natural) e.natural = Math.max(e.natural, r.natural);
      occ.set(r.key, e);
    }
  }
  await page.close();

  plan.pages[slug] = [...occ.entries()]
    .map(([key, e]) => ({ key, ...e, ...derive(e) }))
    .filter((e) => e.needsWork);
}
await browser.close();
server.kill();

writeFileSync(outFile, JSON.stringify(plan, null, 1));

let total = 0;
for (const [slug, items] of Object.entries(plan.pages)) {
  if (!items.length) continue;
  console.log(`\n=== /${slug}/  (${items.length} image occurrence(s) to fix)`);
  for (const it of items) {
    total++;
    console.log(
      `  ${it.src}#${it.nth}\n` +
        `    natural=${it.natural} worst=${it.worstRatio.toFixed(2)}x  ` +
        `painted ${SWEEP.map((v) => `${v}:${it.painted[v] ?? '-'}`).join(' ')}\n` +
        `    sizes="${it.sizesValue}"\n` +
        `    want widths: ${it.wantWidths.join(', ')}  ->  worst after: ${it.worstAfter.toFixed(2)}x` +
        (it.worstAfter > MAX_RATIO ? '   *** PLAN DOES NOT CLEAR THE CAP ***' : ''),
    );
  }
}
console.log(`\n${total} occurrence(s) planned across ${Object.keys(plan.pages).length} page(s)`);

/**
 * Turn a painted-width sweep into a `sizes` value and the candidate widths it needs.
 */
function derive(e) {
  const paintedVals = SWEEP.map((v) => e.painted[v]).filter((x) => x != null);
  if (!paintedVals.length || !e.natural) return { needsWork: false };
  const worstRatio = e.natural / Math.min(...paintedVals);

  const segs = [];
  for (const band of BANDS) {
    const pts = band.pts.filter((v) => e.painted[v] != null);
    if (!pts.length) continue;
    const px = pts.map((v) => e.painted[v]);
    const lo = Math.min(...px);
    const hi = Math.max(...px);
    // FIXED vs FLUID. A band whose painted width barely moves across its own width range
    // is a fixed panel and must be declared in px — declaring vw there would shrink the
    // request on narrow screens inside the band. A band where painted tracks the viewport
    // must be declared in vw — declaring px there is the reverted bug.
    const fluid = (hi - lo) / hi > 0.12;
    if (fluid) {
      const vw = Math.ceil(Math.max(...pts.map((v) => e.painted[v] / v)) * 100);
      segs.push({ band, value: `${vw}vw`, maxPx: hi });
    } else {
      segs.push({ band, value: `${Math.ceil(hi)}px`, maxPx: hi });
    }
  }
  if (!segs.length) return { needsWork: false };

  // Merge adjacent bands that resolve to the same value, so `sizes` stays readable.
  const merged = [];
  for (const s of segs) {
    const last = merged[merged.length - 1];
    if (last && last.value === s.value) {
      last.hi = s.band.hi;
      last.maxPx = Math.max(last.maxPx, s.maxPx);
    } else merged.push({ hi: s.band.hi, value: s.value, maxPx: s.maxPx });
  }
  const sizesValue = merged
    .map((m, i) =>
      i === merged.length - 1 ? m.value : `(max-width:${m.hi}px) ${m.value}`,
    )
    .join(', ');

  // What the browser will actually ASK FOR at each measured viewport, given the `sizes`
  // above. At DPR 1 it then picks the smallest candidate >= that number, so this is the
  // set of widths that have to exist.
  const demands = [];
  for (const s of segs) {
    for (const v of s.band.pts) {
      const painted = e.painted[v];
      if (painted == null) continue;
      const declared = s.value.endsWith('vw')
        ? (parseFloat(s.value) / 100) * v
        : parseFloat(s.value);
      demands.push({ vp: v, painted, declared: Math.ceil(declared / 20) * 20 });
    }
  }

  // One variant per distinct demand would mean nine files per image. Merge a smaller
  // demand into a larger one whenever the larger still lands under the ratio cap for the
  // smaller's box — then VERIFY, and unmerge anything the verification rejects. Merging
  // by a fixed tolerance without re-checking the ratio is how a "reasonable-looking"
  // ladder ships a file 2.4x its box.
  const wantWidths = [];
  for (const w of [...new Set(demands.map((d) => d.declared))].sort((a, b) => b - a)) {
    const covered = wantWidths.find((existing) => {
      const users = demands.filter((d) => d.declared <= existing && d.declared >= w);
      return users.every((d) => existing / d.painted <= MAX_RATIO * 0.95);
    });
    if (!covered) wantWidths.push(w);
  }
  wantWidths.sort((a, b) => a - b);

  // Drop anything at or above the master — the master is always the top candidate.
  const finalWidths = wantWidths.filter((w) => w > 40 && w < e.natural * 0.95);
  const widest = Math.max(...paintedVals);

  // Prove the plan on its own numbers before anyone generates a file from it: for every
  // measured viewport, resolve which candidate the browser would pick and check the ratio.
  const candidates = [...finalWidths, e.natural].sort((a, b) => a - b);
  const worstAfter = Math.max(
    ...demands.map((d) => {
      const pick = candidates.find((c) => c >= d.declared) ?? e.natural;
      return pick / d.painted;
    }),
  );

  const needsWork = worstRatio > MAX_RATIO;
  return { needsWork, worstRatio, sizesValue, wantWidths: finalWidths, widest, worstAfter };
}
