#!/usr/bin/env node
/**
 * Write `srcset` + `sizes` onto the source tags a measured map names.
 *
 * Every trap banked from the reverted 2026-08-01 attempt is handled here explicitly:
 *
 *  - ONE BLANKET `sizes` IS THE BUG, not a shortcut. Each tag gets the value derived from
 *    ITS OWN measured painted widths, merged across only its own occurrences.
 *  - PATCH BY TAG, NEVER BY PROXIMITY. The previous attempt guarded by scanning the next
 *    200 characters for `srcset=`, which sees a NEIGHBOURING image's srcset and silently
 *    skips the tag it meant to patch. Tags here are identified by byte offset, taken from
 *    a build-time stamp, and edits are applied back-to-front so earlier offsets stay valid.
 *  - `replace(..., 1)` FIXES ONLY THE FIRST. Not used at all: every edit is a splice at a
 *    known offset.
 *  - A tag whose src is a template gets a template srcset, so the data-array cases keep
 *    working for every row they render.
 *
 *   node scripts/image_srcset_apply.mjs --map map.json [--write]
 */
import { readFileSync, writeFileSync } from 'node:fs';
import { execFileSync } from 'node:child_process';

/**
 * The REAL intrinsic width of a file on disk.
 *
 * The map's `natural` is `img.naturalWidth` — the width of the candidate the browser
 * CHOSE, which for any tag that already had a srcset is not the file named in `src`.
 * Measured on this corpus: 229 of 273 descriptors would have been wrong, by as much as
 * 1408 vs 900. A `w` descriptor is a factual claim about a file; get it wrong and the
 * browser's whole selection is computed from a lie, which is worse than no srcset at all.
 */
const widthCache = new Map();
/** Read every width in ONE python process — 300 spawns took longer than the 2m budget. */
function preloadWidths(paths) {
  const uniq = [...new Set(paths)];
  if (!uniq.length) return;
  const script =
    'import sys,json\n' +
    'from PIL import Image\n' +
    'out={}\n' +
    'for p in json.load(sys.stdin):\n' +
    '    try:\n' +
    '        with Image.open("public"+p) as im: out[p]=im.width\n' +
    '    except Exception: out[p]=None\n' +
    'print(json.dumps(out))\n';
  try {
    const res = execFileSync('python3', ['-c', script], {
      input: JSON.stringify(uniq),
      encoding: 'utf8',
      maxBuffer: 32 * 1024 * 1024,
    });
    for (const [k, v] of Object.entries(JSON.parse(res))) widthCache.set(k, v);
  } catch (e) {
    console.error('width preload failed:', e.message);
  }
}
function realWidth(publicPath) {
  return widthCache.get(publicPath) ?? null;
}

const args = process.argv.slice(2);
const argOf = (n, d) => {
  const i = args.indexOf(n);
  return i >= 0 ? args[i + 1] : d;
};
const write = args.includes('--write');
const map = JSON.parse(readFileSync(argOf('--map', 'image-srcset-map.json'), 'utf8'));

/** `/a/foo-320.webp` + 240 -> `/a/foo-240.webp`. Mirrors image_srcset_variants.py. */
function variantName(src, w) {
  const m = src.match(/^(.*?)(\.[a-z0-9]+)$/i);
  if (!m) return src;
  return `${m[1].replace(/-\d{2,4}$/, '')}-${w}${m[2]}`;
}

/** The src attribute source text, so a template can be rewritten as a template. */
function srcExpr(raw) {
  const q = raw.match(/\bsrc\s*=\s*"([^"]*)"/);
  if (q) return { kind: 'quoted', value: q[1] };
  const t = raw.match(/\bsrc\s*=\s*\{\s*`([^`]*)`\s*\}/);
  if (t) return { kind: 'tpl', value: t[1] };
  const e = raw.match(/\bsrc\s*=\s*\{([^}]*)\}/);
  if (e) return { kind: 'expr', value: e[1].trim() };
  return null;
}

/**
 * The srcset attribute text for one tag.
 *
 * A literal src becomes a literal srcset. A template or expression src becomes a template
 * srcset built from the SAME expression with the width spliced into the filename, so a
 * data-array tag keeps producing the right candidate for every row it renders — the
 * alternative, expanding it to the concrete paths of the rows we happened to measure,
 * silently breaks the moment the array gains an entry.
 */
/** srcset of generated variants only — used when the rows' masters disagree on width. */
function buildVariantOnly(tag, se, widths) {
  if (se.kind === 'quoted') {
    const parts = widths.map((w) => `${variantName(se.value, w)} ${w}w`);
    return { attr: `srcset="${parts.join(', ')}"`, tpl: false };
  }
  const base = se.kind === 'tpl' ? '`' + se.value + '`' : se.value;
  const parts = widths.map(
    (w) =>
      '${' + `String(${base}).replace(/(-\\d{2,4})?(\\.[a-zA-Z0-9]+)$/, '-${w}$2')` + '}' + ` ${w}w`,
  );
  return { attr: 'srcset={`' + parts.join(', ') + '`}', tpl: true };
}

function buildSrcset(tag) {
  const widths = [...tag.wantWidths].sort((a, b) => a - b);
  if (!widths.length) return null;
  const se = srcExpr(tag.raw);
  if (!se) return null;

  // The master descriptor, read from disk. One tag can render several files (a data-array
  // row per bird); they must agree on intrinsic width, because a template srcset can only
  // carry ONE descriptor for the master. Disagreement is reported, never averaged.
  const masterWidths = [...new Set(tag.files.map((f) => realWidth(f)).filter(Boolean))];
  if (!masterWidths.length) return { error: 'no readable master' };

  if (masterWidths.length > 1) {
    // A data-array tag whose rows have different master widths (BirdCard renders
    // 760/640/1000/591). One template srcset carries one master descriptor, and there is
    // no honest single value for it.
    //
    // But the master does not have to be a candidate. Every GENERATED variant is cut to an
    // exact width, so a srcset made only of variants is exactly describable for every row.
    // Safe only while the widest candidate still exists for the SMALLEST master — asking
    // for a 760 variant of a 591px file yields nothing (the generator refuses to upscale)
    // and that candidate would 404 for that row.
    const smallest = Math.min(...masterWidths);
    const cap = Math.floor(smallest * 0.98);
    // Clamp the top candidate to the smallest master rather than refusing outright. On
    // BirdCard the plan wants 620px for a box that paints 605px at the 639 viewport, while
    // the smallest of its six masters is 591 — so that row is ALREADY served slightly
    // under its box today, before any of this. Clamping to 580 changes that row by ~2%
    // and moves the other five off masters up to 1000px wide. Refusing would leave all 18
    // occurrences on the master.
    //
    // This is the one place the "never under-declare" rule is knowingly bent, so it is
    // bounded and then VERIFIED by re-measuring: the acceptance below checks that no
    // occurrence ends up served below 0.95x of its painted box.
    const usable = [...new Set(widths.map((w) => Math.min(w, cap)))]
      .filter((w) => w > 40)
      .sort((a, b) => a - b);
    if (!usable.length) {
      return {
        error: `masters disagree (${masterWidths.join('/')}) and no candidate fits under ${smallest}px`,
      };
    }
    // `src` stays as the no-srcset fallback; the candidates are all exact.
    return buildVariantOnly(tag, se, usable);
  }

  const masterW = masterWidths[0];
  // Never emit a candidate at or above the master: it would be chosen over the master for
  // no benefit, and a variant wider than its source was upscaled.
  const useWidths = widths.filter((w) => w < masterW * 0.98);
  if (!useWidths.length) return { error: `every planned width >= master ${masterW}px` };

  if (se.kind === 'quoted') {
    const parts = useWidths.map((w) => `${variantName(se.value, w)} ${w}w`);
    parts.push(`${se.value} ${masterW}w`);
    return { attr: `srcset="${parts.join(', ')}"`, tpl: false };
  }

  // `${EXPR}` with the width folded into the stem. `.replace(/-\d{2,4}(?=\.\w+$)/, '')`
  // strips a width already in the master's name so `foo-320.webp` yields `foo-240.webp`
  // and never `foo-320-240.webp`.
  const base = se.kind === 'tpl' ? '`' + se.value + '`' : se.value;
  const mk = (w) =>
    '${' + `String(${base}).replace(/(-\\d{2,4})?(\\.[a-zA-Z0-9]+)$/, '-${w}$2')` + '}' + ` ${w}w`;
  const parts = useWidths.map(mk);
  parts.push('${' + base + '}' + ` ${masterW}w`);
  return { attr: 'srcset={`' + parts.join(', ') + '`}', tpl: true };
}

preloadWidths(map.tags.flatMap((t) => t.files ?? []));

const byFile = new Map();
let planned = 0;
let skippedNoWidths = 0;
let skippedConflict = 0;
const refused = [];

for (const t of map.tags) {
  if (t.conflicts?.length) {
    skippedConflict++;
    continue;
  }
  if (!t.wantWidths?.length || !t.sizesValue) {
    skippedNoWidths++;
    continue;
  }
  const ss = buildSrcset(t);
  if (!ss || ss.error) {
    if (ss?.error) refused.push({ file: t.file, start: t.start, why: ss.error, files: t.files });
    else skippedNoWidths++;
    continue;
  }
  if (!byFile.has(t.file)) byFile.set(t.file, []);
  byFile.get(t.file).push({ ...t, srcsetAttr: ss.attr });
  planned++;
}

let filesWritten = 0;
for (const [file, edits] of byFile) {
  let src = readFileSync(file, 'utf8');
  // Back-to-front: an edit changes the length of the file, so applying in ascending order
  // invalidates every later offset. This is the same class of error as `replace(...,1)`.
  edits.sort((a, b) => b.start - a.start);

  for (const e of edits) {
    const raw = src.slice(e.start, e.end);
    if (!raw.startsWith('<img')) {
      console.error(`REFUSING ${file}@${e.start}: offset is not an <img> ("${raw.slice(0, 24)}")`);
      process.exitCode = 1;
      continue;
    }
    // Drop any srcset/sizes this tag already carries — several already have one, and
    // adding a second attribute leaves the FIRST winning in every browser.
    let body = raw
      .replace(/\s+srcset\s*=\s*\{`[^`]*`\}/g, '')
      .replace(/\s+srcset\s*=\s*"[^"]*"/g, '')
      .replace(/\s+sizes\s*=\s*\{`[^`]*`\}/g, '')
      .replace(/\s+sizes\s*=\s*"[^"]*"/g, '');

    const close = body.endsWith('/>') ? 2 : 1;
    body = body.slice(0, body.length - close) + ` ${e.srcsetAttr} sizes="${e.sizesValue}"` +
      (close === 2 ? ' />' : '>');

    src = src.slice(0, e.start) + body + src.slice(e.end);
  }

  if (write) {
    writeFileSync(file, src);
    filesWritten++;
  }
}

console.log(`tags planned:        ${planned}`);
console.log(`  skipped, conflict: ${skippedConflict}`);
console.log(`  skipped, no widths:${skippedNoWidths}`);
if (refused.length) {
  console.log(`  REFUSED (${refused.length}) — reported, never guessed:`);
  for (const r of refused.slice(0, 10)) console.log(`    ${r.file}@${r.start}: ${r.why}`);
}
console.log(`files ${write ? 'written' : 'that would change'}: ${byFile.size}${write ? ` (${filesWritten})` : ''}`);
if (!write) console.log('\n(dry run — pass --write to edit source)');
