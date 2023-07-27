| Source (name [type])  | Field (index [id])  | Source Location               | Label at Source             |
|-----------------------|---------------------|-------------------------------|-----------------------------|
| current               |                     | security/selinux/hooks.c:4226 | subject, dynamic, external  |
| sock                  |                     | security/selinux/hooks.c:4224 | object, dynamic, input      |
| 16 [SOCKET__GETATTR]  |                     | security/selinux/hooks.c:4226 | operation, static, mediator |
| 1 [SECINITSID_KERNEL] |                     | security/selinux/hooks.c:3969 | all, static, mediator       |
| 1 [_THIS_IP_]         |                     | include/linux/rcupdate.h:418  | all, static, external       |
| 0 [_THIS_IP_]         |                     | include/linux/rcupdate.h:423  | all, static, external       |