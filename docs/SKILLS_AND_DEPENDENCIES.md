# Skills and dependencies

Keep every skill under `skills/<skill-name>/`. Preserve its exact name and internal paths so linked instructions, scripts, assets and integrity hashes continue to resolve. Select skills by task scope rather than loading the entire collection.

## Coordination layers

| Skill | Main dependencies | Responsibility |
| --- | --- | --- |
| `project-creator` | `chatgpt-task-creator` and authenticated project/GitHub capabilities | Set up real resources, briefs and bounded task conversations. |
| `autotaska` | `nexus-full-stack`, `chatgpt-task-creator` and relevant engineering skills | Lead execution, integrate results and monitor evidence during active runs. |
| `chatgpt-task-creator` | Authenticated ChatGPT project/conversation capabilities | Coordinate visible conversations and accepted contract revisions. |
| `nexus-full-stack` | Bundled OWL, router, workflow references and selected personal skills | Select phase-specific engineering knowledge and verification obligations. |
| `full-stack` | All four `template-*` skills when the requested scope requires them | Coordinate Template architecture, backend, frontend and verification. |

## Engineering layers

| Skill | Bundled support | Use |
| --- | --- | --- |
| `template-architecture` | Architecture references, `scripts/scaffold.py`, `assets/blank-project` | Scaffold and extend the modular single-host structure. |
| `template-backend` | Backend contracts and implementation rules | Domain, application, persistence, API and server authorization. |
| `template-frontend` | Frontend contracts and publishing rules | React/Blazor routes, real API data and interface states. |
| `template-verification` | Verification matrix | Proportionate checks and factual delivery evidence. |
| `professional-interface-builder` | Interface references and audit script | Product interface quality and production integration. |

## Supporting packages

`find-skills` provides ecosystem discovery. `mahoer` remains an experimental placeholder with no established delivery workflow. Neither is required merely to execute NEXUS.

NEXUS includes 25 pinned upstream engineering workflows inside `references/upstream/`. These are selectively loaded references, not 25 additional independently installed personal skills. Preserve upstream attribution and the MIT notice.

## Package resources

| Resource | Purpose |
| --- | --- |
| `SKILL.md` | Trigger metadata and operating instructions |
| `agents/` | Host-facing display metadata |
| `references/` | Contracts and guidance loaded when needed |
| `scripts/` | Deterministic operations and validators |
| `assets/` | OWL, task schemas, templates and output resources |

Install whole skill folders. Do not flatten all files into one directory, rename the original skill names or copy only their entry points. External tools, accounts and framework runtimes remain explicit prerequisites; the collection does not supply credentials.

## Ontology maintenance

Edit `skills/nexus-full-stack/assets/nexus.owl` as the canonical knowledge model. Regenerate `graph.json` and the Turtle mirror with `compile_graph.py`, then run `validate.py` and `test_router.py`. Workflow hashes intentionally prevent unnoticed drift. Keep the original contract, evidence and budget semantics when extending the model.
