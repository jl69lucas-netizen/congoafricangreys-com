/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    extend: {
      colors: {
        'logo-dark':  '#12100e',
        'gold':       '#c4a05a',
        'cream':      '#f5eeda',
        'rust':       '#b43c2d',
        'warm-white': '#faf7f4',
      },
      fontFamily: {
        lora: ['Lora', 'Georgia', 'serif'],
        sora: ['Sora', 'system-ui', 'sans-serif'],
      },
    },
  },
  plugins: [],
};
