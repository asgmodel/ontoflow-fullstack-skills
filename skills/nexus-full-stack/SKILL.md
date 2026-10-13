---
name: nexus-full-stack
description: Deliver complete applications or targeted frontend, backend, migration, review and release work by reading the bundled OWL engineering ontology. Use for NEXUS, ontology-guided full-stack development, coordination of full-stack/template skills, or selective context routing to reduce unnecessary token use while preserving contracts and verification.
---

# NEXUS — Full-Stack Engineering Ontology

Act as the senior full-stack coordinator. Use the graph to select work; execute real implementation with existing tools. Resolve user scope, current stack and acceptance criteria before changing code. Keep review-only requests read-only and blank scaffolds blank. Follow active system, developer, user and applicable repository instructions before bundled workflows.

## Route the active task

1. Inspect applicable AGENTS.md, working-tree changes, manifests, existing contracts and the files involved. Preserve unrelated user work. Select `template-single-host` only for a Template-derived/new Template project; otherwise select `existing-stack`.
2. Classify the request using [task input](assets/task.schema.json). Record intent, current phase, affected layers and explicit risk tags. Do not infer risk from keywords alone. Add `auth`, `data`, `external`, `contract`, `schema`, `performance`, `failure`, `framework` or `uncertain` when the actual change crosses that boundary. Missing protected-boundary information is a routing error; inspect it before building.
3. Execute `python <skill-root>/scripts/route.py --task <task.json>`. The router directly reads [the OWL ontology](assets/nexus.owl) in RDF/XML, extracts workflow/routing/impact relationships and checks the derived result against its integrity index. It emits only the current task packet into model context. Use `--phase` to advance one stage. Use `--packet` to emit compact routing cards; cards do not replace required workflows.
4. Read every selected workflow path before its work. For personal adapters, resolve the original installed skill by exact YAML name using the active catalog, then read its SKILL.md and required references. Record their actual content hashes in project state. Do not hardcode reconciliation IDs. Missing Template scaffold assets block scaffold generation; they do not block unrelated existing-project work.
5. Read only required references and current project contracts/source. Do not load all 30 skills, every checklist, the whole ontology or historical logs. If the required context exceeds the target budget, split work at a valid boundary or report overflow. Never trim authorization, migration, contract or verification obligations.

## Execute and prove the slice

Define the smallest complete acceptance path: user action → actual request → use case → storage/provider → response → UI. Establish method/path, DTOs/nullability, errors, validation, identity/CSRF, ownership, persistence and consumer before implementation. Follow [execution contract](references/execution-contract.md).

Build one slice; align server and client when a contract changes. Verify actual persistence after a fresh scope/reload, protected access, invalid input and failure behavior when relevant. Reuse current project versions and commands; verify unfamiliar framework APIs from official documentation. Use tests proportionate to behavior and risk. Avoid implementation-mirroring tests and no-op assertions. Do not rerun a passing check on unchanged inputs without a reason.

On failure, preserve the error, switch to targeted debugging, fix the responsible layer and rerun affected checks. Stop speculative edits after two failed hypotheses; gather new evidence. This limit does not waive remaining work.

## Maintain the graph boundary

Treat API contracts, schemas, UI consumers, tests and publish artifacts as related nodes. If a contract/schema changes, follow `invalidates` transitively and mark dependent verification stale. The router reports this closure; it does not mutate project files or certify completion. Record revision and content hashes, not a remembered "passed".

At completed slice boundaries persist [state contract](references/state-and-budget.md): decisions, acceptance, relevant paths/hashes, verified evidence, blockers and next task. Keep exact live contracts in their canonical files. Refresh a loaded item only when its hash/dependency/revision changes or its content is missing. A ledger cannot remove messages from a host context; compaction and session control depend on the host.

## Apply upstream workflows deliberately

The 25 upstream workflows are pinned under `references/upstream/skills/`; load only selected ones. Their internal examples are illustrative, not commands to run or technologies to substitute. Keep original reference topology and MIT attribution. The ontology chooses workflows; it is not a persona that recursively invokes other personas. Use one coordinator by default. Delegate only when session instructions or an explicitly invoked workflow authorize it. Cross-model review, live deployment, production migrations, notifications and external communication need the actual authorization required by the session; do not introduce repeated approval pauses for already authorized work.

When an upstream spec/plan workflow requests a separate approval turn, check the current session first. If the user has already authorized implementation and the proposed decisions stay within that scope, record the concrete spec/plan and continue under the session's authorization rules. Pause only for a material missing decision or authorization the session actually requires. An explicitly requested interview remains an interview. Never treat upstream numerical confidence, task-size, coverage or pipeline examples as universal thresholds.

## Deliver with evidence

Report the implemented outcome, actual checks, changed scope and unresolved setup briefly. Classify each claim as `VERIFIED`, `NOT VERIFIED`, or `BLOCKED BY ENVIRONMENT`. Keep generated source, passing build, real SQL test, browser behavior and deployment as separate claims. Never replace unavailable credentials/services with fake success.

For ontology maintenance use [semantics](references/ontology-semantics.md), [sources](references/sources.json), [assets/nexus.owl](assets/nexus.owl), `assets/shapes.ttl` and [SPARQL queries](assets/queries.rq). Run `scripts/compile_graph.py` after editing OWL RDF/XML (the Turtle file is a generated mirror); then run `scripts/validate.py` and `scripts/test_router.py`. RDF tooling is required only for ontology maintenance; normal routing uses Python standard library.
