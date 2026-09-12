// scripts/board_thumbs.mjs <slug>
// Screenshots every Desktop artboard in docs/design/board-<slug>/ into
// docs/artifacts/boards/<slug>/thumbs/<section>--<candidate>--desktop.png (1440 wide, capped 900 tall).
// A candidate's `#` is spelled `+` in both names, exactly as board_canvas.py wrote it;
// build_page_board.py maps it back when it keys thumbs by (section, candidate).
import { chromium } from 'playwright';
import { readdirSync, mkdirSync } from 'node:fs';
import { resolve } from 'node:path';
const slug = process.argv[2];
if (!slug) { console.error('usage: node scripts/board_thumbs.mjs <slug>'); process.exit(1); }
const src = resolve('docs/design', `board-${slug}`);
const out = resolve('docs/artifacts/boards', slug, 'thumbs');
mkdirSync(out, { recursive: true });
const files = readdirSync(src).filter((f) => f.endsWith('--Desktop.dc.html'));
const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });
for (const f of files) {
  await page.goto('file://' + resolve(src, f));
  await page.waitForTimeout(400);                       // fonts + inline layout
  const [section, cand] = f.replace('--Desktop.dc.html', '').split('--');
  await page.locator('#root').screenshot({ path: resolve(out, `${section}--${cand}--desktop.png`) });
  console.log('thumb', section, cand);
}
await browser.close();
console.log(`${files.length} thumbs in docs/artifacts/boards/${slug}/thumbs/`);
