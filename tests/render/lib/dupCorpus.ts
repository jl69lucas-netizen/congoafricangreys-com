import { readFileSync, existsSync, readdirSync } from 'node:fs';
import { resolve, dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const here = dirname(fileURLToPath(import.meta.url));
export const REPO = resolve(here, '../../..');

/**
 * The whitelist is READ FROM `scripts/dup_content_audit.py`, never copied.
 *
 * That file's list is the only tuned one this project has: it was built by working
 * through real reports and encodes exactly what CLAUDE.md says may legitimately repeat
 * across siblings — the shipping cost line, doc-badge enumerations, the counter strip,
 * the CITES notice, real reviews. Forking it into TypeScript would create two lists that
 * agree today and drift the first time either is tuned, and the drift would show up as a
 * check reporting a mandated line as a defect.
 *
 * The trade-off, stated: this parses Python string literals with a regex, so a future
 * entry written with an f-string or built by concatenation would be missed. The parse
 * therefore ASSERTS a floor on how many entries it found — a silently-empty whitelist
 * would turn every mandated line into a defect on every page at once.
 */
export function loadWhitelist(): string[] {
  const src = readFileSync(join(REPO, 'scripts/dup_content_audit.py'), 'utf8');
  const start = src.indexOf('WHITELIST_SNIPPETS');
  if (start < 0) throw new Error('dup_content_audit.py no longer defines WHITELIST_SNIPPETS');
  const end = src.indexOf('\n]', start);
  const block = src.slice(start, end < 0 ? undefined : end);
  const out: string[] = [];
  for (const m of block.matchAll(/"([^"]{8,})"|'([^']{8,})'/g)) {
    out.push((m[1] ?? m[2]).toLowerCase());
  }
  if (out.length < 10) {
    throw new Error(
      `parsed only ${out.length} whitelist entries from dup_content_audit.py — refusing to ` +
        `run with a near-empty whitelist, which would report every mandated line as a defect`,
    );
  }
  return out;
}

/** The same normalisation the Python auditor applies, so runs are comparable. */
export function normalise(text: string): string[] {
  return text
    .toLowerCase()
    .replace(/[^a-z0-9$ ]+/g, ' ')
    .split(/\s+/)
    .filter(Boolean);
}

/** Visible text of a built page — script, style and JSON-LD stripped. */
export function distText(slug: string): string | null {
  const file = join(REPO, 'dist', slug, 'index.html');
  if (!existsSync(file)) return null;
  let html = readFileSync(file, 'utf8');
  html = html.replace(/<script[\s\S]*?<\/script>/gi, ' ');
  html = html.replace(/<style[\s\S]*?<\/style>/gi, ' ');
  html = html.replace(/<!--[\s\S]*?-->/g, ' ');
  const main = /<main[\s\S]*?>([\s\S]*)<\/main>/i.exec(html);
  return (main ? main[1] : html).replace(/<[^>]+>/g, ' ');
}

/** Every .html file in a fixture corpus directory, for the meta gate. */
export function fixtureCorpus(dir: string): { slug: string; text: string }[] {
  const full = join(REPO, dir);
  if (!existsSync(full)) return [];
  return readdirSync(full)
    .filter((f) => f.endsWith('.html'))
    .map((f) => ({
      slug: f.replace(/\.html$/, ''),
      text: readFileSync(join(full, f), 'utf8')
        .replace(/<script[\s\S]*?<\/script>/gi, ' ')
        .replace(/<style[\s\S]*?<\/style>/gi, ' ')
        .replace(/<[^>]+>/g, ' '),
    }));
}
