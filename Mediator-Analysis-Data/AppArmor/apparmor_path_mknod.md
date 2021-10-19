| Source (name [type]) | Field (index [id]) | Source Location | Label at Source |
| -------------------- | ------------------ | --------------- | --------------- |
| dentry [dentry] | | /security/apparmor/lsm.c:276 | object, dynamic, input |
| path [path] | | /security/apparmor/lsm.c:276 | object, dynamic, input |
| 6 [OP_MKNOD] |  | /security/apparmor/include/audit.h:57 | operation, static, mediator |
| 16 [AA_MAY_CREATE] |  | /security/apparmor/include/file.h:29 | operation, static, mediator |
| mode |  | /security/apparmor/lsm.c:276 | operation, input |
| cond [path_cond] | 0 | /security/apparmor/lsm.c:251 | subject, dynamic, external |
| profile [aa_profile] |  | /security/apparmor/lsm.c:165 | subject, dynamic, external |
| path [path] |  | /security/apparmor/lsm.c:189 | object, dynamic, mediator |