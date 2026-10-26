# Optional ASP.NET single-host profile

Select `aspnet-single-host` only for a chosen scaffold or a compatible existing
project. Retain other projects' native technologies. The included scaffold has
one ASP.NET host with folder-based Domain/Application/Infrastructure boundaries,
EF Core SQL Server, React TypeScript/Vite and Blazor. Inspect inherited manifests
and runtime availability before use; do not silently change versions.

Generate only into a new destination:

```sh
python <engineering-root>/scripts/scaffold.py --output <new-directory> --name MyProduct
```

The scaffold has no business entities or invented authentication. Scaffold file
creation is separate from build, database and runtime verification. Initialize
OntoLink using the current external installed coordinator before phase work; do not copy its package into the application.
Read [architecture](profiles/aspnet-architecture-architecture.md),
[source audit](profiles/aspnet-architecture-source-audit.md),
[backend](profiles/aspnet-backend-backend-contracts.md),
[frontend](profiles/aspnet-frontend-frontend-contracts.md) and
[verification](profiles/aspnet-verification-verification.md) as needed.
