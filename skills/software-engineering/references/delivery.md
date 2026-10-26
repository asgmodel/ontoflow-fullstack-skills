# Delivery engineering

Confirm scope, accepted outcomes, current proofs, artifact hashes and remaining
prerequisites before handoff. Build/package using the project's native toolchain
and lockfiles. Keep environment configuration documented and secrets external.

For CI run relevant lint/type/build/tests and check reproducibility in a clean
checkout. Deployment additionally requires the actual session authorization,
provider access and release target. Verify the deployed revision, health and
critical journeys with real receipts; source upload alone is not deployment.

For consequential releases define recovery/rollback, migration compatibility and
operational ownership. Preserve user work and source history. Deliver a concise
report with changed behavior, relevant files, actual checks and exact blockers.
Do not mark the deliver phase complete merely because a release plan exists.
