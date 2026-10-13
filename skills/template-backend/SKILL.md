---
name: template-backend
description: Implement or review Template ASP.NET Core APIs, Domain and Application layers, EF Core SQL Server migrations, authentication, authorization, AI integrations, notifications and background jobs. Use for backend features in Template-derived projects.
---

# خلفية Template

اقرأ [عقود التنفيذ](references/backend-contracts.md) قبل العمل. افحص الكود الحالي والنسخ وعقد البيانات؛ لا تستنتج وجود خدمة من اسم مجلد.

1. ضع الكيانات وقواعد الأعمال في Domain؛ ضع DTOs والواجهات والتحقق وحالات الاستخدام في Application.
2. ضع تطبيق الواجهات وDbContext والتكاملات في Infrastructure. أبقِ قاعدة واحدة وسجل الخدمات في Extensions. أبقِ Controllers رفيعة تحت /api/v1.
3. عرّف الطلب والاستجابة والأخطاء والتصفح والصلاحيات قبل ربط الواجهة. استخدم DTOs ولا تُرجع كيانات EF مباشرة. مرّر CancellationToken في عمليات I/O.
4. أضف EF configurations والقيود والفهارس؛ أنشئ migration فعلية ثم اختبر قاعدة فارغة وترقية قاعدة موجودة في بيئة معزولة. لا تستخدم EnsureCreated أو ALTER TABLE عند بدء الإنتاج.
5. طبّق التحقق والصلاحيات وعزل المالك على الخادم. استخدم هوية المستخدم المسجلة؛ لا تثق في userId أو role القادمة من العميل.
6. أبقِ أسرار Google وAI وSQL على الخادم، ولا تمررها في VITE_* أو سجلات الطلبات.
7. أضف اختبارات قواعد الأعمال والوصول غير المصرح والبيانات غير الصحيحة والأخطاء المهمة. لا تستخدم Assert.True(true) كدليل.
8. سلّم نتيجة فعلية؛ ميّز التنفيذ عن الإعداد الذي يحتاج بيانات اعتماد أو خدمة خارجية.

عند طلب هيكل فارغ فقط، استخدم template-architecture ولا تملأه بكيانات افتراضية. لا تغيّر المعمارية إلى عدة خوادم أو Backend داخل ClientApp.
