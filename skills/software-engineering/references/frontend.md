# Frontend engineering

Preserve the approved design and native framework. Inventory required routes,
roles, primary actions and data sources before replacing existing UI. Keep one
canonical component tree and a centralized API client/contract boundary.

Implement real loading, empty, validation, error, retry, permission-denied,
session-expired and success states as applicable. Cancellation, duplicate submits
and cache invalidation must reflect actual server results. Never show fake
success or silently replace failed business requests with fixtures.

Read [design-system.md](design-system.md) when changing visual language and
[product-integration.md](product-integration.md) for existing-product integration.
Apply requested locales, direction and themes throughout scope; test responsive
layouts, keyboard navigation, labels, focus, contrast and reduced motion. Add
portals and locales only when required by the product.

Trace page action -> typed client -> real endpoint -> persistence/provider ->
response -> refreshed view. Verify direct URL entry, reload and back navigation.
UI route guards complement server authorization. Keep credentials out of bundles
and browser storage. Presentation preferences may use local storage when allowed.

Run type/build and browser checks supported by the environment. Read
[qa-and-evidence.md](qa-and-evidence.md) for substantial UI work; for the optional
ASP.NET profile read [frontend contracts](profiles/aspnet-frontend-frontend-contracts.md).
