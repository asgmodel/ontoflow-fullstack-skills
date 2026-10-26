# Backend contracts

## Data
Keep Domain independent of EF and transport. Put interfaces in Application/Interfaces and implementations in Infrastructure. Configure required lengths, keys, foreign keys, unique constraints and delete behavior explicitly. Translate expected conflicts to stable client responses, avoid leaking SQL exceptions. Scope transactions to a use case; protect concurrent updates when needed. Register mappings from the server assembly. Keep one DbContext under Infrastructure/Data; do not duplicate it under Persistence.

Run EF commands from the server directory so the design-time factory finds configuration. Supply ConnectionStrings__AppDb from the environment. Add migrations only after defining actual domain entities. Review destructive diffs before applying to real data. Keep automatic production migrations and production seeding disabled. Requested seed data must be idempotent, dependency ordered and isolated from production. Never hardcode administrator passwords.

## API
Use /api/v1, DTOs and a documented error shape (ProblemDetails by default). Return correct 400/401/403/404/409 responses. Bound page sizes and validate filters. Define API changes before UI consumption. Register scoped services; avoid singleton DbContext. Use async database/provider I/O and structured logs without secrets or raw sensitive documents.

## Authentication and authorization
The source only has placeholder auth configuration, not a working auth system. Select existing session strategy; otherwise prefer same-origin secure cookies for browser-only apps when requirements fit. Implement HttpOnly/Secure cookie and CSRF protection for state-changing API requests; merely calling UseAntiforgery is not complete API protection. Register authentication and authorization before mapping protected endpoints and order middleware correctly. For JWT, validate issuer, audience, signature and lifetime, keep signing secrets server-side, define revocation/refresh policy. Never invent OAuth success. Use provider middleware, real callback registration and state/nonce checks. Prevent unsafe account linking. Enforce permissions and ownership per use case; hiding a button is not authorization.

## AI, notifications, audit and jobs
Put AI contracts in Application/AI and provider SDK usage in Infrastructure/AI. Define timeout, cancellation, bounded retries, usage limits, safe logging and streaming termination. Treat uploaded content and model output as data rather than authority. Validate structured output before database mutation; require normal authorization for AI-triggered actions.
Persist notifications with recipient ownership, read state and delivery status. Keep provider delivery failure distinct from database persistence. Write audit events with actor/action/target/outcome, exclude secrets. Use BackgroundJobs with scoped services, cancellation, idempotency and retry bounds. Store uploads behind validated size/type/name rules; do not serve arbitrary user paths publicly.

## Meaningful checks
Test invariant rejection, duplicate creation, unauthorized and cross-user access, successful authorized operation, failed provider call, and database persistence after a new scope. Use a disposable SQL Server for SQL-specific constraints and migrations; EF InMemory does not prove SQL Server correctness. Report absent database/provider credentials as blocked, never substitute fake success.
