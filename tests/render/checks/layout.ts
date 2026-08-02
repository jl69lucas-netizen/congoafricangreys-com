import { register, type CheckResult } from '../lib/registry.js';
import type { Page } from '@playwright/test';

register({
  id: 'layout-no-horizontal-overflow',
  family: 'LAYOUT',
  severity: 'blocking',
  describe: 'the document must not scroll sideways at any viewport',
  // This check judges exactly ONE unit: the document's own overflow measurement.
  // The per-element walk below runs only to NAME offenders, never to decide.
  // That keeps it free of false positives from intentionally-translated
  // decorative elements — but it also means the fixture pair is this check's
  // only real protection, so never weaken the fixtures.
  minExamined: 1,
  async run(page: Page, viewport: number): Promise<CheckResult> {
    const r = await page.evaluate(() => {
      const de = document.documentElement;
      const limit = de.clientWidth;
      const overflow = de.scrollWidth - limit;
      const offenders: string[] = [];
      if (overflow > 1) {
        for (const el of Array.from(document.body.querySelectorAll<HTMLElement>('*'))) {
          if (getComputedStyle(el).position === 'fixed') continue;
          const box = el.getBoundingClientRect();
          if (box.width === 0 || box.height === 0) continue;
          if (box.right > limit + 1) {
            const cls =
              typeof el.className === 'string' && el.className.trim()
                ? '.' + el.className.trim().split(/\s+/).slice(0, 3).join('.')
                : '';
            offenders.push(`${el.tagName.toLowerCase()}${cls}@${Math.round(box.right)}px`);
          }
        }
      }
      return { overflow, offenders: offenders.slice(0, 8) };
    });

    return {
      examined: 1,
      defects:
        r.overflow > 1
          ? [
              {
                checkId: 'layout-no-horizontal-overflow',
                family: 'LAYOUT' as const,
                viewport,
                count: 1,
                message: `document overflows by ${r.overflow}px — offenders: ${
                  r.offenders.join(' | ') || 'none isolated'
                }`,
              },
            ]
          : [],
    };
  },
});

register({
  id: 'layout-min-font-size',
  family: 'LAYOUT',
  severity: 'blocking',
  describe: 'no visible text may render below 12.5px',
  // 12.5 was questioned on 2026-08-01: 88 declarations of `.78rem` compute to 12.48px
  // and fail by 0.02px, which reads like a rounding artifact, and the backlog advised
  // exempting them. It is not an artifact — `.78rem` is the single most-used small size
  // in this codebase (88 declarations across 17 files), so moving the threshold to 12.4
  // would retire the check's LARGEST cohort permanently and leave it unable to speak
  // about that band again. The threshold stayed; the codebase moved to `--fs-micro`
  // (0.79rem = 12.64px). Do not lower this number to make a sweep smaller.
  minExamined: 3,
  async run(page: Page, viewport: number): Promise<CheckResult> {
    const r = await page.evaluate(() => {
      const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
      let examined = 0;
      const bad: string[] = [];
      let node: Node | null;
      while ((node = walker.nextNode())) {
        const text = (node.textContent || '').trim();
        if (!text) continue;
        const el = node.parentElement;
        if (!el) continue;
        // getClientRects() is empty when ANY ancestor is display:none
        if (el.getClientRects().length === 0) continue;
        const cs = getComputedStyle(el);
        if (cs.visibility === 'hidden') continue;
        examined++;
        const size = parseFloat(cs.fontSize);
        if (size < 12.5) {
          bad.push(`${el.tagName.toLowerCase()} ${size}px "${text.slice(0, 30)}"`);
        }
      }
      return { examined, bad: bad.slice(0, 10), count: bad.length };
    });

    return {
      examined: r.examined,
      defects: r.count
        ? [
            {
              checkId: 'layout-min-font-size',
              family: 'LAYOUT' as const,
              viewport,
              count: r.count,
              message: `${r.count} text node(s) below 12.5px: ${r.bad.join(' | ')}`,
            },
          ]
        : [],
    };
  },
});

register({
  id: 'layout-tap-target-size',
  family: 'LAYOUT',
  severity: 'blocking',
  describe: 'every visible interactive control is at least 24x24px',
  minExamined: 2,
  async run(page: Page, viewport: number): Promise<CheckResult> {
    const r = await page.evaluate(() => {
      const sel = 'a[href], button, input:not([type=hidden]), select, textarea, [role=button]';
      const nodes = Array.from(document.querySelectorAll<HTMLElement>(sel));
      let examined = 0;
      const bad: string[] = [];
      // WCAG 2.2 SC 2.5.8 exempts two things this check used to flag on every page.
      // In the 2026-08-01 baseline all 45 LAYOUT rows named the skip link, and inline
      // prose links supplied the bulk of every message — so the report's "worst
      // family / next action" line was pointing at the standard's own exemptions.

      // (1) Visually-hidden controls in the 1px-clip pattern. The WCAG-MANDATED skip
      //     link is the canonical case: it has client rects and is not
      //     visibility:hidden, so a naive size test counts it and reports an
      //     accessibility feature as an accessibility defect.
      const isVisuallyHidden = (el: HTMLElement, box: DOMRect, cs: CSSStyleDeclaration) =>
        box.width <= 4 ||
        box.height <= 4 ||
        cs.clipPath === 'inset(50%)' ||
        /rect\(0(px)?[,\s]/.test(cs.clip) ||
        /(^|\s)(sr-only|visually-hidden|skip-link)(\s|$)/.test(el.className || '');

      // (2) A link sitting INSIDE a sentence. SC 2.5.8: "the target is in a sentence
      //     or its size is otherwise constrained by the line-height". Enlarging these
      //     would break the line box, so the standard does not ask for it. Detected
      //     structurally — an inline <a> whose parent carries text beyond the link
      //     itself — which distinguishes prose links from nav pills, where the parent
      //     <li> contains nothing but the link.
      const isInlineProseLink = (el: HTMLElement, cs: CSSStyleDeclaration) => {
        // EXACTLY `inline`, never `startsWith('inline')`: inline-block and inline-flex
        // are how every button-shaped control on this site is laid out, and matching
        // the prefix exempted the known_broken fixture's own 44x44 control because
        // <body> happened to contain other text. Caught by the fixture, not by review.
        if (el.tagName !== 'A' || cs.display !== 'inline') return false;
        const parent = el.parentElement;
        if (!parent) return false;
        const own = (el.textContent || '').trim().length;
        const around = (parent.textContent || '').trim().length;
        return around > own + 1;
      };

      // (3) A form control whose LABEL is the real target. A 13x13 checkbox inside a
      //     341x62 <label class="inq-checkbox-item"> is activated by clicking anywhere
      //     in the label, so the effective target is the label — measuring the raw input
      //     reports a defect that no user can experience. Measured on
      //     /african-grey-parrot-care-guide/ and /african-grey-parrot-health-guarantee/,
      //     where all 12 flagged controls were 13x13 radios and checkboxes wrapped in
      //     labels between 86x47 and 341x62. "Enlarge the checkbox" would have been a
      //     design change bought for zero accessibility gain.
      const effectiveBox = (el: HTMLElement): DOMRect => {
        if (!/^(INPUT|SELECT|TEXTAREA)$/.test(el.tagName)) return el.getBoundingClientRect();
        const wrapping = el.closest('label');
        const referencing = el.id
          ? document.querySelector<HTMLElement>(`label[for="${CSS.escape(el.id)}"]`)
          : null;
        const lab = wrapping || referencing;
        if (!lab || lab.getClientRects().length === 0) return el.getBoundingClientRect();
        const lb = lab.getBoundingClientRect();
        const own = el.getBoundingClientRect();
        return lb.width * lb.height > own.width * own.height ? lb : own;
      };

      const judged: { el: HTMLElement; box: DOMRect }[] = [];
      for (const el of nodes) {
        if (el.getClientRects().length === 0) continue;
        const cs = getComputedStyle(el);
        if (cs.visibility === 'hidden') continue;
        const box = effectiveBox(el);
        if (box.width === 0 || box.height === 0) continue;
        if (isVisuallyHidden(el, box, cs)) continue;
        if (isInlineProseLink(el, cs)) continue;
        examined++;
        judged.push({ el, box });
      }

      // (4) SC 2.5.8's SPACING exception, implemented rather than approximated. The
      //     standard does not require 24x24 outright: an undersized target passes if a
      //     24px-diameter circle centred on it intersects neither another target nor
      //     another undersized target's circle. A card-title link is small but sits
      //     alone in its card, and the standard says that is fine. Without this the
      //     check reports every isolated small control on the site as a defect — the
      //     third time this one check has flagged something WCAG itself exempts.
      const centre = (b: DOMRect) => ({ x: b.left + b.width / 2, y: b.top + b.height / 2 });
      const distToBox = (c: { x: number; y: number }, b: DOMRect) => {
        const dx = Math.max(b.left - c.x, 0, c.x - b.right);
        const dy = Math.max(b.top - c.y, 0, c.y - b.bottom);
        return Math.hypot(dx, dy);
      };
      const small = judged.filter((j) => j.box.width < 24 || j.box.height < 24);

      for (const t of small) {
        const c = centre(t.box);
        let intersects = false;
        for (const o of judged) {
          if (o.el === t.el) continue;
          if (o.el.contains(t.el) || t.el.contains(o.el)) continue; // nested control, one target
          const otherSmall = o.box.width < 24 || o.box.height < 24;
          if (otherSmall) {
            const oc = centre(o.box);
            if (Math.hypot(oc.x - c.x, oc.y - c.y) < 24) {
              intersects = true;
              break;
            }
          } else if (distToBox(c, o.box) < 12) {
            intersects = true;
            break;
          }
        }
        if (!intersects) continue; // isolated: SC 2.5.8 spacing exception
        const label = (t.el.textContent || t.el.getAttribute('aria-label') || '').trim().slice(0, 24);
        bad.push(
          `${t.el.tagName.toLowerCase()} ${Math.round(t.box.width)}x${Math.round(t.box.height)} "${label}"`,
        );
      }
      return { examined, bad: bad.slice(0, 10), count: bad.length };
    });

    return {
      examined: r.examined,
      defects: r.count
        ? [
            {
              checkId: 'layout-tap-target-size',
              family: 'LAYOUT' as const,
              viewport,
              count: r.count,
              message: `${r.count} control(s) under 24x24: ${r.bad.join(' | ')}`,
            },
          ]
        : [],
    };
  },
});
