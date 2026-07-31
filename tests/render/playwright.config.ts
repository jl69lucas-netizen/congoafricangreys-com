import { defineConfig } from '@playwright/test';

const PORT = 4321;

export default defineConfig({
  testDir: '.',
  testMatch: ['meta.spec.ts', 'pages.spec.ts'],
  fullyParallel: false,
  workers: 2,
  timeout: 120_000,
  reporter: [['list']],
  use: {
    baseURL: `http://127.0.0.1:${PORT}`,
    deviceScaleFactor: 1,
  },
  projects: [
    { name: 'vp375', use: { viewport: { width: 375, height: 812 } } },
    { name: 'vp768', use: { viewport: { width: 768, height: 1024 } } },
    { name: 'vp1280', use: { viewport: { width: 1280, height: 800 } } },
  ],
  webServer: {
    command: `python3 -m http.server ${PORT} --bind 127.0.0.1`,
    cwd: '../../',
    port: PORT,
    reuseExistingServer: true,
    timeout: 60_000,
  },
});
