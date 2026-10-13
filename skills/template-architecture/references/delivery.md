# Delivery contract

For a blank request, deliver infrastructure skeleton only, no sample business modules or invented product screens. Preserve empty extension folders and explain database/auth setup remains to be implemented when requested.

For a feature request, map each acceptance criterion to actual API, persistence, UI and verification evidence. Include changed paths, setup commands, environment variable names without values, migration notes, tests run, and known blockers. Distinguish VERIFIED, NOT VERIFIED, BLOCKED BY ENVIRONMENT.

For portability, keep SKILL.md frontmatter (name and description), relative references, assets and scripts together. Do not embed machine-specific skill checkout paths. Other assistants can read Markdown directly; automatic skill discovery, tool access and code execution depend on that assistant. Never promise universal automatic compatibility.

Example requests:
- «أنشئ مشروعًا فارغًا باسم Mizan بنفس معمارية Template» → generate skeleton, no users/orders.
- «أضف إدارة الطلبات إلى المشروع الحالي» → inspect existing contracts, implement one real authorized feature end to end.
- «غيّر الاسم فقط» → inspect rename mapping, preserve data and design, verify references.
- «جهّز للنشر» → produce and verify an artifact; publishing externally requires user authorization when not already requested.
