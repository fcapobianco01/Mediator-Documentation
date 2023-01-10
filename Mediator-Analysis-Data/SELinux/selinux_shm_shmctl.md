| Source (name [type]) | Field (index [id]) | Source Location                 | Label at Source             |
|----------------------|--------------------|---------------------------------|-----------------------------|
| current              |                    | security/selinux/hooks.c:5346   | subject, dynamic, external  |
| current              |                    | security/selinux/hooks.c:218    | subject, dynamic, external  |
| shp                  |                    | security/selinux/hooks.c:5337   | object, dynamic, input      |
| cmd                  |                    | security/selinux/hooks.c:5337   | operation, dynamic, input   |
| 1 [SYSTEM__IPC_INFO] |                    | security/selinux/hooks.c:5438   | operation, static, mediator |
| 4 [SHM__GETATTR]     |                    | security/selinux/hooks.c:5349   | operation, static, mediator |
| 64 [SHM__ASSOCIATE]  |                    | security/selinux/hooks.c:5349   | operation, static, mediator |
| 8 [SHM__SETATTR]     |                    | security/selinux/hooks.c:5352   | operation, static, mediator |
| 512 [SHM__LOCK]      |                    | security/selinux/hooks.c:5356   | operation, static, mediator |
| 2 [SHM__DESTROY]     |                    | security/selinux/hooks.c:5359   | operation, static, mediator |
| 0 [_THIS_IP_]        |                    | include/linux/rcupdate.h:418    | all, static, external       |
| 1 [_THIS_IP_]        |                    | include/linux/rcupdate.h:423    | all, static, external       |
| 3 [IPC_INFO]         |                    | security/selinux/hooks.c:5343   | all, static, external       |
| 12 [SHM_UNLOCK]      |                    | security/selinux/hooks.c:5355   | all, static, external       |
| 0 [IPC_RMID]         |                    | security/selinux/hooks.c:5358   | all, static, external       |
| 13 [SHM_STAT]        |                    | security/selinux/hooks.c:5348   | all, static, external       |
| 11 [SHM_LOCK]        |                    | security/selinux/hooks.c:5354   | all, static, external       |
| 1 [IPC_SET]          |                    | security/selinux/hooks.c:5351   | all, static, external       |
| 14 [SHM_INFO]        |                    | security/selinux/hooks.c:5344   | all, static, external       |
| 2 [IPC_STAT]         |                    | security/selinux/hooks.c:5347   | all, static, external       |