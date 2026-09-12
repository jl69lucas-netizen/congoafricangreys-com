// scripts/board_thumbs.mjs <slug>
// Screenshots every Desktop artboard in docs/design/board-<slug>/ into
// docs/artifacts/boards/<slug>/thumbs/<section>--<candidate>--desktop.png (1440 wide, capped 900 tall).
// A candidate's `#` is spelled `+` in both names, exactly as board_canvas.py wrote it;
// build_page_board.py maps it back when it keys thumbs by (section, candidate).
import { chromium } from 'playwright';
import { readdirSync, mkdirSync } from 'node:fs';
import { dirname, resolve } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

const slug = process.argv[2];
if (!slug) { console.error('usage: node scripts/board_thumbs.mjs <slug>'); process.exit(1); }
// Paths resolve from THIS file, not from the shell's cwd: the canvas and the thumbs live
// at fixed places in the repo, and a run from any other directory must still find them.
const root = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const src = resolve(root, 'docs/design', `board-${slug}`);
const out = resolve(root, 'docs/artifacts/boards', slug, 'thumbs');
mkdirSync(out, { recursive: true });
const files = readdirSync(src).filter((f) => f.endsWith('--Desktop.dc.html')).sort();
const browser = await chromium.launch();
try {
  const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });
  for (const f of files) {
    await page.goto(pathToFileURL(resolve(src, f)).href);
    await page.waitForTimeout(400);                     // fonts + inline layout
    const [section, cand] = f.replace('--Desktop.dc.html', '').split('--');
    await page.locator('#root').screenshot({ path: resolve(out, `${section}--${cand}--desktop.png`) });
    console.log('thumb', section, cand);
  }
} finally {
  await browser.close();                                // a thrown artboard must not leak a browser
}
console.log(`${files.length} thumbs in docs/artifacts/boards/${slug}/thumbs/`);
