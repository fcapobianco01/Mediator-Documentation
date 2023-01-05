| Source (name [type]) | Field (index [id]) | Source Location                          | Label at Source             |
|----------------------|--------------------|------------------------------------------|-----------------------------|
| file                 |                    | security/apparmor/lsm.c:459              | object, dynamic, input      |
| cmd                  |                    | security/apparmor/lsm.c:459              | operation, dynamic, input   |
| 1024 [AA_MAY_LOCK]   |                    | security/apparmor/lsm.c:461              | operation, static, mediator |
| 17 [OP_FLOCK]        |                    | security/apparmor/lsm.c:466              | operation, static, mediator |
| 1 [F_WRLCK]          |                    | security/apparmor/lsm.c:463              | all, static, external       |
| 2 [MAY_WRITE]        |                    | security/apparmor/lsm.c:464              | all, static, external       |
| 0 [MS_NOUSER]        |                    | security/apparmor/include/apparmor.h:117 | all, static, external       |
| current              |                    | security/apparmor/include/context.h:99   | subject, dynamic, external  |

