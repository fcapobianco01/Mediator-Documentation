| Source (name [type])  | Field (index [id]) | Source Location               | Label at Source             |
| --------------------- | ------------------ | ----------------------------- | --------------------------- |
| fown                  |                    | security/selinux/hooks.c:3390 | subject, dynamic, input     |
| tsk                   |                    | security/selinux/hooks.c:3390 | object, dynamic, input      |
| signum                |                    | security/selinux/hooks.c:3390 | operation, dynamic, input   |
| 4 [PROCESS__SIGCHLD]  |                    | security/selinux/hooks.c:1479 | operation, static, mediator |
| 8 [PROCESS__SIGKILL]  |                    | security/selinux/hooks.c:1483 | operation, static, mediator |
| 16 [PROCESS__SIGSTOP] |                    | security/selinux/hooks.c:1487 | operation, static, mediator |
| 64 [PROCESS__SIGNAL]  |                    | security/selinux/hooks.c:1491 | operation, static, mediator |
| 29 [SIGIO]            |                    | security/selinux/hooks.c:3404 | all, static, external       |
| 0 [_THIS_IP_]         |                    | include/linux/rcupdate.h:418  | all, static, external       |
| 1 [_THIS_IP_]         |                    | include/linux/rcupdate.h:423  | all, static, external       |
| 9 [SIGKILL]           |                    | security/selinux/hooks.c:1481 | all, static, external       |
| 19 [SIGSTOP]          |                    | security/selinux/hooks.c:1485 | all, static, external       |
| 17 [SIGCHLD]          |                    | security/selinux/hooks.c:1477 | all, static, external       |




