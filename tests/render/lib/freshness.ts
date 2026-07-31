import { existsSync, readdirSync, statSync } from 'node:fs';
import { join, relative, resolve } from 'node:path';

/**
 * Directory names that are never source, wherever they appear. `src/pages/node_modules/.vite/`
 * exists in this repo — walking it costs thousands of stats and would refuse every run the
 * moment Vite touched a vendored dep.
 */
const SKIP = new Set(['node_modules', '.vite', '.git', '.DS_Store', '.astro', '.cache']);

/** Source paths whose mtime should force a rebuild. Missing entries are skipped, not fatal. */
const SOURCES = ['src', 'public', 'astro.config.mjs', 'package.json'];

export interface Freshness {
  fresh: boolean;
  /** Always populated — on failure it names the offending file AND the remedy. */
  reason: string;
}

function newest(path: string): { path: string; ms: number } {
  let best = { path, ms: 0 };
  const walk = (dir: string): void => {
    let entries;
    try {
      entries = readdirSync(dir, { withFileTypes: true });
    } catch {
      return;
    }
    for (const e of entries) {
      if (SKIP.has(e.name)) continue;
      const p = join(dir, e.name);
      if (e.isDirectory()) {
        walk(p);
      } else {
        let ms = 0;
        try {
          ms = statSync(p).mtimeMs;
        } catch {
          continue;
        }
        if (ms > best.ms) best = { path: p, ms };
      }
    }
  };
  let st;
  try {
    st = statSync(path);
  } catch {
    return best;
  }
  if (st.isDirectory()) walk(path);
  else best = { path, ms: st.mtimeMs };
  return best;
}

/**
 * A stale `dist/` is the quietest way this harness can lie: every check passes, every
 * number is real, and all of them describe a build nobody is shipping. Refuse to measure.
 */
export function checkDistFreshness(root: string = process.cwd()): Freshness {
  const dist = resolve(root, 'dist');
  if (!existsSync(dist)) {
    return { fresh: false, reason: 'dist/ does not exist — run `npm run build` first' };
  }
  const newestDist = newest(dist);
  if (newestDist.ms === 0) {
    return { fresh: false, reason: 'dist/ contains no files — run `npm run build` first' };
  }

  for (const rel of SOURCES) {
    const p = resolve(root, rel);
    if (!existsSync(p)) continue;
    const n = newest(p);
    if (n.ms > newestDist.ms) {
      const ageMin = Math.round((n.ms - newestDist.ms) / 60000);
      return {
        fresh: false,
        reason:
          `${relative(root, n.path)} is ${ageMin} min newer than the newest file in dist/ ` +
          `(${relative(root, newestDist.path)}) — run \`npm run build\` first. ` +
          `Measuring a stale dist/ produces real numbers about a build nobody ships.`,
      };
    }
  }
  return { fresh: true, reason: `dist/ is current (newest: ${relative(root, newestDist.path)})` };
}
