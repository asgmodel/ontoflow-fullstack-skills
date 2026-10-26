# Necessary file inventory

The two installed packages contain runtime instructions, ontologies and selected resources. Repository tests, CI and documentation support maintenance. Project state, generated context, proof logs, virtual environments and temporary work are excluded from the distribution inventory.

`MANIFEST.json` records the exact source paths and SHA-256 values; it excludes itself to avoid a hash cycle. Regenerate this list and the manifest with `python scripts/manifest.py --write`.

| File | Purpose |
| --- | --- |
| `.github/workflows/validate.yml` | Continuous validation workflow. |
| `.gitignore` | Distribution documentation, catalog, provenance or configuration. |
| `MANIFEST.json` | Distribution documentation, catalog, provenance or configuration. |
| `README.md` | Distribution documentation, catalog, provenance or configuration. |
| `THIRD_PARTY_NOTICES.md` | Distribution documentation, catalog, provenance or configuration. |
| `catalog.json` | Distribution documentation, catalog, provenance or configuration. |
| `docs/architecture.md` | Distribution documentation, catalog, provenance or configuration. |
| `docs/file-inventory.md` | Distribution documentation, catalog, provenance or configuration. |
| `scripts/check.py` | Runtime operation, maintenance validator or source inventory tool. |
| `scripts/compile_lifecycle.py` | Runtime operation, maintenance validator or source inventory tool. |
| `scripts/manifest.py` | Runtime operation, maintenance validator or source inventory tool. |
| `scripts/run_tests.py` | Runtime operation, maintenance validator or source inventory tool. |
| `skills/ontolink-skills/.rule/ONTOLOGY-FIRST.md` | Distribution documentation, catalog, provenance or configuration. |
| `skills/ontolink-skills/.rule/ontolink.py` | Distribution documentation, catalog, provenance or configuration. |
| `skills/ontolink-skills/SKILL.md` | Skill identity, trigger metadata or operating entrypoint. |
| `skills/ontolink-skills/agents/openai.yaml` | Skill identity, trigger metadata or operating entrypoint. |
| `skills/ontolink-skills/assets/catalog.json` | Distribution documentation, catalog, provenance or configuration. |
| `skills/ontolink-skills/assets/ontolink.owl` | Authoritative ontology model or explicitly labelled example graph. |
| `skills/ontolink-skills/assets/ontolink.ttl` | Derived ontology projection or validation shape; no project state. |
| `skills/ontolink-skills/assets/package-source.json` | Distribution documentation, catalog, provenance or configuration. |
| `skills/ontolink-skills/assets/shapes.ttl` | Derived ontology projection or validation shape; no project state. |
| `skills/ontolink-skills/references/execution-contract.md` | On-demand execution, engineering or evidence contract. |
| `skills/ontolink-skills/references/knowledge-model.md` | On-demand execution, engineering or evidence contract. |
| `skills/ontolink-skills/references/lifecycle.md` | On-demand execution, engineering or evidence contract. |
| `skills/ontolink-skills/references/project-intelligence.md` | On-demand execution, engineering or evidence contract. |
| `skills/ontolink-skills/references/quickstart.md` | On-demand execution, engineering or evidence contract. |
| `skills/ontolink-skills/references/record-contract.md` | On-demand execution, engineering or evidence contract. |
| `skills/ontolink-skills/references/uncertainty.md` | On-demand execution, engineering or evidence contract. |
| `skills/ontolink-skills/scripts/context_compiler.py` | Runtime operation, maintenance validator or source inventory tool. |
| `skills/ontolink-skills/scripts/mediator.py` | Runtime operation, maintenance validator or source inventory tool. |
| `skills/ontolink-skills/scripts/project_indexer.py` | Runtime operation, maintenance validator or source inventory tool. |
| `skills/ontolink-skills/scripts/project_intelligence.py` | Runtime operation, maintenance validator or source inventory tool. |
| `skills/ontolink-skills/scripts/project_setup.py` | Runtime operation, maintenance validator or source inventory tool. |
| `skills/ontolink-skills/scripts/rdf_store.py` | Runtime operation, maintenance validator or source inventory tool. |
| `skills/ontolink-skills/scripts/retrieval.py` | Runtime operation, maintenance validator or source inventory tool. |
| `skills/ontolink-skills/skills/ontolink-architecture/SKILL.md` | Bundled lifecycle phase procedure, metadata or outcome contract. |
| `skills/ontolink-skills/skills/ontolink-architecture/agents/openai.yaml` | Bundled lifecycle phase procedure, metadata or outcome contract. |
| `skills/ontolink-skills/skills/ontolink-architecture/references/phase-contract.md` | Bundled lifecycle phase procedure, metadata or outcome contract. |
| `skills/ontolink-skills/skills/ontolink-delivery/SKILL.md` | Bundled lifecycle phase procedure, metadata or outcome contract. |
| `skills/ontolink-skills/skills/ontolink-delivery/agents/openai.yaml` | Bundled lifecycle phase procedure, metadata or outcome contract. |
| `skills/ontolink-skills/skills/ontolink-delivery/references/phase-contract.md` | Bundled lifecycle phase procedure, metadata or outcome contract. |
| `skills/ontolink-skills/skills/ontolink-discovery/SKILL.md` | Bundled lifecycle phase procedure, metadata or outcome contract. |
| `skills/ontolink-skills/skills/ontolink-discovery/agents/openai.yaml` | Bundled lifecycle phase procedure, metadata or outcome contract. |
| `skills/ontolink-skills/skills/ontolink-discovery/references/phase-contract.md` | Bundled lifecycle phase procedure, metadata or outcome contract. |
| `skills/ontolink-skills/skills/ontolink-implementation/SKILL.md` | Bundled lifecycle phase procedure, metadata or outcome contract. |
| `skills/ontolink-skills/skills/ontolink-implementation/agents/openai.yaml` | Bundled lifecycle phase procedure, metadata or outcome contract. |
| `skills/ontolink-skills/skills/ontolink-implementation/references/phase-contract.md` | Bundled lifecycle phase procedure, metadata or outcome contract. |
| `skills/ontolink-skills/skills/ontolink-monitoring/SKILL.md` | Bundled lifecycle phase procedure, metadata or outcome contract. |
| `skills/ontolink-skills/skills/ontolink-monitoring/agents/openai.yaml` | Bundled lifecycle phase procedure, metadata or outcome contract. |
| `skills/ontolink-skills/skills/ontolink-monitoring/references/phase-contract.md` | Bundled lifecycle phase procedure, metadata or outcome contract. |
| `skills/ontolink-skills/skills/ontolink-planning/SKILL.md` | Bundled lifecycle phase procedure, metadata or outcome contract. |
| `skills/ontolink-skills/skills/ontolink-planning/agents/openai.yaml` | Bundled lifecycle phase procedure, metadata or outcome contract. |
| `skills/ontolink-skills/skills/ontolink-planning/references/phase-contract.md` | Bundled lifecycle phase procedure, metadata or outcome contract. |
| `skills/ontolink-skills/skills/ontolink-verification/SKILL.md` | Bundled lifecycle phase procedure, metadata or outcome contract. |
| `skills/ontolink-skills/skills/ontolink-verification/agents/openai.yaml` | Bundled lifecycle phase procedure, metadata or outcome contract. |
| `skills/ontolink-skills/skills/ontolink-verification/references/phase-contract.md` | Bundled lifecycle phase procedure, metadata or outcome contract. |
| `skills/software-engineering/SKILL.md` | Skill identity, trigger metadata or operating entrypoint. |
| `skills/software-engineering/agents/openai.yaml` | Skill identity, trigger metadata or operating entrypoint. |
| `skills/software-engineering/assets/engineering-index.json` | Derived ontology projection or validation shape; no project state. |
| `skills/software-engineering/assets/engineering.owl` | Authoritative ontology model or explicitly labelled example graph. |
| `skills/software-engineering/assets/engineering.ttl` | Derived ontology projection or validation shape; no project state. |
| `skills/software-engineering/assets/example-task.json` | Distribution documentation, catalog, provenance or configuration. |
| `skills/software-engineering/assets/queries.rq` | Distribution documentation, catalog, provenance or configuration. |
| `skills/software-engineering/assets/shapes.ttl` | Derived ontology projection or validation shape; no project state. |
| `skills/software-engineering/assets/task.schema.json` | Distribution documentation, catalog, provenance or configuration. |
| `skills/software-engineering/assets/templates/aspnet-react/.env.example` | Optional ASP.NET/React/Blazor scaffold source; copied only when selected. |
| `skills/software-engineering/assets/templates/aspnet-react/.gitattributes` | Optional ASP.NET/React/Blazor scaffold source; copied only when selected. |
| `skills/software-engineering/assets/templates/aspnet-react/.github/workflows/ci.yml` | Optional ASP.NET/React/Blazor scaffold source; copied only when selected. |
| `skills/software-engineering/assets/templates/aspnet-react/.gitignore` | Optional ASP.NET/React/Blazor scaffold source; copied only when selected. |
| `skills/software-engineering/assets/templates/aspnet-react/AGENTS.md` | Optional ASP.NET/React/Blazor scaffold source; copied only when selected. |
| `skills/software-engineering/assets/templates/aspnet-react/Template.slnx` | Optional ASP.NET/React/Blazor scaffold source; copied only when selected. |
| `skills/software-engineering/assets/templates/aspnet-react/docs/architecture/.gitkeep` | Optional ASP.NET/React/Blazor scaffold source; copied only when selected. |
| `skills/software-engineering/assets/templates/aspnet-react/docs/deployment/.gitkeep` | Optional ASP.NET/React/Blazor scaffold source; copied only when selected. |
| `skills/software-engineering/assets/templates/aspnet-react/docs/development/.gitkeep` | Optional ASP.NET/React/Blazor scaffold source; copied only when selected. |
| `skills/software-engineering/assets/templates/aspnet-react/docs/security/.gitkeep` | Optional ASP.NET/React/Blazor scaffold source; copied only when selected. |
| `skills/software-engineering/assets/templates/aspnet-react/scripts/database-add-migration.ps1` | Optional ASP.NET/React/Blazor scaffold source; copied only when selected. |
| `skills/software-engineering/assets/templates/aspnet-react/scripts/database-update.ps1` | Optional ASP.NET/React/Blazor scaffold source; copied only when selected. |
| `skills/software-engineering/assets/templates/aspnet-react/src/App.Server/App.Server.csproj` | Optional ASP.NET/React/Blazor scaffold source; copied only when selected. |
| `skills/software-engineering/assets/templates/aspnet-react/src/App.Server/Application/AI/.gitkeep` | Optional ASP.NET/React/Blazor scaffold source; copied only when selected. |
| `skills/software-engineering/assets/templates/aspnet-react/src/App.Server/Application/DTOs/.gitkeep` | Optional ASP.NET/React/Blazor scaffold source; copied only when selected. |
| `skills/software-engineering/assets/templates/aspnet-react/src/App.Server/Application/Interfaces/.gitkeep` | Optional ASP.NET/React/Blazor scaffold source; copied only when selected. |
| `skills/software-engineering/assets/templates/aspnet-react/src/App.Server/Application/Mapping/.gitkeep` | Optional ASP.NET/React/Blazor scaffold source; copied only when selected. |
| `skills/software-engineering/assets/templates/aspnet-react/src/App.Server/Application/Services/.gitkeep` | Optional ASP.NET/React/Blazor scaffold source; copied only when selected. |
| `skills/software-engineering/assets/templates/aspnet-react/src/App.Server/Application/UseCases/.gitkeep` | Optional ASP.NET/React/Blazor scaffold source; copied only when selected. |
| `skills/software-engineering/assets/templates/aspnet-react/src/App.Server/Application/Validators/.gitkeep` | Optional ASP.NET/React/Blazor scaffold source; copied only when selected. |
| `skills/software-engineering/assets/templates/aspnet-react/src/App.Server/BackgroundJobs/.gitkeep` | Optional ASP.NET/React/Blazor scaffold source; copied only when selected. |
| `skills/software-engineering/assets/templates/aspnet-react/src/App.Server/ClientApp/index.html` | Optional ASP.NET/React/Blazor scaffold source; copied only when selected. |
| `skills/software-engineering/assets/templates/aspnet-react/src/App.Server/ClientApp/package.json` | Optional ASP.NET/React/Blazor scaffold source; copied only when selected. |
| `skills/software-engineering/assets/templates/aspnet-react/src/App.Server/ClientApp/public/.gitkeep` | Optional ASP.NET/React/Blazor scaffold source; copied only when selected. |
| `skills/software-engineering/assets/templates/aspnet-react/src/App.Server/ClientApp/src/api/.gitkeep` | Optional ASP.NET/React/Blazor scaffold source; copied only when selected. |
| `skills/software-engineering/assets/templates/aspnet-react/src/App.Server/ClientApp/src/app/App.tsx` | Optional ASP.NET/React/Blazor scaffold source; copied only when selected. |
| `skills/software-engineering/assets/templates/aspnet-react/src/App.Server/ClientApp/src/app/styles.css` | Optional ASP.NET/React/Blazor scaffold source; copied only when selected. |
| `skills/software-engineering/assets/templates/aspnet-react/src/App.Server/ClientApp/src/auth/.gitkeep` | Optional ASP.NET/React/Blazor scaffold source; copied only when selected. |
| `skills/software-engineering/assets/templates/aspnet-react/src/App.Server/ClientApp/src/components/.gitkeep` | Optional ASP.NET/React/Blazor scaffold source; copied only when selected. |
| `skills/software-engineering/assets/templates/aspnet-react/src/App.Server/ClientApp/src/features/ai/.gitkeep` | Optional ASP.NET/React/Blazor scaffold source; copied only when selected. |
| `skills/software-engineering/assets/templates/aspnet-react/src/App.Server/ClientApp/src/hooks/.gitkeep` | Optional ASP.NET/React/Blazor scaffold source; copied only when selected. |
| `skills/software-engineering/assets/templates/aspnet-react/src/App.Server/ClientApp/src/layouts/.gitkeep` | Optional ASP.NET/React/Blazor scaffold source; copied only when selected. |
| `skills/software-engineering/assets/templates/aspnet-react/src/App.Server/ClientApp/src/main.tsx` | Optional ASP.NET/React/Blazor scaffold source; copied only when selected. |
| `skills/software-engineering/assets/templates/aspnet-react/src/App.Server/ClientApp/src/pages/.gitkeep` | Optional ASP.NET/React/Blazor scaffold source; copied only when selected. |
| `skills/software-engineering/assets/templates/aspnet-react/src/App.Server/ClientApp/src/routes/.gitkeep` | Optional ASP.NET/React/Blazor scaffold source; copied only when selected. |
| `skills/software-engineering/assets/templates/aspnet-react/src/App.Server/ClientApp/src/services/.gitkeep` | Optional ASP.NET/React/Blazor scaffold source; copied only when selected. |
| `skills/software-engineering/assets/templates/aspnet-react/src/App.Server/ClientApp/src/stores/.gitkeep` | Optional ASP.NET/React/Blazor scaffold source; copied only when selected. |
| `skills/software-engineering/assets/templates/aspnet-react/src/App.Server/ClientApp/src/types/.gitkeep` | Optional ASP.NET/React/Blazor scaffold source; copied only when selected. |
| `skills/software-engineering/assets/templates/aspnet-react/src/App.Server/ClientApp/src/utils/.gitkeep` | Optional ASP.NET/React/Blazor scaffold source; copied only when selected. |
| `skills/software-engineering/assets/templates/aspnet-react/src/App.Server/ClientApp/tsconfig.json` | Optional ASP.NET/React/Blazor scaffold source; copied only when selected. |
| `skills/software-engineering/assets/templates/aspnet-react/src/App.Server/ClientApp/vite.config.ts` | Optional ASP.NET/React/Blazor scaffold source; copied only when selected. |
| `skills/software-engineering/assets/templates/aspnet-react/src/App.Server/Components/App.razor` | Optional ASP.NET/React/Blazor scaffold source; copied only when selected. |
| `skills/software-engineering/assets/templates/aspnet-react/src/App.Server/Components/Layout/MainLayout.razor` | Optional ASP.NET/React/Blazor scaffold source; copied only when selected. |
| `skills/software-engineering/assets/templates/aspnet-react/src/App.Server/Components/Pages/BlazorHome.razor` | Optional ASP.NET/React/Blazor scaffold source; copied only when selected. |
| `skills/software-engineering/assets/templates/aspnet-react/src/App.Server/Components/Routes.razor` | Optional ASP.NET/React/Blazor scaffold source; copied only when selected. |
| `skills/software-engineering/assets/templates/aspnet-react/src/App.Server/Components/Shared/.gitkeep` | Optional ASP.NET/React/Blazor scaffold source; copied only when selected. |
| `skills/software-engineering/assets/templates/aspnet-react/src/App.Server/Components/_Imports.razor` | Optional ASP.NET/React/Blazor scaffold source; copied only when selected. |
| `skills/software-engineering/assets/templates/aspnet-react/src/App.Server/Controllers/SystemController.cs` | Optional ASP.NET/React/Blazor scaffold source; copied only when selected. |
| `skills/software-engineering/assets/templates/aspnet-react/src/App.Server/Domain/Common/Entity.cs` | Optional ASP.NET/React/Blazor scaffold source; copied only when selected. |
| `skills/software-engineering/assets/templates/aspnet-react/src/App.Server/Domain/Entities/.gitkeep` | Optional ASP.NET/React/Blazor scaffold source; copied only when selected. |
| `skills/software-engineering/assets/templates/aspnet-react/src/App.Server/Domain/Enums/.gitkeep` | Optional ASP.NET/React/Blazor scaffold source; copied only when selected. |
| `skills/software-engineering/assets/templates/aspnet-react/src/App.Server/Domain/Events/.gitkeep` | Optional ASP.NET/React/Blazor scaffold source; copied only when selected. |
| `skills/software-engineering/assets/templates/aspnet-react/src/App.Server/Domain/Exceptions/.gitkeep` | Optional ASP.NET/React/Blazor scaffold source; copied only when selected. |
| `skills/software-engineering/assets/templates/aspnet-react/src/App.Server/Extensions/ServiceCollectionExtensions.cs` | Optional ASP.NET/React/Blazor scaffold source; copied only when selected. |
| `skills/software-engineering/assets/templates/aspnet-react/src/App.Server/Extensions/WebApplicationExtensions.cs` | Optional ASP.NET/React/Blazor scaffold source; copied only when selected. |
| `skills/software-engineering/assets/templates/aspnet-react/src/App.Server/HealthChecks/SqlServerHealthCheck.cs` | Optional ASP.NET/React/Blazor scaffold source; copied only when selected. |
| `skills/software-engineering/assets/templates/aspnet-react/src/App.Server/Infrastructure/AI/.gitkeep` | Optional ASP.NET/React/Blazor scaffold source; copied only when selected. |
| `skills/software-engineering/assets/templates/aspnet-react/src/App.Server/Infrastructure/Authentication/.gitkeep` | Optional ASP.NET/React/Blazor scaffold source; copied only when selected. |
| `skills/software-engineering/assets/templates/aspnet-react/src/App.Server/Infrastructure/Authorization/.gitkeep` | Optional ASP.NET/React/Blazor scaffold source; copied only when selected. |
| `skills/software-engineering/assets/templates/aspnet-react/src/App.Server/Infrastructure/Data/AppDbContext.cs` | Optional ASP.NET/React/Blazor scaffold source; copied only when selected. |
| `skills/software-engineering/assets/templates/aspnet-react/src/App.Server/Infrastructure/Data/AppDbContextFactory.cs` | Optional ASP.NET/React/Blazor scaffold source; copied only when selected. |
| `skills/software-engineering/assets/templates/aspnet-react/src/App.Server/Infrastructure/Data/Configurations/.gitkeep` | Optional ASP.NET/React/Blazor scaffold source; copied only when selected. |
| `skills/software-engineering/assets/templates/aspnet-react/src/App.Server/Infrastructure/Data/DatabaseInitializer.cs` | Optional ASP.NET/React/Blazor scaffold source; copied only when selected. |
| `skills/software-engineering/assets/templates/aspnet-react/src/App.Server/Infrastructure/Data/Migrations/.gitkeep` | Optional ASP.NET/React/Blazor scaffold source; copied only when selected. |
| `skills/software-engineering/assets/templates/aspnet-react/src/App.Server/Infrastructure/ExternalServices/.gitkeep` | Optional ASP.NET/React/Blazor scaffold source; copied only when selected. |
| `skills/software-engineering/assets/templates/aspnet-react/src/App.Server/Infrastructure/Notifications/.gitkeep` | Optional ASP.NET/React/Blazor scaffold source; copied only when selected. |
| `skills/software-engineering/assets/templates/aspnet-react/src/App.Server/Infrastructure/Persistence/.gitkeep` | Optional ASP.NET/React/Blazor scaffold source; copied only when selected. |
| `skills/software-engineering/assets/templates/aspnet-react/src/App.Server/Middleware/.gitkeep` | Optional ASP.NET/React/Blazor scaffold source; copied only when selected. |
| `skills/software-engineering/assets/templates/aspnet-react/src/App.Server/Program.cs` | Optional ASP.NET/React/Blazor scaffold source; copied only when selected. |
| `skills/software-engineering/assets/templates/aspnet-react/src/App.Server/Properties/launchSettings.json` | Optional ASP.NET/React/Blazor scaffold source; copied only when selected. |
| `skills/software-engineering/assets/templates/aspnet-react/src/App.Server/Security/.gitkeep` | Optional ASP.NET/React/Blazor scaffold source; copied only when selected. |
| `skills/software-engineering/assets/templates/aspnet-react/src/App.Server/appsettings.Development.json` | Optional ASP.NET/React/Blazor scaffold source; copied only when selected. |
| `skills/software-engineering/assets/templates/aspnet-react/src/App.Server/appsettings.Production.json` | Optional ASP.NET/React/Blazor scaffold source; copied only when selected. |
| `skills/software-engineering/assets/templates/aspnet-react/src/App.Server/appsettings.json` | Optional ASP.NET/React/Blazor scaffold source; copied only when selected. |
| `skills/software-engineering/assets/templates/aspnet-react/src/App.Server/wwwroot/.gitkeep` | Optional ASP.NET/React/Blazor scaffold source; copied only when selected. |
| `skills/software-engineering/assets/templates/aspnet-react/tests/App.Server.IntegrationTests/App.Server.IntegrationTests.csproj` | Optional ASP.NET/React/Blazor scaffold source; copied only when selected. |
| `skills/software-engineering/assets/templates/aspnet-react/tests/App.Server.IntegrationTests/HostTests.cs` | Optional ASP.NET/React/Blazor scaffold source; copied only when selected. |
| `skills/software-engineering/assets/templates/aspnet-react/tests/App.Server.UnitTests/App.Server.UnitTests.csproj` | Optional ASP.NET/React/Blazor scaffold source; copied only when selected. |
| `skills/software-engineering/references/architecture.md` | On-demand execution, engineering or evidence contract. |
| `skills/software-engineering/references/aspnet-profile.md` | On-demand execution, engineering or evidence contract. |
| `skills/software-engineering/references/backend.md` | On-demand execution, engineering or evidence contract. |
| `skills/software-engineering/references/data.md` | On-demand execution, engineering or evidence contract. |
| `skills/software-engineering/references/delivery.md` | On-demand execution, engineering or evidence contract. |
| `skills/software-engineering/references/design-system.md` | On-demand execution, engineering or evidence contract. |
| `skills/software-engineering/references/frontend.md` | On-demand execution, engineering or evidence contract. |
| `skills/software-engineering/references/ontology-semantics.md` | On-demand execution, engineering or evidence contract. |
| `skills/software-engineering/references/operations.md` | On-demand execution, engineering or evidence contract. |
| `skills/software-engineering/references/product-integration.md` | On-demand execution, engineering or evidence contract. |
| `skills/software-engineering/references/profiles/aspnet-architecture-architecture.md` | Optional ASP.NET profile contract or retained source provenance. |
| `skills/software-engineering/references/profiles/aspnet-architecture-source-audit.md` | Optional ASP.NET profile contract or retained source provenance. |
| `skills/software-engineering/references/profiles/aspnet-backend-backend-contracts.md` | Optional ASP.NET profile contract or retained source provenance. |
| `skills/software-engineering/references/profiles/aspnet-frontend-frontend-contracts.md` | Optional ASP.NET profile contract or retained source provenance. |
| `skills/software-engineering/references/profiles/aspnet-verification-verification.md` | Optional ASP.NET profile contract or retained source provenance. |
| `skills/software-engineering/references/profiles/source-manifest.json` | Optional ASP.NET profile contract or retained source provenance. |
| `skills/software-engineering/references/qa-and-evidence.md` | On-demand execution, engineering or evidence contract. |
| `skills/software-engineering/references/requirements.md` | On-demand execution, engineering or evidence contract. |
| `skills/software-engineering/references/security.md` | On-demand execution, engineering or evidence contract. |
| `skills/software-engineering/references/sources.json` | On-demand execution, engineering or evidence contract. |
| `skills/software-engineering/references/state-and-budget.md` | On-demand execution, engineering or evidence contract. |
| `skills/software-engineering/references/task-assignment.md` | On-demand execution, engineering or evidence contract. |
| `skills/software-engineering/references/testing.md` | On-demand execution, engineering or evidence contract. |
| `skills/software-engineering/references/upstream/LICENSE` | Attributed engineering workflow or supporting reference; selectively loaded. |
| `skills/software-engineering/references/upstream/docs/agents.md` | Attributed engineering workflow or supporting reference; selectively loaded. |
| `skills/software-engineering/references/upstream/personas/code-reviewer.md` | Attributed engineering workflow or supporting reference; selectively loaded. |
| `skills/software-engineering/references/upstream/personas/security-auditor.md` | Attributed engineering workflow or supporting reference; selectively loaded. |
| `skills/software-engineering/references/upstream/personas/test-engineer.md` | Attributed engineering workflow or supporting reference; selectively loaded. |
| `skills/software-engineering/references/upstream/personas/web-performance-auditor.md` | Attributed engineering workflow or supporting reference; selectively loaded. |
| `skills/software-engineering/references/upstream/references/accessibility-checklist.md` | Attributed engineering workflow or supporting reference; selectively loaded. |
| `skills/software-engineering/references/upstream/references/definition-of-done.md` | Attributed engineering workflow or supporting reference; selectively loaded. |
| `skills/software-engineering/references/upstream/references/observability-checklist.md` | Attributed engineering workflow or supporting reference; selectively loaded. |
| `skills/software-engineering/references/upstream/references/orchestration-patterns.md` | Attributed engineering workflow or supporting reference; selectively loaded. |
| `skills/software-engineering/references/upstream/references/performance-checklist.md` | Attributed engineering workflow or supporting reference; selectively loaded. |
| `skills/software-engineering/references/upstream/references/security-checklist.md` | Attributed engineering workflow or supporting reference; selectively loaded. |
| `skills/software-engineering/references/upstream/references/testing-patterns.md` | Attributed engineering workflow or supporting reference; selectively loaded. |
| `skills/software-engineering/references/upstream/skills/api-and-interface-design/workflow.md` | Attributed engineering workflow or supporting reference; selectively loaded. |
| `skills/software-engineering/references/upstream/skills/browser-testing-with-devtools/workflow.md` | Attributed engineering workflow or supporting reference; selectively loaded. |
| `skills/software-engineering/references/upstream/skills/ci-cd-and-automation/workflow.md` | Attributed engineering workflow or supporting reference; selectively loaded. |
| `skills/software-engineering/references/upstream/skills/code-review-and-quality/workflow.md` | Attributed engineering workflow or supporting reference; selectively loaded. |
| `skills/software-engineering/references/upstream/skills/code-simplification/workflow.md` | Attributed engineering workflow or supporting reference; selectively loaded. |
| `skills/software-engineering/references/upstream/skills/constraint-driven-development/references/floor-guard.md` | Attributed engineering workflow or supporting reference; selectively loaded. |
| `skills/software-engineering/references/upstream/skills/constraint-driven-development/workflow.md` | Attributed engineering workflow or supporting reference; selectively loaded. |
| `skills/software-engineering/references/upstream/skills/context-engineering/workflow.md` | Attributed engineering workflow or supporting reference; selectively loaded. |
| `skills/software-engineering/references/upstream/skills/debugging-and-error-recovery/workflow.md` | Attributed engineering workflow or supporting reference; selectively loaded. |
| `skills/software-engineering/references/upstream/skills/deprecation-and-migration/workflow.md` | Attributed engineering workflow or supporting reference; selectively loaded. |
| `skills/software-engineering/references/upstream/skills/documentation-and-adrs/workflow.md` | Attributed engineering workflow or supporting reference; selectively loaded. |
| `skills/software-engineering/references/upstream/skills/doubt-driven-development/workflow.md` | Attributed engineering workflow or supporting reference; selectively loaded. |
| `skills/software-engineering/references/upstream/skills/frontend-ui-engineering/workflow.md` | Attributed engineering workflow or supporting reference; selectively loaded. |
| `skills/software-engineering/references/upstream/skills/git-workflow-and-versioning/workflow.md` | Attributed engineering workflow or supporting reference; selectively loaded. |
| `skills/software-engineering/references/upstream/skills/idea-refine/examples.md` | Attributed engineering workflow or supporting reference; selectively loaded. |
| `skills/software-engineering/references/upstream/skills/idea-refine/frameworks.md` | Attributed engineering workflow or supporting reference; selectively loaded. |
| `skills/software-engineering/references/upstream/skills/idea-refine/refinement-criteria.md` | Attributed engineering workflow or supporting reference; selectively loaded. |
| `skills/software-engineering/references/upstream/skills/idea-refine/scripts/idea-refine.sh` | Attributed engineering workflow or supporting reference; selectively loaded. |
| `skills/software-engineering/references/upstream/skills/idea-refine/workflow.md` | Attributed engineering workflow or supporting reference; selectively loaded. |
| `skills/software-engineering/references/upstream/skills/incremental-implementation/workflow.md` | Attributed engineering workflow or supporting reference; selectively loaded. |
| `skills/software-engineering/references/upstream/skills/interview-me/workflow.md` | Attributed engineering workflow or supporting reference; selectively loaded. |
| `skills/software-engineering/references/upstream/skills/observability-and-instrumentation/workflow.md` | Attributed engineering workflow or supporting reference; selectively loaded. |
| `skills/software-engineering/references/upstream/skills/performance-optimization/references/optimization-patterns.md` | Attributed engineering workflow or supporting reference; selectively loaded. |
| `skills/software-engineering/references/upstream/skills/performance-optimization/workflow.md` | Attributed engineering workflow or supporting reference; selectively loaded. |
| `skills/software-engineering/references/upstream/skills/planning-and-task-breakdown/workflow.md` | Attributed engineering workflow or supporting reference; selectively loaded. |
| `skills/software-engineering/references/upstream/skills/security-and-hardening/references/hardening-patterns.md` | Attributed engineering workflow or supporting reference; selectively loaded. |
| `skills/software-engineering/references/upstream/skills/security-and-hardening/workflow.md` | Attributed engineering workflow or supporting reference; selectively loaded. |
| `skills/software-engineering/references/upstream/skills/shipping-and-launch/workflow.md` | Attributed engineering workflow or supporting reference; selectively loaded. |
| `skills/software-engineering/references/upstream/skills/source-driven-development/workflow.md` | Attributed engineering workflow or supporting reference; selectively loaded. |
| `skills/software-engineering/references/upstream/skills/spec-driven-development/workflow.md` | Attributed engineering workflow or supporting reference; selectively loaded. |
| `skills/software-engineering/references/upstream/skills/test-driven-development/workflow.md` | Attributed engineering workflow or supporting reference; selectively loaded. |
| `skills/software-engineering/references/upstream/skills/using-agent-skills/workflow.md` | Attributed engineering workflow or supporting reference; selectively loaded. |
| `skills/software-engineering/scripts/compile_graph.py` | Runtime operation, maintenance validator or source inventory tool. |
| `skills/software-engineering/scripts/owl_reader.py` | Runtime operation, maintenance validator or source inventory tool. |
| `skills/software-engineering/scripts/project_audit.py` | Runtime operation, maintenance validator or source inventory tool. |
| `skills/software-engineering/scripts/requirements-maintenance.txt` | Runtime operation, maintenance validator or source inventory tool. |
| `skills/software-engineering/scripts/route.py` | Runtime operation, maintenance validator or source inventory tool. |
| `skills/software-engineering/scripts/scaffold.py` | Runtime operation, maintenance validator or source inventory tool. |
| `skills/software-engineering/scripts/validate.py` | Runtime operation, maintenance validator or source inventory tool. |
| `tests/test_integration.py` | Executable behavioral regression or integration test. |
| `tests/test_mediator.py` | Executable behavioral regression or integration test. |
| `tests/test_project_intelligence.py` | Executable behavioral regression or integration test. |
| `tests/test_project_setup.py` | Executable behavioral regression or integration test. |
| `tests/test_router.py` | Executable behavioral regression or integration test. |
