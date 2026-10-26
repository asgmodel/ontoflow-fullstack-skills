# Data engineering

Inspect the real schema, migration history, database version and query paths.
Define entities, relationships, constraints, indexes, ownership and retention
from actual requirements. Enforce invariants at suitable application and database
boundaries; use parameterized queries and least-privilege credentials.

Define transaction and concurrency behavior, idempotency and retry handling.
Avoid unbounded reads, accidental N+1 queries and indiscriminate indexing. Measure
query plans and actual workload before a performance claim.

For schema changes create a native versioned migration. Test creation from an
empty database and upgrade from a representative prior schema in an isolated
environment. Plan compatibility, backfill, rollback or forward recovery and data
validation. Production migration requires the session's actual authorization.

Development seed data must be requested/needed, deterministic and idempotent,
with production disabled by default. Never ship seed credentials or fake business
storage as an integration substitute. Record real database checks separately
from in-memory/unit tests and report inaccessible databases as unverified.
