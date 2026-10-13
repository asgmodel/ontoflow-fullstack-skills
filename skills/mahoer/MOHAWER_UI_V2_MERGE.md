# Mohawer UI v2 merge record

This package uses `mohawer.ui.v2(2).zip` as the visual and interaction reference and
`Mohawer-EF-complete-integrated-2026-09-15(1).zip` as the ASP.NET Core, EF Core, and
SQL Server reference.

The final runtime frontend is the single application under
`src/Mohawer.Server/ClientApp`. Its active entry point is `index.tsx` → `App.tsx`.
The approved UI styling is preserved in `index.css`; the asset files are kept under
`ClientApp/public`.

The source UI archive also contains an Express server, Firebase/Firestore adapters,
browser-local system data, and JSON demo databases. Those files are deliberately not
copied into the final runtime because the project contract requires ASP.NET Core and
SQL Server to be the only operational backend and source of truth. Their visible
flows are represented by the integrated components and real `services/api.ts` calls.

Included active UI areas:

- Authentication, registration, OTP, password reset, Google flow, and account security.
- Dashboard overview, practice, links, participants, submissions, templates, jobs,
  analytics, profile, tokens, quotas, users, plans, and advisor.
- Interview preflight, camera/microphone checks, screen sharing, live session,
  answer submission, completion, evaluation, and final report.
- Candidate invitation exchange, one-use session protection, loading/error states,
  Arabic/English direction, and light/dark themes.

The `FRONTEND_BACKEND_INTEGRATION_MATRIX.md` file maps the active screens to the
ASP.NET controllers, DTOs, services, and persisted SQL Server tables.
