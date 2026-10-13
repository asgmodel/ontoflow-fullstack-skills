import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import { fileURLToPath } from 'node:url';
export default defineConfig({
  plugins: [react()],
  build: { outDir: fileURLToPath(new URL('../wwwroot', import.meta.url)), emptyOutDir: true },
  server: { port: 5173, proxy: { '/api': 'http://localhost:64751' } }
});
