import { register, type CheckResult } from '../lib/registry.js';
import type { Page } from '@playwright/test';

/**
 * The CSS family: markup and stylesheet drifting apart.
 *
 * `scripts/page_hardening_scan.py` already implements a static half of this
 * (`markup-css-drift`, `markup-css-orphan`, `component-color-loses-to-descendant`) by
 * regex-matching a page's `<style>` block against its own markup. The logic is ported
 * here rather than reinvented — including its hard-won exclusions — but the render
 * version is strictly stronger for three reasons, and those reasons are the whole point:
 *
 *   1. It reads the CSSOM, so a class styled in a GLOBAL sheet, a layout, or a component
 *      is seen. The static version has to concatenate a guessed list of files
 *      (`src/styles/*.css`, `src/layouts/*.astro`, `src/components/*.astro`) and misses
 *      anything outside it.
 *   2. It reads COMPUTED style, so "does this component's colour actually survive?" is
 *      measured rather than inferred from selector specificity. The static check is
 *      explicitly a WARN for that reason — "a go-and-measure-it signal, not a verdict".
 *      This one measures.
 *   3. It sees the rendered DOM, so "styled but never rendered" means never rendered,
 *      not "no literal class attribute matched my regex". The static harvester had to
 *      grow three separate parsers for Astro template-literal class expressions and
 *      still produced a false report on the baby page.
 */

register({
  id: 'css-class-resolves',
  family: 'CSS',
  severity: 'advisory',
  describe: 'every class on a rendered element is matched by at least one CSS rule',
  minExamined: 3,
  async run(page: Page, viewport: number): Promise<CheckResult> {
    const r = await page.evaluate(() => {
      // Collect every class token any rule in the document mentions. Reading the CSSOM
      // means a class styled in global.css, a layout, or another component counts —
      // which is the half the static scanner has to approximate by globbing files.
      const styled = new Set<string>();
      const collect = (rules: CSSRuleList) => {
        for (const rule of Array.from(rules)) {
          const anyRule = rule as CSSStyleRule & { cssRules?: CSSRuleList };
          if (anyRule.selectorText) {
            for (const m of anyRule.selectorText.matchAll(/\.(-?[_a-zA-Z][\w-]*)/g)) {
              styled.add(m[1]);
            }
          }
          if (anyRule.cssRules && anyRule.cssRules.length) collect(anyRule.cssRules); // @media, @supports, @layer
        }
      };
      for (const sheet of Array.from(document.styleSheets)) {
        try {
          collect(sheet.cssRules);
        } catch {
          // A cross-origin sheet throws on .cssRules. Reporting orphans while blind to
          // one sheet would invent defects, so refuse rather than guess.
          return { blocked: true, examined: 0, orphans: [] as string[], count: 0 };
        }
      }

      let examined = 0;
      const orphanCounts = new Map<string, number>();
      for (const el of Array.from(document.querySelectorAll<HTMLElement>('[class]'))) {
        for (const c of Array.from(el.classList)) {
          examined++;
          if (!styled.has(c)) orphanCounts.set(c, (orphanCounts.get(c) || 0) + 1);
        }
      }
      const orphans = [...orphanCounts.entries()]
        .sort((a, b) => b[1] - a[1])
        .map(([c, n]) => `${c} x${n}`);
      return {
        blocked: false,
        examined,
        orphans: orphans.slice(0, 12),
        count: orphanCounts.size,
      };
    });

    if (r.blocked) {
      return {
        examined: 0,
        defects: [
          {
            checkId: 'css-class-resolves',
            family: 'CSS' as const,
            viewport,
            count: 1,
            message:
              'a stylesheet could not be read (cross-origin); refusing to report orphans from a partial rule set',
          },
        ],
      };
    }

    return {
      examined: r.examined,
      defects: r.count
        ? [
            {
              checkId: 'css-class-resolves',
              family: 'CSS' as const,
              viewport,
              count: r.count,
              message: `${r.count} class(es) on rendered elements match no CSS rule: ${r.orphans.join(', ')}`,
            },
          ]
        : [],
    };
  },
});

register({
  id: 'css-no-dead-component-rule',
  family: 'CSS',
  severity: 'advisory',
  describe: 'every page-scoped CSS rule matches at least one element on the page',
  minExamined: 2,
  async run(page: Page, viewport: number): Promise<CheckResult> {
    const r = await page.evaluate(() => {
      // SCOPE: page-scoped rules only. Astro stamps a page's own <style> selectors with
      // `[data-astro-cid-xxxx]`, and only those can be judged here — a rule in global.css
      // that matches nothing on THIS page is styling some other page and is not dead.
      // Judging global rules per page is how a check reports several hundred defects
      // that are all the same non-defect.
      const dead: string[] = [];
      let examined = 0;
      const walk = (rules: CSSRuleList) => {
        for (const rule of Array.from(rules)) {
          // `rule.cssRules` is TRUTHY ON EVERY CSSStyleRule in current Chromium — nested
          // CSS gave plain style rules an empty CSSRuleList — so `if (rule.cssRules)
          // { recurse; continue; }` skips every rule in the document and the check
          // examines ZERO units while reporting a clean pass. Measured, not reasoned:
          // a probe over this file's own fixture returned hasSub:true for `body`.
          // Test `.length`, and handle the rule's own declarations before recursing.
          const anyRule = rule as CSSStyleRule & { cssRules?: CSSRuleList };
          if (anyRule.cssRules && anyRule.cssRules.length) walk(anyRule.cssRules);
          const sel = anyRule.selectorText;
          if (!sel || !sel.includes('data-astro-cid-')) continue;
          // Pseudo-elements and interaction states never match a static query.
          const testable = sel
            .split(',')
            .map((s) => s.trim())
            .filter(
              (s) =>
                s &&
                !/::/.test(s) &&
                !/:(hover|focus|focus-visible|focus-within|active|visited|target|checked|disabled|open|placeholder|first-line|first-letter|before|after|not\()/.test(
                  s,
                ),
            );
          if (!testable.length) continue;
          examined++;
          let matched = false;
          for (const s of testable) {
            try {
              if (document.querySelector(s)) {
                matched = true;
                break;
              }
            } catch {
              matched = true; // unparseable to querySelector — do not call it dead
              break;
            }
          }
          if (!matched) dead.push(sel.replace(/\[data-astro-cid-[^\]]*\]/g, '').slice(0, 60));
        }
      };
      for (const sheet of Array.from(document.styleSheets)) {
        try {
          walk(sheet.cssRules);
        } catch {
          /* cross-origin: contributes no page-scoped rules */
        }
      }
      return { examined, dead: dead.slice(0, 10), count: dead.length };
    });

    return {
      examined: r.examined,
      defects: r.count
        ? [
            {
              checkId: 'css-no-dead-component-rule',
              family: 'CSS' as const,
              viewport,
              count: r.count,
              message:
                `${r.count} page-scoped rule(s) match nothing on the page: ${r.dead.join(' | ')}` +
                ' — triage each: a variant this page does not ship, or a component the spec mandates and the page never rendered',
            },
          ]
        : [],
    };
  },
});

register({
  id: 'css-component-color-not-overridden',
  family: 'CSS',
  severity: 'advisory',
  describe: "a component's own colour is not silently overridden by a descendant rule",
  minExamined: 1,
  async run(page: Page, viewport: number): Promise<CheckResult> {
    const r = await page.evaluate(() => {
      // The mechanism, measured rather than inferred: `.ship-tier{color:#fff}` is
      // specificity (0,1,0); `.ship-c p{color:#5b524a}` is (0,1,1) and wins, so white
      // text intended on forest green shipped as dark grey at 1.19:1. Three instances on
      // one page, 2026-07-28.
      //
      // NARROW ON PURPOSE. Only a single-class component rule losing to a DESCENDANT
      // rule that does not name that class counts. A modifier (`.tag.is-active`) or a
      // media-query override is a deliberate change and must not be reported, or the
      // check drowns its own signal.
      const spec = (sel: string): [number, number, number] => {
        const ids = (sel.match(/#[\w-]+/g) || []).length;
        const cls =
          (sel.match(/\.[\w-]+/g) || []).length +
          (sel.match(/\[[^\]]*\]/g) || []).length +
          (sel.match(/:(?!:)[a-z-]+/g) || []).length;
        const tags = (sel.replace(/\[[^\]]*\]/g, '').match(/(^|[\s>+~])[a-z][\w-]*/g) || []).length;
        return [ids, cls, tags];
      };
      const gt = (a: number[], b: number[]) =>
        a[0] !== b[0] ? a[0] > b[0] : a[1] !== b[1] ? a[1] > b[1] : a[2] > b[2];

      type R = { sel: string; color: string; order: number };
      const colorRules: R[] = [];
      let order = 0;
      const walk = (rules: CSSRuleList) => {
        for (const rule of Array.from(rules)) {
          // `rule.cssRules` is TRUTHY ON EVERY CSSStyleRule in current Chromium — nested
          // CSS gave plain style rules an empty CSSRuleList — so `if (rule.cssRules)
          // { recurse; continue; }` skips every rule in the document and the check
          // examines ZERO units while reporting a clean pass. Measured, not reasoned:
          // a probe over this file's own fixture returned hasSub:true for `body`.
          // Test `.length`, and handle the rule's own declarations before recursing.
          const anyRule = rule as CSSStyleRule & { cssRules?: CSSRuleList };
          if (anyRule.cssRules && anyRule.cssRules.length) walk(anyRule.cssRules);
          const c = anyRule.style?.getPropertyValue('color');
          if (!c || !anyRule.selectorText) continue;
          for (const s of anyRule.selectorText.split(',')) {
            colorRules.push({ sel: s.trim(), color: c.trim(), order: order++ });
          }
        }
      };
      for (const sheet of Array.from(document.styleSheets)) {
        try {
          walk(sheet.cssRules);
        } catch {
          /* unreadable sheet */
        }
      }

      // A "component rule" is a bare single-class selector that sets colour.
      const componentRules = colorRules.filter((r) =>
        /^\.[-\w]+(\[data-astro-cid-[^\]]*\])?$/.test(r.sel),
      );
      let examined = 0;
      const bad: string[] = [];
      const seen = new Set<string>();

      for (const cr of componentRules) {
        const cls = (cr.sel.match(/^\.([-\w]+)/) as RegExpMatchArray)[1];
        let el: HTMLElement | null = null;
        try {
          el = document.querySelector<HTMLElement>(cr.sel);
        } catch {
          continue;
        }
        if (!el || el.getClientRects().length === 0) continue;
        examined++;
        const actual = getComputedStyle(el).color;

        // CHEAP TEST FIRST. Searching every colour rule for a winner is O(components x
        // rules) with an el.matches() per pair — on a real page that is hundreds of
        // thousands of selector matches, and the sibling SEM check has already shown
        // what a check that merely runs slowly does to a page run. Almost every
        // component's colour is fine, so resolve the declared value against the computed
        // one first and only pay for the winner search when they actually disagree.
        const probe = document.createElement('span');
        probe.style.color = cr.color;
        document.body.appendChild(probe);
        const declared = getComputedStyle(probe).color;
        probe.remove();
        if (declared === actual) continue;

        // They disagree — now find the rule that actually won for this element.
        let winner: R | null = null;
        for (const r of colorRules) {
          let matches = false;
          try {
            matches = el.matches(r.sel);
          } catch {
            continue;
          }
          if (!matches) continue;
          if (!winner) {
            winner = r;
            continue;
          }
          const a = spec(r.sel);
          const b = spec(winner.sel);
          if (gt(a, b) || (!gt(b, a) && r.order > winner.order)) winner = r;
        }
        if (!winner || winner.sel === cr.sel) continue;
        // Only a DESCENDANT rule that never names this component counts. Anything that
        // mentions the class is a deliberate modifier of it.
        if (winner.sel.includes(`.${cls}`)) continue;
        if (!/[\s>+~]/.test(winner.sel)) continue;
        const key = `${cls}<-${winner.sel}`;
        if (seen.has(key)) continue;
        seen.add(key);
        bad.push(`.${cls} wants ${cr.color} but "${winner.sel}" wins -> ${actual}`);
      }
      return { examined, bad: bad.slice(0, 6), count: bad.length };
    });

    return {
      examined: r.examined,
      defects: r.count
        ? [
            {
              checkId: 'css-component-color-not-overridden',
              family: 'CSS' as const,
              viewport,
              count: r.count,
              message: `${r.count} component colour(s) lost to a descendant rule: ${r.bad.join(' | ')} — qualify the component rule (\`.wrap p.tag{...}\`)`,
            },
          ]
        : [],
    };
  },
});
