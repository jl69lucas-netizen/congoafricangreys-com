#!/usr/bin/env node
/**
 * Give the inline `/emoji/cag-*-64.webp` icons an `x`-descriptor srcset.
 *
 * These are the images the `w`-descriptor work could not fix, and the backlog already said
 * why: the master is 60px and it paints anywhere from 14px to 30px depending on which
 * component renders it, so `img-srcset-within-2x` sees up to 4.29x. Shrinking the master
 * would satisfy the metric and soften the icon on every retina screen — the trade that got
 * the first srcset attempt reverted. An `x` descriptor is the correct instrument: it hands
 * DPR-1 screens a small file and keeps the 60px master for DPR 2.
 *
 * One 1x width cannot serve every call site — 32px into a 14px box is 2.29x (fails) and
 * 24px into a 30px box is 0.8x (blur). So the 1x width is chosen PER TAG from the size the
 * tag itself declares, via width= or an inline style.
 *
 *   node scripts/image_srcset_emoji.mjs [--write]
 */
import { readFileSync, writeFileSync } from 'node:fs';
import { execSync } from 'node:child_process';

const write = process.argv.includes('--write');
const files = execSync(`grep -rl 'emoji/cag-[a-z]*-64\\.webp' src --include='*.astro' || true`, {
  encoding: 'utf8',
})
  .trim()
  .split('\n')
  .filter(Boolean);

/** Declared painted size of this tag, in px, or null when it does not say. */
function declaredSize(tag) {
  const w = tag.match(/\bwidth\s*=\s*"(\d+(?:\.\d+)?)"/);
  if (w) return parseFloat(w[1]);
  const rem = tag.match(/width\s*:\s*([\d.]+)rem/);
  if (rem) return parseFloat(rem[1]) * 16;
  const px = tag.match(/width\s*:\s*([\d.]+)px/);
  if (px) return parseFloat(px[1]);
  return null;
}

let patched = 0;
let skipped = 0;
const touched = [];

for (const file of files) {
  const src = readFileSync(file, 'utf8');
  let out = '';
  let last = 0;
  const re = /<img\b[^>]*?src="\/emoji\/(cag-(?:congo|timneh))-64\.webp"[^>]*>/g;
  let m;
  while ((m = re.exec(src))) {
    const tag = m[0];
    if (/\bsrcset\s*=/.test(tag)) {
      skipped++;
      continue;
    }
    const stem = m[1];
    const size = declaredSize(tag);
    // 24px covers boxes up to ~16px (24/14 = 1.71x); 32px covers the rest and never
    // under-serves the 30px footer mark (32/30 = 1.07x).
    const oneX = size != null && size <= 16 ? 24 : 32;
    const attr = ` srcset="/emoji/${stem}-${oneX}.webp 1x, /emoji/${stem}-64.webp 2x"`;
    const close = tag.endsWith('/>') ? 2 : 1;
    const rebuilt = tag.slice(0, tag.length - close) + attr + (close === 2 ? ' />' : '>');
    out += src.slice(last, m.index) + rebuilt;
    last = m.index + tag.length;
    patched++;
  }
  if (last) {
    out += src.slice(last);
    if (write) writeFileSync(file, out);
    touched.push(file);
  }
}

console.log(`emoji tags patched: ${patched} across ${touched.length} file(s)`);
console.log(`  already had a srcset: ${skipped}`);
if (!write) console.log('\n(dry run — pass --write)');
