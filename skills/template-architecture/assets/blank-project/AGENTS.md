# Template project contract

Use the existing single ASP.NET Core host. Domain owns invariants; Application owns DTOs, ports and use cases; Infrastructure implements ports and SQL Server persistence. Controllers are thin /api/v1 boundaries. React lives in ClientApp; Blazor lives in Components; both share this host. Never create a backend in ClientApp. Keep secrets on the server.

This is a blank scaffold, not an implemented product. Do not invent business modules, users or demo data. Do not claim authentication, SQL schema or providers work without implementation and evidence.

Before modifying: read relevant source, identify owning layer, preserve current design and user requirements. Before handoff: run available build/tests/publish checks and report VERIFIED / NOT VERIFIED / BLOCKED BY ENVIRONMENT. Do not modify production data as a test.

Setup: .NET 10 SDK, compatible Node/npm, SQL Server when data is needed. Run npm install in src/App.Server/ClientApp once, review and retain the lockfile, then npm ci for subsequent installs. Run npm run build, then dotnet build Template.slnx and dotnet test Template.slnx. Run dotnet publish src/App.Server/App.Server.csproj -c Release -o artifacts/publish. SQL configuration uses ConnectionStrings__AppDb. No .env auto-loader is configured. Add migrations after defining real entities; production automatic migration is disabled.
