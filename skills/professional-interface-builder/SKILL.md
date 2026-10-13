---
name: professional-interface-builder
description: Design, rebuild, and production-integrate polished product interfaces across web projects. Use for complete UI work, frontend migrations, or API-connected portals—especially Mohawer, Mihani, Mohassel, or similar systems requiring responsive mobile/desktop layouts, light/dark themes, Arabic/English RTL/LTR, separated roles and portals, real backend data, and evidence-based validation.
---

# Professional Interface Builder

## Outcome

Deliver a coherent product interface that can be maintained and reused across projects. Treat visual quality, complete page coverage, real data flow, security, accessibility, and truthful verification as one job. Produce working routes and states, not a collection of attractive mockups.

## Operating contract

- Inspect the repository and the user's supplied design before editing. Preserve an approved UI's visual language, layout, colors, typography, copy hierarchy, and interaction model unless the user explicitly asks for a redesign.
- Treat the existing backend, database, and API contracts as authoritative when integrating an existing product. Keep the frontend in its existing boundary (for example `ClientApp`) and do not add a parallel Express, Firebase, JSON, or mock backend unless explicitly requested.
- Remove fake core data, static fixtures, and placeholder success paths. Use the real server for business data and operations. Restrict browser storage to presentation preferences such as theme or language unless the product specification explicitly permits more.
- Keep one canonical component tree. Consolidate duplicates instead of creating a second `components` folder or parallel versions of a page.
- Keep headings and labels concise by default (often two words or fewer), but never sacrifice clarity, legal meaning, or accessibility to satisfy a word count.
- Never claim that an external identity, payment, messaging, AI, or government integration is live without a configured provider and a successful test. Use an explicit adapter boundary and report blocked external prerequisites.

## Workflow

### 1. Inspect before designing

Classify the request as a new product, a visual rebuild, a frontend migration, or a full integration. Inventory the framework, package manager, entry points, routes, layouts, components, assets, environment variables, API clients, controllers/DTOs, database models, and existing tests. Run `scripts/project_audit.py` against the source tree when available; keep its report outside the product unless the user asks to commit it.

Record the constraints that must not drift: approved screens, existing layer boundaries, supported languages, role names, authentication providers, and required user journeys. Use the latest explicit requirement when earlier artifacts conflict, and stop to clarify only when the conflict changes data ownership, security, or destructive behavior.

### 2. Map the product

Create a page and role matrix before implementation. Separate individual/professional, business/organization, candidate/customer, and administrator experiences when the domain needs them. For every route, record its purpose, allowed roles, data source, primary action, empty state, loading state, failure state, session-expiry behavior, and mobile layout.

Treat the matrix as a coverage contract: every required screen, dialog, form, upload, report, and completion state must have an owner and an implementation path. Do not silently drop a page because it is absent from a starter template.

### 3. Establish the visual system

Read `references/design-system.md` when creating or changing the visual language. Define tokens before styling individual screens: semantic colors, typography, spacing, radii, elevation, borders, motion, focus rings, and breakpoints. Use a restrained palette and a small font set. Define light and dark values from the same semantic token names so components do not contain hard-coded theme branches.

Support Arabic and English as first-class layouts: translate interface copy, switch `dir` between `rtl` and `ltr`, mirror directional icons and spacing where appropriate, and test long Arabic labels and mixed numerals. Make the same routes work on narrow phones, tablets, and desktop; do not treat mobile as a scaled desktop.

### 4. Build the foundation, then the journeys

Implement the app shell, navigation, route guards, typography, theme and locale providers, form primitives, feedback components, data tables/cards, modal/drawer patterns, and error boundaries first. Reuse these primitives across pages and keep page-specific logic near its route or feature boundary.

Implement complete journeys in user order: entry/authentication, role selection or portal landing, primary work, detail/edit flows, uploads or analysis, notifications/reports, and billing or administration when required. Include success, validation, empty, loading, error, offline, expired-session, and duplicate-submission states. A disabled control must explain why it is disabled.

### 5. Connect the real system

Read `references/product-integration.md` for existing-project integrations. For each user action, trace:

`component → feature service → HTTP client → endpoint → controller/handler → DTO/validation → application service → domain/infrastructure → database`

Align request and response types with the server; do not infer fields from mock data. Centralize authentication, request cancellation, retries, error normalization, and cache invalidation. Enforce authorization on the server and mirror it in the UI for clarity. Keep secrets out of source, bundles, logs, and URLs.

Use server-backed sessions or the project's established secure token strategy. For Google OAuth, Nafath, Absher, payment, email, telephony, or AI providers, implement the real callback/webhook and configuration contract when credentials and provider access exist; otherwise leave a clearly labeled integration boundary and mark it externally blocked rather than simulating success.

For invitation or candidate links, enforce server-side expiry, single use, ownership, and post-completion invalidation where the domain requires it. Protect cross-tenant data, administrator scope, uploads, and report downloads.

### 6. Seed and migrate safely

When a project needs demonstration or development data, add an idempotent, development-only seed that follows the domain schema and never bypasses authentication in production. Create or update migrations only after checking the existing database model and naming conventions. Keep seed credentials and provider secrets out of the repository.

### 7. Verify in layers

Read `references/qa-and-evidence.md` before final verification. Run the checks supported by the environment: formatter/linter, TypeScript or type checks, unit/component tests, frontend build, backend build, migration validation, API tests, and browser or end-to-end journeys. Inspect rendered pages at phone and desktop widths in both themes and both directions. Verify keyboard navigation, focus visibility, contrast, labels, announcements, reduced motion, and zoom/reflow.

Test failure paths deliberately: invalid input, empty data, slow or failed requests, expired sessions, permission denial, disconnected network, repeated clicks, upload failure, and stale data. Check that no required flow still depends on mock data, accidental `localStorage`, or a hidden development bypass.

When a check exposes a defect, repair the smallest correct layer, rebuild or rerun the affected checks, and record the before/after evidence. Do not stop at a written recommendation when the requested scope includes implementation.

Report evidence using three honest states:

- **Verified** — the check actually ran and passed in this environment.
- **Structurally validated** — source and contract inspection support the result, but the required runtime or external service was unavailable.
- **Externally blocked** — a provider, credential, database, SDK, or runtime prerequisite prevented the check.

Never turn a structural check into a claim of live integration.

### 8. Hand off a maintainable result

Summarize the page/role coverage, design tokens and themes, integration map, migrations/seed, tests run, and any blocked prerequisites. Mention changed files and remaining actions. Leave the project buildable, with no generated audit reports, screenshots, or temporary credentials committed unless requested.

## Decision rules for common project types

- **Approved frontend replacing an old one:** keep the approved frontend's appearance and page behavior; adapt data access and routing around it. Clean unused code only after proving it is not imported or required.
- **Existing layered backend (such as ASP.NET Core + EF Core + SQL Server):** preserve the Domain/Application/Infrastructure/Data/Controllers split and validate the frontend-to-database path instead of rebuilding it.
- **New frontend with no API yet:** design the API contract and typed client boundary first. A temporary adapter is allowed only when the user explicitly requests a prototype; label it as non-production.
- **Multiple portals:** give each portal its own route guard, navigation model, empty states, and data scope while sharing the design system and primitives.
- **Locked visual style:** do not add random cards, colors, icons, gradients, or pages merely to fill space. Prefer hierarchy, spacing, and meaningful states.

## Reusable artifacts

Maintain these artifacts during substantial work, in the project or scratch area as appropriate:

1. UI inventory and page/role matrix.
2. Semantic design-token map with light/dark and RTL/LTR notes.
3. Endpoint/DTO/page-action contract map.
4. State and permission matrix.
5. Verification report with evidence and blocked prerequisites.

Use `references/design-system.md` for visual decisions, `references/product-integration.md` for architecture and data flow, and `references/qa-and-evidence.md` for coverage and evidence. Use `scripts/project_audit.py` for a repeatable source-tree audit.
