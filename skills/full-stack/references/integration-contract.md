# Cross-layer integration contract

Before implementation, extract existing contracts and record only decisions needed for the requested feature. Keep this in working notes or existing project documentation; do not add a duplicate documentation framework for a small fix.

| Concern | Required decision | Proof of integration |
| --- | --- | --- |
| Feature | User action and acceptance criterion | Relevant user journey succeeds |
| Route | Method, path, API version and page | Client calls the implemented server route |
| Data | Request/response DTOs, nullability, IDs, dates and paging | Frontend types match serialized server response |
| Validation | Input bounds and error shape | Invalid request produces expected server and UI behavior |
| Identity | Session strategy, CSRF and owner source | Anonymous and cross-owner requests rejected |
| Storage | Entity, mapping, migration and transaction scope | Saved state persists in a fresh scope/reload |
| UX | Loading, empty, error and success states | UI does not show false success on failed request |
| Provider | Real configuration and timeout/failure behavior | Actual provider check, or explicit missing configuration |
| Delivery | Build artifact and runtime routes | Assets present; direct routes work when runtime tested |

Example: an owner-scoped notes feature needs the real authenticated user as owner, not an ownerId trusted from the browser. Add only requested fields. Align create/list/update/delete DTOs across API and client. Test anonymous access, cross-owner lookup/update/delete, validation and persistence. A 200 response with a mock array does not prove integration.

For large requests, track one row per page/action with its API, backend use case, data dependency and verification status. Check all requested rows before calling the work complete. A blocked row remains blocked even when all other rows pass. After an API contract changes, revisit all affected consumers, validation and tests.

Completion requires actual requested code, connected layers, appropriate verification and honest remaining setup notes. Files generated, code reviewed, build passed, SQL tested and deployed are different claims: report only those supported by evidence.
