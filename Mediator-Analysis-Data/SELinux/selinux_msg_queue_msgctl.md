| Source (name [type]) | Field (index [id]) | Source Location               | Label at Source             |
| -------------------- | ------------------ | ----------------------------- | --------------------------- |
| current              |                    | security/selinux/hooks.c:5204 | subject, dynamic, external  |
| current              |                    | security/selinux/hooks.c:218  | subject, dynamic, external  |
| msq                  |                    | security/selinux/hooks.c:5195 | object, dynamic, input      |
| cmd                  |                    | security/selinux/hooks.c:5195 | operation, dynamic, input   |
| 1 [SYSTEM__IPC_INFO] |                    | security/selinux/hooks.c:5204 | operation, static, mediator |
| 4 [MSGQ__GETATTR]    |                    | security/selinux/hooks.c:5207 | operation, static, mediator |
| 64 [MSGQ__ASSOCIATE] |                    | security/selinux/hooks.c:5207 | operation, static, mediator |
| 8 [MSGQ__SETATTR]    |                    | security/selinux/hooks.c:5210 | operation, static, mediator |
| 2 [MSGQ__DESTROY]    |                    | security/selinux/hooks.c:5213 | operation, static, mediator |
| 0 [_THIS_IP_]        |                    | include/linux/rcupdate.h:418  | all, static, external       |
| 1 [_THIS_IP_]        |                    | include/linux/rcupdate.h:423  | all, static, external       |
| 3 [IPC_INFO]         |                    | security/selinux/hooks.c:5435 | all, static, external       |
| 12 [MSG_INFO]        |                    | security/selinux/hooks.c:5202 | all, static, external       |
| 0 [IPC_RMID]         |                    | security/selinux/hooks.c:5212 | all, static, external       |
| 1 [IPC_SET]          |                    | security/selinux/hooks.c:5209 | all, static, external       |
| 11 [MSG_STAT]        |                    | security/selinux/hooks.c:5206 | all, static, external       |
| 2 [IPC_STAT]         |                    | security/selinux/hooks.c:5205 | all, static, external       |
