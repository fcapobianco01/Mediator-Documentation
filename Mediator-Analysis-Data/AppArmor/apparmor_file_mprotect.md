| Source (name [type]) | Field (index [id]) | Source Location                           | Label at Source             |
|----------------------|--------------------|-------------------------------------------|-----------------------------|
| vma                  |                    | security/apparmor/lsm.c:497               | object, dynamic, input      |
| prot                 |                    | security/apparmor/lsm.c:497               | operation, dynamic, input   |
| 19 [OP_FMPROT]       |                    | security/apparmor/lsm.c:500               | operation, static, mediator |
| current              |                    | security/apparmor/include/context.h:99    | subject, dynamic, external  |
| 8 [VM_SHARED]        |                    | security/apparmor/lsm.c:500               | all, static, external       |
| 0 [MAP_PRIVATE]      |                    | security/apparmor/lsm.c:483               | all, static, external       |
| 2 [PROT_WRITE]       |                    | security/apparmor/lsm.c:483               | all, static, external       |
| 4 [MAY_READ]         |                    | security/apparmor/lsm.c:478               | all, static, external       |
| 4 [PROT_EXEC]        |                    | security/apparmor/lsm.c:485               | all, static, external       |
| 2 [MAY_WRITE]        |                    | security/apparmor/lsm.c:484               | all, static, external       |
| 1 [PROT_READ]        |                    | security/apparmor/lsm.c:477               | all, static, external       |
| 0 [MS_NOUSER]        |                    | security/apparmor/include/apparmor.h:117  | all, static, external       |