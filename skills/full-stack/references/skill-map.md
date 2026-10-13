# Skill resolution and handoffs

| Exact skill name | Load for | Produce for next stage |
| --- | --- | --- |
| template-architecture | New skeleton, layer placement, naming, structural change | Actual project path/name, layer map, constraints and scope |
| template-backend | Domain, use cases, data, APIs, identity and providers | Implemented API contracts, migrations, DI, authorization and error behavior |
| template-frontend | React/Blazor, API consumption, routing and requested UX | Pages connected to those contracts; loading/error/session behavior |
| template-verification | Architecture review, meaningful tests, build, publish and readiness | Actual command results, integration evidence and precise blockers |

## Resolve without fragile paths

Use skill locators in the active skill catalog first. If an installed skill is absent from the current catalog, locate it by the exact `name` YAML frontmatter among personal skills, using the skill-creator workflow and the active personal-skills checkout. Its normal root is `/root/.codex/skills/remote-skills`; reconciled directories may be named `skill-<id>`. Do not hardcode an ID or assume that a directory matches the display name. Read the resolved SKILL.md and follow relative links from its own directory.

On another AI platform, use its configured skill directories or the skill folders supplied by the user. No ChatGPT-only integration is required to read the Markdown. Automatic discovery and execution depend on the platform.

If missing, distinguish missing from installed-but-disabled. Do not claim a skill was loaded or re-enable it without authorization. Continue independent work using the constraints in Full Stack; identify exactly which missing skill or asset blocks remaining work. If new skeleton generation needs missing assets, request the relevant skill package rather than inventing a matching template. Do not stop an unrelated existing-project fix merely because a scaffold is unavailable.

## Choose the smallest complete workflow

- Blank project: architecture → relevant verification; no business entities, login or invented dashboard.
- Complete new product: architecture → backend/frontend per feature → verification → delivery.
- Existing end-to-end feature: inspect architecture → backend contract and implementation → frontend integration → targeted verification.
- UI-only fix: frontend → targeted verification; inspect API only if the change crosses its boundary.
- Backend-only fix: backend → targeted verification; inspect frontend consumers if the contract changes.
- Review-only request: architecture and verification as relevant; report findings without editing.

Full Stack owns coordination, scope and completion. Specialized skills own their detailed implementation rules. Do not recursively hand coordination back from architecture to Full Stack. Treat architecture references to backend/frontend/verification as steps in the current workflow, not another independent run. Resolve conflicts using the instruction hierarchy and user's current scope, and explain material architectural conflicts instead of silently switching technologies.
