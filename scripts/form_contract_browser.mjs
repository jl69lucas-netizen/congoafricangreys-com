#!/usr/bin/env node
// scripts/form_contract_browser.mjs
// Proof in a real browser, for EVERY in-scope inquiry form (not just the 19 harness targets):
//   1. the untouched form refuses to submit (checkValidity() === false)
//   2. once every control is filled with a valid value it accepts (checkValidity() === true)
//   3. a screenshot of the form at 375 and 1280 lands in sessions/2026-09-11-form-screens/
// Never clicks submit — that would send real mail to the breeder.
// Input: the --json output of scripts/form_contract_audit.py (run it first).
import { chromium } from '@playwright/test';
import { readFileSync, mkdirSync } from 'node:fs';
import { spawn } from 'node:child_process';

const ROWS = JSON.parse(readFileSync(process.argv[2] ?? '/tmp/cag-forms.json', 'utf8')).filter((r) => r.in_scope);
const OUT = 'sessions/2026-09-11-form-screens';
const PORT = 4323;
mkdirSync(OUT, { recursive: true });

const server = spawn('python3', ['-m', 'http.server', String(PORT), '--directory', 'dist'], { stdio: 'ignore' });
await new Promise((r) => setTimeout(r, 800));

const browser = await chromium.launch();
const failures = [];
let checked = 0;
try {
  for (const vp of [375, 1280]) {
    const page = await browser.newPage({ viewport: { width: vp, height: vp === 375 ? 812 : 800 } });
    for (const row of ROWS) {
      const url = `http://127.0.0.1:${PORT}/${row.slug === 'index' ? '' : row.slug + '/'}`;
      await page.goto(url, { waitUntil: 'load' });
      // row.n is the audit's 1-based index over EVERY <form> in document order (the header's
      // search form included — the audit numbers all forms and only skips judging search).
      const target = page.locator('form').nth(row.n - 1);
      const emptyValid = await target.evaluate((f) => f.checkValidity());
      await target.evaluate((f) => {
        const seen = new Set();
        for (const c of f.querySelectorAll('input,select,textarea')) {
          if (c.type === 'hidden' || c.name === '_gotcha') continue;
          if (c.type === 'radio' || c.type === 'checkbox') { if (!seen.has(c.name)) { c.checked = true; seen.add(c.name); } continue; }
          if (c.tagName === 'SELECT') { c.selectedIndex = [...c.options].findIndex((o) => o.value !== ''); continue; }
          c.value = c.type === 'email' ? 'test@example.com' : c.type === 'tel' ? '5550001111' : 'test';
        }
      });
      const filledValid = await target.evaluate((f) => f.checkValidity());
      checked++;
      const ok = emptyValid === false && filledValid === true;
      if (!ok) failures.push(`${row.slug} form#${row.n} @${vp}: empty=${emptyValid} filled=${filledValid}`);
      await target.evaluate((f) => f.reset());
      await target.screenshot({ path: `${OUT}/${row.slug.replace(/\//g, '__')}__form${row.n}__${vp}.png` });
      console.log(`${ok ? 'ok  ' : 'FAIL'} ${row.slug} form#${row.n} @${vp} fields=${row.fields.length}`);
    }
    await page.close();
  }
} finally {
  await browser.close();
  server.kill();
}
console.log(`\nchecked ${checked} form-viewports across ${ROWS.length} in-scope forms; ${failures.length} failure(s)`);
for (const f of failures) console.log('  ' + f);
process.exit(failures.length ? 1 : 0);
