# Architecture and integration

Inspect the native stack, deployment shape, entrypoints, module dependencies and
existing decisions before proposing structure. Keep the smallest architecture
that satisfies the current scope. Record a meaningful decision with alternatives,
basis, consequences and affected requirements; avoid documents that repeat code.

Define contract ownership across domain, application/use case, persistence,
transport and presentation. Keep business rules independent of transport/UI.
Use repository-native boundaries; an ASP.NET folder layout is optional.

For each API contract record method/path/version, DTOs, nullability, date and
identifier formats, validation, pagination, error semantics, identity, CSRF where
relevant, ownership and the consuming action. Keep one canonical contract file
and register its artifact hash. Align both server and consumer on changes.

Implement a complete slice: user action -> request -> use case -> real
storage/provider -> response -> visible result. Verify persistence after a fresh
scope/reload and protected access. A UI restriction does not enforce server rules.

Link Requirement -> Contract -> Task -> Artifact -> Evidence with `satisfies`,
`dependsOn`, `usesArtifact` and `derivedFrom` as appropriate. Add every affected
consumer/build/test artifact to change impact, update hashes through the mediator
and rerun affected checks. Do not keep separate lifecycle or completion ledgers.
