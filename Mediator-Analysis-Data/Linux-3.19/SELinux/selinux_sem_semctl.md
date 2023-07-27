| Source (name [type]) | Field (index [id]) | Source Location                  | Label at Source             |
|----------------------|--------------------|----------------------------------|-----------------------------|
| current              |                    | security/selinux/hooks.c:5438    | subject, dynamic, external  |
| current              |                    | security/selinux/hooks.c:218     | subject, dynamic, external  |
| sma                  |                    | security/selinux/hooks.c:5429    | object, dynamic, input      |
| cmd                  |                    | security/selinux/hooks.c:5429    | operation, dynamic, input   |
| 1 [SYSTEM__IPC_INFO] |                    | security/selinux/hooks.c:5438    | operation, static, mediator |
| 4 [SEM__GETATTR]     |                    | security/selinux/hooks.c:5476    | operation, static, mediator |
| 16 [SEM__READ]       |                    | security/selinux/hooks.c:5476    | operation, static, mediator |
| 32 [SEM__WRITE]      |                    | security/selinux/hooks.c:5478    | operation, static, mediator |
| 2 [SEM__DESTROY]     |                    | security/selinux/hooks.c:5478    | operation, static, mediator |
| 8 [SEM__SETATTR]     |                    | security/selinux/hooks.c:5478    | operation, static, mediator |
| 4 [SEM__GETATTR]     |                    | security/selinux/hooks.c:5478    | operation, static, mediator |
| 64 [SEM__ASSOCIATE]  |                    | security/selinux/hooks.c:5478    | operation, static, mediator |
| 0 [_THIS_IP_]        |                    | include/linux/rcupdate.h:418     | all, static, external       |
| 1 [_THIS_IP_]        |                    | include/linux/rcupdate.h:423     | all, static, external       |
| 3 [IPC_INFO]         |                    | security/selinux/hooks.c:5435    | all, static, external       |
| 17 [SETALL]          |                    | security/selinux/hooks.c:5449    | all, static, external       |
| 0 [IPC_RMID]         |                    | security/selinux/hooks.c:5452    | all, static, external       |
| 18 [SEM_STAT]        |                    | security/selinux/hooks.c:5459    | all, static, external       |
| 14 [GETNCNT]         |                    | security/selinux/hooks.c:5440    | all, static, external       |
| 15 [GETZCNT]         |                    | security/selinux/hooks.c:5441    | all, static, external       |
| 1 [IPC_SET]          |                    | security/selinux/hooks.c:5455    | all, static, external       |
| 16 [SETVAL]          |                    | security/selinux/hooks.c:5448    | all, static, external       |
| 12 [GETALL]          |                    | security/selinux/hooks.c:5445    | all, static, external       |
| 13 [GETVAL]          |                    | security/selinux/hooks.c:5444    | all, static, external       |
| 11 [GETPID]          |                    | security/selinux/hooks.c:5439    | all, static, external       |
| 2 [IPC_STAT]         |                    | security/selinux/hooks.c:5458    | all, static, external       |
| 19 [SEM_INFO]        |                    | security/selinux/hooks.c:5436    | all, static, external       |