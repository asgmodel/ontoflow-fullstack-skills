# Task ownership and dependencies

Use OntoLink Task nodes as the task register. Decompose accepted scope by
checkable outcome and dependency, not a fixed list of departments or agents.
Each task has a stable ID, phase, accountable owner, required outcome kind,
dependencies and linked acceptance/source artifacts. Preserve each phase's
mandatory outcome. Record actual people/agents as Actors before assigning their
identity; a planned engineering role is a declared role, not proof of a live agent.

Keep the write set and integration contract in a linked planning artifact:

| Field | Required content |
| --- | --- |
| Goal | Concrete behavior or review result |
| Inputs | Current requirement/contract IDs and artifact hashes |
| Ownership | One accountable owner; file/module write set |
| Dependencies | Required predecessor tasks and consumed artifacts |
| Outcome | Deliverable path/kind and acceptance criteria |
| Verification | Command or observed behavior needed for acceptance |
| Constraints | Native stack, security boundary, scope and authorization |
| Handoff | Changes, proof, unresolved issues and next consumer |

Architecture owns boundary and contract decisions; backend owns use cases/API;
data owns persistence/migration; frontend owns routes/states and consumers;
verification owns independent acceptance checks; delivery owns packaging and
operational recovery. Combine roles for small work. Keep one coordinator to
accept results and update the canonical graph.

Dispatch only tasks whose predecessors are complete and blockers resolved.
Parallelize independent outcomes only when file ownership and contracts are
clear and the session permits delegation. Serialize overlapping write sets or
assign one integration owner; never let two workers overwrite the same files.
An assignment, a role name or a recommendation does not launch agents.

Record handoffs as draft Message facts unless a real authorized transmission
occurred. A returned proposal needs review and current proof before acceptance.
Reconcile revision conflicts by rereading state; never bypass the revision guard.
