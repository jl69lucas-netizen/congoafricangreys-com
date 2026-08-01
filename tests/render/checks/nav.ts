import { register, type CheckResult, type Defect } from '../lib/registry.js';
import { measureTopChrome, resetScrollInstant, waitForScrollSettle } from '../lib/probes.js';
import type { Page } from '@playwright/test';

register({
  id: 'nav-anchors-resolve',
  family: 'NAV',
  severity: 'advisory',
  describe: 'every in-page #anchor points at an element that exists',
  minExamined: 2,
  async run(page: Page, viewport: number): Promise<CheckResult> {
    const r = await page.evaluate(() => {
      const links = Array.from(document.querySelectorAll<HTMLAnchorElement>('a[href^="#"]')).filter(
        (a) => (a.getAttribute('href') || '').length > 1,
      );
      const dead: string[] = [];
      for (const a of links) {
        const raw = a.getAttribute('href') as string;
        const id = decodeURIComponent(raw.slice(1));
        const byId = document.getElementById(id);
        const byName = document.querySelector(`[name="${CSS.escape(id)}"]`);
        if (!byId && !byName) dead.push(raw);
      }
      return { examined: links.length, dead: Array.from(new Set(dead)).slice(0, 10) };
    });

    return {
      examined: r.examined,
      defects: r.dead.length
        ? [
            {
              checkId: 'nav-anchors-resolve',
              family: 'NAV' as const,
              viewport,
              message: `dead in-page anchor(s): ${r.dead.join(', ')}`,
            },
          ]
        : [],
    };
  },
});

register({
  id: 'nav-jump-target-lands',
  family: 'NAV',
  severity: 'advisory',
  describe: 'clicking an in-page link must leave its target visible below the sticky chrome',
  minExamined: 2,
  async run(page: Page, viewport: number): Promise<CheckResult> {
    const defects: Defect[] = [];
    const chrome = await measureTopChrome(page);

    if (chrome.implausible) {
      defects.push({
        checkId: 'nav-jump-target-lands',
        family: 'NAV' as const,
        viewport,
        message: `pinned chrome measures ${chrome.height}px, over 40% of the viewport — refusing to judge landings against a number that is probably wrong. Parts: ${JSON.stringify(chrome.parts)}`,
      });
      return { examined: 0, defects };
    }

    // One entry per unique target, and only targets reachable from a link with a
    // real box. 0x0 duplicates and sr-only skip links are not user-facing chips;
    // clicking them via a synthetic pointer event hangs for 30s and then throws.
    const targets: string[] = await page.evaluate(() => {
      const byHref = new Map<string, boolean>();
      for (const a of Array.from(document.querySelectorAll<HTMLAnchorElement>('a[href^="#"]'))) {
        const href = a.getAttribute('href') || '';
        if (href.length < 2) continue;
        if (!document.getElementById(decodeURIComponent(href.slice(1)))) continue;
        const box = a.getBoundingClientRect();
        const cs = getComputedStyle(a);
        if (cs.visibility === 'hidden' || cs.display === 'none') continue;
        if (box.width < 8 || box.height < 8) continue; // 0x0 dupes and sr-only
        byHref.set(href, true);
      }
      return Array.from(byHref.keys());
    });

    const lo = chrome.height - 8;
    const hi = chrome.height + 60;

    for (const href of targets) {
      try {
        await resetScrollInstant(page);

        // Click the first link for this href that has a real box, in the page
        // itself. This triggers the browser's own fragment navigation — the
        // behaviour a user gets — without requiring viewport visibility.
        const clicked = await page.evaluate((h: string) => {
          const links = Array.from(
            document.querySelectorAll<HTMLAnchorElement>(`a[href="${h.replace(/"/g, '\\"')}"]`),
          );
          const el = links.find((a) => {
            const b = a.getBoundingClientRect();
            return b.width >= 8 && b.height >= 8;
          });
          if (!el) return false;
          el.click();
          return true;
        }, href);

        if (!clicked) {
          defects.push({
            checkId: 'nav-jump-target-lands',
            family: 'NAV' as const,
            viewport,
            message: `${href} has no clickable link with a real box`,
          });
          continue;
        }

        const settle = await waitForScrollSettle(page);
        if (!settle.settled) {
          defects.push({
            checkId: 'nav-jump-target-lands',
            family: 'NAV' as const,
            viewport,
            message: `${href} was still scrolling after ${settle.ms}ms at y=${settle.y}`,
          });
          continue;
        }

        const top = await page.evaluate((h: string) => {
          const el = document.getElementById(decodeURIComponent(h.slice(1)));
          return el ? Math.round(el.getBoundingClientRect().top) : NaN;
        }, href);

        if (Number.isNaN(top)) {
          defects.push({
            checkId: 'nav-jump-target-lands',
            family: 'NAV' as const,
            viewport,
            message: `${href} target vanished after navigation`,
          });
        } else if (top < lo || top > hi) {
          defects.push({
            checkId: 'nav-jump-target-lands',
            family: 'NAV' as const,
            viewport,
            message: `${href} landed at ${top}px; expected ${lo}-${hi}px (measured chrome ${chrome.height}px = ${chrome.parts
              .map((p) => `${p.tag}:${p.height}`)
              .join('+')})`,
          });
        }
      } catch (err) {
        // A thrown check drops the page from the scorecard silently. Never throw.
        defects.push({
          checkId: 'nav-jump-target-lands',
          family: 'NAV' as const,
          viewport,
          message: `${href} could not be tested: ${(err as Error).message.split('\n')[0]}`,
        });
      }
    }

    return { examined: targets.length, defects };
  },
});
