# Requirements and acceptance

Inspect the actual application and resolve whether the user requests analysis,
implementation, review, repair, scaffolding or delivery. Preserve their scope.
Identify actors, journeys, data ownership, constraints and external prerequisites.
Ask only for missing decisions that materially affect the outcome.

Record requirements as graph nodes with stable IDs. Keep detailed acceptance
criteria in one linked requirements artifact. For each journey identify the
trigger, expected result, permissions, failure behavior and verification method.
Include latency, availability, accessibility or retention requirements only when
relevant; do not invent numeric targets.

Separate established facts, routine assumptions and unresolved decisions. Link
contracts/tasks to their requirements through `satisfies` and dependencies. A
changed requirement reopens affected work. For review-only scope the requested
output is findings/evidence; source writes need user authorization.
