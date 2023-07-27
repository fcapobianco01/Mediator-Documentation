| Source (name [type]) | Field (index [id]) | Source Location                          | Label at Source             |
|----------------------|--------------------|------------------------------------------|-----------------------------|
| path                 |                    | security/apparmor/lsm.c:347              | object, dynamic, input      |
| mode                 |                    | security/apparmor/lsm.c:347              | operation, dynamic, input   |
| 12 [OP_CHMOD]        |                    | security/apparmor/lsm.c:352              | operation, static, mediator |
| 256 [AA_MAY_CHMOD]   |                    | security/apparmor/lsm.c:352              | operation, static, mediator |
| 0 [MS_NOUSER]        |                    | security/apparmor/include/apparmor.h:117 | all, static, external       |
| current              |                    | security/apparmor/include/context.h:99   | subject, dynamic, external  |