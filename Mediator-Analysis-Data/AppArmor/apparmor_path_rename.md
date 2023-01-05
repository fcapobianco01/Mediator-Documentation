| Source (name [type])   | Field (index [id]) | Source Location                          | Label at Source             |
|------------------------|--------------------|------------------------------------------|-----------------------------|
| old_dir                |                    | security/apparmor/lsm.c:317              | object, dynamic, input      |
| new_dir                |                    | security/apparmor/lsm.c:317              | object, dynamic, input      |
| old_dentry             |                    | security/apparmor/lsm.c:317              | object, dynamic, input      |
| new_dentry             |                    | security/apparmor/lsm.c:317              | object, dynamic, input      |
| current                |                    | security/apparmor/include/context.h:99   | subject, dynamic, external  |
| 10 [OP_RENAME_SRC]     |                    | security/apparmor/lsm.c:334              | operation, static, mediator |
| 11 [OP_RENAME_DEST]    |                    | security/apparmor/lsm.c:339              | operation, static, mediator |
| 64 [AA_MAY_META_WRITE] |                    | security/apparmor/lsm.c:336              | operation, static, mediator |
| 32 [AA_MAY_META_READ]  |                    | security/apparmor/lsm.c:335              | operation, static, mediator |
| 64 [AA_MAY_DELETE]     |                    | security/apparmor/lsm.c:336              | operation, static, mediator |
| 4 [MAY_READ]           |                    | security/apparmor/lsm.c:335              | all, static, external       |
| 2 [MAY_WRITE]          |                    | security/apparmor/lsm.c:335              | all, static, external       |
| 64 [AA_MAY_META_WRITE] |                    | security/apparmor/lsm.c:340              | operation, static, mediator |
| 16 [AA_MAY_CREATE]     |                    | security/apparmor/lsm.c:335              | operation, static, mediator |
| 2 [MAY_WRITE]          |                    | security/apparmor/lsm.c:340              | all, static, external       |
| 2 [MAY_WRITE]          |                    | security/apparmor/lsm.c:291              | all, static, external       |
| 0 [MS_NOUSER]          |                    | security/apparmor/include/apparmor.h:117 | all, static, external       |
| 0 [_THIS_IP_]          |                    | include/linux/rcupdate.h:418             | all, static, external       |
| 1 [_THIS_IP_]          |                    | include/linux/rcupdate.h:423             | all, static, external       |