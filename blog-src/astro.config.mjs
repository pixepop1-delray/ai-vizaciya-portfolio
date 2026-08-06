// @ts-check
import { defineConfig } from 'astro/config';

// Blog builds standalone (base "/") and the build output gets copied into
// /blog at the repo root by the GitHub Actions workflow — this keeps the
// Astro project itself portable (works locally, previews cleanly, and
// survives a future move to a custom domain without base-path surgery).
export default defineConfig({
  outDir: './dist',
  build: {
    format: 'directory',
  },
});
