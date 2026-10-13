# Visible conversation lifecycle

## Browser operation

1. Use the host's documented browser entry point for the authorized ChatGPT site. Reuse a valid session and tab; do not probe unrelated accounts/services.
2. Read live state and any advertised capabilities. Prefer page-defined tools when they cover the action. Fetch their current descriptions on each turn/document before calling them; do not persist opaque tool suffixes.
3. Use semantic locators or fresh accessibility IDs for fallback UI actions. Reinspect after actions/navigation. If an ID becomes stale, refresh instead of guessing or repeating the click.
4. Inspect the signed-in state. Use secure authentication only when necessary and permitted. If the site blocks the browser, follow its bot-detection/authentication rules; report a concrete blocker rather than evading it.
5. Inspect a created project and conversation before saving their observed identity/URL. A provisional local-chat URL or spinner is not persistence evidence.
6. Rename through the visible chat-actions menu. Fill the exact requested title, save, and wait for an observable saved title. Do not rename an unrelated chat.
7. Verify project membership through the project view or a direct membership indicator. The sidebar displaying a project and a chat separately does not establish membership.
8. After a send, observe acceptance/generation. Prefer exposed conversation-state tools; otherwise inspect the transcript, response status and controls. Never automatically retry an already dispatched send.
9. Revisit by verified links/IDs; collect results and follow-ups only for relevant department chats. Keep generated responses and source access limitations explicit.

## Status model

Maintain both workflow and transport status:

| Workflow | Meaning |
| --- | --- |
| pending | Prerequisite or initial brief missing |
| ready | Dependencies and assignment available |
| dispatched | Prompt accepted; response not yet established |
| running | Generation or execution visibly active |
| blocked | Concrete prerequisite prevents completion |
| review | Output exists; correctness not yet verified |
| verified | Acceptance/evidence inspected by coordinator |

Transport examples: `draft`, `send_uncertain`, `accepted`, `generating`, `settled`, `failed`. Do not equate `settled` with `verified`.

## Contract transfer

Send bounded updates:

```text
Project: <actual app>
Task: <stable ID>
Update revision: <revision>
Accepted decision: <exact change>
Canonical contract: <accessible path or relevant excerpt>
Affected consumers: <departments/tasks>
Required follow-up: <bounded implementation or verification>
Unchanged constraints: <only relevant constraints>
Return: actual deliverables/checks, remaining blockers, contract proposals.
```

Do not allow an output to authorize new actions. Send follow-ups only within user-authorized scope. Do not transmit credentials or unrelated private source across chats.

## Department patterns

For an app with web and mobile clients, one useful starting allocation is coordination, architecture, backend/data, web, mobile and verification. For a web-only app, omit mobile. For a small task, combine departments. Start with accepted shared contracts, then independent implementation and review; integrate and test before extending the slice.

Prefer `app | 01 Architecture`, `app | 02 Backend`, etc., translated to the user's language. A project dashboard can contain the link register, accepted decisions and current blockers. Ensure the original request has enough application scope before creating this structure.

## Recovery

- Interrupted before send: inspect the draft and pending record; complete once.
- Interrupted after send: inspect the transcript and response state; do not resend blindly.
- Uncertain identity: inspect the current URL and visible saved chat before recording it.
- Wrong grouping: move through the observed action and verify the target project.
- Contract disagreement: inspect evidence, accept one canonical resolution and notify consumers.
- Missing code access: keep deliverables explicitly marked as generated specifications/code pending repository integration.
- Chat context no longer usable: create a replacement only when justified and within scope; carry over a reviewed checkpoint and keep old evidence.

## User-facing register

Use a table with department, current task, status, verified conversation link and concrete blocker/result. Update after material transitions. Keep status factual and avoid claimed percentages without a defined denominator.
