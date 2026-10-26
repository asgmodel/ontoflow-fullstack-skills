# Source assessment and template scope

The upload is a starter, not a complete product. Repeated README.md/PROMPT.md/promet.md files were consolidated into focused skill instructions.

Observed in source: single .NET host, SQL Server registration, empty layer folders, Users/Notifications example models and mappings, informational API, React placeholder dashboard, Blazor placeholder, health endpoints, development migration initializer, publish hook and CI.

Not implemented in source: full authentication, Google OAuth, permission checks, audit system, AI provider, real notification delivery, feature services, initial migration, seed data, meaningful integration tests. Test bodies only asserted true; no global Xunit import was present. Do not turn these into completion claims.

Blank asset changes: remove User/Notification models and mappings, remove placeholder tests and repeated prompts, empty DbContext, blank React/Blazor pages, clear committed connection strings, disable automatic migration by default, complete Razor imports, add API dev proxy, use ESM-safe Vite path, keep SPA fallback from swallowing API/health/framework paths, include fresh React output explicitly in publish, use explicit Xunit imports for substantive host tests. Preserve architectural directories with .gitkeep.

The uploaded archive has no npm lockfile. Generate and inspect package-lock.json with npm install on first setup, commit it, then use npm ci. Build/publish intentionally require that setup; do not manufacture a lockfile. Target framework/packages are retained from source, not upgraded.

The template is not production-ready by itself. It has no authentication or protected business routes and no SQL schema. Add migrations only after real entities are specified. Runtime build, SQL and browser checks require the corresponding tools and services.
