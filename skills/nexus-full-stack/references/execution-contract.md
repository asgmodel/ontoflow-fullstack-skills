# Execution and handoff contract

| Boundary | Required contract | Proof |
| --- | --- | --- |
| Product | Role, action, acceptance criterion, requested scope | Requested journey completes |
| Architecture | Existing stack or explicit Template profile; layer ownership | No forbidden layer dependency |
| API | Method, route, version, DTOs, nullability, dates, paging, status/errors | Actual response matches consumer types |
| Identity | Session, CSRF, permissions and server-derived ownership | Anonymous/wrong-role/cross-owner attempts rejected |
| Data | Entity, constraints, concurrency and transaction; migration if changed | Fresh-scope persistence; real SQL fresh/upgrade checks |
| UI | Loading, empty, error, retry, success, permissions; requested locale/theme | Real browser interaction, direct route and refresh |
| Providers | Actual configuration, timeout, cancellation and retry/idempotency | Real call or explicit configuration blocker |
| Publish | Server bundle, static assets and reserved route ownership | Clean publish and published-host smoke checks |
| Operations | Redacted logs, bounded metrics and correlated traces as needed | Actual signals answer operational questions |

Template profile: one ASP.NET host serves API, React and Blazor; one SQL Server DbContext; folder-based Domain/Application/Infrastructure; thin Controllers; production React in wwwroot. Development Vite proxy is permitted. Preserve source versions and use the installed Template scaffold rather than an invented replica.

Existing-stack profile: use the existing languages, framework, persistence and directory conventions. The same cross-layer acceptance and evidence requirements apply. Do not route to Template implementation adapters for a Node/Flutter/other existing application.

No business mocks, fake authentication or browser-stored business records as substitutes for integration. Keep secrets server-side. UI restrictions cannot replace server authorization. Runtime/deployment checks remain unverified when unavailable. Mark conditional gates not applicable with a reason; never silently omit them.
