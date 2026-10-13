---
name: template-frontend
description: Build or integrate React TypeScript Vite and Blazor interfaces in Template single-host ASP.NET Core projects. Use for ClientApp pages, browser routing, real API wiring, shared Blazor services and frontend publishing.
---

# واجهات Template

اقرأ [عقد الواجهات](references/frontend-contracts.md). افحص التصميم وعقد API والصفحات الحالية قبل التعديل.

1. ضع React داخل src/App.Server/ClientApp فقط، وBlazor داخل Components. حافظ على الهوية البصرية المتفق عليها.
2. وزّع الصفحات في pages والميزات في features والعناصر المشتركة في components. اجعل api نقطة اتصال HTTP، وtypes للعقود، وauth لحالة الجلسة. تجنب نسخ components متكررة.
3. اربط البيانات بـASP.NET API حقيقية؛ لا تستخدم mock أو localStorage كمصدر لبيانات العمل أو الدخول. يمكن استخدام تخزين محلي لتفضيلات العرض غير الحساسة إذا سمح المشروع.
4. استخدم BrowserRouter وروابط URL حقيقية، وحدد مساحة Blazor مستقلة. اختبر فتح الرابط مباشرة وتحديثه والرجوع منه.
5. أضف حالات التحميل والفراغ والخطأ وإعادة المحاولة المناسبة. لا تعرض بيانات وهمية عند فشل الطلب.
6. استخدم نفس هوية الخادم وصلاحياته في React وBlazor؛ القيود البصرية مساعدة فقط.
7. اختبر type-check وbuild والعرض والتنقل على الجوال والكمبيوتر. إذا طلبت العربية/الإنجليزية أو الوضعين فاتبع مصفوفة الحالات في المرجع.
8. أبقِ إنتاج React في wwwroot وداخل مخرجات نشر الخادم الواحد. لا تنشر Vite كخادم إنتاج مستقل.

عند طلب قالب فارغ، أبقِ الصفحات فارغة؛ لا تضف لوحة تحكم أو بيانات نموذجية أو تسجيل دخول تجريبي.
