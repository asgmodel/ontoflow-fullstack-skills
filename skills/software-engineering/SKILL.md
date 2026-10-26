---
name: software-engineering
description: Implement, review, debug and deliver software using ontology-selected engineering knowledge under OntoLink. Use for full-stack applications, backend, frontend, data, security, migrations, testing and release work; preserve the existing stack and use the optional ASP.NET scaffold only when selected.
---

# Full Stack Engineering

Execute the current OntoLink task as the software engineering adapter. Keep
`ontolink-skills` as the sole lifecycle coordinator and `knowledge.owl` as the
sole operational state. OntoLink is an external installed skill, never a bundled
copy. Resolve its current directory by exact skill name, not a project-local
placeholder. Read its current execution contract and selected phase procedure
before engineering work. Apply user/host instructions before bundled references.

## Route the eligible task

1. Inspect project instructions, working-tree changes, manifests, current contracts
   and acceptance criteria. Preserve unrelated work and the approved design.
2. At each new project session, request/load the original `ontolink-skills` from
   the host skill registry. Refresh only that external dependency through the
   host's skill manager before reading it. With Skills CLI run:

   ```sh
   npx skills add https://github.com/asgmodel/ontolink-skills --skill ontolink-skills --global --yes
   ```

   Then resolve/read its current SKILL.md, required contracts and selected phase.
   Set `ONTOLINK_SKILL_ROOT` to the actual installed package or pass
   `--coordinator-root`. `scripts/dependency.py` resolves exact-name global host
   installations, including host-generated folder IDs and symlinks. It does not
   download code or certify freshness. Do not copy OntoLink into this repository
   or application; execute bootstrap/context/record from the external directory
   according to its current instructions. Preserve explicit state and existing
   proofs. On a missing dependency, update failure or incompatible API, report
   the exact condition; never fall back to a hidden bundled copy.
3. Prepare task input using [task.schema.json](assets/task.schema.json). Classify
   intent, profile, affected layers and real boundary tags by inspecting source.
   Use `existing-stack` normally; use `aspnet-single-host` only for the chosen
   ASP.NET/React/Blazor scaffold. Omit `phase`; the engineering ontology maps the live external lifecycle phase to its engineering stage.
4. Run the installed engineering router:

   ```sh
   python <engineering-root>/scripts/route.py --task <task-input.json> \
     --state <canonical-state.owl> --coordinator-root <ontolink-root>
   ```

   The router invokes the external mediator anew and validates current project task eligibility before
   selecting engineering references. `--focus-task <task-id>` targets an eligible
   subtask. It never advances lifecycle state or executes the selected work.
5. Read every selected workflow and required linked reference before applying it.
   Read only the current source/contracts needed for that task. A phase without
   an applicable engineering recipe still requires its OntoLink outcome; do not
   skip ahead. A route is neither approval nor evidence of completion.

## Apply engineering depth selectively

| Need | Reference |
| --- | --- |
| Scope and acceptance | [requirements.md](references/requirements.md) |
| Architecture, contracts and complete slices | [architecture.md](references/architecture.md) |
| Ownership and dependency-based task distribution | [task-assignment.md](references/task-assignment.md) |
| APIs, use cases and authorization | [backend.md](references/backend.md) |
| Interfaces, accessibility and integration | [frontend.md](references/frontend.md) |
| Persistence, migrations and concurrency | [data.md](references/data.md) |
| Identity, isolation, secrets and threats | [security.md](references/security.md) |
| Meaningful validation and evidence | [testing.md](references/testing.md) |
| Delivery, CI and recovery | [delivery.md](references/delivery.md) |
| Operational signals and resume | [operations.md](references/operations.md) |
| Exact graph semantics and maintenance | [ontology-semantics.md](references/ontology-semantics.md) |
| Context freshness and accounting | [state-and-budget.md](references/state-and-budget.md) |
| Optional scaffold and inherited versions | [aspnet-profile.md](references/aspnet-profile.md) |

Implement one complete acceptance path through its actual layers. When a check
fails, preserve the error, investigate the responsible boundary and rerun affected
checks after correction. Record dependencies and change impact in the project
graph; stale verification cannot close work.

Keep the 25 attributed upstream workflows under `references/upstream/` selectively
loaded. Their examples do not choose the stack, authorize deployment or require
repeated approval for already-authorized work. Delegation follows session rules;
role suggestions do not launch agents or transmit messages. External OntoLink engineering candidates are suggestions; this package supplies the engineering work without recursively invoking absent legacy coordinators.

Store generated documents and proof logs in `.ontolink/artifacts/` and
`.ontolink/proofs/` beside the canonical state. Write state only through the
mediator with the observed revision. Report implemented behavior, actual checks
and unresolved prerequisites. Distinguish VERIFIED, NOT VERIFIED and BLOCKED BY
ENVIRONMENT; do not infer runtime or deployment success from generated files.
