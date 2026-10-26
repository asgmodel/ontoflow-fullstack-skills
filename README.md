# Full Stack Engineering

حزمة هندسة Full Stack تستخدم **OntoLink الخارجية** لإدارة دورة العمل، مع معرفة هندسية منتقاة وعقود ومهام وأدلة فعلية. لا تُضمّن نسخة من OntoLink أو وسيطها أو أنطولوجيتها أو مراحلها.

## البنية

| المسار | المسؤولية |
| --- | --- |
| [`skills/software-engineering/`](skills/software-engineering/SKILL.md) | مهارة هندسة البرمجيات الكاملة، والتوجيه، والمراجع، والقالب الاختياري |
| [`skills/ontolink-skills/`](skills/ontolink-skills/README.md) | تعليمات فقط لطلب وتحميل/تحديث OntoLink من مستودعها الأصلي |

## التثبيت والتحميل الديناميكي

ثبّت مهارة الهندسة من هذا المستودع:

```sh
npx skills add https://github.com/asgmodel/ontoflow-fullstack-skills --skill software-engineering --global --yes
```

عند بداية كل جلسة مشروع، اطلب مهارة OntoLink الأصلية من مدير مهارات المضيف وحدّث **هذه المهارة وحدها**. مع Skills CLI:

```sh
npx skills add https://github.com/asgmodel/ontolink-skills --skill ontolink-skills --global --yes
```

`--global` يبقي المهارة مشتركة خارج مستودع التطبيق. يدعم الأمر تحديد المضيف عبر `--agent`. عند استخدام مدير مهارات مختلف، استدعِ المهارة وحدّثها من المصدر الرسمي من خلاله. لا تعِد نسخها إلى مجلد الربط.

بعد التحديث اقرأ `SKILL.md` الحالي لـOntoLink والعقود والمرحلة المطلوبة منه. عيّن `ONTOLINK_SKILL_ROOT` إلى موقع الحزمة الخارجية الفعلي، أو استخدم `--coordinator-root`. يعثر المحلّل أيضًا على التثبيتات العالمية المعروفة بالاسم، بما يشمل معرفات المجلدات التي يولدها المضيف والروابط الرمزية.

```sh
python <engineering-root>/scripts/dependency.py
```

المحلّل يحدد الموقع فقط؛ تحديث المهارة يحصل بواسطة مدير المهارات قبل بدء الجلسة. إذا تعذر التحديث، يصرّح الوكيل بالسبب وحالة حداثة النسخة المتاحة. لا يُدّعى تحديث لم يحدث، ولا يُنشأ بديل مضمّن. تحديث الاعتمادية لا يحذف حالة المشروع أو يعيدها إلى البداية.

## دورة العمل

OntoLink الخارجية تدير الاكتشاف والمعمارية والتخطيط والتنفيذ والتحقق والتسليم والمتابعة. استخدم أوامر bootstrap/context/record وتعليمات المرحلة من **موقعها الخارجي الحالي**. لا تشغّل مثبتًا ينسخ OntoLink إلى التطبيق لمجرد استخدام هذه الحزمة.

تظل `knowledge.owl` الحالة الأساسية للمشروع، أو المسار الصريح الموجود. سجلات `.ontolink/records/` والمخرجات والأدلة تبقى بجوار الحالة. كتابة الحالة وقبول الإنجاز من مسؤولية وسيط OntoLink وحده. تحديث المهارة منفصل عن تحديث حقائق المشروع.

## توجيه المعرفة الهندسية

أنشئ إدخالًا يصف النطاق الفعلي؛ المرحلة تُستخرج من المهمة المؤهلة في الحالة الخارجية:

```json
{
  "intent": "feature",
  "profile": "existing-stack",
  "layers": ["frontend", "backend", "data"],
  "tags": ["auth", "data", "contract"]
}
```

```sh
python <engineering-root>/scripts/route.py \
  --task <task-input.json> --state <project>/knowledge.owl \
  --coordinator-root <current-external-ontolink-root>
```

الموجّه يستدعي الوسيط الخارجي في كل مرة ويتحقق من الأهلية والمراجعة الحالية، ثم يستخدم مطابقة المراحل في **أنطولوجيا الهندسة**. لا يطلب تعديل أنطولوجيا OntoLink الأصلية. عند تغير واجهة الاعتمادية بصورة غير متوافقة، يتوقف بخطأ واضح ويحافظ على الحالة.

## التحقق والصيانة

Python 3.10+ مطلوب للموجّه؛ التشغيل المعتاد يستخدم المكتبة القياسية. Skills CLI له متطلبات Node الخاصة بنسخته. حزم RDF التالية للصيانة فقط:

```sh
python -m venv .venv
.venv/bin/python -m pip install -r skills/software-engineering/scripts/requirements-maintenance.txt
.venv/bin/python scripts/check.py
```

لتشغيل اختبارات الربط، ثبّت أو حمّل OntoLink خارجيًا، ثم:

```sh
ONTOLINK_SKILL_ROOT=/absolute/external/ontolink-skills .venv/bin/python scripts/run_tests.py
```

CI يحمّل الإصدار الحالي من مستودع OntoLink إلى مجلد مؤقت **خارج checkout**، ويختبر الربط على Python 3.10 و3.12. لا تحفظ الاختبارات أو المصدر الخارجي داخل هذا المستودع.

بعد تعديل الأنطولوجيا أو المراجع المرتبطة بها:

```sh
.venv/bin/python skills/software-engineering/scripts/compile_graph.py
python scripts/manifest.py --write
.venv/bin/python scripts/check.py
```

راجع [المعمارية والإجراء](docs/architecture.md)، و[قائمة الملفات الضرورية](docs/file-inventory.md)، و[المصادر](THIRD_PARTY_NOTICES.md). يحافظ التنفيذ على تقنيات المشروع؛ قالب ASP.NET/React/Blazor اختياري. تشغيل التطبيقات والنشر والمراقبة المستمرة يحتاج أدواته وأدلته الفعلية.
