# Ontology semantics

NEXUS is an OWL/RDF ontology with a constrained application router, not a list disguised as a graph. Skill, Capability, Phase, Role, Task, Artifact, Gate, Evidence, Decision, ProjectProfile, ContextPacket, Policy, Risk, Source, Intent and RoutingRule are distinct concepts. APIContract, DataSchema, UIComponent, TestSuite and DeploymentBundle specialize Artifact.

| Property | Meaning | Execution consequence |
| --- | --- | --- |
| requiresSkill | Workflow prerequisite | Deterministic dependency closure |
| implementsCapability | Skill provides a capability | Capability discovery and coverage queries |
| appliesInPhase | Workflow stage | Phase-aware loading |
| ownedBy | Responsible engineering perspective | Accountability, no automatic subagent spawn |
| producesArtifact / consumesArtifact | Contract production and consumption | Cross-layer handoff traceability |
| verifiedBy / needsEvidence | Artifact gate and supporting evidence | Completion must have actual evidence |
| invalidates / dependsOn | Directed artifact impact/dependency | Contract/schema changes stale dependent proofs |
| derivedFrom | Source origin | Provenance and version-aware refresh |
| constrainedBy | Applicable project policy | Stack preservation and budget integrity |

`requiresSkill` closure and `invalidates` closure are explicit application-level graph operations. No OWL reasoner is required or claimed in the routing runtime. SHACL provides closed-world constraints for catalog/rule integrity; OWL alone does not enforce field presence. The task JSON schema and router validation govern actual request inputs. Proposed runtime state/evidence are a separate instance graph, not fabricated evidence in the catalog.

OWL RDF/XML in `assets/nexus.owl` is authoritative. The router parses its named RDF/XML nodes on every invocation; the full graph is not placed in model context. The constrained reader supports the bundled export, not arbitrary RDF/XML or an OWL reasoner. Unsupported constructs are rejected. `compile_graph.py` produces `graph.json`, including the OWL SHA-256. Routing refuses a stale or mismatched integrity projection. Turtle is a generated mirror. Per-workflow hashes protect adapted bundled text. Original upstream hashes and commit live in sources.json. Personal skill names are resolved at execution; environment reconciliation IDs are deliberately excluded.

Selection: intent + current phase + profile + explicitly inspected layers/tags → roots → dependency closure → selected paths + gates + stale artifact closure. Add security for protected boundaries; contract design for contract changes; browser checks for UI; SQL checks for schema; root-cause debugging for failure; primary-source workflow for framework uncertainty. A blank scaffold does not inherit feature tests or invented auth. Review-only never grants write authorization. A schema change in UI-only scope is rejected rather than ignored. The router validates declarations; it cannot detect an authentication or schema boundary omitted by the classifying agent. Inspect code and acceptance criteria before supplying tags. Report undeclared/uncertain boundaries rather than presenting routing as a security scanner.

The catalog contains 30 mapped skills: 5 personal full-stack/Template skills plus 25 pinned upstream workflows. This package implements ontology routing and context accounting. The agent host still executes code, tools and verification; this is not a deployed autonomous application builder.

`--phase` selects a stage; it does not prove that earlier stages passed. Before advancing execution, the coordinator must inspect project acceptance, decisions, actual contracts and fresh evidence. Unresolved blockers remain blockers. The current runtime is deliberately read-only and does not implement a persistent state store, provider prompt cache, scheduler, production deployment service or automatic security scanner.
