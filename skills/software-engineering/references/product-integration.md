# Product integration playbook

Use this reference when a UI must become a real product surface or when replacing an existing frontend. Keep the existing server and data architecture authoritative unless the user explicitly requests architectural change.

## Boundary and ownership

For layered applications such as Mohawer, preserve the established `Domain`, `Application`, `Infrastructure`, `Data`, `Controllers`/API, and `ClientApp` boundaries. The intended path is:

`ClientApp → API client → controller/handler → DTO and validation → application service → domain/infrastructure → EF/repository → database`

Do not introduce Express, Firebase, a JSON database, or a second source of truth inside the frontend. A frontend migration changes presentation and client access, not ownership of business rules. Keep authorization, validation, state transitions, idempotency, and concurrency rules on the server.

## Page-to-contract map

Create a row for every route and primary action:

| Route/feature | Role/tenant | Read endpoint | Write endpoint | Request/response types | States | Security |
| --- | --- | --- | --- | --- | --- | --- |
| Example | Business admin | `GET …` | `POST …` | `FeatureDto` | loading/empty/error/success | owner/admin |

Resolve every field from the server DTO or schema. If the UI wants a field that does not exist, add a deliberate contract/migration change or redesign the presentation; do not fabricate it in a mock object.

## Authentication and authorization

- Use the project's secure server-backed session or token strategy. Centralize login, refresh, logout, session-expiry handling, and unauthorized redirects.
- Enforce role and tenant checks on the server. UI route guards are an early feedback layer, not a security boundary.
- Keep individual/professional, business/organization, candidate/customer, and administrator data scopes separate where the product requires them. Test that a user cannot open another portal by editing a URL.
- Do not ship demo/admin bypasses, default secrets, tokens, or provider credentials. Read secrets from the configured environment or secret manager.
- For OAuth or government identity (Google, Nafath, Absher), implement the provider's real redirect/callback and verification contract. Without provider access, show the integration as pending or externally blocked; never pretend that a local button is a live verification.

## Request lifecycle

Each data operation needs a consistent lifecycle:

1. Validate input before sending and again on the server.
2. Show a pending state and prevent accidental duplicate submission.
3. Cancel or ignore stale requests when the route or query changes.
4. Normalize network, validation, authorization, conflict, and server errors into useful user messages.
5. Invalidate or update affected cached data after a successful mutation.
6. Preserve unsaved input where safe, and explain recovery after a session loss or disconnection.

Use idempotency keys or server-side state checks for operations that can be retried, charged, sent, or completed more than once.

## Domain workflows

For interview/recruitment products such as Mohawer, map the entire lifecycle instead of only the dashboard: accounts and roles, jobs and templates, invitations and participants, interviews and sessions, questions/answers/evaluations, CV and job-description upload/analysis, reports, plans/subscriptions, invoices/quotas, email, and secure single-use candidate links. Keep each transition server-authoritative and show the state in the UI.

For professional/business portals such as Mihani or Mohassel, model the entry flow, account type, organization membership, verification or collection workflow, records, alerts, reports, and admin scope explicitly. Share primitives and tokens, but do not merge data or navigation merely because the screens look similar.

## Files, AI, and external services

- Upload through the real API with size/type validation, progress, cancellation, retry policy, and a safe failure state. Do not expose storage credentials or trust a client-provided MIME type.
- Represent AI work as an observable server job with pending, completed, failed, and retryable states. Never display invented results when a job has not completed.
- For email, payment, telephony, webhooks, or government services, keep provider-specific logic in a server adapter. Validate signatures, replay protection, ownership, and event ordering on the server.

## Seed and migration rules

Use idempotent development-only seeds that match the current domain model and exercise each portal and important state. Never use seed data to bypass production authentication. Run migrations against a disposable or explicitly approved database, inspect the generated SQL, and document rollback implications.

## Migration and cleanup

When replacing an old frontend:

1. Inventory imports and routes before deleting anything.
2. Copy the approved visual system and assets without silently changing them.
3. Move data access behind one typed client/service layer.
4. Replace fixture calls one feature at a time and verify the server contract.
5. Remove unused files only after a build, route scan, and import search prove they are unreferenced.
6. Confirm there is one canonical `components` tree and no duplicate route implementation.

Keep a list of intentionally deferred integrations and mark each as verified, structurally validated, or externally blocked.
