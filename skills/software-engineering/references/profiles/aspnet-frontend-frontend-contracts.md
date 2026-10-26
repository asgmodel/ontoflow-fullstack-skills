# Frontend integration

Use relative /api/v1 URLs in production. Vite development uses a proxy to the actual ASP.NET HTTP development port (source: 64751); update both when ports change. A development proxy is not a second backend. Never put SQL/provider credentials into client build variables.

Wrap fetch with typed contracts, explicit non-2xx handling, cancellation and safe error messages. Handle empty 204 responses without parsing JSON. Send appropriate credentials and CSRF token for cookie sessions; do not invent a token header the backend does not validate. Verify logout invalidates server session and refresh restores real session state. Check ownership on server.

React owns normal browser paths, Blazor owns /blazor and intentionally assigned descendants. Reserve /api, /health and /_framework from SPA fallback. Deep links must work after publish; unknown API paths must return 404 rather than index.html. Register Blazor and React on the same host and use shared Application services; do not duplicate business logic in Razor components.

Use accessible labels, keyboard focus, semantic HTML and visible loading/error states. Preserve requested design; do not add arbitrary colors or a new design system. If bilingual/theme scope is requested, cover Arabic RTL and English LTR, light/dark, mobile/desktop, long labels and empty states. Keep text in centralized dictionaries, avoid hardcoded language fragments. Use CSS logical properties and reduced-motion support where relevant.

First setup: npm install creates package-lock.json; inspect and commit it. Repeated setup/CI: npm ci. Run npm run lint and npm run build. No fabricated dependency versions or lockfile hashes. Check frontend build artifacts actually reach dotnet publish output on a clean checkout, not only after local warm builds.
