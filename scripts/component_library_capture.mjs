#!/usr/bin/env node
/**
 * component_library_capture.mjs — photograph every live CAG component at
 * 375 / 768 / 1280 into docs/artifacts/component-library/ + manifest.json.
 *
 * Task D1. Read-only with respect to the site: it serves the already-built
 * dist/ over HTTP and screenshots elements. It never edits a page or component.
 *
 * Usage:
 *   node scripts/component_library_capture.mjs             # resolve + capture
 *   node scripts/component_library_capture.mjs --resolve   # resolve only
 *
 * Traps handled (all previously measured on this site):
 *  - A viewport screenshot resets scroll → we use locator.screenshot(), which
 *    scrolls the element into view itself.
 *  - Desktop-only / mobile-only components have a zero-size rect at the other
 *    widths → rect < 8px in either axis is recorded as null, not photographed.
 *  - Lazy images are still decoding when the shot is taken → after
 *    scrollIntoViewIfNeeded we wait, then await decode() on every incomplete
 *    image, so a straggler is not photographed blank.
 */

import { chromium } from 'playwright';
import { createServer } from 'node:http';
import { readFile, writeFile, mkdir, readdir, stat, unlink } from 'node:fs/promises';
import { existsSync } from 'node:fs';
import { execFileSync } from 'node:child_process';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const DIST = path.join(ROOT, 'dist');
const OUT = path.join(ROOT, 'docs/artifacts/component-library');
// 4399, not 4321 — 4321 is SITE_PORT in tests/render/lib/servers.ts and a
// concurrent render-harness run would collide with it.
const PORT = 4399;
const VIEWPORTS = [
  { vp: '375', width: 375, height: 900 },
  { vp: '768', width: 768, height: 1100 },
  { vp: '1280', width: 1280, height: 900 },
];
const MAX_H = 1400;

export const CATALOG = [
  { id:'hero-v3b',        category:'hero',    name:'Hero V3:b Authority Green',        page:'',                                          selector:'.hero-v3-b',                         source:'src/components/cag-library/HeroV3.astro' },
  { id:'hero-congo',      category:'hero',    name:'Split-Hero (congo for-sale)',       page:'congo-african-grey-for-sale',               selector:'.chero',                             source:'src/pages/congo-african-grey-for-sale/index.astro' },
  { id:'hero-timneh',     category:'hero',    name:'Split-Hero (timneh for-sale)',      page:'timneh-african-grey-for-sale',              selector:'.chero',                             source:'src/pages/timneh-african-grey-for-sale/index.astro' },
  { id:'hero-dna',        category:'hero',    name:'Dark + Grid (dna-tested)',          page:'dna-tested-african-grey-for-sale',          selector:'header.hero, .hero',                 source:'src/pages/dna-tested-african-grey-for-sale/index.astro' },
  { id:'hero-pair',       category:'hero',    name:'Polaroid Scatter (breeding pair)',  page:'african-grey-breeding-pair-for-sale',       selector:'.phero',                 source:'src/pages/african-grey-breeding-pair-for-sale/index.astro' },
  { id:'hero-hub',        category:'hero',    name:'Mosaic Metrics (hub)',              page:'african-grey-parrots-for-sale',             selector:'#main-content section.bg-logo-dark',                 source:'src/pages/african-grey-parrots-for-sale/index.astro' },
  { id:'hero-eggs',       category:'hero',    name:'Eggs Hero',                         page:'african-grey-parrot-bird-eggs-for-sale-usa', selector:'.egg-hero, header.hero, .hero',     source:'src/pages/african-grey-parrot-bird-eggs-for-sale-usa/index.astro' },
  { id:'hero-cvt',        category:'hero',    name:'Comparison Two-Portrait Hero',      page:'congo-vs-timneh-african-grey',              selector:'header.hero, .hero, .cvt-hero',      source:'src/pages/congo-vs-timneh-african-grey/index.astro' },
  { id:'counter-home',    category:'counter', name:'Counter Snippet (home)',            page:'',                                          selector:'.counter-snippet',                   source:'src/components/cag-library/CounterSnippet.astro' },
  { id:'counter-congo',   category:'counter', name:'Counter Strip (congo)',             page:'congo-african-grey-for-sale',               selector:'.counter-row',                      source:'src/pages/congo-african-grey-for-sale/index.astro' },
  { id:'counter-eggs',    category:'counter', name:'Counter Strip (eggs)',              page:'african-grey-parrot-bird-eggs-for-sale-usa', selector:'.counter-row',                     source:'src/pages/african-grey-parrot-bird-eggs-for-sale-usa/index.astro' },
  { id:'dial-timneh',     category:'toc',     name:'Desktop Dial .tdial (canonical)',   page:'timneh-african-grey-for-sale',              selector:'.tdial',                             source:'src/pages/timneh-african-grey-for-sale/index.astro' },
  { id:'dial-congo',      category:'toc',     name:'Desktop Dial .cdial',               page:'congo-african-grey-for-sale',               selector:'.cdial',                             source:'src/pages/congo-african-grey-for-sale/index.astro' },
  { id:'rail-congo',      category:'toc',     name:'Mobile Rail .chero-rail',           page:'congo-african-grey-for-sale',               selector:'.chero-rail',                        source:'src/pages/congo-african-grey-for-sale/index.astro' },
  { id:'rail-eggs',       category:'toc',     name:'Mobile Rail .egg-rail',             page:'african-grey-parrot-bird-eggs-for-sale-usa', selector:'.egg-rail',                         source:'src/pages/african-grey-parrot-bird-eggs-for-sale-usa/index.astro' },
  { id:'rail-cvt',        category:'toc',     name:'Comparison Rail .cvt-rail',         page:'congo-vs-timneh-african-grey',              selector:'.cvt-rail',                          source:'src/pages/congo-vs-timneh-african-grey/index.astro' },
  { id:'jumprail-home',   category:'toc',     name:'JumpRail Dot Rail (desktop)',       page:'',                                          selector:'#cag-jump-rail',                     source:'src/components/cag-library/JumpRail.astro' },
  { id:'jumpsheet-home',  category:'toc',     name:'JumpRail Sections Sheet (mobile)',  page:'',                                          selector:'#cag-section-sheet',                 source:'src/components/cag-library/JumpRail.astro', open:'#cag-sections-fab', openMaxVp:768 },
  { id:'toc-v3',          category:'toc',     name:'TocV3 Grouped',                     page:'',                                          selector:'nav.toc-v3, .toc-v3, [data-toc]',    source:'src/components/cag-library/TocV3.astro' },
  { id:'table-mvf',       category:'table',   name:'Male vs Female (home)',             page:'',                                          selector:'#compare-species table', nth:1,      source:'src/pages/index.astro' },
  { id:'table-others',    category:'table',   name:'Grey vs Macaw/Cockatoo/Amazon (home)', page:'',                                       selector:'#compare-species table', nth:2,      source:'src/pages/index.astro' },
  { id:'table-cmp',       category:'table',   name:'Comparison .cmp-tbl (congo-vs-timneh)',   page:'congo-vs-timneh-african-grey', selector:'table.cmp-tbl',   source:'src/pages/congo-vs-timneh-african-grey/index.astro' },
  { id:'table-score',     category:'table',   name:'Comparison .score-tbl (congo-vs-timneh)', page:'congo-vs-timneh-african-grey', selector:'table.score-tbl', source:'src/pages/congo-vs-timneh-african-grey/index.astro' },
  { id:'table-tblc',      category:'table',   name:'.tblC (hand-raised)',               page:'hand-raised-african-grey-parrot-for-sale',  selector:'.tblC',                              source:'src/pages/hand-raised-african-grey-parrot-for-sale/index.astro' },
  { id:'pricing-table',   category:'table',   name:'PricingTable Classic',              page:'',                                          selector:'#pricing',                           source:'src/components/cag-library/PricingTable.astro' },
  { id:'faq-home',        category:'faq',     name:'FAQ Accordion (home)',              page:'',                                          selector:'#faq',                               source:'src/pages/index.astro' },
  { id:'shipping-home',   category:'shipping',name:'Shipping Split (home)',             page:'',                                          selector:'#shipping',                          source:'src/pages/index.astro' },
  { id:'bird-card',       category:'bird-card', name:'BirdCard',                        page:'',                                          selector:'#available-birds article',           source:'src/components/BirdCard.astro' },
  { id:'mini-bird-card',  category:'bird-card', name:'MiniBirdCard',                    page:'african-grey-breeding-pair-for-sale',       selector:'.mbc, .mini-bird, [class*="minibird"]', source:'src/components/cag-library/MiniBirdCard.astro' },
  { id:'reviews-feature', category:'reviews', name:'Testimonials Feature',              page:'',                                          selector:'#reviews-mid',                       source:'src/components/cag-library/Testimonials.astro' },
  { id:'reviews-grid',    category:'reviews', name:'Testimonials Grid',                 page:'',                                          selector:'#reviews',                           source:'src/components/cag-library/Testimonials.astro' },
  { id:'key-takeaway',    category:'key-takeaway', name:'KeyTakeawayV2',                page:'',                                          selector:'[class*="takeaway"], .key-takeaway', source:'src/components/cag-library/KeyTakeawayV2.astro' },
  { id:'owner-card',      category:'owner',   name:'OwnerCard',                         page:'',                                          selector:'#about',                             source:'src/components/cag-library/OwnerCard.astro' },
  { id:'trust-stats',     category:'trust',   name:'TrustStats Classic',                page:'',                                          selector:'#health',                            source:'src/components/cag-library/TrustStats.astro' },
  { id:'scam-grid',       category:'trust',   name:'ScamAwareness Grid + Proof List',   page:'',                                          selector:'#trust',                             source:'src/components/cag-library/ScamAwareness.astro' },
  { id:'seam',            category:'seam',    name:'Seam Divider',                      page:'',                                          selector:'.cag-seam',                          source:'src/pages/index.astro' },
  { id:'newsletter-v2',   category:'newsletter', name:'NewsletterV2',                   page:'',                                          selector:'div[style*="#f0f9f4"]', source:'src/components/cag-library/NewsletterV2.astro' },
  { id:'inquiry-form',    category:'form',    name:'InquiryForm',                       page:'',                                          selector:'#contact',                           source:'src/components/cag-inquiry-form.astro' },
];

/* ---------------------------------------------------------------- server */

const MIME = {
  '.html':'text/html; charset=utf-8', '.css':'text/css', '.js':'text/javascript',
  '.json':'application/json', '.webp':'image/webp', '.png':'image/png',
  '.jpg':'image/jpeg', '.jpeg':'image/jpeg', '.svg':'image/svg+xml',
  '.mp4':'video/mp4', '.woff2':'font/woff2', '.woff':'font/woff',
  '.ico':'image/x-icon', '.txt':'text/plain', '.xml':'application/xml',
};

function startServer() {
  const server = createServer(async (req, res) => {
    try {
      let p = decodeURIComponent(new URL(req.url, 'http://x').pathname);
      let file = path.join(DIST, p);
      if (!file.startsWith(DIST)) { res.writeHead(403).end(); return; }
      let s = existsSync(file) ? await stat(file) : null;
      if (s?.isDirectory()) { file = path.join(file, 'index.html'); s = existsSync(file) ? await stat(file) : null; }
      if (!s) { res.writeHead(404).end('not found'); return; }
      const body = await readFile(file);
      res.writeHead(200, { 'Content-Type': MIME[path.extname(file).toLowerCase()] || 'application/octet-stream' });
      res.end(body);
    } catch { res.writeHead(500).end(); }
  });
  return new Promise((resolve, reject) => {
    server.on('error', reject);
    server.listen(PORT, '127.0.0.1', () => resolve(server));
  });
}

/* ------------------------------------------------------------- capturing */

/** Navigate with a hard bound: `load` then a best-effort networkidle.
 *  A page carrying a Google Maps iframe or a Formspree endpoint may never
 *  reach networkidle, so the idle wait is advisory and its timeout is not
 *  an error. */
async function goto(page, url) {
  await page.goto(url, { waitUntil: 'load', timeout: 25000 });
  await page.waitForLoadState('networkidle', { timeout: 6000 }).catch(() => {});
}

/** Give still-loading images a bounded decode budget, then move on.
 *  decode() on an image whose src never resolves never settles — and an
 *  unbounded await here hangs the whole run — so the budget is a race, not
 *  a promise-all. Still-loading is not broken; it is just late. */
async function settle(page) {
  await page.evaluate(() => Promise.race([
    Promise.all([...document.images].filter(i => !i.complete).map(i => i.decode().catch(() => {}))),
    new Promise(r => setTimeout(r, 2500)),
  ])).catch(() => {});
}

/** Hide any fixed/sticky page chrome that is not the target and does not
 *  contain (or is not contained by) the target, so a sticky header/footer/
 *  jump-rail/tab-bar cannot bleed into the element screenshot. Uses
 *  visibility, not display, so layout — and the target's own boundingBox —
 *  does not shift. Rows that ARE the chrome (e.g. the jump rail itself) are
 *  unaffected because `contains` exempts them.
 *  Assumption: any fixed/sticky element outside the target's ancestor/
 *  descendant chain is page chrome, not part of the component being
 *  photographed — true for this site's header/footer/rails/tab-bars, but it
 *  would wrongly hide a fixed element that is a sibling-of-content design
 *  choice inside some future component. */
async function hideChrome(loc) {
  await loc.evaluate((target) => {
    for (const el of document.querySelectorAll('*')) {
      if (el === target || target.contains(el) || el.contains(target)) continue;
      const cs = getComputedStyle(el);
      if (cs.position === 'fixed' || cs.position === 'sticky') {
        el.style.visibility = 'hidden';
      }
    }
  });
}

async function resolveOn(page, row) {
  return page.evaluate(({ sel, nth }) => {
    for (const part of sel.split(',').map(s => s.trim()).filter(Boolean)) {
      if (document.querySelectorAll(part).length > (nth ?? 0)) return part;
    }
    return null;
  }, { sel: row.selector, nth: row.nth });
}

function toWebp(png, outPath) {
  const script = `
import io, sys
from PIL import Image
src, dst = sys.argv[1], sys.argv[2]
im = Image.open(src).convert('RGB')
MAX_H = int(sys.argv[3])
if im.height > MAX_H:            # cap tall elements (a whole FAQ is ~6000px)
    im = im.crop((0, 0, im.width, MAX_H))
if im.width > 1280:
    im = im.resize((1280, round(im.height * 1280 / im.width)), Image.LANCZOS)
im.save(dst, 'WEBP', quality=82, method=6)
import os
# MAX_BYTES = 90 KB per image. The plan said <=60 KB; 90 KB was chosen
# deliberately so tables stay legible at 1280 — the folder runs ~3.4 MB
# against a 6 MB budget, and the D2 artifact inlines it under a 16 MB cap,
# so the extra headroom is affordable.
if os.path.getsize(dst) > 90*1024:
    im.save(dst, 'WEBP', quality=70, method=6)
if os.path.getsize(dst) > 90*1024 and im.width > 1000:
    im2 = im.resize((1000, round(im.height * 1000 / im.width)), Image.LANCZOS)
    im2.save(dst, 'WEBP', quality=70, method=6)
    im = im2
print(im.width, im.height)
`;
  const out = execFileSync('python3', ['-c', script, png, outPath, String(MAX_H)], { encoding: 'utf8' }).trim();
  const [w, h] = out.split(/\s+/).map(Number);
  return { w, h };
}

async function main() {
  try {
    execFileSync('python3', ['-c', 'import PIL']);
  } catch {
    console.error('Pillow (PIL) is required: python3 -m pip install pillow');
    process.exit(2);
  }

  const resolveOnly = process.argv.includes('--resolve');
  const onlyArg = process.argv.find(a => a.startsWith('--only='));
  const only = onlyArg ? onlyArg.slice(7).split(',').map(s => s.trim()) : null;
  const catalog = only ? CATALOG.filter(r => only.includes(r.id)) : CATALOG;
  await mkdir(OUT, { recursive: true });

  let server, browser;
  try {
    server = await startServer();
    browser = await chromium.launch();

    // ---- pass 1: resolve every selector on its built page (at 1280) ------
    const resolvePage = await (await browser.newContext({ viewport: { width: 1280, height: 900 }, deviceScaleFactor: 1 })).newPage();
    const rows = [];
    const dropped = [];
    const corrected = [];
    for (const row of catalog) {
      process.stdout.write(`  resolving ${row.id}\n`);
      let hit = null;
      try {
        await goto(resolvePage, `http://127.0.0.1:${PORT}/${row.page ? row.page + '/' : ''}`);
        hit = await resolveOn(resolvePage, row);
      } catch (e) {
        console.log(`  NAV   ${row.id.padEnd(16)} ${e.message.split('\n')[0]}`);
      }
      if (!hit && row.openMaxVp) hit = row.selector.split(',')[0].trim(); // hidden-until-opened
      if (!hit) {
        // one more try at 375 — a mobile-only component is display:none at 1280
        // but still present in the DOM, so querySelector would have found it;
        // absence here means it is genuinely not on the page.
        dropped.push(row.id);
        console.log(`  DROP  ${row.id.padEnd(16)} no match for ${row.selector}`);
        continue;
      }
      if (hit !== row.selector) { corrected.push(`${row.id}: "${row.selector}" -> "${hit}"`); }
      rows.push({ ...row, selector: hit, captures: {} });
    }
    console.log(`\nResolve: ${catalog.length} rows · ${rows.length} resolved · ${dropped.length} dropped`);
    if (corrected.length) { console.log('Corrected (comma-list narrowed to first match):'); corrected.forEach(c => console.log('  ' + c)); }
    await resolvePage.context().close();
    if (resolveOnly) return;

    // ---- pass 2: capture ---------------------------------------------
    const tmp = path.join(OUT, '.tmp.png');
    for (const { vp, width, height } of VIEWPORTS) {
      const ctx = await browser.newContext({ viewport: { width, height }, deviceScaleFactor: 1 });
      const page = await ctx.newPage();
      for (const row of rows) {
        row.captures[vp] = null;
        try {
          await goto(page, `http://127.0.0.1:${PORT}/${row.page ? row.page + '/' : ''}`);
          if (row.open && width <= (row.openMaxVp ?? 99999)) {
            await page.evaluate(() => window.scrollTo(0, 1800));
            await page.waitForTimeout(700);
            const btn = page.locator(row.open).first();
            if (await btn.count() && await btn.isVisible()) { await btn.click(); await page.waitForTimeout(500); }
          }
          const loc = page.locator(row.selector).nth(row.nth ?? 0);
          if (!(await loc.count())) continue;
          let box = await loc.boundingBox();
          if (!box || box.width < 8 || box.height < 8) continue;
          await loc.scrollIntoViewIfNeeded().catch(() => {});
          await page.waitForTimeout(400);
          await settle(page);
          await hideChrome(loc).catch(() => {});
          box = await loc.boundingBox();
          if (!box || box.width < 8 || box.height < 8) continue;
          // locator.screenshot() has no `clip` option — the MAX_H cap is applied
          // by the Pillow step, which crops before it resizes.
          await loc.screenshot({ type: 'png', path: tmp });
          const file = `${row.id}-${vp}.webp`;
          const { w, h } = toWebp(tmp, path.join(OUT, file));
          const bytes = (await stat(path.join(OUT, file))).size;
          row.captures[vp] = { file, w, h, bytes };
          console.log(`  ${vp.padStart(4)}  ${row.id.padEnd(16)} ${w}x${h}  ${(bytes/1024).toFixed(0)}KB`);
        } catch (e) {
          console.log(`  ${vp.padStart(4)}  ${row.id.padEnd(16)} ERROR ${e.message.split('\n')[0]}`);
        }
      }
      await ctx.close();
    }
    await unlink(tmp).catch(() => {});

    const commit = execFileSync('git', ['rev-parse', 'HEAD'], { cwd: ROOT, encoding: 'utf8' }).trim();
    let out = rows.map(({ open, openMaxVp, nth, ...r }) => r);
    if (only && existsSync(path.join(OUT, 'manifest.json'))) {
      const prev = JSON.parse(await readFile(path.join(OUT, 'manifest.json'), 'utf8'));
      const byId = new Map(out.map(r => [r.id, r]));
      out = prev.rows.map(r => byId.get(r.id) ?? r);
      for (const r of byId.values()) if (!out.some(o => o.id === r.id)) out.push(r);
    }
    const manifest = { generated: new Date().toISOString(), commit, rows: out };
    await writeFile(path.join(OUT, 'manifest.json'), JSON.stringify(manifest, null, 2) + '\n');

    const files = await readdir(OUT);
    let total = 0;
    for (const f of files) total += (await stat(path.join(OUT, f))).size;
    const caps = rows.reduce((n, r) => n + Object.values(r.captures).filter(Boolean).length, 0);
    console.log(`\n${rows.length} rows · ${caps} captures · ${dropped.length} dropped · folder ${(total/1048576).toFixed(2)} MB`);
    if (total > 6 * 1048576) console.log('WARNING: folder exceeds the 6 MB budget for the D2 artifact.');

    // expected = every resolved row at all 3 viewports, minus rows too small
    // to ever be captured at that viewport (recorded null and skipped above
    // isn't distinguishable here, so this is a coarse ceiling: rows × 3).
    const expected = rows.length * VIEWPORTS.length;
    if (caps < 0.5 * expected) {
      console.error(`\nFAILURE: only ${caps}/${expected} captures succeeded (< 50% threshold).`);
      process.exitCode = 1;
    }
  } finally {
    await browser?.close();
    server?.close();
  }
}

if (process.argv[1] && fileURLToPath(import.meta.url) === path.resolve(process.argv[1])) {
  main().catch(e => { console.error(e); process.exit(1); });
}
