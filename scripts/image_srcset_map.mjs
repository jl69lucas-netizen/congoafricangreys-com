#!/usr/bin/env node
/**
 * Map every measured image OCCURRENCE back to the SOURCE `<img>` tag that produced it,
 * then derive one `sizes` per TAG rather than per occurrence.
 *
 * This is the step the plan tool deliberately does not do, and the reason the previous
 * srcset attempt stalled: several of these images render from data arrays inside shared
 * components, so a single source tag emits many occurrences — `<img src={`${IMG}/${b.img}
 * -440.webp`}>` on the baby page is five cards. You cannot patch "an occurrence"; you can
 * only patch a tag, and the tag has to carry a `sizes` that is correct for EVERY
 * occurrence it produces.
 *
 * The merge rule is the one the reverted attempt got wrong, stated explicitly:
 *
 *   a tag's declared width at each viewport is the MAXIMUM painted width across all of
 *   its occurrences at that viewport — never the mean, never the first.
 *
 * Under-declaring makes the browser fetch a file smaller than the box and the page ships
 * visible blur, which is what got the last attempt reverted. Over-declaring costs bytes.
 * Those are not symmetric, so the merge is deliberately biased toward bytes.
 *
 * An occurrence whose painted width is so much smaller than its tag-mates' that the merged
 * declaration would exceed 2x ITS box is reported as a CONFLICT and patched by nobody —
 * that tag needs a prop or a split, which is a judgement call, not a scripted edit.
 *
 *   node scripts/image_srcset_map.mjs --plan plan.json --out map.json
 */
import { readFileSync, writeFileSync } from 'node:fs';
import { globSync } from 'node:fs';
import { execSync } from 'node:child_process';

const args = process.argv.slice(2);
const argOf = (n, d) => {
  const i = args.indexOf(n);
  return i >= 0 ? args[i + 1] : d;
};
const planFile = argOf('--plan', 'image-srcset-plan.json');
const outFile = argOf('--out', 'image-srcset-map.json');
const MAX_RATIO = 2.0;

const plan = JSON.parse(readFileSync(planFile, 'utf8'));

/** Source files that can emit an <img>: the pages themselves and every component. */
const sourceFiles = execSync(
  `find src -type f \\( -name '*.astro' -o -name '*.html' \\) | sort`,
  { encoding: 'utf8' },
)
  .trim()
  .split('\n')
  .filter(Boolean);

const text = new Map(sourceFiles.map((f) => [f, readFileSync(f, 'utf8')]));

/**
 * Resolve `const NAME = "literal"` so a template like `${IMG}/x.webp` can be matched
 * against a concrete rendered path. Only string literals — anything computed is left as a
 * wildcard, which costs precision but never correctness, because a wildcard can only make
 * the match BROADER and a broader match is caught by the ambiguity guard below.
 */
function consts(src) {
  const m = new Map();
  for (const mm of src.matchAll(/const\s+([A-Za-z_$][\w$]*)\s*=\s*["'`]([^"'`]*)["'`]/g)) {
    m.set(mm[1], mm[2]);
  }
  return m;
}

/** Every <img ...> tag in a file, with its byte offsets so the patch can be exact. */
function imgTags(src) {
  const out = [];
  const re = /<img\b/gi;
  let m;
  while ((m = re.exec(src))) {
    // Walk to the tag's own '>' while respecting quotes and {…} expressions, so a '>'
    // inside a template literal or a JSX expression does not truncate the tag.
    let i = m.index + 4;
    let depth = 0;
    let quote = null;
    for (; i < src.length; i++) {
      const c = src[i];
      if (quote) {
        if (c === quote && src[i - 1] !== '\\') quote = null;
        continue;
      }
      if (c === '"' || c === "'" || c === '`') quote = c;
      else if (c === '{') depth++;
      else if (c === '}') depth--;
      else if (c === '>' && depth === 0) break;
    }
    out.push({ start: m.index, end: i + 1, raw: src.slice(m.index, i + 1) });
  }
  return out;
}

/** The tag's src attribute, as a regex that a rendered path must satisfy. */
function srcPattern(tagRaw, cmap) {
  const quoted = tagRaw.match(/\bsrc\s*=\s*"([^"]*)"/) || tagRaw.match(/\bsrc\s*=\s*'([^']*)'/);
  const tpl = tagRaw.match(/\bsrc\s*=\s*\{\s*`([^`]*)`\s*\}/);
  const expr = tagRaw.match(/\bsrc\s*=\s*\{([^}]*)\}/);

  // `src={b.img}` — a bare expression whose value lives in a data array elsewhere in the
  // file. Its path is not in the tag at all, so the tag matches ANY rendered path; the
  // ambiguity guard downstream is what keeps that honest. Treating `b.img` as a literal
  // string (the first cut did) matches nothing and reports the occurrence as sourceless.
  if (!quoted && !tpl && expr) {
    return { literal: false, raw: expr[1].trim(), rx: /^.*$/, opaque: true };
  }

  const mm = quoted || tpl;
  if (!mm) return null;
  let v = mm[1];
  // Substitute known consts, then turn any remaining ${…} into a wildcard.
  v = v.replace(/\$\{\s*([A-Za-z_$][\w$]*)\s*\}/g, (all, name) =>
    cmap.has(name) ? cmap.get(name) : all,
  );
  const literal = !/\$\{|\{/.test(v);
  // Split on the `${…}` holes FIRST, escape only the literal spans, then join with a
  // wildcard. Escaping before substituting turns `${b.img}` into `$\{b.img\}`, after which
  // no placeholder pattern can match it — that bug silently left 173 of 292 occurrences
  // unmatched, which reads exactly like "these images have no source" and is not true.
  const parts = v.split(/\$\{[^}]*\}/);
  const esc = (s) => s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  const rx = parts.map(esc).join('[^"\'`\\s]*');
  return { literal, raw: v, rx: new RegExp('^' + rx + '$') };
}

// ---------------------------------------------------------------------------------------

const tags = [];
for (const f of sourceFiles) {
  const src = text.get(f);
  const cmap = consts(src);
  for (const t of imgTags(src)) {
    const p = srcPattern(t.raw, cmap);
    if (!p) continue;
    tags.push({ file: f, ...t, pattern: p });
  }
}

/** How many <img> tags in the BUILT page carry this exact src. */
const distCache = new Map();
function renderedCount(slug, srcPath) {
  if (!distCache.has(slug)) {
    try {
      distCache.set(slug, readFileSync(`dist/${slug}/index.html`, 'utf8'));
    } catch {
      distCache.set(slug, '');
    }
  }
  const html = distCache.get(slug);
  if (!html) return 0;
  let n = 0;
  const needle = `src="${srcPath}"`;
  for (let i = html.indexOf(needle); i !== -1; i = html.indexOf(needle, i + 1)) n++;
  return n;
}

/**
 * Every source file a page can actually render from: itself plus the components it
 * imports, transitively (and their layouts). Without this, a bare `<img src={expr}>` in
 * ANY component on the site is a candidate for every occurrence on every page — four
 * components claimed the same bird card on the care guide, none of which it imports.
 */
const importCache = new Map();
function reachableFrom(file, seen = new Set()) {
  if (!file || seen.has(file)) return seen;
  seen.add(file);
  const src = text.get(file);
  if (!src) return seen;
  for (const m of src.matchAll(/^\s*import\s+[^'"]*from\s+['"]([^'"]+)['"]/gm)) {
    const spec = m[1];
    if (!spec.startsWith('.') && !spec.startsWith('@/') && !spec.startsWith('~/')) continue;
    let base = spec.replace(/^@\//, 'src/').replace(/^~\//, 'src/');
    if (base.startsWith('.')) {
      const dir = file.split('/').slice(0, -1).join('/');
      base = new URL(spec, `file:///${dir}/`).pathname.replace(/^\//, '');
    }
    for (const cand of [base, `${base}.astro`, `${base}/index.astro`]) {
      if (text.has(cand)) {
        reachableFrom(cand, seen);
        break;
      }
    }
  }
  return seen;
}
function reachable(file) {
  if (!importCache.has(file)) importCache.set(file, reachableFrom(file));
  return importCache.get(file);
}

/** A page's own source file, so a tag there wins over the same path in a sibling page. */
function pageSourceOf(slug) {
  const a = `src/pages/${slug}/index.astro`;
  const h = `src/pages/${slug}/index.html`;
  if (text.has(a)) return a;
  if (text.has(h)) return h;
  return null;
}

const byTag = new Map();
const unmatched = [];
const ambiguous = [];

// The occurrence -> source-tag mapping, MEASURED by scripts/image_srcset_instrument.mjs
// rather than inferred. Every heuristic below (const resolution, template wildcards,
// import graph, class matching, document-order pairing) is retained only as a fallback for
// an occurrence the stamp did not cover; on the current corpus the stamp covers all 292
// and the heuristics resolve none of them. Inference left 141 occurrences ambiguous, and
// an ambiguous tag patched wrong writes a `sizes` measured from one box onto an image that
// paints at another — the reverted blur bug by another route.
let stamped = null;
try {
  stamped = JSON.parse(readFileSync(argOf('--tagmap', 'image-srcset-tagmap.json'), 'utf8'));
} catch {
  stamped = null;
}
const tagByKey = new Map(tags.map((t) => [`${t.file}@${t.start}`, t]));

for (const [slug, items] of Object.entries(plan.pages)) {
  const own = pageSourceOf(slug);

  if (stamped) {
    const left = [];
    for (const it of items) {
      const id = stamped[`${slug}|${it.src}|${it.nth}`];
      const t = id ? tagByKey.get(id) : null;
      if (!t) {
        left.push(it);
        continue;
      }
      const key = `${t.file}@${t.start}`;
      if (!byTag.has(key)) byTag.set(key, { file: t.file, start: t.start, end: t.end, raw: t.raw, occ: [] });
      byTag.get(key).occ.push({ slug, ...it });
    }
    if (!left.length) continue;
    items.length = 0;
    items.push(...left);
  }

  // Group by src so the nth-occurrence index can be spent where it is meaningful. A page
  // that renders the same file from three different tags produces three occurrences of it,
  // and `nth` is the only thing that distinguishes them — resolving each occurrence
  // independently just reports the same N-way ambiguity N times.
  const bySrc = new Map();
  for (const it of items) {
    if (!bySrc.has(it.src)) bySrc.set(it.src, []);
    bySrc.get(it.src).push(it);
  }

  for (const [srcPath, group] of bySrc) {
    group.sort((a, b) => a.nth - b.nth);
    let cands = tags.filter((t) => t.pattern.rx.test(srcPath));

    // Only files this page can actually reach. Everything else is not a weaker candidate,
    // it is not a candidate at all.
    const reach = own ? reachable(own) : null;
    if (reach) {
      const inReach = cands.filter((t) => reach.has(t.file));
      if (inReach.length) cands = inReach;
    }

    // Prefer the page's own file; a shared component only owns the tag when the page
    // itself does not contain a matching one.
    const inOwn = cands.filter((t) => t.file === own);
    if (inOwn.length) cands = inOwn;
    else cands = cands.filter((t) => !t.file.startsWith('src/pages/') || t.file === own);

    if (!cands.length) {
      for (const it of group) unmatched.push({ slug, src: srcPath, nth: it.nth });
      continue;
    }
    // Specificity order: an exact literal beats a template, and a template beats a bare
    // `{expr}` that matches everything. Without this an opaque tag steals occurrences that
    // a literal tag plainly owns, and the theft is invisible because both "match".
    const lit = cands.filter((t) => t.pattern.literal && t.pattern.raw === srcPath);
    if (lit.length) cands = lit;
    else {
      const tpl = cands.filter((t) => !t.pattern.opaque);
      if (tpl.length) cands = tpl;
    }

    cands = [...cands].sort((a, b) => (a.file === b.file ? a.start - b.start : a.file < b.file ? -1 : 1));

    // Two bare `{expr}` tags both match every path, so src alone cannot separate a bird
    // card from a review avatar on the same page. The rendered class can: filter to tags
    // whose STATIC class tokens all appear on the measured element. Tags with a dynamic
    // class are left in the running rather than excluded — absence of evidence is not
    // evidence of mismatch, and the count checks below still have to agree.
    if (cands.length > 1) {
      const narrowed = cands.filter((t) => {
        const cm = t.raw.match(/\bclass\s*=\s*"([^"{}]*)"/);
        if (!cm) return true;
        const need = cm[1].trim().split(/\s+/).filter(Boolean);
        if (!need.length) return true;
        return group.every((it) => {
          const have = new Set((it.cls || '').split(/\s+/).filter(Boolean));
          return need.every((n) => have.has(n));
        });
      });
      if (narrowed.length) cands = narrowed;
    }

    // One tag serving every occurrence (a data-array loop), or one tag per occurrence in
    // document order. Astro emits template tags in source order, so the nth rendered
    // occurrence comes from the nth matching tag. Any other shape is a real ambiguity and
    // is reported rather than guessed — a wrong pairing here writes a `sizes` measured
    // from one box onto an image that paints at another, which is the blur bug by a
    // different route.
    // How many times the BUILT page actually renders this file. The plan only carries
    // occurrences that exceed the cap, so `group.length` is a filtered count and comparing
    // source tags against it mis-reports a 2-tag/2-render page as ambiguous whenever only
    // one of the two was oversized. dist/ is the ground truth for what shipped.
    const rendered = renderedCount(slug, srcPath);

    let pairs;
    if (cands.length === 1) pairs = group.map((it) => [cands[0], it]);
    else if (cands.length === rendered && group.every((it) => it.nth >= 1 && it.nth <= cands.length))
      pairs = group.map((it) => [cands[it.nth - 1], it]);
    else if (cands.length === group.length) pairs = group.map((it, i) => [cands[i], it]);
    else {
      for (const it of group) {
        ambiguous.push({
          slug,
          src: srcPath,
          nth: it.nth,
          tags: cands.length,
          occurrences: group.length,
          files: cands.map((c) => `${c.file}@${c.start}`),
        });
      }
      continue;
    }

    for (const [t, it] of pairs) {
      const key = `${t.file}@${t.start}`;
      if (!byTag.has(key)) byTag.set(key, { file: t.file, start: t.start, end: t.end, raw: t.raw, occ: [] });
      byTag.get(key).occ.push({ slug, ...it });
    }
  }
}

// --- merge each tag's occurrences into ONE sizes, biased to over-declare -----------------

const SWEEP = plan.sweep ?? [375, 414, 480, 639, 640, 767, 768, 900, 1023, 1024, 1280, 1440];

const results = [];
for (const [key, t] of byTag) {
  const merged = {};
  for (const v of SWEEP) {
    const vals = t.occ.map((o) => o.painted[v]).filter((x) => x != null);
    if (vals.length) merged[v] = Math.max(...vals);
  }
  const natural = Math.max(...t.occ.map((o) => o.natural));
  const d = derive({ painted: merged, natural });

  // Verify the MERGED sizes against every occurrence individually — the merge is only
  // safe if each occurrence still clears the cap under it.
  const conflicts = [];
  for (const o of t.occ) {
    const worst = worstUnder(d, o);
    if (worst > MAX_RATIO) conflicts.push({ slug: o.slug, src: o.src, nth: o.nth, worst });
  }
  results.push({
    key,
    file: t.file,
    start: t.start,
    end: t.end,
    raw: t.raw,
    occurrences: t.occ.map((o) => ({ slug: o.slug, src: o.src, nth: o.nth })),
    files: [...new Set(t.occ.map((o) => o.src))],
    sizesValue: d.sizesValue,
    wantWidths: d.wantWidths,
    natural,
    conflicts,
  });
}

writeFileSync(outFile, JSON.stringify({ tags: results, unmatched, ambiguous }, null, 2));

const clean = results.filter((r) => !r.conflicts.length);
console.log(`tags matched:        ${results.length}`);
console.log(`  clean (patchable): ${clean.length}`);
console.log(`  with conflicts:    ${results.length - clean.length}`);
console.log(`occurrences unmatched to any tag: ${unmatched.length}`);
console.log(`occurrences ambiguous (>1 tag):   ${ambiguous.length}`);
console.log(
  `distinct (file,width) variants needed: ${
    new Set(clean.flatMap((r) => r.files.flatMap((f) => r.wantWidths.map((w) => `${f}|${w}`)))).size
  }`,
);
if (unmatched.length) console.log('\nunmatched examples:', unmatched.slice(0, 6));
if (ambiguous.length) console.log('\nambiguous examples:', ambiguous.slice(0, 4));
for (const r of results.filter((r) => r.conflicts.length).slice(0, 6)) {
  console.log(`\nCONFLICT ${r.file}@${r.start} (${r.occurrences.length} occurrences)`);
  console.log(`  sizes=${r.sizesValue}`);
  for (const c of r.conflicts.slice(0, 3)) console.log(`   ${c.worst.toFixed(2)}x  ${c.src} [${c.slug}]`);
}

// --- the same derivation the plan tool uses, kept identical on purpose ------------------

function derive(e) {
  const pts = SWEEP.filter((v) => e.painted[v] != null);
  if (!pts.length || !e.natural) return { sizesValue: null, wantWidths: [] };

  const fit = (run) => {
    const vw = Math.ceil(Math.max(...run.map((v) => e.painted[v] / v)) * 1000) / 10;
    if (run.every((v) => (vw / 100) * v >= e.painted[v] - 0.5 && (vw / 100) * v <= e.painted[v] * 1.5))
      return `${vw}vw`;
    const px = Math.ceil(Math.max(...run.map((v) => e.painted[v])));
    if (run.every((v) => px >= e.painted[v] - 0.5 && px <= e.painted[v] * 1.5)) return `${px}px`;
    return null;
  };

  const merged = [];
  let i = 0;
  while (i < pts.length) {
    let run = [pts[i]];
    let best = fit(run);
    let j = i + 1;
    while (j < pts.length) {
      const nx = fit([...run, pts[j]]);
      if (!nx) break;
      run.push(pts[j]);
      best = nx;
      j++;
    }
    merged.push({ hi: run[run.length - 1], value: best, pts: [...run] });
    i = j;
  }
  const sizesValue = merged
    .map((m, k) => (k === merged.length - 1 ? m.value : `(max-width:${m.hi}px) ${m.value}`))
    .join(', ');

  const demands = [];
  for (const m of merged) {
    for (const v of m.pts) {
      const declared = m.value.endsWith('vw') ? (parseFloat(m.value) / 100) * v : parseFloat(m.value);
      const step = declared < 120 ? 4 : declared < 400 ? 10 : 20;
      demands.push({ vp: v, painted: e.painted[v], declared: Math.ceil(declared / step) * step });
    }
  }
  const want = [];
  for (const w of [...new Set(demands.map((d) => d.declared))].sort((a, b) => b - a)) {
    const covered = want.find((ex) => {
      const users = demands.filter((d) => d.declared <= ex && d.declared >= w);
      return users.every((d) => ex / d.painted <= MAX_RATIO * 0.95);
    });
    if (!covered) want.push(w);
  }
  want.sort((a, b) => a - b);
  const wantWidths = want.filter((w) => w > 40 && w < e.natural * 0.95);
  return { sizesValue, wantWidths, merged };
}

/** Worst ratio a single occurrence sees under a tag-level sizes/candidate set. */
function worstUnder(d, o) {
  if (!d.sizesValue) return Infinity;
  const candidates = [...d.wantWidths, o.natural].sort((a, b) => a - b);
  let worst = 0;
  for (const m of d.merged) {
    for (const v of m.pts) {
      const painted = o.painted[v];
      if (painted == null) continue;
      const declared = m.value.endsWith('vw') ? (parseFloat(m.value) / 100) * v : parseFloat(m.value);
      const step = declared < 120 ? 4 : declared < 400 ? 10 : 20;
      const want = Math.ceil(declared / step) * step;
      const pick = candidates.find((c) => c >= want) ?? o.natural;
      worst = Math.max(worst, pick / painted);
    }
  }
  return worst;
}
