# Backend engineering

Implement business rules and use cases within the current architecture. Define
input/output DTOs and validation before wiring consumers. Keep transport handlers
thin, normalize errors and propagate cancellation/timeouts through I/O.

Enforce authentication, permission checks, tenant/owner scoping and state
transitions on the server. Derive identity from the validated session; never
trust client-supplied role or owner IDs. Use appropriate CSRF defenses for the
chosen session model. Keep secrets on the server and redact sensitive logs.

Use real persistence and providers for business operations. Define transaction
boundaries, concurrency handling and idempotency for retries, callbacks and
repeated writes. Bound external requests and retries; check response signatures
when the provider requires them. Report absent credentials/services explicitly.

Verify successful use cases, invalid input, anonymous/wrong-role/cross-owner
attempts, failure paths and persistence across fresh scopes. Use native commands
and versions. For the selected ASP.NET profile additionally read
[ASP.NET backend contracts](profiles/aspnet-backend-backend-contracts.md).
