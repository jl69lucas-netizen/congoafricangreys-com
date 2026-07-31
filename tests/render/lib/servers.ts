/**
 * Two static servers, deliberately.
 *
 * Built pages reference their assets with absolute paths (`/images/...`,
 * `/cag-header-logo-160.webp`) that resolve against `dist/`. Serving the repo
 * root instead would 404 every one of them — and a 404'd image has
 * `naturalWidth === 0`, which the IMG checks skip, which means a page full of
 * oversized images would report clean. So `dist/` is its own server root.
 *
 * Fixtures live outside dist/, so they get their own server on the repo root.
 */
export const SITE_PORT = 4321;
export const FIXTURE_PORT = 4322;

export const SITE_BASE = `http://127.0.0.1:${SITE_PORT}`;
export const FIXTURE_BASE = `http://127.0.0.1:${FIXTURE_PORT}`;

/** Absolute URL of a fixture page, e.g. fixtureUrl('known_broken', 'img-srcset-within-2x'). */
export function fixtureUrl(kind: 'known_good' | 'known_broken', checkId: string): string {
  return `${FIXTURE_BASE}/tests/render/fixtures/${kind}/${checkId}.html`;
}
