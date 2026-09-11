#!/usr/bin/env node
// scripts/form_title_gap_probe.mjs — added 2026-09-11 after the breeder saw group titles sitting
// flush against the pills above them on /available/ and the bird pages (Tailwind v4 space-y-4 is
// :where()-scoped margin-block-end, so an m-0 utility on a <fieldset> silently cancels it).
// Run after: python3 scripts/form_contract_audit.py --json /tmp/cag-forms.json
//   node scripts/form_title_gap_probe.mjs /tmp/cag-forms.json      (exit 1 on any title < 12px)
// Title-gap probe: every group title (legend, or a label that is not a radio/card option) must sit
// >= MIN px below the bottom of the nearest preceding control/option in the same form.
import { chromium } from '@playwright/test';
import { readFileSync } from 'node:fs';
import { spawn } from 'node:child_process';
const MIN = 12, PORT = 4325;
const rows = JSON.parse(readFileSync(process.argv[2], 'utf8')).filter(r => r.kind === 'inquiry');
const srv = spawn('python3', ['-m', 'http.server', String(PORT), '--directory', 'dist'], { stdio: 'ignore' });
await new Promise(r => setTimeout(r, 800));
const b = await chromium.launch();
const worst = {};
try {
  for (const w of [375, 768, 1280]) {
    const p = await b.newPage({ viewport: { width: w, height: 900 } });
    for (const r of rows) {
      await p.goto(`http://127.0.0.1:${PORT}/${r.slug === 'index' || r.slug === '' ? '' : r.slug + '/'}`, { waitUntil: 'load' });
      const res = await p.evaluate(({ n, MIN }) => {
        const f = document.forms[n - 1]; if (!f) return { err: 'no form' };
        const vis = e => { const s = getComputedStyle(e); const b = e.getBoundingClientRect(); return s.display !== 'none' && s.visibility !== 'hidden' && b.height > 0 && b.width > 2; };
        const isOption = l => !!l.querySelector('input[type=radio],input[type=checkbox]');
        const titles = [...f.querySelectorAll('legend, label')].filter(e => vis(e) && !(e.tagName === 'LABEL' && (isOption(e) || e.closest('legend'))));
        // An option's box is its pill/card LABEL, never the radio circle inside it: the circle sits
        // ~12px above the pill's bottom edge, so measuring it hides a 0px title-to-pill collision.
        const ctrls = [...f.querySelectorAll('input:not([type=hidden]):not([name=_gotcha]), select, textarea, label')]
          .filter(e => vis(e) && (e.tagName !== 'LABEL' || isOption(e)))
          .filter(e => !(e.tagName === 'INPUT' && e.closest('label') && isOption(e.closest('label'))));
        const out = [];
        for (const t of titles) {
          const tt = t.getBoundingClientRect().top;
          // nearest preceding control in document order that is NOT inside this title
          let prev = null;
          // same column only: a control beside the title in a 2-col row is not "above" it
          const tb = t.getBoundingClientRect();
          for (const c of ctrls) {
            if (t.contains(c) || c.contains(t)) continue;
            if (!(c.compareDocumentPosition(t) & Node.DOCUMENT_POSITION_FOLLOWING)) continue;
            const cb = c.getBoundingClientRect();
            if (cb.right <= tb.left + 1 || cb.left >= tb.right - 1) continue;
            if (cb.bottom > tb.top + tb.height) continue;
            prev = c;
          }
          if (!prev) continue;
          const gap = Math.round(tt - prev.getBoundingClientRect().bottom);
          if (gap < MIN) out.push(`${gap}px  "${t.textContent.trim().replace(/\s+/g, ' ').slice(0, 48)}"`);
        }
        return { out };
      }, { n: r.n, MIN });
      const key = `${r.slug} form#${r.n}`;
      if (res.err) { console.log(`ERR ${key} @${w} ${res.err}`); continue; }
      if (res.out.length) { worst[key] = worst[key] || {}; worst[key][w] = res.out; }
    }
    await p.close();
  }
} finally { await b.close(); srv.kill(); }
const keys = Object.keys(worst);
for (const k of keys) { console.log(`TIGHT ${k}`); for (const [w, list] of Object.entries(worst[k])) console.log(`   @${w}: ${list.length} → ${list.slice(0, 4).join(' | ')}`); }
console.log(`\n${rows.length} inquiry forms probed x 3 widths; ${keys.length} form(s) with a title < ${MIN}px below the control above it`);
process.exit(keys.length ? 1 : 0);
