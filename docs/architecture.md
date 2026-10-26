# Architecture and external dependency contract

## Ownership

| Component | Location | Authority |
| --- | --- | --- |
| Full Stack Engineering | This repository, `skills/software-engineering/` | Engineering knowledge, task routing, roles and verification obligations |
| OntoLink | Current external host installation from asgmodel/ontolink-skills | Lifecycle, canonical project state, evidence and guarded record writes |
| Loader folder | `skills/ontolink-skills/README.md` only | Instructions to request/load/update the external skill |
| Project state | Existing `knowledge.owl` or explicit configured path | Actual requirements, tasks, contracts, artifacts, evidence and blockers |

The engineering ontology owns only the compatibility mapping from external
OntoLink phase URIs to engineering stages. It never patches the external ontology,
replaces its mediator, changes phase order or advances project state.

## Session procedure

1. Request the original `ontolink-skills` by exact identity from the host registry.
2. Refresh only that dependency through the host skill manager. The documented
   CLI command installs/refreshes it globally from the moving official source.
3. Resolve and read the current installed SKILL.md, contracts and selected phase.
   Do not reuse a previously loaded instruction snapshot after an update.
4. Run the external coordinator against the existing project state. Preserve
   explicit state paths and all graph-referenced proof. No package copy is needed.
5. Invoke the engineering router with that coordinator path. Each invocation runs
   its mediator afresh and checks eligibility before selecting knowledge.
6. Execute the owned outcome, inspect real proof, and record via the external
   mediator with its current revision. Query fresh context after changes.

Installation/update is an agent workflow, not a hidden network call inside the
read-only router. The path resolver never downloads code or asserts freshness.
If offline/update fails, report freshness as unknown or the known observed state.
If the external API changes incompatibly, report the contract error and preserve
project data. The repository contains no frozen fallback or pinned OntoLink copy.

## Task distribution

One external coordinator accepts contracts and integration results. Tasks have
one accountable owner, explicit outcomes, dependencies, acceptance criteria,
verification and file write sets. Architecture, backend, data, frontend,
verification and delivery are responsibilities, not automatically spawned agents.
Dispatch only eligible work. Parallelism follows session authorization and clear
file ownership; serialize overlapping writes or name one integration owner.

## Engineering resources

The engineering ontology routes 10 local references and 25 attributed upstream
engineering workflows. Existing projects keep their native stack. The optional
ASP.NET/React/Blazor scaffold is selected explicitly. Detailed reference loading
is task-scoped; no measured token-savings percentage is asserted.

## Validation

Source checks enforce a single bundled skill and a loader folder containing only
README instructions. Adapter tests use a real external OntoLink installation,
not copied coordinator source or embedded phase packages. CI downloads current
upstream into its runner temporary directory and runs Python 3.10/3.12 checks.
Synthetic dependency fixtures test resolution, missing/ambiguous installs,
symlinks, live changes and incompatible APIs; they are labelled fixtures, not
an alternative OntoLink implementation.

Evidence and lifecycle validation remain the external mediator's responsibility.
The adapter cannot certify proof semantics, actual user identity, provider access,
application deployment or continuous monitoring from hashes and role labels.
