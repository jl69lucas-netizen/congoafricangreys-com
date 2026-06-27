import { defineConfig } from 'astro/config';

import tailwindcss from '@tailwindcss/vite';

import react from '@astrojs/react';

import mdx from '@astrojs/mdx';

export default defineConfig({
  // Inline small render-blocking component stylesheets (JumpRail ~5.4KB,
  // cag-inquiry-form ~5.8KB, small per-route index.*.css) into <style> tags so
  // they leave the critical request path. 'auto' inlines any stylesheet smaller
  // than vite.build.assetsInlineLimit; we raise it to 6500 to catch those two
  // component files while keeping the 105KB BaseLayout.css external. Verified safe:
  // zero non-CSS assets are <7KB, so no image/font gets base64-inlined as a side effect.
  build: {
    inlineStylesheets: 'auto',
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