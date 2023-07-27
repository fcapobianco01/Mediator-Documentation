| Source (name [type]) | Field (index [id]) | Source Location                           | Label at Source             |
|----------------------|--------------------|-------------------------------------------|-----------------------------|
| file                 |                    | security/apparmor/lsm.c:376               | object, dynamic, input      |
| cred                 |                    | security/apparmor/lsm.c:376               | subject, dynamic, input     |
| 15 [OP_OPEN]         |                    | security/apparmor/lsm.c:400               | operation, static, mediator |
| 2048 [AA_EXEC_MMAP]  |                    | security/apparmor/lsm.c:391               | operation, static, mediator |
| current              |                    | security/apparmor/lsm.c:390               | subject, dynamic, external  |
| 4 [MAY_READ]         |                    | security/apparmor/include/file.h:203      | all, static, external       |
| 64 [O_CREAT]         |                    | security/apparmor/include/file.h:210      | all, static, external       |
| 1024 [O_APPEND]      |                    | security/apparmor/include/file.h:205      | all, static, external       |
| 2 [FMODE_WRITE]      |                    | security/apparmor/include/file.h:200      | all, static, external       |
| 1 [FMODE_READ]       |                    | security/apparmor/include/file.h:202      | all, static, external       |
| 8 [MAY_APPEND]       |                    | security/apparmor/include/file.h:206      | all, static, external       |
| 512 [O_TRUNC]        |                    | security/apparmor/include/file.h:208      | all, static, external       |
| 2 [MAY_WRITE]        |                    | security/apparmor/include/file.h:201      | all, static, external       |
| 2 [MAY_WRITE]        |                    | security/apparmor/include/file.h:205      | all, static, external       |
| 2 [MAY_WRITE]        |                    | security/apparmor/include/file.h:206      | all, static, external       |
| 2 [MAY_WRITE]        |                    | security/apparmor/include/file.h:209      | all, static, external       |
| 4 [MAY_READ]         |                    | security/apparmor/lsm.c:391               | all, static, external       |
| 1 [MAY_EXEC]         |                    | security/apparmor/lsm.c:391               | all, static, external       |
| 0 [MS_NOUSER]        |                    | security/apparmor/include/apparmor.h:117  | all, static, external       |

