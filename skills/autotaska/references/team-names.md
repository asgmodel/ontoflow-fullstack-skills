# AutoTaska department names

Use AutoTaska as the master skill/product name. Use these names as human-facing department labels; they are not claims that separate skills have been installed. Preserve the exact installed skill identifiers used for routing.

| Display name | Responsibility | Implementation route |
| --- | --- | --- |
| AutoTaska | Main senior full-stack coordinator | autotaska |
| NEXUS | Engineering reasoning, ontology and workflow selection | nexus-full-stack |
| AutoTaska Delegator | Visible project/chat structure, assignment and result transfer | chatgpt-task-creator |
| AutoTaska Monitor | Progress, blockers, evidence freshness and checkpoints | Integrated monitor.md |
| AutoTaska Architect | Structure, module boundaries and integration contracts | Relevant architecture workflow |
| AutoTaska Data | Data modeling, persistence, migrations and isolation | Relevant data/backend workflow |
| AutoTaska Backend | API, use cases, permissions and provider integration | Relevant backend workflow |
| AutoTaska Frontend | Web client, design, real API wiring and responsive behavior | Relevant client/interface workflow |
| AutoTaska QA | Integration, acceptance tests and verified readiness | Relevant verification workflow |
| AutoTaska DevOps | Builds, configuration, authorized deployment and handoff | Relevant release workflow |
| AutoTaska Mobile | Actual Flutter/native/mobile client when requested | Actual platform workflow |

Create only departments required by the application. Combine Data and Backend when tightly coupled; omit Mobile for a web-only app. Keep NEXUS as the existing skill name rather than renaming it. Use conversation titles `<app> | <NN> <department name>` unless the user supplies an exact title. Keep the current main conversation as coordination owner; do not create a competing autonomous supervisor.
