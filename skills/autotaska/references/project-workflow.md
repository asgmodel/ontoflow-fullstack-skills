# Project plan and contracts

## Scope

Record application outcome, actors, main workflows, required/excluded features, stack, runtime/deployment target, language/theme requirements, available source and material open decisions. Use current authoritative files for prior project details. Do not invent requirements from another product.

## Acceptance and dependencies

Define stable acceptance-path IDs and observable results. Start with one useful vertical slice. Map tasks to dependencies and keep ordered work ordered. Define actor/ownership and API/schema contracts before dispatching dependent backend/client implementation. Parallelize independent discovery, bounded components, module work and review when their inputs are ready.

## Canonical contract record

Reference the project's actual OpenAPI/shared DTO/schema files and revision/hashes. Establish HTTP methods/paths, fields/nullability, validation, error shapes, session/CSRF requirements, authorization, ownership, identifiers, timestamps, migration behavior and UI consumers as relevant. Keep draft and accepted contracts distinct.

Do not have separate departments invent competing schemas. A coordinator can resolve routine in-scope decisions without a new user approval. Material missing scope choices still need user input.

## Ownership

Name one mutable-file owner per task. Assign shared configuration, startup files, dependency manifests/lockfiles and migration sequencing deliberately. Preserve existing user edits. Use disjoint source directories or supported isolated worktrees. Never reset/clean/discard another writer's work.

## Control point

Use the current conversation as coordination owner. If visible projects are requested, maintain a linked dashboard within the project through Delegator. Keep one authoritative register; dashboard messages are views of it. Include department, current task, status, contract revision, evidence, blockers and next action. Use real links only after observing saved identities.
