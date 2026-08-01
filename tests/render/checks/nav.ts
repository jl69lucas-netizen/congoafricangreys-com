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
              count: 1,
              message: `dead in-page anchor(s): ${r.dead.join(', ')}`,
            },
          ]
        : [],
    };
  },
});

/**
 * Names the ONE page-level thing most likely to be producing the landings we measured.
 * Returns null rather than guessing — a wrong root cause is worse than none, because it
 * sends the next person to edit a file that was never the problem.
 */
async function diagnoseLandingCause(page: Page, chromeHeight: number): Promise<string | null> {
  return page.evaluate((chromeH: number) => {
    const docH = document.documentElement.scrollHeight;
    const behavior = getComputedStyle(document.documentElement).scrollBehavior;

    const ids = new Set(
      Array.from(document.querySelectorAll<HTMLAnchorElement>('a[href^="#"]'))
        .map((a) => (a.getAttribute('href') || '').slice(1))
        .filter(Boolean)
        .map((h) => decodeURIComponent(h)),
    );
    let seen = 0;
    let short = 0;
    for (const id of ids) {
      const el = document.getElementById(id);
      if (!el) continue;
      seen++;
      if (parseFloat(getComputedStyle(el).scrollMarginTop || '0') < chromeH - 8) short++;
    }

    if (seen && short === seen) {
      return `every target's scroll-margin-top is under the ${chromeH}px of pinned chrome`;
    }
    if (short) {
      return `${short} of ${seen} targets have scroll-margin-top under the ${chromeH}px of pinned chrome`;
    }
    if (behavior === 'smooth' && docH > 8000) {
      return `html{scroll-behavior:smooth} on a ${docH}px document`;
    }
    return null;
  }, chromeHeight);
}

register({
  id: 'nav-jump-target-lands',
  family: 'NAV',
  severity: 'advisory',
  describe: 'clicking an in-page link must leave its target visible below the sticky chrome',
  minExamined: 2,
  async run(page: Page, viewport: number): Promise<CheckResult> {
    const chrome = await measureTopChrome(page);

    if (chrome.implausible) {
      return {
        examined: 0,
        defects: [
          {
            checkId: 'nav-jump-target-lands',
            family: 'NAV' as const,
            viewport,
            count: 1,
            message: `pinned chrome measures ${chrome.height}px, over 40% of the viewport — refusing to judge landings against a number that is probably wrong. Parts: ${JSON.stringify(chrome.parts)}`,
          },
        ],
      };
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

    // Three buckets, three rows. Never one row per anchor: NAV supplied 81% of the
    // first baseline's headline number by counting granularity alone, which made the
    // family totals incomparable and pointed the next-action list at the wrong family.
    //
    // `unsettled` is partitioned but NOT split into two rows, because the split it
    // encodes is a claim about WHOSE defect it is, not a second failure mode: a target
    // still travelling when the budget expired is probably OUR budget being short,
    // while one that never moved at all is the page's. Both belong in one row that
    // says which is which — splitting them would make "at most 3 rows" a lie the very
    // first time a page produced both.
    const missed: string[] = [];
    const unsettledMoving: string[] = [];
    const unsettledStuck: string[] = [];
    const untestable: string[] = [];

    for (const href of targets) {
      try {
        await resetScrollInstant(page);

        // Click the first link for this href that has a real box, in the page itself.
        // This triggers the browser's own fragment navigation — the behaviour a user
        // gets — without requiring viewport visibility.
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
          untestable.push(`${href} (no clickable box)`);
          continue;
        }

        const settle = await waitForScrollSettle(page);
        if (!settle.settled) {
          const detail = `${href} (gave up at ${settle.ms}ms, y=${settle.y}, last tick ${settle.lastDeltaPx}px)`;
          if (settle.lastDeltaPx > 0) unsettledMoving.push(detail);
          else unsettledStuck.push(detail);
          continue;
        }

        const top = await page.evaluate((h: string) => {
          const el = document.getElementById(decodeURIComponent(h.slice(1)));
          return el ? Math.round(el.getBoundingClientRect().top) : NaN;
        }, href);

        if (Number.isNaN(top)) {
          untestable.push(`${href} (target vanished after navigation)`);
        } else if (top < lo || top > hi) {
          missed.push(`${href}@${top}px`);
        }
      } catch (err) {
        // A thrown check drops the page from the scorecard silently. Never throw.
        untestable.push(`${href} (${(err as Error).message.split('\n')[0]})`);
      }
    }

    const defects: Defect[] = [];
    const chromeDesc = `${chrome.height}px = ${chrome.parts.map((p) => `${p.tag}:${p.height}`).join('+')}`;

    if (missed.length) {
      const cause = await diagnoseLandingCause(page, chrome.height);
      defects.push({
        checkId: 'nav-jump-target-lands',
        family: 'NAV' as const,
        viewport,
        count: missed.length,
        message:
          `${missed.length} of ${targets.length} in-page links land outside ${lo}-${hi}px ` +
          `(measured chrome ${chromeDesc})` +
          (cause ? ` — ROOT CAUSE: ${cause}` : ' — no single page-level cause identified') +
          `; first: ${missed.slice(0, 5).join(', ')}`,
      });
    }

    const unsettled = unsettledMoving.length + unsettledStuck.length;
    if (unsettled) {
      defects.push({
        checkId: 'nav-jump-target-lands',
        family: 'NAV' as const,
        viewport,
        count: unsettled,
        message:
          `${unsettled} of ${targets.length} links never stopped scrolling inside the harness's own settle budget` +
          (unsettledMoving.length
            ? ` — ${unsettledMoving.length} were STILL MOVING when it expired, which is PROBABLY A BUDGET DEFECT, NOT A PAGE DEFECT; raise maxMs before touching the page (first: ${unsettledMoving.slice(0, 3).join(', ')})`
            : '') +
          (unsettledStuck.length
            ? ` — ${unsettledStuck.length} never moved at all, so the click produced no scroll, which is a page defect (first: ${unsettledStuck.slice(0, 3).join(', ')})`
            : ''),
      });
    }

    if (untestable.length) {
      defects.push({
        checkId: 'nav-jump-target-lands',
        family: 'NAV' as const,
        viewport,
        count: untestable.length,
        message: `${untestable.length} of ${targets.length} links could not be tested; first: ${untestable.slice(0, 3).join(', ')}`,
      });
    }

    return { examined: targets.length, defects };
  },
});
