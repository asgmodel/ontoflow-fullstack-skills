# Verification and evidence

Derive checks from acceptance and changed boundaries. Use meaningful unit tests
for business rules, integration checks for contracts/data/auth, browser journeys
for UI and isolated database migration tests when schemas change. Keep blank
scaffolds blank; conditional checks may be inapplicable with an explicit reason.

Record the exact command/tool action, exit status/observation, environment,
source revision/content fingerprint and acceptance criterion in a proof file.
Run checks; never infer success from an intended command or an existing filename.
Avoid no-op assertions and tests that only repeat the implementation.

Use the coordinator record contract for Artifact and Evidence nodes. PASS needs
an inspected proof whose SHA-256 and target artifact hash match current bytes.
Hash provenance does not establish the truth of a claim on its own. Register
source snapshots/manifests when a proof concerns multiple files. Re-run affected
checks after relevant source or contract changes before closing work.

Distinguish VERIFIED, NOT VERIFIED and BLOCKED BY ENVIRONMENT. Keep source
inspection, compilation, real database tests, browser behavior and external
receipts separate. For the selected ASP.NET scaffold read
[verification matrix](profiles/aspnet-verification-verification.md).
