---
name: template-verification
description: Verify and prepare Template projects for handoff, CI and single-host deployment. Use for architecture audits, meaningful tests, SQL migration verification, React build/publish checks and honest readiness reports.
---

# تحقق Template

اقرأ [مصفوفة التحقق](references/verification.md). افحص الأدوات المتاحة قبل التنفيذ وسجل الأدلة الفعلية.

1. راجع اتجاه الاعتماد ومسارات الطبقات: Domain مستقل، Application عبر interfaces، Infrastructure للتنفيذ، Controllers رفيعة، ClientApp للواجهة فقط.
2. افحص الإعدادات والأسرار والمصادقة والمسارات وعقود API. فرّق بين المطلوب في المستندات والمنفّذ فعليًا.
3. نفّذ فحوص البناء والاختبارات والنشر ذات الصلة بالتغيير. لا توسع الفحص بلا سبب بعد تحقق المخاطر المطلوبة.
4. تحقق من قاعدة جديدة والترقيات وعزل المستخدمين إذا تغيّرت البيانات أو الصلاحيات؛ استخدم بيئة اختبار معزولة.
5. افحص مجلد النشر وتشغيل الخادم الواحد وReact وBlazor والصحة. لا تعتبر وجود ملف نجاحًا للتشغيل.
6. أبلغ بالتصنيفات VERIFIED وNOT VERIFIED وBLOCKED BY ENVIRONMENT، مع سبب وخطوة لازمة لكل بند غير متحقق.
7. لا تنشر لخدمة خارجية أو تطبق migration على الإنتاج إلا إذا شمل الطلب هذا الإجراء.

عند مراجعة قالب فارغ، غياب وظائف الأعمال مقصود وليس عيبًا؛ غياب التحقق الفعلي يجب التصريح به. مهارة Template نفسها لا تحتاج Node أو .NET لقراءة تعليماتها، لكن المشروع الناتج يحتاجهما للبناء.
