| Source (name [type]) | Field (index [id]) | Source Location                          | Label at Source             |
|----------------------|--------------------|------------------------------------------|-----------------------------|
| dir                  |                    | security/apparmor/lsm.c:276              | object, dynamic, input      |
| dentry               |                    | security/apparmor/lsm.c:276              | object, dynamic, input      |
| mode                 |                    | security/apparmor/lsm.c:276              | operation, dynamic, input   |
| 6 [OP_MKNOD]         |                    | security/apparmor/lsm.c:279              | operation, static, mediator |
| current              |                    | security/apparmor/include/context.h:99   | subject, dynamic, external  |
| 0 [MS_NOUSER]        |                    | security/apparmor/include/apparmor.h:117 | all, static, external       |
| 16 [AA_MAY_CREATE]   |                    | security/apparmor/lsm.c:379              | operation, static, mediator |
| current              |                    | security/apparmor/lsm.c:251              | subject, dynamic, external  |