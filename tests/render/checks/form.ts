import { register, type CheckResult, type CheckContext, type Defect } from '../lib/registry.js';
import type { Page } from '@playwright/test';

/**
 * FORM family. Added 2026-09-11 after the breeder found inquiries "still going to the MFS
 * email": 14 forms carried data-netlify with no action (a Netlify handler that does not
 * exist on Cloudflare Pages — the browser POSTed to the page itself and the mail vanished),
 * two POSTed to /thank-you/ (no such page), one GET to /contact-us/, one to the retired
 * xpqoeazq ID. No invariant covered any of it, so per skills/cag-learning-loop.md §4 this
 * check enters ADVISORY with a fixture that went red first. It is judged in the browser,
 * not from source: `checkValidity()` on the untouched form is the one honest test that
 * `required` is live on every control the contract names.
 *
 * `examined === 0` is a legitimate, silent state on `location` and `hub` page types (those
 * clusters carry no inquiry form by design) AND on any slug in `LOCATION_CLUSTER` — two
 * `for-sale`-typed slugs (`buy-african-grey-parrots-with-shipping`,
 * `african-grey-parrots-for-sale-near-me`) carry only the search form and are slug-exempt
 * by the plan even though their `pageType` says `for-sale`. On every other page, zero forms
 * examined is itself the defect (the page lost its form, or the form is a `/search/` form
 * in disguise), and this check reports it as one row instead of passing silently — a check
 * that returns clean on zero is indistinguishable from a check that never ran.
 *
 * `fieldChecksSkipped()` exempts `buy-*` slugs from the seven-field contract only because,
 * as of this writing, no `buy-*` page carries an inquiry form at all (plan §0 groups them
 * with the location cluster for that reason). That is a fact about today's page inventory,
 * not a permanent property of the slug pattern — if a `buy-*` page ever grows a real
 * inquiry form, this exemption must be revisited or it will silently stop checking it.
 */
const FORM_ENDPOINT = 'https://formspree.io/f/xrejpnvn';
const LOCATION_CLUSTER = /^(african-grey-parrots?-for-sale-|buy-)/;
/** Same contracts as scripts/form_contract_audit.py `contract_keys()`. The homepage and
 *  /contact-us/ carry the full contract since the breeder lifted their opt-out (2026-09-11,
 *  brief Flag 1); blog posts carry the short one (confirm number, confirm email, resale,
 *  surrender — breeder, 2026-09-11). */
export function fieldChecksSkipped(slug: string): boolean {
  return LOCATION_CLUSTER.test(slug);
}
export function contractFor(slug: string): 'full' | 'short' | 'none' {
  if (fieldChecksSkipped(slug)) return 'none';
  return slug.startsWith('blog/') ? 'short' : 'full';
}
export function formExpected(slug: string, pageType: string): boolean {
  return pageType !== 'location' && pageType !== 'hub' && !LOCATION_CLUSTER.test(slug);
}

register({
  id: 'form-inquiry-contract',
  family: 'FORM',
  severity: 'advisory',
  describe:
    'every non-search form POSTs to the one Formspree endpoint; every in-scope inquiry form carries the seven screening fields, each required, and refuses to submit empty',
  // known_good carries one inquiry form + one newsletter (the search form is skipped) → 2.
  minExamined: 2,
  async run(page: Page, viewport: number, ctx: CheckContext): Promise<CheckResult> {
    const r = await page.evaluate(
      ({ endpoint, contract }) => {
        const ALL: [string, RegExp][] = [
          ['confirm number', /^(phone|cell|mobile)[_-]?confirm$/],
          ['confirm email', /^email[_-]?confirm$/],
          ['resale screening', /^resale_screening$/],
          ['surrender history', /^surrender_history$/],
          ['experience', /^experience$/],
          ['delivery', /^delivery(_method)?$/],
          ['message', /^(message|msg)$/],
        ];
        const SHORT = ['confirm number', 'confirm email', 'resale screening', 'surrender history'];
        const KEYS = contract === 'short' ? ALL.filter(([n]) => SHORT.includes(n)) : ALL;
        const fieldsApply = contract !== 'none';
        const wrongEndpoint: string[] = [];
        const missing: string[] = [];
        let missingCount = 0;
        const submitsEmpty: string[] = [];
        let examined = 0;
        Array.from(document.querySelectorAll('form')).forEach((f, i) => {
          const action = f.getAttribute('action') || '';
          if (action.startsWith('/search')) return;
          examined++;
          const subject = f.querySelector('input[name="_subject"]') as HTMLInputElement | null;
          const label = `form#${i + 1}(${
            f.getAttribute('id') ||
            f.getAttribute('aria-label') ||
            subject?.value ||
            f.getAttribute('name') ||
            f.className.split(' ')[0] ||
            'unnamed'
          })`;
          const netlify =
            f.hasAttribute('data-netlify') ||
            f.hasAttribute('netlify-honeypot') ||
            !!f.querySelector('[name="form-name"],[name="bot-field"]');
          if (action !== endpoint || netlify || (f.getAttribute('method') || 'get').toLowerCase() !== 'post') {
            wrongEndpoint.push(`${label} action="${action || '(none)'}"${netlify ? ' +netlify' : ''}`);
          }
          // Same classification as scripts/form_contract_audit.py: a NEWSLETTER is a form whose
          // visible controls are exactly one email box; anything else is an inquiry form. Two
          // gates must agree on what an inquiry form is (reference_same_input_different_verdict).
          const controls = Array.from(f.querySelectorAll('input,select,textarea')) as HTMLInputElement[];
          const visible = controls.filter((c) => c.type !== 'hidden' && c.name !== '_gotcha');
          const isInquiry = !(visible.length === 1 && visible[0].type === 'email');
          if (!isInquiry) {
            // Same parity check as form_contract_audit.py: a newsletter's one real control
            // must carry a `name`, or Formspree receives an unlabeled value and drops it.
            if (!visible[0].name) {
              wrongEndpoint.push(`${label}: email input has no name — Formspree receives nothing`);
            }
            return;
          }
          if (!fieldsApply) return;
          const formIssues: string[] = [];
          for (const [name, rx] of KEYS) {
            const hits = controls.filter((c) => rx.test(c.name));
            if (!hits.length || !hits.some((c) => c.required)) formIssues.push(name);
          }
          if (formIssues.length) {
            missingCount += formIssues.length;
            missing.push(`${label}: ${formIssues.length} missing/optional (${formIssues.join(', ')})`);
          }
          if (f.checkValidity()) submitsEmpty.push(label);
        });
        return { examined, wrongEndpoint, missing, missingCount, submitsEmpty };
      },
      { endpoint: FORM_ENDPOINT, contract: contractFor(ctx.slug) },
    );
    const defects: Defect[] = [];
    if (r.examined === 0 && formExpected(ctx.slug, ctx.pageType)) {
      defects.push({
        checkId: 'form-inquiry-contract', family: 'FORM' as const, viewport, count: 1,
        message: `no non-search form on a ${ctx.pageType} page — nothing to judge`,
      });
    }
    if (r.wrongEndpoint.length) {
      defects.push({ checkId: 'form-inquiry-contract', family: 'FORM' as const, viewport, count: r.wrongEndpoint.length,
        message: `not posting to ${FORM_ENDPOINT}: ${r.wrongEndpoint.slice(0, 4).join(' | ')}` });
    }
    if (r.missing.length) {
      defects.push({ checkId: 'form-inquiry-contract', family: 'FORM' as const, viewport, count: r.missingCount,
        message: `screening fields: ${r.missing.slice(0, 6).join(' | ')}` });
    }
    if (r.submitsEmpty.length) {
      defects.push({ checkId: 'form-inquiry-contract', family: 'FORM' as const, viewport, count: r.submitsEmpty.length,
        message: `checkValidity() is true on the untouched form (no live required constraint, or a control is pre-filled/pre-checked): ${r.submitsEmpty.join(' | ')}` });
    }
    return { examined: r.examined, defects };
  },
});
