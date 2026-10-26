# Security engineering

Identify actual trust boundaries: user/session, role, tenant, uploaded content,
server/provider and deployment configuration. Tie threats and acceptance checks
to the affected features. Preserve established authentication architecture.

Verify authorization on every protected operation; test anonymous, wrong-role,
cross-owner and cross-tenant attempts where applicable. Validate inputs on the
server, encode output, constrain uploads and protect file/download ownership.
Use the framework's supported session, CSRF and security mechanisms.

Keep secrets out of source, graph records, evidence and client bundles. Use
least-privilege provider/database access, validate callbacks/webhooks, and bound
request size, timeouts, retries and abuse controls as required by the product.
Inspect dependencies/configuration with available tools; do not claim that
routing tags or static checks constitute a complete security audit.

Record unresolved material risks and blockers against affected graph nodes.
An unavailable credential is a prerequisite to resolve, never justification for
fake authentication or bypassing server checks.
