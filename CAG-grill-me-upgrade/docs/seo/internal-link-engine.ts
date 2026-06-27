export type Page = {
  slug: string;
  title: string;
  category: 'money' | 'geo' | 'comparison' | 'trust' | 'blog';
  keywords: string[];
};

export const pages: Page[] = [
  { slug: '/african-grey-for-sale/', title: 'African Grey For Sale', category: 'money', keywords: ['african grey','for sale'] },
  { slug: '/baby-african-grey-for-sale/', title: 'Baby African Grey For Sale', category: 'money', keywords: ['baby african grey'] },
  { slug: '/african-grey-for-sale-texas/', title: 'African Grey For Sale Texas', category: 'geo', keywords: ['texas','african grey'] },
  { slug: '/african-grey-vs-macaw/', title: 'African Grey vs Macaw', category: 'comparison', keywords: ['macaw','comparison'] },
  { slug: '/trusted-african-grey-breeder-usa/', title: 'Trusted African Grey Breeder USA', category: 'trust', keywords: ['trusted breeder'] },
  { slug: '/african-grey-lifespan/', title: 'African Grey Lifespan', category: 'blog', keywords: ['lifespan'] },
];

export function scoreRelated(current: Page, candidate: Page): number {
  if (current.slug === candidate.slug) return -999;
  let score = 0;
  if (current.category === candidate.category) score += 3;
  current.keywords.forEach(k => {
    if (candidate.keywords.includes(k)) score += 2;
  });
  if (candidate.category === 'money') score += 2;
  if (candidate.category === 'trust') score += 1;
  return score;
}

export function getRelatedLinks(currentSlug: string, limit = 6): Page[] {
  const current = pages.find(p => p.slug === currentSlug);
  if (!current) return [];

  return pages
    .map(p => ({ page: p, score: scoreRelated(current, p) }))
    .sort((a,b) => b.score - a.score)
    .slice(0, limit)
    .map(x => x.page);
}

export function renderLinks(currentSlug: string): string {
  const related = getRelatedLinks(currentSlug, 6);
  return `<section class='related-links'>\n<h2>Related Guides</h2>\n<ul>\n${related.map(link => `<li><a href='${link.slug}'>${link.title}</a></li>`).join('\n')}\n</ul>\n</section>`;
}

/* Usage in Astro:
---
import { renderLinks } from '../lib/internal-links';
const html = renderLinks(Astro.url.pathname);
---
<Fragment set:html={html} />
*/
