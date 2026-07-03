import { defineConfig } from 'astro/config';

import tailwindcss from '@tailwindcss/vite';

import react from '@astrojs/react';

import mdx from '@astrojs/mdx';

export default defineConfig({
  // Inline ALL stylesheets (incl. the ~105KB raw / ~18KB gzip BaseLayout.css) into
  // <style> tags. Lighthouse flagged the external BaseLayout.css as the render-blocking
  // request + critical-chain tail (~300ms) on every page; inlining removes that round
  // trip entirely. Trade-off: the CSS is no longer cached across page navigations
  // (+~18KB gzip per HTML load) — accepted 2026-07-03 to clear the perf gate.
  build: {
    inlineStylesheets: 'always',
  },
  vite: {
    plugins: [tailwindcss()],
    build: {
      assetsInlineLimit: 6500,
      rollupOptions: {
        external: ['/pagefind/pagefind.js']
      }
    }
  },

  integrations: [react(), mdx()]
});