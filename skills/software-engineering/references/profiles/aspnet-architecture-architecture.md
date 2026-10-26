# Architecture contract

Baseline: uploaded Template-master.zip. .NET 10, ASP.NET Core, EF Core SQL Server 10.0.8, React 19, TypeScript, Vite 7, React Router 7, Blazor. These are source versions, not a claim about latest or recommended releases.

| Path under src/App.Server | Responsibility | Boundary |
| --- | --- | --- |
| Domain/Common, Entities, Enums, Events, Exceptions | Domain model and invariants | No EF, HTTP, UI or Infrastructure dependency |
| Application/DTOs, Interfaces, Mapping, Services, UseCases, Validators, AI | Contracts, validation, orchestration | Depend on Domain; use ports rather than Infrastructure implementations |
| Infrastructure/Data/Configurations, Migrations | SQL Server DbContext, mappings and migrations | Implement Application ports; no SQL in controllers |
| Infrastructure/Persistence | Persistence adapters if needed | Keep one authoritative AppDbContext in Data |
| Infrastructure/Authentication, Authorization | Authentication providers and policy implementation | Enforce authorization on server |
| Infrastructure/AI, ExternalServices, Notifications | Provider adapters and delivery | Secrets on server; do not claim configured integrations |
| Controllers | /api/v1 HTTP boundary | Thin DTO-based endpoints invoking Application |
| ClientApp/src | React UI | HTTP API only; no database/server code |
| Components | Blazor views | Shared Application services, identity and database |
| Extensions | DI and request pipeline | Keep Program.cs small |
| HealthChecks | Liveness/readiness | Readiness checks SQL, liveness does not |
| Middleware, Security | Cross-cutting request and security behavior | No business use cases |
| BackgroundJobs | Hosted work | Scope DbContext per operation; cancellation and idempotency |
| Storage | Storage coordination | No public unrestricted upload paths |
| wwwroot | Published static assets | Built React assets; no secrets |

Production: one ASP.NET Core process serves API, Blazor and React. Development: Vite may run separately with /api proxy to the ASP.NET host. Keep React browser routes and /blazor route ownership explicit. Unknown /api requests must return a real 404 rather than React HTML.

Top level: solution, src, tests (unit/integration), scripts, docs, CI. Preserve all original architectural folders. Add feature files inside their owning layer. Introduce new folders only when justified by actual scope.
