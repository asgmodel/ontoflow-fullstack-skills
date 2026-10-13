# Integrated Project Monitor

Monitor actual state, not optimistic narrative. Run observation after meaningful events and on resume; monitoring is not an always-on service.

## Separate three state tracks

| Track | States |
| --- | --- |
| Task | pending, ready, dispatched, running, blocked, review, verified |
| Transport/generation | draft, send_uncertain, accepted, generating, settled, failed |
| Verification | not_run, passed, failed, stale, blocked |

A settled reply moves the task to review. Mark verified only when acceptance evidence for the current source/contracts is inspected. Never convert a generated test command into a passing test record.

## Observation record

For each task keep ID, owner, dependencies, acceptance IDs, relevant conversation/link, scope/source paths, contract revisions and state. For checks retain command/action, observed result, evidence location, timestamp and source revision/hashes. For blockers retain exact missing prerequisite/error, responsible owner, next resolution and whether independent work can continue. Record credential names/setup status, never values.

Keep task and verification evidence in the source project's existing records or an adapted project-state.json. Use appropriate persistent storage for deliverable checkpoints; do not rely only on chat memory. Do not write private screenshots or source secrets into monitoring artifacts.

## Monitor loop

1. Read current register and relevant live conversation/source state.
2. Detect actual transition, blocker, contract drift, stale check or inconsistent claim.
3. Update the authoritative record; keep the coordinator as state writer.
4. Send a scoped follow-up/repair through Delegator or permitted agent tools.
5. Continue other ready work.
6. Review outputs and integrate actual changes before rerunning affected checks.
7. Report material outcomes, uncertainty and next resolution.

Do not poll all chats repeatedly without a reason. Prefer event/receipt-driven checks and bounded revisits for running work. Never automatically resend an accepted/uncertain prompt; inspect transcript first. Do not create substitute chats as an unverified recovery shortcut.

## Change impact

When source, contract, schema, authorization or deployment configuration changes, identify downstream consumers/checks. Use NEXUS invalidation where available and record the transitive affected closure. Mark dependent verification stale. Do not claim current verification from an obsolete revision. Recheck passing work only when inputs/requirements changed or evidence is missing.

## Resume

Inspect saved project/chat identities, pending dispatches, current source/user changes and evidence freshness. Reconcile uncertain operations before continuation. Resume ready tasks with bounded context and accepted contracts. Carry over useful results; do not restart the project merely because the host context was compacted.

## Reporting

Show a concise factual table: department/task, status, implemented result, blocker/next action and verified link. Use percentage progress only with an explicit denominator and completion rule. Distinguish planned, generated, integrated and verified. Report scheduler/automation limits if future monitoring is configured; never promise uninterrupted autonomy from skill text alone.
