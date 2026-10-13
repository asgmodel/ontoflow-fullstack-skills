# GitHub repository workflow

## Capability selection

Inspect current tools for repository creation. File/blob/tree/commit/branch/PR creation does not imply permission/capability to create a repository. Use an available sufficient connector first. Otherwise use a permitted authenticated GitHub CLI or browser workflow. Inspect current help/UI; do not make unsupported API calls or install tools just to assume access.

If a sufficient connector fails or appears unavailable, follow host fallback rules. If it simply lacks repository creation, a permitted browser/CLI route can fulfill that unsupported operation. Do not request the user to paste a token/password in chat.

## Identity and conflicts

Use the instructed owner; otherwise use the unambiguous authenticated personal account. Keep organizations subject to actual user intent/policies. Choose a clear compatible slug from the project name and default visibility to private unless instructed otherwise.

Look up the exact owner/name before creation. Reuse when the existing repository belongs to the intended project. If it is unrelated, preserve it and resolve the naming decision. Never overwrite, delete, change visibility or create numbered duplicate repositories as an automatic fix.

After creation inspect actual owner/name/visibility/URL and record the observed identity. Confirm default branch/initialization separately. Never claim a remote exists from a local git init or failed create receipt.

## Initial content

For setup, prepare a concise product README, docs/project/brief.md, docs/project/register.json and bounded task definitions. Put canonical contracts in their real repository formats/locations when agreed; mark drafts. Prepare AGENTS.md only when useful for actual source ownership/project rules, preserving existing instructions.

Use stack-appropriate source scaffolding and ignore rules only after stack resolution. Reuse the Template scaffold through its installed skill when that architecture is selected. Do not create fake endpoints, placeholder passing tests or dummy green CI. Do not add a license granting rights without the user's choice; repository privacy is the default.

Keep private source, credential values, uploaded personal records, browser screenshots and chat history out of initial commits unless specifically necessary and authorized. Use credential names in setup docs, never values. Verify files to stage; stage only intended project paths. Respect actual author identity and current branch; never force-push/rewrite existing history as routine setup.

## Source verification

Prefer supported repository mutations or ordinary git operations. Confirm upstream/default branch and safe remote provenance. After commit/push inspect the actual remote commit/files through available readback or matching commit evidence. A successful upload is distinct from a build or deployment.

If repository creation succeeded but initialization failed, retain the verified repo and pending initialization task. Do not delete it/recreate it. If local work is ready but remote access fails, preserve prepared files and report the unsaved remote outcome while continuing independent ChatGPT setup.
