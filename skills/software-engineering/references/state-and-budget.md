# State, freshness and context accounting

Use the project's canonical OntoLink `knowledge.owl` exclusively for operational
state. JSON task inputs, generated context/index and distribution catalogs are
transport or navigation data. Do not create another task register or completion
ledger. Store long documents/proof files beside the state under `.ontolink/`.

Register acceptance, contracts, decisions, actors, tasks, artifacts and evidence
through the mediator. Link dependencies explicitly and use the observed revision.
After changing an artifact register its current hash and impact, rerun affected
checks and query fresh context. Missing/stale evidence is unknown, not success.

Load the current phase and selected engineering workflows, then relevant source
and contracts. Never drop authorization, security, blockers or evidence facts to
meet a budget. The packet accounting is static instruction cost plus an explicit
project reserve; it excludes conversation, tool output and linked material. With
no tokenizer it uses labelled UTF-8 bytes/3 estimation. Neither OWL nor a context
cache guarantees token savings or removes host conversation history.
