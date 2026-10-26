# OntoLink Software Engineering

منظومة هندسة برمجيات قائمة على الأنطولوجيا: **منسّق واحد، حالة مشروع واحدة، ومهام مرتبطة بعقود وأدلة فعلية**.

## الحزمتان

| الحزمة | المسؤولية |
| --- | --- |
| [`ontolink-skills`](skills/ontolink-skills/SKILL.md) | إدارة الاكتشاف والمعمارية والتخطيط والتنفيذ والتحقق والتسليم والمتابعة |
| [`software-engineering`](skills/software-engineering/SKILL.md) | المعرفة الهندسية للخلفية والواجهات والبيانات والأمن والاختبارات والتشغيل |

تحتوي الحزمة الأولى سبعة إجراءات مراحل داخلية. تحتوي الثانية مراجع هندسية منتقاة وقالب ASP.NET/React/Blazor اختياريًا. يحافظ العمل على تقنيات المشروع الموجود. اختُصرت طبقات التنسيق المتكررة، وأُزيلت أدوات إدارة المحادثات والمهارات التجريبية من هذه الحزمة.

## التثبيت والاستخدام

Python 3.10+ مطلوب للوسيط والتوجيه؛ التشغيل المعتاد يستخدم المكتبة القياسية فقط.

```sh
git clone https://github.com/asgmodel/ontoflow-fullstack-skills.git
cd ontoflow-fullstack-skills
python skills/ontolink-skills/scripts/project_setup.py \
  --project /absolute/path/to/application --skills-dir .agents/skills
```

الأمر يثبّت **الحزمتين معًا**، ويحفظ التعليمات الموجودة، وينسخ قواعد المشروع، وينشئ أو يعيد استخدام الحالة. استخدم مجلد المهارات المناسب لأداة الوكيل لديك. للتحديث شغّل الأمر نفسه من نسخة المصدر المحدّثة؛ يحتفظ بنسخ احتياطية من الملفات المستبدلة.

للحالة الموجودة في مسار صريح أضف `--state relative/path.owl` في التثبيت وكل أوامر المشروع. لا تنشئ حالة ثانية.

من داخل المشروع المستهدف:

```sh
python .rule/ontolink.py start --root . \
  --skill-root .agents/skills/ontolink-skills
```

اطلب من الوكيل: «استخدم `$ontolink-skills` لتنفيذ المهمة الحالية، وطبّق `$software-engineering` على المهمة المؤهلة، مع حفظ العقود والأدلة في الأنطولوجيا». عند غياب استدعاء المهارات في الأداة، اطلب قراءة ملفي `SKILL.md` مباشرة. أسماء الاستدعاء تختلف بحسب المضيف.

## توجيه المعرفة الهندسية

أنشئ ملف إدخال يصف النطاق الفعلي؛ لا تحتاج تحديد المرحلة لأنها مشتقة من حالة OntoLink:

```json
{
  "intent": "feature",
  "profile": "existing-stack",
  "layers": ["frontend", "backend", "data"],
  "tags": ["auth", "data", "contract"]
}
```

ثم شغّل من المشروع:

```sh
python .agents/skills/software-engineering/scripts/route.py \
  --task .ontolink/artifacts/task-input.json --state knowledge.owl \
  --coordinator-root .agents/skills/ontolink-skills
```

التوجيه يتحقق من الحالة الحالية وأهلية المهمة ويعرض المراجع والفحوص المطلوبة؛ تنفيذ المهمة وتسجيل دليلها عمل الوكيل. لا يمكن اختيار مرحلة تنفيذ لاحقة لتجاوز الاعتماديات. يمكن استخدام `--focus-task task-id` لمهمة فرعية مؤهلة.

## تنظيم ملفات المشروع

| المسار بجوار الحالة الأساسية | الغرض |
| --- | --- |
| `knowledge.owl` | الحقائق والمهام والعلاقات وحالة الإنجاز |
| `.ontolink/records/` | مدخلات السجل وإيصالات المراجعات |
| `.ontolink/artifacts/` | المتطلبات والعقود والخطط والمخرجات النصية |
| `.ontolink/proofs/` | نتائج الفحوص والأدلة |
| `.ontolink/context.json` | سياق مولّد يمكن إعادة بنائه |
| `.ontolink/index/` | فهرس كود اختياري للملاحة فقط |

يتطلب إغلاق المهمة مخرجًا حاليًا ودليل PASS مطابقًا له، مع اكتمال الاعتماديات وحل العوائق. تغيير المتطلبات أو العقود أو المخرجات يعيد فتح العمل المتأثر. التوزيع يحدد مسؤولًا واحدًا ومخرجًا ومعيار قبول وملكية ملفات لكل مهمة.

## التحقق من المستودع

حزم RDF مخصصة للصيانة والتحقق من النماذج، وليست لازمة للتشغيل المعتاد:

```sh
python -m venv .venv
.venv/bin/python -m pip install -r skills/software-engineering/scripts/requirements-maintenance.txt
.venv/bin/python scripts/check.py
.venv/bin/python scripts/run_tests.py
```

بعد تعديل الأنطولوجيا أو المراجع المرتبطة بها:

```sh
.venv/bin/python skills/software-engineering/scripts/compile_graph.py
.venv/bin/python scripts/compile_lifecycle.py
python scripts/manifest.py --write
.venv/bin/python scripts/check.py
.venv/bin/python scripts/run_tests.py
```

راجع [المعمارية والإجراء](docs/architecture.md)، و[قائمة الملفات الضرورية](docs/file-inventory.md)، و[إشعارات المصادر](THIRD_PARTY_NOTICES.md). يسجل `MANIFEST.json` الملفات وبصماتها دون تضمين ادعاءات ثابتة بنجاح اختبارات.

هذه الحزمة تنسّق عمل الوكيل وتتحقق من السجل والتوجيه؛ تشغيل التطبيق الناتج والنشر والمزودات الخارجية تحتاج أدواتها وأدلتها الفعلية. المتابعة تتم أثناء العمل والاستئناف؛ المراقبة المستمرة تحتاج خدمة مجدولة فعلية.
