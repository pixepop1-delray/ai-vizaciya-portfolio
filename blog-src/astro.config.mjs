// @ts-check
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

// Blog builds standalone (base "/") and the build output gets copied into
// /blog at the repo root by the GitHub Actions workflow — this keeps the
// Astro project itself portable (works locally, previews cleanly, and
// survives a future move to a custom domain without base-path surgery).
// `site` is used only for absolute URLs in the generated sitemap; when the
// custom domain arrives, update it here (and siteRoot in BlogLayout.astro).
export default defineConfig({
  site: 'https://ai-garage.tech',
  outDir: './dist',
  build: {
    format: 'directory',
  },
  integrations: [
    sitemap({
      // these pages live outside Astro (main landing, static About/Privacy), so add by hand
      customPages: [
        'https://ai-garage.tech/',
        'https://ai-garage.tech/about/',
        'https://ai-garage.tech/privacy/',
        'https://ai-garage.tech/cases/ii-sekretar/',
        'https://ai-garage.tech/cases/menedzher-zadach/',
        'https://ai-garage.tech/cases/uchet-rashodov/',
        'https://ai-garage.tech/cases/baza-znaniy/',
        'https://ai-garage.tech/cases/transkribator/',
        'https://ai-garage.tech/cases/ii-prodazhi/',
      ],
    }),
  ],
});
