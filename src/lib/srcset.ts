import widths from '../data/image-widths.json';

const W = widths as Record<string, number>;

/** `/a/foo-320.webp` + 240 -> `/a/foo-240.webp`. Mirrors the generator scripts. */
function variantName(src: string, w: number): string {
  const m = src.match(/^(.*?)(\.[A-Za-z0-9]+)$/);
  if (!m) return src;
  return `${m[1].replace(/-\d{2,4}$/, '')}-${w}${m[2]}`;
}

/**
 * A truthful `srcset` for an image a shared component received as a PROP.
 *
 * A component cannot hardcode a `w` descriptor for an image it has never seen. Doing so
 * shipped two concrete defects on 2026-08-02: `NewsletterV2` declared `${img} 640w` for a
 * master that is actually 375px wide, and asked for a `-390` variant of it that cannot
 * exist. A false descriptor makes the browser's entire candidate selection wrong, and a
 * missing candidate renders as a broken image — both strictly worse than the oversized
 * image the srcset was added to fix.
 *
 * So every width here is read from the build-time manifest:
 *   - candidates are emitted ONLY where the variant file actually exists;
 *   - the master's descriptor is its real width;
 *   - a candidate at or above the master is dropped (it would win for no benefit);
 *   - an unknown image yields `undefined`, so the caller omits `srcset` entirely and the
 *     page keeps working exactly as it did before.
 *
 * Regenerate the manifest with `python3 scripts/build_image_manifest.py` after adding
 * images, and fill any newly-referenced variant with
 * `python3 scripts/image_srcset_fill_missing.py --apply`.
 */
export function srcsetFor(src: string | undefined, wanted: number[]): string | undefined {
  if (!src || !src.startsWith('/')) return undefined;
  const master = W[src];
  if (!master) return undefined;

  const parts: string[] = [];
  for (const w of [...wanted].sort((a, b) => a - b)) {
    if (w >= master * 0.98) continue;
    const v = variantName(src, w);
    const actual = W[v];
    if (!actual) continue;
    parts.push(`${v} ${actual}w`);
  }
  if (!parts.length) return undefined;
  parts.push(`${src} ${master}w`);
  return parts.join(', ');
}
