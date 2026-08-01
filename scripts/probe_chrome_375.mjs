#!/usr/bin/env node
// One-off diagnostic for the 375px chrome-measurement question (plan Task 2).
//
// measureTopChrome reports 96px (header only) at 375px on dna-tested and hand-raised,
// but 158px (header + rail) at 768px on baby — for the same header+rail shape, with all
// three rails declared inside @media (max-width:980px) and NOT hidden at <=640px.
//
// Either the rails genuinely stop being PINNED at 375px (a position:sticky element only
// sticks within its parent's box, and measureTopChrome scrolls 1.5 viewports before
// measuring — at 375px that is ~1,220px, possibly past the rail's parent), or the probe
// misses them. Those have opposite fixes, so this measures instead of reasoning.
//
// It DECIDES NOTHING. It prints every sticky/fixed element with its box and its parent's
// bottom, at the exact scroll position the real probe measures from, so the branch is
// chosen on evidence.
//
// Run:  node scripts/probe_chrome_375.mjs
// Needs: a server on 4321 rooted at dist/  (npx http-server dist -p 4321 --silent)

import { chromium } from 'playwright';

const PAGES = [
  'dna-tested-african-grey-for-sale',
  'hand-raised-african-grey-parrot-for-sale',
  'baby-african-grey-parrot-for-sale',
];
const VIEWPORTS = [375, 768];

const browser = await chromium.launch();

for (const slug of PAGES) {
  for (const width of VIEWPORTS) {
    const page = await browser.newPage({
      viewport: { width, height: 800 },
      deviceScaleFactor: 1,
    });
    await page.goto(`http://localhost:4321/${slug}/`, { waitUntil: 'load' });

    // Exactly what measureTopChrome does: 1.5 viewports down, settle, then look.
    await page.evaluate(() => window.scrollBy(0, Math.round(window.innerHeight * 1.5)));
    await page.waitForTimeout(250);

    const seen = await page.evaluate(() => {
      const out = [];
      for (const el of Array.from(document.body.querySelectorAll('*'))) {
        const cs = getComputedStyle(el);
        if (cs.position !== 'fixed' && cs.position !== 'sticky') continue;
        if (cs.visibility === 'hidden' || cs.display === 'none') continue;
        const b = el.getBoundingClientRect();
        if (b.height === 0 || b.width === 0) continue;
        out.push({
          tag: el.tagName.toLowerCase(),
          cls: (el.className || '').toString().trim().split(/\s+/).slice(0, 2).join(' '),
          position: cs.position,
          cssTop: cs.top,
          opacity: cs.opacity,
          top: Math.round(b.top),
          bottom: Math.round(b.bottom),
          left: Math.round(b.left),
          right: Math.round(b.right),
          // Why a sticky element may have stopped sticking: its parent scrolled past.
          parentBottom: el.parentElement
            ? Math.round(el.parentElement.getBoundingClientRect().bottom)
            : null,
          // The three guards in measureTopChrome that can exclude a real element.
          wouldPassZeroSize: b.height !== 0 && b.width !== 0,
          wouldPassHorizontal: !(b.right <= 0 || b.left >= window.innerWidth),
          wouldPassOpacity: parseFloat(cs.opacity) !== 0,
        });
      }
      return { scrollY: Math.round(window.scrollY), innerWidth: window.innerWidth, els: out };
    });

    console.log(`\n=== ${slug} @ ${width}px  (scrollY=${seen.scrollY}) ===`);
    if (!seen.els.length) console.log('  no sticky/fixed elements visible');
    for (const e of seen.els) {
      const pinned = e.top <= 2 ? 'PINNED-AT-TOP' : `top=${e.top}`;
      const guards =
        [
          e.wouldPassZeroSize ? null : 'ZERO-SIZE',
          e.wouldPassHorizontal ? null : 'OFF-CANVAS',
          e.wouldPassOpacity ? null : 'OPACITY-0',
        ]
          .filter(Boolean)
          .join(',') || 'ok';
      console.log(
        `  ${e.position.padEnd(6)} ${(e.tag + '.' + e.cls).padEnd(26)} css-top=${String(e.cssTop).padEnd(7)} ${pinned.padEnd(14)} bottom=${String(e.bottom).padEnd(5)} L/R=${e.left}/${e.right} parentBottom=${e.parentBottom} guards=${guards}`,
      );
    }
    await page.close();
  }
}

await browser.close();
