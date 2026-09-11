import { register, type CheckResult, type CheckContext } from '../lib/registry.js';
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
 */
export const FORM_ENDPOINT = 'https://formspree.io/f/xrejpnvn';
const FIELD_CHECKS_SKIP = (slug: string) =>
  slug === 'index' || slug === 'contact-us' || /^(african-grey-parrots?-for-sale-|buy-)/.test(slug);

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
      ({ endpoint, fieldsApply }) => {
        const KEYS: [string, RegExp][] = [
          ['confirm number', /^(phone|cell|mobile)[_-]?confirm$/],
          ['confirm email', /^email[_-]?confirm$/],
          ['resale screening', /^resale_screening$/],
          ['surrender history', /^surrender_history$/],
          ['experience', /^experience$/],
          ['delivery', /^delivery(_method)?$/],
          ['message', /^(message|msg)$/],
        ];
        const wrongEndpoint: string[] = [];
        const missing: string[] = [];
        const submitsEmpty: string[] = [];
        let examined = 0;
        Array.from(document.querySelectorAll('form')).forEach((f, i) => {
          const action = f.getAttribute('action') || '';
          if (action.startsWith('/search')) return;
          examined++;
          const label = `form#${i + 1}(${f.getAttribute('name') || f.className.split(' ')[0] || 'unnamed'})`;
          const netlify =
            f.hasAttribute('data-netlify') || !!f.querySelector('[name="form-name"],[name="bot-field"]');
          if (action !== endpoint || netlify || (f.getAttribute('method') || 'get').toLowerCase() !== 'post') {
            wrongEndpoint.push(`${label} action="${action || '(none)'}"${netlify ? ' +netlify' : ''}`);
          }
          // Same classification as scripts/form_contract_audit.py: a NEWSLETTER is a form whose
          // visible controls are exactly one email box; anything else is an inquiry form. Two
          // gates must agree on what an inquiry form is (reference_same_input_different_verdict).
          const controls = Array.from(f.querySelectorAll('input,select,textarea')) as HTMLInputElement[];
          const visible = controls.filter((c) => c.type !== 'hidden' && c.name !== '_gotcha');
          const isInquiry = !(visible.length === 1 && visible[0].type === 'email');
          if (!isInquiry || !fieldsApply) return;
          for (const [name, rx] of KEYS) {
            const hits = controls.filter((c) => rx.test(c.name));
            if (!hits.length) missing.push(`${label}: ${name} absent`);
            else if (!hits.some((c) => c.required)) missing.push(`${label}: ${name} not required`);
          }
          if (f.checkValidity()) submitsEmpty.push(label);
        });
        return { examined, wrongEndpoint, missing, submitsEmpty };
      },
      { endpoint: FORM_ENDPOINT, fieldsApply: !FIELD_CHECKS_SKIP(ctx.slug) },
    );
    const defects = [];
    if (r.wrongEndpoint.length) {
      defects.push({ checkId: 'form-inquiry-contract', family: 'FORM' as const, viewport, count: r.wrongEndpoint.length,
        message: `not posting to ${FORM_ENDPOINT}: ${r.wrongEndpoint.slice(0, 4).join(' | ')}` });
    }
    if (r.missing.length) {
      defects.push({ checkId: 'form-inquiry-contract', family: 'FORM' as const, viewport, count: r.missing.length,
        message: `screening fields: ${r.missing.slice(0, 6).join(' | ')}` });
    }
    if (r.submitsEmpty.length) {
      defects.push({ checkId: 'form-inquiry-contract', family: 'FORM' as const, viewport, count: r.submitsEmpty.length,
        message: `checkValidity() is true on the untouched form (required is not live): ${r.submitsEmpty.join(' | ')}` });
    }
    return { examined: r.examined, defects };
  },
});
