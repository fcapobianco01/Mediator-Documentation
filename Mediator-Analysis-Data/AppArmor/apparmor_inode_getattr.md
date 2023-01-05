| Source (name [type])     | Field (index [id]) | Source Location                          | Label at Source             |
|--------------------------|--------------------|------------------------------------------|-----------------------------|
| mnt                      |                    | security/apparmor/lsm.c:367              | object, dynamic, input      |
| dentry                   |                    | security/apparmor/lsm.c:367              | object, dynamic, input      |
| 17 [OP_GETATTR]          |                    | security/apparmor/lsm.c:372              | operation, static, mediator |
| 128 [AA_MAY_META_READ]   |                    | security/apparmor/lsm.c:372              | operation, static, mediator |
| 0 [MS_NOUSER]            |                    | security/apparmor/include/apparmor.h:117 | all, static, external       |
| current                  |                    | security/apparmor/include/context.h:99   | subject, dynamic, external  |