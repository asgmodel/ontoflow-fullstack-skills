# Task conversations and engineering handoff

Read installed chatgpt-task-creator as the actual Delegator implementation. Pass the verified ChatGPT project and repository identities, brief and accepted scope. Keep one source of project state and a single coordinator. Do not invoke a nonexistent use_skill tool.

## Task graph

Use stable task IDs and dependency references. Define acceptance first. Separate briefing a blocked task from dispatching executable work. Start scope/contracts before dependent implementation. Once shared contracts are accepted, backend/data and client work can progress independently when file ownership is disjoint.

Use one chat per coherent major task or department as requested. Reuse it for bounded follow-ups; avoid unnecessary context duplication. Each assignment must include goal, actual accessible source/tools, input contracts/revision, allowed paths, dependencies, outputs, acceptance and evidence. Never assume shared project membership or a GitHub URL provides code execution access.

Keep statuses `pending`, `ready`, `dispatched`, `running`, `blocked`, `review`, `verified` separately from transport states `draft`, `send_uncertain`, `accepted`, `generating`, `settled`, `failed`. Require live evidence for sends and source checks. A completed answer is reviewed output; it is not verified implementation.

## Cross-linking and updates

Maintain a task table in the coordinating chat and an authoritative register in the repository when available. Use observed URLs/IDs. Verify project membership and exact chat title. Include repo/contract reference in relevant chat briefs and a project link in private repository records; do not change access to make private links public.

Accept or reject contract proposals against source/user scope. Notify consumers of accepted revisions, invalidate affected checks and assign repairs. Preserve exact errors and avoid repeated speculative edits. Continue independent ready work during blockers.

## Handoff

For an implementation request, load autotaska and relevant NEXUS routing while preserving the current coordinator. Transfer current project/repo/chat identities, brief, accepted contracts, task graph, evidence and blockers. Use stack-specific adapters only when applicable. For setup-only scope, finish ready setup/research/architecture task dispatch and give the user the linked register; do not silently build/deploy the entire app.
