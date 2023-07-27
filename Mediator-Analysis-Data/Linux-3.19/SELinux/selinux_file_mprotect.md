| Source (name [type])          | Field (index [id]) | Source Location                 | Label at Source             |
|-------------------------------|--------------------|---------------------------------|-----------------------------|
| current                       |                    | security/selinux/hooks.c:3303   | subject, dynamic, external  |
| current                       |                    | security/selinux/hooks.c:3317   | subject, dynamic, external  |
| vma                           |                    | security/selinux/hooks.c:3299   | object, dynamic, input      |
| 524288 [FILE__EXECMOD]        |                    | security/selinux/hooks.c:3339   | operation, static, mediator |
| 67108864 [PROCESS__EXECSTACK] |                    | security/selinux/hooks.c:3339   | operation, static, mediator |
| 134217728 [PROCESS__EXECHEAP] |                    | security/selinux/hooks.c:3339   | operation, static, mediator |
| 1 [FD__USE]                   |                    | security/selinux/hooks.c:1686   | operation, static, mediator |
| 2 [PROT_WRITE]                |                    | security/selinux/hooks.c:3242   | all, static, external       |
| 2 [PROT_WRITE]                |                    | security/selinux/hooks.c:3258   | all, static, external       |
| 4 [PROT_EXEC]                 |                    | security/selinux/hooks.c:3242   | all, static, external       |
| 4 [PROT_EXEC]                 |                    | security/selinux/hooks.c:3261   | all, static, external       |
| 0 [_THIS_IP_]                 |                    | include/linux/rcupdate.h:418    | all, static, external       |
| 1 [_THIS_IP_]                 |                    | include/linux/rcupdate.h:423    | all, static, external       |
| 4 [PROT_EXEC]                 |                    | security/selinux/hooks.c:3309   | all, static, external       |
| 4 [VM_EXEC]                   |                    | security/selinux/hooks.c:3309   | all, static, external       |
| 0 [VM_SHARED]                 |                    | security/selinux/hooks.c:3332   | all, static, external       |
