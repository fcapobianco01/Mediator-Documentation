| Source (name [type])   | Field (index [id]) | Source Location                             | Label at Source             |
|------------------------|--------------------|---------------------------------------------|-----------------------------|
| path                   |                    | security/apparmor/lsm.c:282                 | object, dynamic, input      |
| 7 [OP_TRUNC]           |                    | security/apparmor/lsm.c:291                 | operation, static, mediator |
| current                |                    | security/apparmor/include/context.h:99      | subject, dynamic, external  |
| 0 [MS_NOUSER]          |                    | security/apparmor/include/apparmor.h:117    | all, static, external       |
| 2 [MAY_WRITE]          |                    | security/apparmor/lsm.c:291                 | all, static, external       |
| 64 [AA_MAY_META_WRITE] |                    | security/apparmor/lsm.c:291                 | operation, static, mediator |