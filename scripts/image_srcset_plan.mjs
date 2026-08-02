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
        naturalAt: {},
      };
      e.painted[vp] = r.painted;
      // Natural width PER VIEWPORT. Taking the max across the sweep and dividing it by the
      // minimum painted width pairs the file loaded at 1440 with the box painted at 375 —
      // a ratio no viewport ever experiences. That was harmless while `natural` was
      // constant (one file, no srcset) and became the dominant error the moment srcset
      // started working: after patching 212 tags the tool still reported 274 occurrences
      // over the cap, because it was measuring the fix against a ratio it had invented.
      // Each viewport is a fresh `goto`, so the per-viewport reading is the honest one.
      e.naturalAt[vp] = r.natural || null;
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
  // Per viewport: the file the browser actually loaded THERE against the box it painted
  // THERE. `e.natural` (the max across the sweep) is kept only as the master-width
  // reference for planning candidate widths, never as a numerator for the ratio.
  const ratios = SWEEP.filter((v) => e.painted[v] != null && e.naturalAt?.[v])
    .map((v) => e.naturalAt[v] / e.painted[v]);
  const worstRatio = ratios.length ? Math.max(...ratios) : e.natural / Math.min(...paintedVals);

  // SEGMENT ADAPTIVELY FROM THE MEASURED SWEEP, not into the four fixed Tailwind bands.
  //
  // The fixed-band form could not be satisfied for 68 of 292 occurrences, and adding more
  // variant files could never have fixed them. A band takes the MAXIMUM vw across its own
  // points, so when one band contains viewports whose painted width differs by more than
  // 2x — measured up to 3.70x on the congo-pair cards, 157.73px at one end and 407.17px at
  // the other — the declaration over-states at the narrow end by more than 2x. Every
  // candidate must satisfy `c >= declared`, so `c >= declared > 2 * painted` makes the cap
  // unreachable by construction. The granularity of `sizes` is the defect, not the ladder.
  //
  // So grow segments greedily instead: extend a segment only while ONE declaration still
  // fits every point in it, under two constraints that encode which way it is safe to be
  // wrong.
  //
  //   declared >= painted   — never under-declare. Under-declaring is the reverted bug:
  //                           the browser fetches a file smaller than the box and the page
  //                           ships visible blur. Bytes are recoverable; blur is not.
  //   declared <= 1.5x painted — leave room for a candidate to exist under the 2.0x cap.
  //
  // Boundaries land on measured sweep points, and SWEEP straddles every Tailwind
  // breakpoint (639/640, 767/768, 1023/1024), so a boundary is never interpolated across
  // the discontinuity where the layout actually switches.
  const pts = SWEEP.filter((v) => e.painted[v] != null);
  if (!pts.length) return { needsWork: false };

  /** The one declaration that covers every point in `run`, or null if none does. */
  const fit = (run) => {
    // Prefer vw when the painted width tracks the viewport, px when it does not; try both
    // and keep whichever satisfies the constraints for EVERY point.
    const vwNeeded = Math.max(...run.map((v) => e.painted[v] / v));
    const vw = Math.ceil(vwNeeded * 1000) / 10; // 0.1vw resolution
    const vwOk = run.every((v) => {
      const d = (vw / 100) * v;
      return d >= e.painted[v] - 0.5 && d <= e.painted[v] * 1.5;
    });
    if (vwOk) return { value: `${vw}vw`, kind: 'vw', vw };

    const pxNeeded = Math.max(...run.map((v) => e.painted[v]));
    const px = Math.ceil(pxNeeded);
    const pxOk = run.every((v) => px >= e.painted[v] - 0.5 && px <= e.painted[v] * 1.5);
    if (pxOk) return { value: `${px}px`, kind: 'px', px };

    return null;
  };

  const merged = [];
  let i = 0;
  while (i < pts.length) {
    let run = [pts[i]];
    let best = fit(run);
    let j = i + 1;
    while (j < pts.length) {
      const next = fit([...run, pts[j]]);
      if (!next) break;
      run = [...run, pts[j]];
      best = next;
      j++;
    }
    // A single point always fits itself (declared === painted), so `best` cannot be null.
    merged.push({ hi: run[run.length - 1], value: best.value, pts: run });
    i = j;
  }

  const sizesValue = merged
    .map((m, k) => (k === merged.length - 1 ? m.value : `(max-width:${m.hi}px) ${m.value}`))
    .join(', ');

  // Re-shape into the {band:{pts}} form the demand loop below already expects.
  const segs = merged.map((m) => ({ band: { pts: m.pts }, value: m.value, maxPx: Math.max(...m.pts.map((v) => e.painted[v])) }));

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
      // Round the demand UP to a tidy variant width, but proportionally: a flat 20px step
      // is 1.4% of a 1408px feature image and 143% of a 14px emoji, and rounding a 21px
      // demand up to 40 puts a 2.86x file in the box the rounding was meant to protect.
      const step = declared < 120 ? 4 : declared < 400 ? 10 : 20;
      demands.push({ vp: v, painted, declared: Math.ceil(declared / step) * step });
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
