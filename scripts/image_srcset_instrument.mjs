#!/usr/bin/env node
/**
 * Stamp every source `<img>` with the identity of the tag that wrote it, so the built page
 * says which source tag produced each rendered image instead of us inferring it.
 *
 *   node scripts/image_srcset_instrument.mjs --on     # add data-cagtag="file@offset"
 *   node scripts/image_srcset_instrument.mjs --off    # remove every data-cagtag
 *
 * WHY THIS EXISTS. Occurrence -> source-tag is the whole difficulty of the srcset work:
 * several images render from data arrays inside shared components, so one tag emits many
 * occurrences and one page renders many tags for the same file. Inferring the mapping from
 * the src path needs a stack of heuristics — const resolution, template wildcards, import
 * graphs, class matching, document-order pairing — and each one is a guess that fails
 * silently. A guess that mislabels a tag writes a `sizes` measured from one box onto an
 * image that paints at another, which is the blur bug that got the last attempt reverted,
 * arriving by a different route.
 *
 * The build already knows the answer. Stamping the tag, building, and reading the stamp
 * back turns the mapping into a measurement. Run --on, build, read dist, run --off.
 *
 * The stamp is removed by --off before any real edit is written, and `git diff` after a
 * round trip must be empty — the acceptance check for this script is that it is invisible.
 */
import { readFileSync, writeFileSync } from 'node:fs';
import { execSync } from 'node:child_process';

const mode = process.argv.includes('--off') ? 'off' : process.argv.includes('--on') ? 'on' : null;
if (!mode) {
  console.error('usage: image_srcset_instrument.mjs --on | --off');
  process.exit(2);
}

const files = execSync(`find src -type f \\( -name '*.astro' -o -name '*.html' \\) | sort`, {
  encoding: 'utf8',
})
  .trim()
  .split('\n')
  .filter(Boolean);

let touched = 0;
let stamps = 0;

for (const f of files) {
  const src = readFileSync(f, 'utf8');
  let out;

  if (mode === 'off') {
    out = src.replace(/\s+data-cagtag="[^"]*"/g, '');
  } else {
    // Walk tags from the END so earlier offsets stay valid as we splice, and so the offset
    // recorded in each stamp is the offset in the ORIGINAL file — the same number the map
    // and apply scripts use to identify the tag.
    const positions = [];
    const re = /<img\b/gi;
    let m;
    while ((m = re.exec(src))) positions.push(m.index);

    out = src;
    for (const start of [...positions].reverse()) {
      // Skip a tag that is already stamped, so --on is idempotent.
      const head = out.slice(start, start + 400);
      if (/^<img\b[^>]*data-cagtag=/.test(head)) continue;
      out = out.slice(0, start + 4) + ` data-cagtag="${f}@${start}"` + out.slice(start + 4);
      stamps++;
    }
  }

  if (out !== src) {
    writeFileSync(f, out);
    touched++;
  }
}

console.log(`${mode}: ${touched} file(s) rewritten${mode === 'on' ? `, ${stamps} tag(s) stamped` : ''}`);
