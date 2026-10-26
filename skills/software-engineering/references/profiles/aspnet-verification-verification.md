# Verification matrix

Run from generated project root unless indicated. Replace App.Server/solution with actual generated names.

| Gate | Action | Required evidence |
| --- | --- | --- |
| Tooling | python --version; dotnet --info; node --version; npm --version | Actual available tools, missing tools marked blocked |
| Client setup | In ClientApp: npm install once when lock absent; otherwise npm ci | Exit code and reviewed lockfile |
| Client | npm run lint; npm run build | Successful type check and emitted assets |
| Server | dotnet restore <solution>.slnx; dotnet build <solution>.slnx -c Release --no-restore | Successful clean build |
| Tests | dotnet test <solution>.slnx -c Release --no-build | Meaningful behavior assertions, count and failures |
| Publish | dotnet publish src/App.Server/App.Server.csproj -c Release -o artifacts/publish | Server output plus wwwroot/index.html and referenced assets |
| SQL | EF migrations against a disposable real SQL Server | Schema created/upgraded, constraints and persistence verified |
| Runtime | Start published server with supplied config | React route and /blazor accessible; direct URL refresh works |
| Health | GET /health/live; /health/ready | Live independent of SQL; ready 503 without DB and 200 with working DB |
| Routing | GET nonexistent /api/v1 route and nonexistent client route | API 404 with no SPA HTML; client route handled by client |
| Security | Anonymous, wrong-role and cross-owner requests | 401/403 or deliberate 404; no data leakage |

For blank template, authentication and domain tests are not applicable until features are requested. Existing host tests verify liveness and API fallback only; they do not prove SQL, browser rendering, identity or publishing.

Inspect source versions before installing tools; use matching SDK/provider tooling. Do not silently switch SQL provider to make tests pass. Do not call readiness healthy merely because the process started. Do not accept Assert.True(true), hidden UI controls or fake seeded success as evidence.

Report: Scope; Changed paths; VERIFIED (command/result); NOT VERIFIED (not run); BLOCKED BY ENVIRONMENT (missing tool/service/credentials); Remaining product configuration. Include actual failing output in a concise, secret-free form.
