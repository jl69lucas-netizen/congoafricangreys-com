import { mkdirSync, writeFileSync } from 'node:fs';
import { resolve } from 'node:path';
import type { Defect } from './registry.js';

/** Named PagePartial, not Partial — `Partial<T>` is a TypeScript built-in. */
export interface PagePartial {
  slug: string;
  page_type: string;
  viewport: number;
  examined: Record<string, number>;
  defects: Defect[];
  overrides: { checkId: string; reason: string }[];
}

const RAW_DIR = resolve(process.cwd(), 'data/quality/raw');

export function writePartial(p: PagePartial): void {
  mkdirSync(RAW_DIR, { recursive: true });
  writeFileSync(resolve(RAW_DIR, `${p.slug}-vp${p.viewport}.json`), JSON.stringify(p, null, 2));
}

/**
 * The list of every registered check id, written once per run.
 * The merge script needs this to detect a check that ran NOWHERE — such a check
 * contributes no key to any partial's `examined` map, so it is invisible to a
 * guard that only reads the partials.
 */
export function writeManifest(checkIds: string[], expectedPartials: number): void {
  mkdirSync(RAW_DIR, { recursive: true });
  writeFileSync(
    resolve(RAW_DIR, '_manifest.json'),
    JSON.stringify({ checkIds, expectedPartials }, null, 2),
  );
}
