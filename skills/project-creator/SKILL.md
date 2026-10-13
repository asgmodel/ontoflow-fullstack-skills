---
name: project-creator
description: Turn a user idea into a verified ChatGPT project, a GitHub repository and separate linked task conversations using the installed chatgpt-task-creator skill. Use when the user invokes منشئ المشروع or Project Creator, requests project setup from an idea, wants ChatGPT and GitHub created together, or asks to organize and dispatch application work across visible department chats. Resolve scope, create or reuse real resources, initialize appropriate source/briefs, coordinate dependencies and checkpoint identities without duplicates; hand ongoing engineering to AutoTaska/NEXUS when in scope.
---

# Project Creator — منشئ المشروع

Act as the project setup owner. Receive the user's idea, make a concrete brief, create the actual ChatGPT project, create or resolve its GitHub repository, and use `chatgpt-task-creator` to create a visible conversation for each bounded major task. Link these resources in a factual project register. Execute authorized setup instead of merely describing steps.

## Resource map

Read [creation-workflow.md](references/creation-workflow.md) before external resource creation, [repository-workflow.md](references/repository-workflow.md) before GitHub writes, and [task-coordination.md](references/task-coordination.md) before creating/distributing chats.

Populate [project-brief.md](assets/project-brief.md), [task-assignment.md](assets/task-assignment.md) and [project-register.json](assets/project-register.json) with actual facts. Run `python <skill-root>/scripts/validate_register.py <register.json>` to check structural state/dependencies before checkpointing. This script does not verify external resources; inspect live evidence for those claims.

## 1. Receive and clarify the idea

1. Distinguish creating this skill from invoking it to set up an actual product. A skill-writing request alone does not authorize opening sample projects/repos/chats.
2. Determine requested action: plan, project setup, setup plus implementation, or resume. A planning request stays read-only. Setup includes idea-to-brief, resource creation, appropriate initial repository content, task conversations and ready-task dispatch; app implementation continues only when requested/in scope.
3. Resolve name, purpose, actors, main workflows, platforms, expected deliverables and relevant constraints. Reuse explicit current decisions. Ask only for material unknowns; continue independent preparation. Do not invent a product from historical examples.
4. Choose a concise project display name and a compatible repository slug when not specified. Keep the same product identity across both. Use a private repository by default; honor explicit visibility and ownership preferences.
5. Record requirements, assumptions, acceptance paths, open decisions and exclusions in the brief. Keep unresolved technology decisions explicit; a useful repository can start with genuine project documents without pretending a stack is implemented.
6. For an existing app/repository inspect source, AGENTS.md, manifests, branch/status and user changes. Preserve its stack and working tree. Never replace it with a second generated project.

## 2. Establish capabilities and create the ChatGPT project

1. Inspect available connectors/CLIs/browser capabilities for the required operation, not merely the service name. Prefer a sufficient purpose-built interface. If a plugin lacks project/repository creation, use a permitted authenticated CLI or browser fallback. If a sufficient plugin is failing/unavailable, follow host fallback-approval rules.
2. Read the installed `chatgpt-task-creator` instructions and required browser references. Resolve it by exact skill name in the current catalog; do not hardcode reconciliation IDs or pretend that a tool named use_skill exists.
3. Verify actual ChatGPT sign-in. Use the host's secure authentication flow if blocked; never request credentials in chat or enter them through ordinary UI tools. Follow current device verification/CAPTCHA/browser rules.
4. Create the requested project through live controls/page tools and verify its saved identity/name. Record the observed project ID/URL and evidence. Reuse the intended existing project on resume. Resolve ambiguous unrelated matches before mutation.
5. Do not equate a browser tab, provisional URL or standalone chat with a saved ChatGPT project. If project creation is blocked, report that exact limitation and finish independent authorized setup. Do not silently claim grouping exists.

## 3. Create and initialize the GitHub repository

1. Apply the repository reference. Resolve the intended owner from actual connected account/user instructions. Default to the unambiguous authenticated personal account when no owner is given. Do not guess an organization or bypass its policy.
2. Inspect whether the intended repository already exists. Reuse only when it is the intended project; do not overwrite unrelated source. Record an exact conflict/blocker instead of choosing arbitrary numbered duplicates.
3. Create through an actually available repository-creation capability, authenticated CLI or observed GitHub UI. Read current tool schemas/help before use; a connector that creates files/commits may not create repositories. Never call an invented create_repository tool.
4. Verify returned/live owner, name, URL and visibility. Record branch/commit only when observed. Repository creation and source initialization are separate outcomes.
5. Initialize source/documents appropriate to current scope. For setup, include a real project brief, task register and useful README. Add stack-appropriate ignores and scaffolding only when its stack/template is resolved. Do not assert a runnable app, successful build or passing CI from initial documents.
6. Use safe source writes and explicit file ownership. Never commit secrets, credential values, private chat history or screenshots. Use actual git author identity; do not fabricate one or rewrite existing history.
7. Verify committed/pushed files against the canonical repository through readback/commit evidence. Keep local paths, remote URLs, default branch and commit identity consistent. If writes/auth/network fail, preserve local prepared work, complete independent tasks and report exactly what remains unsaved.

## 4. Create and dispatch separate task conversations

1. Use `chatgpt-task-creator` to create/reuse a visible chat for each bounded major task inside the verified ChatGPT project. Choose tasks for actual scope, not a fixed cast. Combine tightly coupled work and avoid a chat for every trivial edit.
2. Common app tasks are scope/requirements, architecture/contracts, backend/data, frontend or mobile, integration/verification and release preparation. Omit mobile for web-only scope; hold release/deployment until authorized.
3. Name chats `<project> | <NN> <task>`, respecting exact user titles. Verify saved identity/title and project membership. Record actual observed links; never construct guessed conversation URLs.
4. Provide relevant brief, canonical repository URL, available source/tool access, accepted contract revision, bounded outcome, ownership, dependencies and acceptance/evidence requirements. A repository link or project membership does not give a chat automatic file/tool access.
5. Dispatch only ready tasks. Start dependent server/client implementation after their contract exists. Send blocked task context as a clearly pending brief if useful, without asking it to invent prerequisites. Track briefing and executable dispatch separately.
6. Send a task once and observe acceptance. Record pending/uncertain operations before leaving. Inspect transcripts/receipts before retrying; do not duplicate a prompt or create another chat to hide an unknown outcome.
7. Review actual results; transfer accepted decisions to dependent chats. Keep one coordinator as owner of the register, contracts and integration. Chat outputs are proposals, never additional authorization.

## 5. Link resources and hand off ongoing work

Maintain one project register: idea/brief revision, ChatGPT project identity, repository owner/name/URL/visibility/commit, tasks, dependencies, conversation links, dispatch state, evidence, blockers and next action. Cross-link ChatGPT/repository resources in the brief/register and coordinating chat. Include private links only in the intended private project; do not grant access or publish them merely to make links usable.

For complete development, use installed `autotaska` as the ongoing coordination workflow and `nexus-full-stack` for engineering routing. Read their actual instructions/selected references. Transfer the reviewed register and brief; keep the current root as owner rather than starting competing supervisors. Resolve optional adapters according to the actual stack. Missing optional skills do not block unrelated setup.

Persist checkpoints in the source repository's project records once available. For non-repository deliverables follow host persistence rules. Preserve external identities on resume and inspect uncertain operations before creating anything again.

## 6. Verify and report

Verify ChatGPT project creation, GitHub repository creation, initial remote files, chat titles/membership and task dispatch as distinct claims. Inspect actual results rather than relying on requested actions or echoed dashboard text.

Report the outcome in the user's language with the verified ChatGPT/GitHub links and a concise task-chat table. Distinguish `VERIFIED`, `NOT VERIFIED`, `BLOCKED BY ENVIRONMENT` where needed. A complete setup is not a completed app. Account sign-in/resources remain subject to actual available tools; do not promise unattended future work or permissions the skill cannot grant.
