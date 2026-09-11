/**
 * The homepage hero image and its responsive contract, shared by HeroV3's <img> and the
 * homepage <link rel="preload"> so the two can never list different candidates or sizes.
 *
 * Sizes are the rendered photo width inside the Paperwork card (hero round 5, variation A):
 *   ≥1280 card 492px − 2×14 padding = 464px · 1024–1279 card 420px − 28 = 392px
 *   768–1023 card 292px − 2×12 = 268px · <768 full width − 2×16 page − 2×12 card = 100vw − 56px
 */
export const HERO_IMG = '/african-grey-parrot-breeder-midland-tx-hero.webp';
export const HERO_WIDTHS = [300, 600];
export const HERO_SIZES =
  '(min-width: 1280px) 464px, (min-width: 1024px) 392px, (min-width: 768px) 268px, calc(100vw - 56px)';
