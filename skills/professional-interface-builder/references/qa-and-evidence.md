# QA and evidence playbook

Use this reference before handoff. Adapt commands to the project's stack and report what actually ran.

## Coverage matrix

Keep one row per route, dialog, or important state. Minimum columns:

| Surface | Persona/role | Happy path | Validation | Empty/loading/error | Permission/session | Phone + desktop | Light + dark | RTL + LTR | Evidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Route or dialog | Allowed scope | Action and result | Invalid input | Failure and recovery | Denied/expired | Checked | Checked | Checked | Command/screenshot/test |

An unchecked cell is a gap, not an assumption. Include entry/authentication, portal selection, primary CRUD, uploads/analysis, notifications/reports, billing/admin, and completion flows when they are in scope.

## Verification layers

Run the strongest available layer in this order:

1. **Static:** formatter/linter, type check, route/import scan, duplicate component scan, forbidden mock/localStorage scan, dependency and secret scan.
2. **Build:** frontend production build and, when present, backend build and generated-client checks.
3. **Contract:** compare every client request/response with controller/handler DTOs, validation, migrations, and database schema.
4. **Unit/component:** reducers, validators, permissions, state transitions, and critical shared components.
5. **API/integration:** authenticated happy and failure paths, tenant isolation, idempotency, uploads, and server jobs.
6. **Browser/E2E:** real route journeys at phone/desktop widths, both themes, both directions, and after refresh/session expiry.
7. **Visual/accessibility:** inspect screenshots or a live browser; test keyboard, screen-reader names, focus, contrast, zoom, reflow, and reduced motion.

Do not skip a lower layer silently when a higher layer is unavailable; state the limitation.

## Failure-path checklist

Exercise invalid and missing fields, slow responses, network loss, 401/403/404/409/422/5xx responses, empty collections, stale detail pages, expired sessions, permission changes, repeated clicks, double uploads, cancellation, unsupported files, and server-side job failure. Ensure the UI explains what happened, preserves safe input, and offers a valid next action.

## Security checks

- Search source and built assets for secrets, private keys, bearer tokens, connection strings, and debug bypasses.
- Confirm server-side authorization and tenant filtering for every read/write/download route.
- Confirm output escaping, safe file handling, CSRF/CORS/session settings, rate limits where relevant, webhook signature and replay checks, and audit logging for sensitive transitions.
- Verify error messages do not reveal stack traces, tokens, internal paths, or another tenant's data.

## Visual review

Compare against the approved reference at consistent viewport sizes. Check hierarchy, alignment, spacing rhythm, typography, control states, icon consistency, image cropping, scroll behavior, tables, dialogs, and long content. Review Arabic and English separately; direction bugs often hide when only short Latin labels are tested.

## Evidence language

Use these exact categories in reports:

- **Verified:** executed in this environment and observed to pass.
- **Structurally validated:** source, types, contracts, or static inspection support it, but live execution was unavailable.
- **Externally blocked:** a missing runtime, database, credential, SDK, provider, or network dependency prevented the check.

Include the command, environment limitation, sample route or test case, and date for material claims. A successful static build does not prove API, database, OAuth, Nafath, Absher, payment, email, AI, or telephony behavior.

## Release gate

Handoff only when required routes exist, no required flow is a placeholder, the component tree is canonical, API contracts are aligned, role/tenant isolation is tested or explicitly blocked, themes/locales/directions render, failure states are usable, secrets are absent, and the evidence report distinguishes verified work from structural and external limitations.
